#!/usr/bin/env python3
"""
Stop hook — end_of_turn.py
Runs at the end of each Claude turn. Writes a rolling state file so that
context can be recovered after /clear (which doesn't trigger SessionEnd).

rolling-state.json is consumed by session-start.sh for [CLEAR RECOVERY].
It is deleted by session_end.py on proper CLI exit.
"""
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path


def find_active_specstory(workspace: Path, session_start_time: str | None) -> Path | None:
    """Return the most recent specstory transcript if it looks active this session."""
    history_dir = workspace / ".specstory" / "history"
    if not history_dir.exists():
        return None

    candidates = sorted(history_dir.glob("*.md"), key=lambda p: p.stat().st_mtime, reverse=True)
    if not candidates:
        return None

    latest = candidates[0]
    # Must have been modified in the last 4 hours to be considered active
    age_hours = (datetime.now().timestamp() - latest.stat().st_mtime) / 3600
    if age_hours > 4:
        return None

    return latest


def write_rolling_state(workspace: Path) -> None:
    """Write lightweight recovery state after each turn — no LLM call."""
    cache_dir = workspace / ".cache" / "claude" / "hooks"
    cache_dir.mkdir(parents=True, exist_ok=True)

    # Load current session intent
    intent_file = workspace / "🤖 AI" / "session-intent.json"
    session_state: dict = {}
    if intent_file.exists():
        try:
            session_state = json.loads(intent_file.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            pass

    intent = session_state.get("intent", "").strip()
    user_description = session_state.get("user_description", "").strip()
    session_start = session_state.get("start_time", "")

    # Use specstory presence as the "active session" signal when intent isn't set
    transcript = find_active_specstory(workspace, session_start)
    if not intent and not user_description and not transcript:
        return  # Nothing worth recovering

    rolling_state = {
        "ts": datetime.now(timezone.utc).isoformat(),
        "event": "rolling_state",
        "intent": intent,
        "user_description": user_description,
        "session_id": session_state.get("session_id", ""),
        "transcript": transcript.name if transcript else "",
    }

    rolling_state_path = cache_dir / "rolling-state.json"
    try:
        rolling_state_path.write_text(json.dumps(rolling_state, indent=2), encoding="utf-8")
    except OSError:
        pass


def write_turn_marker(workspace: Path) -> None:
    """Append a lightweight turn marker to the session log."""
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


def main():
    workspace = Path(os.environ.get("CLAUDE_WORKSPACE", ".")).resolve()
    write_turn_marker(workspace)
    write_rolling_state(workspace)


if __name__ == "__main__":
    try:
        main()
    except Exception:
        pass
    sys.exit(0)
