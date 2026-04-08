# Workspace Memory

> Sections marked VOLATILE are overwritten automatically at session end by the LLM extractor.
> Sections marked PERMANENT are never auto-updated — edit manually only.

---

## Current Focus

Two research artifacts completed and filed in Knowledge/Market/: csm-jtbd-workflows.md (personas, JTBDs, workflows, journey maps) and csm-icp-market-research.md (ICP profile, purchase triggers, pain points, competitive analysis). Awaiting decision on next step (synthesis pass or other direction).

## Active Decisions

**Strategic Questions**:

- Whether to proceed with synthesis pass combining both research tracks into strategic framing document

**Recent Decisions**:

- Used parallel agent approach: jtbd + research/competitive-analysis skills
- Stored research in separate Knowledge/Market/ artifacts (not merged)
- Identified three non-obvious strategic findings: CS investment paradox, cross-functional orchestration whitespace, AI adoption stuck on data quality


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

**Context Change**: New Knowledge/Market files created; strategic competitive positioning identified (ServiceNow CSP as only credible platform for cross-functional post-sales orchestration)

**Context Change**: CSP research foundation complete. Market research reveals ServiceNow's platform architecture as uniquely positioned to address cross-functional post-sales orchestration gap that no current competitor solves. Data quality as AI blocker is actionable insight for product positioning.

**Context Change**: Research surfaced that root cause of NRR decline is coordination/model design, not tooling investment — positioning ServiceNow's workflow orchestration as answering the actual structural problem competitors miss. AI adoption is stuck on data fragmentation as a byproduct of workflow execution, which ServiceNow platform could uniquely address.

**Context Change**: Identified three non-obvious strategic findings: (1) CS investment paradox—NRR declining despite increased CS spend suggests model design problem, not tooling issue; (2) Real whitespace in cross-functional post-sales orchestration (Sales→CS→Support→PS→Product) where ServiceNow has unique platform advantage; (3) AI adoption blocked by data fragmentation, not ambition—platform that unifies post-sales data via workflow execution would unlock AI for majority of teams.

**Context Change**: Completed market research artifacts now available in knowledge system. Identified three non-obvious strategic findings: CS investment paradox, cross-functional orchestration whitespace, and AI adoption data quality blockers.

**Context Change**: Key insight emerged: ServiceNow's workflow orchestration capability uniquely addresses the real market problem (coordination model design, not tooling), which no competitor currently solves. AI adoption in CS is blocked by data fragmentation, not ambition — positioning opportunity for unified post-sales platform.

**Context Change**: Session ended before synthesis decision. User initiated /login command which interrupted ongoing conversation.


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

**Last Updated**: 2026-04-08
**Purpose**: Single unified memory file for AI context across sessions
**Location**: `🤖 AI/memory/memory.md`