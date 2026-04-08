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
## Staging Area
New pattern candidates live in `🤖 AI/patterns/candidate-patterns.md` (pending manual review).
Promote here only after passing all 4 quality gates.
