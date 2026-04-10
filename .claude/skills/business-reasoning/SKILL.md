---
name: business-reasoning
description: Use when making product decisions that have financial impact, cross-functional tradeoffs, or business constraint implications. Triggers: unit economics, ARR impact, business case, how does sales think about this, cost-to-serve, revenue model, margin tradeoffs, cross-functional alignment, what does CS think, what does finance care about, what does legal care about, business justification, business case section.
---

# Business Reasoning

Apply financial and organizational reasoning to product decisions — so business constraints inform what we build, not just constrain it after the fact.

## When This Skill Activates

Use this skill when:
- PM is building a business case for a product investment
- PM is reasoning about revenue or cost implications of a decision
- PM needs to understand how CS, Sales, Finance, or Legal will react to a product decision
- PM is preparing for a budget or resource allocation ask
- PM is writing the Business Case section of a full PRD
- PM needs to quantify the tradeoffs between competing options

## Default Stance: Financial Clarity Mode

Label all estimates clearly as PM estimates. Ground financial reasoning in what's observable in the workspace (ICP file, product-context, revenue data in GOALS.md) before modeling. Never present financial models as Finance-validated without explicit confirmation.

## Core Frameworks

### 1. B2B SaaS Unit Economics Model

When estimating revenue or cost impact, use this layered model:

**Revenue Impact Pathway**:
```
Feature → Adoption rate (% of ICP accounts using it) [Confidence: ?%]
  → Affected account segment (new logo / expansion / retention) [Confidence: ?%]
  → ARR mechanism: which of these does it drive? [Confidence: ?%]
    - New logo enablement: feature closes deals by removing a blocker
    - Expansion: feature enables seat expansion or tier upgrade
    - Retention: feature reduces churn by addressing a retention risk
  → ARR impact = (affected accounts) × (ARR per account) × (adoption rate) [Combined confidence: ?%]
```
Label confidence at each step before multiplying. A 70% × 70% × 70% chain produces ~34% confidence in the output, not 70%. Own that math.

**Cost-to-Serve Impact**:
```
Feature → Support ticket reduction (fewer "how do I?" questions)
  → Onboarding time reduction (faster time-to-value)
  → CS capacity freed (fewer manual touchpoints required)
  → Engineering maintenance cost (complexity added vs. removed)
```

**Churn/Retention Calculus**:
- Feature as retention moat: customers who use it renew at higher rates → reduces GRR risk
- Feature as table stakes: customers expect it; absence actively drives churn
- Feature as NPS driver: high satisfaction feature → reduces renewal friction

**Expansion Signal**:
- Does this feature create a natural expansion upsell moment? (e.g., seat-based limits reached, usage-based pricing trigger)
- Does serving this feature at scale require a packaging/pricing change?

---

### 2. Cross-Functional Incentive Map (Product Context)

Each function has distinct metrics, fears, and ask patterns. Knowing their incentive structure lets the PM pre-empt objections:

| Function | What They Measure | What They Fear | What They'll Ask For |
|----------|-------------------|----------------|---------------------|
| **Customer Success** | NPS, renewal rate, feature adoption, CS escalations | Features requiring heavy onboarding without enablement; changes that break existing workflows; features that create more support surface without CS capacity | Enablement materials, clear rollout plan, migration path for existing customers |
| **Sales** | ARR, deal velocity, win rate, competitive position | Gaps that lose deals, pricing complexity ("I can't explain this"), promises the product can't keep | Demo assets, battlecard update, clear positioning vs. key competitors |
| **Finance** | Gross margin, ARR growth rate, CAC payback period | Cost-to-serve creep from engineering complexity, investment without clear ARR path, delayed revenue recognition | ROI model, timeline to ARR impact, cost-to-build vs. expected return |
| **Legal / Compliance** | Risk exposure, regulatory compliance, contract adherence | Data handling changes affecting privacy/compliance posture, contractual implications, security posture changes | Data flow documentation, privacy review, legal review of user agreements |
| **Engineering** | Delivery velocity, technical debt ratio, system reliability | Scope changes mid-sprint, architectural decisions that create long-term debt, unclear requirements that require rework | Clear non-goals, acceptance criteria, priority stack-ranking within the feature |

---

### 3. Business Constraint Reasoning Framework

Not every function has veto power — map authority correctly before designing your alignment strategy:

**Veto Power** (decision can be blocked without their approval):
- Finance: resource allocation above a budget threshold
- Legal: anything touching data handling, privacy, or contract terms
- Engineering: feasibility decisions on technical architecture

