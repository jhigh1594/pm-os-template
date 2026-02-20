/**
 * Planview PPTX Builder Module
 *
 * Direct pptxgenjs wrapper implementing the Planview Design System.
 * Eliminates need for html2pptx abstraction layer.
 *
 * @version 2.0.0
 * @see PLANVIEW-DESIGN-SYSTEM.md for design specifications
 */

const pptxgen = require('pptxgenjs');
const path = require('path');

// ============================================================================
// DESIGN SYSTEM CONSTANTS
// ============================================================================

const COLORS = {
  // Primary
  DARK_SLATE: '0F172A',
  PLANVIEW_RED: 'E2251B',
  DEEP_RED: 'C00000',
  NAVY_BLUE: '002060',
  BODY_TEXT: '334155',

  // Neutral
  LIGHT_GRAY: 'F8FAFC',
  WHITE: 'FFFFFF',
  BORDER_GRAY: 'E2E8F0',
  MUTED_TEXT: '64748B',
  COPYRIGHT_GRAY: '94A3B8',

  // Accent
  TEAL_BLUE: '6A94AA',
  PURPLE: '451F55',
  GREEN: '09AA61',
  GOLD: 'FFAC47',
};

const SIZES = {
  SLIDE_WIDTH: 10,      // inches (720pt / 72)
  SLIDE_HEIGHT: 5.625,  // inches (405pt / 72) - 16:9

  // Margins and spacing (in inches)
  MARGIN: 0.333,        // 24pt
  CARD_GAP: 0.222,      // 16pt
  HEADER_HEIGHT: 0.667, // 48pt

  // Font sizes (in points)
  TITLE: 24,
  SECTION_HEADER: 24,
  CATEGORY_LABEL: 13,
  CARD_HEADLINE: 16,
  BODY: 11,
  BULLETS: 11,
  CAPTION: 9,
  FOOTER: 6,
  TAGLINE: 10,
};

const FONTS = {
  PRIMARY: 'Nunito Sans',
  FALLBACK: 'Arial',
};

// Path to font files (relative to this module)
const FONT_DIR = path.join(__dirname, 'Nunito_Sans');

// ============================================================================
// FONT REGISTRATION
// ============================================================================

/**
 * Register Nunito Sans fonts with the presentation.
 * Call this before adding any slides.
 *
 * @param {PPTX} pptx - The pptxgenjs instance
 */
function registerFonts(pptx) {
  // Register all Nunito Sans font weights
  const fontWeights = [
    { name: 'Nunito Sans', weight: 'normal', style: 'normal', filename: 'NunitoSans-Regular.ttf' },
    { name: 'Nunito Sans', weight: 'bold', style: 'normal', filename: 'NunitoSans-Bold.ttf' },
    { name: 'Nunito Sans', weight: 'normal', style: 'italic', filename: 'NunitoSans-Italic.ttf' },
    { name: 'Nunito Sans', weight: 'bold', style: 'italic', filename: 'NunitoSans-BoldItalic.ttf' },
    { name: 'Nunito Sans Light', weight: 'normal', style: 'normal', filename: 'NunitoSans-Light.ttf' },
    { name: 'Nunito Sans SemiBold', weight: 'normal', style: 'normal', filename: 'NunitoSans-SemiBold.ttf' },
    { name: 'Nunito Sans ExtraBold', weight: 'normal', style: 'normal', filename: 'NunitoSans-ExtraBold.ttf' },
    { name: 'Nunito Sans Black', weight: 'normal', style: 'normal', filename: 'NunitoSans-Black.ttf' },
  ];

  fontWeights.forEach(font => {
    try {
      pptx.addFont(path.join(FONT_DIR, font.filename), {
        family: font.name,
        weight: font.weight,
        style: font.style,
      });
    } catch (e) {
      // Font registration may fail in some environments, continue gracefully
      console.warn(`Could not register font: ${font.filename}`);
    }
  });
}

// ============================================================================
// PRESENTATION FACTORY
// ============================================================================

