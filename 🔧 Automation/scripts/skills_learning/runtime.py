"""Bootstrap and runtime ingestion for workspace skill learning."""

from __future__ import annotations

import json
import hashlib
import subprocess
import uuid
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable

from observers.observer_manager import ObserverManager
from shared.aipmos_config import AIPMOSConfig

from .learnings import ensure_learned_file
from .models import RegistrySkillEntry, SkillRunRecord
from .registry import (
    build_registry,
    iter_skill_entries,
    iter_wrapper_entries,
    load_learning_config,
    load_registry,
    write_registry,
)
from .store import JsonlStore

SELF_LEARNING_SECTION = """
## Self-Learning

Before responding, read `LEARNED.md` in this skill directory when it exists and treat it as compact runtime guidance that sharpens this skill.

Rules for self-improvement:
- Keep `SKILL.md` human-owned; do not rewrite it directly from normal usage.
- Propose broader instruction changes through the central skill-learning review queue.
- Only promote specific, reusable, evidence-backed lessons into `LEARNED.md`.
""".strip()


def resolve_workspace_root(workspace_root: str | Path | None = None) -> Path:
    if workspace_root:
        return Path(workspace_root).resolve()
    return AIPMOSConfig().workspace_root


def learning_paths(workspace_root: Path) -> dict[str, Path]:
    config = load_learning_config(workspace_root)
    paths = config.get("paths", {})
    return {key: workspace_root / value for key, value in paths.items()}


def bootstrap_skill_learning(
    workspace_root: str | Path | None = None,
    *,
    augment_skill_files: bool = False,
) -> dict[str, Any]:
    workspace = resolve_workspace_root(workspace_root)
    config = load_learning_config(workspace)
    registry = build_registry(workspace)
    write_registry(workspace, registry)

    header_lines = config.get("learnings", {}).get("header_lines", ["# Learned"])
    for entry in iter_skill_entries(registry):
        ensure_learned_file(workspace / entry.learned_path, header_lines)
        if augment_skill_files:
            ensure_self_learning_section(workspace / entry.skill_path)

    paths = learning_paths(workspace)
    for key in ("runs", "candidates", "eval_results"):
        target = paths.get(key)
        if target and not target.exists():
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text("", encoding="utf-8")
    if paths.get("review_queue"):
        paths["review_queue"].mkdir(parents=True, exist_ok=True)
    # Ensure hook_state directory exists (used by capture_instruction_load)
    if paths.get("hook_state"):
        hook_state_dir = paths["hook_state"]
        hook_state_dir.mkdir(parents=True, exist_ok=True)
        # Create empty load-events.jsonl if missing
        load_events_file = hook_state_dir / "load-events.jsonl"
        if not load_events_file.exists():
            load_events_file.write_text("", encoding="utf-8")
    return registry


def ensure_self_learning_section(skill_path: Path) -> None:
    text = skill_path.read_text(encoding="utf-8")
    if "## Self-Learning" in text:
        return
    skill_path.write_text(text.rstrip() + "\n\n" + SELF_LEARNING_SECTION + "\n", encoding="utf-8")


def build_skill_version_hash(skill_path: Path, learned_path: Path) -> str:
    digest = hashlib.sha256()
    digest.update(skill_path.read_bytes())
    if learned_path.exists():
        digest.update(learned_path.read_bytes())
    return digest.hexdigest()[:16]


def capture_instruction_load(payload: dict[str, Any], workspace_root: str | Path | None = None) -> dict[str, Any] | None:
    workspace = resolve_workspace_root(workspace_root)
    bootstrap_skill_learning(workspace, augment_skill_files=False)
    registry = load_registry(workspace)
    relative_path = _relative_payload_path(payload.get("file_path"), workspace)
    if not relative_path:
        return None

    skill_entry = _match_skill_path(relative_path, registry)
    wrapper_entry = _match_wrapper_path(relative_path, registry)
    if not skill_entry and not wrapper_entry:
        return None

    state_dir = learning_paths(workspace)["hook_state"]
    state_dir.mkdir(parents=True, exist_ok=True)
    record = {
        "id": str(uuid.uuid4()),
        "timestamp": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "session_id": payload.get("session_id", ""),
        "load_reason": payload.get("load_reason", ""),
        "file_path": relative_path,
        "kind": "wrapper" if wrapper_entry else "skill",
        "skill_id": wrapper_entry.delegates_to if wrapper_entry else skill_entry.skill_id,
        "wrapper_command": wrapper_entry.command_name if wrapper_entry else "",
    }
    JsonlStore(state_dir / "load-events.jsonl").append(record)
    return record


