# Data Story

Package an existing analysis into an audience-ready narrative. Transforms raw findings, Pendo data, or usage metrics into the specific format each audience needs — executive BLUF, product narrative arc, sales proof points, or CS account specifics.

---

## Relationship

- **`/data-story`** is the packaging layer — downstream of `/pendo`, `b2b-data-analyst` skill, and `/measure`; upstream of `/write` (for exec comms) and battlecards (for sales)
- **`/pendo`** generates raw findings that `/data-story` turns into audience narratives
- **`/measure`** defines metrics; `/data-story` tells the story of those metrics to audiences who can act on them
- **`/write --type exec`** takes the exec output here and polishes it into final communication format
- Not a replacement for analysis — this command packages analysis that already exists

---

## Core Philosophy

**The right insight in the wrong format doesn't move anyone.**

A data finding is only as valuable as the action it produces. An exec who receives a data dump without a clear ask does nothing. A sales rep who can't quote a specific number loses the conversation. A CS manager who can't identify which accounts are at risk can't intervene.

The fatal flaw: running the analysis, writing up the findings for yourself, and distributing the same document to everyone. Different audiences need different structures, different levels of detail, and different calls to action.

---

## Command Syntax

```bash
/data-story [--audience <exec|product|sales|cs>] [--context <path-or-description>] [<analysis>]
```

**Arguments**:
- `--audience`: Target audience format (required; prompts if missing)
  - `exec` — BLUF structure, one number + one implication + one ask
  - `product` — Narrative arc: what's happening → why → what to test or build
  - `sales` — Talktrack-ready proof points with specific quotable numbers
  - `cs` — Account-level specifics with at-risk signals and intervention recommendations
- `--context`: Optional path to source file (e.g., a Pendo export or analysis doc) or brief description of what product/area the data is about
- `<analysis>`: The raw finding or analysis to package — paste verbatim; rough is fine

**Examples**:
```bash
/data-story --audience exec "Pendo shows dependency view adoption dropped 23% in Q1 among enterprise accounts"
/data-story --audience sales --context "agileplace dependency view" "Usage is up 40% YoY in accounts using it weekly"
/data-story --audience cs "NatWest account has 3 active users on dependency view, down from 12 last quarter"
/data-story --audience product "Capacity planning feature has 15% adoption in enterprise, 62% in mid-market — adoption stalls at the 'configure swim lanes' step"
```

---

## Your Approach

### Step 0: Parse Arguments

Extract audience, context, and raw analysis. If `--audience` is missing, ask:
> "Who is this for?
> **(a)** Exec — 1 number, 1 implication, 1 ask (BLUF)
> **(b)** Product — narrative arc with diagnosis and recommendation
> **(c)** Sales — quotable proof points for a customer conversation
> **(d)** CS — account-level specifics with intervention recommendations"

If `<analysis>` is missing, ask: "Paste the finding or analysis you want to package — rough is fine."

---

### Step 1 (Exec Mode): BLUF Structure

**Goal:** One slide, one conversation turn. Exec time is scarce. BLUF = Bottom Line Up Front.

**Exec communication rules** (from `exec-comms` skill):
- Lead with the conclusion, not the data
- One number — the most important metric, stated plainly
- One implication — what does this number mean for the business
- One ask — what do you need from them (approval, decision, awareness)

**Output structure**:

```markdown
## Executive Summary: [Topic] — [Date]

**Bottom line:** [One sentence — the conclusion, not the finding. "We have a retention problem in enterprise accounts using dependency view" not "Adoption dropped 23%."]

**The number:** [One metric that anchors the conversation — specific, concrete, attributable]
- Context: [Brief — what's normal, what's the benchmark, what's changed]

**What it means for the business:** [1-2 sentences — revenue, retention, or strategic implication. Translate usage data into business language.]

**The ask:** [One specific action — decision, approval, or endorsement. Not "awareness."]
- Timeline: [When you need an answer]
- Stakes if we don't act: [What happens in 30/60/90 days without action]

---
*Full analysis available at [path if applicable]. Source: [Pendo / customer interview / support tickets / other]*
```

After generating exec format, offer:
> "Want me to expand this into an exec communication document? Run `/write --type exec [this finding]`"

---

### Step 2 (Product Mode): Narrative Arc

**Goal:** Tell the story of what's happening in the product — from symptom to diagnosis to recommendation. For product team conversations, roadmap reviews, and team alignment sessions.

**Narrative structure**:
1. **What's happening** — the observable pattern (metric movement, adoption curve, behavioral signal)
2. **Why it's happening** — the most likely explanation (don't skip this; a finding without diagnosis is noise)
3. **What to test or build** — specific recommendation (be concrete; "investigate further" is not a recommendation)

**Output structure**:

```markdown
## Product Data Story: [Feature/Area] — [Date]

### What's Happening
[1-2 sentences describing the pattern clearly. State the metric, the direction, and the scope.]

**Key data point:** [Specific number — usage, adoption rate, drop-off point, segment divergence]

### Why It's Happening (Hypothesis)
[Most likely explanation — grounded in product knowledge, customer signals, or usage patterns]

**Supporting evidence:** [Any corroborating signals — support tickets, customer quotes, related metric]
**Alternative hypothesis:** [Second-most-likely explanation — important for preventing premature closure]

### What to Test or Build
**If the primary hypothesis is correct:**
- [Specific action — UX change, onboarding improvement, feature add, or further investigation]
- **Success signal**: [How we'd know this worked in 30/60 days]

**If the alternative hypothesis is correct:**
- [Different action]
- **Success signal**: [Different metric]

**Recommended next step:** [One action — the highest-confidence move regardless of which hypothesis is true]

**Sources consulted:** [Pendo / signals file / customer interview / support tickets]
```

