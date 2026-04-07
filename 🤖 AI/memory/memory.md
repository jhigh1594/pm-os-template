# Workspace Memory

> Sections marked VOLATILE are overwritten automatically at session end by the LLM extractor.
> Sections marked PERMANENT are never auto-updated — edit manually only.

---

## Current Focus

Two research tracks completed: Track 1 mapped CSM personas, JTBDs, workflows, and journey maps; Track 2 identified ICP profile, market pain points, and competitive gaps. Key finding: CSP's whitespace lies in cross-functional post-sales orchestration (Sales→CS→Support→PS→Product) that no existing competitor addresses, plus solving the AI adoption blocker (data quality fragmentation). Ready for strategic synthesis if user wants to proceed.

## Active Decisions

**Strategic Questions**:

- Whether to perform synthesis pass pulling strongest signals into strategic framing document for CSP (user interrupted before answering)

**Recent Decisions**:

- Parallel agent approach with two distinct research tracks (internal + external)
- Used jtbd, research, and competitive-analysis skills for market mapping
- Both artifacts saved to Knowledge/Market/ directory for future reference


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

**Context Change**: Three strategic insights identified: (1) CS investment paradox—75% NRR decline despite increased CS spend signals model design problem, not tooling; (2) Real whitespace is cross-functional post-sales orchestration—no competitor coordinates full Sales→CS→Support→PS→Product motion; (3) AI adoption blocked by data quality, not ambition—72% say critical but only 32% have live use cases. Session interrupted by login command; final synthesis decision pending.

**Context Change**: Session interrupted during synthesis planning phase. Both research tracks complete with evidence-labeled pain points, ICP buyer personas ($10M–$200M ARR, 10–50 CSMs), purchase triggers, and Bain/TSIA/Gainsight sourced market data.

**Context Change**: Two new research artifacts added to Knowledge/Market folder. Session ended via login command interruption before synthesis phase.

**Context Change**: Three non-obvious strategic findings identified: (1) CS investment paradox—75% saw NRR decline despite 60% increasing spend; (2) whitespace in cross-functional post-sales orchestration (Sales→CS→Support→PS→Product); (3) AI adoption blocked by data quality, not ambition. Session ended before synthesis decision.

**Context Change**: Three non-obvious findings surfaced: (1) CS investment paradox—spending up but NRR declining; root cause is coordination model design, not tooling; (2) Real whitespace is cross-functional orchestration; all competitors are point solutions; (3) AI adoption stuck at 32% live use cases due to data fragmentation, not ambition. ServiceNow's platform architecture positioned as credible answer to whitespace.


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

**Last Updated**: 2026-04-07
**Purpose**: Single unified memory file for AI context across sessions
**Location**: `🤖 AI/memory/memory.md`