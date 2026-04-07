#!/usr/bin/env python3
"""
Claude Session Launcher — browse and resume past sessions.

Usage:
    python3 launcher.py          # interactive session board
    python3 launcher.py --list   # print session list without prompting

Add to shell:
    alias csession='python3 ~/SNOW-Work/"🔧 Automation"/scripts/launcher.py'
"""

from __future__ import annotations

import json
import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path


# Derived from script location: scripts/ → Automation/ → workspace root
WORKSPACE = Path(__file__).parent.parent.parent
SESSIONS_DIR = WORKSPACE / "🤖 AI" / "memory" / "sessions"
CLAUDE_BIN = Path.home() / ".local" / "bin" / "claude"
CLAUDE_PROJECTS_DIR = Path.home() / ".claude" / "projects"

# ANSI colors (degrade gracefully if terminal doesn't support them)
BOLD = "\033[1m"
DIM = "\033[2m"
CYAN = "\033[36m"
YELLOW = "\033[33m"
RESET = "\033[0m"
WIDTH = 68


def _no_color() -> bool:
    return not sys.stdout.isatty() or os.environ.get("NO_COLOR")


def _b(s: str) -> str:
    return s if _no_color() else f"{BOLD}{s}{RESET}"


def _dim(s: str) -> str:
    return s if _no_color() else f"{DIM}{s}{RESET}"


def _cyan(s: str) -> str:
    return s if _no_color() else f"{CYAN}{s}{RESET}"


def _yellow(s: str) -> str:
    return s if _no_color() else f"{YELLOW}{s}{RESET}"


def _claude_project_dir(workspace: Path) -> Path:
    key = str(workspace).replace("/", "-")
    return CLAUDE_PROJECTS_DIR / key


def parse_session_file(path: Path) -> dict:
    """Parse frontmatter and sections from a session markdown file.

    Handles both strict YAML frontmatter and the looser format where
    key: value pairs appear between --- markers with optional blank lines
    and ## prefixes (e.g., '## date: 2026-04-07').
    """
    text = path.read_text(encoding="utf-8")

    meta: dict[str, str] = {}
    # Extract the block between the two --- delimiters
    fm = re.search(r"^---\s*\n(.*?)\n---", text, re.DOTALL | re.MULTILINE)
    block = fm.group(1) if fm else text[:500]
    for line in block.splitlines():
        # Strip optional ## prefix (legacy format)
        line = re.sub(r"^##\s*", "", line).strip()
        if ":" in line and not line.startswith("#"):
            k, _, v = line.partition(":")
            meta[k.strip()] = v.strip()

    def section(name: str) -> str:
        m = re.search(rf"## {re.escape(name)}\s*\n(.*?)(?=\n## |\Z)", text, re.DOTALL)
        return m.group(1).strip() if m else ""

    return {
        "path": path,
        "date": meta.get("date", ""),
        "claude_session_id": meta.get("claude_session_id", ""),
        "start_time": meta.get("start_time", ""),
        "summary": section("Summary"),
        "focus": section("Focus"),
        "open_questions": section("Open Questions"),
        "decisions": section("Decisions"),
    }


def _resolve_uuid_by_timestamp(session: dict, proj_dir: Path) -> str | None:
    """Fallback: match JSONL by finding the largest file modified between
    start_time and start_time + 8 hours.

    Largest file heuristic: a meaningful session produces more JSONL content than
    stub sessions, so the biggest file in the window is the most likely match.
    The most recently modified JSONL is excluded (assumed to be the active session).
    """
    start_str = session.get("start_time", "")
    if not start_str:
        return None
    try:
        start_dt = datetime.fromisoformat(start_str.replace("Z", "+00:00"))
    except ValueError:
        return None

    start_ts = start_dt.timestamp()
    end_ts = start_ts + 8 * 3600

    all_files = list(proj_dir.glob("*.jsonl"))
    if not all_files:
        return None

    # Exclude the most recently modified JSONL (likely the active session)
    most_recent = max(all_files, key=lambda f: f.stat().st_mtime)

    candidates = []
    for jf in all_files:
        if jf == most_recent:
            continue
        st = jf.stat()
        if start_ts <= st.st_mtime <= end_ts:
            candidates.append((st.st_size, jf.stem))

    if not candidates:
        return None

    # Largest file in the window = most content = most likely the real session
    candidates.sort(reverse=True)
    return candidates[0][1]


