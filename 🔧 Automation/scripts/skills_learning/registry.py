"""Registry discovery and classification for workspace-local skills."""

from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable

import yaml

from .models import RegistrySkillEntry, RegistryWrapperEntry


def load_learning_config(workspace_root: Path) -> dict[str, Any]:
    path = workspace_root / "🤖 AI" / "skills" / "learning-config.yaml"
    if not path.exists():
        return {}
    data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    return data


def surface_for_path(path: Path) -> str:
    parts = path.parts
    if ".claude" in parts:
        return "claude_skill"
    if ".codex" in parts:
        return "codex_skill"
    if ".agents" in parts:
        return "agents_skill"
    return "workspace_skill"


def surface_prefix(surface: str) -> str:
    mapping = {
        "claude_skill": "claude",
        "codex_skill": "codex",
        "agents_skill": "agents",
        "workspace_skill": "workspace",
    }
    return mapping.get(surface, surface.replace("_skill", ""))


def classify_family(skill_id: str, path: Path, config: dict[str, Any]) -> str:
    overrides = config.get("family_overrides", {})
    if skill_id in overrides:
        return overrides[skill_id]

    lower = f"{skill_id} {path.as_posix()}".lower()
    if any(token in lower for token in ["coach", "review", "critique"]):
        return "evaluator"
    if any(token in lower for token in ["proof", "deck", "imagegen", "qmd", "remotion"]):
        return "tool_execution"
    if any(token in lower for token in ["comms", "story", "okr", "launch", "positioning", "speaking"]):
        return "template"
    return "consultative"


def criticality_for_skill(skill_id: str, config: dict[str, Any]) -> str:
    overrides = config.get("criticality_overrides", {})
    if skill_id in overrides:
        return overrides[skill_id]
    if skill_id in set(config.get("pilots", [])):
        return "high"
    return "medium"


def eval_policy_for_family(family: str, criticality: str) -> str:
    if criticality == "high":
        return "nightly_plus_weekly"
    if family in {"tool_execution", "evaluator"}:
        return "nightly"
    return "hybrid"


def discover_skills(workspace_root: Path, config: dict[str, Any]) -> list[RegistrySkillEntry]:
    entries: list[RegistrySkillEntry] = []
    pilots = set(config.get("pilots", []))

    for root_value in config.get("skill_roots", []):
        root = workspace_root / root_value
        if not root.exists():
            continue
        for skill_path in sorted(root.glob("*/SKILL.md")):
            skill_id = skill_path.parent.name
            family = classify_family(skill_id, skill_path, config)
            criticality = criticality_for_skill(skill_id, config)
            entries.append(
                RegistrySkillEntry(
                    skill_id=skill_id,
                    base_skill_id=skill_id,
                    name=skill_id.replace("-", " "),
                    surface=surface_for_path(skill_path),
                    family=family,
                    owner=config.get("owners", {}).get("default", "workspace"),
                    criticality=criticality,
                    eval_policy=eval_policy_for_family(family, criticality),
                    skill_path=str(skill_path.relative_to(workspace_root)),
                    learned_path=str((skill_path.parent / "LEARNED.md").relative_to(workspace_root)),
                    pilot=skill_id in pilots,
                )
            )
    base_counts: dict[str, int] = {}
    for entry in entries:
        base_counts[entry.base_skill_id] = base_counts.get(entry.base_skill_id, 0) + 1
    for entry in entries:
        if base_counts.get(entry.base_skill_id, 0) > 1:
            entry.skill_id = f"{surface_prefix(entry.surface)}:{entry.base_skill_id}"
    return entries


def discover_wrappers(workspace_root: Path, config: dict[str, Any]) -> list[RegistryWrapperEntry]:
    wrappers: list[RegistryWrapperEntry] = []
    for wrapper_id, data in sorted(config.get("wrapper_overrides", {}).items()):
        path = workspace_root / data["path"]
        if not path.exists():
            continue
        wrappers.append(
            RegistryWrapperEntry(
                wrapper_id=wrapper_id,
                command_name=f"/{wrapper_id}",
                path=data["path"],
                surface=data.get("surface", "claude_command"),
                delegates_to=data["delegates_to"],
                family=data.get("family", "consultative"),
                criticality=data.get("criticality", "medium"),
            )
        )
    return wrappers


def resolve_delegate_skill_id(
    skills: list[RegistrySkillEntry],
    delegates_to: str,
    surface: str | None = None,
) -> str:
    exact = [item for item in skills if item.skill_id == delegates_to]
    if len(exact) == 1:
        return exact[0].skill_id

    base_matches = [item for item in skills if item.base_skill_id == delegates_to]
    if surface:
        surface_matches = [item for item in base_matches if item.surface == surface]
        if len(surface_matches) == 1:
            return surface_matches[0].skill_id
    if len(base_matches) == 1:
        return base_matches[0].skill_id
    return delegates_to


def build_registry(workspace_root: Path) -> dict[str, Any]:
    config = load_learning_config(workspace_root)
    skills = discover_skills(workspace_root, config)
    wrappers = discover_wrappers(workspace_root, config)
    for wrapper in wrappers:
        wrapper.delegates_to = resolve_delegate_skill_id(skills, wrapper.delegates_to)
    wrappers_by_skill: dict[str, list[str]] = {}
    for wrapper in wrappers:
        wrappers_by_skill.setdefault(wrapper.delegates_to, []).append(wrapper.command_name)
    for skill in skills:
        skill.wrappers = wrappers_by_skill.get(skill.skill_id, [])

    return {
        "version": 1,
        "generated_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "skills": [item.to_dict() for item in skills],
        "wrappers": [item.to_dict() for item in wrappers],
    }


def write_registry(workspace_root: Path, registry: dict[str, Any]) -> Path:
    path = workspace_root / "🤖 AI" / "skills" / "registry.yaml"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(yaml.safe_dump(registry, sort_keys=False), encoding="utf-8")
    return path


def load_registry(workspace_root: Path) -> dict[str, Any]:
    path = workspace_root / "🤖 AI" / "skills" / "registry.yaml"
    if not path.exists():
        registry = build_registry(workspace_root)
        write_registry(workspace_root, registry)
        return registry
    return yaml.safe_load(path.read_text(encoding="utf-8")) or {}


def iter_skill_entries(registry: dict[str, Any]) -> Iterable[RegistrySkillEntry]:
    for item in registry.get("skills", []):
        yield RegistrySkillEntry.from_dict(item)


def iter_wrapper_entries(registry: dict[str, Any]) -> Iterable[RegistryWrapperEntry]:
    for item in registry.get("wrappers", []):
        yield RegistryWrapperEntry.from_dict(item)
