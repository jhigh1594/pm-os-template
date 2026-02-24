#!/usr/bin/env python3
"""Fetch Batch 3 meetings with corrected meeting IDs."""

import sys
from pathlib import Path
from datetime import datetime
import json

sys.path.insert(0, str(Path(__file__).parent))
from mcp_client import GranolaCacheReader


def format_date(date_str: str) -> str:
    try:
        dt = datetime.fromisoformat(date_str.replace('Z', '+00:00'))
        return dt.strftime('%y-%m-%d')
    except:
        return datetime.now().strftime('%y-%m-%d')


def sanitize_filename(title: str) -> str:
    invalid_chars = '<>:"/\\|?*'
    for char in invalid_chars:
        title = title.replace(char, '-')
    if len(title) > 100:
        title = title[:100]
    return title.strip()


def create_markdown_file(meeting_id: str, output_dir: Path, cache_reader: GranolaCacheReader) -> Path:
    details = cache_reader.get_meeting_details(meeting_id)
    if not details or not details.get('title'):
        raise ValueError(f"Meeting {meeting_id} not found or has no title")

    title = details['title']
    date_str = details.get('created_at', '')

    date_formatted = format_date(date_str)
    title_sanitized = sanitize_filename(title)
    filename = f"{date_formatted}-{title_sanitized}.md"
    filepath = output_dir / filename

    transcript = cache_reader.get_meeting_transcript(meeting_id)
    documents = cache_reader.get_meeting_documents(meeting_id)
    granola_summary = cache_reader.get_granola_summary(meeting_id)

    state = cache_reader.load_cache().get("state", {})
    documents_dict = state.get("documents", {})
    raw_doc = documents_dict.get(meeting_id, {})

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

    participants = details.get("participants", [])
    participants_str = ', '.join(participants) if participants else 'N/A'

    # Format date for YAML
    date_yaml = date_str[:10] if len(date_str) >= 10 else ""

    lines = [
        "---",
        f'title: "{title}"',
        f'date: "{date_yaml}"',
        f'meeting_id: "{meeting_id}"',
        f"duration: {details.get('duration', 0)}",
        f"participants: {json.dumps(participants)}",
        "---",
        "",
        f"# {title}",
        "",
        f"**Date:** {date_str}",
        f"**Duration:** {details.get('duration', 0)} minutes",
        f"**Participants:** {participants_str}",
        "",
        "---",
        "",
    ]

    summary_added = False

    if granola_summary and granola_summary.strip():
        lines.extend(["## Summary", "", granola_summary.strip(), ""])
        summary_added = True

    if not summary_added and panel_summaries:
        lines.extend(["## Summary", "", "\n\n".join(panel_summaries), ""])
        summary_added = True

    if not summary_added and raw_doc.get('overview'):
        lines.extend(["## Summary", "", raw_doc['overview'], ""])
        summary_added = True

    if not summary_added and documents:
        for doc in documents:
            if doc.get('title') in ['Summary', 'Overview'] and doc.get('content'):
                lines.extend(["## Summary", "", doc['content'], ""])
                summary_added = True
                break

    if not summary_added and raw_doc.get('notes_markdown'):
        lines.extend(["## Summary", "", raw_doc['notes_markdown'], ""])
        summary_added = True

    if transcript and transcript.strip():
        lines.extend(["---", "", "## Transcript", "", transcript.strip(), ""])

    lines.append(f"Chat with meeting transcript: https://notes.granola.ai/t/{meeting_id}")
    lines.append("")

    filepath.write_text('\n'.join(lines), encoding='utf-8')
    return filepath


def main():
    # Corrected meeting IDs for Batch 3
    meeting_ids = [
        ("5eecac9b-3514-498b-8ce2-d0fb206c3582", "Project Advantage roadmap"),
        ("40a155fa-380e-40ed-82c1-0b7e53944de7", "Adaptive Work integration"),
        ("8d3f3175-a87d-4360-87dc-61825d1eb661", "Professional services"),
        ("321d5826-561e-43b7-9157-0ce00df5731f", "Command of message"),
        ("353ff5e1-1716-41ab-99ce-a37e0536e184", "Q1 PI planning"),
        ("4e4b2784-a3aa-4ec0-988a-1123bac68ee2", "IHG Agile Costing"),
    ]

    workspace_root = Path(__file__).parent.parent.parent.parent
    output_dir = workspace_root / 'Company' / 'meeting-notes' / 'granola'
    output_dir.mkdir(parents=True, exist_ok=True)

    cache_reader = GranolaCacheReader()

    print(f"Fetching Batch 3 ({len(meeting_ids)} meetings) from Granola...")
    print()

    saved_files = []
    errors = []

    for i, (meeting_id, description) in enumerate(meeting_ids, 21):
        try:
            filepath = create_markdown_file(meeting_id, output_dir, cache_reader)
            saved_files.append(filepath)

            content = filepath.read_text()
            has_summary = '## Summary' in content
            has_transcript = '## Transcript' in content
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
