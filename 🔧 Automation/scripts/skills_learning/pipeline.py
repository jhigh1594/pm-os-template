"""Nightly and weekly skill-learning cycles."""

from __future__ import annotations

import uuid
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import yaml

from observers.observer_manager import ObserverManager

from .learnings import upsert_learning
from .models import SkillEvalResult, SkillLearningCandidate, SkillRevisionProposal
from .registry import iter_skill_entries, load_learning_config, load_registry
from .runtime import learning_paths
from .store import JsonlStore


def run_nightly_cycle(workspace_root: Path) -> dict[str, Any]:
    eval_results = evaluate_observed_runs(workspace_root)
    candidates = generate_learning_candidates(workspace_root, eval_results)
    accepted = apply_runtime_learnings(workspace_root, candidates)
    return {
        "evaluations": len(eval_results),
        "candidates": len(candidates),
        "accepted_learnings": accepted,
    }


def run_weekly_cycle(workspace_root: Path) -> dict[str, Any]:
    eval_results = evaluate_observed_runs(workspace_root)
    candidates = generate_learning_candidates(workspace_root, eval_results)
    proposals = generate_revision_proposals(workspace_root, eval_results, candidates)
    report_path = write_weekly_report(workspace_root, eval_results, candidates, proposals)
    return {
        "evaluations": len(eval_results),
        "candidates": len(candidates),
        "proposals": len(proposals),
        "report_path": str(report_path),
    }


def evaluate_observed_runs(workspace_root: Path) -> list[SkillEvalResult]:
    workspace_root = Path(workspace_root)
    registry = load_registry(workspace_root)
    skill_map = {entry.skill_id: entry for entry in iter_skill_entries(registry)}
    paths = learning_paths(workspace_root)
    runs = JsonlStore(paths["runs"]).load()
    existing = JsonlStore(paths["eval_results"]).load()
    seen_run_ids = {item.get("run_id") for item in existing if item.get("run_id")}
    results: list[SkillEvalResult] = []

    for run in runs:
        if run.get("run_id") in seen_run_ids:
            continue
        entry = skill_map.get(run["skill_id"])
        if not entry:
            continue
        rubric = _load_rubric(workspace_root, entry.family)
        result = _score_run(run, entry.family, rubric)
        JsonlStore(paths["eval_results"]).append(result.to_dict())
        _record_observer_event(
            workspace_root,
            "skill_eval",
            {
                "skill_id": result.skill_id,
                "family": result.family,
                "version_hash": result.version_hash,
                "aggregate_score": result.aggregate_score,
                "recommended_action": result.recommended_action,
                "holdout_passed": result.holdout_passed,
                "critical_regressions": result.critical_regressions,
            },
        )
        results.append(result)
    return results


def generate_learning_candidates(
    workspace_root: Path,
    eval_results: list[SkillEvalResult] | None = None,
) -> list[SkillLearningCandidate]:
    workspace_root = Path(workspace_root)
    config = load_learning_config(workspace_root)
    registry = load_registry(workspace_root)
    skill_map = {entry.skill_id: entry for entry in iter_skill_entries(registry)}
    runs = JsonlStore(learning_paths(workspace_root)["runs"]).load()
    existing_records = JsonlStore(learning_paths(workspace_root)["candidates"]).load()
    existing = {(item.get("skill_id"), item.get("lesson")) for item in existing_records}

    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for run in runs:
        grouped[run["skill_id"]].append(run)

    candidates: list[SkillLearningCandidate] = []
    min_runs = config.get("evaluation", {}).get("min_runs_for_candidate", 2)
    for skill_id, skill_runs in grouped.items():
        if len(skill_runs) < min_runs:
            continue
        signal_counts: Counter[str] = Counter()
        run_ids: list[str] = []
        for run in skill_runs:
            signal_counts.update(run.get("outcome_signals", []))
            run_ids.append(run["run_id"])
        dominant_signal, count = signal_counts.most_common(1)[0]
        entry = skill_map.get(skill_id)
        lesson, action, severity, confidence = _candidate_for_signal(entry.family if entry else "consultative", dominant_signal, count)
        if not lesson or (skill_id, lesson) in existing:
            continue
        candidate = SkillLearningCandidate(
            candidate_id=str(uuid.uuid4()),
            skill_id=skill_id,
            lesson=lesson,
            action=action,
            confidence=confidence,
            severity=severity,
            source_run_ids=run_ids[-5:],
            signals=[dominant_signal],
            evidence_count=count,
        )
        JsonlStore(learning_paths(workspace_root)["candidates"]).append(candidate.to_dict())
        _record_observer_event(
            workspace_root,
            "skill_learning_candidate",
            {
                "skill_id": candidate.skill_id,
                "lesson": candidate.lesson,
                "action": candidate.action,
                "confidence": candidate.confidence,
                "severity": candidate.severity,
                "status": candidate.status,
            },
        )
        candidates.append(candidate)
    return candidates


