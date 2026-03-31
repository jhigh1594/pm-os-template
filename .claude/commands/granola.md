---
description: Run the granola workflow
---
Extract yesterday's meetings from Granola and save them as markdown files.

## Command Arguments

Parse the command arguments in order:
1. **Target Date** (optional, default: `yesterday`): `yesterday`, `today`, or `YYYY-MM-DD`
   - `yesterday`: extract meetings from yesterday (default)
   - `today`: extract meetings from today
   - `YYYY-MM-DD`: extract meetings from a specific date
2. **Verbose** (optional, default: `false`): `true` or `false`
   - `true`: enable verbose logging
   - `false`: standard logging

## Execution

Build the command based on arguments:
- Base command: `cd "🔧 Automation/scripts" && python3 -m granola_cmd.main`
- Add `--target-date {target_date}` (always)
- If `verbose` is `true`, add `-v`

Run the command using Bash.

## Examples

- `/granola` → extract yesterday's meetings
- `/granola today` → extract today's meetings
- `/granola 2026-01-10` → extract meetings from January 10, 2026
- `/granola yesterday true` → extract yesterday's meetings with verbose logging

## Output Summary

After execution completes, provide a summary including:
- Number of meetings extracted
- List of meeting titles with file paths
- Any warnings or errors encountered
- Output directory: `/Users/jhigh/Planview Work/🏢 Company/meetings/granola/`

## Post-Meeting Intelligence

After the Output Summary, automatically surface intelligence for each extracted meeting. If 0 meetings were extracted, skip this section entirely.

For each meeting, present the following block — do not require a separate user prompt:

```
## Post-Meeting Intelligence: [Meeting Title]

**Decisions made:**
- [extracted from notes — or "None explicitly stated in notes"]

**Action items:**
- [Owner]: [Action] — [Date if stated]
- (or "None explicitly stated in notes")

**Stakeholder signals:**
- [Name from participants]: [Any position shift, concern surfaced, or alignment signal]
- (only include if something substantive was observable)

**Knowledge/People/ candidates:**
- [name].md: Suggest appending: "[one sentence of new context — their position, concern, or commitment]"
- (only include for participants who have a file in 📚 Knowledge/People/)

**Product signals:**
- [Feature/capability]: [Customer reaction — confusion, resonance, surprise, or gap request]
- (Include only when meeting involved product demo, onboarding review, support escalation, or customer product walk-through)
- Route confusion signals: suggest `/signal --source [call|support] --product [name] "[signal]"` for each one

---
Run `/follow-up --meeting "[title]"` to draft communications and update stakeholder files.
```

**Constraints:**
- Intelligence is **presented, not applied** — no files are written without explicit user action or `/follow-up`
- Do not fabricate decisions or action items — if notes are sparse, say so explicitly
- Include Knowledge/People/ candidates only for participants with existing files in `📚 Knowledge/People/`
- Product signals surfaced **only when meeting context involves direct product interaction** — don't invent signals from non-product meetings
- If multiple meetings were extracted, present one intelligence block per meeting

## Notes

- Files are named `DD-MM-YY-title.md` format
- Each file contains: YAML frontmatter (title, date, participants, duration), transcript, and notes
- Reads directly from Granola's cache at `~/Library/Application Support/Granola/cache-v3.json`
