---
name: dex-improve
description: |
  Workshop AI OS improvements; track Claude Code, Claude Cowork, and Claude Desktop updates vs this repo; audit capabilities.
  TRIGGERS: "/dex-improve", "what's new in Claude Code", "Cowork updates", "Claude Desktop",
  "improve my AIPMOS", "capability audit", "upgrade hooks/skills", "platform evolution for this workspace"
---

# Dex-Improve (Planview AIPMOS)

Design partner for evolving this workspace's AI operating system: release awareness across **Claude Code**, **Claude Cowork**, and **Claude Desktop**, plus implementation planning and capability gaps.

**Not the same as** `/skill-review` (skill health / LEARNED.md pipeline via `skills_learning`). Use **dex-improve** for platform changelogs, hook architecture, and structured improvement plans.

## What This Skill Does

Three modes:

1. **Workshop an idea** — Shape a fuzzy improvement into a concrete plan tied to this repo.
2. **What's new?** — Compare recent releases for **Claude Code**, **Claude Cowork**, and **Claude Desktop** to `🤖 AI/aipmos/platform-state.json` and suggest adoptions for Planview AIPMOS (and Jon’s workflows where the repo is not the whole story).
3. **Full audit** — Inventory what is configured (`.claude/`, Cursor rules, Codex surfaces) vs common Claude Code capabilities; optionally contrast with how Jon uses Cowork / Desktop outside the repo.

**When to use**

- Jon has an idea but needs an implementation path.
- Jon asks what new **Claude Code**, **Cowork**, or **Claude Desktop** capabilities matter for this workspace or workflows.
- Jon wants a gap analysis of hooks, skills, MCP, rules.

**Invocation**

```
/dex-improve                           # Offer menu of modes
/dex-improve "idea or question here"   # Jump to Mode 1
```

---

## Entry Point

When invoked without a focused idea, offer:

```
How should Jon explore improvements?

1. **I have an idea** — Workshop a specific improvement
2. **What's new?** — Review **Claude Code**, **Claude Cowork**, and **Claude Desktop** changes since [last checks per surface in `platform-state.json`]
3. **Full audit** — Capabilities vs current usage in this repo

Or Jon can describe an idea and the workshop starts immediately.
```

If Jon already provided an idea in the message, skip to Mode 1.

---

## Mode 1: Workshop an Idea

**Input:** High-level description of what to improve.

### Phase 1: Understand

1. Identify affected areas:
   - Workflows (`/today`, tasks, Granola)
   - Automation (`🔧 Automation/scripts`, hooks)
   - Claude context (`.claude/`, `CLAUDE.md`, rules, skills)
   - Cursor context (`.cursor/rules/`, Cursor skills under `.cursor/rules/skills/`)
   - Codex context (`AGENTS.md`, `.codex/skills/`)
   - Memory and patterns (`🤖 AI/memory/memory.md`, `🤖 AI/patterns/learned-patterns.md`)
   - Product artifacts (`📦 Products/`, `📝 Docs/`)

2. State understanding in 2–3 sentences.
3. Note ambiguity; ask if blocking.

### Phase 2: Research + Internal Scan

**Always check**

- `🤖 AI/patterns/learned-patterns.md` — durable conventions
- `🤖 AI/memory/memory.md` — current focus (for scope only)
- `GOALS.md` — strategic alignment
- `.claude/commands/` — existing commands
- `.claude/skills/` — Claude skills
- `.claude/rules/` — scoped rules

**When relevant**

- `AGENTS.md`, `.codex/skills/` — Codex parity
- `.cursor/rules/` — Cursor-specific guidance
- `docs/sprints/claude-codex-context-engineering-modernization.md` — hook and instruction architecture decisions
- MCP: workspace `.mcp.json` / Cursor MCP config; `📝 Docs/Anvi/copilot-agents-main/mcp/` only if the change touches that code

**External (when needed)**

- **Claude Code:** `https://github.com/anthropics/claude-code/releases`, `docs.claude.com` / Claude Code docs
- **Claude Cowork:** `https://claude.com/docs` (Cowork section), `claude.com/product/cowork`, product blog / release posts when available
- **Claude Desktop:** Claude app release notes (Help, blog, or `claude.com` changelog if listed); features may overlap Cowork (Cowork ships in the desktop app context)

