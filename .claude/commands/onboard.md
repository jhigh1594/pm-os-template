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

## Interaction mode (required)

**One question per assistant turn.** Do not paste a multi-question survey or a whole step’s “Discover” list in a single message.

- Ask **exactly one** question from the sequences below, wait for the human’s reply, then ask the next.
- Keep prompts short; optional one-line context is fine.
- After the **last** question in a step, **produce that step’s outputs** before starting the next step’s first question.
- If the human volunteers multiple answers early, note them and still confirm anything missing **one item at a time**.

---

## Step 1 — Role, company, goals, working preferences

**Produce (after all Step 1 questions are answered):**

- `GOALS.md` — identity, portfolio table, quarter goals, stakeholder table
- `🤖 AI/memory/memory.md` — current focus, **Working preferences** subsection (so agents respect how the human works), product blurbs if useful
- Do **not** deep-dive full ICP per product here; that belongs in `/discover` or product folders later

**Step 1 — ask in this order (one message each):**

1. Name and current title?
2. Company?
3. Products or areas owned (short list)?
4. This quarter: what are 1–3 **outcomes** (outcome-shaped, not a backlog dump)?
5. **Stakeholders** who matter for decisions or narrative (names + roles; skip “manager” unless it helps)?
6. **Planning rhythm:** daily anchor, weekly anchor, or something else?
7. **Alignment style:** prefer writing, live conversations, or a mix? Default to async or synchronous?
8. What **creates leverage** vs **drains** the human? Anything **agents should not do** (topics, actions, tone)?

---

## Step 2 — Strategy and proof in the workspace

**Produce (after all Step 2 questions are answered):**

- Scaffold initiative folder if needed; optional `exploration-notes.md` only if scope is still fuzzy (see `AGENTS.md` / scratch rules)
- Tighten `GOALS.md` so goals are **observable** where possible
- Update memory with **active initiative** and **open decisions / strategic questions**

**Step 2 — ask in this order (one message each):**

1. Where should **initiatives** live? (Default if they skip: `📦 Products/<product>/initiatives/<initiative>/`)
2. **One active initiative** to anchor the first week — name and rough goal?
3. **Success signals** for the quarter (even qualitative) — what would “good” look like?

---

## Step 3 — Daily loop: `/today` and task source of truth

**Produce (after all Step 3 questions are answered):**

- Edit `🔧 Automation/scripts/today_cmd/config.yaml`: `task_tracker` (type + adapter fields per template comments), `profile.owner_names`, `delivery.slack` as chosen
- Add a short **Setup note** in memory or `GOALS.md` (optional) listing **where** API keys live (`.env` only, never committed) and **which** env vars the chosen adapter needs

**Step 3 — ask in this order (one message each):**

1. **Canonical task / project system** for assigned work: Jira, Linear, Asana, GitHub Issues, Monday.com, AgilePlace, other, or **none yet**?
2. **Name variants** as they appear on assignees (for `profile.owner_names` in `🔧 Automation/scripts/today_cmd/config.yaml`)?
3. If **none yet**: OK to use `task_tracker.type: stub` — prefer **example tasks** or an **empty** list?
4. **Slack delivery** for `/today` output: on or off? (If on, point to env vars documented in that config.)

---

## Step 4 — Connectors, keys, first closed loop

**Discover:** what the human can set **now** vs document for later (locked-down laptops are common).

**Must address (across the questions below):**

- **`GOOGLE_API_KEY`** — required for LLM-backed parts of `/today` (analysis, synthesis); without it, `/today` degrades
- **`GENAIPM_EMAIL`** (or `genaipm.email` in config) — **required** for the mandatory **One Step Better** section in `/today` (see `.claude/skills/menkesu-awesome-pm-skills-one-step-better-ai-pm/`); free subscription at https://genaipm.com
- **Granola / meetings** — enable paths in `config.yaml` if used; otherwise leave documented for later
- **Slack SMTP** — only if Step 3 enabled Slack

**Produce (after Step 4 questions are answered):**

- `.env` or `.env.example` aligned with the above (no secrets in repo)
- Run **`/today dry`** once to validate the pipeline without Slack if possible; if the human prefers, stop at “run `/today` when you’re ready”

**Step 4 — ask in this order (one message each):**

1. For API keys and connectors: what can the human set **on this machine now**, vs **document for later**?
2. **`GOOGLE_API_KEY`** — will they add it (and roughly when), or document-only for now?
3. **`GENAIPM_EMAIL`** (One Step Better in `/today`) — will they add it, or document-only for now?
4. **Granola** (or other meeting notes path): using it — yes, no, or later?
5. If Slack was enabled in Step 3: ready to configure **Slack SMTP** / delivery env vars now, or document for later?
6. Preference: run **`/today dry`** together now, or stop with “run `/today` when you’re ready”?

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

Open with the design principle in one short paragraph, then **start Step 1, question 1** only.

Rules:

- **One question per message** until that step’s question list is done, then write that step’s file outputs, then begin the next step’s question 1.
- Never ask for “the whole Step 1 block” or “everything for Step 3” in one message.
- After Step 4 outputs, give a short checklist of what was written and the **next command** to run (`/today`).
