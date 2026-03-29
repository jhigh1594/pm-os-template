# Product Coaching Wrapper

**Usage:** `/coach [--mode doc|decision|roadmap|research|comms] [--depth quick|full] [artifact-or-text]`

`/coach` is the fast Claude Code wrapper for the canonical `product-coach` skill.

Canonical skill contracts:
- Codex source: `/Users/jhigh/.codex/claude/skills/product-coach/SKILL.md`
- Workspace Claude mirror: `/Users/jhigh/Planview Work/.claude/skills/product-coach/SKILL.md`
- Cursor mirror: `/Users/jhigh/Planview Work/.cursor/rules/skills/product-coach/SKILL.md`

Runtime-backed coaching state:
- Presets: `/Users/jhigh/Planview Work/🤖 AI/coaching/scorecard-presets.yaml`
- Growth profile: `/Users/jhigh/Planview Work/🤖 AI/coaching/growth-profile.json`
- Scorecard history: `/Users/jhigh/Planview Work/🤖 AI/coaching/history/scorecards.jsonl`
- Revision deltas: `/Users/jhigh/Planview Work/🤖 AI/coaching/history/revision-deltas.jsonl`

## Wrapper Contract

When `/coach` is invoked:
1. delegate to the `product-coach` skill behavior
2. preserve the same artifact preset selection rules
3. preserve the same human-readable scorecard format
4. append the same machine-readable JSON block
5. keep stable dimension names so the runtime can persist reviews and compare revisions

## Arguments

- `--mode <mode>`: `doc`, `decision`, `roadmap`, `research`, or `comms`
- `--depth <depth>`: `quick` or `full`
- `artifact-or-text`: repo file, pasted draft, generated output, or artifact summary

Defaults:
- `mode = doc`
- `depth = quick`

## Best Uses

Use `/coach` when you want:
- a scored PM artifact review
- a revision plan with concrete edits
- sharper pushback on trade-offs and assumptions
- PM teaching that improves the next artifact too

Typical handoffs:
- after `/spec` -> `/coach --mode doc --depth full`
- after `/think` or `/prioritize` -> `/coach --mode decision`
- after a roadmap narrative -> `/coach --mode roadmap --depth full`
- after research synthesis -> `/coach --mode research`
- after an exec memo or update -> `/coach --mode comms`

## Notes

- The skill is the behavioral source of truth.
- This command exists for speed and ergonomics inside Claude Code.
- Persistence, growth-memory updates, and revision-delta logic live in the runtime, not in this wrapper.
