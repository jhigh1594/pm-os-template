Execute the /today daily planning workflow (AgilePlace only).

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

The launcher automatically discovers the workspace root and resolves paths via AIPMOSConfig.

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

### Step 1: Interactive Carry-Forward Triage

Read `📋 Tasks/yesterday.md` (the backup) and triage the items that need to carry forward.

**First, offer opt-out:**
```
📋 Run interactive carry-forward triage?

[Yes] Review and select items to carry forward from yesterday
[Quick Skip] Start fresh, skip triage
```

If user selects "Quick Skip", jump to Step 2 with empty carry-forward lists.

If "Yes", proceed with batch triage:

**Batch Triage (Multi-Select):**

Ask the user which items from yesterday to continue working on. Present ALL items from both sections in a single multi-select question:

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

### Step 3: Update today.md
Replace the placeholder comments in `📋 Tasks/today.md`:
- Replace "## 🧠 What's On My Mind Today" section with carried-forward focus areas (if any)
- Replace `<!-- Claude/Cursor populates this with analysis -->` with actual Top 3 Priorities
- Replace `<!-- Claude/Cursor populates this with insights -->` with actual Ideas & Considerations

### Step 4: Display and Ask User
Show the user the completed today.md and ask:

**"What's on your mind today? What additional priorities or focus areas (beyond what you carried forward)?"**

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

## Output Summary

After execution completes, provide a summary including:
- Execution time (seconds, if logged)
- Tasks due today count
- Overdue count
- Top 3 priorities (with reasoning)
- Key insights from analysis
