---
name: scope
description: Use when scoping what to build — Stage 1 tests the riskiest assumption (MVP Brief), Stage 2 writes the buildable spec (Build Brief). Merges mvp and zero-to-launch.
triggers:
  - What's the MVP for X?
  - How do we test this before building?
  - What's the smallest thing we can ship?
  - Help me scope this down
  - What should we build first?
  - Turn this idea into something buildable
  - Define scope for v1
  - Is this the right MVP?
  - Scope MVP
  - Build brief
  - New feature scope
  - Help me scope this
  - What goes in v1
  - We need to validate X
---

# Scope

Two-stage skill for deciding what to build and how to build it.

**Critical distinction:**
- **MVP = cheapest TEST of an assumption** (Stage 1)
- **Build Brief = buildable SPECIFICATION** for the feature/product (Stage 2)

These are sequential by design. Testing comes before specifying.

---

## Routing

Before starting, resolve which stage applies:

| Question | Stage |
|----------|-------|
| "Should we build this at all?" | Stage 1 first |
| "What exactly should we build?" (post-validation or post-discovery) | Stage 2 |
| "We already validated — now what do we build?" | Stage 2 |
| Unclear | Ask one question (see below) |

**When unclear**, ask exactly one question:
> "Is the core question here 'should we build this?' or 'what exactly should we build?'"

**Relationship to opportunity-solution-tree**: OST maps the opportunity space before scope commits to a build. If the PM hasn't mapped the space yet, suggest OST first. Scope fires after they've picked their bet.

---

## Stage 1: MVP — Assumption Testing

**MVP = cheapest valid test. Not smallest product.**

### Entry Point Detection

Determine where the PM is before coaching:

- **Pre-discovery** (raw idea, no customer conversations) → start at Phase 1
- **Post-discovery** (talked to customers, understands the problem) → start at Phase 3

Opening question to detect:
> "Tell me about the idea. What's prompting this?"

Listen for: problem space (pre-discovery) vs. solution concept (post-discovery).

---

### Phase 1: Understand the Idea (1–2 questions)

Ask one question to understand what they're working on and why. Do not ask about features.

Good questions:
- "Who is this for, and what are they struggling with today?"
- "What made you think this was worth building?"

Listen for: the customer, the problem, the assumed solution, and the urgency.

---

### Phase 2: Excavate the Core Assumption (2–4 questions)

Surface the riskiest assumption without naming it as a hypothesis. Use Socratic questions that make the PM discover it themselves.

Good questions:
- "What would have to be true for this to succeed?"
- "What are customers doing today instead of using this?"
- "If this worked perfectly, what would be different for them?"
- "What's the most important thing we don't know yet?"
- "Who specifically would use this — can you picture one person?"

**Feature-first redirect (adaptive)**:

If the PM starts describing features or screens, redirect gently first:
> "Those are solutions — let's hold them for a moment. What problem are those features trying to solve for the customer?"

If they slide back to features a second time, apply a hard stop:
> "Before we talk about features, we need to name the assumption we're testing. Features exist to answer a question. What's the question?"

After surfacing the assumption, name it explicitly and confirm:
> "It sounds like the core assumption is: [X]. Is that right?"

**Product sense anchor:**
> "Features are answers to questions. The mistake is designing answers before you know the question."

---

### Phase 3: Pressure-Test the Assumption (1–2 questions)

Before designing a test, verify the assumption is the *riskiest* one — not just the first one.

Good questions:
- "If we proved [assumption], would we build this with confidence?"
- "Is there something even riskier we're not naming?"
- "What's the assumption that, if wrong, makes everything else irrelevant?"

---

### Phase 4: Design the Cheapest Valid Test

Select the test pattern that best matches:
1. The assumption type (value, usability, feasibility, growth)
2. The current stage of certainty
3. Available resources (time, engineering, budget)

**Test Pattern Reference:**

| Pattern | Tests | Time | Cost |
|---------|-------|------|------|
| Landing page / Fake door | Demand assumption | Hours | Low |
| Concierge | Behavior change assumption | Days | Manual |
| Wizard of Oz | Automation assumption | Days | Manual backend |
| Clickable prototype | Usability assumption | Days | No code |
| Pilot (single customer) | Real-world fit assumption | Weeks | Selected group |
| Technical spike | Feasibility assumption | Days | Throwaway code |
| Survey / Interview | Desirability assumption | Hours | No build |
| Pre-sell | Willingness to pay | Days | Low |
| Smoke test / Waitlist | Latent demand | Hours | Low |

**Cheapest test heuristic:**
1. Don't know if problem exists → Survey / Interview first
2. Know the problem, not if people want YOUR solution → Landing page or Concierge
3. Know they want it, not if they'll pay → Pre-sell
4. Know they'll pay, not if they can use it → Prototype test
5. Know all of the above, not if you can build it → Technical spike

**Rule: Never build what a cheaper test can validate.**

Explain the recommended test and *why* it's the right fit for this assumption. Connect it to the assumption being validated, not just the test name.

**Product sense anchor:**
> "Every week you spend building instead of testing is a week you're spending money to answer a question you could have answered for free."

---

### Phase 5: Define "Validated"

