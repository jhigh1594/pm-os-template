# Dashboard Design Patterns - Deep Dive

## Dashboard Types & Purposes

### Three Dashboard Genres

```yaml
Strategic Dashboards:
  Purpose: High-level KPI monitoring for executives
  Audience: C-suite, VPs, Directors
  Update Frequency: Daily, weekly, monthly
  Data Granularity: Aggregated, trends over time
  Key Metrics: Revenue, growth, high-level health indicators
  Example: CEO Scorecard, Board Dashboard

  Design Principles:
    - Few metrics (5-7 max)
    - Trends over time (sparklines, % change)
    - Color only for meaningful deviation
    - Drill-down available but not prominent

Analytical Dashboards:
  Purpose: Data exploration, root cause analysis
  Audience: Analysts, Product Managers, Operations
  Update Frequency: Real-time to hourly
  Data Granularity: Detailed, filterable, sliceable
  Key Metrics: Conversion rates, cohort analysis, funnel metrics
  Example: Analytics Platform, Conversion Dashboard

  Design Principles:
    - Rich interactivity (filter, sort, drill)
    - Multiple chart types for different questions
    - Comparison capabilities (vs period, vs cohort)
    - Export functionality

Operational Dashboards:
  Purpose: Monitor day-to-day operations, react to issues
  Audience: Support teams, operations managers, RTEs
  Update Frequency: Real-time or near real-time
  Data Granularity: Current status, recent activity
  Key Metrics: Ticket volume, system health, SLA compliance
  Example: Support Dashboard, System Status, Dependency View

  Design Principles:
    - Current status prominence (what's happening NOW)
    - Alerts for anomalies (but not alert fatigue)
    - Quick actions (respond, assign, investigate)
    - Status at a glance (color, indicators)
```

## Dashboard Layout Patterns

### The F-Pattern Layout

```
┌─────────────────────────────────────┐
│ KPI 1    │ KPI 2    │ KPI 3        │ ← Primary eye scan
├───────────┼───────────┼──────────────┤
│           │           │              │
│  Chart    │  Chart    │   Chart      │ ← Secondary content
│           │           │              │
├───────────┴───────────┴──────────────┤
│                                     │
│            Data Table               │ ← Detailed data
│                                     │
└─────────────────────────────────────┘

Users scan F-shape: Top row → Down left → Across middle
Place highest priority content in scan path
```

### The Z-Pattern Layout

```
Top Entry ───────────────► CTA/Action
    │                            │
    │                            │
    ▼                            ▼
Key Visual/Chart          Supporting Detail
    │                            │
    │                            │
    ▼                            ▼
Supporting Info ◄───────── Primary Action

Great for: Narrative dashboards, guided analytics
Less ideal: Complex data exploration
```

### Card-Based Grid (Recommended for SaaS)

```
┌────────────┐ ┌────────────┐ ┌────────────┐
│  KPI Card  │ │  KPI Card  │ │  KPI Card  │
│  Primary   │ │ Secondary  │ │ Tertiary   │
├────────────┤ ├────────────┤ ├────────────┤
│            │ │            │ │            │
│   Chart    │ │   Chart    │ │   Chart    │
│            │ │            │ │            │
└────────────┘ └────────────┘ └────────────┘

Benefits:
- Flexible (responsive, variable card sizes)
- Modular (add/remove without reflow)
- Familiar (Material Design, Ant Design patterns)
- Scannable (clear visual hierarchy)

Considerations:
- Need grid system (8px base unit recommended)
- Card elevation/shadows for depth
- Consistent card padding and spacing
```

## Chart Selection Guide

### When to Use Which Chart

