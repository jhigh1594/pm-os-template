# Full PRD Guide

Complete workflow for comprehensive Product Requirements Documents when features require detailed alignment, cross-team coordination, and thorough risk management.

## When to Use Full PRD Format

Choose this format when:
- **Investment is significant** (>1 month engineering time)
- **Multiple teams involved** (design, engineering, analytics, operations)
- **Technical complexity** is high with many dependencies
- **Stakeholder alignment** is challenging (executives, legal, security)
- **Risk is high** (revenue impact, reputation, compliance)
- **Comprehensive documentation needed** for audit/legal purposes

## Document Structure (10 Parts)

### Part 1: Problem Alignment

**Purpose**: Establish why we're building this before discussing solutions.

#### TL;DR

**Purpose**: Executive summary structured for quick scanning and clear decision-making.

**What to solve**:
- [Problem statement 1: Core issue with specific users affected]
- [Problem statement 2: Pain point with quantified impact] (if needed)

**Why solve**:
- [Business impact: Revenue/cost/strategic value with numbers]
- [User benefit: Measurable outcome change]

**How to solve**:
- [Solution approach: High-level concept in 1-2 sentences]
- [Differentiator: What makes this solution unique vs alternatives]

**AI Context**: Keep tight (~0.5 pages). Use bullets, not paragraphs. Each bullet 1-2 sentences max with specific numbers. Forces separation of problem (what), justification (why), and approach (how).

#### Problem Statement
**Who is affected**: Specific user persona or segment
**The problem**: What's broken, missing, or painful
**Impact**: Quantify time lost, errors made, revenue at risk, churn driver

**Evidence confidence**:
- ☐ Validated (data/research)
- ☐ Assumed (logical inference)
- ☐ TBD (needs validation)

**Example**:
```
Who: Enterprise program managers coordinating 50+ teams
Problem: Manually tracking dependencies across 15+ Jira boards
Impact: 4-6 hours/week wasted, 30% critical dependencies missed causing delays
Evidence: Validated - 12 customer interviews, support ticket analysis
```

#### Current Alternatives & Gaps
How do users solve this today, and why aren't these solutions good enough?

