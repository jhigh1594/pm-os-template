#!/usr/bin/env python3
"""Guarded session-end workflow for Claude hooks."""

from __future__ import annotations

import argparse
import asyncio
import json
import os
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


def load_json_file(path: Path, default: dict[str, Any] | None = None) -> dict[str, Any]:
    """Load a JSON file, returning default on error."""
    if default is None:
        default = {}
    if not path.exists():
        return default
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return default


def load_session_intent(workspace_root: Path) -> dict[str, Any]:
    """Load the canonical session intent file when present."""
    path = workspace_root / "🤖 AI" / "session-intent.json"
    return load_json_file(path)


def session_start_for_git(session_state: dict[str, Any]) -> str | None:
    """Return a git-compatible since timestamp from session state."""
    start_time = (session_state.get("start_time") or "").strip()
    if not start_time:
        return None

    try:
        start_dt = datetime.fromisoformat(start_time.replace("Z", "+00:00"))
    except ValueError:
        return None
    return start_dt.strftime("%Y-%m-%d %H:%M:%S")


def count_git_commits_since_session_start(workspace_root: Path, session_state: dict[str, Any]) -> int:
    """Count git commits made since the session started."""
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


def should_record_observer_session_end(workspace_root: Path) -> bool:
    """Return whether observer-based session-end recording should run."""
    return (
        os.environ.get("AIPMOS_SESSION_END_RECORD_TIME", "1") != "00"
        and (workspace_root / "🤖 AI" / "config.yaml").exists()
    )


def should_run_memory_update(commit_count: int, session_state: dict[str, Any]) -> bool:
    """Auto-update memory when the session produced commits OR had a captured intent.

    Commit-only gating misses PM/knowledge-work sessions (strategy discussions,
    PRD writing, research synthesis) that never produce git commits but are the
    primary work in this workspace. Intent capture is a reliable proxy for
    "something meaningful happened" since continuation_cue.py populates it from
    the first user message.
    """
    if os.environ.get("AIPMOS_SESSION_END_AUTO_MEMORY", "1") == "0":
        return False
    has_commits = commit_count > 0
    has_intent = bool((session_state.get("intent") or "").strip())
    return has_commits or has_intent


def should_run_memory_maintainer(memory_updated: bool) -> bool:
    """Run the maintainer only when memory changed during session end."""
    return (
        os.environ.get("AIPMOS_SESSION_END_RUN_MAINTAINER", "1") != "0"
        and memory_updated
    )


def should_reset_session_intent() -> bool:
    """Return whether session-end should archive and reset the intent file."""
    return os.environ.get("AIPMOS_SESSION_END_RESET_INTENT", "1") != "0"


def should_run_skill_learning_ingest() -> bool:
    """Return whether skill learning should persist session runs."""
    return os.environ.get("AIPMOS_SKILL_LEARNING_INGEST", "1") != "0"


def should_run_pattern_extraction() -> bool:
    """Return whether session-end should extract patterns from learning signals."""
    return os.environ.get("AIPMOS_SESSION_END_PATTERN_EXTRACTION", "1") != "0"


def should_run_semantic_health_check() -> bool:
    """Return whether session-end should run semantic drift detection."""
    return os.environ.get("AIPMOS_SESSION_END_SEMANTIC_HEALTH", "1") != "0"


def load_session_counter(cache_dir: Path) -> dict[str, int]:
    """Load the session counter for weekly operations."""
    counter_file = cache_dir / "session-counter.json"
    return load_json_file(counter_file, {"count": 0})


def save_session_counter(cache_dir: Path, counter: dict[str, int]) -> None:
    """Save the session counter."""
    counter_file = cache_dir / "session-counter.json"
    counter_file.parent.mkdir(parents=True, exist_ok=True)
    counter_file.write_text(json.dumps(counter, indent=2), encoding="utf-8")


def run_semantic_health_check(workspace_root: Path) -> None:
    """Run semantic drift detection and emit warnings."""
    sys.path.insert(0, str(workspace_root / "🔧 Automation/scripts"))
    try:
        from hooks.semantic_health_checker import check_semantic_drift, format_drift_report
    except ImportError:
        return

    drift = check_semantic_drift(workspace_root, days_back=14)
    if drift:
        report = format_drift_report(drift)
        if report:
            print("")
            print(report)


async def _mark_session_end_async(workspace_root: Path) -> int | None:
    """Record session end using the existing observer system when available."""
    sys.path.insert(0, str(workspace_root / "🔧 Automation/scripts"))

    try:
        from observers.observer_manager import ObserverManager
    except Exception:
        return None

    manager = ObserverManager()
    await manager.initialize(workspace_root, str(workspace_root / "🤖 AI" / "config.yaml"))
    time_observer = manager.get_observer("time_patterns")
    if not time_observer:
        return None
    return await time_observer.mark_session_end()


