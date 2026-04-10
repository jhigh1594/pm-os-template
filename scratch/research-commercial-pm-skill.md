# Research: Commercial PM Skill

> Research artifact to inform design of the `commercial-lens` skill. Written 2026-04-07.

---

## Core Thesis

A commercial PM is not the person who writes the business case at the end of discovery. They are the person who applies commercial filters at the beginning — before a team invests discovery time, engineering cycles, or stakeholder capital on a bet that will never generate revenue.

The distinction from `business-reasoning`:
- `business-reasoning` activates **after** a bet is identified: it quantifies ARR pathways, maps cross-functional reactions, and structures the business case section of a PRD.
- `commercial-lens` activates **during** opportunity assessment: it filters whether the bet is even worth structuring into a business case.

Leah Tharin frames it precisely: commercial PMs think about "what the market expects" and "what we need to do to compete" — not "what customers are asking for." They think from the outside in, not the inside out. The commercial lens is a market-viability gate that runs in parallel to desirability and feasibility, not sequentially after them.

The key insight from practitioners (Tharin, Ramp's Geoff Charles, First Round's pricing frameworks): **the commercial lens is a first-class decision input, not a downstream approval step**. PMs who treat commercial thinking as "something Finance reviews later" are implicitly delegating product strategy to Finance.

---

## Key Mental Models

### 1. The Three-Bucket Revenue Map
Every opportunity must map to at least one of three revenue mechanisms before it earns discovery investment:
- **New logo enablement** — removes a blocker that prevents prospects from signing; absence costs deals
- **Expansion** — enables seat growth, tier upgrade, usage-based growth, or cross-sell; drives NRR above 100%
- **Retention moat** — reduces churn by addressing something customers would leave over; protects GRR

If an opportunity cannot be mapped clearly to one of these, it is a table-stakes fix or a nice-to-have. That is not disqualifying — but it should be named honestly, not dressed up as ARR-generating.

### 2. Table Stakes vs. Differentiator vs. Deal-Closer
From Leah Tharin's framework:

- **Table stakes**: Minimum to participate in the market. Customers expect it; absence creates churn risk, not presence creates wins. Metrics: 30+ day retention, churn rate, support tickets.
- **Differentiators**: Opinionated capabilities you do better than anyone else. Enable premium positioning and higher LTV. Metrics: competitive win rate on feature-driven deals, NPS, expansion rate.
- **Deal-closers**: Features that appear on procurement scorecards or executive sign-off criteria. Directly affect pipeline velocity and win rate.

The commercial lens asks: **"Which bucket does this opportunity fall in, and how does our current gap in this area affect revenue mechanics today?"**

### 3. Payback Horizon as Bet-Sizing Input
From Aakash Gupta's framework: the payback period tells you when engineering investment recovers. Use it to calibrate scope, not just justify investment.

Key benchmarks for SaaS:
- Feature with clear ARR path: <2 year payback acceptable
- CAC payback (new logo features): 5–12 months healthy; >18 months is a red flag
- Tech debt / table stakes: ~3 years acceptable, justify with churn risk

Formula for commercial opportunities:
```
Payback = Build Cost (eng weeks × cost/week) ÷ Annual Revenue Impact
```

**Application at discovery**: If a rough payback estimate exceeds 36 months, either re-scope dramatically or require stronger evidence of impact before investing in full discovery. The payback horizon is the earliest commercial filter — it does not require a polished business case, just an order-of-magnitude estimate.

### 4. Value Capture Ratio
From monetization research (Simon-Kucher, Monetizely, First Round): healthy B2B SaaS captures 10–20% of quantifiable customer value as annual software spend.

**PM application**: Estimate customer outcome value before estimating price. If you cannot estimate the outcome value, you do not yet understand the opportunity well enough to assess commercial viability.

Example: "This feature saves 3 hours/week for 2 analysts per account. At $80k loaded cost, that's ~$25k/year in recoverable value. Capturing 15% = $3,750/account/year. At 200 accounts at risk, max expansion pool = ~$750k ARR."

This is rough. It is supposed to be rough. The point is to size the ceiling before investing in precision.

### 5. Pricing Signal Reading
From PMGuru's B2B pricing playbook: commercial PMs read pricing signals in sales behavior, not in Finance reports.

Signals that pricing power exists (or is being left on the table):
- Win rates feel "too easy" — almost no procurement friction
- Buyers describe the product as a "great deal" unprompted
- Pricing isn't a topic in QBRs or renewal conversations
- Competitors are priced higher on comparable features

Signals that commercial viability is weak:
- Feature requests come exclusively from existing customers, never from prospects
- Sales cannot use the feature in a deal narrative
- The feature is "nice to have" in every customer conversation — never "deal-breaker"
- No customer has ever tried to negotiate for it or around it

