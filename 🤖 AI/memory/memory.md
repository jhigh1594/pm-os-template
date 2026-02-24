# Workspace Memory

## Current Focus

**Role**: [UPDATE THIS: Your role and company]

**Product Vision**: [UPDATE THIS: Your product vision]

**Active Task**: [UPDATE THIS: What you're working on now]

**Recent Completed Work**:
- [UPDATE THIS: Recent accomplishments]

## Product Context

### [UPDATE THIS: Your Product Name]

**What is [Product]**: [UPDATE THIS: Product description]

**Value Proposition**: [UPDATE THIS: Core value prop]

**Core Differentiators**:
- [UPDATE THIS: Key differentiators]

**Target Market**: [UPDATE THIS: ICP, market size, etc.]

## Technical Notes

### Workspace configuration
**Discovery**: Automation finds project root by searching upward for `GOALS.md` or `CLAUDE.md`.

**Key Files**:
- `🔧 Automation/scripts/shared/aipmos_config.py` - AIPMOSConfig (workspace discovery, .env loading)
- `🔧 Automation/scripts/today_cmd/` - Daily planning workflow
- Session intent: `🤖 AI/session-intent.json`; env: `.env` at project root

### MCP Integrations
Available: Notion, Figma, GitHub, Browser Automation, Web Search, Claude Mem, Granola

## Workspace Organization

```
./
├── 📦 Products/              # Product strategy, ICP, ROI
├── 🏢 Company/               # Business context
├── 🎓 Product-Management/    # PM frameworks and resources
├── 📝 Docs/                  # Documentation, memos, templates
├── 🔧 Automation/            # Python automation scripts
├── 📋 Tasks/                 # today.md, backlog.md, completed
├── 📚 Knowledge/             # Research, People notes
├── .claude/               # Claude Code configuration
└── 🤖 AI/                 # AI configuration, memory, and patterns
    └── memory/           # This file
```

## Working Principles

1. **Evidence-based decisions** - Data over assumptions, with clear attribution
2. **Executive communication** - BLUF (bottom line up front), clarity over cleverness
3. **Source attribution** - Label claims: SOURCE, ASSUMPTION, INFERENCE, NEEDS VALIDATION
4. **Git workflow** - Frequent checkpoint commits, never force push to main
5. **Quality** - Run typecheck before ending tasks, never commit without explicit approval

## Active Decisions

**Strategic Questions**:
1. [UPDATE THIS: Your strategic questions]

**Open Questions**:
- [UPDATE THIS: Questions you're tracking]

## Known Gaps

**Baseline Metrics Needed**:
- [UPDATE THIS: Metrics you need to gather]

**Documentation Gaps**:
- [UPDATE THIS: Docs that need to be written]

---

**Last Updated**: [DATE]
**Purpose**: Single unified memory file for AI context across sessions
**Location**: `🤖 AI/memory/memory.md`
