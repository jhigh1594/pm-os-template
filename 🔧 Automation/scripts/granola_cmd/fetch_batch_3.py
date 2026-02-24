#!/usr/bin/env python3
"""
Fetch Batch 3 of Granola meetings (meetings 21-26 of 26).
"""

import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent))

from mcp_client import GranolaCacheReader


def format_date(date_str: str) -> str:
    """Format date string for filename."""
    try:
        from datetime import datetime
        dt = datetime.fromisoformat(date_str.replace('Z', '+00:00'))
        return dt.strftime('%y-%m-%d')
    except:
        from datetime import datetime
        return datetime.now().strftime('%y-%m-%d')


def sanitize_filename(title: str) -> str:
    """Sanitize title for use in filename."""
    invalid_chars = '<>:"/\\|?*'
    for char in invalid_chars:
        title = title.replace(char, '-')
    if len(title) > 100:
        title = title[:100]
    return title.strip()


def create_markdown_file(meeting_id: str, output_dir: Path, cache_reader: GranolaCacheReader) -> Path:
    """Create markdown file for a meeting."""
    import json

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
    """Main function to fetch Batch 3 meetings."""

    # Batch 3 meeting IDs (21-26 of 26)
    meeting_ids = [
        "5eecac9b-3c6d-4a00-9375-d5e7c487e7ca",  # 21 - Project Advantage roadmap
        "40a155fa-874e-4444-8f5f-e91a4ec7fc94",  # 22 - Adaptive Work integration
        "8d3f3175-a5cb-4c14-9ecb-2a84455d5f0a",  # 23 - Professional services enablement
        "321d5826-21cd-47de-af68-f9b5ca0bc566",  # 24 - Command of message framework
        "353ff5e1-8377-429d-9e4b-4f849e2eb01b",  # 25 - Q1 PI planning
        "4e4b2784-6406-491b-9880-2af8e6c80545",  # 26 - IHG Agile Costing
    ]

    meeting_descriptions = {
        "5eecac9b-3c6d-4a00-9375-d5e7c487e7ca": "Project Advantage roadmap",
        "40a155fa-874e-4444-8f5f-e91a4ec7fc94": "Adaptive Work integration",
        "8d3f3175-a5cb-4c14-9ecb-2a84455d5f0a": "Professional services enablement",
        "321d5826-21cd-47de-af68-f9b5ca0bc566": "Command of message framework",
        "353ff5e1-8377-429d-9e4b-4f849e2eb01b": "Q1 PI planning",
        "4e4b2784-6406-491b-9880-2af8e6c80545": "IHG Agile Costing",
    }

    # Setup paths
    workspace_root = Path(__file__).parent.parent.parent.parent
    output_dir = workspace_root / "Company" / "meeting-notes" / "granola"
    output_dir.mkdir(parents=True, exist_ok=True)

    # Initialize cache reader
    cache_reader = GranolaCacheReader()

    print(f"Fetching Batch 3 ({len(meeting_ids)} meetings) from Granola...")
    print()

    # Pull each meeting
    saved_files = []
    errors = []

    for i, meeting_id in enumerate(meeting_ids, start=21):
        description = meeting_descriptions.get(meeting_id, "Unknown")
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

            print(f"[{i}] {status} {description}: {filepath.name}")
        except Exception as e:
            errors.append((meeting_id, description, str(e)))
            print(f"[{i}] ✗ Error - {description}: {e}")

    print()
    print("=" * 80)
    print(f"Results: Successfully saved {len(saved_files)} of {len(meeting_ids)} meeting files")
    print(f"Output directory: {output_dir}")
    print("=" * 80)

    if errors:
        print()
        print(f"Errors ({len(errors)}):")
        for meeting_id, description, error in errors:
            print(f"  - [{description}] {meeting_id}: {error}")

    return len(saved_files), len(errors)


if __name__ == "__main__":
    saved, failed = main()
    sys.exit(0 if failed == 0 else 1)