/**
 * Create a new Planview-styled presentation.
 *
 * @param {Object} options - Presentation options
 * @param {string} options.title - Presentation title (for metadata)
 * @param {string} options.author - Author name
 * @returns {PPTX} Configured pptxgenjs instance
 */
function createPresentation(options = {}) {
  const pptx = new pptxgen();

  // Set presentation properties
  pptx.author = options.author || 'Planview';
  pptx.title = options.title || 'Planview Presentation';
  pptx.company = 'Planview, Inc.';

  // Set default layout to 16:9
  pptx.defineLayout({
    name: 'PLANVIEW_16x9',
    width: SIZES.SLIDE_WIDTH,
    height: SIZES.SLIDE_HEIGHT
  });
  pptx.layout = 'PLANVIEW_16x9';

  // Register fonts
  registerFonts(pptx);

  return pptx;
}

// ============================================================================
// SLIDE HELPERS
// ============================================================================

/**
 * Create a slide with default Planview styling (light gray background).
 *
 * @param {PPTX} pptx - The presentation instance
 * @param {string} masterName - Optional master slide name
 * @returns {Slide} The new slide
 */
function addSlide(pptx, masterName = null) {
  const slide = pptx.addSlide({ masterName });

  // Set background color
  slide.background = { color: COLORS.LIGHT_GRAY };

  return slide;
}

/**
 * Add a corporate-style title slide.
 *
 * @param {PPTX} pptx - The presentation instance
 * @param {Object} options - Title slide options
 * @param {string} options.title - Main title text
 * @param {string} options.subtitle - Optional subtitle (teal color)
 * @param {string} options.presenter - Optional presenter name
 * @param {string} options.date - Optional date string
 * @returns {Slide} The title slide
 */
function addTitleSlide(pptx, options = {}) {
  const { title, subtitle, presenter, date } = options;
  const slide = pptx.addSlide();

  // White background
  slide.background = { color: COLORS.WHITE };

  // Planview wordmark at top (simplified - just text)
  slide.addText('PLANVIEW', {
    x: 0,
    y: 1.5,  // Centered vertically
    w: SIZES.SLIDE_WIDTH,
    h: 0.5,
    fontSize: 14,
    fontFace: FONTS.PRIMARY,
    bold: true,
    color: COLORS.PLANVIEW_RED,
    align: 'center',
  });

  // Main title
  if (title) {
    slide.addText(title, {
      x: SIZES.MARGIN,
      y: 2.2,
      w: SIZES.SLIDE_WIDTH - (SIZES.MARGIN * 2),
      h: 0.8,
      fontSize: 32,
      fontFace: FONTS.PRIMARY,
      bold: true,
      color: COLORS.DARK_SLATE,
      align: 'center',
      valign: 'middle',
    });
  }

  // Subtitle (teal)
  if (subtitle) {
    slide.addText(subtitle, {
      x: SIZES.MARGIN,
      y: 3.1,
      w: SIZES.SLIDE_WIDTH - (SIZES.MARGIN * 2),
      h: 0.4,
      fontSize: 16,
      fontFace: FONTS.PRIMARY,
      color: COLORS.TEAL_BLUE,
      align: 'center',
    });
  }

  // Presenter name (if provided)
  if (presenter) {
    slide.addText(presenter, {
      x: SIZES.MARGIN,
      y: 4.5,
      w: SIZES.SLIDE_WIDTH - (SIZES.MARGIN * 2),
      h: 0.3,
      fontSize: 14,
      fontFace: FONTS.PRIMARY,
      color: COLORS.MUTED_TEXT,
      align: 'center',
    });
  }

  // Footer with confidentiality
  const footerText = date ? `Planview Confidential // ${date}` : 'Planview Confidential';
  slide.addText(footerText, {
    x: SIZES.MARGIN,
    y: SIZES.SLIDE_HEIGHT - 0.25,
    w: SIZES.SLIDE_WIDTH - (SIZES.MARGIN * 2) - 0.75,
    h: 0.15,
    fontSize: 6,
    fontFace: FONTS.PRIMARY,
    color: COLORS.COPYRIGHT_GRAY,
    align: 'right',
  });

  // Planview logo in bottom-right (stored in template directory)
  const logoPath = path.join(__dirname, 'planview-logo.png');
  try {
    slide.addImage({
      path: logoPath,
      x: SIZES.SLIDE_WIDTH - SIZES.MARGIN - 0.667,
      y: SIZES.SLIDE_HEIGHT - 0.222,
      w: 0.667,
      h: 0.167,
    });
  } catch (e) {
    console.warn('Could not add Planview logo to title slide:', e.message);
  }

  return slide;
}

