"""
UserPromptSubmit hook — pre_clear_capture.py

Intercepts /clear commands before they wipe conversation context.
Runs the full session-end pipeline (extract → memory → patterns) automatically,
so the user never needs to manually run /checkpoint before clearing.

The hook is synchronous: the CLI waits for it before processing /clear,
giving us the window to capture while the transcript is still intact.
"""

from __future__ import annotations

import json
import os
import sys
from pathlib import Path


def read_payload() -> dict:
    try:
        return json.loads(sys.stdin.read().strip())
    except (json.JSONDecodeError, OSError):
        return {}


def is_clear_command(prompt: str) -> bool:
    return prompt.strip().lower() in {"/clear", "clear"}


def run_capture(workspace_root: Path) -> None:
    """Run the session-end pipeline — same logic as the SessionEnd hook."""
    scripts_dir = workspace_root / "🔧 Automation/scripts"
    sys.path.insert(0, str(scripts_dir))

    # Load session state
    session_state: dict = {}
    intent_file = workspace_root / "🤖 AI" / "session-intent.json"
    if intent_file.exists():
        try:
            session_state = json.loads(intent_file.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            pass

    # 1. Session extraction → memory.md + sessions/
    print("")
    print("## /clear detected — capturing session before clearing")
    try:
        from hooks.session_extractor import run_extraction
        success = run_extraction(workspace_root, session_state)
        if success:
            print("✅ Session captured")
        else:
            print("⚠️  Session extraction skipped (transcript too short or not found)")
    except Exception as exc:
        sys.stderr.write(f"pre_clear_capture: session extraction failed: {exc}\n")

    # 2. Pattern extraction → candidate-patterns.md
    try:
        from pattern_extractor import run_extraction as extract_patterns
        written = extract_patterns(workspace_root)
        if written:
            print(f"📋 {written} new pattern candidates staged")
    except Exception as exc:
        sys.stderr.write(f"pre_clear_capture: pattern extraction failed: {exc}\n")


def main() -> int:
    payload = read_payload()
    prompt = payload.get("prompt", "")

    if not is_clear_command(prompt):
        return 0  # Not /clear — nothing to do, exit fast

    # Resolve workspace root from payload cwd or environment
    cwd = payload.get("cwd") or os.environ.get("CLAUDE_WORKSPACE") or os.getcwd()
    workspace_root = Path(cwd)

    # Walk up to find workspace root (has GOALS.md or CLAUDE.md)
    candidate = workspace_root
    while candidate != candidate.parent:
        if (candidate / "GOALS.md").exists() or (candidate / "CLAUDE.md").exists():
            workspace_root = candidate
            break
        candidate = candidate.parent

    run_capture(workspace_root)

    # Always exit 0 — never block the /clear
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
