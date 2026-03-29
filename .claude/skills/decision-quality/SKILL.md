---
name: decision-quality
description: Help make high-quality decisions quickly using structured frameworks. Use when weighing options, making trade-offs, deciding between speed and quality, struggling with difficult choices, asking "should we do X or Y?", or needing to get stakeholder alignment on a choice.
---

# Decision Quality

Make high-quality decisions quickly using structured decision-making frameworks combined with trade-off evaluation principles from 40+ product leaders.

## How to Help

When the user asks for help with a decision:

1. **Classify the decision** — One-way door (irreversible) vs two-way door (reversible)
2. **Check for agency bias** — "If you had total ownership, what would you do?"
3. **Apply the right rigor** — 70% confidence for two-way doors, 90%+ for one-way doors
4. **Evaluate trade-offs** — Use frameworks below for competing options
5. **Structure the output** — Context, options, criteria, value thesis, recommendation

---

## Part 1: Decision Classification

### One-Way vs Two-Way Doors

**One-Way Door** (irreversible, high stakes):
- Need 90%+ confidence
- Involve stakeholders
- Thorough analysis warranted
- Examples: Major architecture change, pricing model shift, public API contract

**Two-Way Door** (reversible, lower stakes):
- Apply 70% rule — decide when you have 70% certainty
- Speed is a feature
- Learn by doing
- Examples: Feature experiment, UI change, process adjustment

> "Most decisions should probably be made with somewhere around 70% of the information you wish you had." — Jeff Bezos

### Agency Bias Check

Before analyzing options, ask:

> **"If you had total ownership and could move immediately, what would you do?"**

This surfaces your "Founder Mode" intuition—the choice you'd make if coordination, permission-seeking, and analysis paralysis weren't factors. This reveals:
- Where you're over-coordinating on two-way doors
- Which option you actually believe in (before rationalization)
- Whether you're stuck in "consensus mode" vs. "execution mode"

**Important**: This isn't the final decision—it's a bias check. If your analysis leads somewhere else, that's fine. But if your final choice differs dramatically from your agency response, examine why.

---

## Part 2: Trade-Off Evaluation

### Core Principles

#### Optimize for Order-of-Magnitude, Not Precision
> "It doesn't really matter if it's 1,000 or 1,001, who cares? It's orders of magnitude larger than the alternative, and so it is better." — Alex Komoroske

Don't waste effort on false precision in uncertain environments. Focus on whether one option is dramatically better (10x), not marginally better (1.001x).

#### Apply the "Would I Start This Today?" Test
> "If you wouldn't start this today, then that means that everything that you're putting into this going forward is the actual waste." — Annie Duke

When evaluating whether to continue a project, ignore sunk costs entirely. The only relevant question is whether you'd begin this effort with today's knowledge.

#### Think More, Ship Better
> "Most experiments should be thought experiments. They should not even be tried out because they're obviously going to fail." — Anuj Rathi

Don't default to "let's just try it" — rigorous upfront thinking eliminates weak ideas before they consume engineering resources.

#### Accept "Worse First" for Long-Term Gains
> "Everything you want is on the other side of worse first." — Graham Weaver

Meaningful change requires accepting short-term decline. Ask what your 5-year future self would want, not what makes tomorrow easier.

#### Create Decision Tenets to Eliminate Recurring Debates
> "Tenets are really decision-making tools... you sort of make a rule for yourself." — Bob Baxley

Identify debates your team has repeatedly and create a tenet to decide the direction once. Good tenets are specific enough that someone could reasonably argue the opposite.

#### Quantify Countervailing Metrics
> "Here's the money that we generate from the emails. Here's the money that we're losing on long-term value. What's the trade-off?" — Ronny Kohavi

Assign dollar values to negative user actions (unsubscribes, churn, support burden) to make objective trade-offs against short-term gains.

### Weighted Criteria Matrix

For complex multi-factor decisions, use a structured matrix:

```
| Criterion | Weight | Option A | Option B | Option C |
|-----------|--------|----------|----------|----------|
| Speed     | 0.3    | 8 (2.4)  | 6 (1.8)  | 4 (1.2)  |
| Quality   | 0.25   | 6 (1.5)  | 8 (2.0)  | 7 (1.75) |
| Cost      | 0.25   | 7 (1.75) | 5 (1.25) | 9 (2.25) |
| Risk      | 0.2    | 5 (1.0)  | 7 (1.4)  | 6 (1.2)  |
| **Total** | 1.0    | **6.65** | **6.45** | **6.40** |
```

> "Identify the criteria that are most important to you... give everything a score, and just multiply it out." — Nicole Forsgren

The process of creating the matrix often reveals the answer before the math is finished.

### Who Loses Analysis

> "Many of the changes that are most consequential create winners and losers." — Ramesh Johari

When making a decision, explicitly identify:
- Who benefits from this choice?
- Who is harmed or disadvantaged?
- Is the net value positive for the ecosystem?

### Cost of Analysis Itself

