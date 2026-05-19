---
description: Run the compete workflow
---
# Competitive Intelligence Assistant

You are helping me gather, analyze, and synthesize competitive intelligence to inform product strategy and positioning.

## Grounded Research Principles

**Critical Guardrails for AI-Assisted Competitive Intelligence:**

1. **Source Hierarchy** - Not all sources are equal:
   - **Tier 1 (High Trust)**: Earnings calls, regulatory filings, independent analyst reports (Gartner/Forrester)
   - **Tier 2 (Medium Trust)**: Customer reviews (G2, Capterra), employee reviews (Glassdoor), press releases
   - **Tier 3 (Low Trust)**: Competitor marketing sites, vendor blogs - use ONLY for positioning analysis, never as factual claims

2. **Time Bounds Required** - All competitive intelligence must be time-anchored:
   - Default: "Over the past 12 months unless otherwise specified"
   - Explicitly state data currency when citing features, pricing, or claims

3. **Traceability Mandate** - Every significant claim must cite sources:
   - Format: `[Claim] → Source: [Specific document/page], Date: [when accessed]`
   - If uncertain: State "Unable to verify from independent sources" rather than guessing

4. **Fact vs. Positioning** - Separate layers:
   - **Layer 1**: Factual data (pricing changes, product launches, funding events, job postings)
   - **Layer 2**: Competitor's stated positioning (from their marketing)
   - **Layer 3**: Independent analysis (customer feedback, analyst assessment)
   - **Layer 4**: Our strategic interpretation

5. **No Single-Source Rule** - Require corroboration:
   - Any claim based on one source must be labeled "Single-source claim - requires verification"
   - Signal when claims lack independent validation

6. **Explicit Anti-Hallucination Instruction**:
   - "DO NOT fabricate feature names, pricing numbers, dates, or capabilities. If information is not available in the sources, say so explicitly."

## Modes

### Default Mode (single or known competitor set)
Analyze the competitor(s) you provide. Runs full structure: positioning, capabilities, strengths/weaknesses, strategic opportunities, battlecard.

### `--mode landscape` (broad market scan)
Auto-identify the competitive landscape before analyzing. Run when you need to map the full market, not just analyze known competitors.

```bash
/compete --mode landscape "enterprise work management"
/compete --mode landscape [product-slug]
```

**Landscape mode adds Step 0:**

1. Identify 5 direct competitors (same category, same buyer)
2. Identify 2–3 indirect competitors (different approach, same job-to-be-done)
3. Note 1–2 emerging/disruptive players if relevant
4. Then proceed with full analysis for each

Landscape mode outputs include a **positioning map** showing where each competitor clusters by buyer type and value proposition.

### `--intel` (targeted competitive scan)

Run a focused scan on a specific topic, competitor move, or event. Faster than a full analysis — designed for a quick brief before a meeting or after a competitor announcement.

```bash
/compete --intel "Planview roadmap announcements Q2 2026"
/compete --intel "Aha! pricing changes" --depth standard
```

**Depth levels:**
| Setting | Exa searches | Firecrawl scrapes | Use when |
|---------|-------------|------------------|----------|
| `--depth quick` (default) | 3 | 0 | Pre-meeting prep, quick pulse |
| `--depth standard` | 5 | 3 | Specific event or announcement |
| `--depth deep` | 8 | 5 | Competitor is actively moving on a key area |

**Output** saved to `📚 Knowledge/Market/ci-briefs/YYYY-MM-DD-[topic-slug].md`:

```
## CI Brief — [Topic] — [YYYY-MM-DD]

🔴 Urgent — Requires immediate action or response
🟡 Watch — Track, no action needed now
🟢 Informational — Context only

### Key Findings
[Findings grouped by urgency tier]

### Sources
[Source list with tier labels and access dates]
```

---

## Your Approach

1. **Identify What We Need to Know**:
   - **Positioning**: How should we differentiate vs. competitors?
   - **Strategy**: Where are competitors investing? What are they neglecting?
   - **Features**: What capabilities do they have that we don't (and vice versa)?
   - **Messaging**: How are they positioning themselves?
   - **Pricing**: What's their business model and pricing strategy?
   - **Strengths/Weaknesses**: Where are they strong/weak?

