# Execution & Delivery

Use this skill when the user needs help keeping roadmap work moving, unblocking delivery, or deciding what matters most in the current execution window.

## Default Mode: Execution Diagnosis

Default to a concise operator-style response.

Start with:
1. **Status read** - what looks on track, at risk, or blocked
2. **Priority focus** - what matters most right now
3. **Next actions** - 2-4 concrete moves
4. **Communication or escalation** - what to tell whom

Only ask clarifying questions first if the current delivery state is too ambiguous to give a useful recommendation.

## Deep Mode

Use deep mode when:
- the user wants a full delivery operating model
- quarter planning, cadence design, or recurring rituals are the main problem
- the issue spans multiple teams, milestones, or months

## Response Contract

For normal chat, default to:

```markdown
## Status
- [on track / at risk / blocked]

## What Matters Now
- [priority 1]
- [priority 2]

## Next Actions
1. [action]
2. [action]
3. [action]

## Escalations / Risks
- [risk or communication need]
```

Do not begin with a quarter-long planning workshop unless the user explicitly wants that.

## Execution Lenses

Apply only what is relevant:
- delivery risk
- dependency risk
- scope realism
- team capacity
- quality risk
- stakeholder confidence

Useful framing:
- what is blocking value?
- what can slip without breaking the outcome?
- what needs escalation now vs monitoring later?

## Workflow

### For current execution issues

Use for:
- slipping roadmap work
- unclear sprint priorities
- blocker triage
- status and escalation decisions

Process:
1. identify the current target and risk
2. isolate the highest-leverage unblocker
3. recommend the smallest useful set of next moves
4. state what to communicate upward or sideways

### For deeper operating support

Use for:
- cadence design
- quarter execution setup
- delivery system improvements
- recurring planning and review structures

Process:
1. define the operating horizon
2. map commitments, dependencies, and risk points
3. define cadence, ownership, and escalation paths
4. produce the operating plan

Even in deep mode, lead with the most important delivery call first.

## Internal Context

When workspace context matters, prefer:
- `🤖 AI/memory/memory.md`
- `🤖 AI/patterns/learned-patterns.md`
- roadmap, planning, and stakeholder docs in the workspace

## Guardrails

- Do not confuse activity with progress.
- Do not recommend more process when the real problem is priority or ownership.
- Do not hide schedule risk behind vague status language.
- Do not produce a large cadence template when the user needs an unblock plan.
- Do not escalate everything; name the few issues that truly need escalation.

## Output Variants

### Variant: weekly execution read

Use for:
- "Are we off track?"
- "What should I do this week?"

Output:
- status
- top risks
- next moves

### Variant: unblock plan

Use for:
- dependency problems
- slipping milestones
- overloaded teams

Output:
- blocker
- options
- recommended action
- owner or escalation

### Variant: operating model

Use when explicitly requested.

Output:
- cadence
- rituals
- ownership
- risk controls

## Example Behavior

If the user asks:
"We are slipping against the quarter plan. What should I do this week?"

Default behavior:
- call out the most important risk
- recommend the first few actions
- name any necessary stakeholder communication

Do not begin by asking for a full roadmap-management setup unless the user explicitly wants it.

## Self-Learning

Before responding, read `LEARNED.md` in this skill directory when it exists and treat it as compact runtime guidance that sharpens this skill.

Rules for self-improvement:
- Keep `SKILL.md` human-owned; do not rewrite it directly from normal usage.
- Propose broader instruction changes through the central skill-learning review queue.
- Only promote specific, reusable, evidence-backed lessons into `LEARNED.md`.
