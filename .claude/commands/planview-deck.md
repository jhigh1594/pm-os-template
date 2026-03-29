# /planview-deck - Create Editable PowerPoint Decks

Use this command when the deliverable must be an **editable PPTX**.

This command is now the **PowerPoint-only** path. For hosted, animated, shareable decks, use `/planview-slides`.

## What this command is for

- executive decks that must be edited in PowerPoint
- deliverables that need corporate template compatibility
- title-slide + content-slide workflows using html2pptx

## What this command is NOT for

- hosted HTML decks
- password-protected share links
- live animated presentations on Vercel

Those now belong to `/planview-slides`.

## Required reads

Before building a PPTX deck, read:

1. `📽️ Presentations/template/PLANVIEW-DESIGN-SYSTEM.md`
2. `/Users/jhigh/.claude/skills/pptx/html2pptx.md`

## PPTX workflow

1. Define the design approach for the specific deck.
2. Build content slides with the html2pptx workflow from `📽️ Presentations/template/`.
3. Create the title slide from the corporate PPTX template.
4. Generate thumbnails and visually validate spacing, alignment, and overflow.
5. Deliver the PPTX files for final merge in PowerPoint.

## Key paths

- Design system: `📽️ Presentations/template/PLANVIEW-DESIGN-SYSTEM.md`
- Workflow helper: `📽️ Presentations/template/html2pptx-workflow.js`
- Title template: `📽️ Presentations/template/title-slide-only.pptx`

## Decision rule

- Hosted, animated, password-protected deck: `/planview-slides`
- Editable PowerPoint deliverable: `/planview-deck`
