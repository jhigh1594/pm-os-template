# Planview Corporate PowerPoint Template Guide

**Template Location:** `/Users/jhigh/Library/Mobile Documents/com~apple~CloudDocs/Planview Corporate Template-2025.pptx`

**Last Updated:** February 2026

---

> **⚠️ NOTE: This guide describes the legacy text-replacement workflow.**
>
> For new presentations, use the **creative generation workflow** via `/planview-deck` which generates slides from scratch using the Planview Design System (`PLANVIEW-DESIGN-SYSTEM.md`).
>
> This template is kept for reference and for cases where you need to match existing template slides exactly.

---

## Quick Reference (Legacy Workflow)

When creating Planview presentations using the template:

1. **Copy the template** to your working directory first
2. **Use the pptx skill** to rearrange slides and replace content
3. **Never create from scratch** - always start from the corporate template

---

## Template Inventory

**Total Slides:** 15 (0-indexed: slides 0-14)

### Title & Opening Slides

| Index | Slide Name | Purpose |
|-------|------------|---------|
| 0 | Title Slide | Main presentation title with tagline "Connect your Business from Ideas to Impact" |
| 2 | Title Slide-Alternate | Alternative title slide layout |

### Section Divider

| Index | Slide Name | Purpose |
|-------|------------|---------|
| 9 | Section Header | "Next Section of Presentation" - use to divide presentations into sections |

### Content Slides

| Index | Slide Name | Purpose |
|-------|------------|---------|
| 1 | Title and Content (Learned/Next Steps) | Summary slide with "What have we learned", "Go forward benefits", "Recommended process", "Next steps" |
| 3 | Two Content | Two-column content layout |
| 4 | Text Left | Text on left with space for image/graphic on right |
| 5 | Text Right | Text on right with image/graphic on left |
| 6 | Graphical Columns | Multi-column graphical layout with red/blue accent guidance |

### Design Reference Slides

| Index | Slide Name | Purpose |
|-------|------------|---------|
| 7 | Color Palette | Brand color reference - primary and accent colors |
| 8 | Typography | Font guidelines - Nunito Sans corporate font |
| 10 | Graphical Boxes | Red/Blue graphical box examples |
| 11 | Chart Examples | Sample charts - use as reference for data visualization |
| 12 | Logos and Product Icons | Logo usage guidelines |
| 13 | Image Overlay Examples | Dark and light image overlay techniques |

### Closing

| Index | Slide Name | Purpose |
|-------|------------|---------|
| 14 | Thank You | Closing slide |

---

## Available Slide Layouts

When duplicating slides within the template, these layouts are available:

| Layout # | Name | Best For |
|----------|------|----------|
| 1 | Title Slide | Opening slides, section breaks |
| 2 | Title and Content | Standard bullet points, single topic |
| 3 | Title Slide-Alternate | Alternative opening |
| 4 | Two Content | Side-by-side comparison, two topics |
| 5 | Comparison | Feature comparison, before/after |
| 6 | Agenda | Meeting agendas, outlines |
| 7 | Section Header | Major section dividers |
| 8 | Title Only | Large visuals, minimal text |
| 9 | Blank | Full creative control |

---

## Design Guidelines (from Template)

### Colors
- **Primary colors**: Essential for brand representation
- **Red accents**: Use bright red, medium red, and dark red for highlighting and small areas
- **Blue hues**: Available for graphical elements

### Typography
- **Corporate Font**: Nunito Sans
- **Windows**: Use "Nunito Sans" for normal text, "Nunito Sans ExtraBold" for emphasis
- **Fallback**: Arial if Nunito Sans unavailable

---

## Workflow: Creating a New Presentation

### Step 1: Copy Template
```bash
# Copy template to working directory
cp "/Users/jhigh/Library/Mobile Documents/com~apple~CloudDocs/Planview Corporate Template-2025.pptx" "working.pptx"
```

### Step 2: Plan Your Slides
Create an outline mapping your content to template slides:

```markdown
# Presentation Outline
- Slide 0: Title - [Your Title]
- Slide 3: Content - Introduction
- Slide 4: Two Content - Feature Comparison
- Slide 9: Section Header - Next Topic
- Slide 14: Thank You
```

### Step 3: Rearrange Slides
Use the pptx skill's rearrange.py script:

```bash
# Create presentation with slides 0, 3, 4, 4 (duplicate), 9, 14
python /Users/jhigh/.claude/skills/pptx/scripts/rearrange.py \
  "/Users/jhigh/Library/Mobile Documents/com~apple~CloudDocs/Planview Corporate Template-2025.pptx" \
  output.pptx 0,3,4,4,9,14
```

### Step 4: Extract Text Inventory
```bash
python /Users/jhigh/.claude/skills/pptx/scripts/inventory.py output.pptx text-inventory.json
```

### Step 5: Create Replacement JSON
Edit `text-inventory.json` to replace placeholder text with your content.

### Step 6: Apply Replacements
```bash
python /Users/jhigh/.claude/skills/pptx/scripts/replace.py output.pptx text-inventory.json final.pptx
```

---

## Tips

1. **Always start from template** - Never create blank presentations
2. **Duplicate slides you need** - Use rearrange.py to select and order slides
3. **Preserve formatting** - The replace.py script maintains original styling
4. **Check slide count** - Template has slides 0-14 (15 total)
5. **Use section headers** - Slide 9 is great for dividing long presentations

---

## Related Resources

- **PPTX Skill Documentation**: `/Users/jhigh/.claude/skills/pptx/`
- **Template Unpacked**: `/Users/jhigh/Planview Work/Docs/templates/planview-unpacked/`
