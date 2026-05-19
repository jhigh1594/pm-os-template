---
description: Run the granola workflow
---
Extract meetings from Granola and save them as markdown files.

## Command Arguments

Parse the command arguments in order:
1. **Target Date** (optional, default: `yesterday`): `yesterday`, `today`, or `YYYY-MM-DD`
2. **Verbose** (optional, default: `false`): `true` or `false`

## Execution — MCP Primary, Python Fallback

### Step 1: Resolve target date range

Compute `start` and `end` ISO dates from the target date argument:
- `yesterday` → yesterday's date, 00:00 to 23:59
- `today` → today's date, 00:00 to 23:59
- `YYYY-MM-DD` → that date, 00:00 to 23:59

### Step 2: Fetch meetings via Granola MCP

Use `mcp__granola__list_meetings` with:
- `time_range: "custom"`
- `custom_start`: start date (YYYY-MM-DD)
- `custom_end`: end date (YYYY-MM-DD, same day or +1)

For each meeting returned, call `mcp__granola__get_meetings` (batch up to 10 IDs) to get full details: notes, AI summary, attendees, metadata.

For each meeting, call `mcp__granola__get_meeting_transcript` to get the verbatim transcript.

**If MCP tools are unavailable or return errors**, fall back to Python:
```
cd "🔧 Automation/scripts" && python3 -m granola_cmd.main --target-date {target_date}
```
Note which path was used in the output summary.

### Step 3: Write markdown files

For each meeting, write a file to `/Users/jon.high/SNOW-Work/🏢 Company/meetings/granola/` using the Write tool.

**Filename format:** `DD-MM-YY-{slugified-title}.md`
- Slugify: lowercase, spaces → hyphens, strip special chars, truncate at 50 chars

**File format:**
```markdown
---
title: "{meeting title}"
date: "YYYY-MM-DD"
meeting_id: "{uuid}"
duration: {minutes}
participants:
  - "{name}"
source: "mcp"
---

# {meeting title}

**Date:** {Month DD, YYYY}
**Duration:** {N} minutes
**Participants:** {comma-separated names or N/A}

---

## Notes

{AI-generated notes/summary from get_meetings — or "No notes available"}

---

## Transcript

{verbatim transcript from get_meeting_transcript — or "No transcript available"}
```

Skip meetings where `valid_meeting` is false or duration < 5 minutes.

## Examples

- `/granola` → extract yesterday's meetings
- `/granola today` → extract today's meetings
- `/granola 2026-01-10` → extract meetings from January 10, 2026

## Output Summary

After writing files, provide:
- Number of meetings extracted
- Data source used: `mcp` or `python-fallback`
- List of meeting titles with file paths
- Any warnings or errors

## Post-Meeting Intelligence

After the Output Summary, automatically surface intelligence for each extracted meeting. If 0 meetings were extracted, skip this section entirely.

For each meeting, present:

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
- [name].md: Suggest appending: "[one sentence of new context]"
- (only include for participants with a file in 📚 Knowledge/People/)

**Product signals:**
- [Feature/capability]: [Customer reaction — confusion, resonance, surprise, or gap]
- (only when meeting involved product demo, onboarding review, support escalation, or customer product walk-through)
- Route confusion signals: suggest `/signal --source [call|support] --product [name] "[signal]"` for each

---
Run `/follow-up --meeting "[title]"` to draft communications and update stakeholder files.
```

**Constraints:**
- Intelligence presented, not applied — no files written without explicit user action or `/follow-up`
- Do not fabricate decisions or action items — if notes sparse, say so
- Knowledge/People/ candidates only for participants with existing files in `📚 Knowledge/People/`
- Product signals only when meeting context involves direct product interaction

## Notes

- Cron job (`0 20 * * *`) runs `granola_cmd/main.py` via REST API nightly at 8pm PST — independent of MCP
- MCP requires paid Granola plan; REST API fallback handles cron and offline scenarios
- Files named `DD-MM-YY-title.md`
