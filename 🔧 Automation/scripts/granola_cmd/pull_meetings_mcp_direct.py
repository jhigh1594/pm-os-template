#!/usr/bin/env python3
"""
Pull Granola meetings using MCP server directly to get summaries and transcripts.
"""

import json
import sys
from datetime import datetime
from pathlib import Path

# Meeting IDs
MEETING_IDS = [
    "9816a52d-a4e2-43d0-bbf9-5e106e7a38ba",
    "dd16d67a-b834-4ac8-9cd5-221a306ab234",
    "3487c752-5dc4-45ed-9aed-4956a1a60f6c",
    "4e0d4b89-5946-47d3-8f62-60279e62a49a",
    "9c0730b2-3c32-47a6-aa48-f4663b25ec3b",
    "796c1838-f42f-438f-96f0-afb1b077aeb2",
    "68f225b6-ffb5-4d3b-85ca-c74576d02554",
    "060f2b61-f410-48d0-8388-b60b22c38fbd",
]

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

def main():
    """This script needs to be run with MCP tools - showing structure."""
    print("This script should be run via MCP tools.")
    print("Meeting IDs to process:")
    for mid in MEETING_IDS:
        print(f"  - {mid}")

if __name__ == "__main__":
    main()
