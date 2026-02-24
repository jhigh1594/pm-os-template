#!/usr/bin/env python3
"""Fetch multiple Granola meetings and save as markdown files."""

import json
import logging
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

# Add parent directory to path for imports
import sys
sys.path.insert(0, str(Path(__file__).parent))

from mcp_client import GranolaCacheReader

logging.basicConfig(level=logging.INFO, format="%(message)s")
logger = logging.getLogger(__name__)

# Meeting IDs to fetch
MEETING_IDS = [
    "15bd8f2a-996c-47ac-bb8a-24549d7b2cf6",
    "e5724312-72a3-45e2-a83b-6f8f4b556954",
    "fdd9b036-375d-48a0-9418-7ad91f45e6a1",
    "3c717134-b37c-414a-9b06-fbf078d6db07",
    "763b880b-414f-40d2-a638-e03617d5f568",
    "6338ec3d-e338-496d-bc2b-c9b9571817de",
    "25ee734d-dc7e-4b6b-b344-0b5168cc6662",
    "087d3e03-7d8c-4c95-8652-87bdf3243211",
    "a31afb7b-d2f7-4ac7-bf8e-7e7d3fab3214",
    "b27c3df7-6246-4684-9e45-4a2882c58d2a",
    "ef592925-dcad-4f14-97b7-831c4209162f",
    "134f962e-8994-450b-8dc2-e1139c8cf912",
    "3532a55f-d0c5-4283-864f-f847e3967c28",
    "c27cdc82-10e5-458f-b268-eab21c49192a",
    "e858f8b0-7440-4cbd-a302-2e988f23fd9a",
    "138096ca-7f62-4ba5-b28e-ddb2325a1ea8",
    "63a241fc-cd07-4e75-9375-0e170f6ccbfd",
]

# Output directory
OUTPUT_DIR = Path("{{WORKSPACE_PATH}}/Company/meeting-notes/granola")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def slugify(title: str) -> str:
    """Convert title to URL-safe slug."""
    # Remove special characters, replace spaces with hyphens
    slug = title.lower()
    slug = "".join(c if c.isalnum() or c in " -" else " " for c in slug)
    slug = slug.strip()
    slug = "-".join(slug.split())
    return slug


def parse_date(date_str: str) -> datetime:
    """Parse ISO date string to datetime."""
    if not date_str:
        return datetime.now()
    # Handle various ISO formats
    date_str = date_str.replace("Z", "+00:00")
    try:
        return datetime.fromisoformat(date_str)
    except ValueError:
        # Try parsing just the date part
        if "T" in date_str:
            date_part = date_str.split("T")[0]
            return datetime.fromisoformat(date_part)
        return datetime.now()


def format_duration(seconds: int) -> str:
    """Format duration in seconds to human-readable string."""
    if not seconds:
        return "Unknown"
    minutes = seconds // 60
    hours = minutes // 60
    mins = minutes % 60
    if hours > 0:
        return f"{hours}h {mins}m"
    return f"{mins}m"


def save_meeting_as_markdown(reader: GranolaCacheReader, meeting_id: str) -> bool:
    """Fetch and save a single meeting as markdown."""
    try:
        # Get meeting details
        details = reader.get_meeting_details(meeting_id)
        title = details.get("title", "Untitled")
        created_at = details.get("created_at", "")
        duration = details.get("duration", 0)
        participants = details.get("participants", [])

        # Parse date for filename
        meeting_date = parse_date(created_at)
        year_short = meeting_date.strftime("%y")
        month = meeting_date.strftime("%m")
        day = meeting_date.strftime("%d")

        # Create filename
        title_slug = slugify(title)
        filename = f"{year_short}-{month}-{day}-{title_slug}.md"
        filepath = OUTPUT_DIR / filename

        # Get Granola AI summary
        granola_summary = reader.get_granola_summary(meeting_id)

        # Get transcript
        transcript = reader.get_meeting_transcript(meeting_id)

        # Get documents
        documents = reader.get_meeting_documents(meeting_id)

        # Build markdown content
        lines = []

        # YAML frontmatter
        lines.append("---")
        lines.append(f"title: {title}")
        lines.append(f"date: {created_at}")
        lines.append(f"meeting_id: {meeting_id}")
        lines.append(f"duration: {format_duration(duration)}")
        if participants:
            lines.append(f"participants: {json.dumps(participants)}")
        lines.append("---")
        lines.append("")

        # Granola chat link
        lines.append("")
        lines.append(f"[View in Granola](https://granola.ai/chat/{meeting_id})")
        lines.append("")

        # Granola AI Summary
        if granola_summary:
            lines.append("")
            lines.append("## Granola AI Summary")
            lines.append("")
            lines.append(granola_summary)
            lines.append("")

        # Documents (overview, notes, summary)
        if documents:
            for doc in documents:
                doc_title = doc.get("title", "")
                doc_content = doc.get("content", "")
                if doc_title and doc_content:
                    lines.append("")
                    lines.append(f"## {doc_title}")
                    lines.append("")
                    lines.append(doc_content)
                    lines.append("")

        # Transcript
        if transcript:
            lines.append("")
            lines.append("## Transcript")
            lines.append("")
            lines.append(transcript)
            lines.append("")

        # Write file
        content = "\n".join(lines)
        filepath.write_text(content, encoding="utf-8")

        logger.info(f"Saved: {filename}")
        return True

    except Exception as e:
        logger.error(f"Failed to fetch meeting {meeting_id}: {e}")
        return False


def main():
    """Fetch all meetings and save as markdown."""
    logger.info(f"Output directory: {OUTPUT_DIR}")
    logger.info(f"Fetching {len(MEETING_IDS)} meetings...")

    # Initialize cache reader
    reader = GranolaCacheReader()
    reader.load_cache()

    # Fetch and save each meeting
    success_count = 0
    for meeting_id in MEETING_IDS:
        if save_meeting_as_markdown(reader, meeting_id):
            success_count += 1

    logger.info("")
    logger.info(f"Successfully saved {success_count}/{len(MEETING_IDS)} meetings")


if __name__ == "__main__":
    main()