**Calibration:** Code has a single GitHub changelog. Cowork and Desktop may have **less centralized** release notes — use official Anthropic sources first; label **medium confidence** when inferring from secondary coverage.

Check: overlap with existing commands/skills; patterns to reuse.

### Phase 3: Capability Match (Planview)

Map requirement patterns to surfaces. Prefer **documented** platform features only; do not assume Codex hooks that do not exist.

| Requirement pattern | Suggested surface | Notes |
|---------------------|-------------------|--------|
| Every time a tool completes, follow-up | Claude `PostToolUse` hook | `.claude/settings.json` + hook script |
| Before tool use, gate or confirm | Claude `PreToolUse` hook | Same |
| Session start context | Claude `SessionStart` hook | Keep bounded; see sprint doc R2 |
| After compaction, restore slice | Claude `PreCompact` / resume flow | See sprint doc |
| Session end cleanup | Claude `SessionEnd` | e.g. `session-end.sh` |
| Prompt-time retrieval | Cue-triggered only | `UserPromptSubmit` + retrieval builder |
| Reusable multi-step workflow | Claude skill | `.claude/skills/<name>/SKILL.md` |
| User-triggered slash workflow | Claude command | `.claude/commands/<name>.md` |
| External tool integration | MCP | Workspace MCP configs |
| Cursor editor behavior | Cursor rules / skills | `.cursor/rules/` — not Claude hooks |
| Codex agent instructions | `AGENTS.md`, `.codex/skills/` | No unsupported lifecycle-hook emulation |

Present this table selectively (only rows that apply).

### Phase 4: Expand

Offer 2–3 adjacent improvements: compound wins, pillar/goal ties, links to gaps in `GOALS.md` or sprint doc.

### Phase 5: Refine

Max 2–3 questions at a time until requirements and acceptance criteria are clear.

### Phase 6: Plan + Write (after explicit confirmation)

1. Write the plan to `📚 Knowledge/Systems-and-Processes/improvement-plans/dex-improvement-<slug>.md` using the template below.
2. If Jon agrees, add durable one-liners to `🤖 AI/patterns/learned-patterns.md` (not noise).
3. Optional: if the idea is a simple task only, point to `📋 Tasks/backlog.md` instead of a full plan doc.

**Never** create or edit files beyond what Jon approves in this phase.

---

## Mode 2: What's New? (Claude Code, Cowork, Claude Desktop)

Run **three passes** in one response (unless Jon asks for only one surface). Each pass uses the same inner schema under `🤖 AI/aipmos/platform-state.json`.

### Surfaces (definitions)

| Surface | What it is | Primary sources for “what changed” |
|--------|------------|-------------------------------------|
| **Claude Code** | CLI / IDE extension agent (this repo’s `.claude/`, hooks, skills) | GitHub `anthropics/claude-code` releases; official Code docs |
| **Claude Cowork** | Anthropic agentic product for knowledge work (files, docs, spreadsheets, scheduled tasks); **research preview**; often used from **Claude Desktop** | `claude.com/docs` Cowork docs; product blog; in-app announcements |
| **Claude Desktop** | macOS / Windows Claude application (chat, projects, optional Cowork, voice, etc.) | App release notes; `claude.com` / Anthropic blog when versioned |

**Overlap:** Cowork and Desktop changelogs may **not** be cleanly separated — call that out when one update applies to both.

### Process (repeat per surface: `claude_code`, `cowork`, `claude_desktop`)

1. Read `🤖 AI/aipmos/platform-state.json`. If missing or empty, initialize with the schema below (all three keys).

2. **Fetch changelog:** Web search **official** sources for that surface since `last_check` for that key (if `last_check` is empty, summarize **recent** notable releases and treat as baseline).

3. **Compare:** New versions or features since `last_check` / `last_version_seen` for that key.

4. For each meaningful change:
   - Relevant to this PM workspace **or** Jon’s stated workflows?
   - **Claude Code:** tie to repo paths (hooks, skills, MCP).
   - **Cowork / Desktop:** tie to **habits** (e.g. file workflows, meetings, projects) and whether to mirror anything in `learned-patterns.md` or `GOALS.md` — the repo may not contain Cowork config.