def ingest_session_runs(
    workspace_root: str | Path | None = None,
    session_state: dict[str, Any] | None = None,
) -> list[SkillRunRecord]:
    workspace = resolve_workspace_root(workspace_root)
    bootstrap_skill_learning(workspace, augment_skill_files=False)
    registry = load_registry(workspace)
    session_state = session_state or _load_session_state(workspace)
    start_time = _parse_session_start(session_state.get("start_time", ""))
    hook_state_dir = learning_paths(workspace)["hook_state"]
    load_events = JsonlStore(hook_state_dir / "load-events.jsonl").load()
    checkpoint = _load_checkpoint(hook_state_dir / "ingest-checkpoint.json")
    history_summary = summarize_session_outcomes(workspace, start_time)

    skill_map = {item.skill_id: item for item in iter_skill_entries(registry)}
    fresh_events = [event for event in load_events if _is_new_event(event, checkpoint, start_time)]
    grouped: dict[tuple[str, str], dict[str, Any]] = {}
    for event in fresh_events:
        key = (event["skill_id"], event.get("wrapper_command", ""))
        grouped.setdefault(key, event)

    run_records: list[SkillRunRecord] = []
    for event in grouped.values():
        skill_entry = skill_map.get(event["skill_id"])
        if not skill_entry:
            continue
        skill_path = workspace / skill_entry.skill_path
        learned_path = workspace / skill_entry.learned_path
        version_hash = build_skill_version_hash(skill_path, learned_path)
        run_records.append(
            SkillRunRecord(
                run_id=str(uuid.uuid4()),
                skill_id=skill_entry.skill_id,
                skill_name=skill_entry.name,
                surface=skill_entry.surface,
                family=skill_entry.family,
                version_hash=version_hash,
                instruction_path=skill_entry.skill_path,
                wrapper_command=event.get("wrapper_command", ""),
                source="instructions_loaded",
                session_id=session_state.get("session_id", "") or event.get("session_id", ""),
                timestamp=event.get("timestamp", datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")),
                user_ask=history_summary.get("user_ask") or (session_state.get("user_description") or session_state.get("intent") or ""),
                outcome_signals=history_summary["signals"],
                tool_errors=history_summary["tool_errors"],
                retry_count=history_summary["retry_count"],
                user_correction_count=history_summary["user_correction_count"],
                positive_reinforcement_count=history_summary["positive_reinforcement_count"],
                success_confidence=history_summary["confidence"],
                evidence_paths=history_summary["evidence_paths"],
                metadata={
                    "load_reason": event.get("load_reason", ""),
                    "history_inference": history_summary["metadata"],
                },
            )
        )

    if not run_records:
        return []

    runs_store = JsonlStore(learning_paths(workspace)["runs"])
    for run in run_records:
        runs_store.append(run.to_dict())
    _record_run_observers(workspace, run_records)

    latest_seen = max(event.get("timestamp", "") for event in fresh_events)
    _write_checkpoint(hook_state_dir / "ingest-checkpoint.json", {"last_timestamp": latest_seen})
    return run_records


def summarize_session_outcomes(workspace_root: Path, start_time: datetime | None) -> dict[str, Any]:
    config = load_learning_config(workspace_root)
    signals: set[str] = set()
    evidence_paths: list[str] = []
    tool_errors: list[str] = []
    retry_count = 0
    user_correction_count = 0
    positive_reinforcement_count = 0
    user_ask = ""

    session_files = _recent_session_files(workspace_root, start_time)
    for session_file in session_files:
        evidence_paths.append(str(session_file.relative_to(workspace_root)))
        content = session_file.read_text(encoding="utf-8", errors="ignore")
        if not user_ask:
            user_ask = _extract_first_user_message(content)
        lower = content.lower()
        retry_count += _count_terms(lower, config.get("signals", {}).get("retry_terms", []))
        user_correction_count += _count_terms(lower, config.get("signals", {}).get("correction_terms", []))
        positive_reinforcement_count += _count_terms(lower, config.get("signals", {}).get("praise_terms", []))
        error_hits = _count_terms(lower, config.get("signals", {}).get("error_terms", []))
        if error_hits:
            tool_errors.append(f"{session_file.name}: {error_hits} error-like marker(s)")

    commit_count = _git_commit_count_since(workspace_root, start_time)
    if commit_count > 0 or positive_reinforcement_count > 0:
        signals.add("success")
    if tool_errors:
        signals.add("tool_error")
    if retry_count > 0:
        signals.add("retry_loop")
    if user_correction_count > 0:
        signals.add("user_correction")
    if positive_reinforcement_count > 0:
        signals.add("positive_reinforcement")
    if not signals:
        signals.add("unresolved")

    confidence = "medium" if evidence_paths else "low"
    if commit_count > 0 and evidence_paths:
        confidence = "high"

    return {
        "signals": sorted(signals),
        "tool_errors": tool_errors,
        "retry_count": retry_count,
        "user_correction_count": user_correction_count,
        "positive_reinforcement_count": positive_reinforcement_count,
        "confidence": confidence,
        "evidence_paths": evidence_paths,
        "user_ask": user_ask,
        "metadata": {
            "commit_count": commit_count,
            "session_files": len(session_files),
        },
    }


def _record_run_observers(workspace: Path, run_records: Iterable[SkillRunRecord]) -> None:
    manager = ObserverManager()

    async def _run() -> None:
        await manager.initialize(workspace, str(workspace / "🤖 AI" / "config.yaml"))
        observer = manager.get_observer("skill_run")
        if not observer:
            return
        for record in run_records:
            await observer.observe_and_record(**record.to_dict())

    import asyncio

    asyncio.run(_run())


def _relative_payload_path(file_path: str | None, workspace_root: Path) -> str:
    if not file_path:
        return ""
    try:
        return str(Path(file_path).resolve().relative_to(workspace_root.resolve()))
    except (OSError, ValueError):
        return file_path


def _match_skill_path(relative_path: str, registry: dict[str, Any]) -> RegistrySkillEntry | None:
    for entry in iter_skill_entries(registry):
        if entry.skill_path == relative_path:
            return entry
    return None


def _match_wrapper_path(relative_path: str, registry: dict[str, Any]):
    for entry in iter_wrapper_entries(registry):
        if entry.path == relative_path:
            return entry
    return None


def _load_session_state(workspace_root: Path) -> dict[str, Any]:
    session_path = workspace_root / "🤖 AI" / "session-intent.json"
    if not session_path.exists():
        return {}
    try:
        return json.loads(session_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return {}


def _parse_session_start(raw: str) -> datetime | None:
    if not raw:
        return None
    try:
        return datetime.fromisoformat(raw.replace("Z", "+00:00"))
    except ValueError:
        return None


def _load_checkpoint(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return {}


def _write_checkpoint(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2), encoding="utf-8")


def _is_new_event(event: dict[str, Any], checkpoint: dict[str, Any], start_time: datetime | None) -> bool:
    timestamp = event.get("timestamp", "")
    if not timestamp:
        return False
    if checkpoint.get("last_timestamp") and timestamp <= checkpoint["last_timestamp"]:
        return False
    if start_time is None:
        return True
    try:
        event_dt = datetime.fromisoformat(timestamp.replace("Z", "+00:00"))
    except ValueError:
        return True
    return event_dt >= start_time


def _recent_session_files(workspace_root: Path, start_time: datetime | None) -> list[Path]:
    history_dir = workspace_root / ".specstory" / "history"
    if not history_dir.exists():
        return []
    candidates = sorted(history_dir.glob("*.md"), key=lambda item: item.stat().st_mtime, reverse=True)
    if start_time is None:
        return candidates[:2]
    results: list[Path] = []
    for item in candidates:
        modified = datetime.fromtimestamp(item.stat().st_mtime, tz=timezone.utc)
        if modified >= start_time:
            results.append(item)
        if len(results) >= 3:
            break
    return results or candidates[:1]


def _extract_first_user_message(content: str) -> str:
    lines = content.splitlines()
    for index, line in enumerate(lines):
        if line.strip() != "_**User**_":
            continue
        collected: list[str] = []
        for candidate in lines[index + 1 : index + 12]:
            stripped = candidate.strip()
            if not stripped or stripped == "---":
                if collected:
                    break
                continue
            if stripped.startswith("_**"):
                break
            collected.append(stripped)
        if collected:
            return " ".join(collected)[:500]
    return ""


def _count_terms(content: str, terms: list[str]) -> int:
    return sum(content.count(term.lower()) for term in terms)


def _git_commit_count_since(workspace_root: Path, start_time: datetime | None) -> int:
    if not (workspace_root / ".git").exists():
        return 0
    cmd = ["git", "log", "--oneline"]
    if start_time:
        cmd.extend(["--since", start_time.strftime("%Y-%m-%d %H:%M:%S")])
    completed = subprocess.run(
        cmd,
        cwd=workspace_root,
        capture_output=True,
        text=True,
        check=False,
    )
    if completed.returncode != 0:
        return 0
    return sum(1 for line in completed.stdout.splitlines() if line.strip())
