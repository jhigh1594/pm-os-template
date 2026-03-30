# Product Depth

Build systematic product knowledge through structured deep-dives: demo preparation background, changelog awareness, or support confusion synthesis. Distinct from `/demo-prep` (which builds a ready-to-use guide) — this command builds the underlying expertise.

---

## Relationship

- **`/product-depth`** is the product knowledge building layer — upstream of `/demo-prep` and downstream of `/granola` + `/signal --source support`
- **`/demo-prep`** is the output layer — takes the deep knowledge built here and formats it as a customer-ready demo guide
- **`/granola`** extracts product signals from meetings that feed `--mode confusion` here
- **`/signal --source support|cs-escalation`** is the input signal for `--mode confusion`
- **`/prep`** surfaces this command when a demo meeting is detected without a current demo guide
- After running `--mode changelog`, always consider whether product context files need updating via the `product-operational-intelligence` skill

---

## Core Philosophy

**Product expertise has three layers**: capability knowledge (what it does), use case knowledge (how customers use it), and edge knowledge (where it breaks and why).

Most PMs stop at Layer 1. This command forces Layers 2 and 3 — which are the layers that matter when a customer asks a hard question or a demo hits a rough edge.

The fatal flaw: skipping this command before a high-stakes customer interaction because "I know the product." You may know the features. You don't know what PNC's RTE thinks is broken, or which flow makes a new VP of Engineering walk out of a demo impressed.

---

## Command Syntax

```bash
/product-depth [--product <name>] [--mode <demo|changelog|confusion>] [<topic>]
```

**Arguments**:
- `--product`: `agileplace | okrs | roadmaps | dpd | platform` — optional, inferred from topic if obvious
- `--mode`: Mode of knowledge building (default: asks which mode)
  - `demo` — Build background knowledge for a demo scenario
  - `changelog` — Surface what changed recently that the PM needs to internalize
  - `confusion` — Synthesize where customers get stuck
- `<topic>`: Specific feature, workflow, or area to focus on (optional — without it, covers the whole product)

**Examples**:
```bash
/product-depth --product agileplace --mode demo "capacity planning"
/product-depth --product dpd --mode changelog
/product-depth --mode confusion
/product-depth --product roadmaps --mode demo
```

---

## Your Approach

### Step 0: Parse Arguments

Extract product, mode, and optional topic. If mode is not specified, ask:
> "What kind of product knowledge do you need?
> **(a)** Demo background — understanding a product area deeply before a customer demo
> **(b)** Changelog — what's changed recently that I need to internalize
> **(c)** Confusion map — where customers get stuck with a product or feature"

---

### Step 1 (Demo Mode): Build Demo Background Knowledge

**Goal:** 5-section demo knowledge brief that lets the PM walk into a customer interaction with Layer 2 and Layer 3 knowledge, not just Layer 1.

**Sources to read**:
1. `📦 Products/[product]/product-context/[product]-icp.md` — persona jobs and pain points
2. `📦 Products/[product]/product-context/pm-persona.md` or `cto-persona-deep-dive.md` as relevant
3. Any PRDs or spec-briefs in `📦 Products/[product]/initiatives/` or `spec-briefs/` matching the `<topic>`
4. `📚 Knowledge/Research/signals-[current month].md` — filter for `--product [product]` signals with ICP fit High

**Output structure**:

```markdown
## Product Demo Brief: [Product] — [Topic or "Full Product"] — [Date]

**Layer reached:** Layer 2 (Use Case) + Layer 3 (Edge Knowledge)

### 1. Core Job This Product Does
[One sentence in JTBD framing — "Customers hire [product] to [job], especially when [context]"]

### 2. Top 3 Use Cases
For [persona], in [context/workflow]:
1. **[Use Case Name]**: [2-3 sentence description of what they're doing + why it matters to them]
2. **[Use Case Name]**: [description]
3. **[Use Case Name]**: [description]

### 3. Aha Moment to Lead With
[The single workflow or feature demonstration that, when shown well, creates the "that's exactly what I need" reaction for this persona. Why this moment, not another.]

### 4. Demo Traps to Navigate
- **[Feature/area]**: [What goes wrong if you show it to this persona and why — known rough edge, UX gap, or missing capability]
- **[Feature/area]**: [...]

### 5. Discovery Questions to Weave In
During the demo, ask these to deepen signal capture while making the customer feel heard:
1. "[Question 1]" — listens for [job/pain being explored]
2. "[Question 2]" — listens for [job/pain being explored]
3. "[Question 3]" — listens for [job/pain being explored]

**Sources consulted:** [list files read]
**Knowledge gaps flagged:** [anything undocumented or product-context files >60 days old]
```

