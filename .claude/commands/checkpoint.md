---
description: Summarize and extract insights from the current session before clearing
---

Run the session-end pipeline to capture this session's decisions, insights, and memory before the conversation is cleared.

## Command Syntax

```
/checkpoint [--capture [type] [description]]
```

- No flags: session-end pipeline only
- `--capture`: Interactive pattern capture (runs after session pipeline)
  - `type` (optional): `decision` | `convention` | `mistake` | `pattern` | `tool`
  - `description` (optional): brief description

**Pattern capture quality gates** (applied before writing to `learned-patterns.md`):
- Actionable: Can I do something specific with this?
- Specific: Tied to this context, not generic advice?
- Durable: Useful in 5+ future sessions?
- Non-obvious: Wouldn't naturally know this?

If all 4 pass → write to `🤖 AI/patterns/learned-patterns.md` under the correct section with confidence level (High/Medium/Low). Update `_Total patterns: N_` counter.

---

## What This Does

1. Runs the session extractor — calls Claude to summarize the session and write a structured session file to `🤖 AI/memory/sessions/`
2. Updates `🤖 AI/memory/memory.md` with session activity
3. Runs the pattern extractor — pulls Decisions and Context Changes from the new session file into `🤖 AI/patterns/candidate-patterns.md`
4. Reports what was captured

## Execution

Run this exact command via Bash:

```
cd "$(git rev-parse --show-toplevel 2>/dev/null || pwd)" && .venv/bin/python "🔧 Automation/scripts/hooks/session_end.py" --workspace "$(git rev-parse --show-toplevel 2>/dev/null || pwd)" --python-cmd ".venv/bin/python"
```

## After Running

Report to the user:
- Whether a new session file was created and its filename
- How many pattern candidates were extracted (if any)
- Confirm: "Session captured — safe to /clear"

The user can then run `/clear` to reset conversation context knowing nothing has been lost.
