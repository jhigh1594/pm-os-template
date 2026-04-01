#!/usr/bin/env python3
"""
Stop hook — end_of_turn.py
Runs at the end of each Claude turn. Appends a lightweight turn marker to the
session log so the session timeline stays queryable.
"""
import json
import os
import sys
from datetime import datetime
from pathlib import Path


def main():
    workspace = Path(os.environ.get("CLAUDE_WORKSPACE", ".")).resolve()
    log_dir = workspace / ".claude" / "logs"
    log_dir.mkdir(parents=True, exist_ok=True)
    log_file = log_dir / "session.jsonl"

    entry = {
        "ts": datetime.now().isoformat(),
        "event": "turn_end",
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
