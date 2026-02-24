# Accessibility Standards (WCAG 2.1 AA) - Deep Dive

## The Legal and Ethical Imperative

```
★ Accessibility is not a "nice-to-have" or "polish" item
  → It's a fundamental requirement for inclusive design

★ 15% of the world population experiences some form of disability
  → That's 1 billion people you exclude without accessibility

★ WCAG 2.1 AA is the legal standard in many jurisdictions
  → ADA (USA), EAA (Europe), AODA (Canada), EN 301549 (EU)

★ Accessibility benefits everyone
  → Same principles that help disabled users help all users

★ Accessible design is better design
  → Clearer content, better structure, more usable
```

## WCAG 2.1 Principles (POUR)

```yaml
Perceivable:
  Users must be able to perceive the information being presented
  → It can't be invisible to all of their senses

Operable:
  Users must be able to operate the interface
  → The interface cannot require interaction that a user cannot perform

Understandable:
  Users must be able to understand the information
  → The content or operation cannot be beyond their understanding

Robust:
  Users must be able to access the content as technologies advance
  → As technologies evolve, content remains accessible
```

## WCAG 2.1 AA Requirements Checklist

### 1. Text Alternatives (Perceivable)

```yaml
Non-Text Content:
  Requirement: All non-text content has text alternative
  Examples:
    - Images: Descriptive alt text
    - Charts: Data summary in text
    - Icons: Label or aria-label
    - Decorative images: alt="" (screen readers skip)

  Alt Text Writing:
    ✅ GOOD: "User profile photo of Jane Smith"
    ❌ BAD: "photo.jpg", "image", "picture"

    ✅ GOOD: "Bar chart showing 23% increase in Q3 revenue"
    ❌ BAD: "graph", "chart.png"

    Context Matters:
    - If image is link: Alt describes link destination
    - If image is button: Alt describes button action
    - If image is decorative: alt="" (empty string)

CAPTIONS:
  Requirement: Synchronized captions for all pre-recorded audio
  - For videos with speech: Provide accurate captions
  - For videos with no speech: Mention if relevant
  - Auto-captions (YouTube) not sufficient (errors common)

AUDIO DESCRIPTION:
  Requirement: Audio description for video content
  - Describe visual content not evident in audio
  - Include actions, scene changes, text on screen
```

### 2. Color and Contrast (Perceivable)

```yaml
CONTRAST RATIO:
  Requirement: Minimum contrast ratios for text and UI components
  - Normal text (under 18pt): 4.5:1 minimum
  - Large text (18pt+ or 14pt+ bold): 3:1 minimum
  - UI components (borders, focus indicators): 3:1 minimum
  - Graphical objects: 3:1 minimum

  Testing Tools:
    - axe DevTools (browser extension)
    - WAVE (webaccessibility.com)
    - Lighthouse (Chrome DevTools)
    - Contrast Checker (WebAIM)

COLOR ALONE:
  Requirement: Never use color alone to convey meaning
  - Add icons, text labels, patterns
  - Provide non-color alternatives

  Examples:
    ❌ BAD: "Red indicates errors, green indicates success"
    ✅ GOOD: "Red X icon + 'Error' text" and "Green checkmark + 'Success' text"

    ❌ BAD: Line chart with 3 colors (red/green/blue)
    ✅ GOOD: Different patterns + labels, or colorblind-safe palette
```

### 3. Keyboard Accessibility (Operable)

