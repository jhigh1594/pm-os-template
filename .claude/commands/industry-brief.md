---
description: Run the industry brief workflow
---
# Industry Brief

Scan the broader market landscape beyond direct competitors — analyst coverage, adjacent market moves, enterprise software earnings signals, and job posting demand indicators. Activates the `industry-intelligence` skill for structured analysis with source hierarchy enforcement.

---

## Relationship

- **`/industry-brief`** is the market scanning layer — broader than `/compete` (direct competitors) and more systematic than `/daily-brief --industry` (daily triage)
- **`/compete`** covers direct competitive positioning; `/industry-brief` covers category forces, analyst signals, and adjacent threats
- **`/signal --source analyst|market`** captures findings from this command as structured signals for monthly synthesis
- **`/think`** is the strategic framing layer — route industry signals here when they challenge a Company strategic bet
- **`/synthesize`** picks up analyst/market signals from the monthly signals file in the same synthesis pass as customer signals
- **`/daily-brief --industry`** uses this command's source hierarchy for daily industry signal triage — this command goes deeper

---

## Core Philosophy

**Market intelligence is only as good as its source discipline.**

The fatal flaw: treating a competitor press release the same as a Gartner report. Tier 3 sources (vendor announcements, blog posts) describe how companies want to be perceived — not how analysts evaluate them, how buyers actually choose, or where the category is going.

Source hierarchy from `industry-intelligence` skill (enforced in every output):
- **Tier 1** (High confidence): Analyst reports, earnings call transcripts, regulatory filings — independent analysis with methodology
- **Tier 2** (Medium confidence): Industry trade press, credible customer surveys — editorial judgment applied
- **Tier 3** (Low confidence): Competitor announcements, vendor blogs, press releases — positioning only; never treat as factual capability claims

Every finding gets a tier label. Tier 1 and Tier 3 findings are never mixed without explicit separation.

---

## Command Syntax

```bash
/industry-brief [--mode <analyst|market|earnings|jobs>] [--save]
```

**Arguments**:
- `--mode`: What to scan (default: asks which mode, or run all if user says "full brief")
  - `analyst` — Analyst coverage scan for Company's relevant quadrants/waves
  - `market` — Adjacent market signals — where category borders are moving
  - `earnings` — Enterprise software earnings call signals relevant to Company's space
  - `jobs` — Job posting demand indicators for organizational investment signals
- `--save`: Append findings to `📚 Knowledge/Market/industry-intelligence-[YYYY-MM].md`

**Examples**:
```bash
/industry-brief --mode analyst
/industry-brief --mode market
/industry-brief --mode earnings
/industry-brief --mode jobs
/industry-brief                          # prompts for mode
/industry-brief --save                   # runs all modes and saves output
```

---

## Your Approach

### Step 0: Parse Arguments and Orient

Extract mode and save flag. If mode not specified and user hasn't said "full brief", ask:
> "What kind of market intelligence do you need today?
> **(a)** Analyst — where Company sits in the quadrants/waves and what's changing
> **(b)** Market — adjacent players and category border movements
> **(c)** Earnings — enterprise software companies' portfolio/planning/AI signals
> **(d)** Jobs — demand indicators from job posting patterns
> **(e)** Full brief — all four"

Check if `📚 Knowledge/Market/industry-intelligence-[YYYY-MM].md` exists for the current month — if yes, mention it: "A brief from this month already exists. Running a new scan will add to it."

---

### Step 1 (Analyst Mode): Analyst Coverage Scan

**Goal:** Surface what analysts are evaluating in Company's categories — their criteria, their current ratings, and any signals of criteria shifts. What buyers are being told to look for.

**Key reports to cover** (from `industry-intelligence` skill):
| Report | Relevance | How to use |
|--------|-----------|------------|
| Gartner Magic Quadrant for Strategic Portfolio Management | Direct — Company appears | Criteria weights, leader attributes, buyer evaluation criteria |
| Forrester Wave for [your category] | Direct — [your product] | Evaluation framework, current scores, criteria evolution |
| Gartner Market Guide for Project and Portfolio Management | Category context | Where the market is going broadly |
| IDC MarketScape for PPM | Alternative perspective | Complements Gartner view |

**Output structure for each report surfaced**:

