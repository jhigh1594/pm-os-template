---
description: Run the customer knowledge audit workflow
---
# Customer Knowledge Audit

Diagnose the PM's current state of customer knowledge across five dimensions — coverage, recency, depth, breadth, and action — then recommend the specific investments needed to close identified blind spots.

---

## Relationship

- **`/customer-knowledge-audit`** is the diagnostic layer — it tells you where your customer knowledge has gaps, not what to fill them with
- **`/signal`** is the capture tool that fills Coverage and Recency gaps identified here
- **`/persona-sync`** updates personas when Depth gaps are identified
- **`/discover`** is where Understanding gaps go — initiative framing that needs customer knowledge it doesn't have
- Cadence: **Quarterly** or before a major initiative launch
- Pairs with `/product-depth --mode confusion` for the Product Operational dimension

---

## Core Philosophy

**Customer knowledge degrades if not actively maintained.**

The PM who believes they "know their customers" because they attended discovery calls six months ago is operating on stale evidence. Markets shift. New personas emerge. Old assumptions harden into unexamined beliefs.

The audit doesn't measure what you've done. It measures what you currently know and where the evidence is thin. A passing score isn't the goal — an accurate score is.

**Five dimensions of customer knowledge** (from the Cagan/SVPG framework):
1. **Coverage** — Which personas have evidence? Which are documented but empty?
2. **Recency** — How fresh is the evidence? When did signals last arrive?
3. **Depth** — Are jobs documented with real evidence, or asserted without it?
4. **Breadth** — Do signals come from multiple sources, or is one source dominating?
5. **Action** — Are customer evidence citations showing up in decisions?

---

## Command Syntax

```bash
/customer-knowledge-audit [--product <name>] [--depth <quick|full>]
```

**Arguments**:
- `--product`: `agileplace | okrs | roadmaps | dpd | platform` — if omitted, asks or audits all
- `--depth`:
  - `quick` (default) — H/M/L score per dimension + top 3 blind spots + commands to run. 5-10 minutes.
  - `full` — Detailed evidence inventory per persona, signal distribution chart, decision journal analysis. 15-20 minutes.

**Examples**:
```bash
/customer-knowledge-audit --product agileplace
/customer-knowledge-audit --product agileplace --depth full
/customer-knowledge-audit                                    # asks which product
```

---

## Your Approach

### Step 0: Parse Arguments and Load Evidence Base

Extract product and depth. Load:
1. `📦 Products/[product]/product-context/` — all persona and ICP files (note last-modified dates for each)
2. `📚 Knowledge/Research/signals-[YYYY-MM].md` — current month + prior 2 months (3-month window)
3. `📚 Knowledge/People/` — any account or stakeholder files (if they exist)

Count:
- Total persona files loaded
- Total qualifying signals in 3-month window (ICP fit High + Medium, source = interview|call|support|cs-escalation|renewal)
- Days since last signal captured per product area (most recent signal date)
- Days since each persona file was last modified

---

### Step 1: Score Each Dimension

#### Dimension 1: Coverage
*Which ICP personas have 3+ signal support? Which are documented but evidence-thin?*

**Evidence check**: For each persona file, count qualifying signals in the 3-month window that match this persona.
- 5+ signals: Full coverage
- 3-4 signals: Partial coverage
- 1-2 signals: Thin coverage
- 0 signals: No recent coverage (documented but orphaned)

**Score**:
- **H (High)**: All named personas have 3+ signals; no orphaned personas
- **M (Medium)**: 50-80% of named personas covered; 1-2 orphaned
- **L (Low)**: <50% covered; significant persona gaps

#### Dimension 2: Recency
*When did the most recent signal arrive? When were persona files last updated?*

**Evidence check**:
- Days since last customer signal (any source, any persona)
- Days since last persona file modification
- Last source type (interview is highest fidelity; support is medium)

**Score**:
- **H**: Signal in the last 30 days; persona updated in last 60 days
- **M**: Signal in last 31-60 days; persona updated in last 61-90 days
- **L**: No signal in 60+ days; persona 90+ days old

#### Dimension 3: Depth
*Are functional jobs documented with evidence, or asserted?*

**Evidence check**: For each persona's jobs-to-be-done section:
- Count jobs that have ≥1 signal citation (evidence-backed)
- Count jobs that have no signal citation (asserted)
- Note balance of positive vs. negative evidence (praise vs. pain)

**Score**:
- **H**: >70% of documented jobs have signal evidence; positive and negative evidence both present
- **M**: 40-70% jobs have evidence; some imbalance (all praise or all pain)
- **L**: <40% jobs have evidence; primarily asserted attributes; no negative evidence present

#### Dimension 4: Breadth
*What is the signal source distribution? Is >70% from a single source type?*

**Evidence check**: In the 3-month window, count signals by source type:
- `interview` | `call` | `support` | `cs-escalation` | `renewal` | `expansion` | `analyst` | `market`

**Concentration risk check**: Is any single source >70% of total signals?

**Score**:
- **H**: No source is >60% of signals; at least 3 different source types present
- **M**: One source is 60-75% of signals; 2 source types present
- **L**: One source is >75%; only 1-2 source types; likely single-source bias

#### Dimension 5: Action
*Are decisions citing customer evidence?*

**Evidence check**: If `📚 Knowledge/` has a decision journal or if `/decide` has been run recently — scan for customer evidence citations.
- Count decisions in the last 90 days
- Count how many cite customer signals or persona data
- Calculate the ratio

**If no decision journal found**: Score as Unknown and note: "No decision journal found — consider running `/decide` to establish baseline. Cannot score this dimension without evidence."