5. **Present** (single combined message, three sections)

```
📢 Claude Code (since [claude_code.last_check])
=== NEW CAPABILITIES ===
...
=== SUGGESTED ADOPTIONS === (for this repo)
...

📢 Claude Cowork (since [cowork.last_check])
=== NEW CAPABILITIES ===
...
=== SUGGESTED ADOPTIONS === (workflows / habits; repo if applicable)
...

📢 Claude Desktop (since [claude_desktop.last_check])
=== NEW CAPABILITIES ===
...
=== SUGGESTED ADOPTIONS ===
...

Want to workshop any item? (surface + number)
```

6. **Update state file:** For **each** surface block Jon actually reviewed, set that key’s `last_check` to today (ISO date), bump `last_version_seen` if known, append to `features_noted` for novel items. If a surface had **no** trustworthy delta, still bump `last_check` and note `"no material public delta"` in one `features_noted` entry only if Jon wants to avoid re-querying noise.

### State file schema

**Path:** `🤖 AI/aipmos/platform-state.json`

```json
{
  "claude_code": {
    "last_check": "",
    "last_version_seen": "",
    "features_seen": [],
    "features_noted": []
  },
  "cowork": {
    "last_check": "",
    "last_version_seen": "",
    "features_seen": [],
    "features_noted": []
  },
  "claude_desktop": {
    "last_check": "",
    "last_version_seen": "",
    "features_seen": [],
    "features_noted": []
  }
}
```

Use `features_noted` entries like: `{ "version": "x.y.z or app build", "feature": "short label", "date_seen": "2026-03-24" }`.

**Legacy:** `claude-code-state.json` was replaced by this file; do not recreate it.

---

## Mode 3: Full Capability Audit

### Process

1. **Inventory**
   - `.claude/settings.json`, hooks, scripts referenced by hooks
   - `.claude/skills/`, `.claude/commands/`, `.claude/rules/`
   - `.cursor/rules/` (including `skills/` subtree)
   - `AGENTS.md`, `.codex/skills/`, `.codex/commands/` if present
   - `CLAUDE.md`, key `🤖 AI/` layout (memory, patterns, coaching, skills registry)

2. **Gap analysis** vs Claude Code capabilities (hooks, subagents, skills, commands, MCP).

3. **Optional (if Jon uses them):** Note where **Cowork** or **Claude Desktop** capabilities could complement repo work (e.g. file prep, research, scheduled tasks) without pretending those configs live in git.

4. **Output**

```
=== CAPABILITY AUDIT ===

Using well:
- [...]

Underused:
- [...]

Not used (or N/A for this repo):
- [...]

=== TOP RECOMMENDATIONS ===
(Ranked by impact vs effort)

1. [...]
```

Offer to workshop any item via Mode 1.

---

## Plan Document Template

Save as `📚 Knowledge/Systems-and-Processes/improvement-plans/dex-improvement-<slug>.md`:

```markdown
# Improvement: [Title]

**Created:** [date]
**Status:** Planning → In Progress → Complete
**Strategic anchor:** [GOALS.md section or goal name]

## Overview
[2–3 sentences]

## Requirements
- [ ] ...

## Capability analysis

| Requirement | Implementation | Surface | Rationale |
|-------------|----------------|---------|------------|

## Recommended approach
[Trade-offs]

## Implementation steps
### Phase 1
1. ...

## Files to create or modify

| File | Action | Purpose |
|------|--------|---------|

## Acceptance criteria
- [ ] ...

## Questions resolved
- Q: ... A: ...
```

---

## Behaviors

### Always

- Check internal patterns before inventing new machinery.
- Tie suggestions to `GOALS.md` and real repo paths.
- Update `🤖 AI/aipmos/platform-state.json` after Mode 2 (per surface reviewed).
- Explain why a feature fits before recommending it; distinguish **repo** (Code) vs **workflow** (Cowork / Desktop).

### Never

- Skip research when claiming a new platform capability.
- Recommend unsupported Codex lifecycle hooks.
- Write plans or edit durable docs without Jon's explicit approval.
- Confuse this skill with `/skill-review` or automated skill evaluation.

---

## Philosophy

Capability-aware design for this workspace only: ship what improves Jon's PM operating loop, nothing extra.
