#!/usr/bin/env python3
"""
UserPromptSubmit hook — continuation_cue.py
Runs each time the user submits a prompt. Logs the event timestamp so
session activity can be reconstructed from the log later.
Does NOT read or log prompt content — only the timing signal.
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
        "event": "user_prompt_submit",
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