/**
 * Add the standard dark slate header bar to a slide.
 *
 * @param {Slide} slide - The slide to add header to
 * @param {string} title - The slide title (white text)
 * @param {string} tagline - Optional tagline (red text, uppercase)
 * @returns {Object} Header bounding box {x, y, w, h}
 */
function addHeader(slide, title, tagline = '') {
  const headerY = 0;
  const headerH = SIZES.HEADER_HEIGHT;  // 0.667 in (48pt)
  const headerW = SIZES.SLIDE_WIDTH;

  // Dark slate header background
  slide.addShape('rect', {
    x: 0,
    y: headerY,
    w: headerW,
    h: headerH,
    fill: { color: COLORS.DARK_SLATE },
    line: { color: COLORS.DARK_SLATE },
  });

  // Title text (white) - 8pt from top per HTML spec
  const titleY = headerY + 0.111;  // 8pt from top
  const titleH = 0.278;  // ~20pt height for title
  slide.addText(title, {
    x: SIZES.MARGIN,
    y: titleY,
    w: headerW - (SIZES.MARGIN * 2),
    h: titleH,
    fontSize: 22,
    fontFace: FONTS.PRIMARY,
    bold: true,
    color: COLORS.WHITE,
    valign: 'top',
  });

  // Tagline text (red) - 2pt below title, left-aligned
  if (tagline) {
    slide.addText(tagline.toUpperCase(), {
      x: SIZES.MARGIN,
      y: titleY + titleH + 0.028,  // 2pt below title
      w: headerW - (SIZES.MARGIN * 2),
      h: 0.167,
      fontSize: 9,
      fontFace: FONTS.PRIMARY,
      bold: true,
      color: COLORS.PLANVIEW_RED,
      valign: 'top',
    });
  }

  return { x: 0, y: headerY, w: headerW, h: headerH };
}

/**
 * Add the standard footer to a slide with Planview logo.
 *
 * @param {Slide} slide - The slide to add footer to
 * @param {string} text - Footer text (defaults to "Planview Confidential")
 * @param {Object} options - Optional settings
 * @param {boolean} options.includeLogo - Whether to include logo (default: true)
 */
function addFooter(slide, text = 'Planview Confidential', options = {}) {
  const { includeLogo = true } = options;

  // Footer text on the left
  slide.addText(text, {
    x: SIZES.MARGIN,
    y: SIZES.SLIDE_HEIGHT - 0.167,  // 12pt from bottom
    w: SIZES.SLIDE_WIDTH - (SIZES.MARGIN * 2) - 0.75,  // Leave room for logo
    h: 0.111,
    fontSize: SIZES.FOOTER,
    fontFace: FONTS.PRIMARY,
    color: COLORS.COPYRIGHT_GRAY,
    valign: 'bottom',
  });

  // Planview logo in bottom-right (stored in template directory)
  if (includeLogo) {
    const logoPath = path.join(__dirname, 'planview-logo.png');
    try {
      slide.addImage({
        path: logoPath,
        x: SIZES.SLIDE_WIDTH - SIZES.MARGIN - 0.667,  // 48pt from right
        y: SIZES.SLIDE_HEIGHT - 0.222,  // 16pt from bottom
        w: 0.667,  // 48pt wide
        h: 0.167,  // 12pt tall
      });
    } catch (e) {
      // If logo fails to load, continue without it
      console.warn('Could not add Planview logo:', e.message);
    }
  }
}

// ============================================================================
// CARD LAYOUTS
// ============================================================================

