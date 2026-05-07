# Learned Patterns

*Last updated: 2026-04-03*
*Total patterns: 10*
*Purpose: Accumulated wisdom that makes future sessions faster and higher quality*

**Separation of concerns:** Workspace conventions, tooling, and repo decisions live here. **PM product decisions** (feature prioritization, roadmap bets, product strategy) go in [product-decisions.md](product-decisions.md). Forecasts and calibration live in [product-judgment-test.md](product-judgment-test.md).

---

## Quality Standard

Every pattern must pass **all 4 gates** before capture:


| Gate            | Question                                      |
| --------------- | --------------------------------------------- |
| **Actionable**  | Can I do something specific with this?        |
| **Specific**    | Is it tied to my context, not generic advice? |
| **Durable**     | Will it be useful in 5+ future sessions?      |
| **Non-obvious** | Is this something I wouldn't naturally know?  |


---

## Decisions Made

*Past decisions with reasoning - prevents re-litigating settled questions*

> **Format**: Context → Options → Chosen → Reasoning → Confidence

### 2026-02-17: Semantic Pattern Capture System

**Context**: Old `learned-patterns.md` captured tool invocations (read→read→read) instead of semantic meaning. Generated noise, not signal.
**Options**:

- (A) Delete files, stop generation - cleanest but loses structure
- (B) Rebuild with semantic capture - higher signal, requires design
- (C) Manual curation only - zero noise, relies on discipline
**Chosen**: B - Semantic capture with AI self-filtering and quality gates
**Reasoning**: Best balance of signal quality and maintainability. Quality gates (Actionable, Specific, Durable, Non-obvious) ensure only valuable patterns are captured. On-demand + weekly cadence prevents noise accumulation.
**Confidence**: Medium (new pattern - will validate over coming weeks)
**Validation**: Check in 1 month if patterns are being referenced and useful

---

## Conventions Discovered

*Workspace-specific patterns that aren't obvious to newcomers*

> **Format**: Pattern → Context → Why → Confidence

### Documentation Convention: PRDs vs Memos

**Pattern**: PRDs go in `Products/[product]/initiatives/`; strategic POV docs go in `Docs/memos/`
**Context**: Creating new documentation
**Why**: PRDs are product-specific and live with the product; memos are cross-product strategic communications
**Confidence**: High (reinforced 3x)

### Scratch Is for Disposable Artifacts Only

**Pattern**: Root `scratch/` holds temp exports and session debris; specs, research, and initiative work live under `📦 Products/...` or `📝 Docs/memos/`
**Context**: Starting exploration notes or saving research during a session
**Why**: Prevents a junk drawer of durable docs that are hard to find and link; matches initiative-first organization
**Confidence**: High

### Memory Structure

**Pattern**: Single `memory.md` file for current state; `learned-patterns.md` for accumulated wisdom
**Context**: Understanding where to find/update context
**Why**: Consolidated from multi-file system - simpler maintenance, faster loading
**Confidence**: High

---

## Mistakes to Avoid

*Painful lessons that save future time*

> **Format**: What happened → Why it failed → How to avoid → Cost saved

### Don't Ask Multiple Questions at Once in Discovery Mode

**What happened**: In `/spec` command discovery phase, asked 3 questions simultaneously instead of one at a time
**Why it failed**: The `/spec` template explicitly says "Ask **one question at a time**; wait for the answer before asking the next" - violated Socratic questioning framework
**How to avoid**: Before asking discovery questions, run this pre-flight checklist:

```
BEFORE ASKING QUESTIONS IN DISCOVERY:
[ ] Am I asking only ONE question?
[ ] Have I explicitly stated I'll wait for the answer?
[ ] Is there a clear stop point for me to pause?
```

**Cost saved**: User frustration, violated protocol, lost trust in following templates

### Never Hallucinate or Fabricate Content

**What happened**: In design brief creation, presented synthesized customer quotes and unverified competitor features as factual — removing "(implied from context)" and "(inferred problem)" qualifiers and not flagging competitor assertions as needing verification
**Why it failed**: Violated truth-in-documentation principle; misrepresented synthesized content as validated research; could mislead stakeholders and propagate unverified claims
**How to avoid**: Always label unverified content explicitly:

- Customer quotes: *[Synthesized pain point]* or *[Representative problem statement]*
- Competitor features: *[NEEDS VERIFICATION]* or *[ASSUMPTION, validate before citing]*
- Statistics/benchmarks: *[Industry benchmark, source TBD]* or *[Assumption, needs validation]*
**Self-check before output**:

1. Do I have a verified source? → Cite it
2. Am I inferring/synthesizing? → Label it
3. Am I assuming? → Flag it
4. Am I making this up? → DELETE IT or use labeled placeholder

**Cost saved**: Credibility damage; misleading stakeholders; building on unverified assumptions

### PRDs Always Belong to Initiatives

**What happened**: Created standalone `prds/` folder separate from initiative folders; PRDs lived in isolation from their associated design briefs and implementation context
**Why it failed**: PRDs became orphaned from their initiative context; harder to find related files; violated principle that PRDs are initiative-specific, not standalone documents
**How to avoid**: Always place PRDs within initiative folders: `📦 Products/[Product]/initiatives/[initiative-name]/[name]-prd.md`

- Small features: Use `--type one-pager` or `--type light` with `/spec` instead of full PRD
- Each initiative folder contains: PRD, design brief, spec-briefs (as needed)
**Cost saved**: Context fragmentation; easier file discovery; clear relationship between requirements and design

---

## Productive Patterns

*Repeatable sequences that produce reliable results*

> **Format**: Trigger → Sequence → Why it works → Confidence

### Plan Index/Reference File Changes Before Editing

**Trigger**: Any session where a shared reference file (COMMAND-REFERENCE.md, INDEX.md, or similar) needs updates
**Sequence**:

1. Read the full file first to understand current structure
2. Plan all changes as a list before making the first edit
3. Batch edits into as few operations as possible

**Why it works**: Without planning, small adjustments cascade into many incremental edits as context shifts — confirmed 3x across separate sessions
**Confidence**: High

### Breaking Down Work: Always Establish Parent/Child and Dependencies

**Trigger**: Creating work items from a PRD, epics from initiatives, stories from epics, or any hierarchical breakdown
**Sequence**:

1. Create the parent items (epics, initiatives, high-level work)
2. Create the child items (stories, tasks)
3. Link parent→child connections
4. Link dependencies between items (e.g., B1 blocked by A1 when B1 builds on A1)

**Why it works**: Keeps breakdown traceable and navigable; surfaces blockers; reflects actual delivery order; enables views by hierarchy and dependency chain
**Confidence**: Medium

---

## Tool-Specific Wisdom

*Domain and tool patterns specific to this workspace*

> **Format**: Tool/Domain → Pattern → Context → Gotchas → Confidence



---

## Validation Log

*Patterns are semantically validated based on session learnings*


| Date       | Pattern                                           | Change                    | Reason                                           |
| ---------- | ------------------------------------------------- | ------------------------- | ------------------------------------------------ |
| 2026-02-17 | Semantic Pattern Capture System                   | Added                     | First decision captured - new system design      |
| 2026-02-17 | Documentation Convention                          | Added                     | PRDs vs Memos distinction                        |
| 2026-02-17 | Memory Structure                                  | Added                     | Single-file system understanding                 |
| 2026-02-17 | File created                                      | Initial structure         | Starting fresh                                   |
| 2026-04-03 | Scratch Is for Disposable Artifacts Only          | Ported from prior workspace | Durable workspace policy                         |
| 2026-04-03 | Don't Ask Multiple Questions at Once              | Ported from prior workspace | Methodology mistake to avoid                     |
| 2026-04-03 | Never Hallucinate or Fabricate Content            | Ported from prior workspace | Critical content integrity rule                  |
| 2026-04-03 | PRDs Always Belong to Initiatives                 | Ported from prior workspace | File placement mistake to avoid                  |
| 2026-04-03 | Plan Index/Reference File Changes Before Editing  | Ported from prior workspace | Confirmed 3x — generalized to any reference file |
| 2026-04-03 | Breaking Down Work: Parent/Child and Dependencies | Ported from prior workspace | Work breakdown methodology                       |


---

## How to Use This File

**On-demand capture**: When you notice a substantial pattern worth remembering:

1. Verify it passes all 4 quality gates
2. Add to appropriate section with confidence level
3. Update validation log

**Weekly review**: At end of week:

1. Review sessions for patterns that emerged
2. Reinforce patterns that worked (increase confidence)
3. Update or deprecate patterns that failed
4. Add new patterns that passed quality gates

**Session startup**: AI loads this file to:

- Apply known conventions automatically
- Avoid known mistakes
- Follow productive patterns
- Reference past decisions

---

*Next review: 2026-04-10*

---

## Auto-Captured Session Patterns

*Auto-promoted from session memory. Haiku-curated decisions and insights — no manual review required. Demote to candidate-patterns.md or delete if stale.*

### Decision — 2026-04-07
**Source**: `🤖 AI/memory/sessions/2026-04-07-2230Z.md`  
Simplified app from 6 views to 3 core views (Brief, Cross-Reference, Deep Dive)

### Decision — 2026-04-07
**Source**: `🤖 AI/memory/sessions/2026-04-07-2230Z.md`  
Embedded all data in JS const rather than fetching from files (single-file design)

### Decision — 2026-04-07
**Source**: `🤖 AI/memory/sessions/2026-04-07-2230Z.md`  
Pain × Persona matrix as centerpiece synthesis tool

### Decision — 2026-04-07
**Source**: `🤖 AI/memory/sessions/2026-04-07-2230Z.md`  
Used keyword heuristics for JTBD-to-pain matching instead of manual curation

### Decision — 2026-04-07
**Source**: `🤖 AI/memory/sessions/2026-04-07-2230Z.md`  
Switched to light theme with CSS variables

### Decision — 2026-04-07
**Source**: `🤖 AI/memory/sessions/2026-04-07-2230Z.md`  
Added workflow/journey toggle using state variable rather than separate views

### Strategic Insight — 2026-04-07
**Source**: `🤖 AI/memory/sessions/2026-04-07-2230Z.md`  
Persona > complexity — simplified from 6 views to 3. Added user journey/workflow data requested by user. Shifted from dark to light theme. Using fuzzy keyword matching rather than explicit mapping to reduce manual curation burden.

### Decision — 2026-04-07
**Source**: `🤖 AI/memory/sessions/2026-04-07-2229Z.md`  
Deployed parallel agents for two distinct research tracks (internal synthesis via jtbd skill + external market research via research/competitive-analysis skills)

### Decision — 2026-04-07
**Source**: `🤖 AI/memory/sessions/2026-04-07-2229Z.md`  
Structured ICP profile around VP/Head of CS at $10M–$200M ARR B2B SaaS with board-level NRR accountability

### Decision — 2026-04-07
**Source**: `🤖 AI/memory/sessions/2026-04-07-2229Z.md`  
Identified three purchase triggers: renewal disaster, headcount freeze + growth pressure, board mandate for cohort reporting

