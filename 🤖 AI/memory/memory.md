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

## Strategic Context (as of 2026-04-07)
- **CS investment paradox**: 75% of firms saw NRR decline despite 60% increased CS spend — root cause is coordination model design, not tooling. (Source: csm-icp-market-research.md)
- **Orchestration whitespace**: No competitor coordinates full Sales→CS→Support→PS→Product post-sales motion. ServiceNow's platform architecture is the only credible answer. (Source: csm-icp-market-research.md)
- **AI adoption blocker**: 72% call AI critical, only 32% have live use cases — blocked by data fragmentation, not ambition. Workflow-byproduct data unification is the unlock. (Source: csm-icp-market-research.md)


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