def find_resume_uuid(session: dict, proj_dir: Path) -> str | None:
    """Return the JSONL UUID needed for `claude --resume`."""
    stored = session.get("claude_session_id", "").strip()
    if stored:
        if (proj_dir / f"{stored}.jsonl").exists():
            return stored

    return _resolve_uuid_by_timestamp(session, proj_dir)


def format_card(n: int, session: dict, uuid: str | None) -> str:
    date_str = session["date"] or "Unknown date"
    summary = (session["summary"] or "No summary")[:WIDTH - 4]
    focus = (session["focus"] or "")[:WIDTH - 6]

    first_question = ""
    oq_text = session.get("open_questions", "")
    if oq_text:
        first_line = oq_text.split("\n")[0].lstrip("- ").strip()
        if first_line:
            first_question = first_line[:WIDTH - 8]

    sep = "─" * WIDTH
    lines = [
        sep,
        f"{_b(f'[{n}]')} {_cyan(date_str)}",
        f"    {summary}",
    ]
    if focus and focus != "Not captured.":
        lines.append(f"    {_dim('📍')} {_dim(focus)}")
    if first_question:
        lines.append(f"    {_yellow('❓')} {_dim(first_question)}")
    if uuid:
        lines.append(f"    {_dim(f'→ claude --resume {uuid}')}")
    else:
        lines.append(f"    {_dim('→ (no resume ID — run a session first)')}")

    return "\n".join(lines)


def load_sessions(proj_dir: Path, limit: int = 20) -> list[tuple[dict, str | None]]:
    if not SESSIONS_DIR.exists():
        return []
    files = sorted(SESSIONS_DIR.glob("*.md"), reverse=True)[:limit]
    result = []
    for f in files:
        try:
            s = parse_session_file(f)
            uuid = find_resume_uuid(s, proj_dir)
            result.append((s, uuid))
        except Exception:
            continue
    return result


def run_resume(uuid: str, summary: str) -> None:
    claude = str(CLAUDE_BIN) if CLAUDE_BIN.exists() else "claude"
    print(f"\n  Resuming: {summary[:60]}\n")
    os.chdir(WORKSPACE)
    os.execvp(claude, [claude, "--resume", uuid])


def main() -> int:
    proj_dir = _claude_project_dir(WORKSPACE)
    sessions = load_sessions(proj_dir)

    if not sessions:
        print("No sessions found. Sessions are written at the end of each Claude Code session.")
        return 1

    print(f"\n  {_b('Claude Session Launcher')}  {_dim(str(WORKSPACE.name))}\n")
    for i, (s, uuid) in enumerate(sessions, 1):
        print(format_card(i, s, uuid))
    print("─" * WIDTH)

    if "--list" in sys.argv:
        return 0

    try:
        choice = input(f"\n  {_dim('Enter number to resume (q to quit):')} ").strip()
    except (KeyboardInterrupt, EOFError):
        print()
        return 0

    if choice.lower() in ("q", ""):
        return 0

    try:
        idx = int(choice) - 1
    except ValueError:
        print("  Invalid input.")
        return 1

    if not (0 <= idx < len(sessions)):
        print("  Invalid selection.")
        return 1

    session, uuid = sessions[idx]

    if not uuid:
        print("  No resume ID found for this session.")
        return 1

    run_resume(uuid, session["summary"])
    return 0  # unreachable after execvp


if __name__ == "__main__":
    raise SystemExit(main())