/**
 * Card options for card-based layouts.
 * @typedef {Object} CardOptions
 * @property {string} category - Navy category label at top
 * @property {string} headline - Bold headline text
 * @property {string[]} bullets - Array of bullet points
 * @property {string} accentColor - Accent line color (default: DEEP_RED)
 */

/**
 * Add a single card to a slide.
 *
 * @param {Slide} slide - The slide to add card to
 * @param {number} x - X position (inches)
 * @param {number} y - Y position (inches)
 * @param {number} w - Width (inches)
 * @param {number} h - Height (inches)
 * @param {CardOptions} options - Card content options
 * @returns {Object} Card bounding box
 */
function addCard(slide, x, y, w, h, options) {
  const { category, headline, bullets, accentColor = COLORS.DEEP_RED } = options;

  // Card background (white with rounded corners)
  slide.addShape('roundRect', {
    x,
    y,
    w,
    h,
    fill: { color: COLORS.WHITE },
    line: { color: COLORS.WHITE },
    radius: 0.042,  // ~3pt
    shadow: { type: 'outer', blur: 3, offset: 1, angle: 45, opacity: 0.1 },
  });

  // Accent line (left edge)
  slide.addShape('rect', {
    x,
    y,
    w: 0.042,  // 3pt
    h,
    fill: { color: accentColor },
    line: { color: accentColor },
  });

  let contentY = y + 0.139;  // 10pt padding

  // Category label (navy)
  if (category) {
    slide.addText(category, {
      x: x + 0.167,  // 12pt from left edge
      y: contentY,
      w: w - 0.222,
      h: 0.167,
      fontSize: 10,
      fontFace: FONTS.PRIMARY,
      bold: true,
      color: COLORS.NAVY_BLUE,
      valign: 'top',
    });
    contentY += 0.194;  // 14pt spacing
  }

  // Headline (dark slate)
  if (headline) {
    slide.addText(headline, {
      x: x + 0.167,
      y: contentY,
      w: w - 0.222,
      h: 0.333,
      fontSize: 13,
      fontFace: FONTS.PRIMARY,
      bold: true,
      color: COLORS.DARK_SLATE,
      valign: 'top',
      wrap: true,
    });
    contentY += 0.306;  // 22pt spacing
  }

  // Bullet points
  if (bullets && bullets.length > 0) {
    const bulletText = bullets.map(b => ({ text: b, options: { bullet: true } }));
    slide.addText(bulletText, {
      x: x + 0.167,
      y: contentY,
      w: w - 0.222,
      h: h - (contentY - y) - 0.111,
      fontSize: 9,
      fontFace: FONTS.PRIMARY,
      color: COLORS.BODY_TEXT,
      valign: 'top',
      wrap: true,
      lineSpacing: 18,  // ~1.3 line height
    });
  }

  return { x, y, w, h };
}

/**
 * Add a 4-column card layout (executive strategy style).
 *
 * @param {Slide} slide - The slide to add cards to
 * @param {CardOptions[]} cards - Array of 4 card content objects
 * @param {number} startY - Y position to start (default: just below header)
 * @returns {Object} Bounding box of the card area
 */
function addFourColumnCards(slide, cards, startY = 0.889) {
  const gap = SIZES.CARD_GAP;
  const totalWidth = SIZES.SLIDE_WIDTH - (SIZES.MARGIN * 2);
  const cardWidth = (totalWidth - (gap * 3)) / 4;
  const cardHeight = 3.5;  // Approximate height for content area

  const startX = SIZES.MARGIN;

  cards.forEach((card, i) => {
    const x = startX + (i * (cardWidth + gap));
    addCard(slide, x, startY, cardWidth, cardHeight, card);
  });

  return {
    x: startX,
    y: startY,
    w: totalWidth,
    h: cardHeight
  };
}

/**
 * Add a 3-column card layout.
 *
 * @param {Slide} slide - The slide to add cards to
 * @param {CardOptions[]} cards - Array of 3 card content objects
 * @param {Object} options - Layout options
 * @param {number} options.startY - Y position to start
 * @param {number} options.cardHeight - Height of cards
 * @returns {Object} Bounding box of the card area
 */
