---
name: commercial-lens
description: Use when assessing whether a new opportunity is commercially viable before investing discovery effort. Triggers: "is this worth building", "does this close deals", "what's the commercial case for", "will this affect renewal", "is this revenue-generating", "should we even pursue", "commercial viability", "deal economics", "does this pencil out", "payback", "value capture", "is this a differentiator".
---

# Commercial Lens

A commercial PM is not the person who writes the business case at the end of discovery. They are the person who applies commercial filters at the beginning — before a team invests discovery time, engineering cycles, or stakeholder capital on a bet that will never generate revenue.

The distinction from `business-reasoning`:
- `business-reasoning` activates **after** a bet is identified: it quantifies ARR pathways, maps cross-functional reactions, and structures the business case section of a PRD.
- `commercial-lens` activates **during** opportunity assessment: it filters whether the bet is even worth structuring into a business case.

The commercial lens is a market-viability gate that runs **in parallel** to desirability and feasibility — not sequentially after them. PMs who treat commercial thinking as "something Finance reviews later" are delegating product strategy to Finance.

---

## When This Skill Activates

**Trigger conditions (in priority order):**
- PM is assessing a new opportunity: "should we pursue this?"
- PM is scoping a discovery sprint and wants to prioritize which bets to explore
- PM is reviewing a request from Sales ("can we build X to close a deal?")
- PM is preparing for roadmap prioritization and needs to rank commercial potential
- Trigger phrases: "is this worth building", "does this close deals", "what's the commercial case for", "will this affect renewal", "is this revenue-generating", "should we even pursue", "commercial viability", "deal economics", "does this pencil out"

**Do NOT activate for:**
- Writing a full business case → use `business-reasoning`
- Pricing model design → use `pricing-intelligence`
- Stakeholder alignment strategy → use `stakeholder-craft`

---

## Default Stance: Consultative First

In chat, clarify the opportunity and its current stage before running the full commercial filter.

### Context-Gathering Phase (Required Before Action)

1. Ask the user one question at a time; wait for the answer before asking the next.
2. Cap at 3 questions for the initial context-gathering phase.
3. If the user has already provided sufficient context, ask at most 1–2 questions or proceed directly.
4. Once context is gathered, proceed to the Commercial Viability Assessment.

Default flow:
1. gather context
2. classify the opportunity type (Three-Bucket Revenue Map + Tharin tripartite)
3. run the payback horizon estimate (rough order of magnitude only)
4. check value capture ratio
5. surface pricing signals
6. produce go/no-go signal with the weakest assumption named

---

## Core Mental Models

### 1. The Three-Bucket Revenue Map

Every opportunity must map to at least one of three revenue mechanisms before it earns discovery investment:

- **New logo enablement** — removes a blocker that prevents prospects from signing; absence costs deals
- **Expansion** — enables seat growth, tier upgrade, usage-based growth, or cross-sell; drives NRR above 100%
- **Retention moat** — reduces churn by addressing something customers would leave over; protects GRR

If an opportunity cannot be mapped clearly to one of these, it is a table-stakes fix or a nice-to-have. That is not disqualifying — but name it honestly rather than dressing it up as ARR-generating.

---

### 2. Table Stakes vs. Differentiator vs. Deal-Closer (Tharin)

- **Table stakes**: Minimum to participate in the market. Customers expect it; absence creates churn risk, not presence creates wins. Metrics: 30+ day retention, churn rate, support tickets.
- **Differentiators**: Opinionated capabilities you do better than anyone else. Enable premium positioning and higher LTV. Metrics: competitive win rate on feature-driven deals, NPS, expansion rate.
- **Deal-closers**: Features that appear on procurement scorecards or executive sign-off criteria. Directly affect pipeline velocity and win rate.

**The commercial lens asks:** "Which bucket does this opportunity fall in, and how does our current gap in this area affect revenue mechanics today?"

---

### 3. Payback Horizon as Bet-Sizing Input (Aakash Gupta)

