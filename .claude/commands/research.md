---
description: Run the research workflow
---
# Product Research & Discovery Assistant

Design targeted validation studies and customer research plans. Produces a structured research plan with scope, screener, and interview guide calibrated to the specific opportunity being validated.

> **Note**: For research that includes automated execution (web search, content fetching, source analysis), use the **research skill** instead. This command focuses on research planning frameworks and methodology design.

---

## Relationship

- **`/research`** is the validation design step — downstream of `/discover` (when evidence confidence is Low or Value Risk is Uncertain) and upstream of actual customer conversations
- **`/discover`** hands off to `/research` via `--opportunity` and `--evidence-confidence` when the evidence gate isn't cleared
- **`/signal`** captures individual customer touchpoints continuously — `/research` designs the structured studies that generate those signals at scale
- **`/synthesize`** consolidates 10+ signals into themes — run after research is complete
- **`/spec`** is downstream — run after Value Risk is validated

---

## Command Syntax

```bash
/research [--opportunity "<statement>"] [--evidence-confidence <High|Medium|Low>] [--risk <value|usability|feasibility|viability>] [--hypothesis "<assumption>"] [<description>]
```

**Arguments**:
- `--opportunity "<statement>"`: Carry Opportunity Statement verbatim from `/discover` handoff (skips generic framing question)
- `--evidence-confidence <High|Medium|Low>`: Current evidence level — sets how many interviews/studies to recommend
- `--risk <value|usability|feasibility|viability>`: Which of the four risks to prioritize (default: value)
- `--hypothesis "<assumption>"`: The specific assumption being tested (optional — focus the study design)

**Examples**:
```bash
/research --opportunity "For enterprise portfolio managers who..." --evidence-confidence Low --risk value
/research --risk usability --hypothesis "Users can configure custom views without training"
/research "validate NatWest capacity planning pain point with 3 ICP customers"
/research                                                    # Interactive — asks what to validate
```

---

## Step 0: Parse Arguments

Extract from the command invocation:
- `--opportunity` value (optional — pre-fills study target)
- `--evidence-confidence` value (optional — calibrates study scope)
- `--risk` value (optional — default: value)
- `--hypothesis` value (optional — sharpens the study design)

**If `--opportunity` is provided:** Acknowledge it, skip generic discovery framing, and proceed directly to designing a targeted study. State: "Designing validation study for: '[opportunity]'. Targeting [risk] risk with [evidence-confidence] evidence baseline."

**If nothing provided:** Ask one question: "What are you trying to validate, and what do you already know? (Paste your Opportunity Statement if you have one, or describe the assumption you're testing.)"

---

## Step 1: Calibrate Study Scope

Based on `--evidence-confidence` (or inferred from context):

| Confidence | Study prescription |
|---|---|
| **Low** (0-1 interviews or assumption-only) | 4-6 customer conversations minimum before advancing; use discovery interviews, not validation |
| **Medium** (2-4 interviews or mixed data) | 2-3 targeted validation sessions; prototype or fake-door test if possible |
| **High** (5+ interviews or strong data) | 1-2 confirmatory sessions; can move to prototype or concierge MVP |

State the prescription explicitly: "Given [Low/Medium/High] evidence confidence, recommend [N] [interview/test] sessions before advancing."

---

## Grounded Research Principles

**Critical Guardrails for AI-Assisted Product Research:**

1. **Curate Your Source Universe** - Define acceptable sources upfront:
   - **Financial/Regulatory**: SEC filings, earnings calls, annual reports
   - **Independent Analysis**: Gartner, Forrester, IDC reports (not vendor-sponsored)
   - **Customer Voice**: G2, Capterra, TrustRadius reviews; Reddit, forums
   - **Internal Data**: Support tickets, sales CRM notes, win/loss analysis
   - **Job Market Signals**: LinkedIn postings (reveal roadmap direction)
   - **Practitioner Evidence**: Lenny's Newsletter/Podcast (via `lennysdata` MCP or `qmd query "..." -c pm-frameworks`) — interview-based patterns from operators at real companies; treat as [Practitioner Interview], not analyst report
   - **NOT Acceptable as Truth**: Vendor marketing sites, press releases (use only for positioning analysis)

