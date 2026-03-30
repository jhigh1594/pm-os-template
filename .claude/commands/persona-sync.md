# Persona Sync

Close the signal-to-persona feedback loop. Reads accumulated signals from `signals-YYYY-MM.md`, compares against current persona files, and proposes evidence-based updates — surfacing validations, contradictions, and documented gaps. No persona changes without explicit user confirmation.

---

## Relationship

- **`/persona-sync`** is the feedback loop closer — downstream of `/synthesize` and `/signal`, upstream of `/prep`, `/discover`, and `/compete`
- **`/signal`** captures individual signals (with Persona Impact Check in Step 2.5 flagging relevant ones)
- **`/synthesize`** surfaces Persona Sync Check as a closing section — the trigger to run this command
- **`/prep`** reads updated personas for richer context briefs — only as good as the last sync
- **`/discover`** uses personas to frame initiative discovery — stale personas create stale framing
- Run **monthly** after signals accumulate, or after any `/synthesize` session where Persona Sync Check flags 2+ personas

---

## Core Philosophy

**Personas are hypotheses, not facts.**

A persona that hasn't been updated in 90 days is not a snapshot of reality — it's a snapshot of what someone believed 90 days ago. Customer jobs shift. Pain points evolve. Workarounds that once defined the product gap sometimes get addressed and new ones emerge.

The fatal flaw: maintaining personas as static documents that get "finalized" at project start and never touched again. By month 3, you're making decisions based on old evidence while new signals sit unread in the signals file.

**Minimum evidence thresholds** prevent anecdote-driven persona drift:
- **3 signals** required to contradict an existing persona attribute
- **2 signals** required to add a new attribute
- **1 signal** → note it as an observation, don't change anything yet

---

## Command Syntax

```bash
/persona-sync [--product <name>] [--persona <filename>] [--period <YYYY-MM>]
```

**Arguments**:
- `--product`: `agileplace | okrs | roadmaps | dpd | platform` — if omitted, asks which product
- `--persona`: Specific persona file to sync (e.g., `rte-persona.md`) — if omitted, syncs all personas for the product
- `--period`: Month of signals to draw from (default: current month + prior month combined)

**Examples**:
```bash
/persona-sync --product agileplace
/persona-sync --product agileplace --persona rte-persona.md
/persona-sync --product okrs --period 2026-03
/persona-sync --product agileplace --period 2026-02
```

---

## Your Approach

### Step 0: Parse Arguments and Orient

Extract product, persona file(s), and period. If product is not specified, ask:
> "Which product's personas should I sync? (`agileplace | okrs | roadmaps | dpd | platform`)"

Identify the signals period: default is current month + prior month (two-month rolling window).

### Step 1: Load Persona Files

Read all persona files in `📦 Products/[product]/product-context/`:
- Look for files matching `*persona*`, `*icp*`, `*customer*` patterns
- Note the last-modified date of each file
- If `--persona` specified, load only that file

**Flag immediately** if any persona file has not been updated in 90+ days:
> "⚠️ [filename] last updated [date] ([N days ago]) — findings from this sync may represent significant drift from current state."

### Step 2: Load and Filter Signals

Read `📚 Knowledge/Research/signals-[period].md` (and prior month if period is current month).

**Filter criteria**:
- Product area matches `--product` (or include all if no product specified)
- ICP fit: High or Medium only (Low = insufficient customer-centricity for persona update)
- Source: All sources valid, but weight by source quality (interview/cs-escalation highest; market/analyst lowest for persona-specific updates)

**Count signals per product area and source type.** If fewer than 5 qualifying signals found:
> "⚠️ Only [N] qualifying signals found for [product] in [period]. Persona sync is most valuable with 10+ signals. Proceeding with available evidence — flag all findings as low-confidence."

### Step 3: Match Signals to Persona Attributes

For each persona file loaded, compare signals against current documented attributes:

