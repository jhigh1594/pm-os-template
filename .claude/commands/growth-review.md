---
description: Run the growth review workflow
---
# /growth-review — Cross-Month Growth Signal Synthesis

Surface repeating PM reasoning patterns across months by aggregating growth signals beyond what `/weekly-review` Step 1.5 covers (current month only).

---

## When to Use

Run quarterly, or any time you want to ask: "What failure modes keep showing up in my work?"

Distinct from `/weekly-review` (current-month triage) — this is the longitudinal synthesis pass.

---

## Command Syntax

```
/growth-review [--months <N>] [--archetype <name>]
```

**Arguments**:
- `--months <N>`: How many months back to read (default: 3)
- `--archetype <name>`: Filter to one archetype only (optional)

---

## Execution

### Step 1: Discover signal files

List all files matching `growth-signals-YYYY-MM.md` in `📚 Knowledge/Growth/`. Sort chronologically. Take the last N months (default: 3). If fewer than 2 months of files exist, note this and run with what's available.

### Step 2: Aggregate entries

Read all entries across the N files. Build a frequency table:

| Pattern tag | Count | Months appeared |
|---|---|---|
| strategy-coherence | N | [list] |
| opportunity-cost | N | [list] |
| ... | | |

Sort by count descending.

### Step 3: Surface repeating patterns

For any pattern tag appearing in 3+ entries:
- Flag as **repeating pattern** — this is a development theme, not a one-off
- Pull the 2 most recent entries for that tag and quote them verbatim
- Name the archetype it maps to (from `.claude/skills/coaching-hooks/SKILL.md` archetype list)

### Step 4: Surface coverage gaps

Identify which of the 7 coaching archetypes have 0 entries across the N months. These are **growth signal gaps** — areas where quality gates haven't fired or responses weren't captured.

List them: "No signal captured for [archetype] in [N] months."

### Step 5: Report

```
## Growth Review: [date range]
Source: [N] months · [total entry count] entries

### Repeating Patterns (3+ entries)
- **[pattern-tag]** ([count] entries, archetype: [name]):
  Most recent: "[quote]" — [date]
  Prior: "[quote]" — [date]

### Coverage Gaps
- [archetype] — no entries in [N] months

### One Thing to Focus On
[The pattern tag appearing most frequently, with one concrete behavior change it implies]
```

---

## Integration

- **Feeds from**: `📚 Knowledge/Growth/growth-signals-YYYY-MM.md` (auto-populated by coaching quality gates)
- **Complements**: `/weekly-review` Step 1.5 (current month only) — this command synthesizes cross-month
- **Cadence**: Quarterly minimum; monthly once coaching hooks are firing regularly

---

## Notes

- Requires at least 1 growth signal file to be meaningful. With auto-save enabled (Phase 1 changes), files accumulate automatically after each analytical command.
- Pattern tags: `assumption-visibility` | `strategy-coherence` | `option-diversity` | `problem-grounding` | `evidence-quality` | `bar-raising` | `opportunity-cost` | `value-mechanism` | `signal-interpretation` | `differentiation-logic` | `story-vs-opinion` | `sequencing-logic`
- The 7 coaching archetypes: Judgment/Tradeoffs · Generative Thinking · Strategic Framing · Evaluative Judgment · Financial Reasoning · Competitive Intelligence · Discovery/Assumption Testing