```markdown
### [Report Name] — [Version/Year if known] — Tier 1

**What analysts evaluate in this category:**
- [Criterion 1]: [How Company typically scores or is positioned]
- [Criterion 2]: [Same]

**Key finding:**
[What this report reveals that's strategically relevant — positioning shift, criteria evolution, buyer guidance]

**So what for Company:**
[1-2 sentences — what should change or be validated based on this signal]

**Validates or challenges:**
[Does this confirm existing strategy, or surface a tension worth investigating?]

**Confidence:** High (Tier 1 — analyst with methodology)
**Recommended action:** [Route to `/signal --source analyst` / Update battlecard / Flag for `/think` / No action needed]
```

---

### Step 2 (Market Mode): Adjacent Market Signals

**Goal:** Detect movement in adjacent markets that could change Company's competitive landscape — players expanding into portfolio management from project management, OKR software, resource management, or strategic planning.

**Adjacent markets to monitor**:
- Project management platforms (Atlassian/Jira, Monday.com, Asana, Smartsheet)
- OKR software (Lattice, Betterworks, Perdoo, 15Five) — specifically moving upmarket
- Resource management (Workday, SAP, Anaplan) — expanding into execution
- Strategic planning tools (Cascade, Quantive) — adding execution layer
- AI-native planning (any new entrant framing around "AI planning copilot")

**Adjacent Market Threat Assessment** (apply for any player showing movement):

```markdown
### Adjacent Player: [Company] — Tier [1/2/3]

**Entry signal:** [What they're doing that signals expansion toward Company's space]
**Source:** [Specific source — earnings call, product announcement, analyst report — with tier]

**Entry Path Analysis:**
- Capability gap they need to close: [What they're missing to compete in Company's space]
- Time to close: [Rough estimate — near-term / 12-18 months / 3+ years]
- Enterprise sales motion: [Do they have the motion to win in Company's target segment?]

**Customer Job Overlap:**
- Shared jobs-to-be-done: [Where their customers and Company's customers overlap]
- Workflow overlap: [Specific workflows where switching opportunity could emerge]
- Dual users: [Are there companies already using both?]

**Switching Cost Comparison:**
- Why a customer might prefer them: [Honest assessment]
- Company's defensible moat in this scenario: [Data network effects / workflow integration / switching cost / other]

**Threat level:** [High / Medium / Low — with reasoning]
**Confidence:** [Tier label]
**Recommended action:** [Monitor / Flag for `/think` / Route to `/compete` for battlecard update]
```

---

### Step 3 (Earnings Mode): Enterprise Software Earnings Signals

**Goal:** Surface signals from enterprise software companies' earnings calls that indicate where the market is going — AI investment, portfolio/planning language, adjacent category moves, and buyer demand shifts.