### 6. NRR Decomposition as Opportunity Lens
From IdeaPlan's NRR framework:
```
NRR = (100% - Logo Churn %) × (100% + Net Expansion %)
```

This decomposition tells you whether an opportunity should be classified as a **retention play** (address logo churn) or an **expansion play** (increase net expansion rate). They require different mechanisms, different stakeholder alignment, and different time horizons.

Expansion levers to assess for each opportunity:
1. Seat expansion (team growth model)
2. Feature upsells (tiering model)
3. Usage-based expansion (consumption model)
4. Add-on cross-sell (multi-product model)

**Application**: Before advancing an opportunity, ask which NRR lever it activates. If the answer is "none directly," classify it as table stakes (necessary for GRR, not NRR).

### 7. The SaaS Economics Inversion for AI Products
From IdeaPlan's AI Unit Economics framework: traditional SaaS approaches near-zero marginal cost per user. AI products face the inverse — costs scale linearly without active optimization.

**PM implication**: For AI opportunities, commercial viability assessment must include:
- Cost-per-query at 10x and 100x current scale
- Gross margin trajectory (healthy AI: 60–70%; below 60% requires structural fix)
- Pricing alignment with consumption (unlimited plans are economically toxic for AI)

This is especially relevant for Jon's AI customer success platform at ServiceNow.

### 8. The Reliability > Optimism Rule (Tharin)
Commercial PMs build credibility by forecasting conservatively and delivering reliably, not by promising aggressively and falling short. This applies directly to commercial assessments: **label your confidence, not just your estimate**.

Every commercial filter output should include:
- The revenue mechanism (clear / plausible / speculative)
- The weakest assumption in the chain
- What evidence would move the estimate materially

---

## What's Currently Missing from the Workspace

`business-reasoning` covers:
- ARR impact pathways (new logo / expansion / retention)
- Cost-to-serve impact
- Cross-functional incentive maps
- Business case section template with go/no-go criteria
- Financial reasoning quality gate

**Gaps that `commercial-lens` should fill:**

1. **Pre-discovery filter** — `business-reasoning` assumes you've already decided to pursue something. `commercial-lens` is the earlier gate: "should we even spend discovery effort here?"

2. **Revenue mechanism typing before quantification** — `business-reasoning` jumps to quantification; `commercial-lens` first establishes *which mechanism* and *whether the mechanism plausibly exists* before attempting numbers.

3. **Pricing signal reading** — no existing skill teaches PMs to read commercial viability signals in sales behavior (win rates, procurement friction, deal narratives). This is entirely absent.

4. **Payback horizon as bet-sizing input** — `business-reasoning` has a business case template but no explicit framework for using payback period to scope discovery investment.

5. **Value capture ratio** — no existing skill frames the customer outcome value → pricing power → ARR ceiling sequence that should precede any quantified business case.

6. **Table stakes vs. differentiator vs. deal-closer classification** — this tripartite lens (from Tharin) does not exist anywhere in the current skill set. It is essential for commercial opportunity typing.

7. **AI-specific unit economics** — no skill covers the cost-per-inference, gross margin trajectory, or consumption-aligned pricing considerations that apply specifically to AI product opportunities.

8. **NRR decomposition as discovery lens** — `business-reasoning` mentions expansion signal, but does not give PMs the NRR decomposition model for classifying whether an opportunity is a retention play vs. expansion play.

---

## Skill Design Recommendations

### When This Skill Activates

Trigger conditions (in order of priority):
- PM is assessing a new opportunity: "should we pursue this?"
- PM is scoping a discovery sprint and wants to prioritize which bets to explore
- PM is reviewing a request from Sales ("can we build X to close a deal?")
- PM is preparing for roadmap prioritization and needs to rank commercial potential
- Trigger phrases: "is this worth building", "does this close deals", "what's the commercial case for", "will this affect renewal", "is this revenue-generating", "should we even pursue", "commercial viability", "deal economics", "does this pencil out"

**Do NOT activate for:**
- Writing a full business case (that is `business-reasoning`)
- Pricing model design (that is `pricing-intelligence`)
- Stakeholder alignment strategy (that is `stakeholder-craft`)

### What It Produces

A **Commercial Viability Assessment** — not a business case. Think of it as a structured pre-read that answers: "Is this commercially viable enough to invest discovery effort in?"

Output format:

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

### Key Questions It Asks During Discovery/Opportunity Assessment

**Revenue mechanism questions:**
1. Which of the three revenue buckets does this fall in — and what evidence supports that classification?
2. Has Sales ever lost a deal because this didn't exist? (New logo signal)
3. Has CS ever flagged this as a churn risk? (Retention signal)
4. Would building this enable a natural upsell conversation or seat expansion? (Expansion signal)

