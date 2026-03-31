---
description: Run the ui refine workflow
---
# /ui-refine - UI Refinement Loop

Run the UI refinement loop until the implementation scores ≥9.3/10 on the objective rubric.

## Canonical Source

**Read and follow:** `/Users/jhigh/workspace/.claude/prompts/ui-refinement-loop.md`

The prompt defines refinement-loop mode, scoring rubric, and output format. This command invokes that behavior.

## Wrapper Behavior

When `/ui-refine` is invoked:

1. **Read** the canonical prompt file completely. (Stack and design constraints are predefined for this repo.)
2. **Resolve task** from user message after `/ui-refine`, attached file, or open file; if missing, ask.
3. **Execute** the refinement loop: implement → rubric → refine → repeat until pass or max iterations.
4. **Output** the scorecard after each pass; only summarize when Pass: YES.

## Usage

```
/ui-refine
/ui-refine Add a settings panel to the sidebar
/ui-refine [with file or selection attached]
```

## When to Suggest

- "Refine this UI until it's polished"
- "Implement this and iterate until it's good"
- "Build this component with the quality loop"
- "Run the UI refinement loop on..."
- User is doing UI work and wants iterative quality assurance

## Triggers

/ui-refine, ui refine, refinement loop, polish this UI, iterate on this component, score my UI
