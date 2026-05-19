---
description: 'Use when deciding whether to ship, iterate, or hold. Triggers: ready
  to ship, ship or wait, launch decision, is this ready, rollout plan, ship to beta,
  not ready yet, when should we release, go no-go.'
name: ship-decisions
---

# Ship Decisions

Use this skill when the user needs to decide whether something is ready to ship, should go to a small group first, needs one more cycle, or is not ready.

## Default Mode: Shipping Verdict

Default to a direct shipping call.

Start with:
1. **Verdict** - ship now, ship to small group, iterate one more cycle, or not ready
2. **Why** - 3-5 bullets max
3. **Risks** - only the few that matter
4. **Rollout / next move** - how to ship or what to fix next

Only ask clarifying questions first if core readiness, reversibility, or user impact is too unclear to give a responsible verdict.

## Deep Mode

Use deep mode when:
- the decision is hard to reverse
- architecture, pricing, or trust risk is unusually high
- the user explicitly wants a more detailed ship/no-ship assessment

## Response Contract

For normal chat, default to:

```markdown
## Verdict
[ship now / ship to small group / iterate one more cycle / not ready]

## Why
- [reason 1]
- [reason 2]
- [reason 3]

## Key Risks
- [risk 1]
- [risk 2]

## Next Move
- [rollout step or fix list]
```

Do not begin with a long framework walk-through unless the user explicitly wants it.

## Shipping Lenses

Use the smallest set needed:
- **Core value works** - can the user complete the main job?
- **Edge cases are acceptable** - can failures be handled or recovered from?
- **Reversibility** - can we roll back or limit exposure?
- **Learning value** - do we learn more by shipping now than polishing more?
- **Risk concentration** - are trust, security, platform, or contract risks too high?

## Verdict Definitions

- **Ship now**
  - core value works, risk is acceptable, and broad release is reasonable
- **Ship to small group**
  - value is there, but exposure should be limited while learning
- **Iterate one more cycle**
  - close to ready, but one or two issues meaningfully block confidence
- **Not ready**
  - core value or risk profile is not good enough yet

## Workflow

1. identify the core job the release must satisfy
2. assess the few risks that could invalidate a release
3. decide broad ship vs small group vs iterate vs stop
4. recommend the rollout or next fix list

If rollout matters, recommend the smallest safe path first.

## Craft Level

Answering whether to ship is only half the call. When the verdict is "iterate one more cycle," this matrix scopes exactly what needs polishing — don't gold-plate the whole feature.

```
                    │ USER-FACING │ INTERNAL
────────────────────┼─────────────┼──────────
CORE PRODUCT        │ HIGH CRAFT  │ MEDIUM
NON-CORE FEATURE    │ MEDIUM      │ LOW
EXPERIMENT          │ LOW         │ LOW
```

Dylan Field: "Craft creates moats in the AI era — quality is the differentiator when execution is commoditized. But only in the right places."

**High-craft signals** (invest here):
- Core product loop
- User-facing and used frequently
- Competitive differentiator
- Brand moment

**Move-fast signals** (don't over-invest):
- Internal tool
- One-time or low-frequency use
- Experiment or validation step
- Fully behind the scenes

Use this when the verdict isn't "ship now" — it tells you what the one more cycle should actually touch.

## Rollout Guidance

When shipping:
- prefer feature flags or limited exposure when available
- start with internal or early adopters when confidence is not yet high
- define what will be monitored
- define the rollback trigger if risk warrants it

## Guardrails

- Do not block shipping because something is imperfect but reversible.
- Do not ship broken core value just to create momentum.
- Do not treat one-way-door decisions like button-copy tests.
- Do not keep polishing if the real missing input is user learning.
- Do not recommend broad launch when small-group rollout is the smarter path.
- Do not gold-plate experiments or internal tools — save craft investment for core product loops.
- Do not ship a core product feature at experiment-level quality and call it done.

## Output Variants

### Variant: quick verdict

Use for:
- "Is this ready?"
- "Should we ship this?"

Output:
- verdict
- reasons
- next move

### Variant: rollout recommendation

Use for:
- deciding how broadly to release

Output:
- verdict
- rollout shape
- risks to monitor

### Variant: deeper risk review

Use when explicitly requested.

Output:
- verdict
- reversibility analysis
- trust or platform risks
- rollout plan

### Variant: craft assessment

Use for:
- "How much polish does this need before we ship?"

Output:
- craft level (high / medium / low)
- specific polish areas worth investing in
- time budget

## Example Behavior

If the user asks:
"Is this dependency alert prototype ready for early access?"

Default behavior:
- give a verdict immediately
- explain why briefly
- recommend rollout shape

Do not begin with a long framework explanation unless the user explicitly wants a deep assessment.



## What Makes This Skill Different

<!-- State what pushes Claude OUT of default behavior. What does a naive response miss? -->

## Self-Learning

Before responding, read `LEARNED.md` in this skill directory when it exists and treat it as compact runtime guidance that sharpens this skill.

Rules for self-improvement:
- Keep `SKILL.md` human-owned; do not rewrite it directly from normal usage.
- Propose broader instruction changes through the central skill-learning review queue.
- Only promote specific, reusable, evidence-backed lessons into `LEARNED.md`.
