# AI Agent Instructions for [YOUR COMPANY] Product Management Workspace

> **Note**: This file contains project-specific context. Customize the sections marked with [UPDATE THIS].

---

## Quick Start (For AI Assistants)

**First 3 Things**:
1. Check `GOALS.md` for role, portfolio, current goals, and key stakeholders
2. Check `📋 Tasks/today.md` for daily priorities and active work
3. Check `🤖 AI/memory/memory.md` for current focus

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

## Accumulated Wisdom

See **`🤖 AI/patterns/learned-patterns.md`** for workspace conventions, past decisions, and patterns worth preserving.
