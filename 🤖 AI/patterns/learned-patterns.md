# Learned Patterns

_Last updated: 2026-02-17_
_Total patterns: 4_
_Purpose: Accumulated wisdom that makes future sessions faster and higher quality_

**Separation of concerns:** Workspace conventions, tooling, and repo decisions live here. **PM product decisions** (feature prioritization, roadmap bets, product strategy) go in [product-decisions.md](product-decisions.md). Forecasts and calibration live in [product-judgment-test.md](product-judgment-test.md).

---

## Quality Standard

Every pattern must pass **all 4 gates** before capture:

| Gate | Question |
|------|----------|
| **Actionable** | Can I do something specific with this? |
| **Specific** | Is it tied to my context, not generic advice? |
| **Durable** | Will it be useful in 5+ future sessions? |
| **Non-obvious** | Is this something I wouldn't naturally know? |

---

## Decisions Made

_Past decisions with reasoning - prevents re-litigating settled questions_

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

_Workspace-specific patterns that aren't obvious to newcomers_

> **Format**: Pattern → Context → Why → Confidence

### Planview Presentations Always Start with Corporate Template
**Pattern**: Use `/Users/jhigh/Library/Mobile Documents/com~apple~CloudDocs/Planview Corporate Template-2025.pptx` for all presentations
**Context**: Any slide deck creation for Planview (internal or external)
**Why**: Ensures brand consistency, saves 1-2 hours on formatting per deck, pre-approved by marketing
**Confidence**: High (reinforced 5x)

### Documentation Convention: PRDs vs Memos
**Pattern**: PRDs go in `Products/[product]/initiatives/`; strategic POV docs go in `Docs/memos/`
**Context**: Creating new documentation
**Why**: PRDs are product-specific and live with the product; memos are cross-product strategic communications
**Confidence**: High (reinforced 3x)

### AIPMOS Memory Structure
**Pattern**: Single `memory.md` file for current state; `learned-patterns.md` for accumulated wisdom
**Context**: Understanding where to find/update context
**Why**: Consolidated from 7-file system - simpler maintenance, faster loading
**Confidence**: High (reinforced 2x)

---

## Mistakes to Avoid

_Painful lessons that save future time_

> **Format**: What happened → Why it failed → How to avoid → Cost saved

<!-- Example:
### Don't Create Presentations from Scratch
**What happened**: Built deck from blank slides, spent 2 hours on formatting
**Why it failed**: Corporate template already has approved layouts, colors, fonts
**How to avoid**: Always start with corporate template, use pptx skill
**Cost saved**: ~2 hours per deck
-->

---

## Productive Patterns

_Repeatable sequences that produce reliable results_

> **Format**: Trigger → Sequence → Why it works → Confidence

<!-- Example:
### Creating PRDs in This Workspace
**Trigger**: New feature or significant enhancement
**Sequence**:
1. Check `Products/[product]/initiatives/` for existing related work
2. Use PRD template from `.claude/commands/spec.md`
3. Include success metrics with source attribution
4. Review with `/think` before sharing
**Why it works**: Ensures alignment with existing work, consistent format, strategic validation
**Confidence**: Medium (new pattern)
-->

---

## Tool-Specific Wisdom

_Domain and tool patterns specific to this workspace_

> **Format**: Tool/Domain → Pattern → Context → Gotchas → Confidence

<!-- Example:
### PowerPoint with pptx Skill
**Pattern**: Use `rearrange.py` → `inventory.py` → `replace.py` workflow
**Context**: Editing existing presentations
**Gotchas**: Don't edit .pptx directly - use the skill
**Confidence**: High (reinforced 4x)
-->

---

## Validation Log

_Patterns are semantically validated based on session learnings_

| Date | Pattern | Change | Reason |
|------|---------|--------|--------|
| 2026-02-17 | Semantic Pattern Capture System | Added | First decision captured - new system design |
| 2026-02-17 | Planview Corporate Template | Added | High-value convention from memory.md |
| 2026-02-17 | Documentation Convention | Added | PRDs vs Memos distinction |
| 2026-02-17 | AIPMOS Memory Structure | Added | Single-file system understanding |
| 2026-02-17 | File created | Initial structure | Starting fresh |

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

_Next review: 2026-02-24_

