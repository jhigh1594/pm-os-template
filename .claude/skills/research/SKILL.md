---
name: research
description: Product research and competitive intelligence that plans AND executes research projects. Use for competitive analysis, customer insights, market trends, validation research, and analyst research.
---

# Research

Product research and competitive intelligence that plans AND executes research projects.

**Trigger when user asks:**
- "Research [competitor/feature/topic]"
- "Competitive analysis on..."
- "What are customers saying about..."
- "Market trends for..."
- "Validate this hypothesis..."
- "Investigate [topic] across competitors"

Use this skill when the user needs:
- Competitive analysis (features, positioning, pricing, messaging)
- Customer insight research (reviews, forums, support patterns)
- Market trend research (industry shifts, emerging patterns)
- Validation research (testing hypotheses with real data)
- Analyst research (synthesizing reports, market sizing)

---

## Skill Overview

This skill combines systematic research planning with automated execution using web search, content fetching, and workspace integrations.

**Two-phase approach:**
1. **Planning Phase**: Apply Four Risks Framework, define scope, select methods
2. **Execution Phase**: Fetch sources, analyze content, synthesize findings

---

## Phase 1: Planning

Before executing research, establish the research plan with the user:

### Step 1: Understand What We're Learning

Identify the research type:
- **Discovery**: What problems do customers have? (Open-ended exploration)
- **Validation**: Will customers use/buy this solution? (Testing hypotheses)
- **Optimization**: How can we improve this existing feature? (Iterative improvement)
- **Measurement**: Is this feature working? (Post-launch learning)

### Step 2: Apply Four Risks Framework

Assess which risks to investigate first:

| Risk | Question | Priority |
|------|----------|----------|
| **Value Risk** | Will customers find this valuable? | 🔴 Always first |
| **Usability Risk** | Can customers figure out how to use it? | 🟡 Second |
| **Feasibility Risk** | Can we build this with our technology/resources? | 🟢 Technical |
| **Viability Risk** | Does this work for our business model? | 🟢 Business |

**Rule**: Always validate Value Risk first. The best-built product that solves the wrong problem is worthless.

### Step 3: Define Research Scope

Present to user for confirmation:

```
**Research Scope:**
- **Data sources**: [Competitor sites, G2/Capterra, analyst reports, internal data, etc.]
- **Search strategy**: [Keywords, competitors, sources]
- **Time period**: [What timeframe to analyze]
- **Key questions**:
  1. [Question 1]
  2. [Question 2]
  3. [Question 3]

**Success Criteria:**
- Move forward if: [What signals validate our hypothesis]
- Pivot if: [What would indicate we're wrong]
- Stop if: [What would kill this idea]
```

Get user approval before proceeding to execution.

---

## Phase 2: Execution

### Step 4: Execute Research Using Tools

Based on approved research plan, use appropriate tools:

**For Competitive Analysis:**
```
1. Use web-search-prime to find competitor sites and positioning
2. Use webReader to fetch and analyze competitor pages
3. Use web-search-prime to find G2/Capterra reviews
4. Synthesize: feature gaps, positioning differences, pricing patterns
```

**For Customer Insights:**
```
1. Use web-search-prime to find customer reviews (G2, Capterra, TrustRadius)
2. Use webReader to extract review content
3. Use web-search-prime to find forum discussions (Reddit, industry forums)
4. Synthesize: pain points, desired outcomes, patterns
```

**For Market Trends:**
```
1. Use web-search-prime with recent time filters
2. Search for industry reports, analyst insights
3. Look for LinkedIn job postings (reveal roadmap direction)
4. Synthesize: emerging patterns, shifts, signals
```

**For Internal Data:**
```
1. Use @notion to search for customer research notes
2. Use @granola to search relevant meeting transcripts
3. Use @obsidian-vault for knowledge base references
4. Synthesize: internal findings, prior decisions, context
```

### Step 5: Apply Grounded Research Guardrails

**CRITICAL**: Throughout execution, enforce these principles:

1. **Curate Your Source Universe**
   - ✅ SEC filings, earnings calls, annual reports
   - ✅ Gartner, Forrester, IDC reports (not vendor-sponsored)
   - ✅ G2, Capterra, TrustRadius reviews
   - ✅ Reddit, forums (customer voice)
   - ✅ Internal: support tickets, sales CRM notes, win/loss analysis
   - ❌ Vendor marketing sites (use only for positioning analysis)
   - ❌ Press releases (use only for factual events, not claims)

