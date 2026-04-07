"""Guarded session-end workflow for Claude hooks."""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


def load_json_file(path: Path, default: dict[str, Any] | None = None) -> dict[str, Any]:
    if default is None:
        default = {}
    if not path.exists():
        return default
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return default


def load_session_intent(workspace_root: Path) -> dict[str, Any]:
    path = workspace_root / "🤖 AI" / "session-intent.json"
    return load_json_file(path)


def session_start_for_git(session_state: dict[str, Any]) -> str | None:
    start_time = (session_state.get("start_time") or "").strip()
    if not start_time:
        return None
    try:
        start_dt = datetime.fromisoformat(start_time.replace("Z", "+00:00"))
    except ValueError:
        return None
    return start_dt.strftime("%Y-%m-%d %H:%M:%S")


def count_git_commits_since_session_start(workspace_root: Path, session_state: dict[str, Any]) -> int:
    if not (workspace_root / ".git").exists():
        return 0
    since_value = session_start_for_git(session_state)
    if not since_value:
        return 0
    try:
        completed = subprocess.run(
            ["git", "log", "--since", since_value, "--oneline"],
            cwd=workspace_root,
            capture_output=True,
            text=True,
            check=False,
        )
    except OSError:
        return 0
    if completed.returncode != 0:
        return 0
    return sum(1 for line in completed.stdout.splitlines() if line.strip())


def should_run_memory_extraction(workspace_root: Path) -> bool:
    """Run LLM extraction when .specstory transcripts exist."""
    if os.environ.get("AIPMOS_SESSION_END_AUTO_MEMORY", "1") == "0":
        return False
    history_dir = workspace_root / ".specstory" / "history"
    return history_dir.exists() and any(history_dir.glob("*.md"))


def should_run_skill_learning_ingest() -> bool:
    return os.environ.get("AIPMOS_SKILL_LEARNING_INGEST", "1") != "0"


def run_session_end(workspace_root: Path, python_cmd: str) -> int:
    """Execute the guarded session-end workflow."""
    session_state = load_session_intent(workspace_root)

    # LLM-powered session extraction → memory.md + sessions/
    if should_run_memory_extraction(workspace_root):
        print("")
        print("## Extracting session memory")
        sys.path.insert(0, str(workspace_root / "🔧 Automation/scripts"))
        try:
            from hooks.session_extractor import run_extraction
            success = run_extraction(workspace_root, session_state)
            if success:
                print(f"✅ memory.md updated, session file written")
        except Exception as exc:
            sys.stderr.write(f"Session extraction failed: {exc}\n")

    # Skill learning pipeline
    if should_run_skill_learning_ingest():
        sys.path.insert(0, str(workspace_root / "🔧 Automation/scripts"))
        try:
            from skills_learning.runtime import ingest_session_runs
            ingested = ingest_session_runs(workspace_root, session_state=session_state)
            if ingested:
                print("")
                print(f"## Skill learning captured {len(ingested)} run(s)")
        except Exception as exc:
            sys.stderr.write(f"Skill learning session ingest failed: {exc}\n")

    # Pattern extraction — specstory signals + guest insights → candidate-patterns.md
    if os.environ.get("AIPMOS_SESSION_END_PATTERN_EXTRACT", "1") != "0":
        sys.path.insert(0, str(workspace_root / "🔧 Automation/scripts"))
        try:
            from pattern_extractor import run_extraction as extract_patterns
            written = extract_patterns(workspace_root)
            if written:
                print("")
                print(f"📋 {written} new pattern candidates → 🤖 AI/patterns/candidate-patterns.md")
        except Exception as exc:
            sys.stderr.write(f"Pattern extraction failed: {exc}\n")

    rolling_state_path = workspace_root / ".cache" / "claude" / "hooks" / "rolling-state.json"
    rolling_state_path.unlink(missing_ok=True)

    return 0


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description="Run guarded session-end behavior")
    parser.add_argument("--workspace", type=Path, default=Path.cwd(), help="Workspace root")
    parser.add_argument("--python-cmd", default="python3", help="Python executable for child scripts")
    args = parser.parse_args(argv[1:])
    return run_session_end(args.workspace, args.python_cmd)


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