def apply_runtime_learnings(workspace_root: Path, candidates: list[SkillLearningCandidate]) -> int:
    workspace_root = Path(workspace_root)
    config = load_learning_config(workspace_root)
    registry = load_registry(workspace_root)
    skill_map = {entry.skill_id: entry for entry in iter_skill_entries(registry)}
    accepted = 0
    for candidate in candidates:
        if candidate.action != "LEARNED-only":
            continue
        if candidate.evidence_count < config.get("learnings", {}).get("min_reinforcement_count", 2):
            continue
        if candidate.confidence < config.get("evaluation", {}).get("min_candidate_confidence", 0.55):
            continue
        skill_entry = skill_map.get(candidate.skill_id)
        if not skill_entry:
            continue
        upsert_learning(
            workspace_root / skill_entry.learned_path,
            header_lines=config.get("learnings", {}).get("header_lines", ["# Learned"]),
            lesson=candidate.lesson,
            retention_days=config.get("learnings", {}).get("retention_days", 90),
            max_entries=config.get("learnings", {}).get("max_entries", 40),
        )
        candidate.status = "accepted"
        accepted += 1
    return accepted


def generate_revision_proposals(
    workspace_root: Path,
    eval_results: list[SkillEvalResult],
    candidates: list[SkillLearningCandidate],
) -> list[SkillRevisionProposal]:
    workspace_root = Path(workspace_root)
    registry = load_registry(workspace_root)
    skill_map = {entry.skill_id: entry for entry in iter_skill_entries(registry)}
    results_by_skill: dict[str, list[SkillEvalResult]] = defaultdict(list)
    for item in JsonlStore(learning_paths(workspace_root)["eval_results"]).load():
        results_by_skill[item["skill_id"]].append(
            SkillEvalResult(
                evaluation_id=item["evaluation_id"],
                skill_id=item["skill_id"],
                family=item["family"],
                version_hash=item["version_hash"],
                run_id=item.get("run_id", ""),
                aggregate_score=float(item["aggregate_score"]),
                dimension_scores=list(item.get("dimension_scores", [])),
                critical_regressions=list(item.get("critical_regressions", [])),
                holdout_passed=bool(item.get("holdout_passed", True)),
                recommended_action=item.get("recommended_action", "no_change"),
                summary=item.get("summary", ""),
                human_summary=item.get("human_summary", ""),
                machine_scorecard=dict(item.get("machine_scorecard", {})),
                created_at=item.get("created_at", ""),
            )
        )

    candidates_by_skill: dict[str, list[SkillLearningCandidate]] = defaultdict(list)
    for candidate in candidates:
        candidates_by_skill[candidate.skill_id].append(candidate)

    proposals: list[SkillRevisionProposal] = []
    review_queue = learning_paths(workspace_root)["review_queue"]
    review_queue.mkdir(parents=True, exist_ok=True)
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    for skill_id, entry in skill_map.items():
        results = results_by_skill.get(skill_id, [])
        latest = results[-1] if results else None
        previous = results[-2] if len(results) > 1 else None
        if not latest:
            continue
        score_delta = round(latest.aggregate_score - previous.aggregate_score, 2) if previous else 0.0
        candidate_lessons = [item.lesson for item in candidates_by_skill.get(skill_id, [])]

        if latest.critical_regressions:
            proposal_type = "SKILL.md rewrite"
            recommendation = "Investigate the critical regression before promoting new learnings."
        elif latest.aggregate_score < 3.3:
            proposal_type = "SKILL.md rewrite"
            recommendation = "The skill is under-performing on observed runs; revise the core instructions."
        elif not latest.holdout_passed:
            proposal_type = "eval expansion"
            recommendation = "Expand holdout coverage before trusting broader instruction changes."
        elif candidate_lessons:
            proposal_type = "LEARNED-only"
            recommendation = "Promote the accepted runtime lessons and monitor the next cycle."
        else:
            proposal_type = "no change"
            recommendation = "Keep monitoring; observed runs do not justify an instruction rewrite yet."

        proposal = SkillRevisionProposal(
            proposal_id=str(uuid.uuid4()),
            skill_id=skill_id,
            proposal_type=proposal_type,
            recommendation=recommendation,
            current_version_hash=latest.version_hash,
            score_delta=score_delta,
            failure_modes=_top_failure_modes(latest),
            critical_regressions=latest.critical_regressions,
            learned_updates=candidate_lessons,
        )
        proposal.review_queue_path = str((review_queue / f"{today}-{skill_id}.md").relative_to(workspace_root))
        _write_review_queue_file(workspace_root, proposal, entry.skill_path, latest, previous)
        _record_observer_event(
            workspace_root,
            "skill_revision_proposal",
            {
                "skill_id": proposal.skill_id,
                "proposal_type": proposal.proposal_type,
                "recommendation": proposal.recommendation,
                "score_delta": proposal.score_delta,
                "review_queue_path": proposal.review_queue_path,
                "status": proposal.status,
            },
        )
        proposals.append(proposal)
    return proposals


