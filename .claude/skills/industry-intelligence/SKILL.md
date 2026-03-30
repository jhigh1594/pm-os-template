---
name: industry-intelligence
description: Use when reasoning about industry trends, analyst coverage, adjacent market moves, earnings call signals, or macro forces affecting the agile planning and portfolio management market. Triggers: what's happening in the industry, analyst coverage, Gartner, Forrester, market trends, adjacent competition, enterprise software trends, portfolio management market, what analysts say, industry landscape, market intelligence.
---

# Industry Intelligence

Understand the market forces shaping Planview's competitive context — beyond direct competitors to industry trends, analyst signals, adjacent market moves, and demand shifts.

## When This Skill Activates

Use this skill when:
- PM asks about market trends in agile planning, OKR, or portfolio management
- PM is preparing for an analyst briefing or inquiry call
- PM is evaluating whether an adjacent market move threatens or creates opportunity
- PM is looking for strategic context beyond direct competitor positioning
- PM needs to understand what analysts evaluate in Planview's market
- PM is preparing a strategic narrative that requires market framing

## Default Stance: Consultative + Source-Qualified

Start by clarifying what decision this market intelligence should inform. Apply source hierarchy rigorously — the intelligence is only as good as its source. Always distinguish between Tier 1 (analyst/earnings), Tier 2 (trade press), and Tier 3 (vendor claims).

## Core Frameworks

### 1. Industry Signal Taxonomy

Use this hierarchy to qualify and weight all intelligence sources:

| Tier | Source Type | Examples | Confidence |
|------|-------------|---------|------------|
| **Tier 1** | Analyst reports, earnings call transcripts, regulatory filings | Gartner Magic Quadrant, Forrester Wave, SAP/Atlassian earnings calls, SEC filings | High — independent analysis with methodology |
| **Tier 2** | Industry trade press, credible customer surveys, academic research | CIO Magazine, PM Times, Gartner peer insights (aggregated), State of Agile report | Medium — editorial judgment applied; verify claims |
| **Tier 3** | Competitor announcements, vendor blogs, press releases, marketing copy | Atlassian product announcements, competitor blog posts, industry conference keynotes | Low — positioning only; never treat as factual claims about capabilities |

**Rule**: Label every intelligence claim with its source tier. Never mix Tier 1 and Tier 3 without explicit separation.

---

### 2. Key Quadrants/Waves to Track (Planview Context)

| Report | Relevance | Renewal Cadence |
|--------|-----------|----------------|
| Gartner Magic Quadrant for Strategic Portfolio Management | Direct — Planview appears; customers reference in evaluations | Annual |
| Forrester Wave for Enterprise Agile Planning | Direct — AgilePlace positioning | ~18 months |
| Gartner Market Guide for Project and Portfolio Management | Broader category context | Annual |
| IDC MarketScape for PPM | Alternative analyst perspective | Annual |

**How to use analyst positioning**:
- As a signal for customer perception and evaluation criteria (what buyers are asking for)
- As a framing device for internal strategic priorities (what "leaders" in the quadrant are doing)
- **Not** as ground truth about product capabilities — analysts evaluate based on demos and briefings, which can lag actual product state

---

### 3. Adjacent Market Threat Assessment

When an adjacent market player shows signs of entering Planview's space:

```
Step 1: Entry Path Analysis
→ What capability gap do they need to close to compete?
→ How long would it take to close that gap?
→ Do they have the enterprise sales motion to win in Planview's target segment?

Step 2: Customer Job Overlap
→ Do their customers have the same JTBD as Planview's customers?
→ Is there meaningful workflow overlap that creates switching opportunity?
→ Are there "dual users" — people who use both products at the same company?

Step 3: Switching Cost Comparison
→ If this adjacent player enters, what would make a customer prefer them?
→ What is Planview's defensible moat in this scenario?
→ Is the moat data network effects, workflow integration, or switching cost alone?
```

---

### 4. Demand Signal Patterns

Non-obvious signals that indicate market demand shifts:

| Signal Type | What to Look For | Why It Matters |
|-------------|-----------------|----------------|
| **Job posting surge** | "Head of Portfolio Management", "Agile Program Manager", "OKR Program Lead" surges at target companies | Leading indicator of organizational investment in Planview's value space |
| **Earnings call language** | When large enterprise software companies start using specific terms (e.g., "portfolio intelligence", "connected planning") | Indicates category framing is shifting; buyer vocabulary will follow |
| **Conference agenda shifts** | When Agile Alliance, PMI, or Gartner conferences add new tracks or remove old ones | Leading indicator of practitioner community direction change |
| **Customer job changes** | Former AgilePlace champions moving to new companies | Expansion signal — champions carry product preference to new employers |

---

## Response Contract

When this skill activates, default to:

```markdown
## Industry Intelligence: [Topic]

**Decision this should inform:** [What product, positioning, or strategic call this context serves]

**Signal sources consulted:**
- [Source] — [Tier] — [Date if applicable]

**Key finding:**
[Concise summary of what the signal reveals]

**So what for Planview:**
[1-2 sentences on the strategic implication — what should change or be validated]

**Validates or challenges:**
[Does this confirm existing Planview strategy, or surface a tension worth investigating?]

**Confidence:** [High / Medium / Low — based on source tier]

**Recommended action:**
[Capture as `/signal --source analyst|market` / Route to `/think` / Update battlecard / No immediate action required]
```

---

## Guardrails

- **Label all analyst claims with source, publication date, and version** — a 2023 Gartner report is not current for a 2026 positioning decision
- **Adjacent market analysis is hypothesis, not prediction** — always frame as "signals suggest" not "will happen"
- **Never present competitor announcements (Tier 3) as factual product capability claims** — treat as positioning signals only
- **Recency matters asymmetrically** — Tier 1 sources >12 months old should be used with explicit "as of [date]" labeling; Tier 3 sources should always be labeled regardless of age

## Integration

- Use `/industry-brief` command for structured market intelligence scans (analyst, market, earnings, jobs modes)
- Analyst and market signals captured here feed `/signal --source analyst|market` → `signals-YYYY-MM.md`
- Intel from this skill informs `/compete` competitive analysis (provides market context) and `/think` strategic analysis (provides industry framing)
- `/synthesize` picks up analyst/market signals from the monthly signals file in the same synthesis pass as customer signals
- `/daily-brief --industry` uses this skill's source hierarchy for its industry signals section

## Self-Learning

Before responding, read `LEARNED.md` in this skill directory when it exists and treat it as compact runtime guidance that sharpens this skill.

Rules for self-improvement:
- Keep `SKILL.md` human-owned; do not rewrite it directly from normal usage.
- Only promote specific, reusable, evidence-backed lessons into `LEARNED.md`.
