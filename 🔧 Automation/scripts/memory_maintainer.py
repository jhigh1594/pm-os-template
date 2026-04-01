#!/usr/bin/env python3
"""
Memory Maintainer - Bloat Prevention for memory.md

Implements three-layer defense against memory bloat:
1. Hard Limits: Max 150 lines, 10KB file size
2. Rolling Window: Keep 10 most recent sessions, archive older
3. Smart Summarization: Summarize archived sessions when too large
"""

import argparse
import re
from datetime import date, datetime
from pathlib import Path
from typing import Dict, List, Optional


class MemoryMaintainer:
    """Manages memory.md size through archival and summarization.

    Limits track SESSION CONTENT only, not the permanent reference material
    (Current Focus, Product Context, Technical Notes, etc.).
    """

    # Configuration limits
    MAX_LINES = 500  # Total file limit (increased to account for permanent content)
    MAX_SESSION_LINES = 200  # Session-specific limit (better metric)
    MAX_SIZE_BYTES = 10 * 1024  # 10KB
    KEEP_RECENT_SESSIONS = 10
    SUMMARIZE_THRESHOLD = 50  # Sessions in archive before summarization

    def __init__(self, workspace_root: Path):
        self.workspace = workspace_root
        self.memory_file = workspace_root / "memory-bank" / "memory.md"
        self.archive_file = workspace_root / "memory-bank" / "archive.md"
        self.session_intent_file = workspace_root / ".aipmos" / "session-intent.json"

    def get_file_size_kb(self) -> float:
        """Get file size in KB."""
        if not self.memory_file.exists():
            return 0
        return self.memory_file.stat().st_size / 1024

    def count_lines(self) -> int:
        """Count total lines in memory.md."""
        if not self.memory_file.exists():
            return 0
        return len(self.memory_file.read_text().split("\n"))

    def count_session_lines(self, content: str) -> int:
        """Count only the lines within session entries, excluding permanent content.

        This is the better metric for determining when to archive, as it ignores
        the permanent reference material (Current Focus, Product Context, etc.).
        """
        sessions = self.extract_sessions(content)
        session_lines = 0
        for date, intent, body in sessions:
            # Each session has: header line + body lines + blank line
            session_lines += 1  # "### [Date] Session: [Intent]"
            session_lines += len(body.split("\n"))  # body content
        return session_lines

    def extract_sessions(self, content: str) -> list:
        """Extract session entries from memory content.

        Session format: ### [Date] Session: [Intent]
        Stops at next major section (##), next session (### [), or end of file.
        """
        # Stop at: \n## (major section), ### [ (next session), or end of file
        pattern = r'### \[(.*?)\] Session: (.*?)\n(.*?)(?=\n## |### \[|$)'
        sessions = re.findall(pattern, content, re.DOTALL)
        return sessions

    def count_sessions(self, content: str) -> int:
        """Count session entries in memory content."""
        return len(content.split("### [")) - 1  # -1 because first split is before any ### [

    def archive_old_sessions(self) -> int:
        """Move old sessions to archive, keeping recent ones.

        Returns: Number of sessions archived
        """
        if not self.memory_file.exists():
            return 0

        content = self.memory_file.read_text()
        sessions = self.extract_sessions(content)

        if len(sessions) <= self.KEEP_RECENT_SESSIONS:
            return 0

        # Keep recent sessions, archive older ones
        recent_sessions = sessions[-self.KEEP_RECENT_SESSIONS:]
        archived_sessions = sessions[:-self.KEEP_RECENT_SESSIONS]

        # Build new memory content with only recent sessions
        # Remove all session entries first
        new_content = re.sub(r'### \[.*?\] Session: .*?\n(.*?)(?=### \[|$)', '', content, flags=re.DOTALL)
        new_content = new_content.strip()

        # Add back recent sessions
        for date, intent, body in recent_sessions:
            new_content += f"\n### [{date}] Session: {intent}\n{body}\n"

        # Write updated memory
        self.memory_file.write_text(new_content)

        # Append to archive
        archive_content = ""
        if self.archive_file.exists():
            archive_content = self.archive_file.read_text()

        for date, intent, body in archived_sessions:
            archive_content += f"### [{date}] Session: {intent}\n{body}\n"

        self.archive_file.write_text(archive_content)

        return len(archived_sessions)

    def summarize_archive_if_needed(self) -> bool:
        """Summarize archive if it has too many sessions.

        Returns: True if summarization was performed
        """
        if not self.archive_file.exists():
            return False

        content = self.archive_file.read_text()
        session_count = self.count_sessions(content)

        if session_count < self.SUMMARIZE_THRESHOLD:
            return False

        # Extract all sessions for summarization
        sessions = self.extract_sessions(content)

        # Group by month for summarization
        sessions_by_month = {}
        for date_str, intent, body in sessions:
            try:
                date = datetime.strptime(date_str, "%B %d, %Y")
                month_key = date.strftime("%B %Y")
                if month_key not in sessions_by_month:
                    sessions_by_month[month_key] = []
                sessions_by_month[month_key].append(intent)
            except ValueError:
                # Keep sessions with unparseable dates as-is
                continue

        # Build summarized archive
        summarized = "# Archived Sessions (Summarized)\n\n"

        for month in sorted(sessions_by_month.keys(), reverse=True):
            intents = sessions_by_month[month]
            # Create a thematic summary from intents
            unique_intents = list(set(intents))[:5]  # Top 5 unique intents
            summary_items = []
            for intent in unique_intents:
                intent_clean = intent.lower()
                if "memory" in intent_clean:
                    summary_items.append("Memory system improvements")
                elif "documentation" in intent_clean:
                    summary_items.append("Documentation updates")
                elif "feature" in intent_clean or "implement" in intent_clean:
                    summary_items.append("Feature development")
                elif "fix" in intent_clean or "bug" in intent_clean:
                    summary_items.append("Bug fixes and improvements")
                else:
                    summary_items.append(f"{intent[:50]}...")

            summarized += f"### {month}\n"
            for item in set(summary_items):
                summarized += f"- {item}\n"
            summarized += "\n"

        self.archive_file.write_text(summarized)
        return True

    # Memory decay classes (for documentation/tooling reference):
    #   ephemeral  — review within 1 week  (session-specific learnings)
    #   session    — review within 1 month (project state, active decisions)
    #   project    — review within 3 months (feedback, preferences, tools)
    #   permanent  — no expiry             (user profile, core working style)

    def _parse_frontmatter(self, text: str) -> Dict[str, str]:
        """Parse YAML frontmatter from a markdown file (stdlib only).

        Expects content between the first pair of '---' delimiters.
        Returns a dict of key: value pairs found in the frontmatter block.
        """
        lines = text.splitlines()
        if not lines or lines[0].strip() != "---":
            return {}
        fields: Dict[str, str] = {}
        for line in lines[1:]:
            stripped = line.strip()
            if stripped == "---":
                break
            if ":" in stripped:
                key, _, value = stripped.partition(":")
                fields[key.strip()] = value.strip()
        return fields

    def check_ttl_violations(self) -> List[dict]:
        """Check auto-memory files for missing or overdue review_by dates.

        Scans the Claude Code project auto-memory directory for .md files
        (excluding MEMORY.md), reads YAML frontmatter, and reports files whose
        review_by date is missing or already past today.

        The auto-memory directory is derived from the workspace path using the
        same encoding Claude Code uses: replace '/' with '-'.

        Returns:
            List of dicts with keys: file, issue ("overdue" | "missing"), review_by
        """
        encoded_path = str(self.workspace).replace("/", "-")
        auto_memory_dir = Path.home() / ".claude" / "projects" / encoded_path / "memory"
        violations: List[dict] = []
        today = date.today()

        if not auto_memory_dir.exists():
            return violations

        for md_file in sorted(auto_memory_dir.glob("*.md")):
            if md_file.name.upper() == "MEMORY.MD":
                continue
            try:
                text = md_file.read_text(encoding="utf-8")
            except OSError:
                continue

            fields = self._parse_frontmatter(text)
            review_by_str: Optional[str] = fields.get("review_by") or None

            if review_by_str is None:
                violations.append({"file": md_file.name, "issue": "missing", "review_by": None})
            else:
                try:
                    review_by_date = datetime.strptime(review_by_str, "%Y-%m-%d").date()
                    if review_by_date < today:
                        violations.append(
                            {"file": md_file.name, "issue": "overdue", "review_by": review_by_str}
                        )
                except ValueError:
                    # Unparseable date — treat as missing
                    violations.append(
                        {"file": md_file.name, "issue": "missing", "review_by": review_by_str}
                    )

        return violations

    def evaluate_health(self) -> Dict[str, object]:
        """Inspect memory health without modifying files."""
        line_count = self.count_lines()
        size_kb = self.get_file_size_kb()
        session_count = 0
        session_lines = 0

        if self.memory_file.exists():
            content = self.memory_file.read_text()
            session_count = self.count_sessions(content)
            session_lines = self.count_session_lines(content)

        exceeded_limits: List[str] = []
        if session_lines > self.MAX_SESSION_LINES:
            exceeded_limits.append(f"session lines ({session_lines}/{self.MAX_SESSION_LINES})")
        if line_count > self.MAX_LINES:
            exceeded_limits.append(f"total lines ({line_count}/{self.MAX_LINES})")
        if size_kb > (self.MAX_SIZE_BYTES / 1024):
            exceeded_limits.append(
                f"file size ({size_kb:.2f} KB/{self.MAX_SIZE_BYTES / 1024:.2f} KB)"
            )

        ttl_check = self.check_ttl_violations()

        return {
            "line_count": line_count,
            "session_lines": session_lines,
            "size_kb": round(size_kb, 2),
            "session_count": session_count,
            "action_taken": "none",
            "limits_exceeded": exceeded_limits,
            "ttl_violations": ttl_check,
            "stale_memory_count": len(ttl_check),
        }

    def check_and_maintain(self) -> dict:
        """Check memory health and perform maintenance if needed.

        Returns: Dictionary with maintenance results
        """
        result = self.evaluate_health()

        # Check hard limits (prioritize session_lines over total lines)
        if result["limits_exceeded"]:
            archived = self.archive_old_sessions()
            if archived > 0:
                result = self.evaluate_health()
                result["action_taken"] = f"archived {archived} session(s)"

        # Check if archive needs summarization
        if self.archive_file.exists():
            archive_session_count = self.count_sessions(self.archive_file.read_text())
            if archive_session_count >= self.SUMMARIZE_THRESHOLD:
                if self.summarize_archive_if_needed():
                    result["archive_summarized"] = True

        return result

    def health_status(self, result: Dict[str, object]) -> str:
        """Get human-readable health status from evaluated results."""
        status = f"Memory Status: {result['line_count']} lines ({result['session_lines']} session), {result['size_kb']} KB, {result['session_count']} session{'s' if result['session_count'] != 1 else ''}"

        if result["action_taken"] != "none":
            status += f"\n✅ Action: {result['action_taken']}"
        elif result["limits_exceeded"]:
            status += "\n⚠️  Limits exceeded: " + ", ".join(result["limits_exceeded"])
        # Use session_lines for warning (better metric than total lines)
        elif result["session_lines"] > self.MAX_SESSION_LINES * 0.8:
            status += f"\n⚠️  Approaching session limit ({result['session_lines']}/{self.MAX_SESSION_LINES} session lines)"
        elif result["size_kb"] > ((self.MAX_SIZE_BYTES / 1024) * 0.9):
            status += f"\n⚠️  Approaching file size limit ({result['size_kb']:.2f}/{self.MAX_SIZE_BYTES / 1024:.2f} KB)"
        elif result["line_count"] > self.MAX_LINES * 0.9:
            status += f"\n⚠️  Approaching file limit ({result['line_count']}/{self.MAX_LINES} total lines)"
        else:
            status += "\n✅ Healthy"

        return status


