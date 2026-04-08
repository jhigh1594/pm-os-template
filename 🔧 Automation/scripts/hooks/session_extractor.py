"""
Session Extractor — LLM-powered session summarization and memory update.

Runs at session end via session_end.py. Reads the latest .specstory transcript,
calls the claude CLI to extract key facts, then:
  1. Updates volatile sections of memory.md in-place
  2. Writes a session summary file to 🤖 AI/memory/sessions/
  3. Archives sessions beyond the rolling window of 10
"""

from __future__ import annotations

import json
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


CLAUDE_BIN = Path.home() / ".local" / "bin" / "claude"
SESSIONS_DIR_NAME = "sessions"
CLAUDE_PROJECTS_DIR = Path.home() / ".claude" / "projects"
ARCHIVE_DIR_NAME = "sessions-archive"
MAX_SESSIONS = 10
ARCHIVE_SUMMARIZE_THRESHOLD = 50
TRANSCRIPT_MAX_CHARS = 8000  # Keep prompt manageable

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
- If a field has no content, use empty string or empty array
- Do not fabricate information not present in the transcript

TRANSCRIPT:
"""


def find_claude_session_uuid(workspace: Path) -> str | None:
    """Find the JSONL UUID for the current session.

    At session end, the most recently modified JSONL in the Claude projects
    directory is the current session. Its stem equals the resume UUID.
    """
    key = str(workspace).replace("/", "-")
    proj_dir = CLAUDE_PROJECTS_DIR / key
    if not proj_dir.exists():
        return None
    files = sorted(proj_dir.glob("*.jsonl"), key=lambda f: f.stat().st_mtime, reverse=True)
    return files[0].stem if files else None


def find_session_transcript(workspace: Path, start_time: datetime | None) -> Path | None:
    """Find the most relevant .specstory transcript from this session."""
    history_dir = workspace / ".specstory" / "history"
    if not history_dir.exists():
        return None

    candidates = sorted(
        history_dir.glob("*.md"),
        key=lambda p: p.stat().st_mtime,
        reverse=True,
    )

    if not candidates:
        return None

    if start_time is None:
        return candidates[0]

    # Prefer files modified after session start
    for candidate in candidates:
        mtime = datetime.fromtimestamp(candidate.stat().st_mtime, tz=timezone.utc)
        if mtime >= start_time:
            return candidate

    return candidates[0]


def truncate_transcript(content: str) -> str:
    """Return a representative slice of the transcript for extraction."""
    if len(content) <= TRANSCRIPT_MAX_CHARS:
        return content
    # Take first 2000 chars (opening context) + last 6000 chars (recent work)
    return content[:2000] + "\n\n[... middle truncated ...]\n\n" + content[-(TRANSCRIPT_MAX_CHARS - 2000):]


def _no_hooks_env() -> dict[str, str]:
    """Return os.environ with all session-end guard flags disabled.

    Prevents recursive hook triggering when claude CLI is called from within
    a session_end hook — child claude sessions would otherwise fire SessionEnd
    again, re-running this script.
    """
    import os
    env = dict(os.environ)
    env["AIPMOS_SESSION_END_AUTO_MEMORY"] = "0"
    env["AIPMOS_SKILL_LEARNING_INGEST"] = "0"
    env["AIPMOS_SESSION_END_PATTERN_EXTRACT"] = "0"
    return env


def call_claude_extraction(transcript: str) -> dict[str, Any] | None:
    """Call claude CLI to extract session facts. Returns parsed dict or None."""
    if not CLAUDE_BIN.exists():
        sys.stderr.write("session_extractor: claude CLI not found at ~/.local/bin/claude\n")
        return None

    prompt = EXTRACTION_PROMPT + truncate_transcript(transcript)

    try:
        result = subprocess.run(
            [str(CLAUDE_BIN), "-p", prompt, "--model", "claude-haiku-4-5-20251001",
             "--no-session-persistence"],
            capture_output=True,
            text=True,
            timeout=60,
            env=_no_hooks_env(),
        )
    except (OSError, subprocess.TimeoutExpired) as exc:
        sys.stderr.write(f"session_extractor: claude CLI call failed: {exc}\n")
        return None

    if result.returncode != 0:
        sys.stderr.write(f"session_extractor: claude returned {result.returncode}\n")
        return None

    raw = result.stdout.strip()

    # Strip markdown code fences if present
    raw = re.sub(r"^```(?:json)?\s*", "", raw, flags=re.MULTILINE)
    raw = re.sub(r"```\s*$", "", raw, flags=re.MULTILINE)
    raw = raw.strip()

    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        sys.stderr.write(f"session_extractor: failed to parse JSON from claude output\n")
        return None


def patch_memory_md(workspace: Path, facts: dict[str, Any]) -> bool:
    """Update volatile sections of memory.md in-place."""
    memory_file = workspace / "🤖 AI" / "memory" / "memory.md"
    if not memory_file.exists():
        return False

    content = memory_file.read_text(encoding="utf-8")

    # Build replacement content for each volatile section
    current_focus = facts.get("current_focus", "").strip()
    key_decisions = facts.get("key_decisions", [])
    open_questions = facts.get("open_questions", [])
    context_changes = facts.get("context_changes", "").strip()

    # Patch ## Current Focus
    if current_focus:
        focus_body = f"\n{current_focus}\n"
        content = _replace_section(content, "Current Focus", focus_body)

    # Patch ## Active Decisions
    if key_decisions or open_questions:
        decisions_body = "\n**Strategic Questions**:\n\n"
        for q in (open_questions or []):
            decisions_body += f"- {q}\n"
        if not open_questions:
            decisions_body += "- None active.\n"
        decisions_body += "\n**Recent Decisions**:\n\n"
        for d in (key_decisions or []):
            decisions_body += f"- {d}\n"
        if not key_decisions:
            decisions_body += "- None recorded this session.\n"
        decisions_body += "\n"
        content = _replace_section(content, "Active Decisions", decisions_body)

    # Patch ## Known Gaps — append context_changes if present
    if context_changes:
        gaps_section = _get_section(content, "Known Gaps")
        if context_changes not in gaps_section:
            new_gaps = gaps_section.rstrip() + f"\n\n**Context Change**: {context_changes}\n"
            content = _replace_section(content, "Known Gaps", "\n" + new_gaps + "\n")

    # Update Last Updated timestamp
    today = datetime.now().strftime("%Y-%m-%d")
    content = re.sub(r"\*\*Last Updated\*\*:.*", f"**Last Updated**: {today}", content)

    memory_file.write_text(content, encoding="utf-8")
    return True


def _replace_section(content: str, section_name: str, new_body: str) -> str:
    """Replace content between ## section_name and the next ## header."""
    pattern = rf"(## {re.escape(section_name)}\n)(.*?)(?=\n## |\Z)"
    replacement = rf"\g<1>{new_body}"
    return re.sub(pattern, replacement, content, flags=re.DOTALL)


