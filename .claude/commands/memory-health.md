---
description: Run the memory health workflow
---
# /memory-health — Memory System Health Check

Combined diagnostic replacing `/check-progress` + `/memory-audit`. Surfaces what changed since the last memory update (activity delta) AND runs the Python structural health audit — in one command, ending with one concrete recommended action.

---

## When to Use

Run when you want to know: "Is my memory system stale, and what should I do about it?"

- **Weekly**: as part of your regular maintenance cadence
- **Before a new session**: after a break of 3+ days
- **After major work**: following a sprint, QPR prep, or strategy session

---

## Command Syntax

```
/memory-health
```

No flags needed. Runs both diagnostics by default.

---

## Execution

### Step 1: Activity Delta

Run the following Python inline to check memory file freshness and git activity since the last update:

```python
import subprocess
from datetime import datetime, timedelta
from pathlib import Path

workspace = Path(os.getcwd())
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
    capture_output=True, text=True, cwd=workspace, check=False,
)
commits = commits_result.stdout.strip().splitlines() if commits_result.stdout.strip() else []

files_result = subprocess.run(
    ["git", "log", "--since", baseline.isoformat(), "--name-only", "--format="],
    capture_output=True, text=True, cwd=workspace, check=False,
)
modified_files = sorted({l.strip() for l in files_result.stdout.splitlines() if l.strip()})
relevant_files = [
    f for f in modified_files
    if any(m in f for m in ["🤖 AI/", ".claude/", ".cursor/", "🔧 Automation/", "Products/", "📦 Products/"])
]

print(f"## Activity since {baseline.strftime('%Y-%m-%d')}")
print()
print("### Memory File Freshness")
for name, mtime in sorted(last_updates.items(), key=lambda x: x[1]):
    age = (datetime.now() - mtime).days
    status = "✓" if age < 7 else "⚠" if age < 30 else "✗"
    print(f"  {status} {name}: {mtime.strftime('%Y-%m-%d')} ({age}d ago)")
print()
if commits:
    print(f"### Git Activity ({len(commits)} commits since baseline)")
    for c in commits[:8]:
        print(f"  • {c}")
    if len(commits) > 8:
        print(f"  ... and {len(commits) - 8} more")
    print()
if relevant_files:
    print(f"### Modified Relevant Files ({len(relevant_files)})")
    for f in relevant_files[:15]:
        print(f"  • {f}")
    if len(relevant_files) > 15:
        print(f"  ... and {len(relevant_files) - 15} more")
```

### Step 2: Structural Health Audit

```bash
cd "🔧 Automation/scripts" && python memory_maintainer.py --audit --workspace "../.."
```

### Step 3: Synthesized Recommendation

Based on combined output, give **exactly one** recommended action:

| Scenario | Recommendation |
|---|---|
| Memory files fresh (<7d), no violations | "Memory system is healthy. Last updated [date]. No action needed." |
| 5+ commits or 3+ relevant files since last update | "You have [N] commits since [date]. Run `/refresh-memory` to capture session activity." |
| Recent changes that warrant pattern capture | "You have [N] relevant changes that may reveal new patterns. Run `/capture-pattern` to preserve key learnings." |
| TTL violations in auto-memory | "[N] memory files have overdue review dates. I can update the `review_by` dates — want me to proceed?" |
| memory.md approaching line limit | "memory.md is approaching its line limit ([N] lines). I can archive older sessions — want me to proceed?" |

Always end with **one specific suggested action**, not a list of options.

---

## Integration

- **Replaces**: Running `/check-progress` then `/memory-audit` separately
- **Routes to**: `/refresh-memory` (session state update), `/capture-pattern` (new learnings), or direct remediation for TTL/size issues
- **Cadence**: Weekly, or before starting a new session after a break

---

## Notes

- Reuses `memory_maintainer.py` at `🔧 Automation/scripts/memory_maintainer.py`
- The script's `evaluate_health()` and `check_ttl_violations()` methods are the authoritative health data source
- Does NOT replace `/refresh-memory` (which writes new content) — this command only reads and diagnoses
