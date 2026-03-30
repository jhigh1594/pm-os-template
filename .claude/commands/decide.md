# Decision-Making Assistant

**Usage:** `/decide [decision-context]`

`/decide` is the fast wrapper for the `decision-quality` skill.

**Canonical skill:** `.claude/skills/decision-quality/SKILL.md`

When invoked, delegate to the decision-quality skill behavior, which combines:
- One-way vs two-way door classification
- Agency bias checks and the 70% rule
- Trade-off evaluation frameworks from 40+ product leaders
- Weighted criteria matrices and decision tenets
- Value thesis documentation and decision logging

## Best Uses

Use `/decide` when you need to:
- Weigh competing options with different trade-offs
- Decide between speed vs quality, build vs buy, etc.
- Get stakeholder alignment on a difficult choice
- Evaluate whether to continue or kill a project
- Create a documented decision record

## Typical Handoffs

- After `/think` or `/prioritize` → `/decide` to make the final call
- After `/discover` → `/decide` to choose a direction
- After `/research` → `/decide` to synthesize findings into a choice
- Before `/spec` → `/decide` to lock in the approach

## Notes

- The skill is the behavioral source of truth; this command exists for speed and ergonomics
- For deep trade-off frameworks, see `references/trade-off-frameworks.md` in the skill directory
- Decisions are logged with value theses that can be validated over time

---

## Step Final: Decision Journal Entry

After completing the decision-quality skill analysis, generate a compact journal entry and offer to append it to `📚 Knowledge/decisions/decision-journal.md`.

**Generate the entry automatically from the analysis:**

```
---
**Decision:** [One sentence — what was decided]
**Date:** [today's date YYYY-MM-DD]
**Type:** Type 1 (one-way door) | Type 2 (two-way door)
**Reversibility cost:** [High | Medium | Low] — [one sentence why]
**Confidence at decision time:** [70% | 80% | 90%+]
**Options considered:** [brief label for each option surfaced in analysis]
**Chosen:** [option selected]
**Rationale (30 words max):** [core reason, key tradeoff made]
**Riskiest assumption:** [what must be true for this to work]
**Success criteria:** [specific threshold — not a direction — for how we'll know we were right]
**Review date:** [YYYY-MM-DD — 30 days out for Type 2, 90 days out for Type 1]
**Outcome:**
**What we learned:**
---
```

**Review date rule:**
- Type 2 (two-way door): today + 30 days
- Type 1 (one-way door): today + 90 days

---
## 🎯 Quality Gate: Judgment / Tradeoffs

**Before we lock this in:**

> "The choice you just made implies something about your product strategy. What does choosing this over the alternative say about what you believe drives value for customers? If someone read only your prioritization decisions for the last quarter, what strategy would they infer?"

_(This is the reasoning step that separates a documented decision from a learned one. Your answer here is the output — not a prerequisite to it.)_

**Save this response to** `📚 Knowledge/Growth/growth-signals-[YYYY-MM].md`? [y/n]

---

**Before appending:** Display the entry and ask: "Append this decision to your journal? (y/n)"

If confirmed, append to `📚 Knowledge/decisions/decision-journal.md` below the `<!-- New entries appended below this line by /decide -->` comment.

> **Principle**: Undocumented decisions are unlearned decisions. The journal is what closes the loop between "what we chose" and "were we right."

---

**What decision are we making?**