**Constraint**: Never fabricate product capabilities — cite only what exists in product-context files, PRDs, or spec-briefs. If something is undocumented but you believe it's true, flag it as unverified.

---

### Step 2 (Changelog Mode): Surface What Changed

**Goal:** Organized summary of recent product changes prioritized by user-facing impact — so the PM can internalize what's new without reading every PR or Jira ticket.

**Sources to read**:
- `📦 Products/[product]/initiatives/` — sort by modification date, identify items modified in last 90 days
- `📦 Products/[product]/spec-briefs/` — same recency filter
- Any shipped status notes in initiative files

**Output structure**:

```markdown
## Product Changelog Brief: [Product] — Last 90 Days — [Date]

### High Importance (core workflow changes — internalize before any customer interaction)
- **[Feature/Change]**: [What it does now vs. before] — [Which persona benefits most] — [Any demo implication]

### Medium Importance (new capabilities — good to know)
- **[Feature/Change]**: [Description] — [Persona impact]

### Low Importance (refinements — awareness only)
- **[Feature/Change]**: [Description]

### Demo Guide Refresh Needed
- [Specific areas in any existing demo guides that are now outdated based on these changes]

**Sources consulted:** [list files read]
```

Optional: Offer to save to `📚 Knowledge/Systems-and-Processes/product-changelog-[product]-[YYYY-MM].md`.

---

### Step 3 (Confusion Mode): Map Where Customers Get Stuck

**Goal:** Evidence-based map of customer confusion zones — organized by product area and classified by confusion type — that informs both demo preparation and roadmap input.

**Sources to read**:
- `📚 Knowledge/Research/signals-[current month].md` — filter for `--source support` or `--source cs-escalation`
- `📚 Knowledge/Research/signals-[prior month].md` — same filter
- If both months empty: note absence and recommend running `/signal --source support` after next CS/support review

**Output structure**:

```markdown
## Customer Confusion Map: [Product] — [Date]

**Signals analyzed:** [N signals from support/cs-escalation, [date range]]

### Confusion Zone 1: [Area Name]
**Frequency:** [N occurrences across signals]
**Affected persona:** [Which ICP persona most affected]
**Confusion type:** [Onboarding Gap | Workflow Mismatch | Product Gap]
**Evidence:** "[Representative customer quote or signal description]"
**Response strategy:**
- Onboarding Gap → [Suggested in-app guidance or onboarding improvement]
- Workflow Mismatch → [Suggested UX clarification or affordance change]
- Product Gap → [Roadmap candidate; current workaround if any]

[Repeat for each confusion zone with 3+ occurrences]

### Patterns Below Threshold (1-2 occurrences — monitor, don't act yet)
- [Brief list]

**Sources consulted:** [list files read]
**Recommendation:** If 3+ new confusion zones identified, route to `/signal --synthesize` and flag in `/prioritize` session.
```

---

## Key Constraints

- **Demo mode is displayed, not auto-saved** — output is for PM internalization; PM decides whether to save as a demo guide file
- **Changelog mode can optionally be saved** — offer to append to `📚 Knowledge/Systems-and-Processes/product-changelog-[product]-[YYYY-MM].md`
- **Confusion mode outputs are candidates for signal routing** — if patterns haven't been captured in the signals file yet, offer to run `/signal` for each identified pattern
- **If product-context files are >60 days old**: flag prominently — "⚠️ Product context files for [product] appear outdated. Insights from demo/changelog modes may not reflect current product state."
- **Never fabricate** — only cite what's in workspace files

---

## Anti-Patterns to Avoid

**Treating Layer 1 as sufficient** — knowing the features doesn't mean knowing the product. Push to Layer 3 (edge knowledge) for every demo-critical area.

**Skipping this before a renewal or escalation** — high-stakes customer interactions where the PM is caught off-guard usually trace back to skipped product knowledge prep.

**Running confusion mode without real signals** — if `signals-YYYY-MM.md` is empty or has no support signals, confusion mode will produce speculative output. Acknowledge the data gap rather than hypothesizing.

---

## Integration Points

**Entry from:**
- `/prep` — surfaces this command when a demo meeting is detected
- `/granola` — product signals extracted from meetings become inputs to `--mode confusion`
- `/signal --source support|cs-escalation` — feeds the signals files consumed by `--mode confusion`

**Exit to:**
- `/demo-prep` — takes the demo background built here and produces a customer-ready demo guide
- `/signal` — confusion zones not yet in the signals file should be routed there
- `/spec` — product gaps identified in confusion mode are roadmap candidates
