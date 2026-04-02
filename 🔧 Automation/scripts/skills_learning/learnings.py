"""Per-skill LEARNED.md maintenance."""

from __future__ import annotations

import re
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Iterable, List

from .models import LearningEntry

ENTRY_PATTERN = re.compile(r"^- (\d{4}-\d{2}-\d{2}) \| reinforced=(\d+) \| (.+)$")


def ensure_learned_file(path: Path, header_lines: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists():
        return
    text = "\n".join(header_lines).rstrip() + "\n"
    path.write_text(text, encoding="utf-8")


def parse_learned_file(path: Path) -> List[LearningEntry]:
    if not path.exists():
        return []
    entries: List[LearningEntry] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        match = ENTRY_PATTERN.match(line.strip())
        if not match:
            continue
        entries.append(
            LearningEntry(
                observed_on=match.group(1),
                reinforced=int(match.group(2)),
                lesson=match.group(3),
            )
        )
    return entries


def prune_entries(
    entries: Iterable[LearningEntry],
    retention_days: int,
    max_entries: int,
) -> List[LearningEntry]:
    cutoff = (datetime.now(timezone.utc) - timedelta(days=retention_days)).date()
    kept: List[LearningEntry] = []
    for entry in entries:
        try:
            observed = datetime.strptime(entry.observed_on, "%Y-%m-%d").date()
        except ValueError:
            observed = cutoff
        if observed < cutoff and entry.reinforced < 2:
            continue
        kept.append(entry)
    kept.sort(key=lambda item: (item.observed_on, item.reinforced, item.lesson), reverse=True)
    return kept[:max_entries]


def upsert_learning(
    path: Path,
    header_lines: list[str],
    lesson: str,
    retention_days: int,
    max_entries: int,
) -> List[LearningEntry]:
    ensure_learned_file(path, header_lines)
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    existing = parse_learned_file(path)
    updated = False
    for entry in existing:
        if entry.lesson == lesson:
            entry.reinforced += 1
            entry.observed_on = today
            updated = True
            break
    if not updated:
        existing.append(LearningEntry(observed_on=today, lesson=lesson, reinforced=1))

    pruned = prune_entries(existing, retention_days=retention_days, max_entries=max_entries)
    lines = header_lines[:]
    lines.extend(entry.to_line() for entry in pruned)
    path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    return pruned