def record_observer_session_end(workspace_root: Path) -> None:
    """Best-effort wrapper around observer time recording."""
    if not should_record_observer_session_end(workspace_root):
        return

    try:
        duration = asyncio.run(_mark_session_end_async(workspace_root))
    except Exception as exc:
        sys.stderr.write(f"Session end recording failed: {exc}\n")
        return

    if duration:
        print(f"Session duration: {duration}s")


def run_python_script(python_cmd: str, script_path: Path, *args: str) -> bool:
    """Run a Python script best-effort and report success."""
    if not script_path.exists():
        return False

    try:
        completed = subprocess.run(
            [python_cmd, str(script_path), *args],
            capture_output=True,
            text=True,
            check=False,
        )
    except OSError:
        return False

    if completed.stdout.strip():
        print(completed.stdout.strip())
    if completed.stderr.strip():
        sys.stderr.write(completed.stderr.strip() + "\n")
    return completed.returncode == 0


def archive_and_reset_session_intent(
    workspace_root: Path,
    session_state: dict[str, Any],
    *,
    now: datetime | None = None,
) -> Path | None:
    """Archive the current intent file and reset it for the next session."""
    if not should_reset_session_intent():
        return None

    intent_file = workspace_root / "🤖 AI" / "session-intent.json"
    if not intent_file.exists():
        return None

    now = now or datetime.now(timezone.utc)
    session_id = str(session_state.get("session_id") or "unknown")
    backup_dir = workspace_root / "🤖 AI" / "sessions-archive"
    backup_dir.mkdir(parents=True, exist_ok=True)
    backup_path = backup_dir / f"{session_id}.json"

    try:
        backup_path.write_text(intent_file.read_text(encoding="utf-8"), encoding="utf-8")
    except OSError:
        backup_path = None

    new_session = {
        "session_id": f"{int(time.time())}{os.getpid()}",
        "start_time": now.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "intent": "",
        "user_description": "",
    }
    intent_file.write_text(json.dumps(new_session, indent=2), encoding="utf-8")
    return backup_path


def run_pattern_extraction(workspace_root: Path, session_state: dict[str, Any]) -> list[dict[str, Any]]:
    """Extract patterns from learning signals and write to candidates file."""
    sys.path.insert(0, str(workspace_root / "🔧 Automation/scripts"))
    try:
        from hooks.pattern_extractor import extract_patterns_from_session
    except ImportError:
        return []

    patterns = extract_patterns_from_session(workspace_root, session_state)
    if patterns:
        print("")
        print(f"## Pattern learning extracted {len(patterns)} candidate(s)")
        for p in patterns:
            print(f"  - {p['category']}: \"{p['lesson']}\" ({p['confidence']})")
    return patterns


def run_session_end(workspace_root: Path, python_cmd: str) -> int:
    """Execute the guarded session-end workflow."""
    session_state = load_session_intent(workspace_root)
    commit_count = count_git_commits_since_session_start(workspace_root, session_state)

    record_observer_session_end(workspace_root)

    memory_updated = False
    if should_run_memory_update(commit_count, session_state):
        print("")
        print("## Auto-updating memory.md")
        memory_updated = run_python_script(
            python_cmd,
            workspace_root / "🔧 Automation/scripts/memory_updater.py",
            "--workspace",
            str(workspace_root),
        )
        if memory_updated:
            print("")
            print(f"✅ Memory.md automatically updated with {commit_count} session commit(s)")

    if should_run_memory_maintainer(memory_updated):
        run_python_script(
            python_cmd,
            workspace_root / "🔧 Automation/scripts/memory_maintainer.py",
            "--workspace",
            str(workspace_root),
        )

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

    # Pattern extraction from learning signals
    if should_run_pattern_extraction():
        run_pattern_extraction(workspace_root, session_state)

    # Semantic health check (weekly)
    if should_run_semantic_health_check():
        cache_dir = workspace_root / ".cache" / "claude" / "hooks"
        counter = load_session_counter(cache_dir)
        counter["count"] += 1
        save_session_counter(cache_dir, counter)

        if counter["count"] % 7 == 0:  # Every 7th session
            run_semantic_health_check(workspace_root)

    archive_and_reset_session_intent(workspace_root, session_state)

    # Clean up rolling state file (no longer relevant after session ends)
    rolling_state_path = workspace_root / ".cache" / "claude" / "hooks" / "rolling-state.json"
    rolling_state_path.unlink(missing_ok=True)

    return 0


def main(argv: list[str]) -> int:
    """CLI entrypoint."""
    parser = argparse.ArgumentParser(description="Run guarded session-end behavior")
    parser.add_argument("--workspace", type=Path, default=Path.cwd(), help="Workspace root")
    parser.add_argument("--python-cmd", default="python3", help="Python executable for child scripts")
    args = parser.parse_args(argv[1:])

    return run_session_end(args.workspace, args.python_cmd)


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