**Strong Influence** (won't veto but can create significant friction):
- CS: feature rollout timing and customer impact radius
- Sales: positioning and messaging in market-facing materials

**Advisory** (inform but not block):
- Marketing: naming, messaging, launch timing
- Support: documentation and help content

**Minimum Viable Alignment Pattern**:
1. Identify veto holders — get their input early (before you're committed)
2. Identify friction creators — address their concerns in the PRD proactively
3. Identify advisory stakeholders — inform, don't ask for approval

---

### 4. Business Case Section Template

Standard 6-element structure for PRD Business Case sections:

```markdown
## Business Case

**Strategic rationale:** [1-2 sentences — why this aligns with your product's current direction; cite your product strategy if applicable]

**Revenue impact hypothesis (stated as a bet):**
- We believe [X behavior] will happen in [Y accounts] within [Z months].
- Confidence: [%] — based on [evidence type: interview/data/analogy/assumption]
- What would change this estimate: [specific new information]
- Conservative case: [X% adoption × Y accounts × Z ARR/account = $ARR impact]
- Expected case: [same structure]

**Customer segment:** [Which ICP segment benefits most; cite persona file; rough size of addressable segment]

**Cost-to-build estimate:** [Rough order of magnitude — small (<1 sprint), medium (1-3 sprints), large (>3 sprints) — PM estimate, requires engineering validation]

**Opportunity cost:** [What we are NOT doing to build this — name the competing initiative explicitly]

**Go/no-go criteria:** [Specific, observable threshold that would change the recommendation — e.g., "if adoption <20% in 90 days, reassess" or "if CS enablement requires >40 hours, scope down"]

Frame criteria as bets, not metrics: "We believe adoption will reach 20% in 90 days. If it doesn't, the assumption about [X] was wrong — stop or pivot. If it does, update confidence and increase investment."
```

---
## 🎯 Quality Gate: Financial Reasoning

After producing the business case output above, include this gate before closing:

**Before we lock this in:**

> "First: state your confidence (0-100%) in the value mechanism you're about to trace. Then trace it. If your confidence in the full chain is below 40%, this is a hypothesis requiring a discovery phase, not a business case."

> "Trace the financial logic explicitly: this feature/decision → what customer behavior changes → what metric moves → what revenue or cost impact follows → over what time horizon → at what confidence. At which step is your confidence lowest, and what would increase it? If you can't trace it, you have a feature, not an investment."

_(This is the reasoning step that separates a business case from a strategic rationale statement. The weakest link in the value mechanism chain is what Finance will challenge first.)_

**Auto-saving to** `📚 Knowledge/Growth/growth-signals-[YYYY-MM].md` — append this entry now. No prompt needed.

---

## Response Contract

When this skill activates for financial reasoning:

```markdown
## Business Analysis: [Initiative/Decision]

**Mechanism:** [How this creates/protects/destroys business value]

**Revenue impact estimate (PM model — not Finance-validated):**
- Conservative: [estimate + key assumption]
- Expected: [estimate + key assumption]

**Cross-functional implications:**
- CS: [impact + likely ask]
- Sales: [impact + likely ask]
- Finance: [impact + likely ask]
- Legal: [flag if relevant]

**Hardest objection to pre-empt:** [Most likely pushback + your response]

**Recommended action:** [What to do before taking this to stakeholders]
```

---

## Guardrails

- **Label all financial estimates** as PM model estimates requiring Finance validation — never present modeled numbers as validated data
- Do not compound uncertain estimates without flagging the probability degradation — a chain of assumptions multiplies uncertainty, it doesn't average it.
- **Never assume what other functions care about** without grounding in your product context (check stakeholder docs for actual stakeholder context)
- **Cross-functional perspective is about understanding reasoning**, not characterizing functions as obstacles
- **No precision theater** — a rough estimate with labeled assumptions is more useful than a false-precision spreadsheet model
- **Business Case sections in PRDs must include go/no-go criteria** — otherwise they're strategic rationale statements, not business cases

## Integration

- Use `/biz-case` command to run structured business case analysis (model, tradeoff, perspective, or review modes)
- Business Case section generated here feeds `/spec --type full` PRDs
- Financial reasoning from `--mode model` informs `/decide` decision journal entries
- Cross-functional constraint maps from `--mode tradeoff` feed `/align` stakeholder alignment sessions

## Self-Learning

Before responding, read `LEARNED.md` in this skill directory when it exists and treat it as compact runtime guidance that sharpens this skill.

Rules for self-improvement:
- Keep `SKILL.md` human-owned; do not rewrite it directly from normal usage.
- Only promote specific, reusable, evidence-backed lessons into `LEARNED.md`.
