"""Minimal ObserverManager stub for pm-os-template.

The full observer system (used in Planview Work) records skill run events to
a structured database. This stub satisfies the import so skills_learning works
without the full observer infrastructure — get_observer() returns None, which
the skills_learning module checks before calling any observer methods.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any


class ObserverManager:
    async def initialize(self, workspace_root: Path, config_path: str) -> None:
        pass

    def get_observer(self, name: str) -> None:
        return None
