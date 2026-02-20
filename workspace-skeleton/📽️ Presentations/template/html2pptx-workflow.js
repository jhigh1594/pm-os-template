/**
 * Planview HTML-to-PPTX Workflow Script
 *
 * This script demonstrates the recommended workflow for creating
 * Planview presentations using HTML templates and html2pptx.
 *
 * USAGE:
 *   node html2pptx-workflow.js
 *
 * WORKFLOW:
 *   1. Create HTML files for each slide (use templates from html-templates/)
 *   2. Convert HTML to PPTX using html2pptx library
 *   3. Generate thumbnails for visual validation
 *
 * BENEFITS OVER DIRECT PPTXGENJS:
 *   - CSS flexbox handles alignment automatically
 *   - Visual preview in browser before conversion
 *   - Playwright renders accurate pixel positions
 *   - Less manual coordinate calculation
 */

const pptxgen = require('pptxgenjs');
const html2pptx = require('/Users/jhigh/.claude/skills/pptx/scripts/html2pptx.js');
const fs = require('fs');
const path = require('path');

// Template directory
const TEMPLATES_DIR = __dirname;
const HTML_TEMPLATES = path.join(TEMPLATES_DIR, 'html-templates');

// Planview logo path (use /tmp to avoid emoji path encoding issues)
const LOGO_PATH = path.join(TEMPLATES_DIR, 'planview-logo.png');
const LOGO_TMP_PATH = '/tmp/planview-logo.png';

/**
 * Copy Planview logo to /tmp for use in HTML slides.
 * This avoids path encoding issues with emoji characters in the workspace path.
 * Call this before processing any HTML slides.
 */
function ensureLogoAvailable() {
  if (!fs.existsSync(LOGO_TMP_PATH)) {
    fs.copyFileSync(LOGO_PATH, LOGO_TMP_PATH);
    console.log('Logo copied to /tmp for html2pptx processing');
  }
}

/**
 * Create a Planview presentation from HTML slides.
 *
 * @param {Object} options - Presentation options
 * @param {string} options.title - Presentation title
 * @param {string} options.author - Author name
 * @param {string[]} options.htmlFiles - Array of HTML file paths
 * @param {string} options.outputPath - Output PPTX file path
 * @returns {Promise<void>}
 */
async function createPresentation(options) {
  const { title, author, htmlFiles, outputPath } = options;

  // Ensure logo is available in /tmp
  ensureLogoAvailable();

  // Create presentation with 16:9 layout
  const pptx = new pptxgen();
  pptx.author = author || 'Planview';
  pptx.title = title || 'Planview Presentation';
  pptx.company = 'Planview, Inc.';
  pptx.layout = 'LAYOUT_16x9';

  // Process each HTML file
  for (const htmlFile of htmlFiles) {
    console.log(`Processing: ${htmlFile}`);
    const { slide, placeholders } = await html2pptx(htmlFile, pptx);

    // Add charts to placeholders if needed
    if (placeholders.length > 0) {
      console.log(`  Found ${placeholders.length} placeholder(s)`);
      // Example: slide.addChart(pptx.charts.BAR, data, placeholders[0]);
    }
  }

  // Save presentation
  await pptx.writeFile({ fileName: outputPath });
  console.log(`Created: ${outputPath}`);
}

/**
 * Load an HTML template and replace placeholders with content.
 *
 * @param {string} templateName - Template filename (e.g., '4-column-cards.html')
 * @param {Object} replacements - Key-value pairs to replace {{PLACEHOLDER}} patterns
 * @returns {string} Processed HTML content
 */
function loadTemplate(templateName, replacements) {
  const templatePath = path.join(HTML_TEMPLATES, templateName);
  let html = fs.readFileSync(templatePath, 'utf8');

  // Replace all {{KEY}} patterns with values
  for (const [key, value] of Object.entries(replacements)) {
    const regex = new RegExp(`{{${key}}}`, 'g');
    html = html.replace(regex, value || '');
  }

  return html;
}

/**
 * Save HTML content to a temporary file for html2pptx processing.
 *
 * @param {string} htmlContent - HTML content
 * @param {string} filename - Output filename
 * @returns {string} Absolute path to saved file
 */
function saveHtmlSlide(htmlContent, filename) {
  const tmpDir = '/tmp/planview-slides';
  if (!fs.existsSync(tmpDir)) {
    fs.mkdirSync(tmpDir, { recursive: true });
  }

  const filePath = path.join(tmpDir, filename);
  fs.writeFileSync(filePath, htmlContent);
  return filePath;
}

// Example usage
async function example() {
  // Create a simple 4-column cards slide
  const html = loadTemplate('4-column-cards.html', {
    TITLE: 'Strategic Priorities',
    TAGLINE: 'Q1 2026 ROADMAP',
    CAT1: 'GROWTH',
    HEADLINE1: 'Expand Market Presence',
    BULLET1_1: 'Launch in 3 new regions',
    BULLET1_2: 'Partner program expansion',
    BULLET1_3: '30% ARR growth target',
    CAT2: 'INNOVATION',
    HEADLINE2: 'AI-Powered Features',
    BULLET2_1: 'Anvi intelligent assistant',
    BULLET2_2: 'Predictive analytics',
    BULLET2_3: 'Automated workflows',
    CAT3: 'CUSTOMER',
    HEADLINE3: 'Delight & Retain',
    BULLET3_1: 'NPS target: 50+',
    BULLET3_2: 'Reduce churn by 15%',
    BULLET3_3: 'Customer advisory board',
    CAT4: 'OPERATIONS',
    HEADLINE4: 'Scale Efficiently',
    BULLET4_1: 'Platform reliability 99.9%',
    BULLET4_2: 'Reduce support tickets',
    BULLET4_3: 'Self-service capabilities'
  });

  const slidePath = saveHtmlSlide(html, 'example-slide.html');

  await createPresentation({
    title: 'Example Planview Deck',
    author: 'Planview Product Management',
    htmlFiles: [slidePath],
    outputPath: '/tmp/planview-example.pptx'
  });
}

// Export functions for use in other scripts
module.exports = {
  createPresentation,
  loadTemplate,
  saveHtmlSlide,
  ensureLogoAvailable
};

// Run example if called directly
if (require.main === module) {
  ensureLogoAvailable();
  example().catch(console.error);
}