### Strategic Insight — 2026-04-07
**Source**: `🤖 AI/memory/sessions/2026-04-07-2229Z.md`  
CSP research foundation complete. Market research reveals ServiceNow's platform architecture as uniquely positioned to address cross-functional post-sales orchestration gap that no current competitor solves. Data quality as AI blocker is actionable insight for product positioning.

### Decision — 2026-04-07
**Source**: `🤖 AI/memory/sessions/2026-04-07-2229Z-1.md`  
Disabled session_end.py hook to prevent dual extraction (kept only pre_clear_capture.py on UserPromptSubmit)

### Decision — 2026-04-07
**Source**: `🤖 AI/memory/sessions/2026-04-07-2229Z-1.md`  
Added filename existence check in write_session_file() to prevent overwriting with fresh timestamps

### Decision — 2026-04-07
**Source**: `🤖 AI/memory/sessions/2026-04-07-2229Z-1.md`  
Kept 2026-04-07-2140Z-0.md (most complete context) and deleted 4 near-duplicate files

### Strategic Insight — 2026-04-07
**Source**: `🤖 AI/memory/sessions/2026-04-07-2229Z-1.md`  
Session extraction is now deduplication-safe. The memory system will no longer create multiple files for the same transcript on /clear commands.

### Decision — 2026-04-07
**Source**: `🤖 AI/memory/sessions/2026-04-07-2140Z.md`  
Replaced guest-insights extraction with session-file extraction — session files are the authoritative insight source (9 precise candidates vs 249 bootstrapped entries)

### Decision — 2026-04-07
**Source**: `🤖 AI/memory/sessions/2026-04-07-2140Z.md`  
Built UserPromptSubmit hook intercept for /clear rather than requiring manual /checkpoint — eliminated user burden

### Decision — 2026-04-07
**Source**: `🤖 AI/memory/sessions/2026-04-07-2140Z.md`  
Pattern extractor stages candidates with hash-based deduplication to prevent duplicates across runs

### Strategic Insight — 2026-04-07
**Source**: `🤖 AI/memory/sessions/2026-04-07-2140Z.md`  
Memory architecture transitioned from 'architecturally designed for autonomous learning but broken in practice' to 'fully working end-to-end.' Verified hook registration, tested session extraction, confirmed pattern extraction catches new insights. System now auto-updates on every /clear without user intervention.

### Decision — 2026-04-07
**Source**: `🤖 AI/memory/sessions/2026-04-07-2140Z-1.md`  
Disabled `python.terminal.activateEnvironment` in `.vscode/settings.json` to prevent auto-activation

### Strategic Insight — 2026-04-07
**Source**: `🤖 AI/memory/sessions/2026-04-07-2140Z-1.md`  
Workspace settings updated — Python extension will no longer auto-activate `.venv` in new terminals. Manual activation and explicit `.venv/bin/python` calls still work.

### Decision — 2026-04-07
**Source**: `🤖 AI/memory/sessions/2026-04-07-2102Z.md`  
Architecture: server-side terminal launching (osascript) instead of client-side shell function

### Decision — 2026-04-07
**Source**: `🤖 AI/memory/sessions/2026-04-07-2102Z.md`  
Extraction strategy: background process at session-start hook to retroactively extract summaries from JSONL

### Decision — 2026-04-07
**Source**: `🤖 AI/memory/sessions/2026-04-07-2102Z.md`  
Card display: Summary, Focus, first Open Question (extracted by Claude Haiku at session end or retroactively)

### Strategic Insight — 2026-04-07
**Source**: `🤖 AI/memory/sessions/2026-04-07-2102Z.md`  
Discovered sessions weren't being captured because Stop hook only fires on clean exits (Ctrl+C), not terminal closes. Switched to retroactive extraction at session start as the reliable capture point.

### Strategic Insight — 2026-04-07
**Source**: `🤖 AI/memory/sessions/2026-04-07-1759Z-1.md`  
User has a /compete command available for manual runs but hasn't automated it yet

### Decision — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-07-2229Z.md`  
Spin up parallel agents for internal synthesis (Track 1) and external market research (Track 2)

### Decision — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-07-2229Z.md`  
Use jtbd skill for JTBD/journey mapping, research and competitive-analysis skills for market data

### Decision — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-07-2229Z.md`  
Structured competitive findings with evidence labels and disconfirming evidence sections per project standards

### Strategic Insight — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-07-2229Z.md`  
Completed market research artifacts now available in knowledge system. Identified three non-obvious strategic findings: CS investment paradox, cross-functional orchestration whitespace, and AI adoption data quality blockers.

### Decision — 2026-04-06
**Source**: `🤖 AI/memory/sessions/2026-04-08-1608Z.md`  
Chose Mermaid diagrams over ASCII art for OST visualization (enables dashboard integration and better consumption)

### Decision — 2026-04-06
**Source**: `🤖 AI/memory/sessions/2026-04-08-1608Z.md`  
Applied context-first consultative approach to match your workspace conventions instead of the original output-first marketplace style

### Decision — 2026-04-06
**Source**: `🤖 AI/memory/sessions/2026-04-08-1608Z.md`  
Encoded semantic meaning into Mermaid shapes: stadiums for outcomes, hexagons for opportunities, rectangles for solutions

### Strategic Insight — 2026-04-06
**Source**: `🤖 AI/memory/sessions/2026-04-08-1608Z.md`  
New skill added to registry and LEARNED.md stub created. Skill now reads your actual workspace structure rather than assuming generic paths.

### Decision — 2026-04-07
**Source**: `🤖 AI/memory/sessions/2026-04-08-1607Z.md`  
Create new commercial-lens skill (not fold into existing business-reasoning)

### Decision — 2026-04-07
**Source**: `🤖 AI/memory/sessions/2026-04-08-1607Z.md`  
Run commercial research and probabilistic planning in parallel

### Decision — 2026-04-07
**Source**: `🤖 AI/memory/sessions/2026-04-08-1607Z.md`  
Execute skill building and upgrading in parallel with no file overlap

### Strategic Insight — 2026-04-07
**Source**: `🤖 AI/memory/sessions/2026-04-08-1607Z.md`  
AIPMOS expanded from missing skills gap to 5 new/upgraded skill artifacts (1 new + 4 upgrades), filling commercial reasoning and probabilistic thinking coverage gaps identified in existing skills.

### Decision — 2026-04-06
**Source**: `🤖 AI/memory/sessions/2026-04-08-0240Z.md`  
Wired 6 hooks (InstructionsLoaded, PreCompact, PostToolUse, etc.) into .claude/settings.local.json to activate the learning pipeline

### Decision — 2026-04-06
**Source**: `🤖 AI/memory/sessions/2026-04-08-0240Z.md`  
Confirmed Python learning infrastructure copied from prior workspace is workspace-generic and functional in SNOW-Work without modification

### Strategic Insight — 2026-04-06
**Source**: `🤖 AI/memory/sessions/2026-04-08-0240Z.md`  
The skill learning system transitioned from scaffolded-but-inactive to fully operational. The missing piece was hook wiring, not Python infrastructure—this was already present from prior workspace implementation.

### Decision — 2026-04-02
**Source**: `🤖 AI/memory/sessions/2026-04-08-0239Z.md`  
Feedback on overconfident rank claims is valid — requires calibrated language and evidence methodology

### Decision — 2026-04-02
**Source**: `🤖 AI/memory/sessions/2026-04-08-0239Z.md`  
Adding Section 6 (Why Sophisticated Buyers Still Choose PlanHat) as structural improvement to acknowledge competitive moats honestly

### Decision — 2026-04-02
**Source**: `🤖 AI/memory/sessions/2026-04-08-0239Z.md`  
Narrowing strategic implications from 7 parallel recommendations to 3 prioritized bets per feedback

### Strategic Insight — 2026-04-02
**Source**: `🤖 AI/memory/sessions/2026-04-08-0239Z.md`  
Competitive analysis now subject to higher evidence rigor standard; peer feedback established that confidence must match evidence tier (direct quotes vs. synthesis vs. inference); moat acknowledgment is now seen as strategically important rather than weakness.

### Decision — 2026-04-06
**Source**: `🤖 AI/memory/sessions/2026-04-07-2345Z.md`  
Run parallel agents for two distinct research tracks: internal JTBD/journey synthesis and external market/competitive ICP research

### Decision — 2026-04-06
**Source**: `🤖 AI/memory/sessions/2026-04-07-2345Z.md`  
Output to separate structured markdown artifacts in Knowledge/Market/ rather than consolidating initially

### Decision — 2026-04-06
**Source**: `🤖 AI/memory/sessions/2026-04-07-2345Z.md`  
Use interactive single-file HTML (CSS custom properties + tab navigation) as the synthesis/digestion tool

### Strategic Insight — 2026-04-06
**Source**: `🤖 AI/memory/sessions/2026-04-07-2345Z.md`  
Research revealed the CS investment paradox (75% NRR decline despite 60% increased CS spend per Bain 2024) and identified three critical handoff failures (Sales→PS, PS→CSM, CSM→Renewal) as high-leverage problems. Planhat competitive analysis emerged as the richest existing validation source in the workspace.

### Decision — 2026-04-07
**Source**: `🤖 AI/memory/sessions/2026-04-07-2344Z.md`  
Deleted 15 empty session-intent.json files from sessions-archive/ (were useless, only timestamps with no intent data)

### Decision — 2026-04-07
**Source**: `🤖 AI/memory/sessions/2026-04-07-2344Z.md`  
Removed dead code from session_end.py: archive_and_reset_session_intent(), run_pattern_extraction(), session_synthesis.py call from session-start.sh

### Decision — 2026-04-07
**Source**: `🤖 AI/memory/sessions/2026-04-07-2344Z.md`  
Built three-tier memory: permanent memory.md, rolling 10 sessions/, archive 50+ compacted; LLM extractor runs at session end

### Decision — 2026-04-07
**Source**: `🤖 AI/memory/sessions/2026-04-07-2344Z.md`  
Use claude -p CLI for extraction (no separate API key needed, inherits session auth)

### Strategic Insight — 2026-04-07
**Source**: `🤖 AI/memory/sessions/2026-04-07-2344Z.md`  
Reviewed Gravity Claw's three-tier memory system. Discovered automatic fact extraction (after every exchange) as the key gap in current SNOW-Work system. Now implemented: LLM reads .specstory transcript → extracts session_summary, current_focus, key_decisions, open_questions as JSON → patches memory.md volatile sections in-place each session end.

