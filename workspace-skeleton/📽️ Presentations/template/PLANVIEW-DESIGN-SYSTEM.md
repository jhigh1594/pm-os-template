# Planview Design System for Executive Presentations

**Version:** 2.1 - McKinsey/BCG Style
**Last Updated:** February 2026

---

## Builder Module

**Use the `planview-pptx.js` module to automatically apply this design system:**

```javascript
const { createPresentation, addHeader, addFooter, addCard, COLORS, SIZES } =
  require('/Users/jhigh/Planview Work/📽️ Presentations/template/planview-pptx.js');
```

The builder module provides:
- All color constants (COLORS.DARK_SLATE, COLORS.PLANVIEW_RED, etc.)
- Layout dimensions (SIZES.SLIDE_WIDTH, SIZES.MARGIN, etc.)
- Helper functions that encode these design specifications
- Reference implementation: `pptx/targetprocess-battlecard/create-battlecard.js`

---

## Design Philosophy

**Goal:** Create executive-ready slides that look like they came from McKinsey, Bain, or BCG.

**Key Principles:**
1. **Dark header bars** - Command attention with full-width slate headers
2. **Card-based layouts** - Organize complex information in elegant containers
3. **Subtle depth** - Use shadows sparingly for visual hierarchy
4. **High information density** - Executives want data, not fluff
5. **Strategic color accents** - Red for emphasis, not decoration
6. **Clean footer** - "Planview Confidential" only, no clutter

---

## Color Palette

### Primary Colors
| Color | Hex | Usage |
|-------|-----|-------|
| **Dark Slate** | `#0F172A` | Header bars, high-emphasis backgrounds |
| **Planview Red** | `#E2251B` | Accent lines, key highlights |
| **Deep Red** | `#C00000` | Card accent lines |
| **Navy Blue** | `#002060` | Category labels, section headers |
| **Body Text** | `#334155` | Primary body text, bullets |

### Neutral Colors
| Color | Hex | Usage |
|-------|-----|-------|
| **Light Gray** | `#F8FAFC` | Slide background (softer than white) |
| **White** | `#FFFFFF` | Card backgrounds |
| **Border Gray** | `#E2E8F0` | Subtle borders, dividers |
| **Muted Text** | `#64748B` | Secondary text, captions |
| **Copyright Gray** | `#94A3B8` | Footer text |

### Accent Colors
| Color | Hex | Usage |
|-------|-----|-------|
| **Teal Blue** | `#6A94AA` | Secondary accents, links |
| **Purple** | `#451F55` | Special callouts |
| **Green** | `#09AA61` | Positive metrics, success |
| **Gold** | `#FFAC47` | Highlights, warnings |

---

## Typography

### Font Stack
- **Primary:** Nunito Sans
- **Font Files:** `Nunito_Sans/` (15 TTF files in this directory)
- **HTML Usage:** `font-family: 'Nunito Sans', Arial, sans-serif;`

### Font Weights Available
| Weight | Filename | Usage |
|--------|----------|-------|
| ExtraLight | NunitoSans-ExtraLight.ttf | Large display text |
| Light | NunitoSans-Light.ttf | Subtle headers |
| Regular | NunitoSans-Regular.ttf | Body text |
| SemiBold | NunitoSans-SemiBold.ttf | Emphasized body |
| Bold | NunitoSans-Bold.ttf | Headers, emphasis |
| ExtraBold | NunitoSans-ExtraBold.ttf | Strong headlines |
| Black | NunitoSans-Black.ttf | Maximum impact |

### Type Scale

| Element | Size | Weight | Color |
|---------|------|--------|-------|
| Slide Title | 30pt | Bold | `#FFFFFF` on dark, `#0F172A` on light |
| Section Header | 24pt | Bold | `#0F172A` |
| Category Label | 13pt | Bold | `#002060` |
| Card Headline | 16pt | Bold | `#0F172A` |
| Body Text | 11pt | Regular | `#334155` |
| Bullets | 11pt | Regular | `#334155` |
| Caption | 9pt | Regular | `#64748B` |
| Footer | 6pt | Regular | `#94A3B8` |

---

## Layout Patterns

### 1. Executive Strategy Slide (4-Column Cards)

```
┌─────────────────────────────────────────────────────────────┐
│ ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ DARK SLATE HEADER ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ │
│ Title in White                                              │
│ TAGLINE IN RED                                              │
├─────────┬─────────┬─────────┬─────────┤
│ ┌─────┐ │ ┌─────┐ │ ┌─────┐ │ ┌─────┐ │
│ │RED  │ │ │RED  │ │ │RED  │ │ │RED  │ │
│ │LINE │ │ │LINE │ │ │LINE │ │ │LINE │ │
│ │     │ │ │     │ │ │     │ │ │     │ │
│ │WHITE│ │ │WHITE│ │ │WHITE│ │ │WHITE│ │
│ │CARD │ │ │CARD │ │ │CARD │ │ │CARD │ │
│ │     │ │ │     │ │ │     │ │ │     │ │
│ │Navy │ │ │Navy │ │ │Navy │ │ │Navy │ │
│ │Label│ │ │Label│ │ │Label│ │ │Label│ │
│ │Head │ │ │Head │ │ │Head │ │ │Head │ │
│ │•bullet│ │•bullet│ │•bullet│ │•bullet│ │
│ │•bullet│ │•bullet│ │•bullet│ │•bullet│ │
│ └─────┘ │ └─────┘ │ └─────┘ │ └─────┘ │
└─────────┴─────────┴─────────┴─────────┘
```

