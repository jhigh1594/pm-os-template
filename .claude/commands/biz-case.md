---
description: Run the biz case workflow
---
# Business Case Reasoning

Apply financial and organizational reasoning to product decisions — so business constraints inform what we build, not just constrain it after the fact. Activates the `business-reasoning` skill for structured analysis.

---

## Relationship

- **`/biz-case`** is the business reasoning layer — upstream of `/spec` (provides Business Case section) and `/decide` (provides cross-functional framing)
- **`/spec --type full`** calls `--mode review` to generate or audit the Business Case section
- **`/decide`** pairs with `--mode tradeoff` for decisions with cross-functional dependencies
- **`/think`** is the strategic framing layer; `/biz-case` is the financial and organizational layer — they're complementary, not duplicative
- **`business-reasoning` skill** contains the underlying frameworks this command operationalizes

---

## Core Philosophy

**Business constraints are product inputs, not afterthoughts.**

The fatal error: writing a full PRD before asking "how does Finance think about this" or "what does CS need to adopt it." By then, you're defending a spec against objections instead of designing a spec that pre-empts them.

Four distinct jobs that PMs need from business reasoning:
1. **Quantify** — What does this move on the revenue model?
2. **Map friction** — Which functions will push back, why, and how hard?
3. **Empathize** — What does it look like from a specific function's seat?
4. **Audit** — Does this PRD have a real business case or just a strategic rationale?

Each job is a different mode.

---

## Command Syntax

```bash
/biz-case [--product <name>] [--mode <model|tradeoff|perspective|review>] [<feature-or-initiative>]
```

**Arguments**:
- `--product`: `agileplace | roadmaps | dpd | platform` — optional, inferred if obvious
- `--mode`: Mode of business reasoning (default: asks which mode)
  - `model` — Revenue impact model with Conservative/Expected/Upside cases
  - `tradeoff` — Cross-functional constraint map across all five functions
  - `perspective` — Single-function deep dive using the incentive map
  - `review` — Business Case section audit or generation for an existing spec
- `<feature-or-initiative>`: Name of the feature, initiative, or decision to analyze

**Examples**:
```bash
/biz-case --product agileplace --mode model "bulk card operations"
/biz-case --mode tradeoff "dependency visualization"
/biz-case --mode perspective "what does CS think about dependency view"
/biz-case --product agileplace --mode review "path/to/spec.md"
/biz-case --mode model "Feature usage analytics"
```

---

## Your Approach

### Step 0: Parse Arguments

Extract product, mode, feature/initiative, and any spec path. If mode is not specified, ask:
> "What kind of business reasoning do you need?
> **(a)** Revenue model — quantify ARR impact with Conservative/Expected/Upside cases
> **(b)** Cross-functional tradeoff — map how CS, Sales, Finance, Legal, Engineering will react
> **(c)** Single function perspective — how does one function think about this decision
> **(d)** Business Case review — audit or generate the Business Case section of a spec"

---

### Step 1 (Model Mode): Build Revenue Impact Model

**Goal:** Honest, labeled financial estimate with assumptions explicit — not false-precision modeling, but structured thinking that clarifies what you believe and why.

**Pre-flight**: Ask three questions before modeling:
1. "What's the baseline metric we're trying to move? (retention, expansion, new logo, cost-to-serve)"
2. "Which ICP segment is most affected? (Rough size in accounts or ARR if known)"
3. "What time horizon are we estimating? (Next quarter, next year, 3-year)"

**Model structure** — apply the B2B SaaS unit economics model from the `business-reasoning` skill:

```
Revenue pathway:
Feature → Adoption rate (% of ICP accounts using it in 12 months)
  → Affected account segment (new logo | expansion | retention)
  → ARR mechanism: which does this drive?
    - New logo enablement: feature closes deals by removing a blocker
    - Expansion: feature enables seat expansion or tier upgrade
    - Retention: feature reduces churn — what's the at-risk ARR base?
  → ARR impact = (affected accounts) × (ARR per account) × (adoption rate)
```

**Output structure**:

