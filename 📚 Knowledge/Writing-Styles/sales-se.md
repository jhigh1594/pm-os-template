# Writing Guide: Sales / Solutions Engineer Audience

**Who this is for:** Account Executives, Solutions Engineers, Customer Success Managers — people in revenue-facing roles who need to win, close, or retain deals.

---

## Opening Logic

**Frame everything through: does this help them win?**

Three lenses, in order of relevance:
1. Does this help close a deal or handle an objection?
2. Does this accelerate pipeline?
3. Does this reduce competitive risk in an active deal?

Sentence 1 must answer one of those questions — explicitly.

> ✅ "Here's what to say when Jira Align claims portfolio-level visibility — and why our dependency model wins."
> ✅ "This release addresses the top 3 objections you've been getting from enterprise IT."
> ❌ "We're launching a new feature called Ensemble Custom Views."
> ❌ "The PM team has been working on improvements to the roadmap view."

**Why this works:** Sales teams are in the middle of deals. They don't have time to translate feature announcements into sales language — you have to do it for them.

---

## Evidence Hierarchy

Order evidence from most to least persuasive for this audience:

1. **Objection or competitive claim it addresses** — what question or pushback does this answer in a deal?
2. **Customer proof point** — a named reference, a quote, a metric from a real deployment
3. **Differentiation vs. named competitors** — not generic "we're better" but specific: "Jira Align requires [X]; we do [Y] without it"
4. **Discovery questions** — how do they use this to uncover the problem in a customer conversation?
5. **Product details** — only enough to answer a technical follow-up; SEs need more here than AEs

---

## Structure Template

```
## What This Is (1 sentence)
[Capability name + what it does in plain language]

## When to Use It in a Deal
[The deal stage, competitor situation, or customer role where this matters — 2-3 bullets]
• Use this when: [trigger scenario]
• Use this when: [trigger scenario]

## The Objection / Competitor Claim It Handles
[Exact objection text or competitor pitch] → [Your response / reframe]

## Differentiation (vs. named competitor)
| Claim | Their Approach | Our Approach |
|-------|----------------|--------------|
| [Capability] | [How they do it] | [How we do it — the real difference] |

## Discovery Questions That Expose the Gap
Use these to surface the pain before presenting the solution:
1. "[Question that uncovers the problem this solves]"
2. "[Question]"

## Customer Proof Point
[Reference customer or anonymized segment + specific outcome: "Mid-size insurer, 40% reduction in cross-team dependency conflicts after 90 days"]

## One-Liner for the Deal
[The sentence the AE can use in an email or on a call to make this relevant — written to be copy/pasted]
"[Clean sentence framing the value for an executive buyer]"
```

---

## Tone Markers

- **Deal-focused, always.** Every section ties back to: how does this help them close or retain?
- **Specific about competitors.** Vague differentiation is useless in a live deal — name the competitor, name the claim, name the counter
- **Copy-paste ready.** Sales enablement materials should include sentences or bullets the rep can use directly
- **Honest about limitations.** SEs who trust your materials will use them; if they find an inaccuracy in a demo, it's worse than you not publishing
- **Segment-specific when possible.** "Enterprise IT at financial services" > "enterprise customers"

---

## Anti-Patterns

| Anti-Pattern | Why It Fails | Fix |
|---|---|---|
| Capability list without deal framing | Rep has to translate — they won't | Lead with the objection it handles or the competitor claim it refutes |
| "Best-in-class" / "industry-leading" | Meaningless without specifics | "The only tool that does X without requiring Y" — be specific |
| Missing competitive comparison | SEs face named incumbents in real deals | Include named comparison or don't publish for deal use |
| No proof point | Claims without evidence in B2B enterprise = ignored | Include at minimum an anonymized customer outcome |
| PM language in sales copy | "Unlock value stream alignment" → rep loses the room | Translate: "Show your executives exactly where portfolio delays are happening" |
| Feature-first announcement | Reps have to figure out when to use it | Give them the trigger: "Use this when the customer says X" |

---

## Context-Specific Variants

### Battlecards
Battlecards for this audience follow the template in `📚 Knowledge/Templates/battlecard-template.md`.
Key addition for sales/SE: include "Deal-Stage Notes" — what to say at discovery vs. demo vs. evaluation.

### Release Notes for Sales
- Group by: deals it helps win, objections it addresses, features requested by named accounts
- Don't publish internal codenames or engineering details
- Include: GA date, availability (all tiers? enterprise only?), what changed in trial/demo environments

### SE Technical Deep-Dives
- When the SE audience needs more technical depth, use `technical.md` for the architecture section
- Framing should still stay deal-focused: "Here's how to answer the security review questions"

---

## Integration Notes

- Loaded by `/write --type sales`, `/write --type battlecard`, `/compete`, or when context indicates sales/SE audience
- Pairs with: `/compete` for battlecard generation, `/win-loss` for updating based on deal learnings, `/signal --source sales` for capturing insights
- Cross-reference: `customer.md` for customer-facing materials; `sales-se.md` is for the sales team, not the customer
