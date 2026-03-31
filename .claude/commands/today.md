---
description: Run the today workflow
---
Execute the /today daily planning workflow (Task Tracker only).

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
   - `full`: runs the workflow and sends Slack + stores output
   - `dry`: runs the workflow without Slack delivery or storage
2. **Verbose** (optional, default: `true`): `true` or `false`

## Execution

**Important:** The Python script automatically backs up `today.md` to `yesterday.md` before regenerating, enabling the carry-forward triage workflow.

Build the command based on arguments:
- Base command: `python3 🔧 Automation/scripts/today_cmd/today_launcher.py`
- If `mode` is `dry`, add `--dry-run`
- If `verbose` is `true`, add `-v`

The launcher automatically discovers the workspace root and resolves paths via AIPMOSConfig. When `workspace/.venv` exists, the launcher uses that Python so dependencies (feedparser, google-generativeai, etc.) are available without manual venv activation. Cursor and Claude Code agents run `/today` directly; no separate venv setup is required.

Run the command using Bash.

## Examples

- `/today` → `today_launcher.py -v`
- `/today full false` → `today_launcher.py`
- `/today dry` → `today_launcher.py --dry-run -v`
- `/today dry false` → `today_launcher.py --dry-run`

## Full Workflow

**How it works:**
1. Python script backs up `today.md` → `yesterday.md`
2. Python script regenerates `today.md` with fresh data
3. Claude workflow reads `yesterday.md` for carry-forward triage
4. Interactive triage selects items to keep or complete
5. `today.md` is updated with carried-forward items

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

### Step 2: Read and Analyze
Read `📋 Tasks/today.md` and analyze the data to generate:

**Top 3 Priorities:**
- Consider: overdue items, dependencies, strategic keywords (OKR, roadmap, PRD), high-priority flags
- Use context from `GOALS.md` for Q1 goals and priorities, and `🤖 AI/memory/memory.md` for session activity
- Merge with `carry_forward_priorities` from triage
- Generate 3 prioritized items with clear reasoning

**Ideas & Considerations:**
- Identify themes across tasks (PRD/Spec, Skills/Automation, OKRs/Roadmaps, Planning, Learning)
- Note patterns (batching opportunities, very overdue items, dependencies)
- Surface blockers or risks

### Step 2b: One Step Better AI PM (MANDATORY — never skip)

Every `/today` run **must** execute this step before updating `today.md`. Do not treat GenAI PM / One Step Better as optional: the "## 🚀 One Step Better" section must always contain a completed block (not an empty placeholder).

Read and follow `.claude/skills/menkesu-awesome-pm-skills-one-step-better-ai-pm/SKILL.md` (Phases 1–3 only; never Phase 4 apply from `/today`).

After analyzing the task data:

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

4. **Replace the placeholder** `<!-- Claude populates this with /one-step-better-ai-pm recommendations -->` with the formatted content.

**Failure and edge cases (section still required):**

- Do **not** proceed to Step 3 until "## 🚀 One Step Better" has real content. If the GenAI PM API returns 401 or fails after retry, populate the section with a short **structured fallback**: what failed, that a free subscription is at https://genaipm.com, set `GENAIPM_EMAIL`, re-run `/today`. Same if fetch returns no briefs: state that explicitly and suggest checking tomorrow — still using the same markdown headings so the section is never blank.
- If briefs exist but **no item scores as relevant**, follow the skill: say so honestly in **Recommended Improvement** and give one low-confidence or tooling-adjacent takeaway rather than leaving the section empty.
- Do **not** auto-apply (Phase 4) from `/today` — the user reviews and decides.

**Important:**

- Skipping Step 2b or shipping an empty One Step Better block **invalidates** the `/today` run.

### Step 3: Update today.md
Replace the placeholder comments in `📋 Tasks/today.md`:
- Replace "## 🧠 What's On My Mind Today" section with carried-forward focus areas (if any)
- Replace `<!-- Claude/Cursor populates this with analysis -->` with actual Top 3 Priorities
- **MANDATORY:** Replace `<!-- Claude/Cursor populates this with insights -->` with actual Ideas & Considerations. Never leave this section empty. Include: patterns across tasks, process notes, staleness/blocker observations, or strategic connections.
- **One Step Better (mandatory):** Replace the placeholder in "## 🚀 One Step Better" with the formatted recommendation from Step 2b — never leave this section as the HTML comment placeholder

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
- Top 3 priorities (with reasoning)
- Key insights from analysis
- One Step Better recommendation (title always; say if GenAI PM was unavailable and fallback text was written)
