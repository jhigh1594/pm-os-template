# One-Pager PRD Guide

Streamlined PRD format for smaller features where the problem is clear and solution is bounded. Get to decisions fast without sacrificing quality.

## When to Use One-Pager Format

Choose this format when:
- **Problem is clear and validated** (not exploratory)
- **Solution is bounded** (2-4 weeks engineering time)
- **Single team ownership** (minimal cross-team coordination)
- **Stakeholder alignment is straightforward** (not contentious)
- **Risk is low-to-medium** (can iterate if wrong)
- **Speed matters** (need to move quickly)

**Rule of thumb**: If you can explain the feature in 5 minutes and people "get it", use one-pager.

## Document Structure (6 Sections)

### Header

| Field | Value |
|-------|-------|
| **Feature** | [Name] |
| **Author** | [Name] |
| **Status** | Draft / Approved |
| **Target Release** | [Quarter or date] |

---

### 1. Problem

**Purpose**: 2-3 sentences capturing who is affected, what's broken, and what's the impact.

**What to include**:
- Specific user persona or segment
- The painful workflow or gap
- Quantified impact (time, money, errors, frustration)

**Evidence**: Brief source - customer feedback, data, support tickets

**Example**:
```
Sales reps waste 10-15 minutes per demo searching for relevant case studies across
multiple folders and Slack channels. This results in generic demos that don't
resonate with prospects, contributing to 23% demo-to-trial conversion (below 30% target).

Evidence: 8 sales rep interviews, CRM activity logs showing avg 12 min case study lookup time
```

**AI Context**: Focus on concrete problem statement with real data. Avoid vague language like "users want better X".

---

### 2. Current Alternatives

**Purpose**: How do users solve this today? What's wrong with those approaches?

