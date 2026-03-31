---
description: PM-OS / AIPMOS onboarding — four steps only
---

# /onboard

Portable setup: **Jon’s context first**, then **wire the repo** so `/today` and the rest of AIPMOS work. **Exactly four steps** — no fifth onboarding phase; deeper work uses normal commands afterward.

## Design principle

**Durable (job-to-job):** craft, planning rhythm, how Jon communicates — mostly Step 1; easy to re-seed when switching employers.

**Tenant (this job):** company, products, stakeholders, keys, task tracker — Steps 2–4. Next role: refresh Step 1–2 and re-run Step 3–4.

## The four steps

**1 — Role, company, goals, working preferences**  
Discover in one pass; produce `GOALS.md` and `🤖 AI/memory/memory.md` (include **Working preferences**). No full ICP deep-dive here — use `/discover` or product folders later.

**2 — Strategy in the workspace**  
Initiatives default: `📦 Products/<product>/initiatives/<initiative>/`. One active initiative to anchor week one; success signals for the quarter. Tighten goals to be observable; update memory with active initiative and open questions.

**3 — Daily loop: `/today` + task source of truth**  
Configure `🔧 Automation/scripts/today_cmd/config.yaml`: `task_tracker`, `profile.owner_names`, optional Slack. Stub + example tasks if no tracker yet. Document env vars for the chosen adapter (`.env` only).

**4 — Connectors and first closed loop**  
`GOOGLE_API_KEY` (LLM parts of `/today`), **`GENAIPM_EMAIL`** (mandatory **One Step Better** in `/today` — see `.claude/skills/menkesu-awesome-pm-skills-one-step-better-ai-pm/`, https://genaipm.com). Granola / Slack as needed. Align `.env` / `.env.example`; run **`/today dry`** when ready.

**Done:** confirm all four steps, then use **`/today`** daily.

## After onboarding (not a fifth step)

Idea-to-delivery lifecycle (`/brainstorm` → `/discover` → `/spec` → … → `/learn`) — pick up when Jon has a real initiative. Full command list: `.claude/commands/onboard.md`.

**Ruler:** If the repo uses Ruler, edit `.ruler/AGENTS.md` and run `ruler apply` instead of hand-editing generated `CLAUDE.md`.

## Agent handoff

Start Step 1 with the Step 1 discovery block in **one** message. Complete each step’s outputs before moving on. After Step 4, give a short checklist and point Jon to **`/today`**.

**Full spec:** `.claude/commands/onboard.md`
