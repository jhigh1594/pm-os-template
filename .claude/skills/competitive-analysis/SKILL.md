---
name: competitive-analysis
description: Use when understanding competitors, comparing alternatives, or shaping product and positioning moves. Triggers: competitive analysis, deep dive on competitor, battlecards, competitive read, vs competitor, competitor comparison.
---

# Competitive Analysis

Use this skill when the user needs to understand a competitor, compare alternatives, or decide how competitive information should shape a product, positioning, pricing, or sales move.

## Default Stance: Consultative First

In normal chat, start by clarifying what decision the competitive read should inform.

### Context-Gathering Phase (Required Before Action)

Before recommendations, analysis, or output, gather context related to the task, goal, or ask:

1. Ask the user one question at a time; wait for the answer before asking the next.
2. Cap at 3 questions for the initial context-gathering phase.
3. If the user has already provided sufficient context in their initial message, ask at most 1–2 questions or proceed directly to action.
4. Once context is gathered, proceed to substantive response and continue the iterative collaborative approach.

Default flow:
1. gather context (see Context-Gathering Phase above)
2. reflect back the real competitive question in 1-2 lines
3. gather or use the smallest high-signal source set that can answer it
4. provide a provisional read and implications
5. suggest the next move, response, or deeper follow-up

If the user already gave enough context, ask at most 1-2 questions and still provide a provisional view in the same response.

## Response Contract

For normal chat, default to:

```markdown
## Decision This Read Should Inform
[brief framing]

## Questions to Sharpen It
1. [question]
2. [question]
3. [question]

## Provisional Read
[main takeaway]

## What Matters
- [pattern or difference]
- [pattern or difference]
- [pattern or difference]

## Implications / Next Step
- [product, positioning, pricing, or sales move]
```

Use sources when making evidence-based claims, but do not make source collection the point of the response.

## Deep Mode

Use deep mode when:
- the user asks for a comprehensive competitor analysis
- the output needs to become a dossier or battlecard
- multiple competitors need systematic comparison
- the work informs a high-stakes strategic choice

Even in deep mode:
- frame the decision first
- lead with conclusions
- expand only into the evidence needed to support the call

## Competitive Lenses

Use only the lenses that matter:
- product capabilities and UX
- target customer and use case
- pricing, packaging, and GTM motion
- company signals and likely direction
- strategic position, differentiation, and risk

Frameworks like SWOT or positioning comparison are optional tools, not mandatory outputs.

## Judgment-Building Rule

Help the PM improve competitive judgment:
- separate signal from competitor theater
- explain why a difference matters or does not matter
- connect the read to a real decision, not just a description

## Evidence and Sources

Prefer:
- official docs, pricing pages, release notes, and product pages
- trustworthy third-party analysis
- customer review and discussion sources
- local competitive intelligence already present in the workspace

When current external information matters, use the current browsing/search tools available in the environment. Do not reference obsolete tool names.

Always:
- separate facts from interpretation
- cite sources for material claims
- use exact dates when recency matters
- label low-confidence findings clearly

## Internal Context

When workspace context matters, prefer:
- `🤖 AI/memory/memory.md`
- `🤖 AI/patterns/learned-patterns.md`
- product strategy and competitive analysis docs
- GTM and product context docs that are actually present in the workspace

## Guardrails

- Do not ask more than 3 questions up front.
- Do not confuse feature parity with customer value.
- Do not present vendor messaging as truth.
- Do not stay descriptive when the user needs a point of view.
- Do not force a deep dossier when a quick decision-oriented read is enough.

## Example Behavior

If the user asks:
"How should we assess [competitor] for this roadmap decision?"

Default behavior:
- ask what roadmap decision this comparison should inform
- clarify the most relevant lens
- provide a provisional competitive read
- explain what that means for [your product]
- recommend the next response or validation step

## Self-Learning

Before responding, read `LEARNED.md` in this skill directory when it exists and treat it as compact runtime guidance that sharpens this skill.

Rules for self-improvement:
- Keep `SKILL.md` human-owned; do not rewrite it directly from normal usage.
- Propose broader instruction changes through the central skill-learning review queue.
- Only promote specific, reusable, evidence-backed lessons into `LEARNED.md`.
