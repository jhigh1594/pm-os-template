# AI Agent Instructions for [YOUR COMPANY] Product Management Workspace

> **Note**: This file contains project-specific context. For shared frameworks (communication, copywriting, engineering standards), see the global template at `~/.config/ruler/AGENTS.md`.

This document provides project-specific context to complement the global AI agent rules. The global template contains all reusable frameworks and standards.

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
└── .ruler/                 # Ruler configuration (this file)
```

### Key Knowledge Sources
- **Product Strategy**: `Products/[YOUR PRODUCTS]/`
- **Market Intelligence**: `Company/competitive-analysis.md` [UPDATE THIS]
- **Customer Data**: `Company/customer-research/` [UPDATE THIS]
- **PM Frameworks**: `Product-Management/`

---

## Tool Usage Rules

### Repository Context

**Rule**: Always verify the target repository before git operations.
- Run `git remote -v` before committing to confirm correct repo

### Skills vs Commands

**Rule**: Custom skills have specific placement requirements:
- Skills with SKILL.md → `.claude/skills/<skill-name>/SKILL.md`
- Simple commands → `.claude/commands/<command>.md`
- Always verify directory before creating skills

### Exploration Sessions

**Rule**: For exploration-heavy tasks, produce written output EARLY:
- Create `scratch/exploration-notes.md` within first 5 minutes
- Append findings immediately as you discover them
- Never defer all output until session end
- If session might be interrupted, ensure partial results are captured

### Memory Observation Quality

**Rule**: Memory observers should focus on substantive events only:
- **Capture**: Decisions, discoveries, pattern changes, error resolutions
- **Skip**: Routine file reads, minor edits, trivial observations
- **Score**: Assign significance (1-5), only persist observations scoring 3+

---

## File Placement Guidelines

### Where to Put Different Types of Content

**IMPORTANT**: The `🤖 AI/memory/` directory is ONLY for AI memory/context persistence files. Do NOT put other content there.

| Content Type | Location | Examples |
|--------------|----------|----------|
| **Memory/Context** | `🤖 AI/memory/` | `memory.md` (AI reads at session start) |
| **PRDs** | `Products/[Product]/` | Product requirements documents, feature specs |
| **Design Mockups** | `Products/[Product]/designs/` | HTML/CSS mockups, design decisions |
| **Product Strategy** | `Products/[Product]/` | ICP, ROI, positioning, competitive analysis |
| **PM Frameworks** | `Product-Management/` | Mental models, strategy frameworks |
| **Company Context** | `Company/` | Business context, customer research |
| **Commands/Skills** | `.claude/commands/` or `.claude/skills/` | AI workflow commands, reusable skills |

### Examples

**Correct**:
- ✅ `/Products/[Product]/designs/feature.mockup.html`
- ✅ `/Products/[Product]/feature-prd.md`
- ✅ `/🤖 AI/memory/memory.md`

**Incorrect**:
- ❌ `/memory-bank/mockups/` — Mockups are NOT memories
- ❌ `/memory-bank/prds/` — PRDs are NOT memories
- ❌ `/memory-bank/docs/` — General docs are NOT memories

### Rationale

The `🤖 AI/memory/` folder is for **persistent AI context** that needs to be read at every session start. Putting other content there:
1. Clutters the memory bank with non-memory content
2. Makes it harder to find actual memory files
3. Violates the principle of organizing content by its purpose

### Checkpoint Files

For multi-step tasks, create checkpoint files at `.checkpoints/<task-name>.json`:
- Resume from last recorded state if checkpoint exists
- Write checkpoint after each meaningful phase
- Define explicit completion criteria upfront

---

## Memory Bank

Single unified context file: **`🤖 AI/memory/memory.md`**. Update when session focus or milestones change; use `/refresh-memory` to append session activity.

---

*This document is managed by Ruler and automatically synced to all configured AI agents. Update `.ruler/AGENTS.md` and run `ruler apply` to update agent configurations. For framework updates, modify the global template at `~/.config/ruler/AGENTS.md`.*


## Accumulated Wisdom

See **`🤖 AI/patterns/learned-patterns.md`** for workspace conventions, past decisions, and patterns worth preserving. Read it when starting work that touches presentations, documentation structure, or memory files.
