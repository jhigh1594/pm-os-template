---
description: 'Use when clarifying what to learn, which assumption matters most, or
  which discovery method to use next. Also use when building an ongoing discovery
  system, setting up weekly customer contact, mapping an opportunity solution tree
  (OST), or establishing a product trio workflow. Triggers: discovery plan, what to
  learn, user research method, customer interviews, assumption to test, validation
  approach, research design, Teresa Torres, continuous discovery, opportunity solution
  tree, OST, weekly touchpoints, discovery cadence, product trio, assumption testing
  hierarchy, problem-definition, is this a real problem, problem validation, symptom
  vs root cause, shiny object trap, problem worth solving, pre-mortem on problem framing,
  should we even investigate this.'
name: discovery
---

# Discovery

Use this skill when the user needs to clarify what to learn, which assumption matters most, or what discovery method should come next.

---

## Problem Validation Pre-Gate

Before designing any research, validate the problem statement itself. Wasted discovery starts with an unvalidated problem.

### The Problem-Definition Check

1. **Can you state the problem WITHOUT the solution?**
   If you mention AI, a platform, or technology, you have a solution in search of a problem. Stop.

2. **Is this a business problem or a customer problem?**
   - Business problem: what the company needs (e.g., "increase retention")
   - Customer problem: what the user needs (e.g., "I can't find notes across projects")
   Are they aligned? If in conflict, name it — the research design changes completely.

3. **Can you describe a specific struggling moment?** (Bob Moesta)
   Not "users struggle with X" but "last Tuesday, Jamie was in the middle of Y, trying to accomplish Z, and X got in the way." Without a specific moment, you have a hypothesis, not a problem.

4. **Can you describe the finished state?** (Ryan Singer — "see the end from the beginning")
   If you can't describe what life looks like when this is solved (not the feature — the experience), the problem is too fuzzy to research.

5. **Pre-mortem: What if we're wrong about this being a problem?**
   What would disconfirm your assumption? What evidence would tell you this isn't real?
   If you can't name what would change your mind, you're attached to the problem — not curious about it.

### Problem Worth Investigating? (Three-Criteria Test)
All three must be true:
- **Frequency:** How often does the struggling moment occur? (daily >> weekly >> monthly)
- **Pain intensity:** How much does it hurt? (<5 = nice-to-have; 8+ = real pain)
- **Workaround viability:** How hard is the current workaround? (harder = more pain = more worth solving)

If the problem fails this test, redirect discovery energy before investing further.

---

## Phase 0: Problem Definition (Entry Gate)

Before designing any research, confirm the team is investigating the right problem. Discovery applied to the wrong problem is expensive and misleading.

### Struggling Moment (Bob Moesta)

Demand originates from a specific struggling moment — not from a product, a feature idea, or a trend. Ask:

> "Walk me through the last time you experienced this problem. What were you doing right before? What were you trying to accomplish?"

- What is the user doing RIGHT BEFORE they hit the problem?
- What context were they in? (rushed, distracted, first time, mobile?)
- How were they feeling?

If the team can't answer this from specific observed stories — not opinions customers gave when asked — they don't have a problem worth investigating yet.

### Problem Type Qualification (Christopher Miller)

Not all business problems are customer problems. Distinguish them explicitly:

- **Business problem**: What does the business need?
- **Customer problem**: What does the user need?
- Are these aligned or in conflict?

A solution that serves the business but not the customer is customer-hostile. If there's a conflict, name it before proceeding.

### See the End from the Beginning (Ryan Singer)

Before committing to discovery:

> Can you draw the finished feature? Can you describe the exact user experience when the problem is solved?

If not, the problem isn't crisp enough to research productively. Discovery will generate noise, not signal.

### Shiny Object Trap Guardrail (Marilyn Nika)

> Can you state the problem without mentioning the technology?

If the answer is no — if the problem statement requires naming AI, a new platform, or a specific implementation — you're solution-first. Pause discovery until the problem is clear independent of the solution.

### Problem Statement Template

Use this to sharpen the problem before moving to research design:

```markdown
## The Struggling Moment
[Specific context where user experiences pain — what they were doing, feeling, trying to accomplish]

## Current Workarounds
- [What they do today] — Painfulness: [1-10]

## Problem Type
- [ ] Business problem: [what business needs]
- [ ] Customer problem: [what user needs]
- Aligned / In conflict: [explain]

## Riskiest Assumption
[What must be true for this to be a real problem worth solving]
```

---

## Default Stance: Consultative First

In chat, start by helping the user define the decision discovery should inform before recommending a method.

### Context-Gathering Phase (Required Before Action)

Before recommendations, analysis, or output, gather context related to the task, goal, or ask:

1. Ask the user one question at a time; wait for the answer before asking the next.
2. Cap at 3 questions for the initial context-gathering phase.
3. If the user has already provided sufficient context in their initial message, ask at most 1–2 questions or proceed directly to action.
4. Once context is gathered, proceed to substantive response and continue the iterative collaborative approach.

Default flow:
- **Phase 0**: Define the problem — struggling moment, problem type, riskiest assumption
- **Phase 1**: Design the research — decision-first framing, method selection
- **Phase 2**: Build cadence — ongoing discovery system (Teresa Torres, OST)

Within Phase 1:
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

- Do not jump to research methods before articulating the struggling moment.
- Do not design research around a solution — research should test whether the problem exists, not whether your solution works.
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



## What Makes This Skill Different

<!-- State what pushes Claude OUT of default behavior. What does a naive response miss? -->

## Self-Learning

Before responding, read `LEARNED.md` in this skill directory when it exists and treat it as compact runtime guidance that sharpens this skill.

Rules for self-improvement:
- Keep `SKILL.md` human-owned; do not rewrite it directly from normal usage.
- Propose broader instruction changes through the central skill-learning review queue.
- Only promote specific, reusable, evidence-backed lessons into `LEARNED.md`.
