---
name: zero-to-launch
description: Use when turning an idea, feature request, or rough concept into something buildable. Triggers: scope MVP, build brief, what to build first, turn idea into prototype, new feature scope, minimum viable product, help me scope this, what goes in v1.
---

# Zero to Launch

Use this skill when the user wants to turn an idea, feature request, or rough concept into something buildable.

## Default Mode: Build Brief

Default to a concise, operator-style build brief.

Start with:
1. **Core job** - the one outcome the user must get
2. **MVP scope** - what to build now
3. **Non-goals** - what not to build yet
4. **First user flow** - the minimum complete experience
5. **Implementation path** - how to ship the first version

Only ask clarifying questions when missing information would materially change scope.

## Deep Mode

Go deeper only when:
- the user asks for a full product breakdown
- the concept is ambiguous enough that scope would be reckless
- there are major strategic, design, or AI-product tradeoffs to resolve

## Response Contract

In normal chat, the first response should look like this:

```markdown
## Core Job
[What the product or feature must help the user do]

## MVP Scope
- [must-have 1]
- [must-have 2]
- [must-have 3]

## Non-Goals
- [not now 1]
- [not now 2]

## First User Flow
1. [step]
2. [step]
3. [step]

## Build Plan
1. [implementation step]
2. [implementation step]
3. [implementation step]
```

Do not begin with a framework lecture.

## Core Lenses

Use these as internal filters, not as the main performance:

### AI-first lens

Ask only when relevant:
- can AI meaningfully improve the core job?
- should this be hybrid rather than fully AI-driven?
- what eval or acceptance checks should exist if AI is involved?

### Simplicity lens

Always ask:
- what is the one thing that must work?
- what can be removed without breaking the value?
- what belongs in v2 rather than v1?

### Complete-flow lens

Make sure the first version covers:
- entry point
- happy path
- error state
- empty state
- success state

## Build Workflow

### Step 1: Define the job

State the user outcome in one sentence.

Bad:
- "Build a dashboard"

Better:
- "Help portfolio leads spot dependency risk early enough to act"

### Step 2: Scope the MVP

Include only what is needed for the core job.

Good MVP questions:
- what must be true on day 1?
- what can be manual or simplified?
- what can be hidden, delayed, or mocked?

### Step 3: Define the first complete flow

Describe the smallest end-to-end experience that still feels real.

### Step 4: Choose the build path

Recommend:
- prototype vs production slice
- AI vs non-AI implementation
- single-surface vs multi-surface scope
- what to ship to a small group first

## Guardrails

- Do not let the feature list replace the user job.
- Do not overbuild before validating the core workflow.
- Do not confuse "nice demo" with "useful product."
- Do not leave the first version with missing empty, error, or success states.
- Do not default to AI unless it clearly improves the experience or economics.

## Output Variants

### Variant: 1-week MVP

Use for:
- fast validation
- prototype scoping
- "what should we build first?"

Output:
- core job
- 3-5 must-haves
- 2-5 non-goals
- build steps

### Variant: build vs buy vs hybrid

Use for architecture or tool-choice decisions.

Output:
- recommendation
- tradeoffs
- what to validate first

### Variant: launch-ready v1 outline

Use when the user is beyond MVP scoping.

Output:
- core flow
- edge states
- rollout shape
- measurement

## Example Behavior

If the user asks:
"Help me define a 1-week MVP for a dependency risk alert workflow."

Default behavior:
- define the core job
- scope the smallest viable workflow
- list non-goals explicitly
- recommend the fastest build path

Do not start by teaching the OpenAI, Figma, and Airbnb frameworks.

## Self-Learning

Before responding, read `LEARNED.md` in this skill directory when it exists and treat it as compact runtime guidance that sharpens this skill.

Rules for self-improvement:
- Keep `SKILL.md` human-owned; do not rewrite it directly from normal usage.
- Propose broader instruction changes through the central skill-learning review queue.
- Only promote specific, reusable, evidence-backed lessons into `LEARNED.md`.