**Companies to monitor** (publicly traded, enterprise software, relevant to Company's space):
- Atlassian (TEAM) — most direct signal on agile planning investment
- SAP — portfolio management + strategic planning; large enterprise buyer
- Salesforce — connected planning framing; enterprise buyer context
- [FILL IN: Relevant public companies in your space]
- Microsoft (Project, Azure, Teams) — indirect competitor but strong signal on enterprise tooling investment
- Workday — resource management + strategic planning adjacency

**For each relevant earnings signal found**:

```markdown
### [Company] Earnings Signal — [Quarter/Year] — Tier 1

**Signal:** "[Verbatim or close paraphrase of language used — what executive said on the call]"

**Why it matters for Company:**
[Is this buyer vocabulary shifting? Category framing changing? Adjacent investment signal?]

**Demand signal type:**
[ ] Vocabulary shift — buyers will start using this language; Company's positioning may need updating
[ ] Category entry signal — this company is investing in Company's space
[ ] Validation signal — large company investment validates Company's category as growing
[ ] Competitive pressure — signals they're prioritizing areas that overlap with Company

**So what for Company:**
[1-2 sentences on strategic implication]

**Confidence:** High (Tier 1 — earnings call transcript)
**Recommended action:** [Route to `/signal --source market` / Route to `/think` / No action]
```

---

### Step 4 (Jobs Mode): Demand Indicator Scan

**Goal:** Surface non-obvious signals of organizational investment in Company's value space — based on what companies are hiring for, which indicates where they're investing before product vendors see it.

**Job posting signal types** (from `industry-intelligence` skill):
| Signal | What to look for | Why it matters |
|--------|-----------------|----------------|
| **"Head of Portfolio Management"** surge | Volume and pace of this title appearing at enterprise companies | Leading indicator of organizational portfolio investment |
| **"Agile Program Manager"** at scale | Large non-tech enterprises hiring Agile titles | Category expansion beyond tech — new ICP candidates |
| **"OKR Program Lead"** | OKR-specific program roles at enterprise | Validates OKR category growth; ICP expansion |
| **"Chief of Staff / Head of Strategy Ops"** with planning tools | Strategy ops roles specifying planning/portfolio tools | Champion persona signal — who sponsors Company purchases |

**Output for job signals** (Tier 2 — treat with medium confidence):

```markdown
### Job Signal: [Job Title / Pattern] — Tier 2

**Observation:** [What's changing in job postings — volume, new industries, new requirements]
**Source:** [LinkedIn trends / industry report / press coverage — specify]

**Demand signal:**
[What this hiring pattern reveals about organizational investment direction]

**ICP implication:**
[Does this expand or contract Company's ICP? Does it validate current ICP or suggest a new segment?]

**Confidence:** Medium (Tier 2)
**Recommended action:** [Route to `/signal --source market` / Flag for ICP review / Monitor trend]
```

---

### Step 5: Synthesis and Recommended Actions

After running one or more modes, close with a synthesis section:

```markdown
## Industry Brief Synthesis — [Date]

**Modes covered:** [analyst / market / earnings / jobs]

### Top 3 Strategic Signals
1. **[Finding 1]** — [Tier] — [Strategic implication in one sentence]
2. **[Finding 2]** — [Tier] — [Strategic implication in one sentence]
3. **[Finding 3]** — [Tier] — [Strategic implication in one sentence]

### Validates Company Strategy
[Findings that confirm current strategic direction — what we're doing right]

### Challenges Company Strategy
[Findings that surface tension with current direction — what deserves a second look]

### Recommended Signal Captures
Run these `/signal` commands to preserve findings:
- `/signal --source analyst "[key finding 1]"`
- `/signal --source market "[key finding 2]"`

### For Deeper Analysis
- Route to `/think` if: [specific finding that challenges a foundational strategic assumption]
- Update `/compete` battlecard if: [specific competitor movement detected]
- Route to `/persona-sync` if: [finding challenges ICP definition]
```

---

### Step 6 (if --save): Persist to Knowledge Base

If `--save` flag used, append the full brief to `📚 Knowledge/Market/industry-intelligence-[YYYY-MM].md`:
> "Appending to `📚 Knowledge/Market/industry-intelligence-[YYYY-MM].md`. Confirm? (y/n)"

---

## Key Constraints

- **Label every finding with its source tier** — never present analyst and vendor claims with equivalent confidence
- **Analyst sources >12 months old must be labeled** "as of [date]" — a 2023 Gartner report is not current for a 2026 positioning decision
- **Never present Tier 3 (vendor announcements) as factual capability claims** — treat as positioning signals only
- **Adjacent market analysis is hypothesis, not prediction** — frame as "signals suggest" not "this will happen"
- **Recency asymmetry**: Tier 1 sources >12 months = use with explicit dating; Tier 3 sources = always label regardless of age

---

## Anti-Patterns to Avoid

**Mixing tiers without labeling** — citing a competitor blog post and a Gartner report in the same breath as equivalent evidence. They're not.

**Treating every adjacent market move as a threat** — most adjacent market signals are noise. Apply the full threat assessment framework before escalating to strategy-level concern.

**Running this instead of `/compete`** — this command scans the category and broader market; `/compete` builds positioning against specific named competitors. Both are needed; neither replaces the other.

**Stale analyst cites** — an analyst report from 18 months ago may describe a market that's shifted. Always date your sources.

---

## Integration Points

**Entry from:**
- `/daily-brief --industry` — surfaces 2-3 signals from this command's framework; refers to `/industry-brief` for deeper coverage
- `/think` — when strategic analysis needs market context
- Weekly/monthly cadence as a standalone scan

**Exit to:**
- `/signal --source analyst|market` — capture findings as structured signals
- `/compete` — competitor movements detected here feed battlecard updates
- `/think` — findings that challenge a foundational strategic bet
- `/persona-sync` — if industry signals affect ICP definition
- `📚 Knowledge/Market/industry-intelligence-[YYYY-MM].md` — saved via `--save` flag