2. **Time Bounds Required** - Markets move faster than research:
   - Always specify: "Data from [timeframe] - [current date check]"
   - Flag when information may be outdated

3. **Traceability Mandate** - Research outputs must cite:
   - **Direct quotes** from sources (with attribution)
   - **Pattern frequency** ("Mentioned in 7 of 10 reviews")
   - **Source type labels** ([Customer Review], [Analyst Report], [Vendor Marketing])

4. **Explicit Uncertainty Handling**:
   - "If information is not present or unclear in the sources, explicitly state: 'Unable to determine from available sources'"
   - DO NOT interpolate or extrapolate beyond source data

5. **Fact vs. Interpretation Layers**:
   - **Factual Events**: Product launches, pricing changes, executive changes, funding events
   - **Observed Patterns**: Themes from customer reviews, trends in analyst reports
   - **Strategic Interpretation**: What these facts/patterns mean for our strategy (clearly labeled)

6. **Verification Before Decision**:
   - For any insight influencing roadmap: "List the exact sources behind this claim"
   - Flag low-confidence claims: "Single-source finding - requires independent verification"

## Step 2: Generate Targeted Study Design

If `--opportunity` was provided, generate a study plan directly calibrated to it — do not ask generic framing questions. The output should include:

**ICP-calibrated screener** (Company ICP: Enterprise 500-10K+ employees, Financial Services, Insurance, Logistics, Manufacturing, Technology):
```
Screener criteria:
- Company size: [500+ employees / 10K+ employees for enterprise-grade]
- Industry: [relevant ICP verticals]
- Role: [Director IT / VP Engineering / Agile Program Manager / RTE / Product Owner]
- Pain: [Must have experienced [specific situation from Opportunity Statement]]
```

**Study type by risk:**

- **Value risk** → Discovery interview (JTBD-focused) + optional fake-door test
- **Usability risk** → Task-based prototype walkthrough ("show me how you'd [accomplish task]")
- **Feasibility risk** → Technical spike design (engineering spike, not customer interview)
- **Viability risk** → Pricing research (van Westendorp or JTBD pricing interview)

**Interview guide** (for value or usability risk — generated from the Opportunity Statement):

```
Opening (5 min): "Tell me about the last time you [situation from opportunity]."
Problem exploration (15 min):
  - "What were you trying to accomplish?"
  - "What made that hard?"
  - "What did you try instead? Why didn't that work?"
  - "What would need to be true for this to be worth changing?"
Current state (10 min):
  - "Show me how you handle [task] today."
Close (5 min):
  - "If this were solved perfectly, what would that look like for you?"
```

**Success criteria:**
- **Move forward if**: [N] of [N] participants confirm the problem, describe it in similar terms, and have an active workaround
- **Pivot if**: Participants describe the problem differently than hypothesized, or severity is low ("annoying" not "blocking")
- **Kill if**: No active workaround exists and participants are not bothered by the status quo

---

## Step 3: Framework Guidance (when invoked generically)

If no `--opportunity` was provided, apply the general research framework below. Ask one question first: "What are you trying to validate, and what do you already know?"

1. **Identify What We're Trying to Learn**:
   - **Discovery**: What problems do customers have? (Open-ended exploration)
   - **Validation**: Will customers use/buy this solution? (Testing hypotheses)
   - **Optimization**: How can we improve this existing feature? (Iterative improvement)
   - **Measurement**: Is this feature working? (Post-launch learning)

2. **Apply The Four Risks Framework**:
   Help me assess which risks to investigate first:

   - **Value Risk**: Will customers find this valuable? (Most critical - investigate first)
   - **Usability Risk**: Can customers figure out how to use it?
   - **Feasibility Risk**: Can we build this with our technology/resources?
   - **Viability Risk**: Does this work for our business model?

   **Priority**: Always validate Value Risk first. The best-built product that solves the wrong problem is worthless.

