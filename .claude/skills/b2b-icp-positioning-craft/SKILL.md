---
name: b2b-icp-positioning-craft
description: This skill should be used when defining or refining a B2B ICP, connecting discovery signal to positioning, or drafting strategic documents and messaging from ICP decisions in Claude Code. Trigger phrases include "draft an ICP brief", "refine this ICP", "analyze customer signal", "connect this to positioning", "write a positioning memo", and "turn discovery notes into messaging".
---

# B2B ICP Positioning Craft

## Overview

Develop a narrow, evidence-backed B2B ICP and connect it directly to positioning, qualification, and messaging.

Use this skill to turn broad market thinking into a focused segment choice, a clear champion-centered value story, and practical downstream assets for GTM work.

## Use This Skill When

Use this skill when the task involves any of the following:

- define or refine an ideal customer profile
- narrow a target segment
- identify the best champion or buyer
- determine what alternatives a buyer compares against
- translate product differences into buyer-valued outcomes
- connect discovery findings to positioning
- turn ICP thinking into qualification, messaging, or GTM assets

Do not use this skill for generic persona writing, broad TAM or market sizing work, or lightweight competitor summaries without an ICP decision at stake.

## Core Idea

Treat ICP as a focus decision, not a description exercise.

Treat positioning as the external expression of that focus.

Favor the smallest repeatable segment where:
- the pain is real
- the buyer or champion cares now
- the current product wins for a differentiated reason
- the signal comes from behavior, not polite interest

## Default Workflow

Follow this sequence unless the user explicitly asks for a narrower sub-task.

1. Clarify the decision.
- Determine whether the task is discovery, narrowing, validation, positioning, or asset creation.
- Identify what decision the output is meant to support.

2. Form an initial ICP hypothesis.
- Define 3-5 attributes only.
- Favor attributes like company size, role or champion, workflow, tech environment, trigger event, or buying context.
- Avoid broad firmographic-only ICPs.

3. Identify the champion.
- Determine who feels the pain first.
- Determine who makes the shortlist.
- Determine who can carry the deal internally.
- Separate the champion from stakeholders, influencers, and blockers.

4. Map the alternatives.
- Include the status quo explicitly.
- Include direct competitors, internal workarounds, and adjacent tools.
- Ask: "If this product did not exist, what would the buyer do?"

5. Assess signal quality.
- Prefer observed behavior over stated preference.
- Prefer outbound and clean-market signal over warm intros or friendly conversations.
- Use `references/signal-rubric.md`.

6. Run the "so what?" ladder.
- Start from features or capabilities.
- Ask "so what?" until the value lands in buyer-language business terms.
- Stop before the value becomes generic and interchangeable.

7. Separate value from objections.
- Keep reasons to buy distinct from reasons a buyer may hesitate.
- Do not force deployment, change management, or TCO concerns into core value themes unless the champion truly buys for those reasons.

8. Produce the output.
- Use the smallest template that fits the ask.
- Pull from `references/templates.md`.

## Output Contract

Default to producing the following when enough context exists:

- ICP hypothesis
- not-for segment
- champion definition
- alternative map
- signal assessment
- differentiated value themes
- positioning draft
- discovery or qualification follow-ups

If context is incomplete, still provide:
- a provisional hypothesis
- the biggest uncertainty
- the next 3 questions or data points needed

## Guardrails

Do not:
- define ICP by title alone
- confuse enthusiasm with buying signal
- trust warm-intro demand as primary evidence
- treat every stakeholder as equally important
- position against future-state product claims
- ignore the status quo
- turn every feature into a value theme
- broaden the segment before repeatable wins exist

## Bundled Resources

Use these bundled resources when they fit the task:

### Scripts

- `scripts/scaffold_icp_brief.py`
  - Generate a ready-to-edit ICP brief from the built-in structure.
  - Use when the work needs a concrete working document quickly.

- `scripts/so_what_ladder.py`
  - Turn a raw list of capabilities into a "so what?" worksheet.
  - Use when translating product details into buyer-language outcomes.

### Assets

- `assets/icp-signal-tracker.csv`
  - Copy when tracking segment signal across outbound, discovery, and deal review work.

- `assets/icp-interview-log.csv`
  - Copy when running repeated discovery interviews and needing a consistent log format.

## References

Read these only as needed:

- `references/method.md`
- `references/signal-rubric.md`
- `references/anti-patterns.md`
- `references/templates.md`
- `references/examples.md`
- `references/interview-prompts.md`

## Self-Learning

Before responding, read `LEARNED.md` in this skill directory when it exists and treat it as compact runtime guidance that sharpens this skill.

Rules for self-improvement:
- Keep `SKILL.md` human-owned; do not rewrite it directly from normal usage.
- Propose broader instruction changes through the central skill-learning review queue.
- Only promote specific, reusable, evidence-backed lessons into `LEARNED.md`.
