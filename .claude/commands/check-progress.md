Check what changed since the canonical memory files were last updated.

This command compares current repo activity against:
- `🤖 AI/memory/memory.md`
- `🤖 AI/patterns/learned-patterns.md`

Use it to decide whether to run `/refresh-memory`, `/capture-pattern`, or both.

## Execution

Run this with Bash:

```bash
python3 - <<'PY'
import sqlite3
import subprocess
from datetime import datetime, timedelta
from pathlib import Path

workspace = Path(".")
memory_files = {
    "memory.md": workspace / "🤖 AI" / "memory" / "memory.md",
    "learned-patterns.md": workspace / "🤖 AI" / "patterns" / "learned-patterns.md",
}

last_updates = {}
for name, path in memory_files.items():
    if path.exists():
        last_updates[name] = datetime.fromtimestamp(path.stat().st_mtime)

baseline = min(last_updates.values()) if last_updates else datetime.now() - timedelta(days=30)

commits_result = subprocess.run(
    ["git", "log", "--since", baseline.isoformat(), "--oneline", "--no-merges"],
    capture_output=True,
    text=True,
    cwd=workspace,
    check=False,
)
commits = commits_result.stdout.strip().splitlines() if commits_result.stdout.strip() else []

files_result = subprocess.run(
    ["git", "log", "--since", baseline.isoformat(), "--name-only", "--format="],
    capture_output=True,
    text=True,
    cwd=workspace,
    check=False,
)
modified_files = sorted({line.strip() for line in files_result.stdout.splitlines() if line.strip()})

events_db = workspace / "🤖 AI" / "events.db"
event_summary = None
if events_db.exists():
    try:
        conn = sqlite3.connect(events_db)
        cur = conn.cursor()
        cur.execute("select count(*) from events")
        total_events = cur.fetchone()[0]
        cur.execute("select count(*) from events where event_timestamp > ?", (baseline.isoformat(),))
        recent_events = cur.fetchone()[0]
        conn.close()
        event_summary = (total_events, recent_events)
    except sqlite3.Error:
        event_summary = None

print(f"## Progress Check: Changes since {baseline.strftime('%Y-%m-%d %H:%M')}")
print()

print("### Memory File Updates")
for name, mtime in sorted(last_updates.items(), key=lambda x: x[1]):
    age = (datetime.now() - mtime).days
    status = "✓" if age < 7 else "⚠" if age < 30 else "✗"
    print(f"  {status} {name}: {mtime.strftime('%Y-%m-%d')} ({age}d ago)")
print()

if commits:
    print(f"### Git Commits ({len(commits)} since baseline)")
    for commit in commits[:10]:
        print(f"  • {commit}")
    if len(commits) > 10:
        print(f"  ... and {len(commits) - 10} more")
    print()

if event_summary:
    print("### Observer Activity")
    print(f"  • Total events recorded: {event_summary[0]}")
    print(f"  • Events since baseline: {event_summary[1]}")
    print()

relevant_files = [
    f for f in modified_files
    if any(marker in f for marker in ["🤖 AI/", ".claude/", ".cursor/", "🔧 Automation/", "Products/", "📦 Products/"])
]
if relevant_files:
    print(f"### Modified Relevant Files ({len(relevant_files)})")
    for path in relevant_files[:20]:
        print(f"  • {path}")
    if len(relevant_files) > 20:
        print(f"  ... and {len(relevant_files) - 20} more")
    print()
PY
```

## Output Sections

1. **Memory File Updates** - Freshness of the canonical memory files
2. **Git Commits** - Commits since the last memory baseline
3. **Observer Activity** - Optional summary from `🤖 AI/events.db`
4. **Modified Relevant Files** - Files that may warrant a memory update

## Status Indicators

- `✓` = Fresh (< 7 days)
- `⚠` = Aging (7-30 days)
- `✗` = Stale (> 30 days)

## After Progress Check

Ask the user:

**"Based on this activity, should I update:**
- `🤖 AI/memory/memory.md` for current focus or session summaries?
- `🤖 AI/patterns/learned-patterns.md` for a durable pattern or decision?

If you want, I can run `/refresh-memory` or capture a pattern next."**

## Notes

- Baseline = oldest canonical memory file modification time
- Observer output is optional and should be treated as experimental
- This command complements `/refresh-memory`
