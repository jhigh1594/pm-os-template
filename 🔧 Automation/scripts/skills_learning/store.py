"""Simple JSONL storage helpers for skill learning artifacts."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Callable, Iterable, List


class JsonlStore:
    """Append-only JSONL store with convenience readers."""

    def __init__(self, path: Path):
        self.path = Path(path)

    def append(self, record: dict[str, Any]) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        with self.path.open("a", encoding="utf-8") as handle:
            handle.write(json.dumps(record, sort_keys=True) + "\n")

    def load(self) -> List[dict[str, Any]]:
        if not self.path.exists():
            return []
        items: List[dict[str, Any]] = []
        for line in self.path.read_text(encoding="utf-8").splitlines():
            if not line.strip():
                continue
            try:
                items.append(json.loads(line))
            except json.JSONDecodeError:
                continue
        return items

    def filter(self, predicate: Callable[[dict[str, Any]], bool]) -> List[dict[str, Any]]:
        return [item for item in self.load() if predicate(item)]

    def overwrite(self, records: Iterable[dict[str, Any]]) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        lines = [json.dumps(record, sort_keys=True) for record in records]
        text = "\n".join(lines)
        if text:
            text += "\n"
        self.path.write_text(text, encoding="utf-8")
