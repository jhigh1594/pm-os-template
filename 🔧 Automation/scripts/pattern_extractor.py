#!/usr/bin/env python3
"""
Pattern Extractor — autonomous learning pipeline

Reads two sources every session-end:
  1. 🤖 AI/memory/sessions/ — Claude Code-generated session files → Decisions + Context Changes
  2. .specstory/history/ — recent transcripts → heuristic decision/convention signals (fallback)

Writes candidates to: 🤖 AI/patterns/candidate-patterns.md
Tracks ingested content in: 🤖 AI/patterns/.extraction-manifest.json

Candidates use a clear PENDING header so the user can promote → learned-patterns.md
or discard. The canonical learned-patterns.md is never auto-written.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


# ── Constants ────────────────────────────────────────────────────────────────

CANDIDATE_FILE = "🤖 AI/patterns/candidate-patterns.md"
MANIFEST_FILE = "🤖 AI/patterns/.extraction-manifest.json"
LEARNED_PATTERNS_FILE = "🤖 AI/patterns/learned-patterns.md"

# Keywords that signal a decision or convention in AI response text
DECISION_SIGNALS = [
    r"\bwe(?:'ll| will) (?:use|go with|adopt|follow)\b",
    r"\bconvention[:\s]",
    r"\bpattern[:\s]",
    r"\bdecision[:\s]",
    r"\btrade-?off[:\s]",
    r"\bapproach[:\s]",
    r"\bkey insight[:\s]",
    r"\bimportant[:\s].{0,40}(?:note|rule|principle)",
    r"\balways\b.{0,60}\bwhen\b",
    r"\bnever\b.{0,60}\bwhen\b",
    r"\bprefer\b.{0,60}\bover\b",
]
DECISION_RE = re.compile("|".join(DECISION_SIGNALS), re.IGNORECASE)

# Max characters to pull from a matching AI response chunk
EXCERPT_MAX = 400

# Only ingest sessions modified within the last N days (specstory)
SPECSTORY_LOOKBACK_DAYS = 3


# ── Manifest ─────────────────────────────────────────────────────────────────

def load_manifest(workspace_root: Path) -> dict[str, Any]:
    path = workspace_root / MANIFEST_FILE
    if not path.exists():
        return {"ingested_insight_hashes": [], "last_specstory_extraction": None}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {"ingested_insight_hashes": [], "last_specstory_extraction": None}


def save_manifest(workspace_root: Path, manifest: dict[str, Any]) -> None:
    path = workspace_root / MANIFEST_FILE
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(manifest, indent=2), encoding="utf-8")


def insight_hash(text: str) -> str:
    return hashlib.sha1(text.strip().encode()).hexdigest()[:12]


# ── Specstory extraction ──────────────────────────────────────────────────────

def _ai_turns(content: str) -> list[str]:
    """Split specstory markdown into AI/assistant response chunks."""
    # SpecStory format: _**User**_ / _**Assistant**_ / _**Claude**_ headers
    turn_re = re.compile(r"^_\*\*(?:Assistant|Claude|AI)\*\*_\s*$", re.MULTILINE)
    user_re = re.compile(r"^_\*\*User\*\*_\s*$", re.MULTILINE)

    splits = list(turn_re.finditer(content))
    turns = []
    for i, match in enumerate(splits):
        start = match.end()
        # End at next User or AI marker
        next_markers = [
            m.start() for m in list(turn_re.finditer(content, start)) + list(user_re.finditer(content, start))
        ]
        end = min(next_markers) if next_markers else len(content)
        turns.append(content[start:end].strip())
    return turns


def _extract_decision_excerpts(ai_turn: str) -> list[str]:
    """Return short excerpts from an AI turn that contain decision signals."""
    excerpts = []
    for match in DECISION_RE.finditer(ai_turn):
        # Pull surrounding context: 50 chars before, up to EXCERPT_MAX after
        start = max(0, match.start() - 50)
        end = min(len(ai_turn), match.start() + EXCERPT_MAX)
        chunk = ai_turn[start:end].strip()
        # Trim to nearest sentence boundary
        chunk = re.split(r"(?<=[.!?])\s", chunk)[0] if "." in chunk else chunk
        chunk = chunk[:EXCERPT_MAX]
        if len(chunk) > 60:  # Ignore trivially short matches
            excerpts.append(chunk)
    return excerpts


def extract_specstory_candidates(
    workspace_root: Path, manifest: dict[str, Any]
) -> list[dict[str, str]]:
    """Return candidate patterns from recent specstory sessions."""
    history_dir = workspace_root / ".specstory" / "history"
    if not history_dir.exists():
        return []

    cutoff = datetime.now(timezone.utc).timestamp() - (SPECSTORY_LOOKBACK_DAYS * 86400)
    candidates = []

    for session_file in sorted(history_dir.glob("*.md"), key=lambda p: p.stat().st_mtime, reverse=True):
        if session_file.stat().st_mtime < cutoff:
            break
        try:
            content = session_file.read_text(encoding="utf-8")
        except OSError:
            continue

        turns = _ai_turns(content)
        session_title = session_file.stem.replace("-", " ").replace("_", " ")
        # Strip leading timestamp (e.g. "2026-04-06T17-44-40Z ")
        session_title = re.sub(r"^\d{4}-\d{2}-\d{2}[T_]\d{2}-\d{2}(?:-\d{2})?Z?\s*", "", session_title).strip()

        for turn in turns:
            excerpts = _extract_decision_excerpts(turn)
            for excerpt in excerpts:
                h = insight_hash(excerpt)
                if h in manifest.get("ingested_insight_hashes", []):
                    continue
                candidates.append({
                    "source": "specstory",
                    "session": session_title or session_file.stem,
                    "hash": h,
                    "text": excerpt,
                })

    return candidates


# ── Claude Code session-file extraction ──────────────────────────────────────

def _parse_section(content: str, section: str) -> list[str]:
    """Extract bullet points from a named ## section in a session file."""
    pattern = re.compile(rf"^## {re.escape(section)}\s*$", re.MULTILINE)
    match = pattern.search(content)
    if not match:
        return []

    start = match.end()
    # Section ends at next ## header or EOF
    next_section = re.search(r"^## ", content[start:], re.MULTILINE)
    end = start + next_section.start() if next_section else len(content)
    section_text = content[start:end].strip()

    # Extract bullet points (-) and plain paragraphs
    items = []
    for line in section_text.splitlines():
        line = line.strip().lstrip("- ").strip()
        if line and not line.startswith("#"):
            items.append(line)
    return items


