---
description: Run the today workflow
---
Execute the /today daily planning workflow (Task Tracker only).

## How This Works

**Python handles data collection and deterministic scaffolding** — it calls AgilePlace, Granola, RSS, and GenAIPM, then writes a fully-structured `today.md` with algorithmically-ranked priorities and a One Step Better placeholder. No Gemini or AI is involved.

**Claude handles all synthesis** — contextual reasoning, carry-forward triage, One Step Better, and user personalization. Claude's job is to review Python's draft, apply GOALS.md + memory context, and make the final call.

**Non-Claude Code fallback** — running the Python script directly (without this command) produces the deterministic plan as-is. For AI synthesis outside Claude Code, run `/today` in any Claude session.

## First-Run Setup

**If `config.yaml` has `task_tracker.type: stub` or no `task_tracker` section**, run setup first:

Ask the user: "What task/project management tool do you use to track your daily work?"
Options: Jira / Linear / Asana / GitHub Issues / Monday.com / Something else / None yet

Based on their answer:
1. Update `config.yaml` task_tracker section with their selection
2. If they have a tool, prompt for any needed credentials (API key, domain, etc.)
3. If "None yet", keep `type: stub` for demo purposes

Then continue with the normal workflow.

## Command Arguments

Parse the command arguments in order:
1. **Mode** (optional, default: `full`): `full` or `dry`
   - `full`: runs the workflow and stores output
   - `dry`: runs the workflow without storage
2. **Verbose** (optional, default: `true`): `true` or `false`

## Execution

**Python backs up `today.md` → `yesterday.md`, then regenerates `today.md` with fresh data from all sources.**

Build the command based on arguments:
- Base command: `python3 🔧 Automation/scripts/today_cmd/today_launcher.py`
- If `mode` is `dry`, add `--dry-run`
- If `verbose` is `true`, add `-v`

The launcher auto-discovers the workspace root via AIPMOSConfig. When `workspace/.venv` exists, the launcher uses that Python so dependencies are available without manual venv activation.

Run the command using Bash.

## Examples

- `/today` → `today_launcher.py -v`
- `/today full false` → `today_launcher.py`
- `/today dry` → `today_launcher.py --dry-run -v`
- `/today dry false` → `today_launcher.py --dry-run`

## Full Workflow

**How it works:**
1. Python backs up `today.md` → `yesterday.md`
2. Python regenerates `today.md` with fresh API data + deterministic priority suggestions
3. Claude reviews the draft, applies contextual reasoning, and completes synthesis
4. Interactive triage selects carry-forward items
5. `today.md` is updated with Claude's final synthesis

After the Python script completes:

### Step 1: Interactive Carry-Forward Triage (MANDATORY)

**Always ask** what the user wants to do with yesterday's items. Read `📋 Tasks/yesterday.md` (the backup). Extract "What's On My Mind" and "Top 3 Priorities" from yesterday.

**Ask explicitly:**
```
🔄 From yesterday's What's On My Mind and Top 3 Priorities, what do you want to:
- **Carry over** (keep working on today)
- **Complete** (done — move to completed.md)
- **Archive** (drop for now, don't carry forward)

[Review yesterday's items and respond]
```

If user chooses "Quick Skip" or "Start fresh", jump to Step 2 with empty carry-forward lists.

**Batch Triage (if user engages):** Present ALL items from both sections. For each, user indicates: carry over / complete / archive.

```
🔄 Select items to carry forward from yesterday:

FOCUS AREAS:
☐ Flesh out a PRD for building an OKR focused roadmap
☐ Tinker with an idea for AI-generated reports/views in AP
☐ Define the short and mid term plan and experience for Viz in Ensemble

PRIORITIES:
☐ Flesh out PRD for OKR-focused roadmap
☐ Tinker with AI-generated reports/views idea for AgilePlace
☐ Define short/mid-term Viz in Ensemble plan

[Confirm Selection] [Quick Skip - Start Fresh]
```

**Process the selection:**
- Selected items → Add to `carry_forward_focus` and `carry_forward_priorities` lists
- Unselected items → Move to `📋 Tasks/completed.md` with today's date

**Format for completed.md:**
```markdown
# Completed Items

## Thu Jan 29, 2026

### Focus Areas Completed
- Define the short and mid term plan and experience for Viz in Ensemble

### Priorities Completed
- (Any unselected priorities)
```

### Step 2: Review and Synthesize Priorities

Read `📋 Tasks/today.md`. Python has already suggested Top 3 Priorities using algorithmic scoring (due dates, overdue items, weekly priority alignment). Your job is contextual synthesis — not regeneration.

**Review Python's suggested priorities:**
- Do they align with `GOALS.md` Q-goals and current quarter OKRs?
- Do they reflect active context from `🤖 AI/memory/memory.md`?
- Do carry-forward items from triage change the ranking?

**Make the final call:**
- Keep Python's suggestions if they hold up under contextual review
- Override if your context reveals a better ranking (e.g., Python scored a card high because it's overdue, but you know it's blocked)
- Merge carry-forward priorities from Step 1

