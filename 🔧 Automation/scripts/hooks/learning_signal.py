"""PostToolUse hook - capture learning signals from tool usage.

Watches for error patterns (PostToolUseFailure, retry loops) and writes
observations to a bounded JSONL queue. The end_of_turn hook reads this queue
and nudges the model if significant patterns emerge.

Design: Extremely lightweight. Only fires meaningful output, never on every tool call.
"""

from __future__ import annotations

import json
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


QUEUE_PATH = Path(".cache/claude/hooks/learning-signals.jsonl")
MAX_QUEUE_SIZE = 50
MAX_QUEUE_AGE_HOURS = 24


def load_hook_payload() -> dict[str, Any]:
    """Parse PostToolUse hook JSON from stdin."""
    try:
        raw = sys.stdin.read().strip()
        if not raw:
            return {}
        return json.loads(raw)
    except (json.JSONDecodeError, TypeError):
        return {}


def prune_stale_entries(queue_path: Path) -> int:
    """Remove entries older than MAX_QUEUE_AGE_HOURS."""
    if not queue_path.exists():
        return 0

    cutoff = time.time() - (MAX_QUEUE_AGE_HOURS * 3600)
    try:
        lines = queue_path.read_text(encoding="utf-8").strip().splitlines()
    except (OSError, UnicodeDecodeError):
        return 0

    kept = []
    for line in lines:
        line = line.strip()
        if not line:
            continue
        try:
            entry = json.loads(line)
            if entry.get("timestamp", 0) >= cutoff:
                kept.append(line)
        except json.JSONDecodeError:
            kept.append(line)

    if len(kept) < len(lines):
        queue_path.write_text("\n".join(kept) + "\n", encoding="utf-8")
    return len(lines) - len(kept)


def queue_size(queue_path: Path) -> int:
    """Return current queue length."""
    if not queue_path.exists():
        return 0
    try:
        return sum(1 for line in queue_path.read_text(encoding="utf-8").splitlines() if line.strip())
    except (OSError, UnicodeDecodeError):
        return 0


def enqueue_signal(queue_path: Path, signal: dict[str, Any]) -> None:
    """Append a learning signal to the bounded queue."""
    queue_path.parent.mkdir(parents=True, exist_ok=True)

    # Read existing, prune stale, then append
    prune_stale_entries(queue_path)

    current_size = queue_size(queue_path)
    if current_size >= MAX_QUEUE_SIZE:
        return  # Queue full, FIFO eviction happens on next write

    signal["timestamp"] = int(time.time())
    with open(queue_path, "a", encoding="utf-8") as f:
        f.write(json.dumps(signal) + "\n")


def record_skill_invocation(payload: dict[str, Any], skill_name: str) -> None:
    """Write a Skill tool invocation to load-events.jsonl so the pipeline has data.

    InstructionsLoaded never fires for SKILL.md files — this is the workaround that
    feeds the skills_learning pipeline (runs.jsonl → evals → LEARNED.md updates).
    """
    try:
        from skills_learning.runtime import capture_instruction_load
        synthetic = {
            "session_id": payload.get("session_id", ""),
            "hook_event_name": "InstructionsLoaded",
            "file_path": f".claude/skills/{skill_name}/SKILL.md",
            "load_reason": "skill_invocation",
        }
        capture_instruction_load(synthetic)
    except Exception:
        pass


def main() -> int:
    """Entry point for PostToolUse hook."""
    payload = load_hook_payload()
    if not payload:
        return 0

    # Only capture meaningful signals, not every tool call
    tool_name = payload.get("tool_name", "")
    tool_input = payload.get("tool_input", {})
    is_error = payload.get("is_error", False)
    error = payload.get("error", "")

    signals_to_capture = []

    # Signal 1: Tool failure
    if is_error and error:
        signals_to_capture.append({
            "type": "tool_error",
            "tool": tool_name,
            "summary": error[:200],
        })

    # Signal 2: Retry detection (same tool called multiple times in quick succession)
    # This is a simple heuristic - the end_of_turn hook will aggregate
    if tool_name == "Edit" or tool_name == "Write":
        file_path = tool_input.get("file_path", "")
        if file_path:
            signals_to_capture.append({
                "type": "file_modification",
                "tool": tool_name,
                "file": file_path,
                "summary": f"{tool_name} on {Path(file_path).name}",
            })

    # Signal 3: Skill invocation — feeds the skills_learning pipeline.
    # InstructionsLoaded never fires for SKILL.md files, so PostToolUse is the
    # only reliable hook that can capture skill usage.
    if tool_name == "Skill":
        skill_name = tool_input.get("skill", "")
        if skill_name:
            record_skill_invocation(payload, skill_name)

    for signal in signals_to_capture:
        enqueue_signal(QUEUE_PATH, signal)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