```yaml
KEYBOARD ACCESS:
  Requirement: All functionality available via keyboard
  - No mouse required for any action
  - Visible focus indicator on all interactive elements
  - Logical tab order (follows visual order)
  - No keyboard traps (user can always navigate away)

  Focus Visible:
    - Default browser focus is often insufficient
    - Add custom focus styles with outline or box-shadow
    - Never remove focus indicators (outline: 0 without replacement)

    ✅ GOOD CSS:
      .button:focus-visible {
        outline: 3px solid #005fcc;
        outline-offset: 2px;
      }

    ❌ BAD CSS:
      .button:focus {
        outline: none;  /* Removes focus indicator */
      }

NO KEYBOARD TRAPS:
  Requirement: User can navigate away from any component
  - Modals: Focus trap within modal, Esc to close
  - Menus: Arrow keys to navigate, Esc to close
  - Custom widgets: Follow WAI-ARIA patterns
  - Always provide way out

KEYBOARD SHORTCUTS:
  Requirement: Keyboard shortcuts can be turned off or remapped
  - Document standard shortcuts
  - Avoid single-key shortcuts (conflict with screen readers)
  - Provide on/off toggle for custom shortcuts
```

### 4. Timing and Content (Operable)

```yaml
TIMING ADJUSTABLE:
  Requirement: Users can control timed content
  - Pause, stop, hide content that moves, blinks, or auto-updates
  - Provide mechanism to extend time limits (if session timeout)
  - Exception: Real-time content (auctions, live events)

MOVING CONTENT:
  Requirement: Auto-updating content can be paused
  - Scrolling tickers, carousels, auto-refresh
  - Provide pause/stop button
  - Respect user's "prefers-reduced-motion" OS setting

SEIZURE DISORDERS:
  Requirement: No content flashes more than 3 times per second
  - Absolutely no flashing content between 3-50 Hz
  - Single flash area max 25% of screen
  - Critical for photosensitive epilepsy

HEADINGS AND LABELS:
  Requirement: Clear section headings and form labels
  - Use semantic heading structure (h1 → h2 → h3)
  - Don't skip heading levels (h1 → h3)
  - Every form input has associated label
  - Labels are clear, descriptive, adjacent to input
```

### 5. Navigable (Operable)

```yaml
WAYFINDING:
  Requirement: Multiple ways to locate content
  - Navigation menu
  - Site map
  - Search functionality
  - Breadcrumbs (for deep hierarchies)

LINK PURPOSE:
  Requirement: Link purpose is clear from text alone
  - Avoid "click here", "read more", "more"
  - Descriptive link text: "Download accessibility guide"
  - Unique link text (if multiple links to different URLs)

FOCUS ORDER:
  Requirement: Logical, intuitive navigation order
  - Follow visual layout (left-to-right, top-to-bottom)
  - Skip links for keyboard users (jump to main content)
  - Focus returns after modal closes

FOCUS VISIBLE:
  Requirement: Visible focus indicator for all interactive elements
  - Buttons, links, form inputs, custom widgets
  - High contrast (3:1 minimum against background)
  - Distinct from default browser styles
```

### 6. Readable and Understandable (Understandable)

```yaml
LANGUAGE OF PAGE:
  Requirement: Default human language programmatically determined
  - <html lang="en">
  - Changes in language declared: <span lang="es">Hola</span>

ON FOCUS:
  Requirement: No change of context on focus
  - Focus doesn't trigger actions unexpectedly
  - Exceptions: User-initiated change (dropdown menu)

ON INPUT:
  Requirement: No change of context on data entry
  - Submit button must be explicit (no submit on field change)
  - Exceptions: Search as you type (user expects it)

ERROR IDENTIFICATION:
  Requirement: Errors are identified and described
  - Clear error messages: "Invalid email" → "Email must contain @"
  - List all errors at top of form
  - Associate error with specific input (aria-describedby)

ERROR SUGGESTIONS:
  Requirement: Suggestions for fixing errors (when possible)
  - "Password must contain at least 8 characters"
  - "Email must be in format: user@example.com"
  - "Phone number: 10 digits, no spaces"

ERROR PREVENTION:
  Requirement: Prevention for legal/financial/data consequences
  - Review before submission (confirmation page)
  - Editable data review (summarize, allow corrections)
  - Confirmation for irreversible actions (delete, cancel)
```

### 7. Predictable (Understandable)