def write_weekly_report(
    workspace_root: Path,
    eval_results: list[SkillEvalResult],
    candidates: list[SkillLearningCandidate],
    proposals: list[SkillRevisionProposal],
) -> Path:
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    path = learning_paths(workspace_root)["review_queue"] / f"{today}-weekly-maintainer-report.md"
    failing = sorted(eval_results, key=lambda item: item.aggregate_score)[:5]
    lines = [
        "# Weekly Skill Learning Report",
        "",
        f"- Generated: {datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')}",
        f"- Eval results: {len(eval_results)}",
        f"- Candidate lessons: {len(candidates)}",
        f"- Proposals: {len(proposals)}",
        "",
        "## Top failing skills",
    ]
    if failing:
        for item in failing:
            lines.append(f"- `{item.skill_id}` scored {item.aggregate_score}/5 -> {item.recommended_action}")
    else:
        lines.append("- None")
    lines.extend(["", "## Accepted or candidate learnings"])
    if candidates:
        for candidate in candidates[:10]:
            lines.append(f"- `{candidate.skill_id}`: {candidate.lesson} ({candidate.status})")
    else:
        lines.append("- None")
    lines.extend(["", "## Review queue"])
    if proposals:
        for proposal in proposals[:10]:
            lines.append(f"- `{proposal.skill_id}`: {proposal.proposal_type} -> {proposal.review_queue_path}")
    else:
        lines.append("- None")
    path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    return path


def _load_rubric(workspace_root: Path, family: str) -> dict[str, Any]:
    rubric_path = workspace_root / "🤖 AI" / "skills" / "rubrics" / f"{family}.yaml"
    return yaml.safe_load(rubric_path.read_text(encoding="utf-8")) or {}


def _score_run(run: dict[str, Any], family: str, rubric: dict[str, Any]) -> SkillEvalResult:
    dimensions = rubric.get("dimensions", [])
    signal_weights = rubric.get("signals", {})
    signal_counter = Counter(run.get("outcome_signals", []))
    base_score = 3.4
    dimension_scores = []
    critical_regressions: list[str] = []
    for dimension in dimensions:
        score = base_score
        for signal, count in signal_counter.items():
            score += signal_weights.get(signal, 0.0) * count
        min_score = rubric.get("scale", {}).get("min", 1.0)
        max_score = rubric.get("scale", {}).get("max", 5.0)
        score = max(min_score, min(max_score, round(score, 2)))
        evidence = f"Signals: {', '.join(run.get('outcome_signals', [])) or 'none'}"
        dimension_scores.append({"name": dimension["name"], "score": score, "evidence": evidence})
        if dimension.get("critical") and score < 2.7:
            critical_regressions.append(dimension["name"])

    weights_total = sum(item.get("weight", 1.0) for item in dimensions) or 1.0
    aggregate = round(
        sum(score["score"] * next(dim["weight"] for dim in dimensions if dim["name"] == score["name"]) for score in dimension_scores) / weights_total,
        2,
    )
    holdout_passed = not critical_regressions
    if critical_regressions:
        action = "SKILL.md rewrite"
    elif aggregate < 3.2:
        action = "LEARNED-only"
    else:
        action = "no_change"

    human_summary = (
        f"{run['skill_id']} scored {aggregate}/5 across {family} dimensions. "
        f"Signals observed: {', '.join(run.get('outcome_signals', [])) or 'none'}."
    )
    machine_scorecard = {
        "skill_id": run["skill_id"],
        "family": family,
        "aggregate_score": aggregate,
        "dimensions": dimension_scores,
        "signals": run.get("outcome_signals", []),
        "critical_regressions": critical_regressions,
    }
    return SkillEvalResult(
        evaluation_id=str(uuid.uuid4()),
        skill_id=run["skill_id"],
        family=family,
        version_hash=run["version_hash"],
        run_id=run["run_id"],
        aggregate_score=aggregate,
        dimension_scores=dimension_scores,
        critical_regressions=critical_regressions,
        holdout_passed=holdout_passed,
        recommended_action=action,
        summary=human_summary,
        human_summary=human_summary,
        machine_scorecard=machine_scorecard,
    )


