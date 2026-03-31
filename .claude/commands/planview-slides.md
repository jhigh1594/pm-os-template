---
description: Run the planview slides workflow
---
# /planview-slides - Create Hosted Planview Slidev Decks

Use this command when the deliverable should be a **hosted, animated, shareable HTML deck**.

This is now the default workflow for new Planview presentation pages.

## Source of truth

- Authoring workspace: `📽️ Presentations/slidev/`
- Published site output: `📽️ Presentations/html/`
- Live deck routes: `/decks/<slug>/`

## Required reads

Before building or editing a hosted deck, read:

1. `📽️ Presentations/slidev/README.md`
2. `📽️ Presentations/template/PLANVIEW-DESIGN-SYSTEM.md`

## Workflow

From `📽️ Presentations/slidev/`:

```bash
pnpm install
pnpm create-deck <slug> "Deck Title"
pnpm dev <slug>
pnpm build <slug>
pnpm export-pdf <slug>
pnpm publish
```

## Rules

- `slides.md` frontmatter is the canonical deck metadata source
- deck-local visuals live in `decks/<slug>/public/`
- shared logos and fonts are managed through the Planview Slidev theme and synced into deck builds
- do not hand-author new standalone HTML decks under `📽️ Presentations/html/`
- keep `/planview-deck` reserved for editable PPTX output

## Publish behavior

- builds every `planview.publish: true` deck into `📽️ Presentations/html/decks/<slug>/`
- regenerates `📽️ Presentations/html/decks-manifest.json`
- updates the homepage gallery from manifest data
- writes redirect stubs for any `planview.redirectFrom` legacy routes

## Decision rule

- Hosted share link or live HTML presentation: `/planview-slides`
- Editable PowerPoint deck: `/planview-deck`
