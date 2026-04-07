"""PostToolUse hook — capture skill invocations for the learning pipeline.

Only tracks Skill tool calls. InstructionsLoaded never fires for SKILL.md files,
so this hook is the sole input to the skills_learning pipeline for SNOW-Work.
"""

from __future__ import annotations

import json
import sys
from typing import Any


def load_hook_payload() -> dict[str, Any]:
    try:
        raw = sys.stdin.read().strip()
        if not raw:
            return {}
        return json.loads(raw)
    except (json.JSONDecodeError, TypeError):
        return {}


def record_skill_invocation(payload: dict[str, Any], skill_name: str) -> None:
    """Write a Skill tool invocation to load-events.jsonl for the skills_learning pipeline."""
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
    payload = load_hook_payload()
    if not payload:
        return 0

    if payload.get("tool_name") == "Skill":
        skill_name = (payload.get("tool_input") or {}).get("skill", "")
        if skill_name:
            record_skill_invocation(payload, skill_name)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