> "The cost of doing the analysis was this much. So it's guaranteed to be a loser." — Stewart Butterfield

Evaluate whether the person-hours spent analyzing a decision exceed the maximum possible upside of the improvement. Sometimes the analysis cost is the wrong answer.

---

## Part 3: Structured Decision Framework

Use this structure for documenting decisions:

### Context
- What are we deciding?
- Why does this matter?
- What's the deadline/urgency?

### Options
- Option A: [description, pros, cons]
- Option B: [description, pros, cons]
- Option C: Do nothing / wait for more data

### Decision Criteria
- What matters most? (customer value, speed to market, technical quality, cost, strategic alignment)
- What are we optimizing for?
- What are our constraints?

### Value Thesis
- What belief about customer value is driving this decision?
- Complete: **"I believe [customer action X] drives [business outcome Y] because [mechanism Z]"**

Examples:
- "I believe reducing setup time drives retention because customers who see value in Week 1 are 3x more likely to renew"
- "I believe dependency visibility drives adoption because teams currently waste 40% of planning time hunting for blockers"

**Why this matters**: Decisions based on explicit value beliefs can be validated. Decisions based on implicit assumptions can't.

### Risks & Mitigations
- What could go wrong with each option?
- How would we detect problems early?
- How reversible is this decision?

### Recommendation
- Which option and why?
- What data/insights support this?
- What would change our mind?

---

## Part 4: Stakeholder Communication

### Present Clear Either/Or Choices
> "Be very clear with the tradeoffs... present those tradeoffs back to your leadership team. Here's what we're doing and here's what we're not doing." — Geoff Charles

Communicate what the team is NOT doing as clearly as what they are doing. Present a "menu" of options to force a decision.

### Separate "Can" from "Should"
> "Some people are just locked into the can. They're uber pragmatic... others ask 'What should we do here?'" — John Cutler

Don't let feasibility constraints dominate strategic thinking. Explicitly ask what you should do if technical debt weren't an issue.

### Diagnose with Data, Treat with Design
> "Data is not a tool that's going to tell you what you should build... but it can tell you if you have a problem." — Julie Zhuo

Use data to identify problems and gaps, but rely on design and intuition to invent solutions.

---

## Part 5: Decision Log Format

```markdown
# Decision: [Title]
**Date**: [Today's date]
**Owner**: [DRI name]
**Type**: One-way / Two-way door

## Context
[What we're deciding and why]

## Options Considered
1. [Option A]
2. [Option B]
3. [Option C]

## Decision
We chose [X] because [reasoning].

## Key Risks
- [Risk 1 and mitigation]
- [Risk 2 and mitigation]

## Success Criteria
- 1 month: [metric/outcome]
- 3 months: [metric/outcome]
- 6 months: [metric/outcome]

## Reversibility
[How to undo if needed]

## Value Thesis
I believe [customer action] drives [business outcome] because [mechanism]
```

---

## Output Format

### Decision Classification
**Type**: One-Way / Two-Way Door
**Confidence Level Needed**: 70% / 90%
**Decision Velocity**: Move fast / Take time
**DRI**: [Who owns this?]

### Structured Analysis
[Present context, options, criteria as outlined above]

**Value Thesis**: [Your explicit belief about what customer value this decision creates]

### Recommendation
**Choose**: [Option X]
**Why**: [Core reasoning in 2-3 sentences]
**Reversibility**: [How easy to undo if wrong?]
**Success Criteria**: [How we'll measure this in 1/3/6 months]

### Decision Log Entry
[Pre-formatted decision log you can copy to docs]

---

## Constraints

- Don't over-analyze two-way doors (decision fatigue is real)
- Don't under-analyze one-way doors (irreversible mistakes are costly)
- Don't decide by committee (DRI must own it)
- Don't skip documentation (decisions fade from memory)
- Don't ignore dissenting views (they often reveal blind spots)
- Don't confuse confidence with certainty (perfect information doesn't exist)
- Don't distinguish between options that are only marginally different (focus on 10x)

---

## Common Mistakes to Flag

- **False precision** — Spending excessive time distinguishing between options that are only marginally different
- **Sunk cost fallacy** — Continuing a failing path because of what's already been invested
- **Analysis paralysis** — When the cost of deciding exceeds the value difference between options
- **Ignoring second-order effects** — Not accounting for maintenance burden, feature creep, or organizational complexity
- **Defaulting to your skillset** — "If you're a great engineer, the answer to almost every problem is engineering" (Bret Taylor)
- **Only seeing first-order effects** — Changes ripple through systems in ways that aren't immediately obvious

---

## Integration with Other Skills

- Use **/think** to frame strategic context before deciding
- Use **/discover** to validate assumptions in your value thesis
- Use **/measure** to define metrics that test your value thesis
- Use **/coach** for a scored review of your decision document

---

## Deep Dive

For detailed frameworks and all 42 insights from 40+ product leaders, see `references/trade-off-frameworks.md`

---

**What decision are we making?**
