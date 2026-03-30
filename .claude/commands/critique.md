# Product Critique Framework

**Usage:** `/critique [--mode <1-4>] [product-or-feature]`

`/critique` is the Claude Code wrapper for the canonical `product-critique` skill.

**Canonical skill:** `.claude/skills/critique/SKILL.md`

When invoked, delegate to the product-critique skill behavior, which applies the **7-dimension framework** (First Impression, Getting Started, Core Experience, Value Delivery, Differentiation, Details & Craft, Overall Assessment) plus a quality-bar coaching gate.

## Modes

- `--mode 1` — User empathy (experience as a customer)
- `--mode 2` — Strategic (business and competitive lens)
- `--mode 3` — Quality bar (craft, polish, micro-interactions)
- `--mode 4` — Technical (performance, scalability, reliability)

Default: all 7 dimensions across all lenses.

## Best Uses

- "Critique our new onboarding flow"
- "Compare our product vs [Competitor X]"
- "Review this prototype before we build it"
- "What's the quality bar on our latest launch?"
- "Assess [well-known product] and identify what we can learn"

## Notes

- The skill is the behavioral source of truth.
- This command exists for speed and ergonomics inside Claude Code.
- After critique, chain to `/spec` to document improvements, or `product-coach` skill to score a PM artifact.