### 2. Two-Column Strategy Slide

```
┌─────────────────────────────────────────────────────────────┐
│ ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ DARK SLATE HEADER ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ │
│ Title in White                                              │
├──────────────────────────┬──────────────────────────────────┤
│                          │                                  │
│   LEFT CONTENT           │   RIGHT CONTENT                  │
│   • Bullet points        │   • Bullet points                │
│   • More content         │   • More content                 │
│   • Key insight          │   • Key insight                  │
│                          │                                  │
└──────────────────────────┴──────────────────────────────────┘
```

### 3. Title Slide

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│                                                             │
│                                                             │
│                 PLANVIEW                                    │
│                                                             │
│                 Main Title                                  │
│                 Subtitle in Teal                            │
│                                                             │
│                                                             │
│                                                             │
│                                        Planview Confidential│
└─────────────────────────────────────────────────────────────┘
```

---

## Card Design (McKinsey Style)

Each card has these elements:
1. **White background** with subtle shadow
2. **Red accent line** (4pt) on left edge
3. **Navy category label** at top (13pt bold)
4. **Bold headline** (16pt)
5. **Bullet points** (11pt) with tight spacing

---

## Executive Slide Standards

### Always Include
- Dark slate header bar with white title
- Red tagline (uppercase, 13pt bold)
- Light gray background (#F8FAFC)
- High information density

### Never Include
- Cluttered logos on every slide
- Large copyright text
- Generic stock imagery
- Empty whitespace for no reason
- More than 3 font sizes per slide

### Bullet Point Style
- Tight line spacing (1.2)
- No period at end
- Action-oriented language
- Maximum 4-5 bullets per card

---

## HTML Template (for html2pptx)

### Executive Slide with Cards
```html
<!DOCTYPE html>
<html>
<head>
<style>
html { background: #F8FAFC; }
body {
  width: 720pt;
  height: 405pt;
  margin: 0;
  padding: 0;
  font-family: 'Nunito Sans', Arial, sans-serif;
  background: #F8FAFC;
  position: relative;
}

.header {
  position: absolute;
  top: 0;
  left: 0;
  width: 720pt;
  height: 56pt;
  background: #0F172A;
}

.title {
  color: #FFFFFF;
  font-size: 24pt;
  font-weight: bold;
  margin: 10pt 0 0 24pt;
}

.tagline {
  color: #E2251B;
  font-size: 10pt;
  font-weight: bold;
  margin: 4pt 0 0 24pt;
  letter-spacing: 0.5pt;
}

.cards {
  position: absolute;
  top: 72pt;
  left: 24pt;
  width: 672pt;
  display: flex;
  gap: 16pt;
}

.card {
  flex: 1;
  background: #FFFFFF;
  border-radius: 6pt;
  padding: 16pt;
  position: relative;
  border-left: 3pt solid #C00000;
}

.category {
  color: #002060;
  font-size: 10pt;
  font-weight: bold;
  margin-bottom: 8pt;
}

.headline {
  color: #0F172A;
  font-size: 13pt;
  font-weight: bold;
  margin-bottom: 12pt;
  line-height: 1.3;
}

.bullets {
  color: #334155;
  font-size: 9pt;
  line-height: 1.4;
  margin: 0;
  padding-left: 12pt;
}

.bullets li {
  margin-bottom: 4pt;
}

.footer {
  position: absolute;
  bottom: 8pt;
  left: 24pt;
  color: #94A3B8;
  font-size: 6pt;
}

.planview-logo {
  position: absolute;
  bottom: 8pt;
  right: 24pt;
  height: 16pt;
}
</style>
</head>
<body>
<div class="header">
  <p class="title">Slide Title Here</p>
  <p class="tagline">TAGLINE IN RED</p>
</div>
<div class="cards">
  <div class="card">
    <p class="category">CATEGORY</p>
    <p class="headline">Bold headline here</p>
    <ul class="bullets">
      <li>Bullet point one</li>
      <li>Bullet point two</li>
      <li>Bullet point three</li>
    </ul>
  </div>
</div>
<p class="footer">© 2025 Planview, Inc. // Confidential</p>
<img class="planview-logo" src="/tmp/planview-logo.png">
</body>
</html>
```

---

## Quick Reference

### For Maximum Impact
- Use 4-column card layout for strategy comparisons
- Use dark headers for executive gravitas
- Pack information - executives want data
- Red accents for emphasis only
- Minimal footer: "Planview Confidential"

### Content Guidelines
- Category labels: 1-3 words (e.g., "ARR Growth", "AI-First")
- Headlines: punchy statements, not descriptions
- Bullets: specific metrics or actions, no periods
- Taglines: uppercase, 3-5 words

---

**Last Updated**: February 2026
**Style**: McKinsey/BCG Executive Presentation