def _print_audit_report(maintainer: "MemoryMaintainer", result: Dict[str, object]) -> None:
    """Print a human-readable memory health report to stdout."""
    today_str = date.today().isoformat()
    print(f"## Memory Health Report — {today_str}")
    print()

    # Memory file stats
    memory_path = maintainer.memory_file
    line_count = result["line_count"]
    max_lines = maintainer.MAX_LINES
    print(f"Memory file: {memory_path} ({line_count} lines / {max_lines} max)")

    # Session / archive counts
    session_count = result["session_count"]
    archive_sessions = 0
    if maintainer.archive_file.exists():
        archive_sessions = maintainer.count_sessions(maintainer.archive_file.read_text())
    print(f"Sessions: {session_count} recent, {archive_sessions} archived")

    # Stale memory files
    stale_count = result["stale_memory_count"]
    print(f"Stale memory files: {stale_count}")
    print()

    # TTL violations
    ttl_violations = result["ttl_violations"]
    print("TTL Violations:")
    if ttl_violations:
        for v in ttl_violations:
            if v["issue"] == "overdue":
                print(f"  - {v['file']}: overdue (review_by: {v['review_by']})")
            else:
                review_info = f" (current value: {v['review_by']})" if v["review_by"] else ""
                print(f"  - {v['file']}: missing review_by field{review_info}")
    else:
        print("  (none)")
    print()

    # Recommendations
    recommendations: List[str] = []
    if stale_count > 0:
        recommendations.append(f"Update review_by dates in {stale_count} memory file{'s' if stale_count != 1 else ''}")

    line_pct = line_count / maintainer.MAX_LINES if maintainer.MAX_LINES else 0
    if line_pct >= 0.9:
        recommendations.append(
            f"memory.md is at {line_pct:.0%} of line limit — consider trimming"
        )

    session_lines = result["session_lines"]
    session_pct = session_lines / maintainer.MAX_SESSION_LINES if maintainer.MAX_SESSION_LINES else 0
    if session_pct >= 0.8 and line_pct < 0.9:
        recommendations.append(
            f"Session lines at {session_pct:.0%} of limit ({session_lines}/{maintainer.MAX_SESSION_LINES}) — consider archiving"
        )

    if result["limits_exceeded"]:
        recommendations.append("Run without --audit to auto-maintain: limits are currently exceeded")

    print("Recommendations:")
    if recommendations:
        for rec in recommendations:
            print(f"  - {rec}")
    else:
        print("  Memory system is healthy. No action needed.")