The payback period tells you when engineering investment recovers. Use it to calibrate scope, not just justify investment.

```
Payback = Build Cost (eng weeks × cost/week) ÷ Annual Revenue Impact
```

**SaaS benchmarks:**
- Feature with clear ARR path: <2 year payback acceptable
- CAC payback (new logo features): 5–12 months healthy; >18 months is a red flag
- Tech debt / table stakes: ~3 years acceptable, justify with churn risk

**Application at discovery:** If a rough payback estimate exceeds 36 months, either re-scope dramatically or require stronger evidence of impact before investing in full discovery. Payback horizon is the earliest commercial filter — it does not require a polished business case, just an order-of-magnitude estimate.

---

### 4. Value Capture Ratio

Healthy B2B SaaS captures 10–20% of quantifiable customer value as annual software spend.

**PM application:** Estimate customer outcome value before estimating price. If you cannot estimate the outcome value, you do not yet understand the opportunity well enough to assess commercial viability.

**Example:**
> "This feature saves 3 hours/week for 2 analysts per account. At $80k loaded cost, that's ~$25k/year in recoverable value. Capturing 15% = $3,750/account/year. At 200 accounts at risk, max expansion pool = ~$750k ARR."

This is rough. It is supposed to be rough. The point is to size the ceiling before investing in precision.

---

### 5. Pricing Signal Reading

Commercial PMs read pricing signals in sales behavior, not Finance reports.

**Signals that pricing power exists (or is being left on the table):**
- Win rates feel "too easy" — almost no procurement friction
- Buyers describe the product as a "great deal" unprompted
- Pricing isn't a topic in QBRs or renewal conversations
- Competitors are priced higher on comparable features

**Signals that commercial viability is weak:**
- Feature requests come exclusively from existing customers, never from prospects
- Sales cannot use the feature in a deal narrative
- The feature is "nice to have" in every customer conversation — never "deal-breaker"
- No customer has ever tried to negotiate for it or around it

---

### 6. NRR Decomposition as Opportunity Lens

```
NRR = (100% - Logo Churn %) × (100% + Net Expansion %)
```

This decomposition tells you whether an opportunity is a **retention play** (address logo churn) or an **expansion play** (increase net expansion rate). They require different mechanisms, different stakeholder alignment, and different time horizons.

**Expansion levers to assess for each opportunity:**
1. Seat expansion (team growth model)
2. Feature upsells (tiering model)
3. Usage-based expansion (consumption model)
4. Add-on cross-sell (multi-product model)

**Application:** Before advancing an opportunity, ask which NRR lever it activates. If the answer is "none directly," classify it as table stakes (necessary for GRR, not NRR).

---

### 7. The SaaS Economics Inversion for AI Products

Traditional SaaS approaches near-zero marginal cost per user. AI products face the inverse — costs scale linearly without active optimization.

**PM implication for AI opportunities:** Commercial viability assessment must include:
- Cost-per-query at 10x and 100x current scale
- Gross margin trajectory (healthy AI: 60–70%; below 60% requires structural fix)
- Pricing alignment with consumption (unlimited plans are economically toxic for AI)

This is especially relevant for AI customer success and AI feature development. The question "can we achieve 60%+ gross margin at expected scale?" is a first-class commercial filter for any AI feature opportunity.

---

### 8. The Reliability > Optimism Rule (Tharin)

Commercial PMs build credibility by forecasting conservatively and delivering reliably, not by promising aggressively and falling short.

Every commercial filter output should include:
- The revenue mechanism (clear / plausible / speculative)
- The weakest assumption in the chain
- What evidence would move the estimate materially

---

## Response Contract

Produce a **Commercial Viability Assessment** — not a business case. This answers: "Is this commercially viable enough to invest discovery effort in?"

