---
description: Extract Granola meetings to markdown and add a Cursor-generated AI summary to each file
---

Extract meetings from Granola and save them as markdown files, then **write an AI summary into each new file** (this command runs in Cursor — use Cursor attribution).

## Command arguments

Parse arguments in order:

1. **Target date** (optional, default: `yesterday`): `yesterday`, `today`, or `YYYY-MM-DD`
2. **Verbose** (optional, default: `false`): `true` or `false`

## Execution

1. **Extract (Bash)**  
   - `cd "🔧 Automation/scripts" && python3 -m granola_cmd.main --target-date {target_date}`  
   - If verbose: append `-v`

2. **Parse extractor output**  
   After the script exits successfully, read stdout and parse the JSON object between these two lines (exact text):

   - `GRANOLA_AGENT_RESULT_JSON_BEGIN`  
   - `GRANOLA_AGENT_RESULT_JSON_END`

   The JSON shape is: `{"count": number, "files": string[], "date": string | null}`.

## Workspace AI summary (mandatory when count > 0)

If `count` is `0`, skip this entire section (nothing new was written).

Otherwise, for **each** path in `files`:

1. **Read** the markdown file.
2. **Generate** a short workspace summary from the file’s content (prefer the **## Summary** / notes sections if present; otherwise derive cautiously from **## Transcript**). Rules:
   - Lead with a **BLUF** (one or two sentences).
   - Add a few **bullets** only when they improve scanability (themes, open questions, follow-ups).
   - **Do not invent** decisions, owners, or dates not supported by the text. If the source is thin, say so plainly.
3. **Write** into the file using bounded markers so re-runs are idempotent:
   - If the file contains `<!-- workspace-agent-ai-summary -->` … `<!-- /workspace-agent-ai-summary -->`, **replace** that whole span (including both comment lines) with the new block.
   - Otherwise **insert** the new block **immediately before** the first markdown heading that is the meeting title (`# ` …) after the YAML frontmatter — i.e. the summary sits right under the closing `---` of frontmatter and **above** the `# Title` heading.

Use this block shape (fill `…` with generated content; use today’s date in ISO form for `YYYY-MM-DD`):

```markdown
<!-- workspace-agent-ai-summary -->
## AI summary

*Workspace summary (Cursor, YYYY-MM-DD). If Granola captured a native summary, it still appears under **## Summary** below.*

…

<!-- /workspace-agent-ai-summary -->

```

4. **Save** the file (single edit per meeting file).

## Output summary (chat)

After Bash and file edits:

- Number of meetings extracted (`count`)
- List of meeting titles with file paths
- Warnings or errors from the script
- Output directory: `🏢 Company/meetings/granola/` (under the repo / `WORKSPACE_PATH`)

## Post-meeting intelligence

Same block structure and constraints as `.claude/commands/granola.md` (decisions, action items, stakeholder signals, Knowledge/People candidates, product signals). **Present only in chat** — do not write People files or product signal nuggets unless the human asks or runs `/follow-up`.

## Notes

- Files are named `DD-MM-YY-title.md`.
- Granola cache: `~/Library/Application Support/Granola/cache-v*.json` (extractor picks the newest present file).
