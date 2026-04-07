# AI Agent Instructions for [YOUR COMPANY] Product Management Workspace

> **Note**: This file contains project-specific context. Customize the sections marked with [UPDATE THIS].

---

## Quick Start (For AI Assistants)

**First things to load**:
1. Check `GOALS.md` for role, portfolio, current goals, and key stakeholders
2. Check `📋 Tasks/this-week.md` for weekly priorities, then `📋 Tasks/today.md` for the daily plan
3. Check `📋 Tasks/backlog.md` and `📋 Tasks/ideas.md` when planning, prioritizing, or capturing new work
4. Check `🤖 AI/memory/memory.md` for current focus

**Context**: See `GOALS.md` for role, portfolio, and current goals.

**Common Commands**: `/today`, `/think`, `/brainstorm`, `/compete` — see `.claude/commands/COMMAND-REFERENCE.md`

**Working principle**: Simplicity > Complexity. Shorter is almost always better. Plain language beats jargon. When in doubt, simplify.

**Before any strategic decision or spec**: Braindump before structure — get raw thinking out first, then organize.

---

## Product Rules

These rules define how to operate as a 10X Product Leader. Reference them proactively.

| Rule | When to Reference |
|------|-------------------|
| **pm-core.mdc** | DEFAULT - Always loaded — Core operating principles, quick references, conflict resolution |
| **pm-mental-models.mdc** | Strategic thinking, investment decisions — Load on trigger |
| **pm-decision-detail.mdc** | Decision documentation, reviews — Load on trigger |
| **pm-frameworks.mdc** | Framework selection, when to abandon — Load on trigger |
| **pm-communication.mdc** | Communication deep-dive, audience patterns — Load on trigger |
| **pm-product-sense.mdc** | Product sense/quality, taste vs data — Load on trigger |

**Default**: Follow `pm-core.mdc` always. Detail files load via MEMORY.md wake-on-trigger pattern.

---

## Workspace Organization

### Directory Structure
```
./
├── GOALS.md                # Identity, ownership, quarterly goals, stakeholders (read first)
├── 📦 Products/            # Product strategy, ICP, ROI
├── 📁 Workflows/           # Repeatable processes: QPR prep, weekly update, research synthesis
├── 🏢 Company/             # [UPDATE THIS: Your company] business context
├── 🎓 Product-Management/  # PM frameworks, mental models, strategy
├── 📋 Tasks/               # today.md, backlog.md, completed, archive
├── 📚 Knowledge/           # Reference, Research, People (stakeholder notes)
├── 🤖 AI/memory/           # AI context (memory.md)
├── .cursor/                # Cursor IDE (rules, commands)
└── .ruler/                 # Ruler configuration
```

### Key Knowledge Sources
- **Product Strategy**: `Products/[PRODUCT 1]/`, `Products/[PRODUCT 2]/`
- **Market Intelligence**: `Company/competitive-analysis.md` [UPDATE THIS]
- **Customer Data**: `Company/customer-research/` [UPDATE THIS]
- **PM Frameworks**: `Product-Management/`

---

## Memory Bank

Single unified context file: **`🤖 AI/memory/memory.md`**. Update when session focus or milestones change; use `/refresh-memory` to append session activity.

---

## Session Startup

### Session Continuity (Automatic)

All previous sessions persist as `.jsonl` files in `~/.claude/projects/-Users-jhigh-SNOW-Work/`. The `/clear` command wipes in-memory context only — transcripts are never deleted.

**When the user references prior work, automatically search for context.** Do not wait for them to invoke `/remember` or any other command. The agent detects intent and acts.

**Detection triggers** — any message (not just the first) containing:

- "continue", "resume", "pick up", "back to", "where were we"
- "like we discussed", "as we decided", "what did we decide"
- "remember when", "last time", "previously", "earlier"

**Agent actions by intent:**

| User Intent | Agent Action |
|-------------|-------------|
| Wants to literally resume a specific session | Suggest `claude --resume <session-id>` (find ID via `ls -t ~/.claude/projects/-Users-jhigh-SNOW-Work/*.jsonl \| head -10` or grep for content) |
| Wants to continue most recent work | Suggest `claude --continue`, OR search episodic memory and proceed in current session |
| References a past decision, topic, or discussion | Search episodic memory automatically, summarize what you found, then respond |
| Asks "what did we..." or "remember when..." | Search episodic memory + workspace docs (QMD) in parallel, merge results |

**Principle**: The user should never need to know command names. The agent detects the intent and takes the right action. `/remember` exists as an explicit escape hatch, but the default is agent-initiated.

---

## Accumulated Wisdom

See **`🤖 AI/patterns/learned-patterns.md`** for workspace conventions, past decisions, and patterns worth preserving.

### Self-Improving Knowledge System

**Knowledge router**: `📚 Knowledge/INDEX.md` — read this first to decide which domain subfolder to load rather than listing all files.

**Hypothesis tracking**: Domain-level unvalidated beliefs live in:
- `📚 Knowledge/Growth/hypotheses.md`
- `📚 Knowledge/Market/hypotheses.md`

Add a hypothesis when you observe a pattern but don't have 3+ confirmations yet. Promote to `🤖 AI/patterns/learned-patterns.md` at 3 confirmations using the 4 quality gates: Actionable, Specific, Durable, Non-obvious.
