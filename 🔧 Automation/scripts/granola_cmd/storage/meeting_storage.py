"""
Meeting storage module for Granola automation.

Stores meetings as markdown files with YAML frontmatter.
Filename format: DD-MM-YY-title.md
"""

import json
import logging
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any

logger = logging.getLogger(__name__)


@dataclass
class MeetingData:
    """Meeting data from Granola."""

    meeting_id: str
    title: str
    date: datetime
    duration_minutes: int
    participants: list[str]
    transcript: str | None = None
    notes: str | None = None
    summary: str | None = None
    granola_summary: str | None = None
    documents: list[dict[str, Any]] | None = None


class MeetingStorage:
    """Stores meetings as markdown files."""

    def __init__(self, output_path: str):
        """
        Initialize storage.

        Args:
            output_path: Directory path where meeting files will be saved
        """
        self.output_path = Path(output_path).expanduser()
        self.output_path.mkdir(parents=True, exist_ok=True)
        logger.info(f"MeetingStorage initialized with output: {self.output_path}")

    def save_meeting(self, meeting: MeetingData) -> str:
        """
        Save a single meeting as markdown.

        Args:
            meeting: MeetingData object with all meeting information

        Returns:
            Path to the saved file
        """
        filename = self._generate_filename(meeting)
        file_path = self.output_path / filename

        markdown = self._format_as_markdown(meeting)

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(markdown)

        logger.info(f"Saved meeting: {file_path}")
        return str(file_path)

    def _generate_filename(self, meeting: MeetingData) -> str:
        """
        Generate filename from meeting metadata.

        Format: DD-MM-YY-title.md (e.g., 14-01-26-product-strategy-review.md)

        Args:
            meeting: MeetingData object

        Returns:
            Filename string
        """
        # Format date as DD-MM-YY
        day = meeting.date.strftime("%d")
        month = meeting.date.strftime("%m")
        year_short = meeting.date.strftime("%y")  # 2-digit year

        # Sanitize title for filename
        safe_title = meeting.title.lower()[:50]
        safe_title = "".join(c if c.isalnum() or c in (" ", "-", "_") else "-" for c in safe_title)
        safe_title = safe_title.replace(" ", "-")
        # Remove consecutive hyphens
        while "--" in safe_title:
            safe_title = safe_title.replace("--", "-")
        # Remove leading/trailing hyphens
        safe_title = safe_title.strip("-")

        return f"{day}-{month}-{year_short}-{safe_title}.md"

    def _format_as_markdown(self, meeting: MeetingData) -> str:
        """
        Format meeting as markdown with frontmatter.

        Args:
            meeting: MeetingData object

        Returns:
            Complete markdown document as string
        """
        lines = [
            "---",
            f'title: "{self._escape_yaml_string(meeting.title)}"',
            f'date: "{meeting.date.strftime("%Y-%m-%d")}"',
            f'meeting_id: "{meeting.meeting_id}"',
            f"duration: {meeting.duration_minutes}",
            f"participants: {json.dumps(meeting.participants)}",
            "---",
            "",
            f"# {meeting.title}",
            "",
            f"**Date:** {meeting.date.strftime('%B %d, %Y')}",
            f"**Duration:** {meeting.duration_minutes} minutes",
            f"**Participants:** {', '.join(meeting.participants) if meeting.participants else 'N/A'}",
            "",
            "---",
            "",
        ]

        # Granola AI Summary section (prioritize this over other summary/notes)
        if meeting.granola_summary:
            lines.extend(["## Summary", "", meeting.granola_summary, "", "---", ""])
        elif meeting.summary or meeting.notes:
            lines.extend(["## Summary", "", meeting.summary or meeting.notes, "", "---", ""])

        # Transcript section
        if meeting.transcript:
            lines.extend(["## Transcript", "", meeting.transcript, "", "---", ""])

        # Documents section
        if meeting.documents:
            lines.extend(["## Documents", ""])
            for doc in meeting.documents:
                doc_title = doc.get("title", "Untitled")
                doc_content = doc.get("content", "")
                lines.extend([f"### {doc_title}", "", doc_content, ""])

        return "\n".join(lines)

    def _escape_yaml_string(self, s: str) -> str:
        """
        Escape special characters for YAML strings.

        Args:
            s: String to escape

        Returns:
            Escaped string safe for YAML
        """
        # Escape quotes and backslashes
        return s.replace("\\", "\\\\").replace('"', '\\"')