```markdown
## Revenue Impact Model: [Feature] — [Product] — [Date]

**Baseline metric:** [Retention / Expansion / New Logo / Cost-to-Serve]
**Target segment:** [ICP segment — cite source if from ICP file]
**Time horizon:** [Q / Year / 3-year]

### Conservative Case
- Adoption assumption: [X%] — reason: [...]
- Affected accounts: [N accounts × $Y ARR/account]
- ARR mechanism: [retention / expansion / new logo]
- **Estimated ARR impact: $Z**

### Expected Case
- Adoption assumption: [X%] — reason: [...]
- Affected accounts: [N accounts × $Y ARR/account]
- **Estimated ARR impact: $Z**

### Upside Case
- Adoption assumption: [X%] — reason: [...]
- Affected accounts: [N accounts × $Y ARR/account]
- **Estimated ARR impact: $Z**

### Cost-to-Serve Impact (if relevant)
- Support ticket reduction: [estimated %] — [reasoning]
- CS capacity freed: [estimated hours/accounts]
- Engineering maintenance: [complexity added vs. removed]

### Key Assumptions
1. [Most important assumption — label confidence: High / Medium / Low]
2. [Second assumption]
3. [Third assumption]

**⚠️ PM estimate — not Finance-validated. Present as hypothesis, not projection.**

**Payback horizon:** [If cost-to-build is known: at Expected case, payback in X months]
```

After presenting the model, offer:
> "Want to run `--mode tradeoff` to check how Finance and Sales will react to this estimate?"

---

### Step 2 (Tradeoff Mode): Cross-Functional Constraint Map

**Goal:** Map every function's likely reaction before you walk into an alignment conversation — so you're designing the path through friction, not discovering it in the room.

**For each function** (CS, Sales, Finance, Legal, Engineering), apply the incentive map from the `business-reasoning` skill:

```markdown
## Cross-Functional Constraint Map: [Feature/Initiative] — [Date]

**Decision being evaluated:** [One sentence — what is being decided]

### Customer Success
**What they measure:** NPS, renewal rate, feature adoption, CS escalations
**How this affects them:** [Specific impact — positive or negative]
**Their likely ask:** [What they'll want — enablement materials, rollout plan, migration path, etc.]
**How to pre-empt:** [What to include in the spec/rollout plan that addresses their concern proactively]
**Authority level:** Strong influence (will create friction if not aligned)

### Sales
**What they measure:** ARR, deal velocity, win rate, competitive position
**How this affects them:** [Specific impact]
**Their likely ask:** [Demo assets, battlecard, positioning vs. competitors, etc.]
**How to pre-empt:** [...]
**Authority level:** Strong influence

### Finance
**What they measure:** Gross margin, ARR growth rate, CAC payback
**How this affects them:** [Cost-to-build, expected ARR return, timeline to impact]
**Their likely ask:** [ROI model, investment timeline, cost-to-build estimate]
**How to pre-empt:** [Bring the model; label assumptions; show the payback horizon]
**Authority level:** Veto (resource allocation above budget threshold)

### Legal / Compliance
**How this affects them:** [Flag only if relevant — data handling, privacy, contracts]
**Their likely ask:** [Data flow doc, privacy review, legal review]
**Authority level:** Veto (data handling, regulatory compliance)
**Flag:** [Skip if no legal/compliance surface area — note explicitly "No legal surface area identified"]

### Engineering
**What they measure:** Delivery velocity, tech debt ratio, system reliability
**How this affects them:** [Scope, architectural decisions, complexity added vs. removed]
**Their likely ask:** [Non-goals, acceptance criteria, priority stack within feature]
**How to pre-empt:** [Clear non-goals in spec; specify what's out of scope explicitly]
**Authority level:** Veto (feasibility — can block architectural decisions)

---

### Hardest Objection to Pre-Empt
**Function:** [Which function will push back hardest]
**Objection:** "[Specific objection in their language]"
**Your response:** [How to address it — with data, design choices, or pre-built plan]

### Minimum Viable Alignment Path
1. [Who to talk to first and why — veto holders before friction creators]
2. [Second conversation]
3. [Who to inform, not ask]
```

---

### Step 3 (Perspective Mode): Single-Function Deep Dive

**Goal:** Inhabit one function's mental model — understand their incentives, fears, and how to speak their language.

**Trigger**: Applies when PM says things like "how does CS think about this", "what will Finance say", "how do I get Sales aligned."

**Input parsing**: Extract the named function from the request. If not clear, ask: "Which function's perspective do you need — CS, Sales, Finance, Legal, or Engineering?"

**Output structure**:

```markdown
## Function Perspective: [Function] on [Feature/Initiative] — [Date]

### Their Mental Model
[How this function views the world — what success looks like to them, what keeps them up at night]

### What They Care About Here
[Specific to this feature/initiative — not generic; explain why it hits their metrics or fears]

### What They'll Approve vs. Resist
**Likely to approve if:** [Conditions that make them say yes]
**Likely to resist if:** [Conditions that trigger pushback]

### How to Frame It in Their Language
**Don't say:** "[PM language that won't land]"
**Do say:** "[Their language — metrics they own, outcomes they're rewarded for]"

### Their Most Likely Ask
[The specific thing they'll request before giving alignment — materials, review, timeline, data]

### How to Pre-Empt Their Concern
[Proactive design choice or PRD element that addresses their objection before they raise it]
```

