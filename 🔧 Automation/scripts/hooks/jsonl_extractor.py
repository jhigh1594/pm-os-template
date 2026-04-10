#!/usr/bin/env python3
"""
JSONL Session Extractor — retroactively extracts summaries from Claude Code sessions
that ended via terminal close (SIGHUP) and never triggered the Stop hook.

Called at session start, runs in background, processes up to --max-sessions
recent JSONL files that don't yet have a session MD summary.

Usage:
    python3 jsonl_extractor.py --workspace /path/to/workspace [--max-sessions 3]
"""

from __future__ import annotations

import argparse
import fcntl
import json
import re
import subprocess
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path

CLAUDE_BIN = Path.home() / ".local" / "bin" / "claude"
SESSIONS_DIR_NAME = "sessions"
MIN_JSONL_BYTES = 40_000   # ignore hook-only stubs
MAX_TRANSCRIPT_CHARS = 8000

EXTRACTION_PROMPT = """You are extracting session context from a Claude Code AI assistant conversation.

Read the conversation transcript below and extract the following as JSON. Be concise and specific.

Output ONLY valid JSON, no other text:

{
  "session_summary": "One sentence describing what happened this session",
  "current_focus": "What the user is currently working on (1-2 sentences, present tense)",
  "key_decisions": ["Decision made", "Another decision"],
  "open_questions": ["Unresolved question or blocker"],
  "context_changes": "Any important context shifts worth noting (or empty string if none)"
}

Rules:
- current_focus should reflect the end state, not just what was discussed
- key_decisions only includes decisions that affect future work
- open_questions only includes genuinely unresolved items
- Do not fabricate information not present in the transcript

TRANSCRIPT:
"""

_SKIP_PREFIXES = ("<local-command-caveat>", "<command-", "<system-reminder>")


def _build_transcript(jsonl_path: Path) -> str:
    """Build a readable USER/ASSISTANT transcript from a JSONL file."""
    segments: list[str] = []
    try:
        for raw in jsonl_path.read_text(encoding="utf-8", errors="ignore").splitlines():
            obj = json.loads(raw)
            kind = obj.get("type")

            if kind == "user":
                content = obj.get("message", {}).get("content", "")
                text = ""
                if isinstance(content, list):
                    for c in content:
                        if isinstance(c, dict) and c.get("type") == "text":
                            text = c["text"].strip()
                            break
                elif isinstance(content, str):
                    text = content.strip()
                if text and not any(text.startswith(p) for p in _SKIP_PREFIXES):
                    segments.append(f"USER: {text[:600]}")

            elif kind == "assistant":
                content = obj.get("message", {}).get("content", "")
                text = ""
                if isinstance(content, list):
                    for c in content:
                        if isinstance(c, dict) and c.get("type") == "text":
                            text = c["text"].strip()
                            break
                elif isinstance(content, str):
                    text = content.strip()
                if text:
                    segments.append(f"ASSISTANT: {text[:400]}")

    except Exception:
        pass

    full = "\n\n".join(segments)
    if len(full) <= MAX_TRANSCRIPT_CHARS:
        return full
    # Keep opening context + recent tail
    return full[:2000] + "\n\n[...]\n\n" + full[-(MAX_TRANSCRIPT_CHARS - 2000):]


def _first_message_date(jsonl_path: Path) -> str:
    """Return YYYY-MM-DD of the first user message, or today."""
    try:
        for raw in jsonl_path.read_text(encoding="utf-8", errors="ignore").splitlines()[:20]:
            obj = json.loads(raw)
            if obj.get("type") == "user":
                ts = obj.get("timestamp", "")
                if ts:
                    dt = datetime.fromisoformat(ts.replace("Z", "+00:00"))
                    return dt.strftime("%Y-%m-%d")
    except Exception:
        pass
    return datetime.now(timezone.utc).strftime("%Y-%m-%d")


def _already_extracted(uuid: str, sessions_dir: Path) -> bool:
    for f in sessions_dir.glob("*.md"):
        try:
            if f"claude_session_id: {uuid}" in f.read_text(encoding="utf-8", errors="ignore"):
                return True
        except Exception:
            pass
    return False


