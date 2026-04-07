# Workspace Memory

> Sections marked VOLATILE are overwritten automatically at session end by the LLM extractor.
> Sections marked PERMANENT are never auto-updated — edit manually only.

---

## Current Focus

Two research artifacts completed: csm-jtbd-workflows.md (personas, jobs-to-be-done, workflows, journey maps) and csm-icp-market-research.md (market data, ICP profiles, competitive whitespace analysis). Ready for strategic synthesis.

## Active Decisions

**Strategic Questions**:

- Whether to perform synthesis pass pulling strongest signals from both artifacts into unified strategic framing document for CSP

**Recent Decisions**:

- Deploy parallel agents for internal JTBD synthesis and external market research—two distinct tracks, two separate artifacts
- Focus CSP positioning on three non-obvious strategic findings: CS investment paradox (coordination model design gap), cross-functional post-sales orchestration whitespace (no competitor owns this), AI adoption blocked by data quality not ambition

## Known Gaps

**Baseline Metrics Needed**:

- Metrics measuring CEG Internal Tech and CSP usage/success.

**Documentation Gaps**:

- Need context gathering on CSP ecosystem.
- Need baseline of current tech stack overhead.

---

**Context Change**: User authenticated via /login during synthesis offer—may indicate session state change or next phase of work.

**Context Change**: Two new reference artifacts added to Knowledge/Market/ folder. Market research now documented with 15+ source citations and signal-labeled pain points. ServiceNow CSP positioned against Gainsight, Planhat, Totango with clear competitive differentiation.

**Context Change**: Three strategic insights identified: (1) CS investment paradox—NRR declining despite 60% increased spending, suggesting coordination model problem vs tooling problem; (2) whitespace is cross-functional post-sales orchestration (no competitor owns full Sales→CS→Support→PS→Product motion); (3) AI adoption blocked by data fragmentation, not ambition—platform that unifies data as workflow byproduct would unlock AI for majority of teams.

**Context Change**: Two new research artifacts created in Knowledge/Market/ folder; three non-obvious strategic findings surfaced: (1) CS investment paradox as coordination model problem, (2) whitespace in cross-functional post-sales orchestration, (3) AI adoption blocked by data quality not ambition

**Context Change**: Session interrupted by `/login` command; research phase complete, awaiting strategic synthesis decision

**Context Change**: Session interrupted by user login command; research tracks completed but synthesis step pending user direction.

## Working Preferences

**Energy drivers**: Building automations/frameworks that multiply impact, strategic positioning/competitive analysis, real customer discovery, clear jargon-free communication, shipping.
**Energy drains**: Process for process sake, manual repetitive tasks, complexity that doesn't add value, meetings without decisions, stakeholder misalignment surfacing late.

**Agent Guidelines**:

- Simplicity beats complexity; execution beats endless planning.
- If you can't explain it simply contextually, rethink it.
- Never add unnecessary process or manual repetitive tasks.

---

## Product Context

### Customer Success Platform (CSP)

**What is CSP**: ServiceNow's Customer Success Platform.
**Value Proposition**: TBD
**Core Differentiators**: TBD
**Target Market**: SNOW Customer Success environment.

---

## Technical Notes

### Workspace Configuration

- Project root found by searching upward for `GOALS.md` or `CLAUDE.md`
- `🔧 Automation/scripts/shared/aipmos_config.py` — AIPMOSConfig (workspace discovery, .env loading)
- Session intent: `🤖 AI/session-intent.json`

### Memory System

- `memory.md` — this file; volatile sections updated by LLM extractor at session end
- `sessions/` — rolling 10 session summaries (LLM-written)
- `sessions-archive/` — sessions beyond the rolling window, compacted at 50+
- `patterns/learned-patterns.md` — manually curated patterns and decisions

### MCP Integrations

Available: Notion, Figma, GitHub, Browser Automation, Web Search, Claude Mem, Granola

---

## Working Principles

1. **Evidence-based decisions** — Data over assumptions, with clear attribution
2. **Executive communication** — BLUF (bottom line up front), clarity over cleverness
3. **Source attribution** — Label claims: SOURCE, ASSUMPTION, INFERENCE, NEEDS VALIDATION
4. **Git workflow** — Frequent checkpoint commits, never force push to main
5. **Quality** — Run typecheck before ending tasks, never commit without explicit approval

---

**Last Updated**: 2026-04-06
**Purpose**: Single unified memory file for AI context across sessions
**Location**: `🤖 AI/memory/memory.md`