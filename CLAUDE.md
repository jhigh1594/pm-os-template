# AI Agent Instructions for [YOUR COMPANY] Product Management Workspace

> **Note**: This file contains project-specific context. Customize the sections marked with [UPDATE THIS].

---

## Quick Start (For AI Assistants)

**First 3 Things**:
1. Check `GOALS.md` for role, portfolio, current goals, and key stakeholders
2. Check `📋 Tasks/today.md` for daily priorities and active work
3. Check `.aipmos/memory-bank/memory.md` for current focus

**Context**: See `GOALS.md` for role, portfolio, and current goals.

**Common Commands**: `/today`, `/think`, `/granola`, `/compete` — see `.claude/commands/COMMAND-REFERENCE.md`

**Working principle**: Simplicity > Complexity. Shorter is almost always better. Plain language beats jargon. When in doubt, simplify.

---

## Product Rules

These rules define how to operate as a 10X Product Leader. Reference them proactively.

| Rule | When to Reference |
|------|-------------------|
| **pm-operating-principles.mdc** | Default operating mode — Execution Bias, Ruthless Prioritization, Four Risks, Data-Informed decisions |
| **mental-models.mdc** | Strategic thinking, investment decisions, system design — 20 models including ROI, Working Backwards, Flywheels |
| **decision-framework.mdc** | Making or documenting decisions — One-Way vs Two-Way Doors, 70% Rule, Disagree and Commit |
| **frameworks-as-tools.mdc** | Selecting PM frameworks — library by purpose, when to abandon frameworks |
| **communication-standards.mdc** | Writing for specific audiences — Executives, ICs, Customers, Cross-functional stakeholders |
| **product-sense.mdc** | Product critiques, trusting gut vs data, developing product intuition |

**Default**: Follow `pm-operating-principles.mdc` unless a specific situation calls for another rule.

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
├── .aipmos/memory-bank/    # AI context persistence (memory.md)
└── .claude/                # Claude Code configuration
```

### Key Knowledge Sources
- **Product Strategy**: `Products/[PRODUCT 1]/`, `Products/[PRODUCT 2]/`
- **Market Intelligence**: `Company/competitive-analysis.md` [UPDATE THIS]
- **Customer Data**: `Company/customer-research/` [UPDATE THIS]
- **PM Frameworks**: `Product-Management/`

---

## Memory Bank

Single unified context file: **`.aipmos/memory-bank/memory.md`**. Update when session focus or milestones change; use `/refresh-memory` to append session activity.