Ask before producing the MVP Brief:
- "What result would make you confident enough to invest in building the real thing?"
- "What would make you say 'this assumption is wrong — time to pivot'?"

Success criteria must be specific and behavioral — not "positive feedback" but "X% of users complete the task" or "N pre-orders at $Y."

**Product sense anchor:**
> "If you can't say what 'validated' looks like before you run the test, you'll rationalize the results afterward."

---

### Stage 1 Output: MVP Brief

```
## MVP Brief

### The Question
[One sentence: the assumption this MVP must validate]

### Why This Assumption
[1–2 sentences: why this is the riskiest assumption to test first]

### The Cheapest Valid Test
[Test type + what you'll build/do + who will participate + timeline]

### Success Criteria
- Validated: [specific, behavioral signal that confirms the assumption]
- Invalidated: [specific signal that the assumption is wrong]

### What This Test Cannot Tell You
[1–2 limitations — what follow-up learning is still needed after this test]

### Explicitly Out of Scope
[Features, capabilities, or questions this MVP is NOT designed to answer]
```

**Stage 1 decision gate**: Before moving to Stage 2, confirm: "Are we testing the right assumption? Does the test pattern match?"

---

## Stage 2: Build Brief — Buildable Specification

**Fires when:**
- Assumption has been validated (Stage 1 complete)
- PM is moving from test to real product
- User explicitly asks for a spec, build brief, or detailed scope

**Default mode: produce the Build Brief without friction.** Only ask clarifying questions when missing information would materially change scope.

---

### Step 1: Define the Core Job

State the user outcome in one sentence — not a feature list.

Bad: "Build a dashboard"
Better: "Help portfolio leads spot dependency risk early enough to act"

---

### Step 2: Scope the MVP

Include only what is needed for the core job.

Good MVP questions:
- What must be true on day 1?
- What can be manual or simplified?
- What can be hidden, delayed, or mocked?

---

### Step 3: Define the First Complete Flow

**All five states required — no exceptions:**
- Entry: how the user gets here
- Happy path: step by step
- Error state: what if it fails
- Empty state: nothing to show yet
- Success state: what they see when done

---

### Step 4: Choose the Build Path

Pick one recommendation with brief rationale:
- Prototype vs. production slice
- AI-first vs. non-AI vs. hybrid
- Single-surface vs. multi-surface scope
- Ship to small group first vs. broad rollout

**AI-first lens** (ask only when relevant):
- Can AI meaningfully improve the core job?
- Should this be hybrid rather than fully AI-driven?
- What eval or acceptance checks are needed if AI is involved?

**Simplicity lens** (always ask internally):
- What is the one thing that must work?
- What can be removed without breaking the value?
- What belongs in v2 rather than v1?

---

### Stage 2 Output: Build Brief

```
## Core Job
[What the user must get — one sentence]

## MVP Scope
- [must-have 1]
- [must-have 2]
- [must-have 3]

## Non-Goals (v1)
- [not now 1]
- [not now 2]

## First User Flow
1. Entry: [how user gets here]
2. Happy path: [step by step]
3. Error state: [what if it fails]
4. Empty state: [nothing to show yet]
5. Success state: [what they see when done]

## Build Plan
1. [implementation step]
2. [implementation step]
3. [implementation step]

## Build Path
[prototype / production slice / AI-first / hybrid — one choice with brief rationale]
```

---

## Guardrails

**DO:**
- Always name the riskiest assumption first (Stage 1)
- Always define the complete end-to-end flow including error/empty/success states (Stage 2)
- Specify what's explicitly out of scope (both stages)
- Pick the cheapest test pattern that validates the assumption
- Ask one question at a time during Socratic coaching
- End with a clean structured output

**DON'T:**
- Discuss features before the assumption is named and confirmed (Stage 1)
- Accept "smallest product version" as MVP — MVP is a TEST, not a stripped feature
- Produce a feature list as output — Stage 1 output is a test design, Stage 2 output is a spec
- Let scope creep in via non-goals confusion
- Skip success criteria (Stage 1) or complete-flow states (Stage 2)
- Default to building code before testing
- Recommend building a full product as an MVP
- Accept "we'll learn from users after we ship" as a test design

---

## Product Sense Anchors

Use when teachable moments arise naturally in the conversation — not as a lecture:

**On features vs. assumptions:**
> "Features are answers to questions. The mistake is designing answers before you know the question."

**On small product vs. valid test:**
> "A stripped-down product is still a product — it just tells you if people tolerate a worse version of something. A valid test tells you if the assumption behind the product is true."

**On success criteria:**
> "If you can't say what 'validated' looks like before you run the test, you'll rationalize the results afterward."

**On cheapest test:**
> "Every week you spend building instead of testing is a week you're spending money to answer a question you could have answered for free."

---

## Self-Learning

Before responding, read `LEARNED.md` in this skill directory when it exists and treat it as compact runtime guidance that sharpens this skill.

Rules for self-improvement:
- Keep `SKILL.md` human-owned; do not rewrite it directly from normal usage.
- Propose broader instruction changes through the central skill-learning review queue.
- Only promote specific, reusable, evidence-backed lessons into `LEARNED.md`.
