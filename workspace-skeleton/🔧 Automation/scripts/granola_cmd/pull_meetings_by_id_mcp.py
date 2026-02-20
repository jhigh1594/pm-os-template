#!/usr/bin/env python3
"""
Pull specific Granola meetings by ID using MCP server and save to Company/meeting-notes/granola.
"""

import json
import subprocess
import sys
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent))

from mcp_client import GranolaCacheReader


def extract_meeting_id(url: str) -> str:
    """Extract meeting ID from Granola URL."""
    parts = url.split('/t/')
    if len(parts) > 1:
        meeting_id_part = parts[1].split('-00b881l8')[0]
        return meeting_id_part
    return url


def format_date(date_str: str) -> str:
    """Format date string for filename."""
    try:
        dt = datetime.fromisoformat(date_str.replace('Z', '+00:00'))
        return dt.strftime('%y-%m-%d')
    except:
        return datetime.now().strftime('%y-%m-%d')


def sanitize_filename(title: str) -> str:
    """Sanitize title for use in filename."""
    invalid_chars = '<>:"/\\|?*'
    for char in invalid_chars:
        title = title.replace(char, '-')
    if len(title) > 100:
        title = title[:100]
    return title.strip()


def get_mcp_meeting_data(meeting_id: str) -> Dict[str, Any]:
    """Get meeting data using MCP server via subprocess."""
    # This would require the MCP server to be running
    # For now, we'll use the cache reader but enhance it
    return {}


def create_markdown_file(meeting_id: str, output_dir: Path, cache_reader: GranolaCacheReader) -> Path:
    """Create markdown file for a meeting."""
    # Get meeting details
    details = cache_reader.get_meeting_details(meeting_id)
    if not details or not details.get('title'):
        raise ValueError(f"Meeting {meeting_id} not found or has no title")
    
    title = details['title']
    date_str = details.get('created_at', '')
    
    # Format date for filename
    date_formatted = format_date(date_str)
    title_sanitized = sanitize_filename(title)
    filename = f"{date_formatted}-{title_sanitized}.md"
    filepath = output_dir / filename
    
    # Get all available data
    transcript = cache_reader.get_meeting_transcript(meeting_id)
    documents = cache_reader.get_meeting_documents(meeting_id)
    granola_summary = cache_reader.get_granola_summary(meeting_id)
    
    # Get raw document for additional fields
    state = cache_reader.load_cache().get("state", {})
    documents_dict = state.get("documents", {})
    raw_doc = documents_dict.get(meeting_id, {})
    
    # Also check documentPanels more thoroughly
    document_panels = state.get("documentPanels", {})
    panel_summaries = []
    if meeting_id in document_panels:
        panels = document_panels[meeting_id]
        for panel_id, panel in panels.items():
            if panel.get("content"):
                try:
                    panel_summary = cache_reader._extract_text_from_tiptap(panel["content"])
                    if panel_summary and panel_summary.strip():
                        panel_summaries.append(panel_summary.strip())
                except:
                    pass
    
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
    
    # Add summary - try multiple sources in order of preference
    summary_added = False
    
    # 1. Try Granola's AI summary from documentPanels (most complete)
    if granola_summary and granola_summary.strip():
        lines.extend([
            "## Summary",
            "",
            granola_summary.strip(),
            "",
        ])
        summary_added = True
    
    # 2. Try panel summaries if granola_summary didn't work
    if not summary_added and panel_summaries:
        lines.extend([
            "## Summary",
            "",
            "\n\n".join(panel_summaries),
            "",
        ])
        summary_added = True
    
    # 3. Try overview field from document
    if not summary_added and raw_doc.get('overview'):
        lines.extend([
            "## Summary",
            "",
            raw_doc['overview'],
            "",
        ])
        summary_added = True
    
    # 4. Try documents list
    if not summary_added and documents:
        for doc in documents:
            if doc.get('title') in ['Summary', 'Overview'] and doc.get('content'):
                lines.extend([
                    "## Summary",
                    "",
                    doc['content'],
                    "",
                ])
                summary_added = True
                break
    
    # 5. Try notes_markdown as fallback
    if not summary_added and raw_doc.get('notes_markdown'):
        lines.extend([
            "## Summary",
            "",
            raw_doc['notes_markdown'],
            "",
        ])
        summary_added = True
    
    # Add transcript if available
    if transcript and transcript.strip():
        lines.extend([
            "---",
            "",
            "## Transcript",
            "",
            transcript.strip(),
            "",
        ])
    
    # Add Granola link
    lines.append(f"Chat with meeting transcript: https://notes.granola.ai/t/{meeting_id}")
    lines.append("")
    
    # Write file
    filepath.write_text('\n'.join(lines), encoding='utf-8')
    return filepath


def main():
    """Main function to pull meetings by ID."""
    # Meeting URLs/IDs provided by user
    meeting_urls = [
        "https://notes.granola.ai/t/9816a52d-a4e2-43d0-bbf9-5e106e7a38ba-00b881l8",
        "https://notes.granola.ai/t/dd16d67a-b834-4ac8-9cd5-221a306ab234-00b881l8",
        "https://notes.granola.ai/t/3487c752-5dc4-45ed-9aed-4956a1a60f6c-00b881l8",
        "https://notes.granola.ai/t/4e0d4b89-5946-47d3-8f62-60279e62a49a-00b881l8",
        "https://notes.granola.ai/t/9c0730b2-3c32-47a6-aa48-f4663b25ec3b-00b881l8",
        "https://notes.granola.ai/t/796c1838-f42f-438f-96f0-afb1b077aeb2-00b881l8",
        "https://notes.granola.ai/t/68f225b6-ffb5-4d3b-85ca-c74576d02554-00b881l8",
        "https://notes.granola.ai/t/060f2b61-f410-48d0-8388-b60b22c38fbd-00b881l8",
    ]
    
    # Extract meeting IDs
    meeting_ids = [extract_meeting_id(url) for url in meeting_urls]
    
    # Setup paths
    workspace_root = Path(__file__).parent.parent.parent.parent
    output_dir = workspace_root / "Company" / "meeting-notes" / "granola"
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Initialize cache reader
    cache_reader = GranolaCacheReader()
    
    print(f"Pulling {len(meeting_ids)} meetings from Granola...")
    
    # Pull each meeting
    saved_files = []
    errors = []
    
    for meeting_id in meeting_ids:
        try:
            filepath = create_markdown_file(meeting_id, output_dir, cache_reader)
            saved_files.append(filepath)
            
            # Check what we got
            content = filepath.read_text()
            has_summary = "## Summary" in content
            has_transcript = "## Transcript" in content
            status = "✓"
            if not has_summary:
                status += " (no summary)"
            if not has_transcript:
                status += " (no transcript)"
            
            print(f"{status} Saved: {filepath.name}")
        except Exception as e:
            errors.append((meeting_id, str(e)))
            print(f"✗ Error saving {meeting_id}: {e}")
    
    print(f"\nSuccessfully saved {len(saved_files)} meeting files to {output_dir}")
    if errors:
        print(f"\nErrors ({len(errors)}):")
        for meeting_id, error in errors:
            print(f"  - {meeting_id}: {error}")


if __name__ == "__main__":
    main()
