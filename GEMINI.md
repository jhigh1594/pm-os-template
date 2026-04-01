# AI Agent Instructions for ServiceNow Product Management Workspace

> **Note**: This file serves as the core instruction manual for Gemini (and other AI agents) navigating this ServiceNow PM-OS workspace. 

---

## Quick Start (For AI Assistants)

**First 3 Things**:
1. Check `GOALS.md` for my role as Senior AI PM, portfolio (CSP context), goals, and key stakeholders like Garin Landry.
2. Check `📋 Tasks/today.md` for daily priorities and active work.
3. Check `🤖 AI/memory/memory.md` for current focus and working preferences (simplicity, fast shipping, zero jargon).

**Context**: See `GOALS.md` for role, portfolio, and current goals.

**Common Commands**: `/today`, `/think`, `/brainstorm`, `/compete` — (typically tracked in `.claude/commands/` or `.agent/workflows/` equivalent).

**Working principle**: Simplicity > Complexity. Shorter is almost always better. Plain language beats jargon. When in doubt, simplify. Explain things like I am 5 if they are complex.

**Before any strategic decision or spec**: Braindump before structure — get raw thinking out first, then organize to avoid process-for-process-sake.

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

**Default**: Follow `pm-core.mdc` always. Detail files load via `memory.md` wake-on-trigger pattern.

---

## Workspace Organization

### Directory Structure
```
./
├── GOALS.md                # Identity, ownership, quarterly goals, stakeholders (read first)
├── 📦 Products/            # Product strategy, ICP, ROI (Focus: CSP)
├── 📁 Workflows/           # Repeatable processes: QPR prep, weekly update, research synthesis
├── 🏢 Company/             # ServiceNow business context
├── 🎓 Product-Management/  # PM frameworks, mental models, strategy
├── 📋 Tasks/               # today.md, backlog.md, completed, archive
├── 📚 Knowledge/           # Reference, Research, People (stakeholder notes)
├── 🤖 AI/memory/           # AI context (memory.md)
├── .claude/               # AI rules and commands configuration
└── .ruler/                 # Ruler configuration
```

### Key Knowledge Sources
- **Product Strategy**: `📦 Products/CSP/`
- **Market Intelligence**: `🏢 Company/competitive-analysis.md` 
- **Customer Data**: `🏢 Company/customer-research/`
- **PM Frameworks**: `🎓 Product-Management/`

---

## Memory Bank

Single unified context file: **`🤖 AI/memory/memory.md`**. Update when session focus or milestones change; use `/refresh-memory` to append session activity.

---

## Accumulated Wisdom

See **`🤖 AI/patterns/learned-patterns.md`** for workspace conventions, past decisions, and patterns worth preserving.

### Self-Improving Knowledge System

**Knowledge router**: `📚 Knowledge/INDEX.md` — read this first to decide which domain subfolder to load rather than listing all files.

**Hypothesis tracking**: Domain-level unvalidated beliefs live in:
- `📚 Knowledge/Growth/hypotheses.md`
- `📚 Knowledge/Market/hypotheses.md`

Add a hypothesis when you observe a pattern but don't have 3+ confirmations yet. Promote to `🤖 AI/patterns/learned-patterns.md` at 3 confirmations using the 4 quality gates: Actionable, Specific, Durable, Non-obvious.