def main():
    parser = argparse.ArgumentParser(description="Maintain memory.md size")
    parser.add_argument("--workspace", type=Path, default=Path.cwd(), help="Workspace root")
    parser.add_argument("--check-only", action="store_true", help="Check status without making changes")
    parser.add_argument("--force-archive", action="store_true", help="Force archival of old sessions")
    parser.add_argument("--force-summarize", action="store_true", help="Force archive summarization")
    parser.add_argument("--audit", action="store_true", help="Print a human-readable memory health report")
    args = parser.parse_args()

    maintainer = MemoryMaintainer(args.workspace)

    if args.force_archive:
        archived = maintainer.archive_old_sessions()
        print(f"✅ Archived {archived} session(s)")
        return 0

    if args.force_summarize:
        if maintainer.summarize_archive_if_needed():
            print("✅ Archive summarized")
        else:
            print("ℹ️  Archive not large enough to summarize")
        return 0

    if args.audit:
        result = maintainer.evaluate_health()
        _print_audit_report(maintainer, result)
        return 0

    if args.check_only:
        print(maintainer.health_status(maintainer.evaluate_health()))
        return 0

    # Default: check and maintain
    result = maintainer.check_and_maintain()
    print(maintainer.health_status(result))
    return 0


if __name__ == "__main__":
    exit(main())