def extract_session_insight_candidates(
    workspace_root: Path, manifest: dict[str, Any]
) -> list[dict[str, Any]]:
    """Extract Decisions and Context Changes from Claude Code session files."""
    sessions_dir = workspace_root / "🤖 AI" / "memory" / "sessions"
    if not sessions_dir.exists():
        return []

    ingested = set(manifest.get("ingested_insight_hashes", []))
    candidates = []

    for session_file in sorted(sessions_dir.glob("*.md"), key=lambda p: p.stat().st_mtime, reverse=True):
        try:
            content = session_file.read_text(encoding="utf-8")
        except OSError:
            continue

        date_match = re.search(r"^date:\s*(.+)$", content, re.MULTILINE)
        date_str = date_match.group(1).strip() if date_match else session_file.stem

        # Pull Decisions (individual bullets → individual candidates)
        for decision in _parse_section(content, "Decisions"):
            h = insight_hash(decision)
            if h in ingested:
                continue
            candidates.append({
                "source": "session-decision",
                "date": date_str,
                "file": session_file.name,
                "hash": h,
                "text": decision,
            })

        # Pull Context Changes (strategic insights — usually a paragraph)
        context_items = _parse_section(content, "Context Changes")
        if context_items:
            combined = " ".join(context_items)
            h = insight_hash(combined)
            if h not in ingested:
                candidates.append({
                    "source": "session-insight",
                    "date": date_str,
                    "file": session_file.name,
                    "hash": h,
                    "text": combined,
                })

    return candidates


# ── Already-in-learned-patterns dedup ────────────────────────────────────────

def load_learned_hashes(workspace_root: Path) -> set[str]:
    """Hashes of content already in learned-patterns.md (rough dedup)."""
    path = workspace_root / LEARNED_PATTERNS_FILE
    if not path.exists():
        return set()
    content = path.read_text(encoding="utf-8")
    # Hash every 80-char chunk of the file for fuzzy dedup
    hashes = set()
    for i in range(0, len(content) - 80, 40):
        hashes.add(insight_hash(content[i : i + 80]))
    return hashes


# ── Candidate file writer ─────────────────────────────────────────────────────

def _format_specstory_block(c: dict[str, str]) -> str:
    return (
        f"### [PENDING] Session signal — {c['session']}\n"
        f"**Source**: `.specstory/history/`  \n"
        f"**Excerpt**: {c['text']}\n\n"
        f"*Promote to `learned-patterns.md` if it passes the 4 gates (Actionable · Specific · Durable · Non-obvious)*\n"
    )