---

### Step 3 (Sales Mode): Talktrack Proof Points

**Goal:** Give sales reps specific, quotable numbers they can use in customer conversations — with the narrative context to use them correctly, not just cite them awkwardly.

**Sales proof point requirements**:
- Specific numbers (percentages, timeframes, comparisons) — not vague claims
- Attributable to a credible source — "Pendo data across X enterprise accounts"
- Framed as customer benefit — "accounts that use it weekly see X" not "we have X users"
- Usage: can be dropped into a conversation naturally without rehearsal

**Output structure**:

```markdown
## Sales Proof Points: [Feature/Area] — [Date]

### The Headline Number
"[Quotable stat in one sentence — frame as customer outcome, not product metric]"
Source: [Pendo / survey / customer interview — give reps the attribution]

### Supporting Stats (use 1-2 max per conversation)
- "[Stat 2]" — [Source]
- "[Stat 3]" — [Source]

### How to Use It
**In a discovery conversation:** "[Natural language talktrack — how to introduce this without it sounding like a sales pitch]"

**When a prospect says they're happy with their current tool:** "[Specific response using this data to create contrast]"

**When asked for proof:** "[Response that establishes credibility — cites source, names the account segment]"

### What This Doesn't Prove
[Important: what this data can't claim — prevents reps from over-claiming and losing credibility]

**Source:** [Full attribution — date, source type, account segment covered]
```

After generating sales format, offer:
> "Want to add this as an evidence row in a battlecard? I can append to `📚 Knowledge/Market/battlecard-[competitor].md` if this is competitive proof."

---

### Step 4 (CS Mode): Account-Level Specifics

**Goal:** Give CS teams the account-level detail they need to have an informed customer conversation — at-risk signals, intervention recommendations, and context for a QBR or renewal discussion.

**CS needs from data**:
- Account-specific (not aggregate) — "NatWest" not "enterprise accounts"
- At-risk signals surfaced explicitly — declining usage, feature abandonment, low adoption
- Actionable intervention — what should CS do with this information
- Context for conversation — what to say to the customer, not just what the data shows

**Output structure**:

```markdown
## CS Account Brief: [Account Name or Segment] — [Date]

### Account Signal
**[Account name / Segment]**: [1-2 sentence summary of what the data shows]

**Risk level:** [High / Medium / Low — with reasoning]
- At-risk indicator: [Specific metric — declining usage, feature drop-off, inactive users]
- Benchmark: [What healthy looks like for accounts of this size/tier]
- Trend: [Improving / Stable / Declining — with timeframe]

### What to Watch
- **[Metric 1]**: [Current value] vs. [Benchmark] — [Direction]
- **[Metric 2]**: [Current value] vs. [Benchmark] — [Direction]

### Recommended Intervention
**If high risk:** [Specific CS action — proactive outreach, executive sponsor engagement, onboarding re-run, feature coaching]
**What to say:** "[Suggested customer-facing framing — honest, not alarming]"

### QBR/Renewal Context
[1-2 sentences — what to acknowledge vs. what to push on in a renewal or QBR conversation]

**Source:** [Pendo / CS notes / support tickets — with date]
```

After generating CS format, offer:
> "Want to add this to the account file? I can append to `📚 Knowledge/People/[account-name].md` as an at-risk note."

---

## Key Constraints

- **Never fabricate data** — only package analysis that already exists. If the analysis doesn't have specific numbers, note the gap rather than inventing estimates.
- **Source every claim** — state where the data came from (Pendo, customer interview, support signals) in every output format. Sourceless claims erode credibility.
- **Audience-specific, not audience-diluted** — don't append "additional context" sections that turn an exec BLUF into a product narrative. Each format is intentionally constrained.
- **Flag stale data** — if the analysis is from a Pendo export or signals file more than 60 days old, note it: "Data as of [date] — verify current state before using in customer conversation."

---

## Anti-Patterns to Avoid

**Same deck for everyone** — execs and product teams need fundamentally different structures. Packaging the same analysis for both means neither gets what they need.

**The data without the "so what"** — a chart without an implication is decoration. Every data story must answer: "So what does this mean and what should we do about it?"

**Over-citing in exec comms** — one number, one implication, one ask. The exec doesn't need the methodology; they need the conclusion. Save the supporting data for questions.

**Vague CS signals** — "adoption is low" is not an account brief. "NatWest has 3 active users this month, down from 12 last quarter, on a renewal call next Thursday" is.

---

## Integration Points

**Entry from:**
- `/pendo trend|anomaly|adoption|health` — raw Pendo finding ready for packaging
- `b2b-data-analyst` skill analysis — any substantial data finding
- `/measure` — metrics findings ready for communication
- Any moment when data exists but the audience-specific format doesn't

**Exit to:**
- `exec` format → `/write --type exec` for final polish
- `sales` format → `📚 Knowledge/Market/battlecard-[competitor].md` as evidence row
- `cs` format → `📚 Knowledge/People/[account].md` as at-risk account note
- `product` format → feeds `/spec` or `/signal` if it reveals a product gap
