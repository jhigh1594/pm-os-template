"""CLI entrypoint for skill learning automation."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from .pipeline import run_nightly_cycle, run_weekly_cycle
from .runtime import bootstrap_skill_learning, ingest_session_runs


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Workspace skill learning tools")
    parser.add_argument("--workspace", type=Path, default=Path.cwd(), help="Workspace root")
    subparsers = parser.add_subparsers(dest="command", required=True)

    bootstrap = subparsers.add_parser("bootstrap", help="Create registry and LEARNED.md files")
    bootstrap.add_argument("--augment-skill-files", action="store_true", help="Append the standard self-learning section to SKILL.md files")

    subparsers.add_parser("ingest-session", help="Persist skill runs observed in the current session")
    subparsers.add_parser("nightly", help="Run nightly evaluation and candidate generation")
    subparsers.add_parser("weekly", help="Run weekly evaluation and proposal generation")

    args = parser.parse_args(argv)
    workspace = args.workspace.resolve()

    if args.command == "bootstrap":
        result = bootstrap_skill_learning(workspace, augment_skill_files=args.augment_skill_files)
    elif args.command == "ingest-session":
        result = [item.to_dict() for item in ingest_session_runs(workspace)]
    elif args.command == "nightly":
        result = run_nightly_cycle(workspace)
    else:
        result = run_weekly_cycle(workspace)

    print(json.dumps(result, indent=2, default=str))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