**Format**:
- **They currently**: [Workaround or competitor solution]
- **The gap**: [Why it's not good enough]

**Example**:
```
They currently: Manually search Dropbox folders + Slack + ask colleagues
The gap:
- No filtering by industry/use case/deal size
- Information is scattered and outdated
- Relies on tribal knowledge from senior reps
```

**AI Context**: Show we understand the landscape. Establishes credibility that we're solving a real gap.

---

### 3. Desired Outcome

**Purpose**: What does the user's world look like after we solve this?

**What to include**:
- After-state in user terms (not feature description)
- Observable behavior change
- Measurable improvement

**Example**:
```
Sales reps find 3 relevant, up-to-date case studies in <2 minutes filtered by
industry and deal stage. Demo-to-trial conversion increases to 32%+ as prospects
see themselves in the success stories.
```

**AI Context**: Write the after-state as if you're watching the user. What do they do differently?

---

### 4. Solution

**Purpose**: What are we building? Keep it high-level - capabilities, not implementation.

**Format**:
**We will**:
- Capability 1
- Capability 2
- Capability 3 (keep to 2-4 key capabilities)

**We won't (this release)**:
- Out of scope item with brief rationale

**Example**:
```
We will:
- Create searchable case study library with industry/stage/deal size filters
- Surface 3 most relevant case studies based on opportunity details from CRM
- Enable 1-click sharing to prospect email or demo deck

We won't:
- Build case study authoring tools (use existing process)
- Translate case studies (English only for V1)
- Integrate with proposal generation (future enhancement)
```

**AI Context**: Be explicit about what's OUT of scope. This prevents scope creep and sets clear expectations.

---

### 5. How We Differentiate

**Purpose**: Why is our approach better than alternatives?

**What to include**:
1-2 sentences on competitive advantage or unique approach

**Example**:
```
Unlike generic content libraries, our solution uses CRM opportunity data to automatically
surface the most relevant case studies - reducing search time from 12 minutes to under 2
while improving relevance matching.
```

**AI Context**: If you can't articulate a differentiation, question whether this is worth building.

---

### 6. Hypothesis & Success Metric

**Purpose**: The bet we're making and how we'll know if we were right.

**Hypothesis format**:
**If we** [build X], **then** [users will] [change behavior], **resulting in** [outcome].

**Metrics**:
- **Primary metric**: [Metric]: [Current] → [Target] by [Date]
- **Leading indicator**: [What we can measure in 2-4 weeks]

**Example**:
```
Hypothesis:
If we build a CRM-integrated case study library, then sales reps will find relevant
case studies 5x faster, resulting in 25% improvement in demo-to-trial conversion.

Primary metric: Demo-to-trial conversion: 23% → 29%+ within 60 days
Leading indicator: Avg case study lookup time: 12 min → <2 min within 2 weeks
```

**AI Context**: Use specific numbers, not "improve" or "increase". Be testable.

---

### 7. Key Risks

**Purpose**: What could go wrong and how we'll address it.

**Format**:

| Risk | Mitigation |
|------|------------|
| Risk 1 | How we address it |
| Risk 2 | How we address it |

**Example**:

| Risk | Mitigation |
|------|------------|
| Case studies become outdated | Monthly review process + notification to content owner |
| Reps don't trust relevance algorithm | Show match reasoning + allow manual override |
| Low adoption (reps stick to old habits) | Launch with top 20% reps (early adopters) + track usage |

**AI Context**: 2-4 risks maximum. Focus on likely risks with clear mitigation.

---

### 8. Open Questions

**Purpose**: What needs to be resolved before or during implementation.

**Format**:
- [ ] Question 1 — Owner: [Name]
- [ ] Question 2 — Owner: [Name]

**Example**:
- [ ] What's the threshold for "relevance" score? — Owner: PM (test with reps)
- [ ] How do we handle confidential case studies? — Owner: Legal review
- [ ] Where in the CRM UI should this surface? — Owner: Design research

**AI Context**: These should be genuine unknowns, not things you should figure out now.

---

### 9. Decision Log

**Purpose**: Track changes and decisions made after initial draft.

**Format**:

| Date | Decision | Rationale |
|------|----------|-----------|
| Date | What was decided | Why |

**Example**:

| Date | Decision | Rationale |
|------|----------|-----------|
| 2025-12-01 | Limit to English-only for V1 | Translation adds 3 weeks, can validate core hypothesis without it |
| 2025-12-05 | Target top 20% reps for pilot | Early adopters will give better feedback than full rollout |

---

## Socratic Discovery for One-Pagers

**Key Difference from Full PRD**: Ask 2-3 questions (not 3-5) focusing on:

1. **Problem clarity** (most critical)
   - "What specific pain point does this solve?"
   - "How do we know this is a real problem?"

2. **Success criteria** (second most critical)
   - "How will we measure if this feature is successful?"
   - "What would make you consider this a failure?"

3. **Scope** (third - if needed)
   - "What are we NOT doing as part of this?"
   - "If we had half the time, what would we cut?"

**Skip questioning if**:
- User's input already covers problem, solution, success metric, and scope clearly
- User explicitly requests to skip questions

---

## Writing Process for One-Pagers

### Timeline: 2-4 hours total

**Hour 1: Problem & Evidence**
- Write Problem section with specific example
- Gather evidence (quotes, data, tickets)
- Document Current Alternatives

**Hour 2: Solution & Outcomes**
- Draft Desired Outcome (after-state)
- Define Solution (2-4 capabilities)
- **Critical**: Write explicit non-goals

**Hour 3: Metrics & Risks**
- Craft testable hypothesis
- Define primary metric with specific threshold
- Identify 2-4 key risks with mitigation

**Hour 4: Review & Polish**
- Validate against quality checklist
- Get feedback from 1-2 stakeholders
- Update based on input

---

## Quality Checklist for One-Pagers

### Problem Clarity
- [ ] Problem statement is 2-3 sentences
- [ ] Specific user persona identified
- [ ] Impact is quantified
- [ ] Evidence source is cited

### Solution Specificity
- [ ] 2-4 key capabilities listed
- [ ] Non-goals are explicit
- [ ] Solution connects logically to problem

### Success Measurement
- [ ] Hypothesis is testable
- [ ] Primary metric has specific threshold (not "improve")
- [ ] Leading indicator is defined
- [ ] Timeline for measurement is clear

### Risk Management
- [ ] 2-4 key risks identified
- [ ] Mitigation strategy for each risk
- [ ] Risks are realistic (not exhaustive)

### Overall Quality
- [ ] Can be read in 5 minutes
- [ ] Engineering knows what to build
- [ ] Decisions are clear (not descriptions)
- [ ] No vague language ("better", "improve", "enhance")

---

## When to Upgrade to Full PRD

Start with one-pager, but upgrade to full PRD if:

1. **Scope expands** beyond initial estimate (>4 weeks)
2. **Stakeholder alignment becomes challenging** (multiple competing interests)
3. **Technical complexity increases** (more dependencies discovered)
4. **Risk assessment changes** (higher than initially thought)
5. **Multiple teams get involved** (not single team anymore)
6. **Regulatory/legal concerns emerge** (need comprehensive documentation)

**Rule**: If one-pager reaches 4+ pages or requires 10+ minutes to read, upgrade to full PRD structure.

---

## Common Pitfalls for One-Pagers

### Pitfall 1: Too Vague
"Improve the sales process" or "Make demos more engaging"

**Fix**: "Reduce case study lookup time from 12 min to <2 min, increasing demo-to-trial conversion from 23% to 29%+"

### Pitfall 2: Missing Non-Goals
Only saying what's IN scope, not what's OUT

**Fix**: Add explicit "We won't" section with 2-3 clear exclusions

### Pitfall 3: No Evidence
Assuming problem exists without validation

**Fix**: Add evidence source - even if it's just "5 sales rep conversations" or "Support ticket #1234"

### Pitfall 4: Metric Theater
"Increase engagement" or "Improve user satisfaction"

**Fix**: "Weekly active users increases from 1,200 to 1,500+ (25% increase) within 60 days"

### Pitfall 5: Scope Creep in Disguise
Starting with one-pager but sneaking in complexity

**Fix**: If solution has >4 capabilities or >2 pages, consider if full PRD is more appropriate

---

## Template Summary

```markdown
## [Feature Name] - One Pager

| Field | Value |
|-------|-------|
| **Feature** | [Name] |
| **Author** | [Name] |
| **Status** | Draft / Approved |
| **Target Release** | [Quarter/Date] |

### Problem
[2-3 sentences: who, what's broken, impact]
**Evidence**: [Source]

### Current Alternatives
- **They currently**: [Workaround]
- **The gap**: [Why insufficient]

### Desired Outcome
[After-state in user terms]

### Solution
**We will**:
- Capability 1
- Capability 2

**We won't**:
- Out of scope item

### How We Differentiate
[1-2 sentences on competitive advantage]

### Hypothesis & Success Metric
**If we** [X], **then** [behavior], **resulting in** [outcome].

**Primary metric**: [Metric]: [Current] → [Target] by [Date]
**Leading indicator**: [Early signal metric]

### Key Risks
| Risk | Mitigation |
|------|------------|
| [Risk] | [How we address] |

### Open Questions
- [ ] Question — Owner: [Name]

### Decision Log
| Date | Decision | Rationale |
|------|----------|-----------|
```

---

## Key Reminders

1. **Speed is the feature** - One-pager should take 2-4 hours, not days
2. **Decisions over descriptions** - Every section decides something
3. **Non-goals are mandatory** - Explicit scope boundaries prevent creep
4. **Specific metrics only** - "≥25%" not "improve"
5. **Evidence always** - Even if minimal, cite your source
6. **Upgrade when needed** - Don't force complexity into one-pager format