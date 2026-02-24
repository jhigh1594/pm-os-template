"""SynthesisAgent generates daily plan from analyzed data."""

import json
import logging
import os
import re
from datetime import datetime, timedelta
from typing import Dict, Any, Optional

import google.generativeai as genai
from google.generativeai.types import GenerationConfig

from ..prompts.synthesis_prompt import get_synthesis_prompt, get_synthesis_system_instruction
from ..models.analyzed_data import AnalyzedData
from ..models.daily_plan import DailyPlan

logger = logging.getLogger(__name__)


class SynthesisAgent:
    """
    Synthesizes analyzed data into daily plan.

    Process:
    1. Build prompt with analyzed data + ruthless prioritization framework
    2. Call Gemini AI for synthesis
    3. Parse response into structured DailyPlan
    4. Return Top 3 priorities, 3-day view, insights, recommendations
    """

    def __init__(
        self,
        api_key: str,
        model: str = "gemini-2.0-flash-exp",
        temperature: float = 0.3
    ):
        """
        Initialize SynthesisAgent.

        Args:
            api_key: Google Generative AI API key
            model: Gemini model to use (default: gemini-2.0-flash-exp)
            temperature: AI temperature (0.0-1.0, lower for more deterministic)
        """
        self.api_key = api_key
        self.model_name = model
        self.temperature = temperature
        self.agileplace_domain = (os.getenv("AGILEPLACE_DOMAIN") or "https://planview.leankit.com").rstrip("/")
        logger.info(f"SynthesisAgent initialized with model {model}")

        # Configure GenAI
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel(
            model_name=model,
            system_instruction=get_synthesis_system_instruction()
        )

    async def synthesize(self, analyzed_data: AnalyzedData) -> DailyPlan:
        """
        Synthesize analyzed data into daily plan.

        Args:
            analyzed_data: Output from AnalysisAgent

        Returns:
            DailyPlan with Top 3 priorities, rolling view, insights
        """
        logger.info("Starting synthesis to daily plan")

        try:
            # Build prompt
            prompt = get_synthesis_prompt(analyzed_data)

            # Generate daily plan
            response = await self._generate_plan(prompt)

            # Parse response
            daily_plan = self._parse_response(response)

            logger.info(f"Synthesis complete: {len(daily_plan['top_priorities'])} priorities, "
                       f"{len(daily_plan['rolling_view'])} day rolling view")

            return daily_plan

        except Exception as e:
            logger.error(f"Synthesis failed: {e}")
            # Return empty plan on failure
            return self._empty_plan()

    async def _generate_plan(self, prompt: str) -> str:
        """
        Generate daily plan using Gemini AI.

        Args:
            prompt: Full synthesis prompt

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

    def _parse_response(self, response: str) -> DailyPlan:
        """
        Parse Gemini response into DailyPlan.

        Args:
            response: Raw JSON response from Gemini

        Returns:
            Parsed DailyPlan dictionary
        """
        logger.debug("Parsing synthesis response")

        try:
            # Try direct parse first (with response_mime_type, should be clean)
            try:
                parsed = json.loads(response)
            except json.JSONDecodeError:
                # Extract valid JSON from response
                response = self._extract_valid_json(response)
                # Repair common JSON issues
                response = self._repair_json(response)
                parsed = json.loads(response)

            # Add metadata
            parsed["date"] = datetime.now().strftime("%Y-%m-%d")
            parsed["generated_at"] = datetime.now().isoformat()

            # Validate structure
            if "top_priorities" not in parsed:
                parsed["top_priorities"] = []
            if "rolling_view" not in parsed:
                parsed["rolling_view"] = []
            if "insights_warnings" not in parsed:
                parsed["insights_warnings"] = []
            if "time_blocking_recommendations" not in parsed:
                parsed["time_blocking_recommendations"] = []
            if "data_sources_used" not in parsed:
                parsed["data_sources_used"] = []
            if "confidence_score" not in parsed:
                parsed["confidence_score"] = 0.5

            for priority in parsed.get("top_priorities", []):
                card_id = priority.get("card_id")
                if card_id and not priority.get("card_url"):
                    priority["card_url"] = f"{self.agileplace_domain}/card/{card_id}"

            # Validate top priorities count (ruthless: max 3)
            if len(parsed["top_priorities"]) > 3:
                logger.warning(f"AI returned {len(parsed['top_priorities'])} priorities, truncating to 3")
                parsed["top_priorities"] = parsed["top_priorities"][:3]

            return parsed

        except json.JSONDecodeError as e:
            logger.error(f"Failed to parse JSON response: {e}")
            logger.debug(f"Response was: {response[:500]}...")
            return self._empty_plan()

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

    def _repair_json(self, json_str: str) -> str:
        """
        Repair common JSON issues from LLM-generated responses.

        Fixes:
        - Trailing commas in arrays and objects
        - Missing commas between objects/arrays
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
        json_str = re.sub(r'\}(\s*)"', '},\1"', json_str)

        # Fix missing commas between arrays (when ] is followed by ")
        json_str = re.sub(r'\](\s*)"', '],\1"', json_str)

        # Fix unquoted property names (if any)
        json_str = re.sub(r'(\w+):', r'"\1":', json_str)

        return json_str

    def _empty_plan(self) -> DailyPlan:
        """Return empty plan structure for graceful degradation."""
        return {
            "date": datetime.now().strftime("%Y-%m-%d"),
            "generated_at": datetime.now().isoformat(),
            "top_priorities": [],
            "rolling_view": [],
            "insights_warnings": [
                {
                    "type": "SYSTEM_ERROR",
                    "severity": "HIGH",
                    "message": "Failed to generate daily plan - AI synthesis failed",
                    "actionable": "Please check logs and retry"
                }
            ],
            "time_blocking_recommendations": [],
            "data_sources_used": [],
            "confidence_score": 0.0
        }