function addThreeColumnCards(slide, cards, options = {}) {
  const { startY = 0.889, cardHeight = 2.5 } = options;
  const gap = 0.167;
  const totalWidth = SIZES.SLIDE_WIDTH - (SIZES.MARGIN * 2);
  const cardWidth = (totalWidth - (gap * 2)) / 3;

  const startX = SIZES.MARGIN;

  cards.forEach((card, i) => {
    const x = startX + (i * (cardWidth + gap));
    addCard(slide, x, startY, cardWidth, cardHeight, card);
  });

  return {
    x: startX,
    y: startY,
    w: totalWidth,
    h: cardHeight
  };
}

/**
 * Add a 2-column card layout.
 *
 * @param {Slide} slide - The slide to add cards to
 * @param {CardOptions} leftCard - Left card content
 * @param {CardOptions} rightCard - Right card content
 * @param {number} startY - Y position to start
 * @returns {Object} Bounding box of the card area
 */
function addTwoColumnCards(slide, leftCard, rightCard, startY = 0.889) {
  const gap = SIZES.CARD_GAP;
  const totalWidth = SIZES.SLIDE_WIDTH - (SIZES.MARGIN * 2);
  const cardWidth = (totalWidth - gap) / 2;
  const cardHeight = 3.5;

  const startX = SIZES.MARGIN;

  addCard(slide, startX, startY, cardWidth, cardHeight, leftCard);
  addCard(slide, startX + cardWidth + gap, startY, cardWidth, cardHeight, rightCard);

  return {
    x: startX,
    y: startY,
    w: totalWidth,
    h: cardHeight
  };
}

// ============================================================================
// SPECIALIZED LAYOUTS
// ============================================================================

/**
 * Add a positioning statement box (dark background, centered text).
 *
 * @param {Slide} slide - The slide
 * @param {string} text - Positioning statement text
 * @param {number} y - Y position
 */
function addPositioningBox(slide, text, y = 0.889) {
  const boxH = 0.389;
  const boxW = SIZES.SLIDE_WIDTH - (SIZES.MARGIN * 2);

  slide.addShape('roundRect', {
    x: SIZES.MARGIN,
    y,
    w: boxW,
    h: boxH,
    fill: { color: COLORS.DARK_SLATE },
    line: { color: COLORS.DARK_SLATE },
    radius: 0.042,
  });

  slide.addText(text, {
    x: SIZES.MARGIN,
    y,
    w: boxW,
    h: boxH,
    fontSize: 12,
    fontFace: FONTS.PRIMARY,
    italic: true,
    color: COLORS.WHITE,
    align: 'center',
    valign: 'middle',
  });
}

/**
 * Add a stat/callout box (navy background).
 *
 * @param {Slide} slide - The slide
 * @param {string} text - Stat text (can include **bold** markdown)
 * @param {number} y - Y position
 */
function addStatBox(slide, text, y) {
  const boxH = 0.444;
  const boxW = SIZES.SLIDE_WIDTH - (SIZES.MARGIN * 2);

  slide.addShape('roundRect', {
    x: SIZES.MARGIN,
    y,
    w: boxW,
    h: boxH,
    fill: { color: COLORS.NAVY_BLUE },
    line: { color: COLORS.NAVY_BLUE },
    radius: 0.042,
  });

  slide.addText(text, {
    x: SIZES.MARGIN + 0.139,
    y,
    w: boxW - 0.278,
    h: boxH,
    fontSize: 10,
    fontFace: FONTS.PRIMARY,
    color: COLORS.WHITE,
    align: 'center',
    valign: 'middle',
    boldFormatting: true,
  });
}

/**
 * Add a differentiation box (white with red accent).
 *
 * @param {Slide} slide - The slide
 * @param {string} title - Box title (navy)
 * @param {Object[]} items - Array of {title, description} objects
 * @param {number} y - Y position
 * @returns {number} Height of the box
 */