def _format_session_insight_block(c: dict[str, Any]) -> str:
    label = "Decision" if c["source"] == "session-decision" else "Strategic insight"
    return (
        f"### [PENDING] {label} — {c['date']}\n"
        f"**Source**: `🤖 AI/memory/sessions/{c['file']}`  \n"
        f"{c['text']}\n\n"
        f"*Promote to `learned-patterns.md` if it passes the 4 gates (Actionable · Specific · Durable · Non-obvious)*\n"
    )


def write_candidate_file(
    workspace_root: Path,
    specstory_candidates: list[dict],
    session_candidates: list[dict],
) -> int:
    """Append new candidates to the candidate file. Returns count written."""
    path = workspace_root / CANDIDATE_FILE
    path.parent.mkdir(parents=True, exist_ok=True)

    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    total = len(specstory_candidates) + len(session_candidates)

    if total == 0:
        return 0

    lines = [f"\n---\n\n## Extraction batch — {now}\n\n"]

    if session_candidates:
        lines.append(f"### Session Insights ({len(session_candidates)} new)\n\n")
        for c in session_candidates:
            lines.append(_format_session_insight_block(c))
            lines.append("\n")

    if specstory_candidates:
        lines.append(f"### Session Signals ({len(specstory_candidates)} new)\n\n")
        for c in specstory_candidates:
            lines.append(_format_specstory_block(c))
            lines.append("\n")

    # Ensure header exists
    header = (
        "# Candidate Patterns — Pending Review\n\n"
        "*Auto-extracted by `pattern_extractor.py`. Promote entries to `learned-patterns.md` "
        "if they pass the 4 quality gates (Actionable · Specific · Durable · Non-obvious). "
        "Delete or ignore the rest.*\n"
    )
    if not path.exists():
        path.write_text(header, encoding="utf-8")

    with open(path, "a", encoding="utf-8") as f:
        f.write("".join(lines))

    return total


# ── Main ──────────────────────────────────────────────────────────────────────

def run_extraction(workspace_root: Path) -> int:
    """Run full extraction pipeline. Returns count of new candidates written."""
    manifest = load_manifest(workspace_root)
    learned_hashes = load_learned_hashes(workspace_root)

    def not_learned(c: dict) -> bool:
        text = c.get("text") or ""
        return insight_hash(text[:80]) not in learned_hashes

    # Primary: Claude Code-generated session files (Decisions + Context Changes)
    session_candidates = extract_session_insight_candidates(workspace_root, manifest)
    session_candidates = [c for c in session_candidates if not_learned(c)]

    # Secondary: heuristic specstory signals (capped to avoid noise)
    specstory_candidates = extract_specstory_candidates(workspace_root, manifest)
    specstory_candidates = [c for c in specstory_candidates if not_learned(c)][:10]

    written = write_candidate_file(workspace_root, specstory_candidates, session_candidates)

    all_hashes = (
        [c["hash"] for c in session_candidates]
        + [c["hash"] for c in specstory_candidates]
    )
    manifest["ingested_insight_hashes"] = list(
        set(manifest.get("ingested_insight_hashes", [])) | set(all_hashes)
    )
    manifest["last_extraction"] = datetime.now(timezone.utc).isoformat()
    save_manifest(workspace_root, manifest)

    return written


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Extract pattern candidates from session files and specstory")
    parser.add_argument("--workspace", type=Path, default=Path.cwd())
    parser.add_argument("--dry-run", action="store_true", help="Report counts without writing")
    args = parser.parse_args(argv)

    workspace = args.workspace
    manifest = load_manifest(workspace)
    learned_hashes = load_learned_hashes(workspace)

    def not_learned(c: dict) -> bool:
        text = c.get("text") or ""
        return insight_hash(text[:80]) not in learned_hashes

    session_candidates = [c for c in extract_session_insight_candidates(workspace, manifest) if not_learned(c)]
    specstory_candidates = [c for c in extract_specstory_candidates(workspace, manifest) if not_learned(c)][:10]
    total = len(session_candidates) + len(specstory_candidates)

    if args.dry_run:
        print(f"Would write {total} candidates ({len(session_candidates)} session insights, {len(specstory_candidates)} specstory signals)")
        return 0

    written = write_candidate_file(workspace, specstory_candidates, session_candidates)

    all_hashes = [c["hash"] for c in session_candidates] + [c["hash"] for c in specstory_candidates]
    manifest["ingested_insight_hashes"] = list(
        set(manifest.get("ingested_insight_hashes", [])) | set(all_hashes)
    )
    manifest["last_extraction"] = datetime.now(timezone.utc).isoformat()
    save_manifest(workspace, manifest)

    if written:
        print(f"📋 {written} new pattern candidates → {CANDIDATE_FILE}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
