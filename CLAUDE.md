# AI Agent Instructions — Jon High / ServiceNow CSP

**Workspace:** PM workspace for Jon High, Senior AI Product Manager at ServiceNow (Customer Success Platform). Simplicity-first. Ships fast. Practicing Stoic.

---

## Session Startup

Load in this order:
1. `GOALS.md` — role, portfolio, quarterly goals, key stakeholders
2. `📋 Tasks/today.md` → `📋 Tasks/this-week.md` → `📋 Tasks/backlog.md`
3. `🤖 AI/memory/memory.md` — current focus and recent context

**Before any strategic decision or spec:** Braindump before structure — raw thinking first, then organize.

---

## Working Principles

- Simplicity > Complexity. Shorter is almost always better.
- Plain language beats jargon.
- Propose, don't ask — best-guess + reasoning over stalling.
- Execution beats planning. Bias toward shipping.
- Challenge assumptions and push back when warranted.

---

## Session Continuity

When the user references prior work — trigger phrases: "continue", "resume", "where were we", "like we discussed", "what did we decide", "last time", "previously":

| Intent | Action |
|--------|--------|
| Resume a specific session | Suggest `claude --resume <id>` — find via `ls -t ~/.claude/projects/-Users-jhigh-SNOW-Work/*.jsonl \| head -10` |
| Continue most recent work | Suggest `claude --continue`, or search episodic memory and proceed |
| Reference a past decision or topic | Search episodic memory automatically, summarize findings, then respond |

Agent detects intent and acts. User should never need to know command names.

---

## Knowledge System

- **Patterns & conventions:** `🤖 AI/patterns/learned-patterns.md`
- **Knowledge router:** `📚 Knowledge/INDEX.md` — read first, load only what's relevant
- **Decisions:** `decisions/` — grep before making any decision that affects more than today's task
- **Commands:** `.claude/commands/COMMAND-REFERENCE.md`