### Decision — 2026-04-07
**Source**: `🤖 AI/memory/sessions/2026-04-07-2231Z.md`  
Abandoned pre_clear_capture.py hook approach (architecturally broken — UserPromptSubmit doesn't fire for built-in CLI commands)

### Decision — 2026-04-07
**Source**: `🤖 AI/memory/sessions/2026-04-07-2231Z.md`  
Implemented rolling-state.json mechanism to capture work state after each turn

### Decision — 2026-04-07
**Source**: `🤖 AI/memory/sessions/2026-04-07-2231Z.md`  
Updated session-start.sh recovery logic to check for .specstory transcripts in addition to intent field

### Strategic Insight — 2026-04-07
**Source**: `🤖 AI/memory/sessions/2026-04-07-2231Z.md`  
Discovered fundamental platform constraint: UserPromptSubmit hooks don't fire for built-in Claude Code commands like /clear — they're intercepted by CLI before hook system runs. This is not a code bug but an architectural limitation.

### Decision — 2026-04-07
**Source**: `🤖 AI/memory/sessions/2026-04-07-2230Z-1.md`  
Commit changes directly to main instead of creating a PR

### Decision — 2026-04-07
**Source**: `🤖 AI/memory/sessions/2026-04-07-2230Z-1.md`  
.specstory/ directory was handled (included or excluded per user's 'PR merged' confirmation)

### Strategic Insight — 2026-04-07
**Source**: `🤖 AI/memory/sessions/2026-04-07-2230Z-1.md`  
User prefers direct commits over PRs for this workspace (indicated by 'No PR needed' feedback)

### Decision — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-07-2229Z.md`  
Use parallel agents for two distinct research tracks (internal JTBD synthesis + external market research)

### Decision — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-07-2229Z.md`  
Maintain two separate artifacts rather than merging (internal vs. external sources)

### Decision — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-07-2229Z.md`  
Structure ICP profile around $10M–$200M ARR B2B SaaS with 10–50 CSMs

### Strategic Insight — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-07-2229Z.md`  
Key insight emerged: ServiceNow's workflow orchestration capability uniquely addresses the real market problem (coordination model design, not tooling), which no competitor currently solves. AI adoption in CS is blocked by data fragmentation, not ambition — positioning opportunity for unified post-sales platform.

### Decision — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-1610Z.md`  
Remove all legacy tools references from codebase and config files

### Decision — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-1610Z.md`  
Keep session continuity guidance in project CLAUDE.md (compressed, not expanded)

### Decision — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-1610Z.md`  
Delete industry-intelligence skill — internal platform doesn't need Gartner/Forrester analyst briefings

### Decision — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-1610Z.md`  
Treat internal enablement and stakeholder comms with same rigor as external launch (launch-execution stays as-is)

### Decision — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-1610Z.md`  
Don't include directory tree in CLAUDE.md — Claude can figure it out

### Strategic Insight — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-1610Z.md`  
Global rules apply to all projects, not just SNOW. Important session correction: assistant was called out for making skill recommendations before reading files — established principle that recommendations require reading and understanding context first.

### Decision — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-1918Z.md`  
Used parallel agents for two distinct research tracks: internal synthesis vs. external market research

### Decision — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-1918Z.md`  
Created two knowledge documents: csm-jtbd-workflows.md and csm-icp-market-research.md

### Decision — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-1918Z.md`  
Identified three strategic findings: (1) CS investment paradox shows model design problem, (2) whitespace in cross-functional post-sales orchestration, (3) AI adoption blocked by data quality not tooling

### Strategic Insight — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-1918Z.md`  
Market research complete with 15+ sourced studies; competitive analysis identified that no existing CS platform (Gainsight, Planhat, Totango) coordinates full post-sales motion—ServiceNow's platform architecture positions as unique solution.

### Strategic Insight — 2026-04-07
**Source**: `🤖 AI/memory/sessions/2026-04-08-1847Z-1.md`  
Confirmed no existing automated competitive analysis infrastructure (no cron jobs, hooks, or triggers) — only manual `/compete` command available

### Decision — 2026-04-07
**Source**: `🤖 AI/memory/sessions/2026-04-08-1847Z.md`  
Modified pre_clear_capture.py to trigger only on /session-save, not every /clear (removes half of duplicate sources)

### Decision — 2026-04-07
**Source**: `🤖 AI/memory/sessions/2026-04-08-1847Z.md`  
Added deduplication check in write_session_file() to skip writing if session file already exists

### Decision — 2026-04-07
**Source**: `🤖 AI/memory/sessions/2026-04-08-1847Z.md`  
Retained 2026-04-08-0107Z.md as the authoritative file (most complete content with all 3 strategic findings)

### Strategic Insight — 2026-04-07
**Source**: `🤖 AI/memory/sessions/2026-04-08-1847Z.md`  
Session extraction hook system is now reliable; no more duplicate files from multiple hook firings. Memory directory cleanup complete.

### Decision — 2026-04-07
**Source**: `🤖 AI/memory/sessions/2026-04-08-1736Z.md`  
Disabled Python venv auto-activation in `.vscode/settings.json` with `"python.terminal.activateEnvironment": false`

### Strategic Insight — 2026-04-07
**Source**: `🤖 AI/memory/sessions/2026-04-08-1736Z.md`  
Terminal startup behavior changed — venv no longer auto-activates. This applies to both VS Code and Cursor (they share workspace settings).

### Decision — 2026-04-07
**Source**: `🤖 AI/memory/sessions/2026-04-08-1735Z.md`  
Session files in 🤖 AI/memory/sessions/ are the authoritative insight source, not guest-insights reference material

### Decision — 2026-04-07
**Source**: `🤖 AI/memory/sessions/2026-04-08-1735Z.md`  
Implemented pre_clear_capture.py hook to intercept /clear via UserPromptSubmit before CLI processes the command

### Decision — 2026-04-07
**Source**: `🤖 AI/memory/sessions/2026-04-08-1735Z.md`  
Two-hook UserPromptSubmit system: pre_clear_capture.py runs first (synchronous, blocking) for /clear detection, followed by general input tracking

### Strategic Insight — 2026-04-07
**Source**: `🤖 AI/memory/sessions/2026-04-08-1735Z.md`  
Discovered memory architecture was partially broken — paths existed but guest-insights were wrong source. Session files produce 9 precisely targeted candidates vs. 249-entry guest-insight dump, showing dramatic quality improvement. System is now autonomous for memory updates on every /clear without requiring user to run /checkpoint.

### Decision — 2026-04-07
**Source**: `🤖 AI/memory/sessions/2026-04-08-1613Z.md`  
Reverse-engineer the LinkedIn post's insight as 'visual layer making the invisible visible' — UUIDs become clickable cards

### Decision — 2026-04-07
**Source**: `🤖 AI/memory/sessions/2026-04-08-1613Z.md`  
Patch session_extractor.py to capture JSONL UUID at session end for resumption

### Decision — 2026-04-07
**Source**: `🤖 AI/memory/sessions/2026-04-08-1613Z.md`  
Create launcher.py as a terminal session board (3-column grid, Forest Green + Paper palette)

### Decision — 2026-04-07
**Source**: `🤖 AI/memory/sessions/2026-04-08-1613Z.md`  
Change Resume architecture: server launches new terminal tab via osascript instead of taking over current shell

### Decision — 2026-04-07
**Source**: `🤖 AI/memory/sessions/2026-04-08-1613Z.md`  
Shift from session-end extraction (unreliable due to SIGHUP) to session-start retroactive extraction

### Strategic Insight — 2026-04-07
**Source**: `🤖 AI/memory/sessions/2026-04-08-1613Z.md`  
Discovered the root blocker: session extraction at end doesn't work because terminal close (SIGHUP) kills Claude before hooks run. Pivoted the entire strategy to extract retroactively at session-start instead, which fires reliably.

### Decision — 2026-04-07
**Source**: `🤖 AI/memory/sessions/2026-04-08-1612Z.md`  
Used Shubham Saboo's profile structure as the template for Jon's README

### Decision — 2026-04-07
**Source**: `🤖 AI/memory/sessions/2026-04-08-1612Z.md`  
Adopted 'PM · Builder · Systems Thinker' as the positioning framing

### Decision — 2026-04-07
**Source**: `🤖 AI/memory/sessions/2026-04-08-1612Z.md`  
Positioned PM-OS as 'complete operating system for PMs who want more leverage and impact with AI' rather than just listing features

### Decision — 2026-04-07
**Source**: `🤖 AI/memory/sessions/2026-04-08-1612Z.md`  
Pushed the final README to production

### Strategic Insight — 2026-04-07
**Source**: `🤖 AI/memory/sessions/2026-04-08-1612Z.md`  
User clarified their actual positioning: Sr. PM at ServiceNow building an AI-powered customer success platform by day, builder and solopreneur by night — this distinction became central to the README's messaging and tone.

### Decision — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-1918Z.md`  
Parallel agents for two distinct tracks: internal JTBD synthesis + external competitive/market research

### Decision — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-1918Z.md`  
Focus on three non-obvious findings: CS investment paradox (coordination model problem, not tooling), cross-functional post-sales orchestration whitespace (ServiceNow's differentiator), and AI adoption blocked by data quality not ambition

### Decision — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-1918Z.md`  
ICP profile defined: VP/Head CS at B2B SaaS, $10M–$200M ARR, 10–50 CSMs, NRR accountability

### Strategic Insight — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-1918Z.md`  
Research validated that ServiceNow's workflow orchestration platform architecture is positioned to solve the actual root causes in customer success market—not as a point solution competitor but as the only credible cross-functional platform for post-sales coordination.

### Decision — 2026-04-07
**Source**: `🤖 AI/memory/sessions/2026-04-08-1921Z.md`  
Excluded .specstory/ from commit (left as untracked)

### Decision — 2026-04-07
**Source**: `🤖 AI/memory/sessions/2026-04-08-1921Z.md`  
Merged PR without keeping the feature branch

### Strategic Insight — 2026-04-07
**Source**: `🤖 AI/memory/sessions/2026-04-08-1921Z.md`  
Launcher scripts removed from codebase; session configuration files updated; back on main with remote synchronized

### Decision — 2026-04-07
**Source**: `🤖 AI/memory/sessions/2026-04-08-1920Z-2.md`  
Created new commercial-lens skill rather than expanding business-reasoning (distinct lens needed)

### Decision — 2026-04-07
**Source**: `🤖 AI/memory/sessions/2026-04-08-1920Z-2.md`  
Upgraded 4 existing skills in parallel rather than creating one monolithic probabilistic-thinking skill

### Decision — 2026-04-07
**Source**: `🤖 AI/memory/sessions/2026-04-08-1920Z-2.md`  
Used two parallel research agents with separate artifacts to avoid duplication and manage complexity

### Decision — 2026-04-07
**Source**: `🤖 AI/memory/sessions/2026-04-08-1920Z-2.md`  
Merged to main without PR — all work already in HEAD

### Strategic Insight — 2026-04-07
**Source**: `🤖 AI/memory/sessions/2026-04-08-1920Z-2.md`  
AIPMOS expansion complete. Session memory pruned (21 stale files removed, 15 new added). Validated two-track parallel research approach for complex skill development work.

### Decision — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-1920Z-1.md`  
Added Step 3.5 to /spec workflow: autonomous review using three lenses (strategic via product-taste-intuition, product taste taste-intuition, copy via elite-copywriter) before presenting draft specs

### Decision — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-1920Z-1.md`  
Decided to sync /spec changes across both SNOW-Work and pm-os-template to keep them in sync

### Strategic Insight — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-1920Z-1.md`  
The /spec workflow now has built-in autonomous polish before user review. Established pattern: changes affecting both SNOW-Work and pm-os-template should be kept synchronized to prevent template drift.

### Decision — 2026-04-05
**Source**: `🤖 AI/memory/sessions/2026-04-08-1920Z.md`  
Added ai-product-strategy skill (12 principles, 94 guests from repo)

### Decision — 2026-04-05
**Source**: `🤖 AI/memory/sessions/2026-04-08-1920Z.md`  
Added ai-evals skill with references

### Decision — 2026-04-05
**Source**: `🤖 AI/memory/sessions/2026-04-08-1920Z.md`  
Updated product-taste-intuition description to match repo version

### Decision — 2026-04-05
**Source**: `🤖 AI/memory/sessions/2026-04-08-1920Z.md`  
Installed managing-up skill after assessing fit—decided YES due to Jon's named manager (Garin Landry) and new product CSP context

### Decision — 2026-04-05
**Source**: `🤖 AI/memory/sessions/2026-04-08-1920Z.md`  
Improved managing-up SKILL.md with HPM template, diagnostic table, and enterprise/new-product-specific guidance

### Strategic Insight — 2026-04-05
**Source**: `🤖 AI/memory/sessions/2026-04-08-1920Z.md`  
Workspace now has managing-up as an active skill tailored to Jon's enterprise PM role with established manager relationship—fills gap between exec-comms and stakeholder-management for upstream alignment on a new product without established metrics.

### Decision — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-1918Z.md`  
Parallel agents approach: Track 1 (internal jtbd + research skills) and Track 2 (research + competitive-analysis skills)

### Decision — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-1918Z.md`  
Save research outputs to Knowledge/Market folder structure

### Decision — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-1918Z.md`  
Three strategic findings prioritized: CS investment paradox, cross-functional orchestration whitespace, AI adoption data quality blocker

### Strategic Insight — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-1918Z.md`  
Identified ServiceNow CSP's strategic positioning advantage over point-solution competitors (Gainsight, Planhat, Totango) in cross-functional post-sales orchestration and AI-enabling data unification.

### Decision — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-1918Z.md`  
Used parallel agents for two distinct research tracks (internal JTBD mapping + external market research)

### Decision — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-1918Z.md`  
Applied evidence-labeling and disconfirming-evidence sections (per established competitive-docs feedback)

### Decision — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-1918Z.md`  
Identified three strategic whitespace opportunities: CS investment paradox (coordination model), cross-functional post-sales orchestration gap, and AI adoption blocked by data fragmentation

### Strategic Insight — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-1918Z.md`  
Discovered non-obvious market insight: ServiceNow's workflow orchestration competency directly addresses root causes of NRR decline that competitors (point solutions) cannot solve. No current CS platform unifies post-sales data as byproduct of workflow execution.

### Decision — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-1918Z.md`  
Structured ICP findings with evidence labels and source citations per competitive standards

### Strategic Insight — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-1918Z.md`  
Two Knowledge/Market/ artifacts now created and ready. Clear positioning angle identified: ServiceNow owns the cross-functional post-sales orchestration layer no existing CS platform provides.

### Decision — 2026-04-07
**Source**: `🤖 AI/memory/sessions/2026-04-08-2209Z.md`  
Simplified app from 6 views to 3 views (Brief, Cross-Reference, Deep Dive)

### Decision — 2026-04-07
**Source**: `🤖 AI/memory/sessions/2026-04-08-2209Z.md`  
Embedded all research data in a JS const object rather than fetching from files (works offline)

### Decision — 2026-04-07
**Source**: `🤖 AI/memory/sessions/2026-04-08-2209Z.md`  
Organized data as persona ID × pain intensity matrix to avoid runtime lookups

### Decision — 2026-04-07
**Source**: `🤖 AI/memory/sessions/2026-04-08-2209Z.md`  
Used keyword heuristics to auto-match JTBDs to pain points rather than manual mapping

### Decision — 2026-04-07
**Source**: `🤖 AI/memory/sessions/2026-04-08-2209Z.md`  
Switched to light theme with inverted color hierarchy

### Decision — 2026-04-07
**Source**: `🤖 AI/memory/sessions/2026-04-08-2209Z.md`  
Added workflows and journey timeline as toggleable sections in the Brief view using CSS pseudo-elements for timeline visualization

### Strategic Insight — 2026-04-07
**Source**: `🤖 AI/memory/sessions/2026-04-08-2209Z.md`  
App evolved from a read-only pain matrix explorer to include dynamic workflow and user journey visualization. Theme shifted from dark to light. Data structure optimized for both brief 5-minute exploration and 30-minute deep dives.

### Decision — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-1918Z.md`  
Used parallel agents for two distinct tracks: internal JTBD/journey mapping and external market/competitive research

### Decision — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-1918Z.md`  
Applied jtbd, research, and competitive-analysis skills

### Decision — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-1918Z.md`  
Identified cross-functional post-sales orchestration as the strategic whitespace for CSP positioning

### Strategic Insight — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-1918Z.md`  
Three non-obvious strategic findings emerged: (1) CS investment paradox—companies increasing CS spend but declining NRR due to model design issues; (2) no competitor coordinates full post-sales workflow (Sales→CS→Support→PS→Product); (3) AI adoption blocked by data fragmentation, not ambition. These frame ServiceNow's unique positioning opportunity.

### Decision — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-1918Z.md`  
Split research into two parallel agent tracks (internal JTBD synthesis vs external market research)

### Decision — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-1918Z.md`  
Save artifacts to Knowledge/Market/ directory with evidence labeling and disconfirming evidence sections

### Decision — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-1918Z.md`  
Used parallel agents for two research tracks (internal JTBD/workflows vs external market/competitive research)

### Decision — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-1918Z.md`  
Identified three strategic findings: CS investment paradox (coordination model problem), cross-functional post-sales orchestration whitespace (ServiceNow platform advantage), and AI adoption blocked by data fragmentation

### Strategic Insight — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-1918Z.md`  
Two new knowledge artifacts created in Knowledge/Market folder (csm-jtbd-workflows.md and csm-icp-market-research.md) with extensive research on CSM personas, workflows, buying triggers, pain points, and competitive gaps

### Decision — 2026-04-07
**Source**: `🤖 AI/memory/sessions/2026-04-08-2210Z.md`  
Abandoned pre_clear_capture.py hook approach — UserPromptSubmit doesn't fire for built-in CLI commands (architectural constraint)

### Decision — 2026-04-07
**Source**: `🤖 AI/memory/sessions/2026-04-08-2210Z.md`  
Implemented rolling-state.json written by end_of_turn.py to track work persistence across /clear

### Decision — 2026-04-07
**Source**: `🤖 AI/memory/sessions/2026-04-08-2210Z.md`  
Updated session-start.sh recovery logic to check both intent field AND transcript existence before recovering

### Strategic Insight — 2026-04-07
**Source**: `🤖 AI/memory/sessions/2026-04-08-2210Z.md`  
Discovered that UserPromptSubmit hooks are intercepted by CLI before hook system processes them — only SessionEnd fires on actual exit. This invalidates the original capture strategy but rolling-state provides equivalent signal.

### Decision — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-1918Z.md`  
Spin up parallel agents for two distinct research tracks (internal JTBD synthesis vs external market/competitive research)

### Decision — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-1918Z.md`  
Generate two separate knowledge artifacts rather than merge immediately

### Decision — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-1918Z.md`  
ICP profile: VP/Head CS at B2B SaaS, $10M–$200M ARR, 10–50 CSMs with NRR accountability

### Strategic Insight — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-1918Z.md`  
Three non-obvious market findings emerged: (1) CS investment paradox—75% NRR decline despite 60% CS spend increase, rooted in coordination model design, not tooling; (2) Real whitespace is cross-functional post-sales orchestration (Sales→CS→Support→PS→Product), which no existing CS platform coordinates; (3) AI adoption stuck on data quality bottleneck (72% say AI critical, only 32% have live use cases), platform that unifies post-sales data as workflow byproduct would unlock majority market.

### Decision — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-1918Z.md`  
Used parallel agent approach for two distinct research tracks (internal JTBD vs. external market research)

### Decision — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-1918Z.md`  
Identified three non-obvious strategic insights: CS investment paradox, cross-functional post-sales orchestration whitespace, and AI adoption bottleneck on data quality

### Decision — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-1918Z.md`  
Structured output as two knowledge artifacts with signal-labeled pain points and source citations

### Strategic Insight — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-1918Z.md`  
Research established that ServiceNow's workflow orchestration capability addresses the root cause of CS team underperformance (coordination model design), not just a tooling gap. No competitor currently coordinates the full Sales→CS→Support→PS→Product motion.

### Decision — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-1918Z.md`  
Apply jtbd and research skills with competitive-analysis for Track 2

### Decision — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-1918Z.md`  
Create separate artifacts for workflows/JTBDs and market ICP data

### Decision — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-1918Z.md`  
Evidence labeling and disconfirming evidence sections required in market research deliverable

### Strategic Insight — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-1918Z.md`  
Session interrupted by user login command at 2026-04-07 00:05:45Z; research phase appears complete but synthesis/next steps unclear.

### Decision — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-1918Z.md`  
Use parallel agents to split internal JTBD research and external market/competitive research

### Decision — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-1918Z.md`  
Track 2 sourced 15+ studies to identify three non-obvious strategic findings: CS investment paradox, cross-functional orchestration whitespace, AI adoption data quality blockers

### Strategic Insight — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-1918Z.md`  
Two research artifacts saved to Knowledge/Market/ directory; identified that ServiceNow's platform orchestration capability uniquely positions CSP to address root cause of CS NRR decline (coordination model, not tooling) and own cross-functional post-sales whitespace no competitor currently addresses.

### Decision — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-2210Z-1.md`  
Extract Karpathy's framing (living knowledge artifact maintenance) rather than implementing his tools directly

### Decision — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-2210Z-1.md`  
Implement 5 specific improvements to existing system (lint prompt, cross-references, dedupe, hypotheses, conventions)

### Decision — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-2210Z-1.md`  
Use ultraplan orchestration to execute changes remotely

### Decision — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-2210Z-1.md`  
Keep archived patterns in candidate-patterns.md rather than migrating (no duplication)

### Strategic Insight — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-2210Z-1.md`  
Knowledge system architecture updated with maintenance-first approach. memory.md reduced 35 lines (duplicate context entries removed), learned-patterns.md reduced 288 lines (staged for future extraction), and new lint prompt + conventions added to prevent knowledge decay.

### Decision — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-1918Z.md`  
Use parallel agents for two research tracks (internal JTBD synthesis + external market/competitive research)

### Decision — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-1918Z.md`  
Document findings in separate Knowledge files (not merged initially)

### Decision — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-1918Z.md`  
Focus ICP on VP/Head CS at $10M–$200M ARR B2B SaaS with NRR accountability

### Strategic Insight — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-1918Z.md`  
Non-obvious competitive finding: no existing CS platform (Gainsight, Planhat, Totango) coordinates full post-sales workflow (Sales→CS→Support→PS→Product); ServiceNow's platform architecture is the only credible way to own this whitespace.

### Decision — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-1918Z.md`  
Spin up parallel agents for two distinct research tracks: internal JTBD/journey synthesis and external market/competitive research

### Decision — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-1918Z.md`  
Use jtbd, research, and competitive-analysis skills to map workflows, pain points, and competitive positioning

### Decision — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-1918Z.md`  
Structure output with persona-specific JTBDs, user journey maps, signal-labeled pain points, disconfirming evidence, and burning problems

### Strategic Insight — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-1918Z.md`  
Session interrupted by user login command before synthesis decision was made. Research artifacts ready for next phase.

### Decision — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-1918Z.md`  
Structure research with evidence labeling, source citations, and disconfirming evidence sections

### Strategic Insight — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-1918Z.md`  
Two major knowledge artifacts added to Knowledge/Market/ directory. Research surfaced specific ServiceNow CSP competitive positioning around workflow orchestration and data unification — addresses ICP's actual root problems, not just point-solution tooling.

### Decision — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-1918Z.md`  
Spun up two parallel agents: JTBD skill for internal mapping, research + competitive-analysis for external market research

### Decision — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-1918Z.md`  
Structured outputs as two separate Knowledge/Market files with evidence labeling and disconfirming sections

### Decision — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-1918Z.md`  
Identified cross-functional post-sales orchestration as ServiceNow's key whitespace advantage vs point-solution competitors

### Strategic Insight — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-1918Z.md`  
Session reveals three strategic non-obvious findings: CS investment paradox (75% NRR decline despite 60% spending increase), no competitor orchestrates full Sales→CS→Support→PS→Product motion, and AI adoption blocked by data fragmentation—not ambition.

### Decision — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-1918Z.md`  
Create two separate artifact files, not merged

### Decision — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-1918Z.md`  
Focus research on three strategic findings: CS investment paradox, cross-functional orchestration whitespace, AI adoption bottleneck on data quality

### Strategic Insight — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-1918Z.md`  
Research surfaced non-obvious strategic positioning: ServiceNow's workflow orchestration competency directly addresses root causes of CS spend inefficiency, and no competitor coordinates full post-sales motion (Sales→CS→Support→PS→Product). AI adoption blocker is data fragmentation, not ambition—platform that unifies post-sales data as workflow byproduct would unlock majority of teams.

### Decision — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-1918Z.md`  
Created separate knowledge artifacts rather than merged output

### Decision — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-1918Z.md`  
Identified cross-functional post-sales orchestration as primary whitespace vs. point-solution competitors

### Strategic Insight — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-1918Z.md`  
Established ServiceNow's unique platform positioning: only credible way to own cross-functional post-sales orchestration (Sales→CS→Support→PS→Product). Reframed CS investment paradox as coordination model problem, not tooling. Identified data quality fragmentation as the actual blocker to AI adoption in post-sales (72% want AI, only 32% have 1+ live use case).

### Decision — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-1918Z.md`  
Use parallel agents for dual research tracks (internal JTBD vs. external market/competitive)

### Decision — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-1918Z.md`  
Use jtbd, research, and competitive-analysis skills for respective tracks

### Decision — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-1918Z.md`  
Output to separate markdown files in Knowledge/Market/ with evidence labeling and disconfirming evidence sections

### Strategic Insight — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-1918Z.md`  
Three non-obvious strategic findings identified: (1) CS investment paradox (NRR declining despite increased spend), (2) whitespace in cross-functional post-sales orchestration, (3) AI adoption blocked by data quality not ambition.

### Decision — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-1918Z.md`  
Track 1: JTBD skill + csm-journey project exploration for workflows and personas

### Decision — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-1918Z.md`  
Track 2: Research skill + competitive-analysis for Planhat and market data

### Decision — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-1918Z.md`  
Store findings in two separate artifact files rather than merged document

### Decision — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-2211Z.md`  
Remove all legacy tools/roadmap references from codebase

### Decision — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-2211Z.md`  
Delete industry-intelligence skill (not relevant for internal CSP platform)

### Decision — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-2211Z.md`  
Keep session continuity guidance in project CLAUDE.md as core startup behavior

### Decision — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-2211Z.md`  
Apply same rigor to internal enablement/stakeholder comms as external launches

### Strategic Insight — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-2211Z.md`  
Significant cleanup: removed 3 skill files and legacy framework folder, deleted outdated rules, rewrote CLAUDE.md to be focused rather than prescriptive. All questioned skills reviewed and validated as still relevant to CSP context.

### Decision — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-1918Z.md`  
Used two parallel research agents: internal JTBD/journey mapping track and external market/competitive track

### Decision — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-1918Z.md`  
Applied jtbd, research, and competitive-analysis skills for parallel execution

### Decision — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-1918Z.md`  
Structured ICP research with evidence labels, purchase triggers, and disconfirming evidence sections

### Strategic Insight — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-1918Z.md`  
Identified three non-obvious strategic findings: (1) CS investment paradox requires model design not tooling, (2) real whitespace is cross-functional post-sales orchestration (no competitor owns this), (3) AI adoption blocked by data quality not ambition. ServiceNow's workflow orchestration is positioned as the only credible solution to address these gaps.

### Decision — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-1918Z.md`  
Spin up parallel agents: Track 1 (internal JTBD/journey) and Track 2 (external market/competitive research)

### Decision — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-1918Z.md`  
Use jtbd and research skills for internal track; research and competitive-analysis for external track

### Decision — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-1918Z.md`  
Create separate output files for JTBD workflows and market research findings

### Strategic Insight — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-1918Z.md`  
Three strategic findings emerged: (1) CS investment paradox — NRR declining despite increased spend; root cause is coordination model design, not tooling. (2) Real whitespace is cross-functional post-sales orchestration — no competitor coordinates Sales→CS→Support→PS→Product. (3) AI stuck on data quality, not ambition — ServiceNow's workflow execution approach could unlock AI by unifying post-sales data.

### Decision — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-1918Z.md`  
Parallel agents approach: track 1 (internal JTBD/journey via jtbd skill + csm-journey project files), track 2 (external market/competitive via research and competitive-analysis skills)

### Decision — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-1918Z.md`  
Output created as two separate knowledge artifacts rather than merged documents

### Decision — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-1918Z.md`  
ICP profiled: VP/Head CS at $10M-$200M ARR B2B SaaS with 10-50 CSMs, triggered by renewal disaster, headcount freeze, or board reporting mandate

### Strategic Insight — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-1918Z.md`  
Key finding: CS investment paradox is a model design problem (not tooling); ServiceNow's whitespace is cross-functional post-sales orchestration; AI adoption blocked by data quality fragmentation, not ambition

### Decision — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-1918Z.md`  
Spin up two parallel research agents: one for internal synthesis (jtbd skill), one for external market research (research + competitive-analysis skills)

### Decision — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-1918Z.md`  
Frame CSP whitespace around unified post-sales workflow orchestration (Sales→CS→Support→PS→Product) vs point solutions

### Decision — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-1918Z.md`  
Surface data quality as AI adoption blocker — platform should unify post-sales data as workflow byproduct

### Strategic Insight — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-1918Z.md`  
Identified non-obvious competitive gap: no existing CS platform (Gainsight, Planhat, Totango) owns cross-functional post-sales orchestration. ServiceNow's platform architecture is only credible approach to this space.

### Strategic Insight — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-2211Z-1.md`  
New focus area: command list optimization and consolidation strategy

### Decision — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-1918Z.md`  
Store results in separate knowledge files, not merged

### Strategic Insight — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-1918Z.md`  
Research identified non-obvious competitive whitespace: no existing CS platform coordinates the full post-sales motion (Sales→CS→Support→PS→Product). ServiceNow's platform architecture positioned as only credible way to own this space.

### Decision — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-1918Z.md`  
Use parallel agents for two distinct research tracks: internal JTBD/journey mapping vs external market/competitive research

### Decision — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-1918Z.md`  
Store findings in separate knowledge artifacts (csm-jtbd-workflows.md and csm-icp-market-research.md)

### Decision — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-1918Z.md`  
Identified cross-functional post-sales orchestration as key whitespace vs point-solution competitors

### Strategic Insight — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-1918Z.md`  
Research revealed three non-obvious strategic findings: CS investment paradox (spending up but NRR down despite tooling investment), no existing CS platform orchestrates full post-sales workflow, and AI adoption blocked by data quality not tooling/ambition.

### Decision — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-1918Z.md`  
Parallel agents for two distinct research tracks: internal JTBD/workflows vs external market/competitive

### Decision — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-1918Z.md`  
Research structure with signal-labeled pain points, disconfirming evidence section, and source citations per competitive document standards

### Strategic Insight — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-1918Z.md`  
Three strategic insights identified: (1) CS investment paradox addressable via workflow orchestration, (2) cross-functional post-sales orchestration as real whitespace vs point-solution competitors, (3) AI adoption bottlenecked on data quality not ambition

### Decision — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-1918Z.md`  
Spin up two parallel research agents (Track 1: internal synthesis; Track 2: external market/competitive)

### Decision — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-1918Z.md`  
Use jtbd skill for internal JTBD/journey mapping

### Decision — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-1918Z.md`  
Use research and competitive-analysis skills for external market research

### Decision — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-1918Z.md`  
Create two separate knowledge artifacts rather than one merged document

### Strategic Insight — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-1918Z.md`  
User now has structured market research identifying three key non-obvious findings: (1) CS investment paradox (75% saw NRR decline despite 60% spending increases), (2) real whitespace is cross-functional post-sales orchestration (no competitor does this), (3) AI adoption bottlenecked on data quality not ambition. These directly inform CSP positioning and roadmap strategy.

### Decision — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-1918Z.md`  
Parallel agent approach: Track 1 for internal JTBD/journey mapping, Track 2 for external market/competitive research

### Decision — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-1918Z.md`  
Three strategic findings identified: CS investment paradox (75% NRR decline despite 60% spending increase), cross-functional post-sales orchestration as unaddressed whitespace, AI adoption blocked by data fragmentation not ambition

### Strategic Insight — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-1918Z.md`  
Two foundational knowledge artifacts created for CSP strategy. Three non-obvious strategic insights surfaced that position ServiceNow's workflow orchestration as differentiated answer to actual CSM problems.

### Decision — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-1918Z.md`  
Decided to use parallel agents for two independent research tracks (internal JTBD vs. external market research)

### Decision — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-1918Z.md`  
Selected skills: jtbd for internal, research + competitive-analysis for external

### Decision — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-1918Z.md`  
Structured output targets: workflows, JTBDs, user journeys, ICP profiles, burning problems with evidence labeling

### Strategic Insight — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-1918Z.md`  
User established two new Knowledge artifacts (csm-jtbd-workflows.md and csm-icp-market-research.md) with structured ICP, persona, and market research data. Identified key competitive whitespace: cross-functional post-sales orchestration and AI-enabled data unification as ServiceNow CSP's strategic positioning opportunities.

### Decision — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-2212Z.md`  
Parallel agent approach for two research tracks (internal synthesis vs external market research)

### Decision — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-2212Z.md`  
Using jtbd, research, and competitive-analysis skills for the work

### Decision — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-2212Z.md`  
Research output format: signals-labeled pain points, disconfirming evidence sections, and evidence citations required

### Strategic Insight — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-2212Z.md`  
Three non-obvious competitive findings emerged: (1) CS investment paradox — NRR declining despite 60% increase in CS spending, (2) whitespace in cross-functional post-sales orchestration (no competitor owns Sales→CS→Support→PS→Product motion), (3) AI adoption bottleneck is data quality, not ambition. ServiceNow's workflow orchestration and data unification capabilities are positioned as unique competitive advantages.

### Decision — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-2212Z.md`  
Parallel agents approach with jtbd + research skills for two-track research

### Decision — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-2212Z.md`  
Separate artifact files per research track (internal synthesis vs. external market research)

### Decision — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-2212Z.md`  
Three strategic findings identified: CS investment paradox, cross-functional orchestration whitespace, AI adoption bottleneck on data quality

### Strategic Insight — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-2212Z.md`  
Session interrupted by /login command at end; unclear if user wants to proceed with synthesis or shift focus elsewhere

### Decision — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-2212Z.md`  
Used parallel agents for two separate research tracks (internal JTBD vs external market research)

### Decision — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-2212Z.md`  
Separated artifacts by track rather than merging — internal synthesis in one file, competitive market analysis in another

### Strategic Insight — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-2212Z.md`  
Discovered ServiceNow CSP's unique competitive positioning: it's the only platform architecture credible for cross-functional post-sales orchestration (Sales→CS→Support→PS→Product), addressing coordination gaps that are the real root cause of CS ROI struggles.

### Decision — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-2212Z.md`  
Track 1 used JTBD skill + csm-journey project exploration; Track 2 used research + competitive-analysis skills

### Strategic Insight — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-2212Z.md`  
Session interrupted by login command mid-conversation; research artifacts saved but synthesis/next-steps decision pending.

### Decision — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-2212Z.md`  
Deployed parallel agents for internal synthesis (JTBD skill) and external market research (research + competitive-analysis skills)

### Decision — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-2212Z.md`  
Created structured knowledge artifacts in Knowledge/Market/ folder with evidence labeling and disconfirming evidence sections

### Strategic Insight — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-2212Z.md`  
Research establishes that no current CS platform (Gainsight, Planhat, Totango) coordinates full post-sales workflow orchestration—identifies clear whitespace for ServiceNow's platform advantage. ICP and pain point research now available to inform competitive positioning.

### Decision — 2026-04-07
**Source**: `🤖 AI/memory/sessions/2026-04-08-2212Z-1.md`  
Adopt Shubhamsaboo's profile README structure and format

### Decision — 2026-04-07
**Source**: `🤖 AI/memory/sessions/2026-04-08-2212Z-1.md`  
Use 'PM · Builder · Systems Thinker' as core positioning

### Decision — 2026-04-07
**Source**: `🤖 AI/memory/sessions/2026-04-08-2212Z-1.md`  
Emphasize ServiceNow CSP work alongside solopreneur/builder identity

### Decision — 2026-04-07
**Source**: `🤖 AI/memory/sessions/2026-04-08-2212Z-1.md`  
Reframe pm-os-template description to focus on PM leverage and impact with AI

### Decision — 2026-04-07
**Source**: `🤖 AI/memory/sessions/2026-04-08-2212Z-1.md`  
Include Stoic quote for brand voice

### Strategic Insight — 2026-04-07
**Source**: `🤖 AI/memory/sessions/2026-04-08-2212Z-1.md`  
Shifted from technical GitHub setup troubleshooting to brand positioning and copywriting. Clarified Jon's value proposition as a PM who builds AI products, moving away from generic 'AI-native tools' framing to something more authentic (PM by day, builder by night).

### Decision — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-2212Z.md`  
Deployed parallel agents (jtbd + research/competitive-analysis skills) for two distinct research tracks

### Decision — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-2212Z.md`  
Structured Track 2 deliverable with signal-labeled pain points, disconfirming evidence, purchase triggers, and buying committee composition

### Strategic Insight — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-2212Z.md`  
Session interrupted by local login command after Track 2 completion. Both knowledge artifacts created and ready for downstream work.

### Decision — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-2212Z.md`  
Used parallel agents for two-track research (internal JTBD + external market research)

### Decision — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-2212Z.md`  
Created two knowledge artifacts: csm-jtbd-workflows.md and csm-icp-market-research.md

### Strategic Insight — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-2212Z.md`  
Discovered that existing CS platforms (Gainsight, Planhat, Totango) are point solutions; no platform coordinates full post-sales workflow orchestration. This represents major strategic whitespace for ServiceNow CSP with platform architecture advantage. . Competitors are all point solutions.

### Decision — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-2212Z.md`  
Use parallel agents for two separate research tracks (internal JTBD vs external market research)

### Decision — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-2212Z.md`  
Create two separate knowledge artifacts rather than merged output

### Decision — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-2212Z.md`  
Focus research on B2B SaaS CSMs/post-sales personas with $10M-$200M ARR and 10-50 CSM headcount

### Decision — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-2212Z.md`  
Identify three key strategic findings: CS investment paradox, cross-functional orchestration whitespace, and AI adoption bottleneck on data quality

### Strategic Insight — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-2212Z.md`  
Session was interrupted by user running a /login command that failed; previous work (csm-journey project) was referenced as existing research baseline

### Decision — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-2212Z.md`  
Used parallel agents for internal + external research tracks

### Decision — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-2212Z.md`  
Track 1: JTBD skill to map CSM personas, workflows, journey maps from existing csm-journey project

### Decision — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-2212Z.md`  
Track 2: Research + competitive-analysis skills to surface market data and competitive whitespace

### Decision — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-2212Z.md`  
Saved both artifacts to Knowledge/Market/ with evidence labeling and disconfirming sections

### Strategic Insight — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-2212Z.md`  
CSP research now has two new comprehensive knowledge artifacts. Key strategic insight: ServiceNow's workflow orchestration competency positions it uniquely to own cross-functional post-sales orchestration space (Sales→CS→Support→PS→Product), which no current competitor coordinates.

### Decision — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-2212Z.md`  
Used parallel agents for internal synthesis and external market research

### Decision — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-2212Z.md`  
Created two separate knowledge artifacts rather than merging research output

### Strategic Insight — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-2212Z.md`  
Research revealed that ServiceNow's workflow orchestration and post-sales data unification capabilities address the real root causes competitors miss — not just CS tooling gaps but fundamental coordination model and data quality problems.

### Decision — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-2212Z.md`  
Use parallel agents for internal JTBD synthesis vs. external market research

### Decision — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-2212Z.md`  
Include disconfirming evidence and source citations in competitive analysis

### Decision — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-2212Z.md`  
Focus competitive analysis on whitespace: cross-functional post-sales orchestration (not point solution)

### Strategic Insight — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-2212Z.md`  
Shifted from research phase to synthesis-ready state. Key non-obvious finding: CS investment problem is model design issue, not tooling — ServiceNow's workflow orchestration positioned uniquely to address this.

### Decision — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-2212Z.md`  
Deployed parallel agents for two-track research (internal synthesis vs external market research)

### Decision — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-2212Z.md`  
Created separate knowledge artifacts to avoid compression of research depth

### Decision — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-2212Z.md`  
Identified ServiceNow's core competitive advantage: only platform capable of end-to-end post-sales orchestration (Sales→CS→Support→PS→Product) vs point-solution competitors

### Strategic Insight — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-2212Z.md`  
Research uncovered three non-obvious strategic findings: (1) 75% of companies saw NRR decline despite 60% increasing CS spend—root cause is coordination model, not tooling; (2) AI adoption stuck at 32% live use cases due to data fragmentation, not lack of ambition; (3) No competitor owns cross-functional post-sales orchestration space—whitespace exists for unified workflow platform.

### Decision — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-2212Z.md`  
Track 1 uses jtbd skill + csm-journey project files; Track 2 uses research skill + competitive-analysis

### Decision — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-2212Z.md`  
Three key strategic findings identified: CS investment paradox, cross-functional post-sales orchestration whitespace, and AI adoption blocked by data quality not ambition

### Strategic Insight — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-2212Z.md`  
Discovered non-obvious competitive positioning: ServiceNow's workflow orchestration competency is uniquely positioned to address the CS investment paradox and cross-functional post-sales coordination gap that no current platform (Gainsight, Planhat, Totango) solves.

### Decision — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-2212Z.md`  
Use parallel agents for two research tracks (jtbd + research/competitive-analysis skills)

### Decision — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-2212Z.md`  
Created structured knowledge artifacts with signal-labeled pain points, ICP profile ($10M–$200M ARR, 10–50 CSM teams), and purchase triggers

### Strategic Insight — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-2212Z.md`  
Session started with CSP research request, completed two concurrent research tracks, and identified specific competitive positioning opportunities around workflow orchestration and AI data unification — directly applicable to CSP product strategy

### Decision — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-2212Z.md`  
Deployed parallel agents for distinct research tracks (Track 1: internal JTBD/journey synthesis; Track 2: external market/competitive analysis)

### Decision — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-2212Z.md`  
Selected jtbd, research, and competitive-analysis skills for execution

### Decision — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-2212Z.md`  
Identified cross-functional post-sales orchestration as real whitespace — no competitor coordinates full Sales→CS→Support→PS→Product workflow

### Strategic Insight — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-2212Z.md`  
Discovered CS investment paradox is a model design problem (75% NRR decline despite 60% CS spend increases), not tooling — ServiceNow's workflow orchestration directly addresses root cause. Also: AI adoption bottleneck is data quality/fragmentation (72% want AI, only 32% deployed), not ambition — CSP's data unification approach could unlock majority of market.

### Decision — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-2212Z.md`  
Spun up two parallel agents for internal JTBD synthesis and external competitive research

### Decision — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-2212Z.md`  
Output strategy: separate knowledge files for JTBD/workflows vs market research

### Decision — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-2212Z.md`  
Identified cross-functional post-sales orchestration as strategic whitespace vs point-solution competitors

### Strategic Insight — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-2212Z.md`  
Identified three non-obvious market findings: (1) CS investment paradox—spending up 60% but NRR declining 75%, rooted in model design not tooling; (2) No competitor owns cross-functional Sales→CS→Support→PS→Product orchestration; (3) AI adoption blocked by data quality, not ambition—72% say critical, 32% deployed. ServiceNow positioned to address all three gaps.

### Decision — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-2212Z.md`  
Parallel agent research approach (Track 1: internal JTBD/workflows, Track 2: external market/competitive)

### Decision — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-2212Z.md`  
Structured research output with evidence labeling and disconfirming evidence sections

### Strategic Insight — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-2212Z.md`  
Two comprehensive research artifacts created with 15+ source citations. Strategic positioning framework for CSP emerged showing ServiceNow's unique competency in workflow orchestration and unified post-sales data. Session interrupted by login command.

### Decision — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-2212Z.md`  
Structure findings with signal-labeled pain points and disconfirming evidence sections per competitive document standards

### Strategic Insight — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-2212Z.md`  
Completed two foundational research artifacts (csm-jtbd-workflows.md and csm-icp-market-research.md) with key non-obvious findings: CS investment paradox, cross-functional orchestration whitespace, and AI adoption blocked by data quality not ambition.

### Decision — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-2212Z.md`  
Run two parallel research tracks: internal JTBD/journey mapping vs. external market/competitive research

### Decision — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-2212Z.md`  
Use jtbd skill for internal track, research + competitive-analysis skills for external track

### Decision — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-2212Z.md`  
Focus on three key strategic findings: CS investment paradox, cross-functional orchestration whitespace, AI adoption data quality blocker

### Strategic Insight — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-2212Z.md`  
Session interrupted by user running /login command; work incomplete but both research tracks delivered.

### Decision — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-2212Z.md`  
Spun parallel agents for internal JTBD synthesis + external market research

### Decision — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-2212Z.md`  
Identified cross-functional post-sales orchestration as uncontested whitespace vs point-solution competitors

### Decision — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-2212Z.md`  
Framed CS investment problem as coordination model design, not tooling capability

### Decision — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-2212Z.md`  
Pinpointed AI adoption blocker as data fragmentation/quality, not technology ambition

### Strategic Insight — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-2212Z.md`  
Session interrupted by user login command before responding to synthesis offer. Two comprehensive research documents created with high-confidence competitive framing ready for product strategy.

### Decision — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-2212Z.md`  
Use parallel agents: Track 1 (internal JTBD/journey synthesis) and Track 2 (external market/competitive research)

### Decision — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-2212Z.md`  
Target ICP: VP/Head of CS at B2B SaaS ($10M-$200M ARR) with NRR accountability

### Decision — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-2212Z.md`  
Strategic positioning: Cross-functional post-sales orchestration as whitespace vs point-solution competitors

### Decision — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-2212Z.md`  
Used parallel agents (jtbd skill + research/competitive-analysis skills) for two distinct research tracks

### Decision — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-2212Z.md`  
Created separate knowledge artifacts for internal JTBD mapping and external market research

### Decision — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-2212Z.md`  
Used parallel agents for Track 1 (internal JTBD/journey mapping) and Track 2 (external market research + competitive analysis)

### Decision — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-2212Z.md`  
Structured outputs with signal-labeled pain points, disconfirming evidence sections, and source citations per user's competitive document standards

### Strategic Insight — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-2212Z.md`  
Research identified that ServiceNow's workflow orchestration and platform architecture uniquely position CSP against fragmented point-solution competitors (Gainsight, Planhat, Totango) in cross-functional post-sales space.

### Decision — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-2212Z.md`  
Used parallel agents for internal JTBD/journey research and external market research

### Decision — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-2212Z.md`  
Structured ICP around VP/Head of CS at $10M–$200M ARR B2B SaaS with 3 purchase triggers

### Decision — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-2212Z.md`  
Stored research artifacts in Knowledge/Market folder structure

### Decision — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-2212Z.md`  
Framed CSP competitive positioning around cross-functional orchestration and data unification for AI

### Strategic Insight — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-2212Z.md`  
Two new research knowledge artifacts created with evidence-labeled pain points, ICP profile details, and strategic insights about ServiceNow's unique positioning relative to point-solution competitors (Gainsight, Planhat, Totango).

### Decision — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-2214Z.md`  
Use existing three-lens review inside /spec (strategic, product taste via elite-copywriter) rather than invoking /product-taste-intuition as a separate review tool

### Decision — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-2214Z.md`  
Add Step 3.5 to /spec workflow to loop back through reviews autonomously before presenting

### Decision — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-2214Z.md`  
Keep commits scoped tightly (spec.md only) to maintain readable git history

### Strategic Insight — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-2214Z.md`  
Template drift problem surfaced and resolved — pm-os-template now matches SNOW-Work on /spec workflow enhancements. This ensures future workspace derivations get the improved workflow by default.

### Decision — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-2212Z.md`  
Deploy parallel agents: Track 1 (internal JTBD/journey mapping) and Track 2 (external market/competitive)

### Decision — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-2212Z.md`  
Use jtbd skill for internal synthesis; research + competitive-analysis skills for external market

### Decision — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-2212Z.md`  
Create two separate artifact files rather than merging

### Decision — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-2212Z.md`  
Structure ICP research with signal-labeled pain points, disconfirming evidence section, and burning problems table

### Strategic Insight — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-2212Z.md`  
Three non-obvious competitive findings identified: (1) CS investment paradox—NRR declining despite spending increases due to coordination model design gaps ServiceNow can address; (2) Real whitespace is cross-functional post-sales orchestration—no competitor owns this; (3) AI adoption blocked by data quality fragmentation, not ambition—ServiceNow's workflow-driven data unification is unique solution.

### Decision — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-2212Z.md`  
Parallel agents for two distinct research tracks (internal JTBD + csm-journey exploration vs. external market/competitive research)

### Decision — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-2212Z.md`  
Evidence labeling and disconfirming evidence sections in competitive research (aligns with established feedback standard)

### Decision — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-2212Z.md`  
Framed three strategic findings: CS investment paradox, cross-functional orchestration whitespace, AI data quality blocker as core CSP positioning angles

### Strategic Insight — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-2212Z.md`  
Session interrupted by login command after Track 2 completion. Two new Knowledge/ artifacts created with 15+ cited sources. Three non-obvious competitive positioning insights identified that directly inform ServiceNow CSP's market differentiation.

### Decision — 2026-04-07
**Source**: `🤖 AI/memory/sessions/2026-04-08-2217Z.md`  
Create new commercial-lens skill instead of just upgrading business-reasoning

### Decision — 2026-04-07
**Source**: `🤖 AI/memory/sessions/2026-04-08-2217Z.md`  
Upgrade 4 existing skills with probabilistic thinking rather than creating a separate skill

### Decision — 2026-04-07
**Source**: `🤖 AI/memory/sessions/2026-04-08-2217Z.md`  
Execute research and planning in parallel tracks with separate artifacts

### Decision — 2026-04-07
**Source**: `🤖 AI/memory/sessions/2026-04-08-2217Z.md`  
Execute skill building in parallel (commercial-lens + 4 upgrades)

### Decision — 2026-04-07
**Source**: `🤖 AI/memory/sessions/2026-04-08-2217Z.md`  
Ship directly to main without PR

### Strategic Insight — 2026-04-07
**Source**: `🤖 AI/memory/sessions/2026-04-08-2217Z.md`  
AIPMOS now has commercial PM lens (value capture, deal economics, payback horizon) and probabilistic decision frameworks (resulting averages, expectancy, chain math confidence compounding). These fill gaps identified in the workspace (zero Lenny matches on commercial PM concepts).

### Decision — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-2212Z.md`  
Use parallel agents for internal and external research tracks

### Decision — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-2212Z.md`  
Create separate knowledge artifacts for JTBD/workflows vs. market/ICP research

### Strategic Insight — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-2212Z.md`  
Research phase complete with high-value findings about ServiceNow's competitive positioning in cross-functional post-sales orchestration and AI-ready unified data infrastructure.

### Decision — 2026-04-07
**Source**: `🤖 AI/memory/sessions/2026-04-08-2247Z.md`  
Excluded .specstory/ (untracked generated directory) from commit

### Decision — 2026-04-07
**Source**: `🤖 AI/memory/sessions/2026-04-08-2247Z.md`  
Deleted 🔧 Automation/scripts/launcher.py and launcher_web.py

### Decision — 2026-04-07
**Source**: `🤖 AI/memory/sessions/2026-04-08-2247Z.md`  
User preferred direct push over PR workflow

### Strategic Insight — 2026-04-07
**Source**: `🤖 AI/memory/sessions/2026-04-08-2247Z.md`  
Launcher automation scripts removed from codebase; session-intent.json and skills registry updated; PR-based workflow changed to direct push on user request

### Decision — 2026-04-07
**Source**: `🤖 AI/memory/sessions/2026-04-08-2217Z-1.md`  
Architecture flip: server owns terminal launch via osascript detection (Warp/Cursor/iTerm2/Terminal.app) instead of shell function

### Decision — 2026-04-07
**Source**: `🤖 AI/memory/sessions/2026-04-08-2217Z-1.md`  
Session-start hook runs background extraction retroactively since session-end hook doesn't fire on SIGHUP

### Decision — 2026-04-07
**Source**: `🤖 AI/memory/sessions/2026-04-08-2217Z-1.md`  
Card shows: Summary (Haiku-extracted), Focus (end state), first Open Question

### Decision — 2026-04-07
**Source**: `🤖 AI/memory/sessions/2026-04-08-2217Z-1.md`  
Exclude current session from resumable list (most recent JSONL)

### Strategic Insight — 2026-04-07
**Source**: `🤖 AI/memory/sessions/2026-04-08-2217Z-1.md`  
Discovered SIGHUP from terminal close prevents hooks from firing. Shifted strategy from session-end extraction to retroactive session-start extraction.

### Decision — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-2212Z.md`  
Structure research around four post-sales personas (CSM, PS, CS Ops, VP CS) with explicit JTBD statements and journey maps

### Decision — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-2212Z.md`  
Frame CSP whitespace around cross-functional post-sales orchestration (Sales→CS→Support→PS→Product) vs competitors' point solutions

### Decision — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-2212Z.md`  
Require signal-labeled pain points with source citations and disconfirming evidence sections in market research artifact

### Decision — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-2212Z.md`  
Track 1: internal JTBD/workflow mapping from csm-journey project

### Decision — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-2212Z.md`  
Track 2: external market and competitive research via Planhat and industry reports

### Decision — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-08-2212Z.md`  
Saved findings with evidence labeling and disconfirming evidence section

### Decision — 2026-04-07
**Source**: `🤖 AI/memory/sessions/2026-04-08-2249Z.md`  
Changed pattern extraction source from guest-insights to session files (higher quality, fewer false positives)

### Decision — 2026-04-07
**Source**: `🤖 AI/memory/sessions/2026-04-08-2249Z.md`  
Built pre_clear_capture.py hook to automatically intercept /clear via UserPromptSubmit instead of requiring manual /checkpoint

### Decision — 2026-04-07
**Source**: `🤖 AI/memory/sessions/2026-04-08-2249Z.md`  
Registered pre_clear_capture.py as a second UserPromptSubmit hook in settings.json for automatic execution

### Strategic Insight — 2026-04-07
**Source**: `🤖 AI/memory/sessions/2026-04-08-2249Z.md`  
Discovered that session files (not guest-insights) are the actual insight source Claude Code generates. Learned that /clear can be intercepted via UserPromptSubmit's prompt field before CLI processes it, enabling fully automatic capture without user action.

### Decision — 2026-04-09
**Source**: `🤖 AI/memory/sessions/2026-04-08-2212Z.md`  
Track 1: jtbd + csm-journey project exploration for workflows and journey maps

### Decision — 2026-04-09
**Source**: `🤖 AI/memory/sessions/2026-04-08-2212Z.md`  
Track 2: research + competitive-analysis skills for market data and ICP profiling

### Decision — 2026-04-09
**Source**: `🤖 AI/memory/sessions/2026-04-08-2212Z.md`  
Output format: two knowledge artifacts with signal-labeled findings and source citations

### Decision — 2026-04-09
**Source**: `🤖 AI/memory/sessions/2026-04-08-2212Z.md`  
Store research artifacts in Knowledge/Market/ directory with structured evidence labeling and disconfirming evidence sections

### Decision — 2026-04-09
**Source**: `🤖 AI/memory/sessions/2026-04-08-2212Z.md`  
Frame CSP strategic positioning around three core findings: CS investment paradox, cross-functional post-sales orchestration whitespace, and AI data quality as unlock

### Strategic Insight — 2026-04-09
**Source**: `🤖 AI/memory/sessions/2026-04-08-2212Z.md`  
ICP profile clarified (VP/Head CS at $10M-$200M ARR B2B SaaS); competitive whitespace identified (no existing CS platform coordinates full Sales→CS→Support→PS→Product motion); data quality identified as primary AI adoption blocker in CS.

### Decision — 2026-04-09
**Source**: `🤖 AI/memory/sessions/2026-04-08-2212Z.md`  
Used jtbd, research, and competitive-analysis skills

### Decision — 2026-04-09
**Source**: `🤖 AI/memory/sessions/2026-04-08-2212Z.md`  
Created two separate artifact files with source citations and evidence labeling

### Decision — 2026-04-09
**Source**: `🤖 AI/memory/sessions/2026-04-08-2212Z.md`  
Identified three strategic findings: CS investment paradox, cross-functional orchestration whitespace, AI/data quality bottleneck

### Strategic Insight — 2026-04-09
**Source**: `🤖 AI/memory/sessions/2026-04-08-2212Z.md`  
Session ended with /login interruption; agent offered synthesis work pending user resume

### Decision — 2026-04-07
**Source**: `🤖 AI/memory/sessions/2026-04-09-1552Z.md`  
Added check-and-skip guard in pre_clear_capture.py to prevent duplicate extraction runs

### Decision — 2026-04-07
**Source**: `🤖 AI/memory/sessions/2026-04-09-1552Z.md`  
Modified write_session_file() to only generate new timestamp when actually writing a new file

### Decision — 2026-04-07
**Source**: `🤖 AI/memory/sessions/2026-04-09-1552Z.md`  
Deleted 4 duplicate session files (0211Z-1.md, 0212Z.md, 0212Z-1.md, 0214Z.md), kept 0107Z.md as most complete

### Strategic Insight — 2026-04-07
**Source**: `🤖 AI/memory/sessions/2026-04-09-1552Z.md`  
Session extraction system had systemic bug: dual hooks (pre_clear + session_end) were both triggering extraction on same transcript, and no deduplication check in filename generation meant each run created new file. Both root causes now fixed.

### Decision — 2026-04-07
**Source**: `🤖 AI/memory/sessions/2026-04-09-0255Z.md`  
Disabled Python extension auto-activation by adding 'python.terminal.activateEnvironment': false to .vscode/settings.json

### Strategic Insight — 2026-04-07
**Source**: `🤖 AI/memory/sessions/2026-04-09-0255Z.md`  
Workspace setting change affects both VS Code and Cursor terminals in this project

### Decision — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-09-0253Z.md`  
Implement 5 improvements via Ultraplan rather than manual implementation

### Decision — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-09-0253Z.md`  
Merge PR #3 that added lint prompt + cross-reference conventions to knowledge system

### Decision — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-09-0253Z.md`  
Keep archived patterns archived (no duplication needed)

### Strategic Insight — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-09-0253Z.md`  
Knowledge system evolved from write-only append model to maintenance-first model with lint pass for health checks. The core insight: maintenance passes prevent knowledge accumulation death spirals.

### Decision — 2026-04-07
**Source**: `🤖 AI/memory/sessions/2026-04-09-1553Z.md`  
Simplified 6-view plan to 3 core views (Brief, Cross-Reference, Deep)

### Decision — 2026-04-07
**Source**: `🤖 AI/memory/sessions/2026-04-09-1553Z.md`  
Embedded all data in single JS const DATA object for offline-first single-file operation

### Decision — 2026-04-07
**Source**: `🤖 AI/memory/sessions/2026-04-09-1553Z.md`  
Switched to light theme with CSS variables for better readability

### Decision — 2026-04-07
**Source**: `🤖 AI/memory/sessions/2026-04-09-1553Z.md`  
Added workflow/journey toggle modes reusing Brief view state management

### Decision — 2026-04-09
**Source**: `🤖 AI/memory/sessions/2026-04-09-1908Z.md`  
Used jtbd and research skills with parallel agents for separate tracks (internal synthesis vs. external market research)

### Decision — 2026-04-09
**Source**: `🤖 AI/memory/sessions/2026-04-09-1908Z.md`  
Separated artifacts by research type rather than combining into single document

### Decision — 2026-04-09
**Source**: `🤖 AI/memory/sessions/2026-04-09-1908Z.md`  
Focused research on pain points, burning problems, and workflow mapping with evidence labeling and disconfirming evidence sections

### Strategic Insight — 2026-04-09
**Source**: `🤖 AI/memory/sessions/2026-04-09-1908Z.md`  
Three strategic insights emerged: (1) CS investment paradox—spending up 60% but NRR declining 75%, suggesting model design problem not tooling gap; (2) whitespace identified in cross-functional post-sales orchestration (no competitor coordinates full Sales→CS→Support→PS→Product); (3) AI adoption bottleneck is data quality/fragmentation, not ambition. ServiceNow's platform architecture uniquely positioned for all three.

### Decision — 2026-04-09
**Source**: `🤖 AI/memory/sessions/2026-04-09-1908Z.md`  
Deployed parallel agents for internal JTBD mapping (Track 1) and external market/competitive research (Track 2)

### Strategic Insight — 2026-04-09
**Source**: `🤖 AI/memory/sessions/2026-04-09-1908Z.md`  
Research session completed with two knowledge artifacts saved. Four-hour research effort produced 15+ source citations and disconfirming evidence. Agent offered next step (synthesis) before session was interrupted.

### Decision — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-09-1908Z-1.md`  
Decided NOT to reduce command count from 51 to 15-20 (routing table already solves discoverability)

### Decision — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-09-1908Z-1.md`  
Kept /critique and /research as distinct operations

### Decision — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-09-1908Z-1.md`  
Removed legacy commands entirely

### Decision — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-09-1908Z-1.md`  
Removed AgilePlace references from /story command

### Decision — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-09-1908Z-1.md`  
Removed broken Canonical Source dependency in legacy-command.md

### Strategic Insight — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-09-1908Z-1.md`  
Discovered documentation drift in command references—paths broken, replaced commands still referenced by callers, new commands missing from routing. Identified /ci-brief replaces /daily-brief. Workflows folders missing (only README exists).

### Decision — 2026-04-09
**Source**: `🤖 AI/memory/sessions/2026-04-09-1908Z.md`  
Launch parallel research tracks for internal/external analysis

### Decision — 2026-04-09
**Source**: `🤖 AI/memory/sessions/2026-04-09-1908Z.md`  
Structured research outputs with JTBD framework + market data synthesis

### Strategic Insight — 2026-04-09
**Source**: `🤖 AI/memory/sessions/2026-04-09-1908Z.md`  
Deep understanding of CS market whitespace: coordination problems over tooling gaps, AI data quality blockers, and cross-functional orchestration opportunity

### Decision — 2026-04-09
**Source**: `🤖 AI/memory/sessions/2026-04-09-1908Z.md`  
To use parallel agents for internal JTBD/journey mapping and external competitive/market research

### Decision — 2026-04-09
**Source**: `🤖 AI/memory/sessions/2026-04-09-1908Z.md`  
To create separate artifacts: workflows/journey maps and market research/ICP profile

### Strategic Insight — 2026-04-09
**Source**: `🤖 AI/memory/sessions/2026-04-09-1908Z.md`  
Completed deep research with two parallel agents producing comprehensive artifacts on CSM workflows, JTBDs, and market whitespace

### Decision — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-09-1915Z.md`  
Used nohup & to detach SessionEnd hooks from parent process

### Decision — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-09-1915Z.md`  
Implemented lockfile mechanism to prevent recursive extraction runs

### Strategic Insight — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-09-1915Z.md`  
Fixed SessionEnd hook configuration by removing duplicates and implementing proper detachment, resolved recursive extraction bug with lockfile

### Decision — 2026-04-09
**Source**: `🤖 AI/memory/sessions/2026-04-09-1908Z.md`  
Created parallel agent approach for internal JTBD vs external market research

### Decision — 2026-04-09
**Source**: `🤖 AI/memory/sessions/2026-04-09-1908Z.md`  
Decided to produce separate artifacts instead of synthesis

### Decision — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-09-1915Z-1.md`  
Added Socratic questioning step before research in /spec

### Decision — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-09-1915Z-1.md`  
Implemented automatic review loops in /spec creation

### Strategic Insight — 2026-04-08
**Source**: `🤖 AI/memory/sessions/2026-04-09-1915Z-1.md`  
Updated spec.md in both SNOW-Work and pm-os-template workspaces

### Decision — 2026-04-09
**Source**: `🤖 AI/memory/sessions/2026-04-09-1908Z.md`  
Use parallel agents for internal (JTBD/journey) and external (market/competitive) research tracks

### Decision — 2026-04-09
**Source**: `🤖 AI/memory/sessions/2026-04-09-1908Z.md`  
Research ICP profile: VP/Head CS at mid-market B2B SaaS with NRR accountability

### Decision — 2026-04-09
**Source**: `🤖 AI/memory/sessions/2026-04-09-1908Z.md`  
Focus competitive analysis on Gainsight, Planhat, Totango as primary comparators

### Decision — 2026-04-09
**Source**: `🤖 AI/memory/sessions/2026-04-09-1908Z.md`  
Created parallel research tracks: internal JTBD mapping and external market analysis

### Decision — 2026-04-09
**Source**: `🤖 AI/memory/sessions/2026-04-09-1908Z.md`  
Focused on three key non-obvious findings with ServiceNow implications

### Strategic Insight — 2026-04-09
**Source**: `🤖 AI/memory/sessions/2026-04-09-1908Z.md`  
Added new knowledge artifacts: 📚 Knowledge/Market/csm-jtbd-workflows.md and 📚 Knowledge/Market/csm-icp-market-research.md

### Decision — 2026-04-09
**Source**: `🤖 AI/memory/sessions/2026-04-09-1908Z.md`  
Launched parallel research tracks with separate skills

### Decision — 2026-04-09
**Source**: `🤖 AI/memory/sessions/2026-04-09-1908Z.md`  
Created comprehensive artifacts: csm-jtbd-workflows.md and csm-icp-market-research.md

### Decision — 2026-04-09
**Source**: `🤖 AI/memory/sessions/2026-04-09-1908Z.md`  
Identified three strategic findings with direct ServiceNow implications

### Strategic Insight — 2026-04-09
**Source**: `🤖 AI/memory/sessions/2026-04-09-1908Z.md`  
Completed deep market research phase with strong strategic findings about CS investment paradox, cross-functional orchestration whitespace, and AI adoption blockers