```yaml
CONSISTENT NAVIGATION:
  Requirement: Navigation is consistent across pages
  - Same navigation in same location
  - Same order, same labels
  - Exceptions: When user initiates change

CONSISTENT IDENTIFICATION:
  Requirement: Consistent identification of components
  - Same icon always means same thing
  - Same terminology (not "profile" vs "account" vs "settings")
  - Consistent behavior across pages
```

### 8. Input Assistance (Understandable)

```yaml
LABELS OR INSTRUCTIONS:
  Requirement: Labels or instructions for content input
  - Every form input has visible label
  - Required fields indicated (not just red border)
  - Input format specified (date: MM/DD/YYYY)
  - Examples for complex inputs

DEFAULT VALUES:
  Requirement: Default values are not required unless user can change
  - Select dropdowns: First option is not auto-selected
  - Checkboxes: Not checked by default
  - Radio buttons: No default selection unless there's safe default

AUTOCOMPLETE:
  Requirement: Where appropriate, autocomplete form fields
  - Use HTML autocomplete attributes
  - Suggest based on common patterns
  - Allow user to type custom value (not just select)
```

### 9. Compatible (Robust)

```yaml
COMPATIBLE:
  Requirement: Maximize compatibility with current/future user agents
  - Use valid HTML (semantic elements)
  - Use ARIA for custom components
  - Don't break accessibility with JavaScript
  - Test with real assistive technologies

NAME, ROLE, VALUE:
  Requirement: Assistive technologies can access name, role, value
  - Native elements preferred (button, not div with click handler)
  - Custom components need ARIA roles, states, properties
  - Test with screen reader (NVDA, JAWS, VoiceOver)
```

## ARIA Usage Guidelines

```yaml
WHEN TO USE ARIA:
  - Native HTML not sufficient for custom component
  - Interactive elements not natively supported
  - Providing additional context or descriptions

WHEN NOT TO USE ARIA:
  ✅ Native HTML is better (button, not role="button")
  ✅ Visual-only elements (use CSS, not ARIA)
  ✅ When it would duplicate native semantics

ARIA ROLES:
  - landmark: header, nav, main, footer, aside, search
  - widget: button, dialog, menu, tab, tooltip
  - composite: grid, listbox, tree
  - document: article, section, heading, list, listitem

ARIA STATES AND PROPERTIES:
  - aria-expanded: true/false/undefined (toggle elements)
  - aria-selected: true/false/undefined (tabs, lists)
  - aria-checked: true/false/mixed (checkboxes)
  - aria-disabled: true/false (form elements)
  - aria-hidden: true/false (hide from screen readers)
  - aria-label: Accessible name (when visible label insufficient)
  - aria-describedby: Reference to description ID
  - aria-live: polite/assertive/off (announce dynamic content)
```

## Screen Reader Testing

### Primary Screen Readers

```yaml
Windows:
  - NVDA (Free, recommended for testing)
  - JAWS (Commercial, common in enterprise)
  - Narrator (Built into Windows 10/11)

macOS:
  - VoiceOver (Built-in, Cmd+F5 to enable)

iOS:
  - VoiceOver (Built-in accessibility feature)

Android:
  - TalkBack (Built-in accessibility feature)
```

### Testing Checklist

```yaml
SETUP:
  ☐ Enable screen reader
  ☐ Learn basic navigation (arrows, Tab, shortcuts)
  ☐ Disable visual output (close eyes or cover screen)

NAVIGATION:
  ☐ Navigate by heading (H key for jumps)
  ☐ Navigate by landmark (semicolons for next landmark)
  ☐ Navigate by link (L for next link)
  ☐ Navigate by form control (Tab between inputs)

CONTENT:
  ☐ All images have alt text or marked decorative
  ☐ Headings form logical outline
  ☐ Lists are announced as lists
  ☐ Links have descriptive names (not "click here")

INTERACTIVE:
  ☐ All buttons are announced as buttons
  ☐ Form inputs have associated labels
  ☐ Error messages are announced
  ☐ Focus indicators visible and announced

DYNAMIC CONTENT:
  ☐ Page updates announced (aria-live regions)
  ☐ Modal dialogs announced and focus moves
  ☐ Auto-complete options announced
```

