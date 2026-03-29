---
name: research
description: Use when needing evidence, validation, or grounded read on market, competitor, or product idea. Triggers: research this, validate assumption, market research, competitor research, evidence for decision, what do we know about.
---

# Research

Use this skill when the user needs evidence, outside validation, or a grounded read on a market, competitor, customer problem, or product idea.

## Default Stance: Consultative First

In chat, start by clarifying what decision the research should support and what unknown matters most.

### Context-Gathering Phase (Required Before Action)

Before recommendations, analysis, or output, gather context related to the task, goal, or ask:

1. Ask the user one question at a time; wait for the answer before asking the next.
2. Cap at 3 questions for the initial context-gathering phase.
3. If the user has already provided sufficient context in their initial message, ask at most 1–2 questions or proceed directly to action.
4. Once context is gathered, proceed to substantive response and continue the iterative collaborative approach.

Default flow:
1. gather context (see Context-Gathering Phase above)
2. reflect back the research brief in 1-2 lines
3. gather the smallest high-signal source set that can answer it
4. synthesize findings into a provisional readout
5. suggest the next research or decision step

If the user already gave enough context, ask at most 1-2 questions and still provide a provisional read in the same response.

## Response Contract

For normal chat, default to:

```markdown
## Decision This Research Supports
[brief framing]

## Questions to Sharpen It
1. [question]
2. [question]
3. [question]

## Most Important Unknown
[what we need to learn]

## Provisional Read
[main finding or current take]

## Confidence / Next Step
- [what feels solid]
- [what still needs verification]
```

Include sources when the response relies on external evidence.

## Full Research Mode

Switch to full research mode when:
- the user explicitly asks for comprehensive research
- the decision is high stakes or expensive
- the source set is large and needs structured synthesis
- the output needs to become a memo, brief, or reusable artifact

Even then:
- lead with the decision, unknown, and current answer
- expand only into the evidence needed to support the recommendation

## Research Lenses

Use only the lenses that matter:
- what decision this research should change
- freshness requirements
- primary vs secondary source quality
- what counts as evidence vs interpretation
- what uncertainty still remains after the first pass

## Judgment-Building Rule

Help the PM become a better researcher:
- explain why a source is strong or weak
- distinguish fact, pattern, and inference
- show where more research stops being valuable

## Source Priorities

Prefer sources in roughly this order when relevant:
- official docs, filings, earnings calls, pricing pages
- product pages and release notes for factual capability checks
- trusted third-party reviews and analyst material
- customer voice sources such as reviews, forums, and discussion communities
- local workspace docs, research notes, and product context

Use vendor marketing pages mostly for positioning and messaging, not truth claims.

## Internal Context

When local context matters, prefer:
- `🤖 AI/memory/memory.md`
- `🤖 AI/patterns/learned-patterns.md`
- product strategy docs
- competitive analysis docs
- customer research and meeting notes that are actually present in the workspace

## Guardrails

- Do not ask more than 3 questions up front.
- Do not start with a research plan when a quick answer is enough.
- Do not treat vendor claims as facts.
- Do not keep gathering sources after the answer is already stable.
- Do not fake certainty when the evidence is thin.

## Example Behavior

If the user asks:
"What should we learn before deciding whether to invest here?"

Default behavior:
- ask what decision is on the table
- clarify the most important unknown
- gather a small, current, high-signal source set
- summarize what appears true so far
- recommend the next learning or decision step

## Self-Learning

Before responding, read `LEARNED.md` in this skill directory when it exists and treat it as compact runtime guidance that sharpens this skill.

Rules for self-improvement:
- Keep `SKILL.md` human-owned; do not rewrite it directly from normal usage.
- Propose broader instruction changes through the central skill-learning review queue.
- Only promote specific, reusable, evidence-backed lessons into `LEARNED.md`.
