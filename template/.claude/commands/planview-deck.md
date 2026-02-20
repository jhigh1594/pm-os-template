# /planview-deck - Create Planview Branded Presentation

Creates executive-ready PowerPoint presentations using the **html2pptx workflow** - HTML/CSS layouts converted to PowerPoint with precise alignment.

## Why html2pptx?

The html2pptx workflow produces better alignment than direct pptxgenjs because:
- **CSS flexbox handles layout** - No manual pixel calculations
- **Browser rendering accuracy** - Playwright renders exact positions
- **Visual preview** - Check HTML in browser before conversion
- **Consistent spacing** - CSS gap, padding, and margin work reliably

---

## CRITICAL: Read These Files First

**Before creating any presentation, you MUST read:**

```
1. Design System: ./Presentations/template/PLANVIEW-DESIGN-SYSTEM.md (relative to workspace root)
2. html2pptx Guide: ~/.claude/skills/pptx/html2pptx.md (READ COMPLETE FILE)
```

---

## Workflow

### Step 1: State Your Design Approach (MANDATORY)

**Before generating any slides, document your design decisions:**

```markdown
## Design Approach

**Content Analysis**: [What is this presentation about? What tone does it suggest?]

**Color Palette**: [Choose from palettes below or create custom - NOT just Planview defaults]

**Visual Elements**:
- Layout pattern: [4-column cards, 3-column, 2-column, full-width]
- Typography treatment: [size contrast, weight hierarchy]
- Visual details: [borders, shadows, geometric patterns]

**Rationale**: [Why these choices fit the content]
```

### Step 2: Choose a Creative Color Palette

**Select a palette based on the content, not just Planview defaults:**

