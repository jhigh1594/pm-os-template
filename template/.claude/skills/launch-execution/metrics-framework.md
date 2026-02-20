# Launch Metrics Framework

Measure what matters. Avoid vanity metrics.

---

## Metrics Philosophy

**Good launch metrics:**
- Connect to business outcomes (revenue, retention, efficiency)
- Have clear targets set before launch
- Include both leading and lagging indicators
- Are actionable (inform decisions, not just report status)

**Bad launch metrics:**
- Vanity metrics (page views, social impressions without conversion)
- Metrics without context or targets
- Metrics that don't inform decisions
- Too many metrics (analysis paralysis)

---

## Metrics by Launch Tier

### Tier 1 Metrics (Strategic Launch)

| Category | Metric | Target Example | Tracking Frequency |
|----------|--------|----------------|-------------------|
| **Adoption** | % of target segment active | 40% in 90 days | Weekly |
| **Revenue** | Incremental ARR attributed | $500K in 6 months | Monthly |
| **Engagement** | Feature usage depth | 3+ sessions/week | Weekly |
| **Satisfaction** | Feature NPS / CSAT | NPS > 40 | Monthly |
| **Sales** | Win rate in competitive deals | +10% vs. baseline | Monthly |
| **Awareness** | Web traffic to feature page | 10K unique visitors | Weekly |
| **Support** | Ticket volume trend | Spike then decline | Daily then weekly |

### Tier 2 Metrics (Major Feature)

| Category | Metric | Target Example | Tracking Frequency |
|----------|--------|----------------|-------------------|
| **Adoption** | % of existing customers active | 25% in 60 days | Weekly |
| **Engagement** | Weekly active users | 1,000 WAU | Weekly |
| **Retention** | Feature retention (D7, D30) | 60% D7 retention | Weekly |
| **Support** | Ticket volume + sentiment | <50 tickets/month | Weekly |
| **Feedback** | Qualitative feedback collection | 50 responses | Monthly |

### Tier 3 Metrics (Enhancement)

| Category | Metric | Target Example | Tracking Frequency |
|----------|--------|----------------|-------------------|
| **Adoption** | Unique users | Track usage | Monthly |
| **Feedback** | Qualitative feedback | Collect 10+ responses | Monthly |
| **Support** | Related ticket volume | Monitor only | As needed |

---

## Leading vs. Lagging Indicators

### Leading Indicators (Predictive)
*Use these to course-correct during launch*

| Leading Indicator | What It Tells You | Action If Low |
|-------------------|-------------------|---------------|
| **Email open rate** | Interest in announcement | Test subject lines, resend to non-openers |
| **Demo requests** | Sales interest | Increase outreach, add social proof |
| **In-app click rate** | Feature discovery | Improve in-app messaging placement |
| **Trial activations** | Willingness to try | Simplify activation flow |
| **Sales conversations** | Competitive traction | Arm sales with more proof points |

### Lagging Indicators (Outcome)
*Use these to evaluate launch success*

| Lagging Indicator | What It Tells You | Action If Low |
|-------------------|-------------------|---------------|
| **Feature adoption %** | Long-term value to customers | Improve onboarding, add use cases |
| **Revenue attributed** | Business impact | Review pricing, positioning |
| **Retention rate** | Stickiness | Investigate churn reasons |
| **NPS/CSAT** | Customer satisfaction | Address feedback, improve UX |

---

## Adoption Tracking

### Adoption Funnel

```
[Awareness] → [Discovery] → [Activation] → [Usage] → [Retention]
     │             │             │            │           │
   Reached      Clicked       First use    Repeated    Still using
   (impressions) (CTR)        (activation) (depth)     (retention)
```

### Adoption Metrics Template

```markdown
# Adoption Tracker: [Feature Name]

## Target Segment
- **Total addressable:** [# customers / # users]
- **Target for launch:** [# customers / # users] ([X%] of addressable)

## Weekly Adoption

| Week | Aware | Activated | Active (3+ uses) | Retained (D7) | Retained (D30) |
|------|-------|-----------|------------------|----------------|-----------------|
| W1 | [%] | [%] | [%] | — | — |
| W2 | [%] | [%] | [%] | [%] | — |
| W3 | [%] | [%] | [%] | [%] | — |
| W4 | [%] | [%] | [%] | [%] | [%] |
| ... | ... | ... | ... | ... | ... |

## Segment Breakdown
| Segment | % Activated | % Active | Notes |
|---------|-------------|----------|-------|
| [Segment 1] | [%] | [%] | [Observation] |
| [Segment 2] | [%] | [%] | [Observation] |

## Cohort Retention
| Cohort | D1 | D7 | D14 | D30 | D60 | D90 |
|--------|-----|-----|-----|-----|-----|-----|
| [Week 1] | [%] | [%] | [%] | [%] | [%] | [%] |
| [Week 2] | [%] | [%] | [%] | [%] | — | — |
```