function addDifferentiatorsBox(slide, title, items, y) {
  const lineH = 0.306;
  const titleH = 0.222;
  const padding = 0.139;
  const boxH = titleH + (items.length * lineH) + 0.111;
  const boxW = SIZES.SLIDE_WIDTH - (SIZES.MARGIN * 2);

  // White background
  slide.addShape('roundRect', {
    x: SIZES.MARGIN,
    y,
    w: boxW,
    h: boxH,
    fill: { color: COLORS.WHITE },
    line: { color: COLORS.WHITE },
    radius: 0.042,
  });

  // Red accent line
  slide.addShape('rect', {
    x: SIZES.MARGIN,
    y,
    w: 0.056,
    h: boxH,
    fill: { color: COLORS.PLANVIEW_RED },
    line: { color: COLORS.PLANVIEW_RED },
  });

  // Title
  slide.addText(title, {
    x: SIZES.MARGIN + 0.167,
    y: y + 0.083,
    w: boxW - 0.222,
    h: titleH,
    fontSize: 10,
    fontFace: FONTS.PRIMARY,
    bold: true,
    color: COLORS.NAVY_BLUE,
    valign: 'top',
  });

  // Items
  let itemY = y + titleH + 0.083;
  items.forEach(item => {
    slide.addText([
      { text: item.title, options: { bold: true, color: COLORS.DARK_SLATE } },
      { text: ' — ' + item.description, options: { color: COLORS.BODY_TEXT } },
    ], {
      x: SIZES.MARGIN + 0.167,
      y: itemY,
      w: boxW - 0.222,
      h: lineH,
      fontSize: 9,
      fontFace: FONTS.PRIMARY,
      valign: 'top',
    });
    itemY += lineH;
  });

  return boxH;
}

/**
 * Add a pivot/action box (navy background with red label).
 *
 * @param {Slide} slide - The slide
 * @param {string} label - Red label text
 * @param {string} text - Body text
 * @param {number} y - Y position
 */
function addPivotBox(slide, label, text, y) {
  const boxH = 0.778;
  const boxW = SIZES.SLIDE_WIDTH - (SIZES.MARGIN * 2);

  slide.addShape('roundRect', {
    x: SIZES.MARGIN,
    y,
    w: boxW,
    h: boxH,
    fill: { color: COLORS.NAVY_BLUE },
    line: { color: COLORS.NAVY_BLUE },
    radius: 0.042,
  });

  // Label
  slide.addText(label, {
    x: SIZES.MARGIN + 0.139,
    y: y + 0.083,
    w: boxW - 0.278,
    h: 0.194,
    fontSize: 8,
    fontFace: FONTS.PRIMARY,
    bold: true,
    color: COLORS.PLANVIEW_RED,
    valign: 'top',
  });

  // Text
  slide.addText(text, {
    x: SIZES.MARGIN + 0.139,
    y: y + 0.278,
    w: boxW - 0.278,
    h: boxH - 0.361,
    fontSize: 9,
    fontFace: FONTS.PRIMARY,
    color: COLORS.WHITE,
    valign: 'top',
    wrap: true,
  });
}

// ============================================================================
// TABLE LAYOUTS
// ============================================================================

/**
 * Add a feature comparison table.
 *
 * @param {Slide} slide - The slide
 * @param {Object[]} rows - Array of {capability, planview, targetprocess, talktrack}
 * @param {number} startY - Y position to start
 */