```
COMPARISON (Ranking, difference between values)
├─ Bar Chart (Horizontal or Vertical)
│  Use for: Comparing values across categories
│  Best for: Up to 10-15 categories
│  Avoid for: Time series (use line instead)
│  Example: Revenue by product, teams by velocity
│
├─ Grouped Bar Chart
│  Use for: Comparing series across categories
│  Best for: 2-3 series max
│  Avoid for: More than 3 series (becomes unreadable)
│  Example: This month vs last month by region
│
└─ Stacked Bar Chart
   Use for: Part-to-whole relationships over time
   Best for: 3-5 segments max
   Avoid for: Comparing totals (hard to read middle segments)
   Example: Ticket status by week (open/in-progress/closed)

TREND OVER TIME (Change, patterns, seasonality)
├─ Line Chart
│  Use for: Continuous data over time
│  Best for: Multiple data series, trends
│  Avoid for: Categorical data (use bar instead)
│  Example: Active users over 6 months, revenue trend
│
├─ Area Chart
│  Use for: Magnitude over time + cumulative
│  Best for: Single series (stacked for multiple)
│  Avoid for: Precise comparison (hard to read)
│  Example: Cumulative revenue, user growth
│
└─ Sparkline
   Use for: Trend in minimal space (KPI cards)
   Best for: Context alongside primary metric
   Avoid for: Detailed analysis (too small)
   Example: Revenue trend on KPI card

DISTRIBUTION (Spread, outliers, frequency)
├─ Histogram
│  Use for: Frequency distribution of continuous data
│  Best for: Understanding data shape (normal, skewed)
│  Avoid for: Categorical data (use bar instead)
│  Example: Ticket resolution time distribution
│
├─ Box Plot (Box and Whisker)
│  Use for: Statistical distribution, outliers
│  Best for: Technical audiences, comparing distributions
│  Avoid for: Non-technical users (confusing)
│  Example: Cycle time distribution across teams
│
└─ Violin Plot
   Use for: Distribution shape + statistics
   Best for: Technical analysis, detailed exploration
   Avoid for: Executive dashboards (too complex)
   Example: Team velocity distributions

CORRELATION (Relationship between two variables)
├─ Scatter Plot
│  Use for: Relationship between two numeric variables
│  Best for: Finding patterns, clusters, outliers
│  Avoid for: Categorical data (use other charts)
│  Example: Team size vs. cycle time, features vs. bugs
│
└─ Bubble Chart
   Use for: Three variables (x, y, size)
   Best for: Multivariate comparison
   Avoid for: More than 20-30 data points (becomes messy)
   Example: Teams (x: velocity, y: quality, size: team size)

PART-TO-WHOLE (Composition, proportion, breakdown)
├─ Pie/Donut Chart
│  Use for: Simple part-to-whole (rarely the best choice)
│  Best for: 3-5 segments, rough comparison
│  Avoid for: More than 5 segments, precise comparison
│  Example: Browser share (3-4 browsers)
│
├─ Treemap
│  Use for: Hierarchical part-to-whole
│  Best for: Many categories, nested relationships
│  Avoid for: Precise comparison (hard to read areas)
│  Example: Disk usage by folder, product revenue by category
│
└─ Stacked Bar
   Use for: Part-to-whole over time
   Best for: Showing composition change
   Avoid for: Comparing totals or middle segments
   Example: Revenue by product over months

RELATIONSHIPS & CONNECTIONS
├─ Network Graph
│  Use for: Relationships, connections, dependencies
│  Best for: Seeing clusters, hubs, paths
│  Avoid for: Large networks (becomes hairball)
│  Example: Dependency graph, social network
│
└─ Sankey Diagram
   Use for: Flow, multistage processes
   Best for: Journey visualization, funnels with branching
   Avoid for: More than 5-6 stages (becomes unreadable)
   Example: User journey from acquisition to retention

GEOGRAPHIC
├─ Choropleth Map
│  Use for: Regional data comparison
│  Best for: Countries, states, provinces
│  Avoid for: Precise comparison (area distorts perception)
│  Example: Sales by country, users by state
│
└─ Dot Map / Hex Map
   Use for: Location-based data with precision
   Best for: Cities, specific locations
   Avoid for: Too many points (performance, readability)
   Example: Store locations, event attendance
```

### Chart Anti-Patterns

```yaml
❌ AVOID:
  - 3D Effects: Distort data perception, harder to read
  - Dual Y-Axes: Confusing, often manipulative
  - Pie Charts for Comparison: Hard to compare angles
  - Red/Green Only: Color blindness inaccessibility
  - Missing Context: No baseline, no time period labels
  - Too Many Data Series: Chart becomes unreadable
  - Decorative Elements: Icons, illustrations that distract

✅ INSTEAD:
  - 2D, flat design: Clean, accurate, accessible
  - Small Multiples: Multiple charts for comparison
  - Bar Charts: For most comparisons
  - Blue/Orange or Diverging Scales: Colorblind-friendly
  - Clear Context: Time periods, baselines, comparison notes
  - Series Limits: 3-5 max, use small multiples for more
  - Data-Ink Ratio: Remove everything that doesn't convey data
```

