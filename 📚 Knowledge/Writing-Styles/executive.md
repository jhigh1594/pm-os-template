# Writing Guide: Executive Audience

**Who this is for:** C-suite, SVPs, VPs — decision-makers with authority to approve, fund, or block.

---

## Opening Logic

**Lead with the decision or recommendation. Never context first.**

Sentence 1 must contain: what you're recommending OR what decision needs to be made.

> ✅ "I recommend we delay the pricing change until Q3 to preserve the renewal cohort."
> ✅ "We need a decision: proceed with the Ensemble integration in Q2 or push to H2."
> ❌ "I wanted to loop you in on our analysis of the pricing situation."
> ❌ "Over the past few weeks, the team has been looking into..."

**Why this works:** Executives read the first sentence and decide if the rest matters. If sentence 1 is context, they may never reach your recommendation.

---

## Evidence Hierarchy

Order evidence from most to least persuasive for this audience:

1. **Business outcome / revenue impact** — what does this do to ARR, retention, win rate, or cost?
2. **Customer signal** — what are customers or the market saying? (Credible social proof)
3. **Competitive context** — what are competitors doing, and what's the risk of inaction?
4. **Risk / downside** — what's the cost of the alternative or inaction?
5. **Technical or operational details** — only if they create a blocker or require their intervention

---

## Structure Template

```
[Recommendation / decision needed — 1 sentence]

[Why now — 2-3 sentences. Business context + urgency signal]

[Options considered — 2-3 bullets max. Lead with the recommended option]
→ Option A (recommended): [outcome + tradeoff in one line]
→ Option B: [outcome + tradeoff in one line]

[What I need from you — specific ask. One of: approval, input, escalation path]

[Next steps if approved — 2-3 bullets with owners and dates]
```

---

## Tone Markers

- **Confident, not hedging.** "I recommend" not "one option could be" or "it might make sense to consider"
- **Outcome-oriented.** Tie every point back to a business result — not activity, not features
- **Tight.** Every sentence earns its place. No warm-up, no sign-off preamble
- **Honest about tradeoffs.** Executives distrust analysis that has no downside. Name the risk of the recommended path
- **Written for 90 seconds.** The entire document should be readable in under 2 minutes

---

## Anti-Patterns

| Anti-Pattern | Why It Fails | Fix |
|---|---|---|
| "I wanted to loop you in on..." | Context-first — buries the recommendation | Start with the recommendation |
| "We're excited to share..." | Promotional, not executive | Replace with the business outcome |
| "There are many options to consider..." | Signals lack of conviction | Lead with your recommendation, then alternatives |
| Long background section | They know the context — that's why they're executives | Cut to 1-2 sentences of context max |
| Passive voice | Obscures ownership and accountability | "I recommend" / "Engineering will..." not "It has been decided" |
| Ending with "Let me know your thoughts" | Vague ask — no call to action | Be specific: "Do I have your approval to proceed?" |

---

## Integration Notes

- Loaded by `/write --type exec` or when recipient in `📚 Knowledge/People/` has executive role
- Also applies to: pre-read docs, escalation memos, strategic alignment briefs
- Pairs with: `/decide` for structured decision documentation, `/coach --mode comms` for review
- For board/analyst audiences: see `board-analyst.md` (higher signal density, less internal framing)