def _call_haiku(transcript: str) -> dict | None:
    if not CLAUDE_BIN.exists():
        return None
    prompt = EXTRACTION_PROMPT + transcript
    try:
        result = subprocess.run(
            [str(CLAUDE_BIN), "-p", prompt, "--model", "claude-haiku-4-5-20251001",
             "--no-session-persistence"],
            capture_output=True, text=True, timeout=90,
        )
    except Exception:
        return None
    if result.returncode != 0:
        return None
    raw = result.stdout.strip()
    raw = re.sub(r"^```(?:json)?\s*", "", raw, flags=re.MULTILINE)
    raw = re.sub(r"```\s*$", "", raw, flags=re.MULTILINE).strip()
    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        return None


def _write_session_file(uuid: str, date: str, facts: dict, sessions_dir: Path) -> bool:
    now = datetime.now(timezone.utc)
    # Avoid filename collision
    base = now.strftime("%Y-%m-%d-%H%MZ")
    candidate = sessions_dir / f"{base}.md"
    counter = 1
    while candidate.exists():
        candidate = sessions_dir / f"{base}-{counter}.md"
        counter += 1

    decisions = facts.get("key_decisions", [])
    questions = facts.get("open_questions", [])
    context_changes = facts.get("context_changes", "")
    summary = facts.get("session_summary", "Session recorded.")
    focus = facts.get("current_focus", "")

    lines = [
        "---",
        f"date: {date}",
        f"claude_session_id: {uuid}",
        "start_time: ",
        "transcript: ",
        "---",
        "",
        "## Summary",
        summary,
        "",
        "## Focus",
        focus or "Not captured.",
        "",
    ]
    if decisions:
        lines += ["## Decisions"] + [f"- {d}" for d in decisions] + [""]
    if questions:
        lines += ["## Open Questions"] + [f"- {q}" for q in questions] + [""]
    if context_changes:
        lines += ["## Context Changes", context_changes, ""]

    try:
        candidate.write_text("\n".join(lines), encoding="utf-8")
        return True
    except Exception:
        return False


def extract_session(jsonl_path: Path, sessions_dir: Path) -> bool:
    uuid = jsonl_path.stem
    if _already_extracted(uuid, sessions_dir):
        return False
    transcript = _build_transcript(jsonl_path)
    if len(transcript) < 300:
        return False
    facts = _call_haiku(transcript)
    if not facts:
        return False
    date = _first_message_date(jsonl_path)
    return _write_session_file(uuid, date, facts, sessions_dir)


def main() -> int:
    # Prevent concurrent instances — if another copy is still running, bail out.
    lock_path = Path(tempfile.gettempdir()) / "jsonl_extractor.lock"
    lock_fd = open(lock_path, "w")
    try:
        fcntl.flock(lock_fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
    except OSError:
        return 0  # Another instance is running; skip silently.

    parser = argparse.ArgumentParser()
    parser.add_argument("--workspace", type=Path, default=Path.cwd())
    parser.add_argument("--max-sessions", type=int, default=3)
    args = parser.parse_args(sys.argv[1:])

    workspace = args.workspace.resolve()
    proj_key = str(workspace).replace("/", "-")
    proj_dir = Path.home() / ".claude" / "projects" / proj_key
    sessions_dir = workspace / "🤖 AI" / "memory" / "sessions"
    sessions_dir.mkdir(parents=True, exist_ok=True)

    if not proj_dir.exists():
        return 0

    all_jsonl = sorted(proj_dir.glob("*.jsonl"), key=lambda f: f.stat().st_mtime, reverse=True)
    # Skip the active session (most recent)
    candidates = [
        f for f in all_jsonl[1:]
        if f.stat().st_size >= MIN_JSONL_BYTES
        and not _already_extracted(f.stem, sessions_dir)
    ][:args.max_sessions]

    for jf in candidates:
        if extract_session(jf, sessions_dir):
            sys.stderr.write(f"jsonl_extractor: extracted {jf.stem[:8]}...\n")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
