"""AnalysisAgent applies PM Operating Principles to categorize and score priorities."""

import json
import logging
import re
from typing import Dict, Any, Optional

import google.generativeai as genai
from google.generativeai.types import GenerationConfig

from ..prompts.analysis_prompt import get_analysis_prompt, get_analysis_system_instruction
from ..models.collected_data import CollectedData
from ..models.analyzed_data import AnalyzedData

logger = logging.getLogger(__name__)


class AnalysisAgent:
    """
    Analyzes collected data using PM Operating Principles.

    Process:
    1. Build prompt with collected data + PM principles
    2. Call Gemini AI for analysis
    3. Parse response into structured AnalyzedData
    4. Return categorized priorities, blocked items, prep gaps, warnings
    """

    def __init__(
        self,
        api_key: str,
        model: str = "gemini-2.0-flash-exp",
        temperature: float = 0.3
    ):
        """
        Initialize AnalysisAgent.

        Args:
            api_key: Google Generative AI API key
            model: Gemini model to use (default: gemini-2.0-flash-exp)
            temperature: AI temperature (0.0-1.0, lower for more deterministic)
        """
        self.api_key = api_key
        self.model_name = model
        self.temperature = temperature
        logger.info(f"AnalysisAgent initialized with model {model}")

        # Configure GenAI
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel(
            model_name=model,
            system_instruction=get_analysis_system_instruction()
        )

    async def analyze(self, collected_data: CollectedData) -> AnalyzedData:
        """
        Analyze collected data with PM Operating Principles.

        Args:
            collected_data: Raw data from collectors

        Returns:
            AnalyzedData with categorized priorities and insights
        """
        logger.info("Starting analysis with PM Operating Principles")

        try:
            # Build prompt
            prompt = get_analysis_prompt(collected_data)

            # Generate analysis
            response = await self._generate_analysis(prompt)

            # Parse response
            analyzed_data = self._parse_response(response)

            logger.info(f"Analysis complete: {len(analyzed_data['priorities'])} priorities, "
                       f"{len(analyzed_data['warnings'])} warnings")

            return analyzed_data

        except Exception as e:
            logger.error(f"Analysis failed: {e}")
            # Return empty analysis on failure
            return self._empty_analysis()

    async def _generate_analysis(self, prompt: str) -> str:
        """
        Generate analysis using Gemini AI.

        Args:
            prompt: Full analysis prompt

        Returns:
            Raw response text from Gemini
        """
        logger.debug("Sending prompt to Gemini AI")

        try:
            response = self.model.generate_content(
                prompt,
                generation_config=GenerationConfig(
                    temperature=self.temperature,
                    max_output_tokens=8192,  # Increased for large responses
                    response_mime_type="application/json"
                )
            )
            return response.text

        except Exception as e:
            logger.error(f"Gemini generation failed: {e}")
            raise

    def _parse_response(self, response: str) -> AnalyzedData:
        """
        Parse Gemini response into AnalyzedData.

        Args:
            response: Raw JSON response from Gemini

        Returns:
            Parsed AnalyzedData dictionary
        """
        logger.debug("Parsing analysis response")

        try:
            # Try direct parse first (with response_mime_type, should be clean)
            try:
                parsed = json.loads(response)
            except json.JSONDecodeError as e:
                logger.debug(f"Direct parse failed: {e}, attempting repair")
                # Extract JSON from response (may have markdown code blocks or trailing text)
                response = self._extract_valid_json(response)
                # Repair common JSON issues
                response = self._repair_json(response)
                parsed = json.loads(response)

            # Validate structure
            required_keys = ["priorities", "blocked_items", "prep_gaps",
                           "strategic_alignment", "warnings", "time_distribution"]

            for key in required_keys:
                if key not in parsed:
                    logger.warning(f"Missing key in response: {key}")
                    parsed[key] = [] if key in ["priorities", "blocked_items",
                                               "prep_gaps", "warnings"] else {}

            logger.debug(f"_parse_response returning: {len(parsed.get('priorities', []))} priorities")
            return parsed

        except json.JSONDecodeError as e:
            logger.error(f"Failed to parse JSON response: {e}")
            logger.debug(f"Response length: {len(response)}, error at position: {e.pos}")

            # Show end of response for debugging
            if len(response) > 100:
                logger.debug(f"Response ends with: ...{response[-200:]}")

            # Try to find valid JSON by truncating at error position
            if hasattr(e, 'pos') and e.pos and e.pos < len(response):
                # Try parsing just the first valid portion
                truncated = response[:e.pos]
                # Find last complete object by finding matching brace
                last_brace = truncated.rfind('}')
                if last_brace > 0:
                    truncated = truncated[:last_brace + 1]
                    try:
                        parsed = json.loads(truncated)
                        logger.warning(f"Successfully parsed truncated JSON ({len(truncated)} chars)")
                        return parsed
                    except:
                        pass

            # Try adding missing closing braces
            response = self._fix_unclosed_braces(response)
            try:
                parsed = json.loads(response)
                logger.warning(f"Successfully parsed after fixing unclosed braces - {len(parsed.get('priorities', []))} priorities")
                return parsed
            except:
                pass

            logger.debug(f"Response starts with: {response[:200]}...")
            return self._empty_analysis()

    def _extract_valid_json(self, response: str) -> str:
        """
        Extract valid JSON by finding matching braces.

        Handles truncated or malformed responses by finding
        the longest valid JSON object.

        Args:
            response: Potentially malformed response string

        Returns:
            Extracted valid JSON string
        """
        response = response.strip()

        # Remove markdown code blocks if present
        if response.startswith('```json'):
            response = response[7:]  # Remove ```json
        if response.startswith('```'):
            response = response[3:]  # Remove ```
        if response.endswith('```'):
            response = response[:-3]  # Remove trailing ```
        response = response.strip()

        # Find the start of JSON object
        start_idx = response.find('{')
        if start_idx == -1:
            return response

        # Count braces to find matching end
        brace_count = 0
        in_string = False
        escape_next = False
        end_idx = start_idx

        for i in range(start_idx, len(response)):
            char = response[i]

            if escape_next:
                escape_next = False
                continue

            if char == '\\':
                escape_next = True
                continue

            if char == '"' and not escape_next:
                in_string = not in_string
                continue

            if not in_string:
                if char == '{':
                    brace_count += 1
                elif char == '}':
                    brace_count -= 1
                    if brace_count == 0:
                        # Found matching closing brace
                        end_idx = i + 1
                        break

        extracted = response[start_idx:end_idx]
        # If extraction returned empty, return original
        if not extracted.strip():
            return response
        return extracted

    def _fix_unclosed_braces(self, json_str: str) -> str:
        """
        Fix unclosed braces/brackets by counting and adding closing ones.

        Args:
            json_str: Potentially malformed JSON string

        Returns:
            JSON string with balanced braces
        """
        original_len = len(json_str)
        open_braces = json_str.count('{') - json_str.count('}')
        open_brackets = json_str.count('[') - json_str.count(']')

        logger.debug(f"Brace check: {open_braces} open braces, {open_brackets} open brackets")

        # Remove trailing content after last valid closing
        json_str = json_str.strip()
        last_close_idx = -1
        for i in range(len(json_str) - 1, -1, -1):
            if json_str[i] in '}]':
                last_close_idx = i
                break

        if last_close_idx >= 0:
            json_str = json_str[:last_close_idx + 1]
            logger.debug(f"Truncated to last closing brace at position {last_close_idx}")

        # Recalculate after truncation
        open_braces = json_str.count('{') - json_str.count('}')
        open_brackets = json_str.count('[') - json_str.count(']')

        # Add missing closing braces (brackets first, then braces)
        for _ in range(open_brackets):
            json_str += ']'
        for _ in range(open_braces):
            json_str += '}'

        logger.debug(f"Fixed JSON: {original_len} -> {len(json_str)} chars")
        return json_str

    def _repair_json(self, json_str: str) -> str:
        """
        Repair common JSON issues from LLM-generated responses.

        Fixes:
        - Trailing commas in arrays and objects
        - Missing commas between objects/arrays
        - Missing commas between array items
        - Unquoted property names

        Args:
            json_str: Potentially malformed JSON string

        Returns:
            Repaired JSON string
        """
        # Remove leading/trailing whitespace
        json_str = json_str.strip()

        # Fix trailing commas in objects/arrays (before } or ])
        json_str = re.sub(r',(\s*[}\]])', r'\1', json_str)

        # Fix missing commas between objects (when } is followed by ")
        # Look for } followed by whitespace then " but no comma
        json_str = re.sub(r'\}(\s*)"', '},\1"', json_str)

        # Fix missing commas between array items (when } or ] is followed by { or [)
        json_str = re.sub(r'\}(\s*)\{', '},\1{', json_str)
        json_str = re.sub(r'\](\s*)\{', '],\1{', json_str)
        json_str = re.sub(r'\}(\s*)\[', '},\1[', json_str)
        json_str = re.sub(r'\](\s*)\[', '],\1[', json_str)

        # Fix missing commas between arrays (when ] is followed by ")
        json_str = re.sub(r'\](\s*)"', '],\1"', json_str)

        # Fix unquoted property names (if any)
        # This pattern finds word: before a value and wraps it in quotes
        # Be careful not to quote values that follow colons
        json_str = re.sub(r'"\s*:\s*"([^"]+)"\s*:\s*', '": "\\1": ', json_str)

        return json_str

    def _empty_analysis(self) -> AnalyzedData:
        """Return empty analysis structure for graceful degradation."""
        return {
            "date": "",
            "priorities": [],
            "blocked_items": [],
            "prep_gaps": [],
            "strategic_alignment": {
                "total_items": 0,
                "high_alignment_count": 0,
                "high_alignment_percentage": 0.0,
                "avg_strategic_score": 0.0,
                "top_okrs_aligned": []
            },
            "warnings": [],
            "time_distribution": {
                "strategic_deep_work": 0.0,
                "meetings": 0.0,
                "reactive": 0.0,
                "prep_available": 0.0,
                "total_available_hours": 0.0
            }
        }
