---
description: 'Use when synthesizing customer feedback from multiple sources into actionable
  insights. Triggers: synthesize feedback, customer interviews analysis, support tickets
  patterns, enhancement requests, thematic analysis, JTBD from feedback, 10+ data
  points, analyze these interviews, I have transcripts, what do my users actually want,
  design an interview guide, decision brief, verify this analysis, confidence in findings,
  disconfirming evidence.'
name: customer-feedback-synthesis
---

# Customer Feedback Synthesis

You are helping me synthesize existing customer feedback into actionable insights using research-validated frameworks.

## Mode Selector

Pick the mode that matches where you are:

| Mode | When to use | Skip to |
|---|---|---|
| **Analyze** | You have raw transcripts, survey data, or call notes | Decision Context loading (before Phase 1) |
| **Design** | You need an interview guide before research happens | Interview Design section |
| **Synthesize** | You have findings; need insights and interpretive position | Phase 3 (Insight Extraction) |
| **Verify** | You have existing AI-generated analysis; need a rigor check | Verification Pass section |

## Your Approach

**Great synthesis transforms raw feedback into strategic decisions.** I'll help you analyze accumulated customer data (interviews, support tickets, enhancement requests, analytics) to extract evidence-based insights and prioritized opportunities.

### Seven Synthesis Frameworks Applied

1. **Thematic Analysis** - Systematic pattern identification across qualitative data (Braun & Clarke)
2. **Affinity Mapping** - Hierarchical clustering of observations by meaning, not keywords
3. **Jobs-to-be-Done** - Extract customer motivations and hiring criteria
4. **Atomic Research Nuggets** - Break feedback into modular, reusable research assets
5. **Signal vs Noise Filtering** - Distinguish high-value insights from outliers
6. **Insight & Opportunity Statements** - Convert patterns to actionable format
7. **Continuous Discovery Pattern Mapping** - Track patterns over time

### Methodology

**Three-phase workflow** designed for single-session synthesis (1-2 hours total):
1. **Data Preparation & Organization** (15-20 min) - Structure raw feedback for analysis
2. **Pattern Identification & Analysis** (30-45 min) - Identify themes and extract jobs
3. **Insight Extraction & Recommendations** (20-30 min) - Convert patterns into actionable insights

**When to use this skill:**
- ✅ Quarterly synthesis of accumulated customer feedback
- ✅ Pattern analysis across multiple interviews (10+)
- ✅ Support ticket root cause analysis (50+ tickets)
- ✅ Enhancement request consolidation
- ✅ Cross-source synthesis (interviews + tickets + analytics)
- ✅ Turning raw transcripts or call notes into a decision brief
- ✅ Designing a JTBD-clean interview guide before research
- ✅ Verifying AI-generated analysis for fabricated quotes or generic themes

**When NOT to use this skill:**
- ❌ Planning future research (use `/discover` or `/research`)
- ❌ Single interview analysis (analyze as you go)
- ❌ Real-time triage of incoming requests (use `/prioritize`)
- ❌ Building personas, segments, or journey maps — use `/research-users`
- ❌ Designing A/B tests or quantitative experiments — use `/exp-driven-dev`

---

## Finding vs Insight — Enforce the Distinction

These are not interchangeable. Never mix them in output.

**Finding** = what happened (observable, verifiable, source-traceable)
> "Six of ten participants mentioned pricing."

**Insight** = mechanism + implication + direction
> "The pricing objection is a proxy for value uncertainty — buyers don't believe the product will change their workflow, and they're using price as an exit rather than the real reason."

Only insights drive decisions. A synthesis full of findings is a summary. A synthesis full of insights is a decision brief.

Four-step upgrade from finding to insight:
1. State what was observed (the finding)
2. Explain why it happens (the mechanism)
3. Name what it means for the decision (the implication)
4. State what to do differently (the direction)

A pattern that stops at step 1 is not an insight.

---

## Decision Context Loading (Required Before Any Analysis)

Before touching any data, establish:

1. **What decision does this synthesis inform?** (name the specific trade-off or choice)
2. **What do you currently believe is true?** (surfaces the hypothesis to stress-test)
3. **What evidence would change your mind?** (defines the evidence threshold)

If context has already been provided, confirm the decision before proceeding. Do not skip this step — it is what separates decision-grade analysis from topic summaries.

---

## Clarifying Questions

