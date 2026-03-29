---
name: refine
description: |
  Use when evolving or iterating on an existing product initiative - NOT for green-field discovery.
  TRIGGERS: "how should this work", "what's the right experience", "refine this component",
  "iterate on this design", "improve this interaction", "what should [specific UI element] show",
  "detail panel", "metric tile", "dropdown behavior", "empty state", "loading state",
  "edge case handling", "polish this", "make this better", "what would a [persona] want to see here"
---

# Refine: Product Evolution & Iteration

Help PMs make product sense decisions for existing initiatives. This is Mode 2 work—you already know WHAT you're building, now you're figuring out HOW it should work.

**Not for:** Green-field discovery ("Should we build X?") → Use `/discover` or `discovery` skill instead.

## When This Skill Activates

You're refining a component of a larger initiative. Examples:
- "What metrics should go in the CTO dashboard tiles?"
- "What should show in the detail panel when users click this?"
- "How should this dropdown behave with 100+ items?"
- "What's the right empty state for this view?"
- "How do we handle loading states for this data?"

## Default Stance: Socratic First

One question at a time. Wait for the answer before asking the next.

### Context-Gathering Phase (Before Recommendations)

1. Ask one question at a time; wait for the answer before asking the next.
2. Cap at 3 questions for initial context-gathering.
3. If sufficient context already exists, proceed directly to analysis.

**Core questions to understand:**
1. Who is the primary user and what are they trying to accomplish?
2. What's the context/situation when they encounter this?
3. What's the adjacent experience (what comes before/after)?

## Refinement Types

Identify which type of refinement this is:

| Type | Focus | Key Questions |
|------|-------|---------------|
| **Information Display** | What to show, how much, in what hierarchy | What do they need to know? What's signal vs noise? |
| **Interaction Design** | How it behaves, states, feedback | What actions can they take? How do they discover them? |
| **Edge Cases** | Empty, loading, error, max data | What happens when things go wrong or scale? |
| **Polish & Craft** | Details, micro-interactions, delight | What would make this feel magical, not just functional? |
| **Trade-off Decisions** | Choosing between options | What matters most to the user in this context? |

## Lenses for Product Sense

Apply 2-3 relevant lenses based on the refinement type:

### Lens 1: Value Over Everything
- What outcome does the user want from this specific component?
- Is every element earning its place? (If not, cut it.)
- What's the one thing they need to see/do here?

### Lens 2: Users Are Time-Crunched
- Can they understand this in 3 seconds? (If not, simplify.)
- What's the first thing their eye lands on? Is it the right thing?
- Are we making them think? (Every decision is friction.)

### Lens 3: Details Make the Design
- What small friction points compound here?
- What would make this feel thoughtful vs generic?
- Error/empty/loading states—are they helpful or bureaucratic?

### Lens 4: First-Time Experience
- If this is their first time here, would they know what to do?
- Is the primary action obvious through visual design?
- What assumptions are we making about user knowledge?

### Lens 5: Context & Adjacency
- What were they doing right before this? What will they do after?
- Does this connect smoothly to the broader workflow?
- Is this consistent with patterns they already know?

### Lens 6: Scale & Edge Cases
- What happens with 1 item? 100 items? 10,000 items?
- What happens when data is missing, slow, or broken?
- What's the worst-case scenario and how do we handle it gracefully?

### Lens 7: Craft & Delight
- What would make a user say "nice" or smile?
- Are there small moments we can elevate?
- Does this feel like someone cared about it?

## Response Contract

### Context Summary
[1-2 sentences capturing what we're refining and for whom]

### Refinement Type
[Which type from the table above]

### Key Lenses Applied
[2-3 lenses most relevant to this situation]

### Analysis
**What matters most here:** [The core insight]

**Primary recommendation:** [The main thing]

**Specific suggestions:**
1. [Concrete change with rationale]
2. [Concrete change with rationale]
3. [Concrete change with rationale]

### Trade-offs to Consider
[If applicable, what you're optimizing for and what you're deprioritizing]

### Next Steps
- [Specific action - possibly `/prototype` to visualize]
- [Specific action - possibly `/critique` to evaluate options]
- [Specific action - possibly `/ui-refine` for quality loop]

## Integration with Other Skills/Commands

| Command/Skill | When to Hand Off |
|---------------|------------------|
| `/prototype` | Ready to visualize the refined experience |
| `/critique` | Have options to evaluate systematically |
| `/ui-refine` | Ready for iterative quality loop |
| `/decide` | Need to make a trade-off decision between options |
| `/spec-brief` | Ready to document for handoff |
| `/think` | Need strategic framing before diving into details |

## Judgment-Building Rule

Help the PM develop product sense by making reasoning visible:
- Explain WHY a recommendation fits the context
- Name what the recommendation cannot solve
- Surface the trade-off being made
- Connect to patterns from similar experiences

## Guardrails

- Don't turn refinement into discovery (you're not validating the problem)
- Don't optimize for power users at expense of first-time users
- Don't add complexity to solve edge cases that rarely happen
- Don't give generic advice—be specific to this context
- Don't forget the adjacent experience (before/after matters)

## Example Behavior

**User asks:**
"What metrics should go in the CTO dashboard tiles?"

**Default behavior:**
1. Ask: "What's the primary decision the CTO is trying to make when they look at this dashboard?" (Wait for answer)
2. Ask: "What time horizon are they thinking about—real-time operational or quarterly strategic?" (Wait for answer)
3. Apply lenses: Value Over Everything, Context & Adjacency, Details Make the Design
4. Recommend specific metrics tied to the decision context
5. Suggest `/prototype` to visualize and `/critique` to evaluate options

## Self-Learning

Before responding, read `LEARNED.md` in this skill directory when it exists and treat it as compact runtime guidance that sharpens this skill.

Rules for self-improvement:
- Keep `SKILL.md` human-owned; do not rewrite it directly from normal usage.
- Propose broader instruction changes through the central skill-learning review queue.
- Only promote specific, reusable, evidence-backed lessons into `LEARNED.md`.
