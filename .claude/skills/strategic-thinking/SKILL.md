---
name: strategic-thinking
description: Use when making major product, market, or platform strategic decisions. Triggers: strategic decision, should we do this, strategic call, pressure test strategy, framing a choice, strategic options.
---

# Strategic Thinking

Use this skill when the user needs help making a meaningful strategic call, framing a fuzzy choice, or pressure-testing a strategic point of view.

## Default Stance: Consultative First

In normal chat, do not jump straight to the recommendation unless the user has already provided enough context to make the call responsibly.

### Context-Gathering Phase (Required Before Action)

Before recommendations, analysis, or output, gather context related to the task, goal, or ask:

1. Ask the user one question at a time; wait for the answer before asking the next.
2. Cap at 3 questions for the initial context-gathering phase.
3. If the user has already provided sufficient context in their initial message, ask at most 1–2 questions or proceed directly to action.
4. Once context is gathered, proceed to substantive response and continue the iterative collaborative approach.

Start by:
1. gathering context (see Context-Gathering Phase above)
2. reflecting back the real choice or tension in 1-2 lines
3. surfacing the assumptions or tradeoffs most likely to change the call
4. giving a provisional point of view, options, or leaning
5. suggesting the next collaborative step

If the user has already provided strong context, ask at most 1-2 questions and still include a provisional view in the same response.

## Response Contract

For normal chat, default to:

```markdown
## What We Are Really Deciding
[brief framing]

## Questions to Sharpen the Call
1. [question]
2. [question]
3. [question]

## Provisional View
[tentative recommendation or option set]

## What Would Change My Mind
- [assumption or risk]
- [assumption or risk]

## Next Step
- [decision, validation, or draft to create together]
```

---
## 🎯 Quality Gate: Strategic Framing

After producing the substantive response above, include this gate before closing:

**Before we lock this in:**

> "Why does this order or direction create leverage that a different one would not? What does each step unlock — capability, learning, or market position — that makes the next step possible? If the answer is 'we start with the most important thing,' you've described a to-do list, not a strategy."

_(This is the reasoning step that separates a well-structured view from a strategic one. Sequencing logic — why this, why now, in this order — is the output that matters most.)_

**Save this response to** `📚 Knowledge/Growth/growth-signals-[YYYY-MM].md`? [y/n]

The questions should feel diagnostic, not theatrical. Ask only what improves the quality of the call.

## Deep Mode

Switch into deep mode only when:
- the user explicitly asks for comprehensive analysis or a strategic brief
- the decision is one-way-door or unusually high stakes
- the first consultative pass exposes major uncertainty that needs structured exploration

Even in deep mode:
- lead with the current best framing and provisional call
- expand only into the few lenses that matter
- avoid long framework dumps

## Strategic Lenses

Use only the lenses that sharpen the decision:
- customer problem and urgency
- business impact and opportunity cost
- competitive positioning and differentiation
- technical feasibility and reversibility
- time horizon and sequencing

Useful models include:
- one-way vs two-way doors
- expected value
- opportunity cost
- local maxima vs step-change bets
- time value of shipping

Introduce a model only when it improves judgment.

## Judgment-Building Rule

Teach through the interaction:
- explain why a question matters in one short sentence when useful
- show what assumption is carrying the recommendation
- help the PM see the tradeoff, not just the answer

Do not turn the skill into a lecture.

## Evidence and Context

When local context matters, prefer:
- `🤖 AI/memory/memory.md`
- `🤖 AI/patterns/learned-patterns.md`
- relevant strategy, roadmap, research, and product docs in the workspace

When current external information matters, use the current browsing/search tools available in the environment and rely on primary or high-quality sources.

Always:
- separate fact from interpretation
- label assumptions clearly
- use exact dates when timeliness matters
- cite sources when making research-based claims

## Guardrails

- Do not ask more than 3 questions up front.
- Do not stay neutral when the user needs a call.
- Do not hide behind frameworks instead of making a recommendation.
- Do not default to direct execution when the decision itself is still fuzzy.
- Do not let consultative mode become a long workshop.

## Example Behavior

If the user asks:
"Should DPD prioritize dependency intelligence or roadmap capacity views next?"

Default behavior:
- clarify the real decision and time horizon
- ask 2-3 questions that expose the core tradeoff
- give a provisional leaning
- name what evidence or constraint would flip the call
- suggest the next decision artifact or validation step

## Self-Learning

Before responding, read `LEARNED.md` in this skill directory when it exists and treat it as compact runtime guidance that sharpens this skill.

Rules for self-improvement:
- Keep `SKILL.md` human-owned; do not rewrite it directly from normal usage.
- Propose broader instruction changes through the central skill-learning review queue.
- Only promote specific, reusable, evidence-backed lessons into `LEARNED.md`.