**Ideas & Considerations:**
- Python generates a set of observations (overdue concentration, staleness warnings, etc.)
- Add any themes, patterns, or blockers you see that Python's algorithm would miss
- Surface strategic connections Python can't infer (e.g., "this overdue card feeds the Q2 OKR")

### Step 2b: One Step Better AI PM (MANDATORY — never skip)

Every `/today` run **must** execute this step before updating `today.md`. Do not treat GenAI PM / One Step Better as optional: the "## 🚀 One Step Better" section must always contain a completed block (not an empty placeholder).

Read and follow `.claude/skills/menkesu-awesome-pm-skills-one-step-better-ai-pm/SKILL.md` (Phases 1–3 only; never Phase 4 apply from `/today`).

After reviewing the task data:

1. **Run Phases 1–3** of the skill (fetch briefs, build repo profile, match and rank). If `GENAIPM_EMAIL` is unset and the skill requires it, **prompt once** for the subscriber email and continue (or document that the user must set `GENAIPM_EMAIL` in `.env` and re-run).
2. **Extract the #1 recommended improvement** from the skill output (or the best available ranked item).
3. **Format the recommendation** for the "🚀 One Step Better" section:

```markdown
### Recommended Improvement

**[Brief title]**
- **Why it matters**: [Relevance to current Company work — connect to GOALS, active initiatives, or repo]
- **What to do**: [Concrete action the user can take]
- **Files affected**: [List specific files or "N/A - process improvement"]
- **Time estimate**: [e.g., "15-20 minutes"]

### Recently Applied
- [Check `.one-step-better/history.json` for last 2-3 improvements and list them; if file missing, omit this subsection only]
```

4. **Replace Python's One Step Better placeholder** with the formatted content. Python writes a fallback placeholder from GenAIPM data; Claude's enriched version should replace it with reasoning specific to current GOALS and active initiatives.

**Failure and edge cases (section still required):**

- Do **not** proceed to Step 3 until "## 🚀 One Step Better" has real content. If the GenAI PM API returns 401 or fails after retry, populate the section with a short **structured fallback**: what failed, that a free subscription is at https://genaipm.com, set `GENAIPM_EMAIL`, re-run `/today`. Same if fetch returns no briefs: state that explicitly and suggest checking tomorrow — still using the same markdown headings so the section is never blank.
- If briefs exist but **no item scores as relevant**, follow the skill: say so honestly in **Recommended Improvement** and give one low-confidence or tooling-adjacent takeaway rather than leaving the section empty.
- Do **not** auto-apply (Phase 4) from `/today` — the user reviews and decides.

**Important:**

- Skipping Step 2b or shipping an empty One Step Better block **invalidates** the `/today` run.

### Step 3: Update today.md

Update `📋 Tasks/today.md` with Claude's synthesis:
- Update "## 🧠 What's On My Mind Today" with carried-forward focus areas (if any)
- Update "## 🎯 Top 3 Priorities for Today" — either confirm Python's suggestions or replace with your refined ranking. Include reasoning for any change.
- Update "## 💡 Ideas & Considerations" — add contextual insights Python can't infer
- **MANDATORY:** Update "## 🚀 One Step Better" with enriched recommendation from Step 2b

### Step 4: Display and Ask User

Show the user the completed today.md. Ask TWO questions:

1. **"What's on your mind today? What additional priorities or focus areas (beyond what you carried forward)?"**
2. **"Which of the Top 3 priorities (or other overdue items) do you want to carry over or complete today — if any?"**

### Step 4.5: Surface Lifecycle Position

Scan `📦 Products/*/initiatives/*/` for any initiative folders. For each active initiative found, check which lifecycle artifacts exist (brainstorm summary, opportunity statement, one-pager, PRD, design brief, story breakdown, SPEC_BRIEF.md, launch plan, learn notes) and infer the current step.

**Output** (inline, compact — do not create a separate section):

> **Lifecycle**: [Initiative name] is at Step [N] — [step name]. Next: `[command]`

If no initiative folders exist: skip this step silently.
If multiple initiatives: show the most recently modified one only.

### Step 5: Incorporate New User Input
1. Read their response
2. Update `📋 Tasks/today.md` by appending to "## 🧠 What's On My Mind Today" section
3. If their stated priorities align with tasks in the list, note that alignment
4. Consider whether their input should adjust the Top 3 Priorities
5. If adjustments needed, update the priorities and explain why

### Step 6: Final Summary
Provide a concise summary showing:
- Final Top 3 Priorities (adjusted for user input if needed)
- Items carried forward from yesterday
- Items moved to completed.md
- Key alignment notes between user's focus and task list
- One Step Better recommendation (brief title only — full details in today.md; always include — note if fallback was used due to API)

## Output Summary

After execution completes, provide a summary including:
- Execution time (seconds, if logged)
- Tasks due today count
- Overdue count
- Top 3 priorities (with reasoning — including whether you confirmed or overrode Python's suggestions)
- Key insights from analysis
- One Step Better recommendation (title always; say if GenAI PM was unavailable and fallback text was written)
