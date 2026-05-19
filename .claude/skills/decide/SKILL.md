---
name: decide
description: Use when facing a decision with multiple valid paths, competing criteria, or unclear tradeoffs. Merges decision-frameworks, decision-quality, and strategic-thinking into one entry point.
---

# Decide

Single entry point for all decision-making. Use when the user is stuck between options, facing uncertainty, needs help making a hard call with incomplete information, or pressure-testing a strategic choice.

**Triggers:** should we do X or Y, how should we decide, which option, tradeoff analysis, decision framework, compare alternatives, decision matrix, weighing options, making trade-offs, struggling with difficult choices, strategic decision, should we do this, pressure test strategy, framing a choice, strategic options, what would X choose, prioritize X vs Y, roadmap decision, resource allocation, competing requests, what should we do with this.

**Boundary with reason:** `reason` helps you understand a problem or domain. `decide` helps you choose between options. They're complementary — use `reason` first if the problem isn't clear, then `decide` to choose a path.

---

## Default Flow

1. Gather context (3 questions max — see below)
2. Reflect back the real decision in 1-2 lines
3. Classify the decision type (one-way vs two-way door)
4. Surface the riskiest assumption
5. Apply the lightest useful lens
6. Provide a provisional call and next step

**Gate:** If the user already provided context, ask 1 question max and give a provisional view in the same response. Never hide behind "it depends."

---

## Context-Gathering (3 Questions Max)

Ask one at a time, wait for answers, stop when you have enough:

1. "What are we really deciding here?" — frames the choice itself
2. "Why does this matter / when does it need to be decided?" — urgency + reversibility
3. "What would have to be true for this to succeed?" — surfaces riskiest assumption

---

## Decision Classification

**One-way door** (irreversible, high stakes):
- Require 90%+ confidence before proceeding
- Involve stakeholders, do thorough analysis
- Examples: pricing model change, public API contract, major architecture shift

**Two-way door** (reversible, lower stakes):
- Apply 70% rule — decide when you have 70% certainty
- Speed is a feature; learn by doing
- Examples: feature experiment, UI change, process adjustment

> Call out the door type explicitly. Two-way doors attract analysis appropriate for one-way doors — naming it breaks the pattern.

---

## Decision Lenses

Use the lightest tool that fits the decision type:

**Expected value** — when upside, downside, and probability can be estimated without fake precision. Optimize for order-of-magnitude differences, not marginal ones.

**Reversibility / optionality** — when timing and the ability to change course dominate.

**Regret minimization** — when long-term missed upside matters more than short-term efficiency. Ask what your 5-year future self would want.

**Pre-mortem** — for high-stakes calls: "If this decision fails 12 months from now, write the two-sentence post-mortem headline. What assumption was wrong? Was it foreseeable or just unlucky?" Separates decision quality from outcome quality.

**Agency bias check** — "If you had total ownership and could move immediately, what would you do?" Surfaces founder-mode intuition before rationalization sets in. If the final choice differs dramatically, examine why.

**70% information rule** — when delay is the bigger risk. Don't wait for perfect information on reversible decisions.

**Opportunity cost vs do-nothing** — always name the default option. Not deciding is a decision.

**Time value of shipping** — make the cost of delay explicit, not implicit.

**Who loses** — explicitly map winners and losers. Many consequential decisions create both. Net value must be positive for the ecosystem.

**Sunk cost clarity** — "Would I start this today with what I know now?" If no, everything going forward is the actual waste.

**Local maxima vs step-change** — are you optimizing within the current model, or does this bet require accepting worse-first for a step-change gain?

**Value thesis** — make the belief explicit: "I believe [customer action X] drives [business outcome Y] because [mechanism Z]." Decisions with explicit value beliefs can be validated. Decisions with implicit assumptions can't.

**Decision tenets** — for recurring debates, make the rule explicit once. Good tenets are specific enough that someone could reasonably argue the opposite.

---

## Output Format

```
## Decision
[brief framing in 1-2 lines]

## Type
One-way door (90%+ confidence required) / Two-way door (70% rule applies)

## What Would Have to Be True
[riskiest assumption carrying the recommendation]

## Confidence
[X%] — what would move this up or down?

## Provisional Call
[decision rule, not a flat recommendation — "If X matters more than Y, go with A; if Y matters more, go with B"]

## Riskiest Assumption
[what must be true + what disconfirms it]

## Next Step
[test / validate / conversation — one concrete action]
```