def _candidate_for_signal(family: str, signal: str, count: int) -> tuple[str, str, str, float]:
    severity = "medium" if count >= 2 else "low"
    confidence = min(0.9, 0.4 + (count * 0.15))
    mapping = {
        ("consultative", "user_correction"): (
            "Clarify the decision or ambiguity before giving a substantive recommendation.",
            "LEARNED-only",
        ),
        ("consultative", "retry_loop"): (
            "After a weak first pass, switch to diagnosis mode and restate the constraint before continuing.",
            "LEARNED-only",
        ),
        ("template", "user_correction"): (
            "Keep outputs tightly aligned to the requested artifact structure instead of broadening scope.",
            "LEARNED-only",
        ),
        ("tool_execution", "tool_error"): (
            "Check prerequisites, auth, and required files before invoking external tooling.",
            "LEARNED-only",
        ),
        ("tool_execution", "retry_loop"): (
            "Do not loop on the same failing command; summarize the blocker and choose a safer recovery path.",
            "LEARNED-only",
        ),
        ("evaluator", "user_correction"): (
            "Keep scoring calibrated and tie every low score to concrete evidence from the artifact.",
            "LEARNED-only",
        ),
    }
    lesson, action = mapping.get((family, signal), ("", "no change"))
    if not lesson:
        return "", "no change", severity, confidence
    if signal in {"tool_error", "user_correction"} and count >= 3:
        severity = "high"
    return lesson, action, severity, confidence


def _top_failure_modes(result: SkillEvalResult) -> list[str]:
    return [item["name"] for item in result.dimension_scores if float(item["score"]) < 3.0][:3]


def _write_review_queue_file(
    workspace_root: Path,
    proposal: SkillRevisionProposal,
    skill_path: str,
    latest: SkillEvalResult,
    previous: SkillEvalResult | None,
) -> None:
    path = workspace_root / proposal.review_queue_path
    diff_summary = "No prior eval available." if previous is None else f"Score delta: {proposal.score_delta:+.2f}"
    lines = [
        f"# Review Proposal: {proposal.skill_id}",
        "",
        f"- Proposal type: `{proposal.proposal_type}`",
        f"- Recommendation: {proposal.recommendation}",
        f"- Skill path: `{skill_path}`",
        f"- Current version hash: `{proposal.current_version_hash}`",
        f"- {diff_summary}",
        "",
        "## Failure modes",
    ]
    if proposal.failure_modes:
        for item in proposal.failure_modes:
            lines.append(f"- {item}")
    else:
        lines.append("- None")
    lines.extend(["", "## Learned updates"])
    if proposal.learned_updates:
        for lesson in proposal.learned_updates:
            lines.append(f"- {lesson}")
    else:
        lines.append("- None")
    lines.extend(["", "## Latest eval summary", latest.human_summary, "", "## Classification", f"- `{proposal.proposal_type}`"])
    path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def _record_observer_event(workspace_root: Path, observer_name: str, payload: dict[str, Any]) -> None:
    manager = ObserverManager()

    async def _run() -> None:
        await manager.initialize(workspace_root, str(workspace_root / "🤖 AI" / "config.yaml"))
        observer = manager.get_observer(observer_name)
        if observer:
            await observer.observe_and_record(**payload)

    import asyncio

    asyncio.run(_run())