**Attribute categories to check** (standard across persona files):
- Jobs-to-be-done (functional, emotional, social)
- Primary pain points / frustrations
- Workarounds currently used
- Success metrics / how they define "done"
- Decision criteria (what makes them choose / reject)
- Language patterns (words they actually use)
- Anti-jobs (what they're trying to avoid)

For each signal, determine:
- **Validates**: Signal confirms an existing attribute — note it with count
- **Contradicts**: Signal conflicts with an existing attribute — note it with signal count and evidence
- **Adds**: Signal describes a job/pain/pattern not currently documented
- **No match**: Signal is interesting but doesn't map to a persona attribute category

### Step 4: Generate Persona Delta Report

Output a structured report showing what changed, what's confirmed, and what's missing:

```markdown
## Persona Delta Report: [Product] — [Persona Name] — [Date]

**Signals analyzed:** [N signals | [period range] | [ICP fit: H/M] | [sources]]
**Persona file:** `[path]` — Last updated: [date] ([N days ago])

---

### ✅ Validated Attributes (confirmed by evidence)
- **[Attribute or job]**: Confirmed by [N] signals — [brief note on consistency or nuance]
  - Evidence: "[Representative signal quote]" — [Source type, date]

[Repeat for each validated attribute with 3+ confirming signals]

---

### ⚠️ Contradicted Attributes (evidence conflicts with current documentation)
> ⚠️ **Evidence threshold met** — [N] signals contradict this attribute (threshold: 3)

- **Current attribute**: "[Exact text from persona file]"
- **What signals show instead**: [Synthesized description of what signals actually show]
- **Signal count**: [N signals, [period]]
- **Evidence sample**:
  - "[Signal quote 1]" — [Source type, date]
  - "[Signal quote 2]" — [Source type, date]
- **Proposed update**: "[Replacement text for this attribute]"
- **Confidence**: [High / Medium — based on signal strength and source diversity]

[Repeat for each contradicted attribute meeting threshold]

---

### 🆕 New Attributes to Add (documented in signals, absent from persona)
> [N signals describe this — threshold to add: 2]

- **Proposed new attribute**: [Job/pain/pattern description]
- **Category**: [Job / Pain / Workaround / Success Metric / Decision Criteria / Language]
- **Evidence**:
  - "[Signal quote 1]" — [Source type, date]
  - "[Signal quote 2]" — [Source type, date]
- **Suggested placement**: [Where in the persona file this belongs]

[Repeat for each new attribute with 2+ supporting signals]

---

### 👁️ Below Threshold — Monitor (1 signal — not actionable yet)
- [Attribute or pattern]: [Brief description] — [1 signal, date, source]

[List, don't elaborate — these need more evidence before acting]

---

### Persona Health Score
| Dimension | Assessment |
|-----------|-----------|
| **Evidence freshness** | [Last signal date vs. persona last-updated date] |
| **Coverage** | [N of N persona attributes have 1+ supporting signals] |
| **Contradiction density** | [N attributes contradicted — H/M/L health] |
| **Gaps identified** | [N new attributes proposed] |
| **Overall** | [Healthy / Needs refresh / Significantly stale] |

**Recommended action**: [Specific next step — accept changes below / run /discover to fill knowledge gap / schedule customer interview for [specific question]]
```

### Step 5: Propose Changes One-by-One (Confirmed Attributes Only)

After the full Delta Report, walk through each proposed change (contradictions + additions) one at a time:

For each **contradiction**:
> "Update: Replace `[current text]` with `[proposed text]` in [persona file]?
> Evidence: [N signals, [period]]
> (y = apply | n = skip | edit = let me modify the proposed text first)"

For each **new attribute**:
> "Add: `[proposed attribute]` to [section] in [persona file]?
> Evidence: [N signals, [period]]
> (y = apply | n = skip | edit = let me modify the proposed text first)"

**Apply only on explicit 'y' confirmation.** No bulk updates.

After all proposed changes reviewed:
> "Sync complete. [N of N proposed changes applied to [persona file]]. Persona last-updated date updated to today."

---

## Key Constraints

- **No changes without confirmation** — present every proposed change for explicit approval before writing. Never batch-apply.
- **Evidence thresholds are hard rules** — 3 to contradict, 2 to add. If threshold not met, present as "below threshold — monitor," not as a proposed change.
- **Preserve exact signal quotes** — when citing evidence, use the verbatim signal text from the signals file, not a paraphrase. Paraphrases drift toward what you expect to find.
- **ICP fit filter is non-negotiable** — Low ICP fit signals don't update personas. A non-ICP customer's confusion is product feedback, not persona intelligence.
- **Flag absence of signals explicitly** — if a signals file is empty or has <5 qualifying signals, say so prominently rather than generating speculative persona updates.
- **One persona at a time when --persona specified** — don't expand scope mid-session unless user asks

---

## Anti-Patterns to Avoid

**Persona drift by anecdote** — updating a persona because one loud customer said something once. The evidence threshold exists to prevent this. One signal = monitor, not change.

**Losing the "why" behind attributes** — when updating attributes, preserve the evidence trail. A persona attribute with no signal provenance is no better than an invented one.

**Over-updating frequently** — persona sync is a monthly operation, not a weekly one. Running it too frequently on sparse signals creates noise, not insight.

**Skipping contradictions** — it's tempting to validate what confirms our beliefs and soft-pedal contradictions. Contradictions are higher-value findings. Flag them prominently.

**Treating Below Threshold findings as noise** — "below threshold — monitor" items are early signals. If the same pattern appears in next month's signals, threshold will be met. Keep them visible.

---

## Integration Points

**Entry from:**
- `/synthesize` — Persona Sync Check at synthesis close surfaces this command
- `/signal` — Persona Impact Check in Step 2.5 flags signals for persona-sync queue
- Quarterly `/customer-knowledge-audit` — if Coverage dimension scores Low, run persona-sync
- Any time a persona file is >60 days old and new signals have accumulated

**Exit to:**
- `📦 Products/[product]/product-context/` — updated persona files (only on confirmation)
- `/prep` — updated personas produce richer context briefs for customer meetings
- `/discover` — updated persona jobs-to-be-done feed initiative framing
- `/compete` — updated ICP definitions feed competitive positioning (who we're fighting for)
- `/signal --source analyst|market` — if persona sync reveals ICP definition drift, route to analyst/market signals for broader market validation