3. **Choose the Right Research Method**:

   **For Discovery** (understanding problems and market):
   - Competitive analysis (feature gaps, positioning, messaging)
   - Market trend research (industry shifts, emerging patterns)
   - Customer review analysis (G2, Capterra, forums)
   - Support ticket analysis (internal data)
   - Analyst research (Gartner, Forrester, industry reports)

   **For Validation** (testing solutions):
   - Prototype testing (fake it before you build it)
   - Landing page tests
   - Concierge MVP (manual before automated)
   - Beta programs
   - A/B tests

   **For Measurement** (post-launch):
   - Analytics review
   - Funnel analysis
   - Cohort analysis
   - NPS/satisfaction surveys
   - Support ticket tracking

4. **Design Good Research**:
   - **Research scope**: What sources, data, or artifacts will we analyze?
   - **Key questions**: What specific questions will answer our hypotheses?
   - **Success criteria**: What would we need to see to move forward? What would make us stop?

5. **Avoid Common Research Pitfalls**:
   - Don't ask customers what to build (they don't know)
   - Do ask about their problems, context, workarounds
   - Don't pitch your solution first (biases their response)
   - Do show prototypes and observe reactions
   - Don't ask leading questions
   - Do ask open-ended "why" questions
   - Don't trust what people say they'll do
   - Do observe what they actually do

## Output Format

> **What this command produces**: A research plan with scope, methods, and success criteria. For executed research with actual findings, use the **research skill** instead.

### Research Plan
**What we're trying to learn**: [Specific question or hypothesis]
**Why this matters**: [How this informs our decision]
**Type**: Discovery / Validation / Optimization / Measurement

### Risk Assessment (Four Risks)
- 🔴 **Value Risk**: [HIGH/MEDIUM/LOW - describe the risk]
- 🟡 **Usability Risk**: [HIGH/MEDIUM/LOW]
- 🟢 **Feasibility Risk**: [HIGH/MEDIUM/LOW]
- 🟢 **Viability Risk**: [HIGH/MEDIUM/LOW]

**Priority Risk to Investigate**: [Which risk to tackle first]

### Recommended Research Method
**Method**: [Interview / Prototype test / Analytics / etc.]
**Why this method**: [How it addresses our risk/question]

### Research Plan

**Research Scope & Sources**:
- **Data sources**: [Competitor sites, analyst reports, customer reviews, internal data, etc.]
- **Search strategy**: [Keywords, competitors, sources to investigate]
- **Time period**: [What timeframe of data/market to analyze]

**Key Questions/Investigation Areas**:
1. [Question 1]
2. [Question 2]
3. [Question 3]

**Success Criteria**:
- **Move forward if**: [What signals would validate our hypothesis]
- **Pivot if**: [What would indicate we're wrong]
- **Stop if**: [What would kill this idea]

**Timeline**: [How long will this take]

### Research & Analysis Framework

**Data Collection Approach**:
- **Primary sources**: [Competitor websites, product docs, pricing pages]
- **Secondary sources**: [Analyst reports, review sites, forums, social media]
- **Internal sources**: [Sales feedback, support tickets, win/loss analysis]

**Synthesis Framework**:
After gathering research, I'll help you synthesize:
- **Patterns**: What themes emerged across sources?
- **Gaps**: What are competitors missing or neglecting?
- **Signals**: What trends or shifts are emerging?
- **Decision**: Move forward / Pivot / Stop?

## Constraints

- Don't skip validation before building (ship to learn, but learn before shipping expensive things)
- Don't confuse feature parity with customer value
- Don't research forever (diminishing returns - gather enough signal, then decide)
- Don't only research competitors you know (seek emerging/indirect competitors)
- Don't copy features without understanding the customer problem they solve
- Don't ignore qualitative insights in favor of only quantitative data
- Don't treat competitive intelligence as a one-time activity (markets evolve continuously)

## Mental Models Applied

- **Confidence Determines Speed vs Quality**: Low confidence in value = fast, cheap research before building
- **Expected Value**: Research reduces uncertainty, improving our probability-weighted outcomes
- **Time Value of Shipping**: Don't research for 6 months; do 2 weeks of research, ship a small test, learn fast
- **Diminishing Returns**: After 5-8 interviews, you'll see repeating patterns (more research yields little new insight)

---

**What do you need to research?**
