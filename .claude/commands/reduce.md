---
description: Removal audit — apply 7 reduction lenses to answer "what would you remove?"
---

# /reduce — Removal Audit

`/reduce` is the Claude Code wrapper for the `reduce` skill.

**Canonical skill:** `.claude/skills/reduce/SKILL.md`

When invoked, delegate to the reduce skill behavior, which applies **7 reduction lenses** (Rubin, Rams, Jobs, Ive, Strunk/White, McKeown, Graham) to any product artifact and produces a Removal Audit.

## Usage

`/reduce [paste artifact or describe what to audit]`

This skill answers one question only: **what would you remove?**

## Best Uses

- "Reduce this PRD section"
- "What would you remove from this feature spec?"
- "Run a ruthless edit on our onboarding flow"
- "What's bloat in this settings screen?"
- "Essentialism review of this feature list"
- "Cut this down to the essentials"
- "What's the minimum version of this?"
- "Simplify this — what goes?"

## Notes

- The skill is the behavioral source of truth.
- This command exists for speed and ergonomics inside Claude Code.
- After a reduction audit, chain to `/spec` to rewrite the artifact with cuts applied.
- Pairs with `/critique` (which adds/improves) for a complete review cycle.
- Use `/product-taste-intuition` to build the removal instinct over time.
