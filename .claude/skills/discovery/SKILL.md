---
name: discovery
description: Use when clarifying what to learn, which assumption matters most, or which discovery method to use next. Also use when building an ongoing discovery system, setting up weekly customer contact, mapping an opportunity solution tree (OST), or establishing a product trio workflow. Triggers: discovery plan, what to learn, user research method, customer interviews, assumption to test, validation approach, research design, Teresa Torres, continuous discovery, opportunity solution tree, OST, weekly touchpoints, discovery cadence, product trio, assumption testing hierarchy.
---

# Discovery

Use this skill when the user needs to clarify what to learn, which assumption matters most, or what discovery method should come next.

## Default Stance: Consultative First

In chat, start by helping the user define the decision discovery should inform before recommending a method.

### Context-Gathering Phase (Required Before Action)

Before recommendations, analysis, or output, gather context related to the task, goal, or ask:

1. Ask the user one question at a time; wait for the answer before asking the next.
2. Cap at 3 questions for the initial context-gathering phase.
3. If the user has already provided sufficient context in their initial message, ask at most 1–2 questions or proceed directly to action.
4. Once context is gathered, proceed to substantive response and continue the iterative collaborative approach.

Default flow:
1. gather context (see Context-Gathering Phase above)
2. reflect back the decision and riskiest assumption in 1-2 lines
3. recommend the lightest valid discovery method
4. explain why that method fits
5. suggest the next collaborative step

If enough context already exists, ask at most 1-2 questions and still provide a method recommendation in the same response.

## Response Contract

For normal chat, default to:

```markdown
## Decision This Discovery Should Inform
[brief framing]

## Questions to Sharpen It
1. [question]
2. [question]
3. [question]

## Riskiest Assumption
[what must be true]

## Best Next Method
[recommended method and why]

## Next Step
- [who to talk to, what to test, or what to draft]
```

The method should follow the decision and assumption, not precede them.

## Deep Mode

Use deep mode when:
- the user wants a full research plan or study design
- the work spans multiple interviews or weeks
- the output needs to become a formal synthesis or reusable artifact

Even then:
- lead with the decision and assumption
- recommend the smallest useful study before expanding into a full program

## Cadence Mode (Teresa Torres)

Use cadence mode when the user wants to build an *ongoing* discovery system rather than answer a one-time research question. Trigger phrases: "set up weekly discovery", "opportunity solution tree", "product trio", "continuous discovery", "Teresa Torres", "discovery habit".

**The three pillars:**
1. **Weekly customer contact** — minimum 3-5 touchpoints/week by the product trio (PM + designer + engineer together, not PM alone)
2. **Opportunity solution tree (OST)** — visualizes the path from outcome → opportunities → solutions → assumptions → experiments
3. **Assumption testing before building** — test highest-risk assumptions with the cheapest valid method first

**OST structure:**
```
Outcome (the business result we're driving)
  ↓ Opportunities (customer needs/pain points, from interviews)
    ↓ Solutions (possible ways to address each opportunity)
      ↓ Assumptions (what must be true for the solution to work)
        ↓ Experiments (cheapest way to test each assumption)
```

**Assumption testing hierarchy** (test in this order):
1. Desirability — do customers want this?
2. Usability — can they use it?
3. Feasibility — can we build it?
4. Viability — should we build it?

Use cheapest test first: Interview < Survey < Prototype < Concierge < Build

**Weekly cadence template:**
- Mon–Wed: 3 interviews (product trio attends together)
- Thu: synthesis session, update OST, capture interview snapshots
- Fri: decide build / test more / pivot; plan next week

**Quality gate — before closing any cadence or OST output:**
> "Is the customer insight here based on *stories* — specific customers, specific moments, specific behaviors observed — or on *opinions* — things customers told you they want when asked directly? Opinions are fast to collect and unreliable. Stories are slow to collect and durable. Which type is this built on, and what would it take to upgrade the weakest evidence?"

**Auto-saving to** `📚 Knowledge/Growth/growth-signals-[YYYY-MM].md` when cadence mode fires — append the outcome being pursued and the riskiest assumption identified.

## Discovery Lenses

Use only the lenses that matter:
- what decision this research should change
- which assumption is riskiest
- whether the question is problem, solution, behavior, or quantification oriented
- what the cheapest valid learning method is
- what result would change scope, roadmap, or confidence

Common methods:
- problem interviews
- prototype tests
- concierge or fake-door tests
- analytics or support-pattern review
- surveys only when the problem is already well framed

## Judgment-Building Rule

Help the PM get better at discovery by making the logic visible:
- explain why the chosen method fits the assumption
- name what the method cannot tell us
- redirect feature-first thinking back to the decision being informed

## Internal Context

When workspace context matters, prefer:
- `🤖 AI/memory/memory.md`
- `🤖 AI/patterns/learned-patterns.md`
- customer research, strategy, and product docs already present in the workspace

## Guardrails

- Do not recommend a large study for a small decision.
- Do not jump to methods before clarifying the decision.
- Do not over-index on surveys when the question is still fuzzy.
- Do not keep researching when the next best move is to test a small slice.
- Do not ask vague questions that fail to sharpen the learning plan.

## Example Behavior

If the user asks:
"How should we validate whether dependency alerts solve a real customer problem?"

Default behavior:
- ask what decision the validation needs to support
- surface the main assumption
- recommend the lightest valid method
- explain what success would look like
- suggest the next interview, prototype, or experiment step

## Self-Learning

Before responding, read `LEARNED.md` in this skill directory when it exists and treat it as compact runtime guidance that sharpens this skill.

Rules for self-improvement:
- Keep `SKILL.md` human-owned; do not rewrite it directly from normal usage.
- Propose broader instruction changes through the central skill-learning review queue.
- Only promote specific, reusable, evidence-backed lessons into `LEARNED.md`.
