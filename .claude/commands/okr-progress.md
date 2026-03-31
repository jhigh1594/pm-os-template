---
description: Run the okr progress workflow
---
# /okr-progress — OKR Progress Analysis

Run OKR progress and risk analysis (portfolio or single-objective). Collects template variables from the user before executing.

## Canonical Source

**Read and follow:** `/Users/jhigh/workspace/.claude/prompts/okr-progress-analysis.md`

The prompt defines the templatized analysis logic, output format, and run-time variable collection.

## Wrapper Behavior

When `/okr-progress` is invoked:

1. **Read** the canonical prompt file.
2. **Collect variables** — Prompt the user for any required placeholders not present in the message:
   - SCOPE (portfolio | single)
   - OBJECTIVE_ID_OR_NAME (when scope=single)
   - AS_OF_DATE (default: today)
   - AUDIENCE (operational | executive, default: operational)
   - OBJECTIVE_URL (optional, when scope=single)
3. **Substitute** collected values into the prompt.
4. **Execute** analysis using OKR tools/data and output per format.
5. **Deliver** one high-impact action and problem-first ordering.

## Usage

```
/okr-progress
/okr-progress portfolio
/okr-progress single "Q1 Revenue Target"
/okr-progress executive
```

**With arguments:** If scope/objective/audience are provided, skip those prompts. Always confirm date if not obvious.

## When to Suggest

- "Track my OKR progress"
- "Analyze progress on my objectives"
- "Evaluate this OKR for the board"
- "Which goals need attention?"
- "OKR health check"
- "Single most impactful action for my OKRs"

## Triggers

/okr-progress, okr progress, track OKRs, OKR analysis, OKR health, evaluate objective, OKR risk
