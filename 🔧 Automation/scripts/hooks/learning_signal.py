#!/usr/bin/env python3
"""
PostToolUse hook — learning_signal.py
Logs tool usage patterns to support continual learning / pattern detection.
Reads Claude Code hook env vars: CLAUDE_TOOL_NAME, CLAUDE_TOOL_INPUT, CLAUDE_TOOL_RESULT
"""
import json
import os
import sys
from datetime import datetime
from pathlib import Path


def main():
    workspace = Path(os.environ.get("CLAUDE_WORKSPACE", ".")).resolve()
    tool_name = os.environ.get("CLAUDE_TOOL_NAME", "unknown")
    log_dir = workspace / ".claude" / "logs"
    log_dir.mkdir(parents=True, exist_ok=True)
    log_file = log_dir / "tool_usage.jsonl"

    entry = {
        "ts": datetime.now().isoformat(),
        "tool": tool_name,
    }

    try:
        with open(log_file, "a") as f:
            f.write(json.dumps(entry) + "\n")
    except Exception:
        pass  # Never block on logging failure


if __name__ == "__main__":
    try:
        main()
    except Exception:
        pass
    sys.exit(0)