**Competitor Solutions:**
1. **Competitor A**: [How they solve it] → **Gap**: [Why it's not good enough]
2. **Competitor B**: [How they solve it] → **Gap**: [Why it's not good enough]

**Current Workarounds:**
- **What users do**: [Manual process/third-party tool]
- **Why it's painful**: [Time cost, error rate, frustration]

**Cost of Doing Nothing:**
[What happens if they don't solve this - tolerable or critical?]

**Unmet Needs:**
- What they wish they could do but can't with any current solution

#### Desired Outcome
Describe the user's world AFTER we solve this.

Focus on the outcome they experience, not the feature we build.

**Example**: "A program manager sees all cross-team dependencies on a single screen, identifies blockers 2 weeks before they impact delivery, and confidently commits to dates in stakeholder meetings."

#### Strategic Fit

**Purpose**: Connect this feature to broader company strategy and current initiatives.

[Which company bet/initiative this enables. Be specific about strategic alignment.]

**Example**: "Aligns with Q3 'AI-First Productivity' initiative and directly supports our goal to increase daily active usage by 12%."

**AI Context**: Be explicit about how this feature advances current company priorities. Include specific metrics or goals from company strategy. If it doesn't clearly fit a strategic initiative, question whether it should be built now.

#### Customer Insights & Motivating Data

**Motivating Data** [Quantitative evidence]:
- Metric 1: [Current state]
- Metric 2: [Gap to target]
- Metric 3: [Market benchmark]

**Example**:
- Current avg reply time: 47 seconds
- Target: <40 seconds (15% improvement)
- Slack benchmark: 38 seconds

**Qualitative Evidence** [3 user quotes]:

**Example quotes**:
1. "I spend half my day typing the same responses" — Enterprise Admin, 500+ person org
2. "By the time I reply, the conversation has moved on" — Power User, 50 messages/day
3. "I need faster ways to respond without seeming robotic" — Team Lead, Customer Success

**Open questions to validate**:
- What we still need to learn

---

### Part 2: Solution Alignment

**Purpose**: Define what we're building and how we'll know if it worked.

#### Hypothesis & Expected Impact
State the bet we're making.

**Hypothesis**:
If we [build X], then [user segment] will [change behavior], resulting in [measurable outcome].

**Expected impact**:
- Primary metric improvement: "Reduce time-to-detection of blockers by 50%"
- Secondary benefit: "Decrease status meeting time by 2 hours/week"
- Business outcome: "Improve deal win rate for prospects citing dependency pain"

**ROI justification**:
Why the investment is worth it - development cost vs expected return

**Key assumptions to validate**:
- Assumption 1 — How we'll test: Method
- Assumption 2 — How we'll test: Method

#### Proposed Solution
High-level description of what we're building.

**What we're building**:
[Description focusing on capabilities, not implementation]

**Key capabilities**:
1. Capability 1
2. Capability 2
3. Capability 3

**Explicitly out of scope (for this release)**:
- Thing we're not building and why
- Thing we're deferring to future iteration

**Design artifacts**:
- Link to mockups/prototypes
- Link to user flow diagrams

#### How We Differentiate
How is our solution better than existing alternatives?

**vs Competitor A**: [Our advantage]
**vs Competitor B**: [Our advantage]
**vs Current workarounds**: [Our advantage]

**Defensibility**: What makes this hard for others to copy - platform integration, data advantage, UX, network effects

#### Solutions Considered
What alternatives did we evaluate? Why this path?

| Option | Description | Why We Rejected |
|--------|-------------|-----------------|
| Option A | Brief description | Cost, complexity, doesn't solve root problem |
| Option B | Brief description | Reason |
| Option C | Brief description | Reason |

**Why the chosen approach wins**:
Summary of why this solution best balances value, feasibility, and risk

#### Key Use Cases / Workflows
Describe 2-4 core scenarios in detail.

**Use Case 1: [Name]**
- **User**: [Persona]
- **Context**: [When/why they need this]
- **Goal**: [What they're trying to accomplish]
- **Workflow**:
  1. Step 1
  2. Step 2
  3. Step 3
- **Success looks like**: [Observable outcome]

[Repeat for Use Cases 2-3]

#### Success Metrics
Define how we measure success.

**Primary metric (North Star)**:
[Metric name]: [Current state] → [Target state] by [Timeframe]

**Example**: "Critical dependencies missed: 30% → <5% within 3 months"

**Leading indicators (measurable in 2-4 weeks)**:
- Metric 1: Target
- Metric 2: Target

**Guardrail metrics (what we don't want to break)**:
- Metric: Should not decrease below threshold

**Instrumentation requirements**:
- What we need to track
- Events to log

#### Dependencies & Risks
What could block or derail this?

**Technical dependencies**:
- Dependency: Owner — Status: On track/At risk/Blocked

**Cross-team dependencies**:
- Team: What we need from them — Status: Confirmed/Requested/TBD

**Risks**:

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| Risk 1 | High/Med/Low | High/Med/Low | How we reduce it |
| Risk 2 | Likelihood | Impact | Mitigation |

#### Open Questions
What's still unresolved?

| Question | Owner | Target Date | Status |
|----------|-------|-------------|--------|
| Question | Name | Date | Open/Resolved |

#### Decision Log
Track decisions made after initial draft.

| Date | Decision | Rationale | Decided By |
|------|----------|-----------|------------|
| Date | What was decided | Why | Who |

---

## Appendix (Optional Sections)

### Technical Notes
- Architecture considerations
- API requirements
- Performance requirements
- Scale and reliability targets

### Go-to-Market Considerations
- Launch strategy
- Enablement needs
- Customer communication plan
- Sales/support training

### Research & References
- Links to supporting research
- Customer interview notes
- Competitive analysis
- Market sizing data

---

## Writing Process for Full PRD

### Phase 1: Planning (Speclet)
**Duration**: 1-2 days

Create lightweight exploration document:
- Problem + motivating data (quantitative + 3 user quotes)
- Hypothesis + strategy fit
- Competitive landscape research
- Open questions & owners

**Output**: Alignment to proceed with full PRD

### Phase 2: Kickoff
**Duration**: 2-3 days

Add structure and boundaries:
- Clear in/out of scope
- Initial mockups or prototypes
- Success metrics with thresholds
- Impact sizing (order-of-magnitude)

**Output**: Engineering can estimate effort

### Phase 3: Solution Review
**Duration**: 3-5 days

Detailed specification:
- Complete workflows and use cases
- Edge cases identified
- Tracking requirements specified
- Rollout design v1

**Output**: Engineering can build to this spec

### Phase 4: Launch Readiness
**Duration**: 1-2 days

Pre-ship checklist:
- Testing criteria defined
- Monitoring and alerts configured
- Runbook + fallbacks + kill switch
- Legal/Security review complete

**Output**: Safe, measurable launch

### Phase 5: Impact Review (Post-Ship)
**Duration**: Ongoing

Learning and iteration:
- Link results document at top of PRD
- What surprised us? What will we change?
- Add new examples from production
- Decision: iterate, scale, or retire

**Output**: Close the loop, capture learnings

---

## Quality Checklist for Full PRD

Before considering complete:

### Strategic Clarity
- [ ] Problem statement is specific and evidence-based
- [ ] Hypothesis is clear and testable
- [ ] Strategy fit is explicit
- [ ] Opportunity sizing is quantified

### Measurability
- [ ] Primary metric has specific threshold (not "improve")
- [ ] Leading indicators defined for early signals
- [ ] Guardrail metrics protect existing value
- [ ] Instrumentation plan is concrete

### Actionability
- [ ] Engineering team knows exactly what to build
- [ ] Use cases cover major workflows
- [ ] Edge cases are enumerated
- [ ] Design artifacts exist and are linked

### Risk Management
- [ ] Technical dependencies identified with owners
- [ ] Cross-team dependencies confirmed
- [ ] Risks assessed with mitigation plans
- [ ] Rollback strategy exists

### Decision Quality
- [ ] Non-goals are explicit
- [ ] Alternatives considered and rejected with rationale
- [ ] Every "will" has "how" and "when"
- [ ] Owners assigned for open questions

### Stakeholder Alignment
- [ ] Problem alignment achieved before solution discussion
- [ ] Success criteria agreed upon
- [ ] Go-to-market plan coordinated
- [ ] Legal/security requirements addressed

---

## Common Pitfalls to Avoid

### Pitfall 1: Solution Before Problem
Writing solution section before stakeholders align on problem

**Fix**: Get explicit sign-off on Part 1 (Problem Alignment) before writing Part 2

### Pitfall 2: Vague Metrics
"Improve engagement", "Increase satisfaction", "Reduce costs"

**Fix**: "DAU increases ≥25% (from 1,200 to 1,500+)", "NPS increases from 42 to 48+", "Server costs decrease $12K/month"

### Pitfall 3: Missing Non-Goals
Only listing what's included, not what's excluded

**Fix**: Explicit "Out of Scope" section with rationale for each exclusion

### Pitfall 4: No Customer Evidence
Relying on assumptions and internal opinions

**Fix**: Include 3+ customer quotes, usage data, support tickets, or research findings

### Pitfall 5: One-Time Documentation
Written once, never updated, becomes outdated

**Fix**: Update PRD at each phase, link to results post-launch, maintain decision log

---

## Template Ready to Use

Copy the structure above into your PRD document. For each section:
1. Read the AI Context guidance
2. Fill in based on your feature
3. Mark assumptions explicitly
4. Use specific numbers and examples
5. Get feedback at each phase

Remember: **Decisions over documentation**. Every section should decide something, not just describe something.