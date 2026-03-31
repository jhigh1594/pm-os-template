---
description: Run the refresh memory workflow
---
Update `🤖 AI/memory/memory.md` with session activity by running the memory updater script.

## Command Arguments

Parse the command arguments in order:
1. **Dry Run** (optional, default: `false`): `true` or `false`
   - `true`: Show what would be updated without writing
   - `false`: Update memory.md with session activity

## Execution

Build the command based on arguments:
- Base command: `python3 "🔧 Automation/scripts/memory_updater.py" --workspace "/Users/jhigh/Planview Work"`
- If `dry_run` is `true`, add `--dry-run`

Run the command using Bash.

## How It Works

The `memory_updater.py` script:
1. Reads session intent from `🤖 AI/session-intent.json`
2. Fetches git commits since session start
3. Falls back to `.specstory/history/` when session intent is empty
4. Creates a formatted session entry
5. Appends to memory.md in the correct location
6. Runs memory maintainer to prevent bloat

---

## Session Entry Format

Entries are added to memory.md in this format:

```markdown
### [January 27, 2026] Session: Implement /brainstorm command
**Context**: Create persona-based brainstorming command for tactical pre-PRD exploration
**Planned**: Implement /brainstorm command with PM, Designer, and Engineer personas
**Completed**:
- Create /brainstorm command with three persona files
- Add command to COMMAND-REFERENCE.md
**Outcome**: Planned to: Implement /brainstorm command | Completed: feature development, documentation | Changes: 3 feature, 2 doc commits
```

---

## Session Intent Setup

The script reads from `🤖 AI/session-intent.json`:

```json
{
  "intent": "Implement /brainstorm command",
  "user_description": "Create persona-based brainstorming with three expert perspectives",
  "start_time": "2026-01-27T08:00:00Z"
}
```

Session intent is typically set via:
- `/today` command (daily planning workflow)
- `set_intent.py`
- Manual edit of `🤖 AI/session-intent.json`

---

## Memory Maintainer

After updating memory.md, the script automatically runs `memory_maintainer.py` to:
- Prevent memory file bloat
- Archive old session entries
- Consolidate redundant information
- Maintain performance

---

## Integration Points

**Triggered by**:
- End of work session (manual invocation)
- Before `/check-progress` (to ensure current memory state)
- After significant feature completion
- Automatically at session end via `.claude/scripts/session-end.sh`

**Complements**:
- `/check-progress` - Shows deltas since last memory update
- `/today` - Sets session intent that this command reads

---

## Usage Pattern

Typical workflow:

1. **Start session**: Set intent via `/today` or manual edit
2. **Do work**: Make commits, create files
3. **Run `/refresh-memory`**: Capture session in memory.md
4. **Continue**: Repeat as needed

---

## Output

Success message:
```
✅ Updated memory.md with session: Implement /brainstorm command...
   File: /Users/jhigh/Planview Work/🤖 AI/memory/memory.md
   Commits: 5
```

---

## Notes

- If no session intent exists, falls back to git commits only
- If session intent is empty, it may infer intent from recent `.specstory/history/` sessions
- No commits = records as planning/research session
- Entries are inserted after "Current Focus" section
- "Last Updated" timestamp is automatically updated