| Palette | Colors | Best For |
|---------|--------|----------|
| **Classic Blue** | Deep navy (#1C2833), slate gray (#2E4053) | Professional, corporate |
| **Teal & Coral** | Teal (#5EA8A7), coral (#FE4447) | Modern, energetic |
| **Burgundy Luxury** | Burgundy (#5D1D2E), gold (#997929) | Premium, executive |
| **Deep Purple & Emerald** | Purple (#B165FB), emerald (#40695B) | Innovative, tech |
| **Sage & Terracotta** | Sage (#87A96B), terracotta (#E07A5F) | Natural, grounded |
| **Charcoal & Red** | Charcoal (#292929), red (#E33737) | Bold, impactful |
| **Planview Default** | Dark slate (#0F172A), Planview red (#E2251B) | Brand consistency |

**Brand Integration**:
- Use **Planview palette** (Dark slate, Planview red) for: title slide, header bars, footer
- Use **creative palette** for: content accents, card backgrounds, highlights
- This maintains brand identity while adding visual interest

### Step 3: Plan Slide Structure

Create an outline with specific layouts:

```markdown
# Presentation Outline

## Slide 1: Title Slide (from template)
- Title: [Main title]
- Subtitle: [Optional subtitle/tagline]
- Date: [Date]

## Slide 2: Overview (4-column-cards template)
- Title: [Section title]
- Tagline: [Red uppercase tagline]
- Cards: [4 card contents]

## Slide 3: Details (3-column-cards template)
- Title: [Section title]
- Cards: [3 card contents]

## Slide 4: Data (full-width-content template)
- Title: [Section title]
- Chart/Table: [Data visualization]
```

### Step 4: Create HTML Slides

**Use the HTML templates from `html-templates/` directory:**

| Template | Purpose | CSS Pattern |
|----------|---------|-------------|
| `header-footer.html` | Base template with header/footer | flex-direction: column |
| `4-column-cards.html` | Executive strategy overview | display: flex; flex: 1 |
| `3-column-cards.html` | Feature comparison | display: flex; flex: 1 |
| `2-column-split.html` | Text + visual layout | display: flex; gap: 24pt |
| `full-width-content.html` | Tables, charts, data | single column |
| `positioning-boxes.html` | Strategic callouts | stacked boxes |
| `key-metrics.html` | Stats and numbers display | 4 metric cards |

**Critical HTML Rules:**
- Dimensions: `width: 720pt; height: 405pt` (16:9)
- Text MUST be in `<p>`, `<h1>`-`<h6>`, `<ul>`, `<ol>` tags
- Use web-safe fonts only: Arial, Helvetica, Georgia, Verdana
- No CSS gradients - pre-rasterize as PNG if needed
- Use flexbox for alignment: `display: flex; gap: 12pt;`
- Logo path: reference `planview-logo.png` (copy to working directory)

**Example HTML Slide:**
```html
<!DOCTYPE html>
<html>
<head>
<style>
html { background: #F8FAFC; }
body {
  width: 720pt; height: 405pt; margin: 0; padding: 0;
  font-family: Arial, sans-serif;
  display: flex; flex-direction: column;
}
.header { background: #0F172A; padding: 10pt 24pt; }
.header-title { color: #FFFFFF; font-size: 22pt; font-weight: bold; margin: 0; }
.header-tagline { color: #E2251B; font-size: 9pt; font-weight: bold; margin: 4pt 0 0 0; }
.cards { flex: 1; display: flex; gap: 12pt; padding: 16pt 24pt; }
.card { flex: 1; background: #FFFFFF; border-radius: 4pt; padding: 12pt; border-left: 3pt solid #C00000; }
.card-category { color: #002060; font-size: 9pt; font-weight: bold; margin: 0 0 6pt 0; }
.card-headline { color: #0F172A; font-size: 12pt; font-weight: bold; margin: 0 0 8pt 0; }
.card-bullets { color: #334155; font-size: 9pt; margin: 0; padding-left: 12pt; }
.footer { padding: 6pt 24pt; display: flex; justify-content: space-between; }
.footer-text { color: #94A3B8; font-size: 6pt; margin: 0; }
</style>
</head>
<body>
<div class="header">
  <p class="header-title">Strategic Priorities</p>
  <p class="header-tagline">Q1 2026 ROADMAP</p>
</div>
<div class="cards">
  <div class="card">
    <p class="card-category">GROWTH</p>
    <p class="card-headline">Expand Market Presence</p>
    <ul class="card-bullets">
      <li>Launch in 3 new regions</li>
      <li>Partner program expansion</li>
    </ul>
  </div>
  <!-- Add more cards... -->
</div>
<div class="footer">
  <p class="footer-text">Planview Confidential</p>
  <img src="planview-logo.png" style="height: 10pt;">
</div>
</body>
</html>
```

### Step 5: Convert HTML to PPTX

Use the html2pptx library to convert:

```javascript
const pptxgen = require('pptxgenjs');
const html2pptx = require('~/.claude/skills/pptx/scripts/html2pptx.js');

async function createDeck() {
  const pptx = new pptxgen();
  pptx.layout = 'LAYOUT_16x9';
  pptx.author = 'Planview';
  pptx.title = 'My Presentation';

  // Convert each HTML slide
  await html2pptx('/tmp/slides/slide1.html', pptx);
  await html2pptx('/tmp/slides/slide2.html', pptx);

  // Save
  await pptx.writeFile({ fileName: 'content-slides.pptx' });
}
```

**Or use the workflow helper:**
```javascript
const { createPresentation, loadTemplate, saveHtmlSlide } =
  require('📽️ Presentations/template/html2pptx-workflow.js');

// Load template and replace placeholders
const html = loadTemplate('4-column-cards.html', {
  TITLE: 'Strategic Priorities',
  TAGLINE: 'Q1 2026 ROADMAP',
  // ... more replacements
});

// Save and convert
const slidePath = saveHtmlSlide(html, 'slide1.html');
await createPresentation({
  htmlFiles: [slidePath],
  outputPath: 'my-deck.pptx'
});
```

### Step 6: Create Title Slide from Corporate Template

The title slide comes from the corporate template (not html2pptx):

```bash
# Create replacement JSON
cat > /tmp/title-replacement.json << 'EOF'
{
  "slide-0": {
    "shape-0": { "paragraphs": [{ "text": "Your Title", "bold": true }] },
    "shape-1": { "paragraphs": [{ "text": "Your Subtitle", "font_size": 18.0 }] },
    "shape-2": { "paragraphs": [{ "text": "February 2026" }] }
  }
}
EOF

# Apply replacement
python3 ~/.claude/skills/pptx/scripts/replace.py \
  "📽️ Presentations/template/title-slide-only.pptx" \
  /tmp/title-replacement.json \
  title-slide.pptx
```

### Step 7: Visual Validation (MANDATORY)

**Always generate thumbnails to verify alignment:**

```bash
python3 ~/.claude/skills/pptx/scripts/thumbnail.py \
  content-slides.pptx \
  thumbnails \
  --cols 4
```

**Check for:**
- Lines align with shapes (no pixel offset)
- Cards have consistent spacing
- Text is not cut off
- Colors match design intent
- Logo positioned correctly in footer

### Step 8: Present Two Files

**Do NOT merge programmatically** - present both files for user to combine:

1. `title-slide.pptx` - Title slide from corporate template
2. `content-slides.pptx` - Content slides from html2pptx

**User combines in PowerPoint:**
1. Open `title-slide.pptx`
2. Open `content-slides.pptx` in new window
3. Drag all slides from content into title file
4. Save as final deck

---

## Quick Reference

### Color Constants

| Name | Hex | Usage |
|------|-----|-------|
| DARK_SLATE | `#0F172A` | Header bars |
| PLANVIEW_RED | `#E2251B` | Accents, taglines |
| DEEP_RED | `#C00000` | Card accent lines |
| NAVY_BLUE | `#002060` | Category labels |
| BODY_TEXT | `#334155` | Primary text |
| LIGHT_GRAY | `#F8FAFC` | Slide background |
| WHITE | `#FFFFFF` | Card backgrounds |
| MUTED_TEXT | `#64748B` | Secondary text |
| COPYRIGHT_GRAY | `#94A3B8` | Footer text |

### Font Sizes

| Element | Size | Weight |
|---------|------|--------|
| Header Title | 22pt | Bold |
| Header Tagline | 9pt | Bold |
| Card Category | 9-10pt | Bold |
| Card Headline | 12-13pt | Bold |
| Body/Bullets | 9pt | Regular |
| Footer | 6pt | Regular |

### HTML Template Files

```
📽️ Presentations/template/html-templates/
├── header-footer.html      # Base template
├── 4-column-cards.html     # Executive strategy
├── 3-column-cards.html     # Feature comparison
├── 2-column-split.html     # Text + visual
├── full-width-content.html # Tables, charts
├── positioning-boxes.html  # Strategic callouts
└── key-metrics.html        # Stats display
```

---

## Key Files

| File | Purpose |
|------|---------|
| Design System | `📽️ Presentations/template/PLANVIEW-DESIGN-SYSTEM.md` |
| html2pptx Guide | `~/.claude/skills/pptx/html2pptx.md` |
| html2pptx Script | `~/.claude/skills/pptx/scripts/html2pptx.js` |
| HTML Templates | `📽️ Presentations/template/html-templates/` |
| Workflow Helper | `📽️ Presentations/template/html2pptx-workflow.js` |
| Corporate Title Template | `📽️ Presentations/template/title-slide-only.pptx` |
| Planview Logo | `📽️ Presentations/template/planview-logo.png` |

---

## Common Issues & Fixes

| Issue | Cause | Fix |
|-------|-------|-----|
| Text cut off | Height too small | Increase container height or reduce font |
| Alignment off | Manual coordinates | Use CSS flexbox with `gap` |
| Gradient not showing | CSS not supported | Pre-rasterize as PNG |
| Logo missing | Wrong path | Copy logo to HTML directory |
| Overflow error | Content exceeds body | Reduce content or increase spacing |
| Wrong font | Custom font used | Use web-safe fonts (Arial) |

---

## When to Use Builder Module (planview-pptx.js)

The builder module is still useful for:
- Quick scripts that don't need precise alignment
- Batch generation of many similar slides
- Programmatic chart/table additions

But for **creative, polished presentations**, prefer the html2pptx workflow.
