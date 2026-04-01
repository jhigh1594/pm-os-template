#!/usr/bin/env python3
"""
SessionEnd hook — session_end.py
Runs when the Claude Code session ends. Appends a session-end marker with
timestamp and workspace path to the session log.

Args (optional, passed by settings.json):
  --workspace PATH   absolute path to project root
  --python-cmd CMD   python executable used (for diagnostics)
"""
import argparse
import json
import os
import sys
from datetime import datetime
from pathlib import Path


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--workspace", default=None)
    parser.add_argument("--python-cmd", default=None)
    args, _ = parser.parse_known_args()

    workspace = Path(args.workspace or os.environ.get("CLAUDE_WORKSPACE", ".")).resolve()
    log_dir = workspace / ".claude" / "logs"
    log_dir.mkdir(parents=True, exist_ok=True)
    log_file = log_dir / "session.jsonl"

    entry = {
        "ts": datetime.now().isoformat(),
        "event": "session_end",
        "workspace": str(workspace),
    }

    try:
        with open(log_file, "a") as f:
            f.write(json.dumps(entry) + "\n")
    except Exception:
        pass


if __name__ == "__main__":
    try:
        main()
    except Exception:
        pass
    sys.exit(0)
