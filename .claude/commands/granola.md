---
description: Run the granola workflow
---
Extract meetings from Granola and save them as markdown files, then **write an AI summary into each new file** (this command runs in Claude Code — use Claude Code attribution).

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

### 1) Extract (Bash)

Build the command based on arguments:
- Base command: `cd "🔧 Automation/scripts" && python3 -m granola_cmd.main`
- Add `--target-date {target_date}` (always)
- If `verbose` is `true`, add `-v`

Run the command using Bash.

### 2) Parse extractor output

After the script exits successfully, read stdout and parse the JSON object between these two lines (exact text):

- `GRANOLA_AGENT_RESULT_JSON_BEGIN`
- `GRANOLA_AGENT_RESULT_JSON_END`

The JSON shape is: `{"count": number, "files": string[], "date": string | null}`.

### 3) Workspace AI summary (mandatory when `count` > 0)

If `count` is `0`, skip this entire subsection (nothing new was written).

Otherwise, for **each** path in `files`:

1. **Read** the markdown file.
2. **Generate** a short workspace summary from the file’s content (prefer **## Summary** / notes if present; otherwise derive cautiously from **## Transcript**). Rules:
   - Lead with a **BLUF** (one or two sentences).
   - Add **bullets** only when they improve scanability (themes, open questions, follow-ups).
   - **Do not invent** decisions, owners, or dates not supported by the text. If the source is thin, say so plainly.
3. **Write** into the file using bounded markers so re-runs are idempotent:
   - If the file contains `<!-- workspace-agent-ai-summary -->` … `<!-- /workspace-agent-ai-summary -->`, **replace** that whole span (including both comment lines) with the new block.
   - Otherwise **insert** the new block **immediately before** the first `# ` title heading after the YAML frontmatter (summary sits directly under the closing `---` and **above** `# Title`).
4. Use **Claude Code** in the attribution line (not Cursor).

Use this block shape (fill `…` with generated content; use today’s date in ISO form for `YYYY-MM-DD`):

```markdown
<!-- workspace-agent-ai-summary -->
## AI summary

*Workspace summary (Claude Code, YYYY-MM-DD). If Granola captured a native summary, it still appears under **## Summary** below.*

…

<!-- /workspace-agent-ai-summary -->

```

5. **Save** the file (one edit pass per meeting file).

## Examples

- `/granola` → extract yesterday's meetings
- `/granola today` → extract today's meetings
- `/granola 2026-01-10` → extract meetings from January 10, 2026
- `/granola yesterday true` → extract yesterday's meetings with verbose logging

## Output Summary

After Bash completes **and** any AI summary file edits finish, provide a summary including:
- Number of meetings extracted (`count` from JSON, or equivalent)
- List of meeting titles with file paths
- Any warnings or errors encountered
- Output directory: `🏢 Company/meetings/granola/` (resolved via `WORKSPACE_PATH` / repo root in `config.yaml`)

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
- Each file contains: YAML frontmatter (title, date, participants, duration), optional native Granola **## Summary**, **## AI summary** (workspace agent), transcript, and documents as available
- Reads directly from Granola’s cache (newest `cache-v*.json` under `~/Library/Application Support/Granola/`)