**Score**:
- **H**: >60% of recent decisions cite customer evidence
- **M**: 30-60% cite customer evidence
- **L**: <30% cite customer evidence; or dimension Unknown

---

### Step 2: Generate Audit Output

#### Quick Depth (`--depth quick`)

```markdown
## Customer Knowledge Audit: [Product] — [Date]

**Evidence window:** [3-month period]
**Signals analyzed:** [N qualifying signals]
**Personas reviewed:** [N persona files]

### Dimension Scores

| Dimension | Score | Key Reason |
|-----------|-------|------------|
| Coverage | [H/M/L] | [One-line summary — e.g., "2 of 4 personas have <3 signals"] |
| Recency | [H/M/L] | [One-line — e.g., "Last interview was 47 days ago"] |
| Depth | [H/M/L] | [One-line — e.g., "60% of RTE jobs are asserted without signal support"] |
| Breadth | [H/M/L] | [One-line — e.g., "73% of signals from support — missing interview/call balance"] |
| Action | [H/M/L] | [One-line — e.g., "4 of 7 recent decisions cite customer evidence"] |

**Overall:** [All H = Strong | Mix of H and M = Solid | Any L = Gaps requiring attention]

---

### Top 3 Blind Spots

1. **[Blind spot 1]** — [Dimension affected] — [Specific gap in plain language]
   → Recommended action: [Command + specific arguments]

2. **[Blind spot 2]** — [Dimension affected] — [Specific gap in plain language]
   → Recommended action: [Command + specific arguments]

3. **[Blind spot 3]** — [Dimension affected] — [Specific gap in plain language]
   → Recommended action: [Command + specific arguments]

---

### Recommended Investments

**Highest-value action right now:** [Single most impactful command to run — the one that addresses the worst-scoring dimension]

**Complete recovery sequence:**
```bash
# Address [dimension 1 gap]
[specific command]

# Address [dimension 2 gap]
[specific command]
```

**Knowledge health trajectory:** [Improving / Stable / Degrading] — [One sentence explanation]
```

#### Full Depth (`--depth full`)

Run all Quick Depth content, then append:

```markdown
---

### Evidence Inventory by Persona

#### [Persona Name] — `[file path]` — Last updated: [date]

| Job-to-be-Done | Evidence? | Signal count | Source types | Last signal |
|----------------|-----------|--------------|--------------|-------------|
| [Job 1] | ✅ Backed | [N] | [types] | [date] |
| [Job 2] | ⚠️ Asserted | 0 | — | — |
| [Job 3] | ✅ Backed | [N] | [types] | [date] |

**Coverage gap:** [Which jobs need more evidence]
**Contradiction risk:** [Any jobs that may have drifted from current reality based on signal dates]

[Repeat for each persona]

---

### Signal Source Distribution (3-month window)

| Source | Count | % of total | Assessment |
|--------|-------|------------|------------|
| interview | [N] | [%] | [note if >70%] |
| call | [N] | [%] | |
| support | [N] | [%] | |
| cs-escalation | [N] | [%] | |
| renewal | [N] | [%] | |
| expansion | [N] | [%] | |
| analyst | [N] | [%] | |
| market | [N] | [%] | |

**Concentration risk:** [flag if any source >70%]
**Missing sources:** [source types with 0 signals that should be represented]

---

### Decision Journal Analysis (if available)

| Decision | Customer evidence cited? | Evidence type |
|----------|--------------------------|---------------|
| [Decision 1] | ✅ Yes | [signal type] |
| [Decision 2] | ❌ No | — |
| [Decision 3] | ✅ Yes | [signal type] |

**Action score:** [N]% of decisions cite customer evidence ([N of N])
**Highest-risk decisions:** [Any major decisions made without customer evidence — flag these for retrospective grounding]
```

---

## Key Constraints

- **Scores are evidence-based, not self-reported** — the audit draws from actual files and signal counts, not the PM's self-assessment
- **If signals files don't exist or are empty**: note this explicitly rather than scoring dimensions based on absence. "Cannot score Coverage — no signals file found for this period. Run `/signal` to begin capturing."
- **Unknown is a valid score for Action** when no decision journal exists — don't estimate or assume
- **Don't adjust scores to be more comfortable** — a Low score means the gap is real. The value is in accurate diagnosis.

---

## Anti-Patterns to Avoid

**Running the audit and ignoring the recommendations** — the audit output is only valuable if it changes what you do next. If all three recommended commands don't get run within the next session, the audit produced no value.

**Treating the score as a report card** — the goal is calibration, not achievement. A PM who scores all L and immediately runs the recommended commands is better off than one who scores M and does nothing.

**Auditing instead of discovery** — the audit tells you what you know; `/discover` and actual customer conversations fill the gaps. Don't substitute auditing for the research itself.

**Quarterly audit without monthly signal capture** — the audit reads what's in the signals files. If signals aren't captured monthly, the quarterly audit will always show recency and coverage gaps regardless of how well the PM knows customers from memory.

---

## Integration Points

**Entry from:**
- Quarterly cadence (triggered by PM or calendar reminder)
- Before major initiative launch — confirm customer knowledge foundation is solid
- After returning from a period without customer contact (conference travel, vacation, sprint heads-down)

**Exit to:**
- `/signal` — fills Coverage and Recency gaps
- `/persona-sync` — fills Depth gaps when signals have accumulated
- `/discover` — fills Understanding gaps in active initiatives
- `/product-depth --mode confusion` — addresses the intersection of customer knowledge and product knowledge
- `📚 Knowledge/People/` — source for Breadth gaps if specific accounts are underrepresented
