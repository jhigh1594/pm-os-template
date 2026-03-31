# Skill Review

**Use when**: Jon wants to review degraded or stale skills, inspect the weekly report, propose amendments to underperforming SKILL.md files, or promote LEARNED.md entries. Also triggers on "review skills", "skill health", "what skills are degraded", "skill report", "improve skill", "amend skill", "skill learning report", or "what's in the review queue".

## What this skill does

Reads the skill learning review queue and weekly report, surfaces skills that need attention, and helps Jon propose targeted amendments grounded in execution evidence — keeping Jon in control of every change before it's written.

## Workflow

### Step 1 — Load the review queue

Read `🤖 AI/skills/review-queue/` for the most recent weekly maintainer report and any pending proposal files. If the directory is empty or no report exists yet, say so and offer to run the weekly cycle manually.

```bash
# Run manually if needed
cd "🔧 Automation/scripts" && \
  PYTHONPATH="." \
  /path/to/.venv/bin/python -m skills_learning weekly \
  --workspace /path/to/workspace
```

### Step 2 — Summarize health status

Present a concise table:

| Skill | Score | Signal | Proposal | Action needed |
|-------|-------|--------|----------|---------------|
| `product-coach` | 4.1/5 | success | no change | None |
| `research` | 2.8/5 | retry_loop | SKILL.md rewrite | Review |
| `sample-deck` | 3.1/5 | tool_error | LEARNED-only | Promote lesson |

Focus on skills with `recommended_action` of `SKILL.md rewrite` or `LEARNED-only` first.

### Step 3 — Inspect a specific skill (on request)

When Jon picks a skill to investigate:

1. Read the proposal file from the review queue
2. Read the current `SKILL.md`
3. Read the current `LEARNED.md` (if it exists)
4. Read the last 3-5 run records from `🤖 AI/skills/runs.jsonl` for that skill_id
5. Summarize: what signals dominated, what errors occurred, what the proposal recommends

### Step 4 — Propose an amendment

Based on evidence, draft a targeted change. Follow these rules:

- **LEARNED.md entries**: Specific, reusable, evidence-backed lessons (1-2 sentences max). Write directly to `LEARNED.md` only after Jon approves.
- **SKILL.md patches**: Propose as a diff-style block. Never rewrite the full SKILL.md — only the section that caused failures. Jon must explicitly approve before any SKILL.md edit.
- **Trigger tightening**: If a skill is selected too often or for wrong tasks, propose a narrower trigger description.

Amendment types by signal:
- `retry_loop` → Add a recovery step or clarify ambiguous instructions
- `tool_error` → Add prerequisite checks or auth guidance
- `user_correction` → Tighten scope or clarify output format
- `positive_reinforcement` → No change needed; note what's working

### Step 5 — Write approved changes

After Jon approves:
- For LEARNED.md: append the entry using the standard format (date, lesson, source signals)
- For SKILL.md: apply only the approved patch using StrReplace
- Update the proposal file status to `resolved` by appending a resolution note

## LEARNED.md entry format

```markdown
<!-- {ISO_DATE} | signals: {signals} | confidence: {confidence} -->
- {lesson}
```

Example:
```markdown
<!-- 2026-03-17 | signals: retry_loop | confidence: 0.72 -->
- After a weak first pass on positioning work, restate the constraint before continuing rather than retrying the same approach.
```

## Self-Learning

Before responding, read `LEARNED.md` in this skill directory when it exists and treat it as compact runtime guidance that sharpens this skill.

Rules for self-improvement:
- Keep `SKILL.md` human-owned; do not rewrite it directly from normal usage.
- Propose broader instruction changes through the central skill-learning review queue.
- Only promote specific, reusable, evidence-backed lessons into `LEARNED.md`.