## Accessibility Testing Tools

```yaml
AUTOMATED TOOLS (First Pass, Not Sufficient):
  - axe DevTools (Chrome/Firefox extension)
  - WAVE (webaim.org/resources/wave)
  - Lighthouse (Chrome DevTools, Audits panel)
  - Siteimprove (Chrome extension)

MANUAL TESTING (Required):
  - Keyboard-only navigation (unplug mouse)
  - Screen reader testing (NVDA, VoiceOver)
  - Zoom testing (200% zoom in browser)
  - Color contrast checking (manual verification)

USER TESTING (Gold Standard):
  - Include people with disabilities in testing
  - Remote testing with Fable, AccessWorks
  - Local disability organizations
  - Internal team members with disabilities
```

## Common Accessibility Issues and Fixes

```yaml
ISSUE: Missing Alt Text
  Fix: Add descriptive alt attribute
  <img src="dashboard.png" alt="Revenue dashboard showing 23% increase">

ISSUE: Low Color Contrast
  Fix: Increase contrast to 4.5:1 minimum
  Use contrast checker, adjust colors

ISSUE: Keyboard Traps
  Fix: Ensure focus can move away from all components
  Test with Tab key, add Esc handlers for modals

ISSUE: Missing Form Labels
  Fix: Associate label with input
  <label for="email">Email</label>
  <input id="email" type="text">

ISSUE: Auto-Playing Media
  Fix: Don't auto-play, or provide pause button
  Respect prefers-reduced-motion

ISSUE: Poor Heading Structure
  Fix: Use semantic headings, don't skip levels
  <h1>Page Title</h1>
  <h2>Section Title</h2>
  <h3>Subsection</h3>

ISSUE: Custom Components Without ARIA
  Fix: Use native HTML or add proper ARIA
  <button role="button" aria-pressed="false">Like</button>

ISSUE: Dynamic Content Not Announced
  Fix: Use aria-live regions
  <div aria-live="polite" aria-atomic="true">
    Status updates announced here
  </div>
```

## Accessibility Statement Template

```markdown
# Accessibility Statement

[Company/Product Name] is committed to ensuring digital accessibility
for people with disabilities. We are continually improving the user
experience for everyone and applying the relevant accessibility
standards.

## Conformance Status

The Web Content Accessibility Guidelines (WCAG) defines requirements for
designers and developers to improve accessibility for people with
disabilities. [Company/Product Name] is partially conformant with WCAG
2.1 level AA. Partially conformant means that some parts of the content
do not fully conform to the accessibility standard.

## Feedback

We welcome your feedback on the accessibility of [Product Name]. Please
let us know if you encounter accessibility barriers:

- Email: [accessibility@company.com]
- Phone: [phone number]
- Visit us: [physical address]

We try to respond to accessibility feedback within [X] business days.
```

## Resources

**Standards and Guidelines**:
- WCAG 2.1: w3.org/WAI/WCAG21/quickref
- WAI-ARIA Authoring Practices: w3.org/WAI/ARIA/apg
- Section 508: section508.gov

**Testing Tools**:
- axe DevTools: deque.com/axe
- WAVE: wave.webaim.org
- Lighthouse: developers.google.com/web/tools/lighthouse
- Contrast Checker: webaim.org/resources/contrastchecker

**Learning Resources**:
- WebAIM (webaim.org): Comprehensive accessibility guides
- A11Y Project (a11yproject.com): Community accessibility checklist
- Smashing Magazine (smashingmagazine.com): Accessibility articles
- Inclusive Components (inclusive-components.design): Accessible patterns

**Templates**:
- See `templates/` directory for:
  - accessibility-audit-checklist.md
  - aria-patterns-reference.md
  - accessible-component-library.md
  - user-testing-script-accessibility.md
