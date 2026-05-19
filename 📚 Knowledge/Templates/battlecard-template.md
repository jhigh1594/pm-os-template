# Battlecard Template

**Purpose:** Equip sales and SE teams to win competitive deals. Every section answers a question a rep faces in a live deal.

**Output path:** `📚 Knowledge/Market/battlecard-[competitor-slug].md`
**Maintained by:** PM (product claims + differentiation), Sales/SE (deal-stage notes + proof points)
**Updated triggers:** 3+ losses to this competitor in 90 days (`/win-loss` pattern alert) OR significant competitive product release

---

## [Competitor Name] Battlecard

**Competitor:** [Full name]
**Slug:** [lowercase-hyphenated for file naming]
**Last updated:** YYYY-MM-DD
**Confidence level:** [High / Medium / Low] — [one sentence on data quality: based on X win/loss interviews, product evaluations, etc.]

---

## When They Come Up

[Describe the deal scenarios where this competitor appears. Be specific: deal size, vertical, buyer persona, evaluation stage.]

Examples:
- Large enterprise renewals where buyer is consolidating tools
- Mid-market deals where IT is evaluating an incumbent suite
- Regulated verticals with long procurement cycles

---

## Their Pitch

[What the competitor says about themselves — their strongest positioning claims, in their language. 3-5 bullets.]

- "[Their actual claim or tagline]"
- "[Core capability they lead with]"
- "[The promise they make to the buyer]"

> Source the claims. Date them. Stale competitive intel is dangerous.

---

## The Real Difference

[This is the most important table. Be honest about where they're strong. Sales teams trust battlecards that acknowledge competitor strengths — otherwise they stop using them.]

| Claim | Their Approach | Our Approach | Why It Matters in a Deal |
|-------|---------------|--------------|--------------------------|
| [Capability area] | [What they do, how it works] | [What we do, how it works] | [Which buyer persona cares, and why ours wins *or* when theirs wins] |
| [Capability area] | ... | ... | ... |

**Confidence flags:**
- Mark rows with [LOW CONFIDENCE — verify before using in deal] if data is secondhand or outdated
- Mark with [THEIR WIN] if the competitor genuinely outperforms here — don't hide this

---

## Our Strengths

[Where we win and why — specific to this competitor comparison. 3-5 bullets.]

- **[Strength]:** [One sentence on what makes this real, not marketing language]
- **[Strength]:** ...

---

## Their Real Strengths

[Where the competitor genuinely outperforms us. Be honest. If a rep discovers you've hidden this, they'll stop trusting the card.]

- **[Their strength]:** [What it is and why it matters to some buyers]
- **[Their strength]:** ...

---

## How to Handle Their Strengths

[For each real competitor strength, a counter-move. Not spin — strategy.]

- **When they lead with [their strength]:** [Reframe, redirect, or acknowledge and pivot to our strength]
- **When buyer asks "Why can't you do [X]?":** [Honest answer + why our approach is better for their situation]

---

## Proof Points

[Specific wins against this competitor. Use real numbers. Anonymize if needed.]

- [Customer type / vertical]: "[Outcome achieved]" — displaced [Competitor] after [Y months]
- [Customer type]: Chose us over [Competitor] because [specific reason — not just "better product"]

> **Rule:** If you can't name at least 2 proof points, mark this card as low confidence.

---

## Discovery Questions That Expose Their Gaps

[Questions a rep can ask to surface the pain that this competitor can't solve. Write them to sound natural in a conversation.]

1. "[Question that uncovers a limitation of the competitor without naming them]"
2. "[Question that highlights a use case we own]"
3. "[Question about buying committee or integration needs we handle better]"

---

## Deal-Stage Notes

[Different plays for different moments in the evaluation cycle.]

### Discovery
[What to establish early that tilts the evaluation criteria in our favor]

### Demo / Evaluation
[What to show, what to avoid showing, what to make them show the competitor]

### Late-Stage / POC
[How we win when it goes to a formal evaluation or proof of concept]

### Negotiation / Legal
[Pricing, terms, or contract patterns that come up with this competitor]

---

## Signals This Competitor Is In the Deal

[Behavioral signals that indicate the competitor is being evaluated. Helps reps know when to raise their game.]

- Buyer asks about [specific integration or feature this competitor leads with]
- IT/procurement starts asking about [compliance/pricing pattern specific to competitor]
- Evaluation includes [tool/process associated with their ecosystem]
- Champion goes quiet after demo — often means competitor got a better demo slot

---

## Quick Reference (for the rep in a hurry)

**One-line differentiator:**
[The cleanest sentence to say when asked "How are you different from [Competitor]?"]

**Biggest risk if we don't address it:**
[The one thing that loses deals to this competitor if not handled]

**Go-to discovery question:**
[The single best question to ask to expose their gap]

---

*This battlecard is maintained by Product. Sales/SE: flag gaps or stale data via `/signal --source sales` or `/win-loss`.*