## Color in Data Visualization

### Sequential Scales (Ordered Data)

```yaml
Use For: Intensity, magnitude (low to high)
Examples: Heat maps, choropleth maps, density

Single-Hue Sequential (Best for accessibility):
  - Light to dark of one color
  - Example: Light blue → Dark blue
  - Benefits: Colorblind-friendly, professional

Diverging Scales (Deviation from midpoint):
  Use For: Positive/negative, above/below average
  Examples: Profit/loss, temperature anomaly, sentiment

  Pattern:
    - Cool color (low) → Neutral (mid) → Warm color (high)
    - Example: Blue → White/Yellow → Orange/Red
    - Benefits: Clear directionality, midpoint emphasis

  Colorblind-Safe Diverging Palettes:
    - Blue-Orange (most accessible)
    - Purple-Orange (good contrast)
    - Teal-Pink (distinctive)
```

### Categorical Scales (No inherent order)

```yaml
Use For: Categories, groups, nominal data
Examples: Product lines, teams, statuses

Best Practices:
  - Use distinct colors (6-8 max)
  - Maintain consistent color mapping across views
  - Use colorblind-safe palettes
  - Avoid red/green as primary categorical colors

Recommended Palettes (Colorblind-Safe):
  - Tableau 10: Blue, Orange, Green, Red, Teal, Yellow, Purple,
                 Pink, Brown, Grey (tested for accessibility)
  - Set2 (ColorBrewer): Muted, professional palette
  - Google Material: Designed for accessibility
```

### Semantic Color (Status, Action)

```yaml
Status Colors (Universal meaning):
  Success: Green (but also checkmark, "Complete")
  Warning: Yellow/Orange (caution, attention needed)
  Error: Red (destructive, critical issues)
  Info: Blue (neutral information, system status)
  Neutral: Grey (disabled, unavailable, inactive)

Best Practices:
  - Never rely on color alone (add icons, labels)
  - Consider cultural associations (red ≠ bad everywhere)
  - Use semantic colors consistently
  - Provide color key for all categorical data
```

## Dashboard Interactivity

### Interactive Elements

```yaml
Filtering:
  Purpose: Reduce data to relevant subset
  Patterns:
    - Dropdown filters (single or multi-select)
    - Date range pickers (preset ranges + custom)
    - Search within lists (type-ahead filtering)
    - Checkbox groups (category selection)

  Best Practices:
    - Show active filters clearly
    - Allow filter combinations (AND logic)
    - Preserve filters on navigation
    - Provide "Clear all" option
    - Show result count after filtering

Sorting:
  Purpose: Reorder data by priority
  Patterns:
    - Column headers (click to sort, arrow indicator)
    - Sort dropdown (custom sort logic)
    - Drag-and-drop (manual ordering)

  Best Practices:
    - Show sort direction (↑↓ arrows)
    - Indicate current sort column
    - Support multi-sort (shift+click for secondary)
    - Remember sort preference

Drill-Down:
  Purpose: Navigate from summary to detail
  Patterns:
    - Click chart element → filtered detail view
    - Click KPI card → detailed report
    - Breadcrumb navigation (back to summary)

  Best Practices:
    - Clear indication of drill availability (cursor, hover)
    - Back navigation (breadcrumbs, back button)
    - Preserve context (filters, selections)
    - Progressive disclosure (don't show everything at once)

Export:
  Purpose: Share or analyze data externally
  Formats:
    - CSV (raw data, spreadsheet compatible)
    - PDF (formatted reports, presentations)
    - Image (PNG, social sharing)
    - Excel (with formatting, formulas)

  Best Practices:
    - Export what you see (respect filters)
    - Filename includes context (date, range)
    - Progress indicator for large exports
    - Notification when complete
```

### Dashboard Controls

