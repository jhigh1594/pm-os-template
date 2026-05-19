# AI Agent Instructions — PM Operating System

**Workspace:** Generic PM-OS template. Simplicity-first. Execution over endless planning.

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

## Products and company context

- **Do not assume** product names, competitors, or company facts not present in this repo.
- Product definitions live under `📦 Products/<product-slug>/` — read `GOALS.md` and folder READMEs; if empty, ask the human to name the product before inventing one.
- Company context lives under `🏢 Company/` and `📚 Knowledge/`.

---

## Session Continuity

When the human references prior work — trigger phrases: "continue", "resume", "where were we", "like we discussed", "what did we decide", "last time", "previously":

| Intent | Action |
|--------|--------|
| Resume a specific session | Suggest `claude --resume <id>` — find recent sessions under `~/.claude/projects/` for this workspace |
| Continue most recent work | Suggest `claude --continue`, or search episodic memory and proceed |
| Reference a past decision or topic | Search episodic memory automatically, summarize findings, then respond |

Agent detects intent and acts. The human should not need to know command names.

---

## Knowledge System

- **Patterns & conventions:** `🤖 AI/patterns/learned-patterns.md`
- **Knowledge router:** `📚 Knowledge/INDEX.md` — read first, load only what's relevant
- **Decisions:** `decisions/` — grep before making any decision that affects more than today's task
- **Commands:** `.claude/commands/COMMAND-REFERENCE.md`
