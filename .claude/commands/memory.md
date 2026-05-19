# /memory

Update compiled truth memory or run a health diagnostic on the memory system.

## Usage

- `/memory` — update memory.md with session activity (default)
- `/memory --health` — run structural health audit
- `/memory --dry-run` — show what would be updated without writing

---

## Default: Update Memory

Detect workspace root dynamically:

```bash
WORKSPACE=$(git -C "$(pwd)" rev-parse --show-toplevel 2>/dev/null || pwd)
```

Run:

```bash
python3 "$WORKSPACE/🔧 Automation/scripts/memory_updater.py" --workspace "$WORKSPACE"
```

Add `--dry-run` if `--dry-run` flag was passed.

**What it does:**
1. Reads session intent from `🤖 AI/session-intent.json`
2. Fetches git commits since session start
3. Creates a formatted session entry and appends to `memory.md`
4. Runs memory_maintainer.py to prevent bloat

**Output on success:**
```
✅ Updated memory.md with session: [intent]
   File: [workspace]/🤖 AI/memory/memory.md
   Commits: [n]
```

---

## --health: Structural Health Audit

Run a two-part diagnostic:

**Part 1 — Activity Delta (inline Python):**

```bash
WORKSPACE=$(git -C "$(pwd)" rev-parse --show-toplevel 2>/dev/null || pwd)
python3 - <<'EOF'
import os, subprocess, json
from datetime import datetime, timezone
from pathlib import Path

workspace = os.environ.get("WORKSPACE", os.getcwd())
memory_file = Path(workspace) / "🤖 AI/memory/memory.md"

# File freshness
if memory_file.exists():
    mtime = datetime.fromtimestamp(memory_file.stat().st_mtime, tz=timezone.utc)
    age_days = (datetime.now(timezone.utc) - mtime).days
    print(f"memory.md last modified: {mtime.strftime('%Y-%m-%d')} ({age_days} days ago)")
else:
    print("⚠️  memory.md not found")

# Session files
sessions_dir = Path(workspace) / "🤖 AI/memory/sessions"
if sessions_dir.exists():
    sessions = sorted(sessions_dir.glob("*.md"), key=lambda f: f.stat().st_mtime, reverse=True)
    print(f"Session files: {len(sessions)} (rolling window)")
    if sessions:
        print(f"Most recent: {sessions[0].name}")
else:
    print("⚠️  sessions/ directory not found")

# Git commits since last memory update
try:
    result = subprocess.run(
        ["git", "-C", workspace, "log", "--oneline", "--since", "7 days ago"],
        capture_output=True, text=True
    )
    commits = [l for l in result.stdout.strip().split("\n") if l]
    print(f"Git commits (last 7 days): {len(commits)}")
except Exception as e:
    print(f"Git check failed: {e}")
EOF
```

**Part 2 — Structural audit:**

```bash
python3 "$WORKSPACE/🔧 Automation/scripts/memory_maintainer.py" --workspace "$WORKSPACE" --audit
```

**Interpret results and give one recommended action:**

| Scenario | Action |
|----------|--------|
| memory.md > 14 days stale | Run `/memory` to update compiled truth |
| > 10 session files | Session pruning needed — oldest sessions should roll off |
| 0 commits, no session activity | Nothing to update; memory is current |
| memory_maintainer reports TTL violations | Run `memory_maintainer.py --prune` |
| memory.md missing | Re-initialize from session files |

End with exactly one recommended next action.