```yaml
Layout Controls:
  - Customize dashboard (add/remove cards)
  - Resize cards (drag handles)
  - Reorder cards (drag-and-drop)
  - Save custom layouts (per user)

Time Controls:
  - Date range selector (preset + custom)
  - Time granularity (day/week/month/quarter)
  - Comparison periods (vs last period, vs last year)
  - Real-time toggle (live vs snapshot)

View Controls:
  - Chart type switcher (same data, different viz)
  - Toggle data series (show/hide)
  - Zoom controls (for time series, detailed exploration)
  - Fullscreen mode (presentation mode)
```

## Dashboard Anti-Patterns to Avoid

```yaml
❌ DATA VOMIT
  Problem: Showing everything because you can
  Result: Overwhelmed users, decision paralysis
  Fix: Ruthlessly prioritize, show what matters now

❌ ALERT FATIGUE
  Problem: Everything is red/alerting, nothing is urgent
  Result: Users ignore all alerts
  Fix: Alert for genuine anomalies, use status dashboards

❌ ONE-SIZE-FITS-ALL
  Problem: Single dashboard for all users/roles
  Result: Power users bored, novices overwhelmed
  Fix: Role-based dashboards, customizable views

❌ DECORATION OVER DATA
  Problem: Pretty but not useful
  Result: Trust issues, wasted screen space
  Fix: Data-ink ratio, every element earns its place

❌ MISSING CONTEXT
  Problem: Numbers without meaning (no baseline, comparison)
  Result: Users can't interpret (is this good or bad?)
  Fix: Add context (vs last period, target, benchmark)

❌ SLOW DASHBOARDS
  Problem: Load times >3 seconds
  Result: Frustration, abandonment
  Fix: Optimize queries, cache data, progressive loading

❌ NON-RESPONSIVE
  Problem: Desktop-only design
  Result: Unusable on tablets/mobile
  Fix: Mobile-first, responsive breakpoints

❌ UNCLEAR ACTIONS
  Problem: Data without next steps
  Result: Dashboard as monitoring, not driving action
  Fix: Clear CTAs, drill-downs, inline actions

❌ INCONSISTENT PATTERNS
  Problem: Different chart types for same data type
  Result: Cognitive load, learning curve
  Fix: Establish conventions, document patterns

❌ IGNORING EDGE CASES
  Problem: No data, error states, empty results
  Result: Broken experience, trust issues
  Fix: Design for zero-state, error states, no results
```

## Dashboard Evaluation Checklist

```yaml
CLARITY:
  ☐ Purpose is obvious (what is this dashboard for?)
  ☐ Most important information is most prominent
  ☐ Visual hierarchy guides attention
  ☐ Labels are clear, no jargon or ambiguity
  ☐ Chart types appropriate for data

USABILITY:
  ☐ Load time under 3 seconds
  ☐ Responsive design (mobile, tablet, desktop)
  ☐ Keyboard navigation works
  ☐ Interactive elements are discoverable
  ☐ Export options available

CONTEXT:
  ☐ Data has baselines/comparisons
  ☐ Time periods are labeled
  ☐ Targets or benchmarks shown where relevant
  ☐ Data sources are clear
  ☐ Last update time is visible

ACCESSIBILITY:
  ☐ Color contrast meets WCAG AA (4.5:1)
  ☐ Not relying on color alone
  ☐ Screen reader compatible
  ☐ Keyboard accessible
  ☐ Text zoom to 200% works

ACTIONABILITY:
  ☐ Clear next steps (what should user do?)
  ☐ Drill-down to detail available
  ☐ Filters allow focusing on relevant data
  ☐ Inline actions (quick responses)
  ☐ Alerts are meaningful, not noisy

PERFORMANCE:
  ☐ Optimized queries (under 3s load)
  ☐ Data caching where appropriate
  ☐ Progressive loading for large datasets
  ☐ Pagination for long tables
  ☐ Lazy loading for charts
```

## Resources

**Tools**:
- Chart libraries: D3.js, Chart.js, Plotly, Recharts, Victory
- Dashboard platforms: Tableau, Looker, Power BI, Metabase
- Design tools: Figma, Sketch, Adobe XD (prototyping)

**Books**:
- *Storytelling with Data* by Cole Nussbaumer Knaflic
- *Information Dashboard Design* by Stephen Few
- *The Functional Art* by Alberto Cairo

**Templates**:
- See `templates/` directory for:
  - dashboard-wireframe-kit.md
  - kpi-card-patterns.md
  - chart-selection-decision-tree.md