```markdown
## Commercial Viability Assessment: [Opportunity]

**Revenue mechanism:** [New logo / Expansion / Retention / Table stakes / Unclear]
**Revenue mechanism confidence:** [Clear (evidence) / Plausible (reasoning) / Speculative (assumption)]

**Opportunity type (Tharin):** [Table stakes / Differentiator / Deal-closer]
**What evidence puts it in this bucket:** [brief]

**Rough payback horizon:**
- Build cost estimate: [S/M/L — weeks of eng]
- ARR ceiling estimate: [rough, labeled as PM estimate]
- Implied payback: [months/years, or "uncalculable — missing X"]

**Value capture check:**
- Customer outcome value estimate: [$X/year per account, rough]
- Implied pricing power at 10-20% capture rate: [$Y/account/year]
- Does this pencil out at current pricing? [Yes / No / Need more data]

**Commercial go/no-go signal:**
- Pursue discovery: [Yes / Yes with constraint / Not yet — needs X / No]
- Weakest assumption: [what would break this]
- What would upgrade confidence: [minimum evidence needed]
```

---

## Key Questions

### Revenue Mechanism Questions
1. Which of the three revenue buckets does this fall in — and what evidence supports that classification?
2. Has Sales ever lost a deal because this didn't exist? (New logo signal)
3. Has CS ever flagged this as a churn risk? (Retention signal)
4. Would building this enable a natural upsell conversation or seat expansion? (Expansion signal)

### Pricing Signal Questions
5. Do prospects ask for this during the sales process, or only existing customers?
6. Has any buyer tried to negotiate around this — or negotiate to get it included?
7. Could this feature support a pricing tier differentiation?
8. What's the estimated customer outcome value in dollars? At 10–20% capture, what's the implied price?

### Bet-Sizing Questions
9. What's the rough build cost (eng weeks × average loaded cost)?
10. What's the estimated ARR impact ceiling — conservative and expected?
11. At those numbers, what's the payback horizon?
12. If payback exceeds 24 months, what would need to be true to justify that?

### Commercial Viability Questions (AI Products)
13. What are the per-use inference costs at 10x and 100x scale?
14. Does the pricing model align with consumption patterns?
15. Can we achieve 60%+ gross margins at expected scale?

### Go/No-Go Framing Question
16. If we invest a full discovery sprint in this and confirm all our assumptions — would the commercial case support a roadmap commitment? If the honest answer is "probably not," discovery is premature.

---

## Relationship to Other Skills

```
commercial-lens          →   business-reasoning
(should we explore it?)      (build the case for it)
        ↓                              ↓
   discovery                    full PRD spec
(how do we validate it?)    (how do we ship it)
```

`commercial-lens` outputs a go/no-go signal that either:
- **Releases to `discovery`** — pursue; here's the riskiest assumption to test first
- **Escalates to `business-reasoning`** — strong signal; proceed to full case
- **Returns "not yet"** — specific evidence needed before discovery makes sense
- **Returns "no"** — clear commercial rationale for passing

---

## Guardrails

- **No precision theater** — a rough payback estimate with labeled assumptions is more useful than a false-precision model. The point is to size the ceiling, not produce a Finance-grade projection.
- **Label revenue mechanism confidence** — "clear (evidence)", "plausible (reasoning)", or "speculative (assumption)". Never present a speculative mechanism as if it were validated.
- **Don't confuse table stakes with differentiators** — table stakes reduce churn risk; differentiators enable growth. They require different investment theses.
- **Don't skip the pricing signal scan** — if Sales can't use it in a deal narrative, it's not a deal-closer regardless of how much customers say they want it.
- **AI cost structure is not SaaS cost structure** — for any AI feature, the gross margin trajectory at scale is a required input, not an afterthought.
- **If you can't estimate customer outcome value, you don't understand the opportunity** — this is the test of whether discovery is ready to proceed.

---

## Self-Learning

Before responding, read `LEARNED.md` in this skill directory when it exists and treat it as compact runtime guidance that sharpens this skill.

Rules for self-improvement:
- Keep `SKILL.md` human-owned; do not rewrite it directly from normal usage.
- Propose broader instruction changes through the central skill-learning review queue.
- Only promote specific, reusable, evidence-backed lessons into `LEARNED.md`.