Start by asking these questions to understand the synthesis scope:

1. **What feedback are you synthesizing?**
   - Sources: (Interviews, tickets, requests, analytics, etc.)
   - Volume: (How many data points?)
   - Time range: (Dates covered)

2. **What customer segments are represented?**
   - ICP vs. non-ICP split?
   - Company sizes, industries, roles?

3. **What are you trying to learn?**
   - Specific research questions?
   - Decisions this will inform?
   - Hypotheses to validate?

4. **What's your timeline?**
   - When do you need synthesis completed?
   - How much time can you dedicate today?

---

## The Synthesis Process

### Phase 1: Data Preparation & Organization (15-20 min)

**Goal:** Transform raw feedback into structured, analyzable format.

**Activities:**

#### 1.1 Data Inventory
Create comprehensive inventory of all feedback sources:
- **Source types**: Customer interviews, support tickets, enhancement requests, user analytics, sales calls, user testing
- **Volume**: Total count per source type
- **Quality**: Richness of data (verbatim quotes vs. summaries)
- **Time range**: Date coverage
- **Customer segments**: ICP vs. non-ICP, company size, industry
- **Coverage gaps**: What segments/problems are missing?

#### 1.2 Atomic Nugget Extraction
Break raw feedback into discrete, analyzable units:
- **One observation per nugget**: Each nugget captures single insight, quote, or data point
- **Preserve context**: Who said it, when, in what situation
- **Tag metadata**: Customer segment, source type, date, topic
- **Extract verbatim quotes**: Don't paraphrase - capture exact language

**Quote Verification Rules (enforce on every nugget):**
- Always verbatim — never paraphrase or reconstruct
- Cite with participant ID and approximate timestamp: [P02 ~14:30]
- Start where the thought begins; include hedges and qualifiers — they signal uncertainty
- Include emotional language when present
- Do not combine statements from different parts of an interview
- A quote that would exceed 3 sentences should be split into separate quotes
- No single-source insights — every insight requires at least 2 independent sources
- Quotes that cannot be traced to an exact source in the raw data are fabricated — flag and remove

**Atomic Nugget Template:**
```markdown
**Nugget ID**: [Source]-[Number] (e.g., INT-005, TKT-142)
**Source**: [Interview transcript / Support ticket / Enhancement request / Analytics]
**Customer**: [Segment, company size, role]
**Date**: YYYY-MM-DD
**Quote/Observation**: "[Exact verbatim quote or specific observation]"
**Context**: [What triggered this? What were they trying to do?]
**Tags**: [Problem area, feature category, urgency level]
```

#### 1.3 Initial Signal/Noise Filtering
Apply quick filter to focus on high-signal data:

**Signal indicators:**
- Repeated across multiple sources (frequency)
- High severity/impact (customer explicitly states pain level)
- Aligns with strategic direction
- ICP customers experiencing the problem
- Workarounds exist (evidence of unmet need)

**Noise indicators:**
- Single mention (anecdote, not pattern)
- Off-strategy or edge case
- Non-ICP segment only
- Feature request without underlying problem stated
- Vague or unclear feedback

See `output-templates.md` for the complete Phase 1 output template.

---

### Phase 2: Pattern Identification & Analysis (30-45 min)

**Goal:** Identify themes, extract jobs-to-be-done, and classify signal strength using multiple frameworks.

This phase applies four complementary frameworks. See `frameworks.md` for detailed guidance on each:

- **2a. Thematic Analysis** (Braun & Clarke 6-Phase Model)
- **2b. Affinity Mapping** (Cluster by Meaning, Not Keywords)
- **2c. Jobs-to-be-Done Synthesis**
- **2d. Signal vs Noise Filtering** (Prioritization Matrix)

**Signal Strength Formula:**
```
Signal Strength = Frequency × Severity × Strategic Fit
```

**Classification:**

| Signal Strength Score | Classification | Action |
|----------------------|----------------|--------|
| 60+ | **Very Strong Signal** | High priority, validate and build |
| 30-59 | **Strong Signal** | Prioritize for roadmap consideration |
| 10-29 | **Medium Signal** | Track, may become stronger over time |
| <10 | **Weak Signal / Noise** | Log but don't prioritize |

See `output-templates.md` for the complete Phase 2 output template.

---

### Phase 3: Insight Extraction & Recommendations (20-30 min)

**Goal:** Convert pattern analysis into actionable insights, opportunity statements, and prioritized recommendations.