function addComparisonTable(slide, rows, startY = 0.833) {
  const cols = {
    capability: { w: 2.5, x: SIZES.MARGIN },
    planview: { w: 0.8, x: SIZES.MARGIN + 2.5 },
    targetprocess: { w: 0.8, x: SIZES.MARGIN + 3.3 },
    talktrack: { w: 3.1, x: SIZES.MARGIN + 4.1 },
  };

  const rowH = 0.306;
  const tableW = SIZES.SLIDE_WIDTH - (SIZES.MARGIN * 2);

  // Header row
  slide.addShape('rect', {
    x: SIZES.MARGIN,
    y: startY,
    w: tableW,
    h: rowH,
    fill: { color: COLORS.DARK_SLATE },
    line: { color: COLORS.DARK_SLATE },
  });

  const headerOpts = { fontSize: 8, fontFace: FONTS.PRIMARY, bold: true, color: COLORS.WHITE, align: 'center', valign: 'middle' };
  slide.addText('Capability', { ...headerOpts, x: cols.capability.x, y: startY, w: cols.capability.w, h: rowH });
  slide.addText('DPD', { ...headerOpts, x: cols.planview.x, y: startY, w: cols.planview.w, h: rowH });
  slide.addText('TP', { ...headerOpts, x: cols.targetprocess.x, y: startY, w: cols.targetprocess.w, h: rowH });
  slide.addText('Talk Track', { ...headerOpts, x: cols.talktrack.x, y: startY, w: cols.talktrack.w, h: rowH });

  // Data rows
  let rowY = startY + rowH;
  rows.forEach((row, i) => {
    const bgColor = i % 2 === 0 ? COLORS.WHITE : COLORS.LIGHT_GRAY;

    slide.addShape('rect', {
      x: SIZES.MARGIN,
      y: rowY,
      w: tableW,
      h: rowH,
      fill: { color: bgColor },
      line: { color: COLORS.BORDER_GRAY, width: 0.5 },
    });

    // Capability
    slide.addText(row.capability, {
      x: cols.capability.x + 0.083,
      y: rowY,
      w: cols.capability.w - 0.083,
      h: rowH,
      fontSize: 8,
      fontFace: FONTS.PRIMARY,
      bold: true,
      color: COLORS.DARK_SLATE,
      valign: 'middle',
    });

    // Planview score
    slide.addText(row.planview, {
      x: cols.planview.x,
      y: rowY,
      w: cols.planview.w,
      h: rowH,
      fontSize: 12,
      fontFace: FONTS.PRIMARY,
      color: row.planview.includes('✓✓') ? COLORS.GREEN : row.planview.includes('⚠') ? COLORS.GOLD : COLORS.BODY_TEXT,
      align: 'center',
      valign: 'middle',
    });

    // Targetprocess score
    slide.addText(row.targetprocess, {
      x: cols.targetprocess.x,
      y: rowY,
      w: cols.targetprocess.w,
      h: rowH,
      fontSize: 12,
      fontFace: FONTS.PRIMARY,
      color: row.targetprocess.includes('✓✓') ? COLORS.GREEN : row.targetprocess.includes('⚠') ? COLORS.GOLD : COLORS.DEEP_RED,
      align: 'center',
      valign: 'middle',
    });

    // Talk track
    slide.addText(row.talktrack, {
      x: cols.talktrack.x + 0.083,
      y: rowY,
      w: cols.talktrack.w - 0.083,
      h: rowH,
      fontSize: 7,
      fontFace: FONTS.PRIMARY,
      italic: true,
      color: COLORS.BODY_TEXT,
      valign: 'middle',
    });

    rowY += rowH;
  });
}

// ============================================================================
// UTILITY FUNCTIONS
// ============================================================================

/**
 * Convert points to inches.
 * @param {number} pt - Points
 * @returns {number} Inches
 */
function ptToIn(pt) {
  return pt / 72;
}

/**
 * Convert inches to points.
 * @param {number} in - Inches
 * @returns {number} Points
 */
function inToPt(inches) {
  return inches * 72;
}

// ============================================================================
// MODULE EXPORTS
// ============================================================================

module.exports = {
  // Constants
  COLORS,
  SIZES,
  FONTS,

  // Presentation factory
  createPresentation,

  // Slide helpers
  addSlide,
  addHeader,
  addFooter,
  addTitleSlide,

  // Card layouts
  addCard,
  addFourColumnCards,
  addThreeColumnCards,
  addTwoColumnCards,

  // Specialized layouts
  addPositioningBox,
  addStatBox,
  addDifferentiatorsBox,
  addPivotBox,
  addComparisonTable,

  // Utilities
  ptToIn,
  inToPt,
  registerFonts,
};