def _get_section(content: str, section_name: str) -> str:
    """Extract content of a ## section."""
    pattern = rf"## {re.escape(section_name)}\n(.*?)(?=\n## |\Z)"
    match = re.search(pattern, content, re.DOTALL)
    return match.group(1) if match else ""


def _find_existing_session_file(sessions_dir: Path, transcript_name: str) -> Path | None:
    """Return an existing session file for this transcript, if any."""
    for f in sessions_dir.glob("*.md"):
        try:
            text = f.read_text(encoding="utf-8")
        except OSError:
            continue
        # Check frontmatter for matching transcript field
        for line in text.splitlines()[:10]:
            if line.startswith("transcript:") and transcript_name in line:
                return f
    return None


def write_session_file(
    workspace: Path,
    facts: dict[str, Any],
    session_state: dict[str, Any],
    transcript_path: Path | None,
    claude_session_uuid: str | None = None,
) -> Path | None:
    """Write a session summary file to 🤖 AI/memory/sessions/.

    Idempotent: if a file for the same transcript already exists, overwrites
    it in-place rather than creating a new timestamped duplicate.
    """
    sessions_dir = workspace / "🤖 AI" / "memory" / SESSIONS_DIR_NAME
    sessions_dir.mkdir(parents=True, exist_ok=True)

    transcript_name = transcript_path.name if transcript_path else ""
    now = datetime.now(timezone.utc)

    # Reuse existing file for this transcript to avoid duplicates
    existing = _find_existing_session_file(sessions_dir, transcript_name) if transcript_name else None
    if existing:
        session_file = existing
    else:
        filename = now.strftime("%Y-%m-%d-%H%MZ.md")
        session_file = sessions_dir / filename

    session_id = session_state.get("session_id", "unknown")
    start_time = session_state.get("start_time", "")

    decisions = facts.get("key_decisions", [])
    questions = facts.get("open_questions", [])
    context_changes = facts.get("context_changes", "")
    summary = facts.get("session_summary", "Session recorded.")
    focus = facts.get("current_focus", "")

    lines = [
        f"---",
        f"date: {now.strftime('%Y-%m-%d')}",
        f"session_id: {session_id}",
        f"claude_session_id: {claude_session_uuid or ''}",
        f"start_time: {start_time}",
        f"transcript: {transcript_path.name if transcript_path else 'unknown'}",
        f"---",
        f"",
        f"## Summary",
        f"{summary}",
        f"",
        f"## Focus",
        f"{focus or 'Not captured.'}",
        f"",
    ]

    if decisions:
        lines += ["## Decisions"]
        for d in decisions:
            lines.append(f"- {d}")
        lines.append("")

    if questions:
        lines += ["## Open Questions"]
        for q in questions:
            lines.append(f"- {q}")
        lines.append("")

    if context_changes:
        lines += ["## Context Changes", context_changes, ""]

    session_file.write_text("\n".join(lines), encoding="utf-8")
    return session_file


