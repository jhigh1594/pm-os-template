#!/usr/bin/env python3
"""
InstructionsLoaded hook — instruction_load_audit.py
Runs after Claude loads CLAUDE.md instructions. Records which instruction
files were active at session start for auditability.
"""
import json
import os
import sys
from datetime import datetime
from pathlib import Path


def collect_instruction_files(workspace: Path) -> list[str]:
    """Return relative paths of all CLAUDE.md files found in workspace."""
    return [
        str(p.relative_to(workspace))
        for p in workspace.rglob("CLAUDE.md")
        if ".git" not in p.parts and ".venv" not in p.parts
    ]


def main():
    workspace = Path(os.environ.get("CLAUDE_WORKSPACE", ".")).resolve()
    log_dir = workspace / ".claude" / "logs"
    log_dir.mkdir(parents=True, exist_ok=True)
    log_file = log_dir / "session.jsonl"

    entry = {
        "ts": datetime.now().isoformat(),
        "event": "instructions_loaded",
        "instruction_files": collect_instruction_files(workspace),
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
