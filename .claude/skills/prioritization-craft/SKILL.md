---
name: prioritization-craft
description: Use when deciding what to build first, rank a backlog, or make prioritization tradeoffs. Triggers: what goes first, rank these, prioritize backlog, above the line, RICE, value vs effort, capacity constraint, quarterly prioritization, what to cut.
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
1. [item]
2. [item]
3. [item]

## Why / Next Step
- [main tradeoff]
- [communication or validation step]
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

## Prioritization Lenses

Use only the lenses needed for the decision:
- customer value
- strategic alignment
- effort and complexity
- time sensitivity
- opportunity cost
- commitments and dependencies

Frameworks like RICE, value vs effort, or cost of delay are optional aids, not the point of the response.

## Judgment-Building Rule

Help the PM improve prioritization judgment:
- make the constraint explicit
- show which tradeoff is doing the real work
- explain why ties usually hide indecision

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

## Example Behavior

If the user asks:
"How should we think about ranking these requests for next quarter?"

Default behavior:
- ask what outcome matters most this quarter
- clarify the biggest capacity or commitment constraint
- provide a provisional order
- explain the tradeoff
- suggest the stakeholder message or revisit trigger

## Self-Learning

Before responding, read `LEARNED.md` in this skill directory when it exists and treat it as compact runtime guidance that sharpens this skill.

Rules for self-improvement:
- Keep `SKILL.md` human-owned; do not rewrite it directly from normal usage.
- Propose broader instruction changes through the central skill-learning review queue.
- Only promote specific, reusable, evidence-backed lessons into `LEARNED.md`.
