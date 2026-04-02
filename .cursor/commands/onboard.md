---
description: PM-OS / AIPMOS onboarding — four steps only
---

# /onboard

Portable setup: **Jon’s context first**, then **wire the repo** so `/today` and the rest of AIPMOS work. **Exactly four steps** — no fifth onboarding phase; deeper work uses normal commands afterward.

## Design principle

**Durable (job-to-job):** craft, planning rhythm, how Jon communicates — mostly Step 1; easy to re-seed when switching employers.

**Tenant (this job):** company, products, stakeholders, keys, task tracker — Steps 2–4. Next role: refresh Step 1–2 and re-run Step 3–4.

## Interaction mode

**One question per assistant turn** — never dump a whole step’s survey in one message. After the last question in a step, **produce that step’s file outputs**, then start the next step. Full ordered question lists: `.claude/commands/onboard.md`.

## The four steps (summary)

**1 — Role, company, goals, working preferences**  
Sequential Q&A → `GOALS.md` and `🤖 AI/memory/memory.md` (include **Working preferences**). No full ICP deep-dive here — use `/discover` or product folders later.

**2 — Strategy in the workspace**  
Initiatives path, one active initiative, quarter success signals → scaffold/tighten repo + memory.

**3 — Daily loop: `/today` + task source of truth**  
Configure `🔧 Automation/scripts/today_cmd/config.yaml`: `task_tracker`, `profile.owner_names`, optional Slack. Stub + example tasks if no tracker yet. Document env vars for the chosen adapter (`.env` only).

**4 — Connectors and first closed loop**  
`GOOGLE_API_KEY`, **`GENAIPM_EMAIL`** (mandatory **One Step Better** in `/today` — see `.claude/skills/menkesu-awesome-pm-skills-one-step-better-ai-pm/`, https://genaipm.com). Granola / Slack as needed. Align `.env` / `.env.example`; run **`/today dry`** when ready.

**Done:** confirm all four steps, then use **`/today`** daily.

## After onboarding (not a fifth step)

Idea-to-delivery lifecycle (`/brainstorm` → `/discover` → `/spec` → … → `/learn`) — pick up when Jon has a real initiative. Full command list: `.claude/commands/onboard.md`.

**Ruler:** If the repo uses Ruler, edit `.ruler/AGENTS.md` and run `ruler apply` instead of hand-editing generated `CLAUDE.md`.

## Agent handoff

Start with **Step 1, question 1** only (see full spec). One question per message; write step outputs after each step’s questions; end with a checklist and **`/today`**.

**Full spec:** `.claude/commands/onboard.md`
