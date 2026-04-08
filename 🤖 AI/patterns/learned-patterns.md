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
| 2026-04-03 | Scratch Is for Disposable Artifacts Only          | Ported from Planview Work | Durable workspace policy                         |
| 2026-04-03 | Don't Ask Multiple Questions at Once              | Ported from Planview Work | Methodology mistake to avoid                     |
| 2026-04-03 | Never Hallucinate or Fabricate Content            | Ported from Planview Work | Critical content integrity rule                  |
| 2026-04-03 | PRDs Always Belong to Initiatives                 | Ported from Planview Work | File placement mistake to avoid                  |
| 2026-04-03 | Plan Index/Reference File Changes Before Editing  | Ported from Planview Work | Confirmed 3x — generalized to any reference file |
| 2026-04-03 | Breaking Down Work: Parent/Child and Dependencies | Ported from Planview Work | Work breakdown methodology                       |


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
Confirmed Python learning infrastructure copied from Planview Work is workspace-generic and functional in SNOW-Work without modification

### Strategic Insight — 2026-04-06
**Source**: `🤖 AI/memory/sessions/2026-04-08-0240Z.md`  
The skill learning system transitioned from scaffolded-but-inactive to fully operational. The missing piece was hook wiring, not Python infrastructure—this was already present from prior Planview Work implementation.

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
Remove all Planview/AgilePlace/OKR/Roadmap references from codebase and config files

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
