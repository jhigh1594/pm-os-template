# Orchestrator Workflow Candidates

Captured 2026-04-04. From a session exploring Level 9→10 (swarm architect) for Claude Code.

**Context:** The goal is a narrow orchestrator that coordinates existing skills + agents toward a multi-step workflow — not a general-purpose swarm. Start with one workflow, validate the pattern, then expand.

**Key constraint:** Skills written for interactive use (approval gates, clarifying questions) need to be rewritten or bypassed for headless orchestration. Agents are cleaner inputs than slash commands.

---

## Candidates

### 1. Customer Discovery Synthesis ⭐ (Best first candidate)

**The manual work today:** Granola syncs meeting transcripts into the workspace. They sit as raw files. Synthesis — themes across interviews, JTBD clusters, signal vs. noise — is done manually.

**What the orchestrator does:**
- Trigger: new Granola transcripts detected (or weekly cron)
- Reader agent processes new transcripts
- Analyst agent clusters themes across sessions, maps to JTBD
- Writer agent updates `📚 Knowledge/Customers/` and surfaces new insights for review

**Why it's the best starting point:**
- Input pipeline already exists (Granola cron sync)
- Timing is ideal — currently in 30-day discovery at SNOW
- Clear output: structured insight brief vs. raw transcript dump
- Mentioned most frequently in Lenny transcripts as the workflow most abandoned due to synthesis cost

---

### 2. Monthly Competitor Deep-Dive → Battlecard Update

**The manual work today:** Daily CI brief covers signals. `/compete` runs a deep dive on demand. But synthesizing into updated battlecards — delta vs. last month, positioning shifts, updating battlecard template — is fully manual.

**What the orchestrator does:**
- Trigger: monthly cron (e.g., 1st of month)
- Spawns `competitive-research` agent for each of 5 primary competitors (from `tracked-competitors.md`)
- Compares findings against previous month's CI briefs in `Knowledge/Market/ci-briefs/`
- Generates delta report + updated battlecards
- Flags anything that should change positioning

**Why it's strong:**
- All infrastructure exists: cron, CI brief output, battlecard template, competitive-research agent, tracked-competitors.md
- Mostly orchestration glue, not new capability

---

### 3. Weekly Stakeholder Update Prep

**The manual work today:** `📁 Workflows/weekly-stakeholder-update/` and `/weekly-review` command exist. But tailoring framing for Garin vs. Amit-level, synthesizing the week's work, drafting — still fully manual.

**What the orchestrator does:**
- Trigger: end-of-week cron (Friday 4pm)
- Reads completed tasks, CI brief deltas, Granola notes from the week
- Generates audience-specific drafts using `Knowledge/Writing-Styles/` (executive, manager)
- Surfaces for edit before sending

**Why it matters:**
- GOALS.md flags "stakeholder misalignment that surfaces late" as a drain
- High asymmetric leverage at 30 days into a new role
- Writing style guides already built for each audience

---

### 4. QPR Prep (Quarterly) — Future candidate

Multi-step, high-value, but lower priority for first orchestrator. QPR is quarterly, the inputs (what shipped, customer data) aren't consistently structured yet, and only one QPR cycle has happened. Strong candidate once the discovery synthesis workflow is working and data is flowing.

---

## Skipped: Win/Loss Analysis

Needs enough deal history first. Not enough data yet. Revisit in ~90 days.

---

## Open questions before building

- Which skills need to be rewritten for headless use (no approval gates)?
- What does "done" look like for each workflow — file written? Slack message? Review queue item?
- How does the orchestrator surface output for human review without requiring interactive approval?
