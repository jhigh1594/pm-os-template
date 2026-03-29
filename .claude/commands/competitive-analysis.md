# /competitive-analysis — Competitive Landscape Analysis

Research and analyze your competitive landscape. Identifies direct and indirect competitors, maps positioning, and surfaces differentiation opportunities.

## Invocation

```
/competitive-analysis AI-powered project management tools
/competitive-analysis Our product vs Notion, Asana, and Monday.com
/competitive-analysis [upload a competitor list or market brief]
```

## Grounded Research Principles

**Critical: Claims must be backed by facts and sources.**

1. **Source Hierarchy** — Not all sources are equal:
   - **Tier 1 (High Trust)**: Earnings calls, regulatory filings, independent analyst reports (Gartner/Forrester)
   - **Tier 2 (Medium Trust)**: Customer reviews (G2, Capterra), employee reviews (Glassdoor), press releases
   - **Tier 3 (Low Trust)**: Competitor marketing sites, vendor blogs — use ONLY for positioning analysis, never as factual claims

2. **No Fabrication** — DO NOT fabricate feature names, pricing numbers, dates, or capabilities. If information is not available in the sources, say so explicitly.

3. **Data Currency** — All competitive intelligence must be time-anchored. Include a Data Currency field in every output (date research was conducted). Default time bound: "Over the past 12 months unless otherwise specified."

4. **Training-Data Caveat** — If no live research tools were used, include this block at the top of the output:
   > Claims below are based on training data as of [model cutoff]. Verify before use in sales or strategy.

---

## Workflow

### Step 1: Understand the Competitive Context

Ask:
- What is your product? What category does it compete in?
- Any specific competitors you want analyzed? Or should I identify them?
- What's the lens? (feature comparison, positioning, pricing, go-to-market)
- What will you use this analysis for? (strategy, sales enablement, investor pitch, product roadmap)

### Step 2: Identify Competitors

Apply the **competitive-analysis** skill:

- Identify 5 direct competitors (same category, same buyer)
- Identify 2-3 indirect competitors (different approach, same job-to-be-done)
- Note emerging/disruptive players if relevant
- Use web research to gather current information. If research tools are unavailable, label all claims with confidence tier and note they are based on training data.

### Step 3: Analyze Each Competitor

For each competitor:
- **Positioning**: How they describe themselves, target audience, key messaging
- **Strengths**: What they do well, where they win (cite source tier)
- **Weaknesses**: Where they fall short, common complaints (cite source tier)
- **Pricing**: Model and price points (if public; note "pricing page as of [date]" or "contact sales")
- **Market traction**: Funding, team size, customer base signals (cite Crunchbase, LinkedIn, etc.)
- **Recent moves**: New features, partnerships, pivots (cite release notes, press)
- **Confidence & Sources**: Tier 1/2/3, specific document or "Single-source — verify"

### Step 4: Generate Competitive Analysis

```
## Competitive Analysis: [Your Product/Market]

**Data Currency**: [Date research was conducted — e.g., 2026-03-09]
**Method**: [Live research via web tools / Training data — verify before use]

### Market Overview
[2-3 sentences on market dynamics, trends, and where it's heading]

### Competitive Landscape
| Competitor | Category | Target | Positioning | Strength | Weakness | Confidence & Sources |
|-----------|----------|--------|-------------|----------|----------|----------------------|
| ... | ... | ... | ... | ... | ... | Tier X, [source] |

### Feature Comparison Matrix
| Capability | Your Product | Competitor A | Competitor B | Competitor C |
|-----------|-------------|-------------|-------------|-------------|

### Positioning Map
[2x2 matrix showing competitive positioning on key dimensions]

### Differentiation Opportunities
1. **[Opportunity]** — [why it's defensible and valuable]
2. ...

### Competitive Threats
1. **[Threat]** — [what to watch for, recommended response]
2. ...

### Recommendations
- **Double down on**: [your unique advantages]
- **Close the gap on**: [table-stakes features you're missing]
- **Ignore**: [competitor moves that aren't worth responding to]

### Sources
- [source 1] — Tier [1/2/3]
- [source 2] — Tier [1/2/3]
```

Save as markdown.

### Step 5: Offer Next Steps

- "Want me to **create a battlecard** for sales against a specific competitor?"
- "Should I **develop positioning** that differentiates from the top competitors?"
- "Want me to **identify feature gaps** to close and add to the roadmap?"

---

## Notes

- Web research is used for current competitor data — results are as fresh as available sources
- Distinguish between "table stakes" (must-have to compete) and "differentiators" (must-have to win)
- Don't just list features — analyze *why* competitors make the choices they make
- Pricing intelligence should note whether pricing is public, usage-based, or requires sales contact
- Update this analysis quarterly — competitive landscapes shift fast
- Apply `.claude/skills/competitive-analysis/SKILL.md` and `.claude/agents/competitive-research.md` when doing deep competitive work.
