# Writing Guide: Board / Analyst Audience

**Who this is for:** Board members, investors, industry analysts (Gartner, Forrester, IDC), and financial analysts — audiences evaluating Planview's strategic position, competitive trajectory, and business outcomes.

---

## Opening Logic

**Lead with the market signal or strategic move, then the business implication.**

Sentence 1 must contain: what's happening in the market or what Planview is doing strategically.

> ✅ "Enterprise planning software is consolidating around AI-native orchestration — Planview's SPM-to-execution flywheel positions us ahead of this shift."
> ✅ "Q1 renewal rates reached 94% in the enterprise segment, driven by three product changes made in H2."
> ❌ "I'd like to walk you through our product updates from the quarter."
> ❌ "The team has been working hard on several important initiatives."

**Why this works:** Board members and analysts are pattern-matching against the market, not evaluating features. They need to understand the strategic significance immediately — then you can substantiate it.

---

## Evidence Hierarchy

Order evidence from most to least persuasive for this audience:

1. **Market signal or macro trend** — what's the strategic context? What's the market doing?
2. **Business outcome data** — ARR, NRR, win rate, renewal rate, competitive displacement — specific numbers
3. **Strategic positioning** — how does this differentiate Planview? Why does it matter competitively?
4. **Customer validation** — named reference customers or segmented evidence (enterprise vs. mid-market)
5. **Roadmap or capability** — what's being built, and how does it reinforce the strategic position?

---

## Structure Template

```
## Strategic Context
[1-2 sentences on what's shifting in the market and why it matters now]

## Business Performance
[Key metrics — ARR, growth rate, retention, pipeline. Tables preferred over prose for this section]
| Metric | Q[N] | Q[N-1] | YoY |
|--------|------|--------|-----|
| ...    | ...  | ...    | ... |

## Strategic Initiatives Progress
[3-5 bullets. Each: initiative → status → business outcome or leading indicator]
• [Initiative]: [status] — [outcome: X% improvement in Y, N new logos in Z segment]

## Competitive Position
[Where Planview is winning and why. Where there's risk. Honest assessment]
- **Strength:** [Specific differentiation, with evidence]
- **Risk:** [Where competitors are closing the gap or where we're losing]

## Key Decisions / Input Needed
[1-3 specific items. Be direct about what you need from the board]

## Outlook
[Next 1-2 quarters. Specific commitments, not aspirations]
```

---

## Tone Markers

- **Strategic, not operational.** Boards don't need feature details — they need to understand if the company is on the right trajectory
- **Numbers-led.** Every strategic claim needs a metric attached or a clear path to measurement
- **Honest about competitive reality.** Claiming "no competition" or glossing over threats destroys credibility
- **Confident in uncertainty.** "We expect X; the key risk is Y" is stronger than false precision or excessive hedging
- **Differentiation, always.** Every capability should answer "why couldn't a competitor do this?"

---

## Anti-Patterns

| Anti-Pattern | Why It Fails | Fix |
|---|---|---|
| "We have no real competition" | Destroys credibility — every board member knows the landscape | Acknowledge and differentiate: "ServiceNow competes on [X]; we win on [Y]" |
| Feature catalog without strategic narrative | Board sees a roadmap, not a strategy | Frame capabilities through the strategic position they reinforce |
| Vanity metrics (app downloads, page views) | Easy to inflate, hard to connect to business value | Use NRR, win rate, payback period, pipeline coverage |
| Everything is "on track" | Boards know projects slip; this signals concealment | Acknowledge yellow/red items proactively with the recovery plan |
| Long prose financial sections | Hard to scan under time pressure | Use tables; prose for the narrative, numbers in structured format |
| Roadmap that only shows future | Boards want accountability on what was committed | Show: committed → delivered → outcome, not just what's coming |

---

## Context-Specific Variants

### Analyst Briefings (Gartner, Forrester)
- Lead with the analyst's research question, not Planview's agenda
- Anticipate the Magic Quadrant / Wave criteria and address them explicitly
- Include: differentiation vs. named competitors, customer evidence, roadmap alignment to their evaluation criteria
- No marketing language — analysts are trained to see through it; use product specifics

### Investor Updates
- ARR, NRR, CAC payback, gross margin, pipeline coverage — these are the metrics they're running
- Include guidance vs. actuals, not just actuals
- If there are misses: own them with a clear root cause and corrective action

---

## Integration Notes

- Loaded by `/write --type board`, `/write --type analyst`, or when context indicates investor/analyst audience
- Pairs with: `/think` for strategic framing, `/compete` for competitive positioning, `/measure` for metric selection
- Cross-reference: `executive.md` for internal leadership communications; this guide is specifically for external strategic audiences
