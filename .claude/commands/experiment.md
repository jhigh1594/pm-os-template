---
description: Design experiments and A/B tests — feature flags, guardrails, statistical significance, Kohavi frameworks
---

# /experiment — Experiment-Driven Development

**Canonical skill:** `.claude/skills/exp-driven-dev/SKILL.md`

Applies Ronny Kohavi's and Netflix/Airbnb experimentation culture to product decisions. Designs A/B tests with correct statistical rigor, sets up guardrail metrics, defines success criteria before building, and avoids the most common experimentation mistakes.

## Usage

`/experiment [feature or hypothesis to test]`

## Best Uses

- "Design an A/B test for the new onboarding flow"
- "What guardrail metrics should we track for this AgilePlace change?"
- "Is our sample size large enough to detect a 5% improvement?"
- "Build a feature flag rollout plan for dependency visualization"
- "What's the minimum detectable effect we should care about?"

## Notes

- Use before building — experiment design should happen at spec time, not after
- Pairs with `/measure` (metrics selection) and `/spec` (requirements)
- Distinct from `/measure` (which metrics to track) — this is how to test a hypothesis