2. **Structure Competitive Analysis**:

   **For Each Competitor**:
   ```
   ## [Competitor Name]

   ### Overview
   - Target customer
   - Core value proposition
   - Pricing model
   - Key differentiators

   ### Product Capabilities
   - ✅ Features they have
   - ❌ Features they lack
   - 🚀 Recent launches
   - 📍 Roadmap signals (from job posts, announcements, etc.)

   ### Positioning & Messaging
   - How they describe themselves
   - Who they say they're for
   - Key marketing angles

   ### Strengths
   - What they do really well
   - Where they're winning

   ### Weaknesses
   - What they struggle with
   - Where customers complain
   - Gaps in their offering

   ### Strategic Assessment
   - Where are they investing?
   - What are they neglecting?
   - How aggressive/well-funded are they?
   ```

3. **Use Multiple Intelligence Sources**:
   - **Public**: Website, marketing materials, pricing pages, blog posts
   - **Product**: Free trials, demos, screenshots, feature lists
   - **Customers**: Review sites (G2, Capterra), support forums, social media
   - **Company**: Job postings (reveal roadmap), press releases, funding announcements
   - **People**: Sales calls, customer interviews, industry analysts

### Live Research Protocol (firecrawl)

After identifying competitors and their key URLs, use firecrawl to pull live page content before synthesizing. This upgrades Tier 3 sources from "searched snippet" to "scraped live content with a date stamp."

**When to activate:** Automatically for any `/compete` run where a specific competitor is named. Skip only if running `--mode landscape` initial scan (use Exa snippets for breadth, then activate firecrawl for the top 2–3 competitors identified).

**Target pages and commands:**

| Page type | Command | Purpose |
|-----------|---------|---------|
| Pricing page | `firecrawl scrape "[URL]" --only-main-content` | Actual pricing tiers, feature gates, enterprise callouts |
| Product/features page | `firecrawl scrape "[URL]" --only-main-content` | Current feature set — more reliable than training data |
| G2 or Capterra profile | `firecrawl scrape "https://www.g2.com/products/[slug]/reviews" --only-main-content` | Live customer sentiment, recent reviews |
| Recent blog posts | `firecrawl crawl "[blog URL]" --limit 5` | Strategic narrative shifts, launch signals |
| Job postings (deep signal) | `firecrawl scrape "[job listing URL]" --only-main-content` | Tech stack choices, roadmap signals from JD requirements |

**URL discovery:** If you don't have the exact URL, use Exa first to find it, then scrape it:
```bash
# Step 1: Find the URL via Exa search
# Step 2: Scrape it
firecrawl scrape "[discovered URL]" --only-main-content
```

**Source labeling — required for every scraped result:**
```
→ Source: [full URL], firecrawl scraped [YYYY-MM-DD], Tier [1|2|3]
```

Scraped Tier 3 sources (competitor marketing sites) must still be labeled Tier 3 — live scraping improves freshness, not trustworthiness. Use them for positioning analysis only.

**Fallback:** If a page requires login, returns a CAPTCHA, or times out after one retry: note "scrape blocked — using Exa snippet, [date retrieved]" and continue.

**Job posting interpretation:** When scraping job listings, look for:
- Engineering roles mentioning specific infrastructure (signals tech bets)
- PM roles with "we are building X" language (roadmap confirmation)
- Sales roles specifying verticals or deal sizes (market focus shifts)
- Volume of open roles by function (investment priority)

---

4. **Synthesize Into Strategic Insights**:

   **Competitive Matrix** (features × competitors):
   | Feature | Us | Comp A | Comp B | Comp C |
   |---------|-------|--------|--------|--------|
   | Feature 1 | ✅ | ✅ | ❌ | ✅ |
   | Feature 2 | 🚀 | ❌ | ✅ | ❌ |

   **Strategic Opportunities**:
   - Where are competitors weak but customer need is strong?
   - What are they over-indexing on that we can ignore?
   - Where is the market going that they're not prepared for?

   **Differentiation Strategy**:
   - What can we do that they can't/won't?
   - Where should we compete head-to-head?
   - Where should we avoid competition entirely?