def manage_session_archive(workspace: Path) -> int:
    """Move oldest sessions to archive when count exceeds MAX_SESSIONS. Returns archived count."""
    sessions_dir = workspace / "🤖 AI" / "memory" / SESSIONS_DIR_NAME
    if not sessions_dir.exists():
        return 0

    session_files = sorted(sessions_dir.glob("*.md"))
    if len(session_files) <= MAX_SESSIONS:
        return 0

    archive_dir = workspace / "🤖 AI" / "memory" / ARCHIVE_DIR_NAME
    archive_dir.mkdir(parents=True, exist_ok=True)
    archive_file = archive_dir / "archive.md"

    to_archive = session_files[: len(session_files) - MAX_SESSIONS]

    with open(archive_file, "a", encoding="utf-8") as arc:
        for f in to_archive:
            arc.write(f"\n---\n# {f.stem}\n\n")
            arc.write(f.read_text(encoding="utf-8"))
            f.unlink()

    _maybe_summarize_archive(workspace, archive_file)
    return len(to_archive)


def _maybe_summarize_archive(workspace: Path, archive_file: Path) -> None:
    """Compact the archive with an LLM summary when it exceeds the threshold."""
    if not archive_file.exists():
        return

    content = archive_file.read_text(encoding="utf-8")
    session_count = content.count("# 20")  # Count session headers by year prefix

    if session_count < ARCHIVE_SUMMARIZE_THRESHOLD:
        return

    if not CLAUDE_BIN.exists():
        return

    prompt = (
        "You are compacting an archive of AI session summaries for a product manager. "
        "Synthesize the following session archive into a concise chronological summary, "
        "grouped by month, preserving key decisions and patterns. Keep it under 500 words. "
        "Output plain markdown only.\n\n" + content[:12000]
    )

    try:
        result = subprocess.run(
            [str(CLAUDE_BIN), "-p", prompt, "--model", "claude-haiku-4-5-20251001",
             "--no-session-persistence"],
            capture_output=True,
            text=True,
            timeout=60,
            env=_no_hooks_env(),
        )
        if result.returncode == 0 and result.stdout.strip():
            header = f"# Archive (Compacted {datetime.now().strftime('%Y-%m-%d')})\n\n"
            archive_file.write_text(header + result.stdout.strip() + "\n", encoding="utf-8")
    except (OSError, subprocess.TimeoutExpired):
        pass


def run_extraction(workspace: Path, session_state: dict[str, Any]) -> bool:
    """Main entrypoint. Returns True if extraction succeeded."""
    start_time_str = session_state.get("start_time", "")
    start_time = None
    if start_time_str:
        try:
            start_time = datetime.fromisoformat(start_time_str.replace("Z", "+00:00"))
        except ValueError:
            pass

    transcript_path = find_session_transcript(workspace, start_time)
    if not transcript_path:
        sys.stderr.write("session_extractor: no .specstory transcript found\n")
        return False

    try:
        transcript = transcript_path.read_text(encoding="utf-8", errors="ignore")
    except OSError:
        return False

    # Skip very short transcripts (likely no real work happened)
    if len(transcript) < 500:
        return False

    print("  Extracting session facts via Claude...")
    facts = call_claude_extraction(transcript)
    if not facts:
        return False

    summary = facts.get("session_summary", "")
    print(f"  Session: {summary[:80]}" if summary else "  Session facts extracted.")

    claude_uuid = find_claude_session_uuid(workspace)
    patch_memory_md(workspace, facts)
    session_file = write_session_file(workspace, facts, session_state, transcript_path, claude_uuid)
    archived = manage_session_archive(workspace)

    if session_file:
        print(f"  Session file: {session_file.relative_to(workspace)}")
    if archived:
        print(f"  Archived {archived} old session(s)")

    return True
