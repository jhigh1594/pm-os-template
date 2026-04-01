#!/usr/bin/env python3
"""
PreCompact hook — compact_state.py
Runs before Claude Code compacts the context window.
Captures a lightweight snapshot of current session state so context
can be partially reconstructed after compaction.

Usage: compact_state.py capture
"""
import json
import os
import sys
from datetime import datetime
from pathlib import Path


def capture(workspace: Path):
    log_dir = workspace / ".claude" / "logs"
    log_dir.mkdir(parents=True, exist_ok=True)

    # Read last N lines of session log as pre-compact breadcrumb
    session_log = log_dir / "session.jsonl"
    recent_events = []
    if session_log.exists():
        lines = session_log.read_text().strip().splitlines()
        recent_events = lines[-20:] if len(lines) > 20 else lines

    snapshot = {
        "ts": datetime.now().isoformat(),
        "event": "pre_compact_snapshot",
        "recent_event_count": len(recent_events),
    }

    compact_log = log_dir / "compact_snapshots.jsonl"
    try:
        with open(compact_log, "a") as f:
            f.write(json.dumps(snapshot) + "\n")
    except Exception:
        pass


def main():
    workspace = Path(os.environ.get("CLAUDE_WORKSPACE", ".")).resolve()
    command = sys.argv[1] if len(sys.argv) > 1 else "capture"
    if command == "capture":
        capture(workspace)


if __name__ == "__main__":
    try:
        main()
    except Exception:
        pass
    sys.exit(0)
