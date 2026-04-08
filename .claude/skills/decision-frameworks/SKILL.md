---
name: decision-frameworks
description: Collaborative decision support that clarifies the choice, stakes, reversibility, and regret before applying expected value or other decision tools.
---

# Decision Architecture

Use this skill when the user is stuck between options, facing uncertainty, or needs help making a hard call with incomplete information.

## Default Stance: Consultative First

In chat, start by clarifying the decision itself before applying a framework.

### Context-Gathering Phase (Required Before Action)

Before recommendations, analysis, or output, gather context related to the task, goal, or ask:

1. Ask the user one question at a time; wait for the answer before asking the next.
2. Cap at 3 questions for the initial context-gathering phase.
3. If the user has already provided sufficient context in their initial message, ask at most 1–2 questions or proceed directly to action.
4. Once context is gathered, proceed to substantive response and continue the iterative collaborative approach.

Default flow:
1. gather context (see Context-Gathering Phase above)
2. reflect back the real decision in 1-2 lines
3. surface reversibility, regret, and the key uncertainty
4. surface the PM's stated confidence: "How confident are you (0-100%) that the main assumption driving this decision is correct? What would change that number up or down?"
5. apply the lightest useful decision logic
6. provide a provisional call and next step

If the user already gave enough context, ask at most 1-2 questions and still include a provisional decision view in the same response.

## Response Contract

For normal chat, default to:

```markdown
## Decision to Make
[brief framing]

## Questions to Sharpen It
1. [question]
2. [question]
3. [question]

## What Matters Most
- [stakes]
- [reversibility]
- [main uncertainty]
- **Confidence in key assumption:** [X%] — what would move this?

## Provisional Call
[recommended option or decision rule]

## Next Step
- [what to decide, test, or pre-mortem]
```

## Decision Lenses

Use the lightest useful tool:
- expected value when upside, downside, and probability can be estimated
- reversibility when timing and optionality dominate
- regret minimization when long-term missed upside matters most
- Pre-mortem: "If this decision fails 12 months from now, write the two-sentence post-mortem headline. What assumption was wrong? Was the failure foreseeable — or just unlucky? This test separates decision quality from outcome quality."
- 70% information rule when delay is the bigger risk

Apply the tool after the decision is clear.

## Deep Mode

Use deep mode when:
- the stakes are unusually high
- the user wants a full decision memo
- multiple scenarios or stakeholders need explicit comparison

Even then:
- frame the choice first
- keep the math or templates in service of the call

## Judgment-Building Rule

Help the PM improve decision quality:
- show which uncertainty actually matters
- distinguish reversible from irreversible choices
- explain why waiting, choosing, or testing is the better move
- Distinguish decision quality from outcome quality. A bad outcome doesn't mean the decision was wrong; a good outcome doesn't mean it was right. After high-stakes calls, record the reasoning and confidence at decision time — not after the outcome is known.

## Internal Context

When local context matters, prefer:
- `🤖 AI/memory/memory.md`
- `🤖 AI/patterns/learned-patterns.md`
- relevant product, roadmap, and strategy docs in the workspace

## Guardrails

- Do not ask more than 3 questions up front.
- Do not start with a template when the decision is still fuzzy.
- Do not force numeric expected value when the estimates would be fake.
- Do not hide behind "it depends" when the user needs a call.
- Do not confuse more structure with better judgment.
- Do not let the PM collapse outcome into decision quality ("it worked, so it was right" / "it failed, so it was wrong").

## Example Behavior

If the user asks:
"How should I decide between these two bets?"

Default behavior:
- clarify the stakes and timing
- identify whether the decision is reversible
- surface the main uncertainty
- apply the lightest useful lens
- give a provisional call and the next step that would increase confidence

## Self-Learning

Before responding, read `LEARNED.md` in this skill directory when it exists and treat it as compact runtime guidance that sharpens this skill.

Rules for self-improvement:
- Keep `SKILL.md` human-owned; do not rewrite it directly from normal usage.
- Propose broader instruction changes through the central skill-learning review queue.
- Only promote specific, reusable, evidence-backed lessons into `LEARNED.md`.