#### 3a. Insight Statement Generation

**Insight Statement Template:**
```
[Customer Segment] struggle with [Specific Problem] because [Root Cause].
This matters because [Business Impact].
We learned [Unique Finding that others might miss].
```

**Quality checklist:**
- [ ] Specific customer segment named
- [ ] Root cause identified (not just symptom)
- [ ] Business impact quantified or described
- [ ] Non-obvious learning included
- [ ] Actionable (points toward solution direction)

#### 3b. Opportunity Statement Creation

**Opportunity Statement Template:**
```
For [Target Customer]
Who [Context/Situation]
The problem is [Specific Pain Point]
Which impacts them by [Consequence/Cost]
A solution would [Desired Outcome]
Unlike [Current Alternatives]
Our approach could [Strategic Differentiation]
```

#### 3b-a. Disconfirming Evidence (Required — Not Optional)

Every synthesis must include at least one finding that cuts against the primary insights. A brief that only shows supporting evidence is a bias report, not research.

Ask explicitly: "What did participants say or do that contradicts the main themes?"

Format:
```
## Disconfirming Evidence
- [Finding that cuts against Insight 1] — Source: [P0X ~timestamp]
- [Finding that cuts against Insight 2 or the overall narrative]
```

**Confidence Assessment per Insight:**

Rate each insight before surfacing it:

| Confidence | Criteria |
|---|---|
| **Strong** | 3+ independent sources; behavioral evidence; consistent across segments |
| **Provisional** | 2 sources; or stated preference only; or single segment |
| **Thin** | Single source; or contradicted by other evidence; or could apply to any product |

Never present all insights as equally confident. Thin insights must be flagged explicitly and paired with a recommended validation method.

#### 3c. Assumption Documentation & Validation Tracking

Track assumptions that need validation before committing to build:

| Assumption | Risk Level | Validation Method | Status | Evidence |
|------------|-----------|-------------------|--------|----------|
| [Assumption 1] | [Critical/High/Medium/Low] | [Interview/Prototype/Analytics/Spike] | [✅ Validated / ⚠️ Uncertain / ❌ Invalidated / 🔄 In Progress] | [Evidence summary] |

#### 3d. Opportunity Prioritization

**Priority Score** = Impact (1-10) × Strategic Fit (1-10) × Confidence (1-10)

See `output-templates.md` for the complete Phase 3 output template.

---

---

## Interview Design Mode

Use when the user needs an interview guide before research happens. Skip directly here from the Mode Selector when mode = Design.

### JTBD-Clean Interview Guide Structure

Interviews should surface the struggling moment, the switch, and the forces — not validate features.

**Opening (build rapport, orient to past behavior):**
- "Walk me through the last time you dealt with [problem area]. Start from the beginning."
- "What were you doing right before you realized you needed to change something?"

**Struggle + trigger:**
- "What was the moment you knew your current approach wasn't working?"
- "What had changed? Why now and not earlier?"

**Alternatives explored:**
- "What did you look at before you made a decision?"
- "What almost made you choose something else?"

**Switch decision:**
- "Walk me through how the decision actually got made."
- "Who else was involved? How did they feel about it?"

**Outcome:**
- "What changed after you made the switch?"
- "What did you expect would happen that didn't?"

### Mom Test Checklist

Before using any question, verify:
- [ ] Does this ask about the past, not a hypothetical future? ("Have you ever..." not "Would you...")
- [ ] Does this avoid leading the witness? (no "Do you think X is a problem?")
- [ ] Does this focus on behavior, not opinion? ("What did you do" not "What do you think")
- [ ] Does this avoid compliments and validation-seeking? ("That's great" shuts down honest feedback)

### Portigal Probing Moves

When an answer is thin or generic, use one of these:
- **Mirroring**: Repeat their last 3 words as a question. "You felt stuck?" Forces elaboration.
- **Naive probe**: "I'm not familiar with that — can you walk me through it?" Removes assumptions.
- **Clarify "we"**: "When you say 'we' decided — who specifically?" Surfaces the real decision-maker.
- **Numerical vagueness**: "You said 'often' — how often exactly?" Makes patterns concrete.
- **Long silence**: Don't fill it. 5-second pause often produces the most honest answer.

### 4 Forces of Progress Questions

