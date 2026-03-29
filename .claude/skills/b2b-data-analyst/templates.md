# B2B Data Analysis Templates

Ready-to-use templates for common B2B product analytics tasks.

---

## 1. Account Health Score Template

```markdown
## Account Health Score: [Account Name]

### Account Overview
- **Account ID:** [ID]
- **Tier:** [Enterprise / Mid-market / SMB]
- **Contract Value:** $[ARR]
- **Contract Start:** [Date]
- **Next Renewal:** [Date]
- **Days to Renewal:** [X]

---

### Health Signals

#### Usage Signals (40% weight)
| Signal | Weight | Raw Value | Score (1-10) | Evidence |
|--------|--------|-----------|--------------|----------|
| Login frequency (MAU) | 15% | [X/month] | [X/10] | Pendo data |
| Feature breadth | 15% | [X/Y features] | [X/10] | Pendo data |
| User growth | 10% | [+X% QoQ] | [X/10] | User count trend |

**Usage Score:** [Weighted Average] / 10

#### Support Signals (25% weight)
| Signal | Weight | Raw Value | Score (1-10) | Evidence |
|--------|--------|-----------|--------------|----------|
| Open tickets | 10% | [X open] | [X/10] | Zendesk data |
| CSAT score | 10% | [X.X/5] | [X/10] | Survey data |
| Escalations | 5% | [X last 90d] | [X/10] | Support data |

**Support Score:** [Weighted Average] / 10

#### Payment Signals (20% weight)
| Signal | Weight | Raw Value | Score (1-10) | Evidence |
|--------|--------|-----------|--------------|----------|
| Payment status | 10% | [Current/Late] | [X/10] | Billing data |
| ARR growth | 10% | [+X% YoY] | [X/10] | Revenue data |

**Payment Score:** [Weighted Average] / 10

#### Engagement Signals (15% weight)
| Signal | Weight | Raw Value | Score (1-10) | Evidence |
|--------|--------|-----------|--------------|----------|
| NPS response | 5% | [X/10] | [X/10] | Survey data |
| Champion activity | 5% | [Active/Inactive] | [X/10] | Login data |
| Event attendance | 5% | [X events] | [X/10] | Marketing data |

**Engagement Score:** [Weighted Average] / 10

---

### Overall Health Score

| Category | Weight | Score | Weighted |
|----------|--------|-------|----------|
| Usage | 40% | [X.X] | [X.XX] |
| Support | 25% | [X.X] | [X.XX] |
| Payment | 20% | [X.X] | [X.XX] |
| Engagement | 15% | [X.X] | [X.XX] |
| **Total** | 100% | - | **[X.X]/10** |

### Health Status: [Healthy / At Risk / Critical]

**Thresholds:**
- 8.0 - 10.0: Healthy ✅
- 5.0 - 7.9: At Risk ⚠️
- 0 - 4.9: Critical 🔴

---

### Recommended Actions
1. [Action based on lowest scoring area]
2. [Action based on upcoming renewal]
3. [Action based on expansion opportunity]

### Owner: [CS/Account Manager Name]
### Last Updated: [Date]
```

---

## 2. Retention Analysis Template

```markdown
## Retention Analysis: [Product/Segment]

### Executive Summary
- **Cohort analyzed:** [Time period]
- **Cohort size:** [N accounts]
- **D30 retention:** [X]% ([Trend: ↑↓→ vs prior cohort])
- **D90 retention:** [X]% ([Trend: ↑↓→ vs prior cohort])
- **Key insight:** [One sentence takeaway]

---

### Retention by Cohort

| Cohort | Size | D1 | D7 | D14 | D30 | D60 | D90 | Trend |
|--------|------|----|----|-----|-----|-----|-----|-------|
| [Month Q] | [N] | [X]% | [X]% | [X]% | [X]% | [X]% | [X]% | [↑↓→] |

---

### Retention Curve Shape

- [ ] **Steep initial drop** → Onboarding/activation problem
- [ ] **Gradual decline** → Engagement decay
- [ ] **Flattening** → Healthy retention
- [ ] **Secondary drop at day X** → [Explain: renewal/contract issue]

**Curve flattens at:** Day [X]

---

### Key Findings

1. **[Finding 1]**: [Data point + interpretation]
2. **[Finding 2]**: [Data point + interpretation]
3. **[Finding 3]**: [Data point + interpretation]

---

### Recommended Actions

| Priority | Action | Expected Impact | Owner |
|----------|--------|-----------------|-------|
| 1 | [Action] | [+X pp D30] | [Team] |
| 2 | [Action] | [+X pp D90] | [Team] |

**Analyst:** [Name]
**Date:** [Date]
```

---

## 3. Executive Summary Template

```markdown
## [Product Name] Analytics: [Time Period] Summary

### 📊 Headline Metric
**[Metric Name]: [Value] ([Trend: ↑↓→ X% vs last period)**

[One sentence context on what this means for business health]

---

### Key Metrics at a Glance

| Metric | Current | vs Last Period | vs Target | Status |
|--------|---------|----------------|-----------|--------|
| [Metric 1] | [X] | [↑↓→ X%] | [On track / At risk] | 🟢🟡🔴 |
| [Metric 2] | [X] | [↑↓→ X%] | [On track / At risk] | 🟢🟡🔴 |
| [Metric 3] | [X] | [↑↓→ X%] | [On track / At risk] | 🟢🟡🔴 |
| [Metric 4] | [X] | [↑↓→ X%] | [On track / At risk] | 🟢🟡🔴 |

---

### Top 3 Insights

**1. [Insight Headline]**
- Data: [Key data point]
- Meaning: [What it means]
- Action: [What we're doing]

**2. [Insight Headline]**
- Data: [Key data point]
- Meaning: [What it means]
- Action: [What we're doing]

**3. [Insight Headline]**
- Data: [Key data point]
- Meaning: [What it means]
- Action: [What we're doing]

---

### Areas of Focus

| Area | Status | Detail | Owner |
|------|--------|--------|-------|
| [Area 1] | 🟢🟡🔴 | [Brief status] | [Name] |
| [Area 2] | 🟢🟡🔴 | [Brief status] | [Name] |
| [Area 3] | 🟢🟡🔴 | [Brief status] | [Name] |

---

### Key Decisions Needed

1. **[Decision]**: [Context] - Decision needed by [Date]
2. **[Decision]**: [Context] - Decision needed by [Date]

---

**Prepared by:** [Name]
**Date:** [Date]
**Next update:** [Date]
```

---

## Quick Reference: Metric Definitions

| Metric | Definition | Formula |
|--------|------------|---------|
| **MAU** | Monthly Active Users | Count of unique users with activity in last 30 days |
| **WAU** | Weekly Active Users | Count of unique users with activity in last 7 days |
| **DAU** | Daily Active Users | Count of unique users with activity today |
| **D+N Retention** | N-day retention | % of cohort returning on day N |
| **NRR** | Net Revenue Retention | (Start MRR + Expansion - Contraction - Churn) / Start MRR |
| **GRR** | Gross Revenue Retention | (Start MRR - Contraction - Churn) / Start MRR |
| **Activation Rate** | % completing key action | Users completing action / Total users |
| **Feature Adoption** | % using feature | Users who used / Users with access |
| **Churn Rate** | % leaving | Churned customers / Starting customers |
| **CAGR** | Compound Annual Growth Rate | (End/Start)^(1/years) - 1 |
