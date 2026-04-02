"""Data models for the skill learning system."""

from __future__ import annotations

from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from typing import Any, Dict, List


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


@dataclass
class RegistrySkillEntry:
    skill_id: str
    base_skill_id: str
    name: str
    surface: str
    family: str
    owner: str
    criticality: str
    eval_policy: str
    skill_path: str
    learned_path: str
    wrappers: List[str] = field(default_factory=list)
    pilot: bool = False

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "RegistrySkillEntry":
        return cls(
            skill_id=data["skill_id"],
            base_skill_id=data.get("base_skill_id", data["skill_id"]),
            name=data["name"],
            surface=data["surface"],
            family=data["family"],
            owner=data["owner"],
            criticality=data["criticality"],
            eval_policy=data["eval_policy"],
            skill_path=data["skill_path"],
            learned_path=data["learned_path"],
            wrappers=list(data.get("wrappers", [])),
            pilot=bool(data.get("pilot", False)),
        )


@dataclass
class RegistryWrapperEntry:
    wrapper_id: str
    command_name: str
    path: str
    surface: str
    delegates_to: str
    family: str
    criticality: str

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "RegistryWrapperEntry":
        return cls(
            wrapper_id=data["wrapper_id"],
            command_name=data["command_name"],
            path=data["path"],
            surface=data["surface"],
            delegates_to=data["delegates_to"],
            family=data["family"],
            criticality=data["criticality"],
        )


@dataclass
class SkillRunRecord:
    run_id: str
    skill_id: str
    skill_name: str
    surface: str
    family: str
    version_hash: str
    instruction_path: str
    wrapper_command: str = ""
    source: str = "instructions_loaded"
    session_id: str = ""
    timestamp: str = field(default_factory=utc_now_iso)
    user_ask: str = ""
    outcome_signals: List[str] = field(default_factory=list)
    tool_errors: List[str] = field(default_factory=list)
    retry_count: int = 0
    user_correction_count: int = 0
    positive_reinforcement_count: int = 0
    success_confidence: str = "low"
    evidence_paths: List[str] = field(default_factory=list)
    metadata: Dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class SkillEvalCase:
    case_id: str
    family: str
    prompt: str
    expectations: List[str]
    holdout: bool = False

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class SkillEvalResult:
    evaluation_id: str
    skill_id: str
    family: str
    version_hash: str
    run_id: str = ""
    aggregate_score: float = 0.0
    dimension_scores: List[Dict[str, Any]] = field(default_factory=list)
    critical_regressions: List[str] = field(default_factory=list)
    holdout_passed: bool = True
    recommended_action: str = "no_change"
    summary: str = ""
    human_summary: str = ""
    machine_scorecard: Dict[str, Any] = field(default_factory=dict)
    created_at: str = field(default_factory=utc_now_iso)

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class SkillLearningCandidate:
    candidate_id: str
    skill_id: str
    lesson: str
    action: str
    confidence: float
    severity: str
    source_run_ids: List[str] = field(default_factory=list)
    signals: List[str] = field(default_factory=list)
    evidence_count: int = 0
    status: str = "candidate"
    reusable: bool = True
    first_seen: str = field(default_factory=utc_now_iso)
    last_seen: str = field(default_factory=utc_now_iso)

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class SkillRevisionProposal:
    proposal_id: str
    skill_id: str
    proposal_type: str
    recommendation: str
    current_version_hash: str
    score_delta: float = 0.0
    failure_modes: List[str] = field(default_factory=list)
    critical_regressions: List[str] = field(default_factory=list)
    learned_updates: List[str] = field(default_factory=list)
    review_queue_path: str = ""
    status: str = "pending_review"
    created_at: str = field(default_factory=utc_now_iso)

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class LearningEntry:
    observed_on: str
    lesson: str
    reinforced: int = 1

    def to_line(self) -> str:
        return f"- {self.observed_on} | reinforced={self.reinforced} | {self.lesson}"