---

## Success Criteria Definition

### Setting Targets

```markdown
# Success Criteria: [Feature Name]

## Definition of Success
[Feature] will be considered successful if:

### Must-Have Targets (All must be met)
1. **Adoption:** [X%] of target segment active within [timeframe]
2. **Revenue:** $[X] attributed revenue within [timeframe]
3. **Satisfaction:** [X] feature NPS or [X]% CSAT

### Stretch Targets (Nice to have)
1. **Viral adoption:** [X%] organic growth month-over-month
2. **Competitive wins:** [X] deals won specifically citing feature
3. **Press/analyst coverage:** [X] mentions in target publications

## Failure Criteria
The launch will be considered unsuccessful if:
- Adoption < [X%] within [timeframe]
- Support ticket volume > [X] with negative sentiment
- Customer churn attributed to feature > [X]

## Evaluation Timeline
- **30-day check:** Leading indicators review
- **60-day check:** Mid-course correction decision
- **90-day review:** Final success/failure assessment
```

---

## Measurement Infrastructure

### Data Sources

| Metric Type | Data Source | Owner |
|------------|-------------|-------|
| **Product usage** | Analytics (Amplitude, Mixpanel, Pendo) | Product |
| **Revenue** | CRM (Salesforce, HubSpot) | Finance/Sales Ops |
| **Support volume** | Support system (Zendesk, Intercom) | Support Lead |
| **Customer feedback** | Surveys (Delighted, Typeform) | CS/PM |
| **Sales activity** | CRM + Sales enablement | Sales Ops |
| **Web/marketing** | Marketing analytics | Marketing |

### Dashboard Requirements

```markdown
# Launch Dashboard: [Feature Name]

## Real-Time (Launch Week)
- Daily active users
- Activation rate
- Support ticket volume
- Key error rates

## Weekly (Month 1)
- Adoption by segment
- Feature usage depth
- Retention cohorts
- NPS/CSAT trend
- Support ticket trend

## Monthly (Quarter 1)
- Adoption trend vs. target
- Revenue attribution
- Competitive win rate
- Customer proof points collected
```

---

## Post-Launch Review Framework

### 30-Day Review

```markdown
# 30-Day Launch Review: [Feature Name]

## Leading Indicators
| Metric | Target | Actual | Status |
|--------|--------|--------|--------|
| Awareness (reached) | [#] | [#] | [🟢/🟡/🔴] |
| Activation rate | [%] | [%] | [🟢/🟡/🔴] |
| Early engagement | [#] | [#] | [🟢/🟡/🔴] |

## What's Working
- [Observation 1]
- [Observation 2]

## What's Not Working
- [Observation 1]
- [Observation 2]

## Course Corrections Needed
- [ ] [Action 1]
- [ ] [Action 2]

## Decision
[Continue as planned / Adjust approach / Escalate concerns]
```

### 90-Day Review

```markdown
# 90-Day Launch Review: [Feature Name]

## Success Criteria Assessment
| Criteria | Target | Actual | Met? |
|----------|--------|--------|------|
| Adoption | [%] | [%] | [Yes/No] |
| Revenue | $[#] | $[#] | [Yes/No] |
| Satisfaction | [#] | [#] | [Yes/No] |

## Overall Assessment
**Launch Status:** [Success / Partial Success / Failure]

## Key Learnings
1. [What we learned about customer need]
2. [What we learned about positioning]
3. [What we learned about go-to-market]

## Recommendations
1. [Product recommendation]
2. [Positioning recommendation]
3. [Process improvement for next launch]

## What to Celebrate
[Team and individual contributions]
```

---

## Metrics Anti-Patterns

| Anti-Pattern | Problem | Fix |
|--------------|---------|-----|
| **Too many metrics** | Information overload, no focus | Pick 3-5 key metrics per tier |
| **No targets set** | Can't evaluate success | Set targets before launch |
| **Only vanity metrics** | Doesn't connect to business | Prioritize revenue, adoption, satisfaction |
| **Metrics without owners** | No accountability | Assign metric owners |
| **No course-correction triggers** | Problems discovered too late | Set thresholds for action |
| **Only lagging indicators** | Can't adjust in time | Track leading indicators too |

---

## Quick Reference: Metrics Selection

**For every launch, ask:**
1. What business outcome does this feature drive?
2. What 3-5 metrics prove that outcome?
3. What's our target for each metric?
4. How will we track it?
5. What triggers a course correction?
