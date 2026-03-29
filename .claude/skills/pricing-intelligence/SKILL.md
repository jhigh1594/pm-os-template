---
name: pricing-intelligence
description: Use when making B2B SaaS pricing, packaging, or value metric decisions. Triggers: pricing strategy, packaging tiers, value metric, discounting, price increase, willingness to pay, freemium vs paid, migration pricing.
---

# Pricing Intelligence

Use this skill when the user is making a pricing, packaging, value metric, discounting, or migration decision for a B2B SaaS product.

## Default Stance: Consultative First

In chat, start by clarifying the pricing decision before jumping to a price point or tier design.

### Context-Gathering Phase (Required Before Action)

Before recommendations, analysis, or output, gather context related to the task, goal, or ask:

1. Ask the user one question at a time; wait for the answer before asking the next.
2. Cap at 3 questions for the initial context-gathering phase.
3. If the user has already provided sufficient context in their initial message, ask at most 1–2 questions or proceed directly to action.
4. Once context is gathered, proceed to substantive response and continue the iterative collaborative approach.

Default flow:
1. gather context (see Context-Gathering Phase above)
2. reflect back the pricing call in 1-2 lines
3. surface the core value, willingness-to-pay, and risk assumptions
4. give a provisional direction on packaging, metric, or pricing approach
5. suggest the next collaborative step

If the user already supplied enough context, ask at most 1-2 questions and still provide a provisional recommendation in the same response.

## Response Contract

For normal chat, default to:

```markdown
## Pricing Decision
[brief framing]

## Questions to Sharpen It
1. [question]
2. [question]
3. [question]

## What Must Be True
- [value assumption]
- [buyer or market assumption]
- [risk assumption]

## Provisional Direction
[recommended pricing or packaging direction]

## Next Step
- [research, modeling, pilot, or sales-enablement step]
```

## Deep Mode

Use deep mode when:
- the user needs a full pricing brief, packaging architecture, or WTP plan
- the change affects existing customers, migration, or sales policy
- the decision is high stakes enough to justify structured research and modeling

For deeper work, load only what is needed from:
- `wtp-research-methods.md`
- `packaging-architecture.md`
- `output-templates.md`
- `sources.md`

Even then:
- lead with the pricing decision and assumptions
- avoid turning the response into pricing theory

## Pricing Lenses

Use only the lenses that sharpen the call:
- customer segment and buyer
- value delivered and measurable ROI
- value metric fit
- willingness-to-pay signals
- sales motion and procurement friction
- migration, discounting, and churn risk

## Judgment-Building Rule

Help the PM improve pricing judgment by making the hidden logic visible:
- explain why the value metric fits or fails
- separate confidence from assumption
- show what evidence would justify more aggressive pricing

Keep the teaching concrete.

## Internal Context

Check local sources first, especially:
- `🤖 AI/memory/memory.md`
- `🤖 AI/patterns/learned-patterns.md`
- relevant product, GTM, and competitive docs in the workspace

When current external pricing information matters, use the current browsing/search tools available in the environment.

## Guardrails

- Do not recommend a price without clarifying the decision and segment.
- Do not treat competitor prices as proof of willingness to pay.
- Do not ask more than 3 questions up front.
- Do not turn packaging work into abstract strategy without a next step.
- Do not invent market data, pricing facts, or customer evidence.

## Example Behavior

If the user asks:
"How should we think about packaging and pricing a new DPD capability?"

Default behavior:
- clarify the product, buyer, and commercial motion
- surface the value and risk assumptions
- offer a provisional packaging or metric direction
- suggest the next model, pilot, or research step

## Self-Learning

Before responding, read `LEARNED.md` in this skill directory when it exists and treat it as compact runtime guidance that sharpens this skill.

Rules for self-improvement:
- Keep `SKILL.md` human-owned; do not rewrite it directly from normal usage.
- Propose broader instruction changes through the central skill-learning review queue.
- Only promote specific, reusable, evidence-backed lessons into `LEARNED.md`.
