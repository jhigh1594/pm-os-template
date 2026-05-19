---
description: PM-OS onboarding — four steps, one question per turn
---

# /onboard

Portable setup: **the PM's context first**, then **wire the repo** so `/today` and the rest of PM-OS work. **Exactly four steps** — no fifth onboarding phase.

## Interaction mode

**One question per assistant turn.** After the last question in a step, write that step's file outputs, then start the next step.

Do **not** invent company names, product names, or competitor names. Use `[FILL IN]` in files until the PM provides real names.

---

## Step 1 — Role, company, goals, working preferences

Ask in order (one per message):

1. What is your name and title?
2. What company do you work for (or `[FILL IN]` if freelancing)?
3. What is your team's mission in one sentence?
4. What products or areas do you own? (List names — user supplies them.)
5. Who are your top 3–5 stakeholders (name + role)?
6. What are your goals for the next 90 days (3 bullets max)?
7. How do you prefer the assistant to communicate (directness, format, pushback)?
8. What should the assistant never do in this workspace?

**Outputs:** Update `GOALS.md` and `🤖 AI/memory/memory.md` (include **Working preferences**).

---

## Step 2 — Strategy in the workspace

Ask in order:

1. What is your **one active initiative** right now (name + one-line outcome)?
2. Where should initiative docs live? (Default: `📦 Products/[product]/` — create folder from `_template` if needed.)
3. What does success look like **this quarter** (2–3 measurable signals)?
4. Any decisions already made that agents must not re-litigate?

**Outputs:** Scaffold product folder from `📦 Products/_template/` if missing; add initiative note to memory; optional stub under product folder.

---

## Step 3 — Daily loop (`/today` + task tracker)

Ask in order:

1. Which task tracker will be source of truth? (`jira` | `linear` | `asana` | `github` | `stub` | other — document in config)
2. What name(s) should `/today` filter tasks by? (maps to `profile.owner_names` in config)
3. Do you want Slack digest in `/today`? (yes/no — if yes, note env vars needed)
4. If no tracker yet: use **stub** mode with example tasks in `📋 Tasks/`?

**Outputs:** Update `🔧 Automation/scripts/today_cmd/config.yaml`; document required env vars in `.env.example` comments only (no secrets); stub `📋 Tasks/today.md` if needed.

---

## Step 4 — Connectors and first closed loop

Ask in order:

1. Will you use Granola for meeting context? (yes/no)
2. **If Granola = yes** — follow the [Granola daily sync branch](#granola-daily-sync-macos) below (macOS only), then continue with question 3.
3. Any MCP servers to enable in `.mcp.json`? (list or skip)
4. Optional: GenAI PM email for "One Step Better" in `/today`? (`GENAIPM_EMAIL` — optional)
5. Ready to run `/today dry` now? (yes/no)

**Outputs:** Align `.env.example` with choices; install LaunchAgent if approved; run `/today dry` if user agrees.

### Granola daily sync (macOS)

**When:** Granola = yes and the machine is macOS (`uname -s` = Darwin).

**Do not install without explicit approval.** One question after explaining:

> Daily sync runs locally at 11:59 PM, exports yesterday's meetings to `🏢 Company/meetings/granola/`, and logs to `.logs/`. It does not send data to the cloud. AI summaries still come from `/granola` in the IDE. Install this LaunchAgent on your Mac? (yes/no)

**If yes:**

1. Run from workspace root (Shell tool, `required_permissions: ["all"]` if needed for `launchctl`):
   ```bash
   bash "🔧 Automation/scripts/granola_cmd/install.sh"
   ```
2. Verify:
   ```bash
   launchctl list | grep pm-os.granola
   ```
3. Tell the PM: output folder, log paths, and that the first run happens at 11:59 PM (or they can run manually: `cd "🔧 Automation/scripts" && python3 -m granola_cmd.main --target-date yesterday`).

**If no:** Point to `🔧 Automation/scripts/granola_cmd/README.md` for manual install later.

**If Granola = yes but not macOS:** Say LaunchAgent is macOS-only; use `/granola` on demand or `🔧 Automation/scripts/granola_cmd/CRON_SETUP.md` for cron.

**Done message:** Confirm all four steps; point to `📝 Docs/guides/workflow-cheatsheet.md` and `COMMAND-REFERENCE.md`.

---

## After onboarding (not a fifth step)

Pick up lifecycle commands when there is a real initiative: `/brainstorm`, `/discover`, `/spec`, `/ship`, etc.

If the repo uses **Ruler**, edit `.ruler/AGENTS.md` and run `ruler apply` instead of hand-editing generated `CLAUDE.md`.