**Add for strategic decisions:** Sequencing logic gate — "Why does this order create leverage? What does each step unlock — capability, learning, or market position — that makes the next step possible? If the answer is 'we start with the most important thing,' you've described a to-do list, not a strategy."

**Add for recurring debates:** Propose a decision tenet — name the debate and write the rule that decides it once.

**Add for high-stakes / one-way doors:** Pre-mortem + decision log entry (see Decision Log section below).

---

## Criteria Weighting

When multiple factors compete, surface the tiebreaker explicitly. Ask: "If all options were equal on four of these five criteria, which single one would decide it?" Listing criteria as if they matter equally is polite but unhelpful.

For complex multi-factor decisions, use a weighted matrix:

```
| Criterion | Weight | Option A | Option B |
|-----------|--------|----------|----------|
| [factor]  | 0.X    | score    | score    |
```

The process of filling the matrix often reveals the answer before the math is done.

---

## Decision Log

For one-way doors or high-stakes calls, auto-generate this entry and offer to append it to `📚 Knowledge/decisions/decision-journal.md`:

```
---
Decision: [one sentence — what was decided]
Date: [YYYY-MM-DD]
Type: One-way door | Two-way door
Confidence at decision time: [X%]
Options considered: [brief label for each]
Chosen: [option]
Rationale (30 words max): [core reason, key tradeoff made]
Riskiest assumption: [what must be true for this to work]
Value thesis: I believe [customer action] drives [business outcome] because [mechanism]
Success criteria: [specific threshold — not a direction — for how we'll know we were right]
Review date: [+30 days for two-way door / +90 days for one-way door]
Outcome:
What we learned:
---
```

> Undocumented decisions are unlearned decisions. The log closes the loop between "what we chose" and "were we right."

---

## Guardrails

**Do:**
- Always give a provisional call, even with incomplete info — a wrong call with clear reasoning is more useful than no call
- Distinguish decision quality from outcome quality (bad outcome ≠ wrong decision; good outcome ≠ right decision)
- Make criteria weighting transparent — name which criterion actually breaks the tie
- Match the lens to the decision type (math problem vs values problem vs timing problem)
- Name assumptions carrying the recommendation
- End every session with a concrete next step that creates commitment

**Don't:**
- Ask more than 3 questions up front
- Hide behind "it depends"
- Force numeric precision when the estimates would be fake
- Apply high-rigor process to reversible (two-way door) decisions
- Give flat recommendations — give decision rules
- Let analysis cost exceed the maximum upside of the improvement
- Default to your strongest tool regardless of fit (engineers default to engineering; PMs default to frameworks)

---

## Common Failure Modes

- **Wrong framework for the decision type** — cost-benefit on a values decision, scenario planning on a simple binary. Ask: is this a math problem, a values problem, or a timing problem?
- **Flat recommendation instead of decision rule** — provisional call should say "if X then A, if Y then B," not just "choose A"
- **Flat criteria weighting** — treating five criteria as equal when one drives 80% of the call
- **Framework without behavior change** — beautiful matrix, no action. If the framework doesn't change the next step, it was the wrong framework
- **Two-way door over-analyzed** — explicitly naming the door type resets the appropriate rigor
- **Analysis paralysis on reversible choices** — cost of deciding exceeds value difference between options

---

## 🎯 Quality Gate: Judgment / Tradeoffs

**Before we lock this in:**

> "The choice you just made implies something about your product strategy. What does choosing this over the alternative say about what you believe drives value for customers? If someone read only your prioritization decisions for the last quarter, what strategy would they infer?"

_(This is the reasoning step that separates a good decision from a great one.)_

**Auto-saving to** `📚 Knowledge/Growth/growth-signals-YYYY-MM.md` — append entry now. No prompt needed.

---

## Self-Learning

Before responding, read `LEARNED.md` in this directory when it exists and treat it as compact runtime guidance.

Rules for self-improvement:
- Keep `SKILL.md` human-owned; do not rewrite it directly from normal usage
- Only promote specific, reusable, evidence-backed lessons into `LEARNED.md`
- Propose broader changes through the central skill-learning review queue
