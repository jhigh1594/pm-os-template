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
- Output directory: `./🏢 Company/meetings/granola/` (relative to workspace root)

## Notes

- Files are named `DD-MM-YY-title.md` format
- Each file contains: YAML frontmatter (title, date, participants, duration), transcript, and notes
- Reads directly from Granola's cache at `~/Library/Application Support/Granola/cache-v3.json`