**Pricing signal questions:**
5. Do prospects ask for this during the sales process, or only existing customers?
6. Has any buyer tried to negotiate around this — or negotiate to get it included?
7. Could this feature support a pricing tier differentiation?
8. What's the estimated customer outcome value in dollars? At 10–20% capture, what's the implied price?

**Bet-sizing questions:**
9. What's the rough build cost (eng weeks × average loaded cost)?
10. What's the estimated ARR impact ceiling — conservative and expected?
11. At those numbers, what's the payback horizon?
12. If payback exceeds 24 months, what would need to be true to justify that?

**Commercial viability questions (AI products):**
13. What are the per-use inference costs at 10x and 100x scale?
14. Does the pricing model align with consumption patterns?
15. Can we achieve 60%+ gross margins at expected scale?

**Go/no-go framing question:**
16. If we invest a full discovery sprint in this and confirm all our assumptions — would the commercial case support a roadmap commitment? If the honest answer is "probably not," discovery is premature.

### Relationship to Existing Skills

```
commercial-lens          →   business-reasoning
(should we explore it?)      (build the case for it)
        ↓                              ↓
   discovery                    full PRD spec
(how do we validate it?)    (how do we ship it)
```

`commercial-lens` outputs a go/no-go that either:
- Releases to `discovery` (pursue, here's the riskiest assumption)
- Escalates to `business-reasoning` (strong signal, proceed to full case)
- Returns a "not yet" with a specific evidence request
- Returns a "no" with a clear commercial rationale

---

## Raw Insights from Lenny QMD

The QMD index (1,524 documents, pm-frameworks and products collections) returned **no matches** for commercial PM, deal economics, revenue thinking, value capture, or payback horizon queries. All four queries returned empty results.

**Interpretation**: This confirms the gap. Commercial thinking as a first-class PM lens is entirely absent from the indexed transcript corpus — meaning it is also absent from the current workspace knowledge base. This is not a search failure; it is evidence that this lens has not been systematically documented or applied in this workspace previously.

What the QMD corpus does contain (from adjacent queries):
- `business-reasoning` skill patterns (financial model after the fact)
- Prioritization frameworks (RICE, value vs. effort)
- Discovery methodologies (Teresa Torres OST, assumption testing)

None of these apply commercial thinking as a pre-discovery filter. They treat commercial viability as an output of discovery, not an input to it.

**Lenny-adjacent signal from web search:**
- Ramp (via Lenny): "A product strategy not anchored on the reality of how the company makes money will not survive." — Geoff Charles, VP Product. Ramp forces teams to understand monetization approaches and tradeoffs between innovation, monetization, and growth as part of planning — not as a post-hoc Finance review.
- Enterprise sales framing (Lenny / Jen Abel): "Sell the alpha, not the feature" — commercial PMs understand that sales can work with a direction, not just a finished product. This implies PMs should know which opportunities have deal-closable narratives early, not just when the feature ships.

---

## Sources

1. **Leah Tharin** — "How to be a commercial PM" (Substack, leahtharin.com)
   - Table stakes / differentiator / deal-closer framework
   - Impact-to-cost matrix
   - Reliability > optimism principle
   - Three diagnostic questions for market expectation

2. **Aakash Gupta** — "Payback Period: The PM's Framework for Making Faster, Smarter Investment Decisions" (aakashg.com, 2026-02-28)
   - Simple / discounted / CAC payback formulas
   - SaaS benchmark thresholds (5–12 months healthy CAC payback)
   - Decision framework: 4-step evaluation

3. **Dee Sahni / First Round Capital** — "Don't Let Growth Hurt Your Margins: A 4-Step Pricing Framework" (review.firstround.com)
   - Segment-by-impact framework
   - Willingness-to-pay + JTBD + demographics + behaviors pricing model
   - Unit economics degradation at scale

4. **IdeaPlan (Tim Adair)** — "Expansion Revenue & NRR Playbook" and "AI Unit Economics Framework" (ideaplan.io)
   - NRR decomposition model
   - Expansion lever taxonomy (seat / feature / usage / add-on)
   - AI gross margin benchmarks and cost scaling dynamics

5. **PMGuru** — "B2B Pricing Playbook" (pmguru.org, 2026-02-25)
   - Win rate friction as underpricing signal
   - Value capture ratio (10–20% of quantified value)
   - Diagnostic questions for commercial viability

6. **Monetizely** — "Pricing for Customer Value Creation" (getmonetizely.com)
   - Value discovery → modeling → validation → communication framework
   - Segmentation by value perception

7. **Geoff Charles / Ramp (via Lenny's Newsletter)** — "How Ramp Builds Product" (lennysnewsletter.com)
   - Revenue mechanism integration in product planning
   - Business outcome organization (teams oriented around explicit financial goals)
   - OKR discipline as commercial filter

8. **QMD Workspace Search** — pm-frameworks and products collections (1,524 docs)
   - Zero matches on commercial PM lens queries — gap confirmed