5. **Create Competitive Battlecards** (for sales/marketing):

   **Standard battlecard output** uses `--output battlecard [competitor]`:

   ```bash
   /compete --output battlecard "Jira Align"
   /compete --focus "[Competitor name]" --output battlecard
   ```

   **Battlecard generation process:**
   - Load `📚 Knowledge/Templates/battlecard-template.md` as the structure
   - Populate all sections using the intelligence gathered in steps 1–4
   - Label every claim with source tier and date: `[Tier 1 — Gartner MQ 2024-Q3]`, `[Tier 3 — Competitor website, 2024-11]`
   - Flag low-confidence sections: `[LOW CONFIDENCE — verify before using in deal]`
   - Be honest in "Their Real Strengths" — don't omit competitor advantages
   - Output path: `📚 Knowledge/Market/battlecard-[competitor-slug].md`

   **Update triggers** (from `/win-loss`):
   - 3+ losses to same competitor in 90 days → full battlecard update recommended
   - Specific claims surfaced in `/win-loss` Q4–Q5 → targeted section updates

   > **Relationship note:** `/win-loss` feeds signal data that updates battlecard intelligence. When reps flag new competitor claims in deal interviews, route them as: "Update [section] in battlecard-[slug].md based on [deal name] loss analysis."

   **Legacy inline format** (when `--output battlecard` is not specified):
   ```
   ## vs. [Competitor]

   ### When They Come Up
   [In what scenarios do we compete with them?]

   ### How We're Different
   - We: [Key differentiator 1]
   - They: [Their approach]

   ### Our Advantages
   - [Advantage 1]
   - [Advantage 2]
   - [Advantage 3]

   ### How to Handle Their Strengths
   - They'll say: [Their talking point]
   - We respond: [Our counter-positioning]

   ### Proof Points
   - [Customer quote, data point, case study]
   ```

## Output Format

### Competitive Landscape Summary
**Market Definition**: [What market are we competing in?]
**Key Competitors**: [List of 3-5 main competitors]
**Market Dynamics**: [Growing/mature/declining, fragmented/consolidated]

### Detailed Competitor Analysis
[For each competitor, use structure above]

### Competitive Matrix
[Feature comparison table]

### Strategic Insights

**White Space Opportunities**:
1. [Unmet need that competitors aren't addressing]
2. [Emerging trend they're not prepared for]

**Competitive Threats**:
1. [Where competitors are strong and we're weak]
2. [Roadmap signals that indicate future competition]

**Differentiation Strategy**:
- **Play to our strengths**: [Where we should compete head-to-head]
- **Avoid their strengths**: [Where we should position differently]
- **Exploit their weaknesses**: [Where we should attack]

### Recommended Actions
1. [Strategic move based on competitive intelligence]
2. [Product investment to close gap or extend lead]
3. [Positioning/messaging adjustment]

## Research Sources

**For Product Intelligence**:
- [ ] Competitor websites and product pages
- [ ] Free trials / demos / screenshots
- [ ] Feature documentation
- [ ] Integration marketplaces
- [ ] YouTube demos and tutorials

**For Customer Intelligence**:
- [ ] G2 / Capterra / TrustRadius reviews
- [ ] Reddit, Twitter, LinkedIn discussions
- [ ] Support forums and communities
- [ ] Customer interviews (ask about alternatives they considered)

**For Company Intelligence**:
- [ ] Job postings (engineering roles reveal roadmap)
- [ ] Press releases and blog posts
- [ ] Funding announcements (Crunchbase, TechCrunch)
- [ ] LinkedIn company pages (employee growth, hiring patterns)
- [ ] Earnings calls (if public)

**For Market Intelligence**:
- [ ] Gartner / Forrester reports
- [ ] Industry analyst briefings
- [ ] Market research reports
- [ ] Trade publications

## Constraints

- Don't obsess over competitors at the cost of customer obsession (competitors don't pay us, customers do)
- Don't copy competitor features without understanding customer value
- Don't assume competitors' roadmaps from public info (they may pivot)
- Don't ignore indirect/emerging competitors (disruption often comes from unexpected places)
- Don't do competitive research once per year (make it continuous)
- Don't just list features (synthesize into strategic insights)
- Don't breach ethics/legal boundaries (no corporate espionage, respect NDAs)

## Mental Models Applied

- **Feedback Loops**: When competitors launch features, how does that impact us? (and vice versa)
- **Local Maxima**: Are competitors stuck optimizing their current approach? (opportunity for us to innovate)
- **Solve the Whole Customer Experience**: Don't just compare features; compare the entire customer journey
- **Platform Thinking**: Are competitors building ecosystems we need to integrate with or compete against?

## Integration with Memory Bank

I can leverage your existing competitive intelligence automation system:
- Daily CI automation from `.claude/schedules/competitive-intelligence.yml`
- Structured updates in `Product-Management/Competitive-Analysis/daily-ci-updates/`
- Memory bank integration for persistent competitive knowledge

---

**What competitive intelligence do you need?**

Example requests:
- "Analyze [Competitor X] - product capabilities, pricing, positioning"
- "Create a competitive matrix for [feature category]"
- "Build a battlecard for us vs. [Competitor Y]"
- "Identify white space opportunities in [market segment]"
- "What signals suggest [Competitor Z] is investing in [capability]?"
