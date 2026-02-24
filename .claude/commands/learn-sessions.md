# /learn-sessions — Extract patterns from recent sessions

Manually reviews recent `.specstory/history/` sessions and extracts patterns worth preserving to `.aipmos/patterns/learned-patterns.md`.

## What This Does

Reads the last N days of sessions from `.specstory/history/` and identifies:
- Repeated workflows or tool sequences worth formalizing
- Problems solved that are worth remembering
- Decisions made with reasoning worth preserving
- Workspace conventions reinforced or discovered

## Usage

```
/learn-sessions           # Review last 7 days
/learn-sessions --days 14 # Review last 14 days
```

## Output

Adds entries to `.aipmos/patterns/learned-patterns.md` that pass the 4-gate quality filter:

| Gate | Question |
|------|----------|
| **Actionable** | Can I do something specific with this? |
| **Specific** | Tied to this workspace, not generic advice? |
| **Durable** | Useful in 5+ future sessions? |
| **Non-obvious** | Not something I'd naturally know? |

Patterns that don't pass all 4 gates are discarded.

## Steps

1. List sessions from `.specstory/history/` within the date range
2. Read each session and extract candidate patterns
3. Filter candidates through the 4 quality gates
4. Append survivors to the appropriate section of `.aipmos/patterns/learned-patterns.md`
5. Update the validation log at the bottom of that file

## Note on Sessions

`.aipmos/sessions/` contains an archived copy of older sessions (pre-Feb 2026) for reference.
Active sessions live in `.specstory/history/` — that's the source to use here.