2. **Time Bounds Required**
   - Always specify: "Data from [timeframe] - [current date]"
   - Flag when information may be outdated

3. **Traceability Mandate**
   - Include direct quotes with attribution
   - Note pattern frequency ("Mentioned in 7 of 10 reviews")
   - Label source types: `[Customer Review]`, `[Analyst Report]`, `[Vendor Marketing]`

4. **Explicit Uncertainty Handling**
   - If information is unclear: "Unable to determine from available sources"
   - DO NOT interpolate or extrapolate beyond source data

5. **Fact vs. Interpretation Layers**
   - **Factual Events**: Product launches, pricing changes, executive changes, funding
   - **Observed Patterns**: Themes from reviews, trends in reports
   - **Strategic Interpretation**: What these mean (clearly labeled)

6. **Verification Before Decision**
   - For roadmap-influencing insights: "Exact sources: [list]"
   - Flag low-confidence: "Single-source finding - requires verification"

---

## Phase 3: Synthesis

### Step 6: Deliver Research Findings

Present findings in this format:

```markdown
# Research Findings: [Title]

**Research Date**: [Date]
**Data Period**: [Timeframe covered]
**Sources Analyzed**: [Number and type of sources]

---

## Executive Summary

[2-3 sentence summary of key findings and recommendation]

**Recommendation**: Move forward / Pivot / Stop

---

## Patterns Identified

### Pattern 1: [Pattern name]
- **Evidence**: [Direct quotes from sources with attribution]
- **Frequency**: [How often mentioned]
- **Sources**: [Source list]

### Pattern 2: [Pattern name]
- **Evidence**: [Direct quotes from sources with attribution]
- **Frequency**: [How often mentioned]
- **Sources**: [Source list]

---

## Competitive Gaps

What competitors are missing:
1. [Gap 1] - [Source attribution]
2. [Gap 2] - [Source attribution]

Opportunity for differentiation:
- [Opportunity description]

---

## Signals & Trends

Emerging patterns detected:
- [Signal 1] - [Source and date]
- [Signal 2] - [Source and date]

---

## Risk Assessment Updates

| Risk | Before | After | Key Findings |
|------|--------|-------|--------------|
| Value Risk | [Level] | [Level] | [What we learned] |
| Usability Risk | [Level] | [Level] | [What we learned] |
| Feasibility Risk | [Level] | [Level] | [What we learned] |
| Viability Risk | [Level] | [Level] | [What we learned] |

---

## Sources

**Primary Sources Analyzed:**
- [Source 1] - [URL] - [Date accessed]
- [Source 2] - [URL] - [Date accessed]

**Confidence Level:**
- ☐ High (multiple independent sources, recent data)
- ☐ Medium (2-3 sources, some corroboration)
- ☐ Low (single source or limited corroboration)

**Open Questions:**
- [What we still need to learn]
```

---

## Constraints & Pitfalls

**Avoid:**
- Don't skip validation before building expensive things
- Don't confuse feature parity with customer value
- Don't research forever (diminishing returns after 5-8 sources)
- Don't only research known competitors (seek emerging/indirect)
- Don't copy features without understanding the customer problem
- Don't ignore qualitative insights for only quantitative data

**Remember:**
- Confidence determines speed vs. quality (low confidence = fast, cheap research)
- Time value of shipping (2 weeks research + small test > 6 months research)
- Diminishing returns (patterns repeat after 5-8 sources)
- Expected value (research reduces uncertainty, improving outcomes)

---

## Tool References

Available tools for research execution:
- `mcp__web-search-prime__webSearchPrime` - Semantic web search with domain/time filters (search_query, search_recency_filter)
- `mcp__web_reader__webReader` - Fetch and convert URLs to markdown (returns clean, LLM-friendly content)
- `mcp__fetch__fetch` - Direct URL fetching for simple HTTP requests
- `mcp__notion__notion-search` - Search Notion workspace for internal data
- `mcp__granola__search_meetings` - Search Granola meeting transcripts
