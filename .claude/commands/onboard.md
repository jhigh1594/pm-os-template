---
description: Run the onboard workflow
---
# PM-OS / AIPMOS Onboarding

Portable setup for a PM Operating System workspace: **human context first**, then **wire the repo** so `/today` and the rest of AIPMOS work. **Onboarding is exactly four steps** — no fifth onboarding phase; deeper work uses normal commands afterward.

---

## Design principle

**Durable (job-to-job):** craft, working style, how the human plans and communicates — mostly Step 1, easy to re-seed when switching employers.

**Tenant (this job):** company name, products, stakeholders, keys, task tracker — Steps 2–4. On the next role, refresh Step 1–2 content and re-run Step 3–4 for new tools and credentials.

---

## Step 1 — Role, company, goals, working preferences

**Discover (ask in one pass, keep answers tight):**

- Name and title; **company**; **products or areas owned** (short list)
- **This quarter:** 1–3 **outcomes** (outcome-shaped, not a backlog dump)
- **Stakeholders** who matter for decisions or narrative (names + roles; skip “manager” unless it helps)
- **Working preferences:** planning rhythm (daily anchor vs weekly), writing vs live alignment, async defaults, what creates leverage vs drain, anything agents should not do

**Produce:**

- `GOALS.md` — identity, portfolio table, quarter goals, stakeholder table
- `🤖 AI/memory/memory.md` — current focus, **Working preferences** subsection (so agents respect how the human works), product blurbs if useful
- Do **not** deep-dive full ICP per product here; that belongs in `/discover` or product folders later

---

## Step 2 — Strategy and proof in the workspace

**Discover:**

- Where **initiatives** should live (default: `📦 Products/<product>/initiatives/<initiative>/`)
- **One active initiative** to anchor the first week (name + rough goal)
- **Success signals** for the quarter (even qualitative)

**Produce:**

- Scaffold initiative folder if needed; optional `exploration-notes.md` only if scope is still fuzzy (see `AGENTS.md` / scratch rules)
- Tighten `GOALS.md` so goals are **observable** where possible
- Update memory with **active initiative** and **open decisions / strategic questions**

---

## Step 3 — Daily loop: `/today` and task source of truth

**Discover:**

- **Canonical task / project system** for *assigned work*: Jira, Linear, Asana, GitHub Issues, Monday.com, AgilePlace, other, or **none yet**
- **Name variants** as they appear on assignees (for `profile.owner_names` in `🔧 Automation/scripts/today_cmd/config.yaml`)
- **Stub mode:** if none yet — use `task_tracker.type: stub`; ask whether **example tasks** are OK or empty list
- **Slack delivery** for `/today` output: on or off (if on, point to env vars documented in that config)

**Produce:**

- Edit `🔧 Automation/scripts/today_cmd/config.yaml`: `task_tracker` (type + adapter fields per template comments), `profile.owner_names`, `delivery.slack` as chosen
- Add a short **Setup note** in memory or `GOALS.md` (optional) listing **where** API keys live (`.env` only, never committed) and **which** env vars the chosen adapter needs

---

## Step 4 — Connectors, keys, first closed loop

**Discover:** what the human can set **now** vs document for later (locked-down laptops are common).

**Must address:**

- **`GOOGLE_API_KEY`** — required for LLM-backed parts of `/today` (analysis, synthesis); without it, `/today` degrades
- **`GENAIPM_EMAIL`** (or `genaipm.email` in config) — **required** for the mandatory **One Step Better** section in `/today` (see `.claude/skills/menkesu-awesome-pm-skills-one-step-better-ai-pm/`); free subscription at https://genaipm.com
- **Granola / meetings** — enable paths in `config.yaml` if used; otherwise leave documented for later
- **Slack SMTP** — only if Step 3 enabled Slack

**Produce:**

- `.env` or `.env.example` aligned with the above (no secrets in repo)
- Run **`/today dry`** once to validate the pipeline without Slack if possible; if the human prefers, stop at “run `/today` when you’re ready”

**Complete onboarding:** confirm all four steps done, then **`/today`** daily.

---

## After onboarding (not a fifth step)

**Idea-to-delivery lifecycle** — pick up when the human has a real initiative:

| Step | Command | When |
|------|---------|------|
| 1 | `/brainstorm` | Exploring a problem or idea |
| 2 | `/discover` | Validating customer problems |
| 3 | `/spec` (one-pager) | Early alignment |
| 4 | `/spec` (full PRD) | Ready to specify |
| 5 | `/design-brief` | Handoff to design |
| 6 | `/story` | Backlog |
| 7 | `/spec-brief` | Eng handoff |
| 8 | `/ship` | Launch |
| 9 | `/learn` | Post-launch |

**Useful commands:** `/today`, `/think`, `/granola`, `/spec`, `/refresh-memory`, `/compete`

**CLAUDE.md / Ruler:** if the repo uses Ruler, prefer editing `.ruler/AGENTS.md` and running `ruler apply` instead of hand-editing generated `CLAUDE.md`.

---

## Constraints

- **Four steps only** for onboarding; do not add a fifth onboarding phase
- **Keep it simple** — iterate later via `GOALS.md` and memory
- **Portable** — make it obvious what to replace when changing jobs (company, products, keys, tracker)

---

## Agent handoff

Start Step 1 by asking for the Step 1 discovery block in one message. Complete each step’s outputs before moving on. After Step 4, give a short checklist of what was written and the **next command** to run (`/today`).