---

### Step 4 (Review Mode): Business Case Section Audit or Generation

**Goal:** Ensure every full PRD has a genuine Business Case section — not just strategic rationale, but a testable hypothesis with go/no-go criteria.

**Input**: Spec path at `<path>` (e.g., `/biz-case --mode review 📦 Products/AgilePlace/specs/bulk-ops.md`)

**If path provided**: Read the spec, check for Business Case section.
- If found: Audit against the 6-element standard. Flag any missing elements.
- If missing: Offer to generate inline.

**If no path provided**: Generate a Business Case section template for the named feature/initiative, ready to paste into a spec.

**Standard 6-element Business Case structure** (from `business-reasoning` skill):

```markdown
## Business Case

**Strategic rationale:** [1-2 sentences — why this aligns with your product's current direction. Cite Q1 OKRs or product strategy if applicable. This is context, not the case itself.]

**Revenue impact hypothesis:** [How this moves ARR or reduces churn — label as PM estimate; specify mechanism: new logo | expansion | retention]
- Conservative case: [X% adoption × Y accounts × Z ARR/account = $ARR impact]
- Expected case: [same structure]

**Customer segment:** [Which ICP segment benefits most; cite persona file if available; rough size of addressable segment]

**Cost-to-build estimate:** [Rough order of magnitude — Small (<1 sprint) | Medium (1-3 sprints) | Large (>3 sprints) — PM estimate, requires engineering validation]

**Opportunity cost:** [What we are NOT doing to build this — name the competing initiative explicitly. If unknown, say so.]

**Go/no-go criteria:** [Specific, observable threshold that would change the recommendation — "if adoption <20% in 90 days, reassess" or "if CS enablement requires >40 hours, scope down"]
```

**Audit checklist** (when reviewing an existing spec):
- [ ] Strategic rationale present and cites current direction (not just "customers want this")
- [ ] Revenue impact has a mechanism (new logo / expansion / retention) — not just "this will grow ARR"
- [ ] Customer segment named with specificity — not "enterprise customers"
- [ ] Cost-to-build has an estimate (even rough) — not absent
- [ ] Opportunity cost explicitly named — not "other projects"
- [ ] Go/no-go criteria is observable and specific — not "if it doesn't work, we'll revisit"

After audit, offer:
> "Want me to fill in any missing elements? Confirm which sections to generate and I'll draft them inline."

If confirmed: draft only the missing sections, present them for review before appending.

---

## Key Constraints

- **All financial estimates must be labeled as PM estimates** — never present modeled numbers as Finance-validated without explicit confirmation
- **Perspective mode is about understanding reasoning**, not characterizing functions as obstacles — frame functionally, not as adversaries
- **No precision theater** — a rough estimate with labeled assumptions is more useful than a false-precision spreadsheet model. Three buckets (conservative/expected/upside) are better than a 40-row model.
- **Business Case sections in PRDs must include go/no-go criteria** — otherwise they're strategic rationale statements, not business cases
- **Never assume what other functions care about** without grounding in Company-specific context — check `📚 Knowledge/People/[name].md` files for actual stakeholder context before making claims about specific individuals

---

## Anti-Patterns to Avoid

**Retrofitting the business case** — writing it after the PRD is "done" to justify a decision already made. Business Case sections written post-hoc defend rather than analyze.

**Precision theater** — detailed spreadsheet models with invented numbers presented as projections. Label everything as PM estimates. Three rough cases with named assumptions beat false precision.

**Treating all functions as veto holders** — not every function has veto power. Mapping authority correctly (veto / strong influence / advisory) prevents over-engineering alignment.

**Skipping opportunity cost** — "we should do this" without naming what you're not doing. Every yes is a no somewhere else. If you can't name it, you haven't done the business reasoning.

**Generic go/no-go criteria** — "we'll reassess if adoption is low" is not a criterion. "If adoption is <20% in 90 days across ICP accounts, we reassess scope" is a criterion.

---

## Integration Points

**Entry from:**
- `/think` — when strategic analysis surfaces a decision with financial or cross-functional implications
- `/spec --type full` — Business Case section requirement triggers `--mode review`
- `/discover` — when initiative needs a business case before getting prioritized
- Any product decision with cross-functional dependencies

**Exit to:**
- `/spec` — Business Case section generated here feeds into full PRD
- `/decide` — financial and cross-functional reasoning feeds decision journal entries
- `/align` — constraint maps from `--mode tradeoff` feed stakeholder alignment sessions
- `📚 Knowledge/People/[name].md` — perspective mode insights about specific stakeholders worth capturing
