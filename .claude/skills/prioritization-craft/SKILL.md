---
description: 'Use when deciding what to build first, rank a backlog, or make prioritization
  tradeoffs. Triggers: what goes first, rank these, prioritize backlog, above the
  line, RICE, value vs effort, capacity constraint, quarterly prioritization, what
  to cut.'
name: prioritization-craft
---

# Prioritization Craft

Use this skill when the user needs help deciding what goes now, later, or not at all.

## Default Stance: Consultative First

In normal chat, do not rank immediately unless the objective, horizon, and constraints are already clear.

### Context-Gathering Phase (Required Before Action)

Before recommendations, analysis, or output, gather context related to the task, goal, or ask:

1. Ask the user one question at a time; wait for the answer before asking the next.
2. Cap at 3 questions for the initial context-gathering phase.
3. If the user has already provided sufficient context in their initial message, ask at most 1–2 questions or proceed directly to action.
4. Once context is gathered, proceed to substantive response and continue the iterative collaborative approach.

Default flow:
1. gather context (see Context-Gathering Phase above)
2. reflect back the prioritization problem in 1-2 lines
3. surface the most important tradeoff or scarce resource
4. provide a ranked recommendation or above/below-the-line call
5. suggest the next collaborative or stakeholder step

If the user already supplied enough context, ask at most 1-2 questions and still include a provisional ranking in the same response.

## Response Contract

For normal chat, default to:

```markdown
## Prioritization Call
[brief framing]

## Questions to Sharpen It
1. [question]
2. [question]
3. [question]

## What Is Constraining Us
- [goal, capacity, dependency, or commitment]

## Provisional Order
1. [item] — Confidence: [High/Med/Low or X%] | Key assumption: [what must be true]
2. [item] — Confidence: [High/Med/Low or X%] | Key assumption: [what must be true]
3. [item] — Confidence: [High/Med/Low or X%] | Key assumption: [what must be true]

## Why / Next Step
- [main tradeoff]
- [communication or validation step]
- "Which item in this ranking are you least confident about? What's the cheapest signal that would let you reorder — a customer interview, a data pull, a spike? Bet size your investment: the lower your confidence, the more you should stage the commitment rather than all-in."
```

The questions should reduce shallow ranking, not delay the answer.

## Deep Mode

Use deep mode when:
- the input is raw feedback rather than a prepared list
- there are 10+ items or multiple source types
- stakeholder communication is a major part of the task
- the user explicitly asks for a deeper prioritization pass

Even then:
- clarify the objective and constraint first
- keep the ranking and rationale concise

### Triage Structure for Raw Feedback (T1–T5)

When the input is verbatim quotes, tickets, interviews, or requests from multiple sources, run these preprocessing steps before prioritizing:

**T1 – Gather and Preserve**
- Collect from all sources (interviews, tickets, sales, internal)
- Preserve verbatim language — don't paraphrase
- Count frequency: 1 request = noise, 3–5 = weak signal, 10+ = strong signal
- Identify requester segment and influence level

**T2 – Summarize and Normalize**
- One-sentence summary per request capturing the essence
- Map to underlying problem (the job, not the solution)
- Assess frequency and business impact

**T3 – Deduplicate by Problem**
- Group requests solving the same underlying problem
- Template: `[Problem Theme] → [Request A, B, C] → [Consolidated Problem Statement]`
- Flag conflicts where customers want opposite things

**T4 – Categorize**
- Assign each group: theme, requester type, strategic fit, type of work
- Use categorization to surface patterns before scoring

**T5 – Transition to Prioritization**
- Once deduplicated, hand off the consolidated problem list to the normal prioritization flow above

## Prioritization Lenses

Use only the lenses needed for the decision:
- customer value
- strategic alignment
- effort and complexity
- time sensitivity
- opportunity cost
- commitments and dependencies
- confidence / assumption risk — how well-validated is the value hypothesis for this item? High-confidence items can be committed fully; low-confidence items should be staged or time-boxed to preserve optionality.

Frameworks like RICE, value vs effort, or cost of delay are optional aids, not the point of the response.

## Judgment-Building Rule

Help the PM improve prioritization judgment:
- make the constraint explicit
- show which tradeoff is doing the real work
- explain why ties usually hide indecision
- Surface confidence explicitly — the constraint doing the real work is often not capacity or strategy, but evidence quality. A tie between two items usually means you need a signal, not a framework.

---

## 🎯 Quality Gate: Opportunity Cost Excavation

**Before we lock this in:**

> "What is this decision saying no to — not just the alternatives you considered, but the types of problems and customers you're de-prioritizing by going in this direction? Who loses in this tradeoff, and is that the right call?"

_(This is the reasoning step that separates a good prioritization from a great one.)_

**Auto-saving to** `📚 Knowledge/Growth/growth-signals-YYYY-MM.md` — append entry now. No prompt needed.

---

## Historical Context

When local context is useful, refer to:
- `🤖 AI/memory/memory.md`
- `🤖 AI/patterns/learned-patterns.md`
- relevant roadmap, strategy, and planning docs in the workspace

## Guardrails

- Do not ask more than 3 questions up front.
- Do not rank items before clarifying the outcome and horizon.
- Do not let every item stay above the line.
- Do not hide hard tradeoffs behind ties or vague scoring.
- Do not score mechanically if the framework obscures the real decision.
- Do not rank items at equal confidence when evidence quality differs sharply — flag the gap and recommend a validation step before committing capacity.

## Example Behavior

If the user asks:
"How should we think about ranking these requests for next quarter?"

Default behavior:
- ask what outcome matters most this quarter
- clarify the biggest capacity or commitment constraint
- provide a provisional order
- explain the tradeoff
- suggest the stakeholder message or revisit trigger



## What Makes This Skill Different

<!-- State what pushes Claude OUT of default behavior. What does a naive response miss? -->

## Self-Learning

Before responding, read `LEARNED.md` in this skill directory when it exists and treat it as compact runtime guidance that sharpens this skill.

Rules for self-improvement:
- Keep `SKILL.md` human-owned; do not rewrite it directly from normal usage.
- Propose broader instruction changes through the central skill-learning review queue.
- Only promote specific, reusable, evidence-backed lessons into `LEARNED.md`.
