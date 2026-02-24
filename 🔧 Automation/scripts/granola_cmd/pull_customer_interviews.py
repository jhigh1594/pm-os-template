#!/usr/bin/env python3
"""
Pull customer interview meetings from Granola and save to Company/meeting-notes/granola.

Since Granola MCP doesn't support folder search, this script:
1. Searches for meetings with customer/interview keywords
2. Pulls full details and transcripts
3. Saves to markdown files in Company/meeting-notes/granola
"""

import json
import os
import sys
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent))

from mcp_client import GranolaCacheReader


def format_date(date_str: str) -> str:
    """Format date string for filename."""
    try:
        dt = datetime.fromisoformat(date_str.replace('Z', '+00:00'))
        return dt.strftime('%y-%m-%d')
    except:
        return datetime.now().strftime('%y-%m-%d')


def sanitize_filename(title: str) -> str:
    """Sanitize title for use in filename."""
    # Remove or replace invalid filename characters
    invalid_chars = '<>:"/\\|?*'
    for char in invalid_chars:
        title = title.replace(char, '-')
    # Limit length
    if len(title) > 100:
        title = title[:100]
    return title.strip()


def create_markdown_file(meeting: Dict[str, Any], output_dir: Path, cache_reader: GranolaCacheReader) -> Path:
    """Create markdown file for a meeting."""
    meeting_id = meeting['meeting_id']
    title = meeting.get('title', 'Untitled Meeting')
    date_str = meeting.get('created_at', '')
    
    # Format date for filename
    date_formatted = format_date(date_str)
    title_sanitized = sanitize_filename(title)
    filename = f"{date_formatted}-{title_sanitized}.md"
    filepath = output_dir / filename
    
    # Get full meeting details
    details = cache_reader.get_meeting_details(meeting_id)
    transcript = cache_reader.get_meeting_transcript(meeting_id)
    documents = cache_reader.get_meeting_documents(meeting_id)
    
    # Build markdown content
    lines = [
        "---",
        f"title: \"{title}\"",
        f"date: \"{date_str[:10] if len(date_str) >= 10 else ''}\"",
        f"meeting_id: \"{meeting_id}\"",
        f"duration: {details.get('duration', 0)}",
        f"participants: {json.dumps(details.get('participants', []))}",
        "---",
        "",
        f"# {title}",
        "",
        f"**Date:** {date_str}",
        f"**Duration:** {details.get('duration', 0)} minutes",
        f"**Participants:** {', '.join(details.get('participants', [])) if details.get('participants') else 'N/A'}",
        "",
        "---",
        "",
    ]
    
    # Add summary/overview if available
    if documents:
        for doc in documents:
            if doc.get('title') == 'Summary' and doc.get('content'):
                lines.extend([
                    "## Summary",
                    "",
                    doc['content'],
                    "",
                ])
                break
    
    # Add transcript if available
    if transcript:
        lines.extend([
            "---",
            "",
            "## Transcript",
            "",
            transcript,
            "",
        ])
    
    # Add Granola link
    lines.append(f"Chat with meeting transcript: https://notes.granola.ai/t/{meeting_id}")
    lines.append("")
    
    # Write file
    filepath.write_text('\n'.join(lines), encoding='utf-8')
    return filepath


def main():
    """Main function to pull customer interview meetings."""
    # Setup paths
    workspace_root = Path(__file__).parent.parent.parent.parent
    output_dir = workspace_root / "Company" / "meeting-notes" / "granola"
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Initialize cache reader
    cache_reader = GranolaCacheReader()
    
    # Search for customer-related meetings
    print("Searching for customer interview meetings...")
    customer_meetings = cache_reader.search_meetings("customer", limit=100)
    
    # Also search for interview-related
    interview_meetings = cache_reader.search_meetings("interview", limit=50)
    
    # Combine and deduplicate
    all_meetings = {}
    for meeting in customer_meetings + interview_meetings:
        meeting_id = meeting['meeting_id']
        if meeting_id not in all_meetings:
            all_meetings[meeting_id] = meeting
    
    # Filter for likely customer interviews (contain "customer" AND ("interview" OR "feedback"))
    customer_interviews = []
    for meeting in all_meetings.values():
        title_lower = (meeting.get('title', '') or '').lower()
        if 'customer' in title_lower and ('interview' in title_lower or 'feedback' in title_lower):
            customer_interviews.append(meeting)
    
    print(f"Found {len(customer_interviews)} potential customer interview meetings")
    
    # Pull each meeting
    saved_files = []
    for meeting in customer_interviews:
        try:
            filepath = create_markdown_file(meeting, output_dir, cache_reader)
            saved_files.append(filepath)
            print(f"✓ Saved: {filepath.name}")
        except Exception as e:
            print(f"✗ Error saving {meeting.get('title', 'Unknown')}: {e}")
    
    print(f"\nSuccessfully saved {len(saved_files)} meeting files to {output_dir}")


if __name__ == "__main__":
    main()