Map each participant to the four forces (Bob Moesta):
- **Push**: "What about your current situation was driving you to look for something new?"
- **Pull**: "What was appealing about the new solution? What did you hope it would do?"
- **Anxiety**: "What made you hesitate before committing?"
- **Habit**: "What almost made you stick with what you had?"

---

## Verification Pass

Use when mode = Verify, or after generating any AI-assisted analysis.

```
VERIFICATION PASS

Review the analysis above for:

QUOTE VERIFICATION
- Confirm each quote exists verbatim in the source
- Flag any quotes that are paraphrased, combined, or not found
- Flag any quote missing participant ID + timestamp

CONTRADICTION CHECK
- For each participant, check if statements at different points conflict
- Look for: stated preferences vs. described behaviors, confidence followed by hedging
- Flag contradictions — do not resolve them silently

CONFIDENCE ASSESSMENT
- For any finding based on fewer than 2 independent sources, flag it as "Thin"
- Flag any theme that could apply to almost any product in this category as "Generic — discard"
- Rate each insight: Strong / Provisional / Thin

DISCONFIRMING EVIDENCE CHECK
- Is there at least one finding that cuts against the primary insights?
- If not, explicitly note: "No disconfirming evidence surfaced — this may indicate a gap"

Output a verification summary with flags and recommended revisions.
```

---

## Output Format

### Synthesis Report
**Location**: `memory-bank/synthesis/[YYYY-MM-DD]-[topic]-synthesis.md`
**Naming**: ISO date, topic area, "synthesis"

The report will contain all outputs from Phases 1-3.

---

## Additional Resources

### Deep-Dive Frameworks
See `frameworks.md` for detailed guidance on:
- Thematic Analysis Framework
- Affinity Mapping
- Jobs-to-be-Done Synthesis
- Atomic Research Nuggets
- Signal vs Noise Filtering
- Insight & Opportunity Statements
- Continuous Discovery Pattern Mapping
- Framework Application Matrix (decision tree)

### Output Templates
See `output-templates.md` for:
- Complete Phase 1 output template
- Complete Phase 2 output template
- Complete Phase 3 output template

### Command Integration
See `integration.md` for:
- Upstream commands that feed into synthesis (`/research`, `/discover`, `/prioritize`)
- Downstream commands that consume synthesis outputs (`/spec`, `/think`, `/decide`)
- When to chain commands vs. use standalone

### MCP Integration
See `mcp-integration.md` for:
- Granola MCP (meeting data)
- Notion MCP (research repository)
- Code examples for each MCP

### Constraints & Anti-Patterns
See `constraints.md` for:
- 8 anti-patterns to avoid
- Why each anti-pattern matters
- Examples of bad vs. good practice

### Usage Examples
See `examples.md` for:
- Quarterly interview synthesis scenario
- Support ticket pattern analysis scenario
- Enhancement request consolidation scenario

### Underlying Mental Models
See `mental-models.md` for:
- Four Risks (Marty Cagan) - Value risk first
- Jobs-to-be-Done (Clayton Christensen)
- Confidence → Speed/Quality (Shreyas Doshi)
- Signal vs Noise (Nate Silver)
- Time Value of Shipping (Shreyas Doshi)

---

## Memory Bank Updates

After synthesis completes, update:

**memory-bank/synthesis/[YYYY-MM-DD]-[topic]-synthesis.md**
- Primary synthesis report output
- Full Phase 1-3 outputs

**memory-bank/activeContext.md**
- Update "Current Focus" section with synthesis findings
- Add "Recent Insights" from synthesis

**memory-bank/value-thesis.md**
- Add validated beliefs from synthesis insights
- Update "What We Believe" based on evidence

**memory-bank/progress.md**
- Log synthesis milestone completion
- Track synthesis cadence (quarterly, annual)



## What Makes This Skill Different

<!-- State what pushes Claude OUT of default behavior. What does a naive response miss? -->



## Gotchas & Common Pitfalls

<!-- Populate from real usage failures. Each entry: failure mode → root cause → what to do instead. -->

## Self-Learning

Before responding, read `LEARNED.md` in this skill directory when it exists and treat it as compact runtime guidance that sharpens this skill.

Rules for self-improvement:
- Keep `SKILL.md` human-owned; do not rewrite it directly from normal usage.
- Propose broader instruction changes through the central skill-learning review queue.
- Only promote specific, reusable, evidence-backed lessons into `LEARNED.md`.
