# MVP Test Pattern Reference

Use this reference when designing the cheapest valid test in Phase 4 of the MVP coaching process.
Select the pattern that matches the assumption type and the stage of certainty.

---

## Pattern Selection by Assumption Type

| Assumption Type | What You're Testing | Recommended Patterns |
|-----------------|--------------------|-----------------------|
| Value (demand) | Do people want this at all? | Landing page, Pre-sell, Fake door |
| Value (willingness to pay) | Will they pay for it? | Pre-sell, Concierge, Pricing page |
| Value (behavior change) | Will they change how they work? | Concierge, Wizard of Oz, Pilot |
| Usability | Can they figure it out? | Prototype / clickthrough, Guerrilla test |
| Feasibility | Can we build it to the required quality? | Technical spike, Proof of concept |
| Growth (acquisition) | Can we reach them? | Landing page + ad, Waitlist |
| Growth (retention) | Will they come back? | Pilot with single customer, Cohort tracking |

---

## Test Patterns

### 1. Landing Page / Fake Door
**What it is**: A page describing the value proposition of something that doesn't exist yet. Visitors can sign up or "try it."
**Measures**: Conversion rate, email signups, clicks on a CTA that leads nowhere.
**Best for**: Testing demand and messaging before building anything.
**Signal**: >X% conversion = enough demand to proceed.
**Time to build**: Hours to days.
**Limitation**: Measures stated intent, not actual behavior.

---

### 2. Pre-sell
**What it is**: Charging real money (or taking deposits) before the product exists.
**Measures**: Actual willingness to pay, not stated intent.
**Best for**: Testing whether customers will pay, not just whether they're interested.
**Signal**: N paid customers = proceed.
**Time to build**: Days.
**Limitation**: Requires confidence in delivery; sets expectations.

---

### 3. Concierge MVP
**What it is**: Delivering the value manually, as if the product existed, to a small number of real customers.
**Measures**: Whether the outcome solves the problem; customer satisfaction; repeatability.
**Best for**: Testing value when the process is unclear and automation is premature.
**Signal**: Customers are satisfied, return, refer others, or pay.
**Time to build**: Days to weeks (no code required).
**Limitation**: Not scalable by design; tests value, not efficiency.

---

### 4. Wizard of Oz
**What it is**: The product appears automated to users but is powered by humans behind the scenes.
**Measures**: Whether the automated experience delivers value; usability; demand.
**Best for**: When the automated version is expensive to build but the experience can be faked.
**Signal**: Users engage as if it's real; quantifiable value delivered.
**Time to build**: Days to weeks.
**Limitation**: Harder to sustain; operations-intensive.

---

### 5. Clickable Prototype / Mockup Test
**What it is**: A non-functional prototype users navigate as if it were real.
**Measures**: Usability, comprehension, desirability, workflow fit.
**Best for**: Testing whether users understand and can navigate the proposed solution.
**Signal**: Users complete tasks without assistance; positive reaction to value proposition.
**Time to build**: Hours to days.
**Limitation**: Tests usability, not value or willingness to pay.

---

### 6. Pilot with a Single Customer
**What it is**: Full, real deployment with one anchor customer who agrees to give structured feedback.
**Measures**: Real-world value delivery, integration fit, expansion potential.
**Best for**: When the solution is directionally right but needs real usage to validate fit and completeness.
**Signal**: Customer achieves the outcome; renews; refers.
**Time to build**: Weeks.
**Limitation**: High selection bias; one data point is not a market.

---

### 7. Smoke Test / Waitlist
**What it is**: A "coming soon" page or in-product prompt measuring intent to use before a feature ships.
**Measures**: Latent demand within existing user base.
**Best for**: Prioritizing features against a captive audience.
**Signal**: X% of active users sign up.
**Time to build**: Hours.
**Limitation**: Existing customers ≠ new customers; may understate market demand.

---

### 8. Technical Spike / Proof of Concept
**What it is**: A focused engineering experiment to determine if a specific technical approach is feasible.
**Measures**: Technical feasibility, performance, integration complexity.
**Best for**: Feasibility risk — when the unknown is "can we build this at all?"
**Signal**: Core technical problem solved in isolation.
**Time to build**: Days.
**Limitation**: Answers "can we build it?" not "should we?"

---

### 9. Survey / Structured Interview
**What it is**: Targeted questions to customers about behavior, pain, and intent.
**Measures**: Stated preferences, frequency/severity of problem, current workarounds.
**Best for**: Early-stage problem validation; understanding the landscape before designing a solution.
**Signal**: >70% of respondents describe the problem and current solution as inadequate.
**Time to build**: Hours.
**Limitation**: Measures stated behavior, not revealed behavior. "I would use that" ≠ "I will use that."

---

## Cheapest Test Selection Heuristic

When in doubt, apply this sequence:

1. **If you don't know if the problem exists** → Survey / Interview first
2. **If you know the problem exists but not if people want YOUR solution** → Landing page or Concierge
3. **If you know they want it but not if they'll pay** → Pre-sell
4. **If you know they'll pay but not if they can use it** → Prototype test
5. **If you know all of the above but not if you can build it** → Technical spike

**Rule**: Never build what a cheaper test can validate.
