# Dex-Improve Wrapper

**Usage:** `/dex-improve` or `/dex-improve "idea or question"`

`/dex-improve` is the Claude Code wrapper for the canonical `dex-improve` skill (AI OS improvements and release alignment for **Claude Code**, **Claude Cowork**, and **Claude Desktop**).

Canonical skill:
- Workspace: `.claude/skills/dex-improve/SKILL.md`
- Cursor mirror: `.cursor/rules/skills/dex-improve/SKILL.md`
- Codex mirror: `.codex/skills/dex-improve/SKILL.md`

State (Mode 2 — what's new):
- `🤖 AI/aipmos/platform-state.json` (`claude_code`, `cowork`, `claude_desktop`)

Plan output (Mode 1 — after Jon confirms):
- `📚 Knowledge/Systems-and-Processes/improvement-plans/dex-improvement-<slug>.md`

## Wrapper Contract

When `/dex-improve` is invoked:

1. Delegate to the `dex-improve` skill behavior (three modes: workshop, what's new, full audit).
2. Use Planview paths from the skill; do not use Dex vault paths (`System/`, `06-Resources/`, etc.).
3. For Mode 2, read and update `🤖 AI/aipmos/platform-state.json` (per surface).
4. For Mode 1, write plan files only after requirements are confirmed and Jon approves.

## Distinction

- **`/dex-improve`** — Platform evolution (Claude Code / Cowork / Desktop updates, hooks, skills architecture, implementation plans).
- **`/skill-review`** — Skill health via `skills_learning` (degraded skills, LEARNED.md, review queue).

## Best Uses

- Adopting new Claude Code capabilities in this repo; tracking Cowork and Desktop for workflow impact.
- Workshopping an AIPMOS change (hooks, rules, commands, memory flow).
- Periodic "what did we miss?" audits of `.claude/` vs official capabilities.
