"""Collects Granola meeting notes for the /today workflow."""

import logging
import os
import re
import sys
import yaml
from datetime import date, datetime, timedelta
from pathlib import Path
from typing import Any, Dict, List, Optional

# Add parent directory to path for shared imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from .base_collector import BaseCollector
from shared.path_utils import get_project_root

logger = logging.getLogger(__name__)


class GranolaCollector(BaseCollector):
    """
    Collects Granola meeting notes for /today analysis.

    Workflow:
    1. Optionally runs granola extraction (reuses granola_cmd.GranolaCollector)
    2. Reads yesterday's meeting markdown files
    3. Parses YAML frontmatter and extracts sections
    4. Returns structured data for analysis
    """

    def __init__(
        self,
        granola_path: Optional[str] = None,
        auto_fetch: bool = True,
        days_back: int = 1
    ):
        """
        Initialize collector.

        Args:
            granola_path: Path to granola meeting notes folder
            auto_fetch: Whether to run granola extraction before reading
            days_back: How many days back to look for meetings (default: 1 = yesterday)
        """
        # Default path: Product-Management/granola in workspace
        if granola_path is None:
            workspace_root = get_project_root()
            granola_path = workspace_root / "Product-Management" / "granola"

        self.granola_path = Path(granola_path)
        self.auto_fetch = auto_fetch
        self.days_back = days_back

        logger.info(
            f"GranolaCollector initialized: path={self.granola_path}, "
            f"auto_fetch={auto_fetch}, days_back={days_back}"
        )

    async def collect(self) -> Dict[str, Any]:
        """
        Collect meeting notes from granola folder.

        Returns:
            Dict with "meetings", "errors", and "date" keys
        """
        result = {
            "meetings": [],
            "errors": [],
            "date": self._get_target_date().strftime("%Y-%m-%d")
        }

        # Step 1: Run granola extraction if auto_fetch is enabled
        if self.auto_fetch:
            logger.info("Running granola extraction...")
            await self._run_granola_extraction()

        # Step 2: Read meeting files for target date
        if not self.granola_path.exists():
            result["errors"].append(f"Granola path not found: {self.granola_path}")
            logger.warning(f"Granola path not found: {self.granola_path}")
            return result

        target_date = self._get_target_date()
        meetings = self._read_meeting_files(target_date)

        if not meetings:
            logger.info(f"No meetings found for {target_date.strftime('%Y-%m-%d')}")
            result["errors"].append(f"No meetings found for {target_date.strftime('%Y-%m-%d')}")
            return result

        result["meetings"] = meetings
        logger.info(f"Collected {len(meetings)} meeting(s) from {target_date.strftime('%Y-%m-%d')}")

        return result

    async def _run_granola_extraction(self):
        """Run the granola extraction script as a subprocess."""
        try:
            import subprocess
            import sys

            # Path to granola command main.py
            granola_main = Path(__file__).parent.parent.parent / "granola_cmd" / "main.py"

            # Build command - run as module to avoid import issues
            cmd = [
                sys.executable,
                str(granola_main),
                "--target-date", "yesterday"
            ]

            logger.info(f"Running granola extraction: {' '.join(cmd)}")

            # Run the command and wait for completion
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=300  # 5 minute timeout
            )

            if result.returncode == 0:
                # Parse output to get count
                for line in result.stdout.split('\n'):
                    if 'Complete:' in line and 'meeting' in line:
                        logger.info(f"Granola extraction: {line.strip()}")
                        break
                else:
                    logger.info("Granola extraction completed")
            else:
                logger.warning(f"Granola extraction failed: {result.stderr}")

        except subprocess.TimeoutExpired:
            logger.warning("Granola extraction timed out after 5 minutes")
        except FileNotFoundError:
            logger.warning(f"Granola command not found at: {granola_main}")
        except Exception as e:
            logger.warning(f"Granola extraction failed: {e}")

    def _get_target_date(self) -> date:
        """Get the target date for collection."""
        return date.today() - timedelta(days=self.days_back)

    def _read_meeting_files(self, target_date: date) -> List[Dict[str, Any]]:
        """
        Read meeting markdown files for target date.

        Args:
            target_date: Date to filter meetings by

        Returns:
            List of meeting dicts with title, date, transcript, notes, etc.
        """
        meetings = []

        # Granola file format: DD-MM-YY-title.md
        date_pattern = target_date.strftime("%d-%m-%y")

        try:
            for file_path in self.granola_path.glob(f"{date_pattern}-*.md"):
                meeting = self._parse_meeting_file(file_path)
                if meeting:
                    meetings.append(meeting)

        except Exception as e:
            logger.error(f"Error reading meeting files: {e}")

        return meetings

    def _parse_meeting_file(self, file_path: Path) -> Optional[Dict[str, Any]]:
        """
        Parse a single meeting markdown file.

        Args:
            file_path: Path to meeting markdown file

        Returns:
            Meeting dict or None if parsing failed
        """
        try:
            with open(file_path, "r") as f:
                content = f.read()

            # Split YAML frontmatter from content
            if content.startswith("---"):
                _, frontmatter, body = content.split("---", 2)
                metadata = yaml.safe_load(frontmatter)
            else:
                metadata = {}
                body = content

            # Extract sections from body
            transcript = self._extract_section(body, "## Transcript")
            notes = self._extract_section(body, "## Meeting Notes")
            summary = self._extract_section(body, "## Summary")

            return {
                "file_path": str(file_path),
                "title": metadata.get("title", file_path.stem),
                "date": metadata.get("date"),
                "meeting_id": metadata.get("meeting_id"),
                "duration": metadata.get("duration", 0),
                "participants": metadata.get("participants", []),
                "transcript": transcript or "",
                "notes": notes or "",
                "summary": summary or "",
                "full_content": body
            }

        except Exception as e:
            logger.warning(f"Failed to parse meeting file {file_path}: {e}")
            return None

    def _extract_section(self, content: str, section_header: str) -> Optional[str]:
        """
        Extract a section from markdown content.

        Args:
            content: Full markdown content
            section_header: Section heading (e.g., "## Transcript")

        Returns:
            Section content or None if not found
        """
        # Find the section - stop only at next section header (##), not separators (---)
        # Use ##[^#] to ensure we only match level-2 headings, not level-3 (###)
        # This allows sections with subsections (like ### Next Steps within ## Summary)
        match = re.search(
            rf"{re.escape(section_header)}\s*\n+(.*?)(?=\n##[^#]|\Z)",
            content,
            re.DOTALL
        )

        if match:
            return match.group(1).strip()

        return None
