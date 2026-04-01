# Workspace Memory

## Current Focus

**Role**: Senior AI Product Manager @ ServiceNow
**Product Vision**: Amplify effectiveness through the Customer Success Platform (CSP), shipping fast and iterating with simplicity.
**Active Task**: Driving strategy on `📦 Products/CSP/initiatives/Onboarding` to codify the 30-60-90 plan and define success signals for 60-day material impact.

**Recent Completed Work**:
- Initialized PM-OS Workspace and defined working profile.
- Scaffolded Onboarding initiative workspace.

## Working Preferences

**Energy drivers**: Building automations/frameworks that multiply impact, strategic positioning/competitive analysis, real customer discovery, clear jargon-free communication, shipping.
**Energy drains**: Process for process sake, manual repetitive tasks, complexity that doesn't add value, meetings without decisions, stakeholder misalignment surfacing late.
**Agent Guidelines**:
- Simplicity beats complexity; execution beats endless planning.
- If you can't explain it simply contextually, rethink it.
- Never add unnecessary process or manual repetitive tasks.

## Product Context

### Customer Success Platform (CSP)

**What is CSP**: ServiceNow's Customer Success Platform.
**Value Proposition**: TBD
**Core Differentiators**:
- TBD
**Target Market**: SNOW Customer Success environment.

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
1. What is the highest leverage feature or automation to execute on within the next 60 days to prove material impact?

**Open Questions**:
- None active at this stage.

## Known Gaps

**Baseline Metrics Needed**:
- Metrics measuring CEG Internal Tech and CSP usage/success.

**Documentation Gaps**:
- Need context gathering on CSP ecosystem.
- Need baseline of current tech stack overhead.

---

**Last Updated**: 2026-04-01
**Purpose**: Single unified memory file for AI context across sessions
**Location**: `🤖 AI/memory/memory.md`
