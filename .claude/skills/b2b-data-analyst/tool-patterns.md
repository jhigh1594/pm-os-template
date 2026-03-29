# Tool Patterns

Tool-agnostic patterns and specific tool guidance for B2B data analysis.

---

## Pendo (Product Analytics)

### When to Use Pendo
- User behavior tracking (page views, feature clicks)
- Account-level usage aggregation
- Funnel and conversion tracking
- Feature adoption analysis
- Segment-based cohort analysis

### Pendo CLI Commands

**Setup** (from `.claude/commands/pendo.md`):
```bash
# Navigate to Pendo CLI directory
cd ~/pendo-cli

# Environment setup
# PENDO_SUBSCRIPTION_ID and PENDO_APP_ID in .env
```

**Common Queries:**
```bash
# Weekly Active Users (WAU)
python3 -m pendo_cli query wau --last-days 7

# N-Day Active Users
python3 -m pendo_cli query wau --last-days 30

# Visitor data
python3 -m pendo_cli query visitors --last-days 30

# Account data
python3 -m pendo_cli query accounts --last-days 30

# List segments
python3 -m pendo_cli segments list
```

### Pendo Analysis Patterns

**Feature Adoption Query:**
1. Identify feature tag name in Pendo
2. Query visitors who triggered feature event
3. Cross-reference with account data
4. Calculate adoption rate = users / total users with access

**Account Health from Pendo:**
1. Query account activity (last login, feature usage breadth)
2. Calculate days since last activity
3. Flag accounts with no activity > 30 days as at-risk
4. Segment by usage frequency (daily, weekly, monthly, inactive)

---

## SQL Patterns

### When to Use SQL
- Complex joins across data sources
- Custom aggregations not available in tools
- Historical data analysis
- Data warehouse queries
- Revenue/payment data analysis

### Common SQL Templates

**Cohort Retention Query:**
```sql
WITH cohorts AS (
  SELECT
    user_id,
    account_id,
    DATE_TRUNC('week', MIN(activity_date)) AS cohort_week
  FROM user_activity
  GROUP BY user_id, account_id
),
retention AS (
  SELECT
    c.cohort_week,
    COUNT(DISTINCT c.user_id) AS cohort_size,
    COUNT(DISTINCT CASE
      WHEN a.activity_date >= c.cohort_week + INTERVAL '7 days'
      THEN c.user_id
    END) AS retained_d7
  FROM cohorts c
  LEFT JOIN user_activity a ON c.user_id = a.user_id
  GROUP BY c.cohort_week
)
SELECT
  cohort_week,
  cohort_size,
  ROUND(100.0 * retained_d7 / cohort_size, 1) AS d7_retention_pct
FROM retention
ORDER BY cohort_week;
```

**Funnel Analysis Query:**
```sql
WITH funnel_steps AS (
  SELECT
    user_id,
    MIN(CASE WHEN event = 'page_view' THEN event_date END) AS step_1,
    MIN(CASE WHEN event = 'signup' THEN event_date END) AS step_2,
    MIN(CASE WHEN event = 'first_login' THEN event_date END) AS step_3
  FROM events
  WHERE event_date >= '2025-01-01'
  GROUP BY user_id
)
SELECT
  COUNT(*) AS total_users,
  COUNT(step_1) AS step_1_page_view,
  COUNT(step_2) AS step_2_signup,
  COUNT(step_3) AS step_3_first_login,
  ROUND(100.0 * COUNT(step_2) / NULLIF(COUNT(step_1), 0), 1) AS s1_to_s2_rate
FROM funnel_steps;
```

---

## Spreadsheet Analysis

### When to Use Spreadsheets
- Quick ad-hoc analysis
- Data from multiple sources needs joining
- Executive-friendly output needed
- Prototyping before building in tools
- Small datasets (< 100K rows)

### Pivot Table Patterns

**Cohort Analysis Pivot:**
```
Rows: Cohort Week
Columns: Days Since Signup (7, 14, 30, 60, 90)
Values: Count of Active Users (as % of cohort size)
```

**Segment Comparison Pivot:**
```
Rows: Account Tier (Enterprise, Mid-market, SMB)
Columns: Metric (MAU, Feature Adoption, Retention)
Values: Average or Sum per segment
```

### Common Spreadsheet Formulas

**Retention Rate:**
```
= (End Users - New Users) / Start Users
```

**Growth Rate:**
```
= (New Value - Old Value) / Old Value
```

**Moving Average (7-day):**
```
= AVERAGE(OFFSET(cell, -6, 0, 7, 1))
```

---

## Cross-Tool Workflows

### Pendo → SQL Workflow
1. **In Pendo**: Identify user segment of interest
2. **Export**: User IDs or account IDs from Pendo
3. **In SQL**: Join with revenue/support data
4. **Analyze**: Correlate usage with business outcomes

### SQL → Spreadsheet Workflow
1. **In SQL**: Query and aggregate data
2. **Export**: CSV from query results
3. **In Spreadsheet**: Create pivot tables and visualizations
4. **Format**: Executive-friendly charts and summaries

---

## Data Quality Checklist

Before trusting any data:

- [ ] **Freshness**: When was this data last updated?
- [ ] **Completeness**: Are there missing values? Expected?
- [ ] **Consistency**: Do related metrics align?
- [ ] **Accuracy**: Spot-check against known examples
- [ ] **Definition**: Is this metric defined consistently across sources?
- [ ] **Sample**: Is this all data or a sample? If sample, how representative?

---

## Implementation Artifacts

Every analysis should produce these deliverables:

### 1. Executive Summary (2-3 sentences)
```
[What we found] + [Business impact] + [Recommended action]

Example: "Feature X adoption reached 35% of accounts, with adopters showing 8pp higher D30 retention. Expansion opportunity exists in mid-market segment (42% untapped). Recommend prioritizing adoption campaign for Q2."
```

### 2. Methodology Note
```
- Data source: Pendo, last 90 days
- Segments: Enterprise (N=45), Mid-market (N=120), SMB (N=200)
- Metric definition: Account with ≥1 feature use in period
- Time range: 2025-01-01 to 2025-03-31
```

### 3. Data Quality Flags
```
- Small sample: Enterprise segment N=45 (wide CIs, interpret with caution)
- Test accounts excluded: Yes (15 employee accounts removed)
- Data completeness: 98% (3% accounts missing usage data)
```

### 4. Follow-up Questions
```
- What drives higher adoption in mid-market?
- Which specific features predict retention?
- Can we identify the "aha moment" for feature X?
```

---

## Code Pattern Examples

### Pendo CLI: Statistical Comparison

```bash
# Compare adoption before/after feature launch
python3 -m pendo_cli query feature-adoption \
  --feature "feature_x" \
  --compare "before:2025-01-01,after:2025-02-01" \
  --segment "account_tier" \
  --output adoption_comparison.csv

# Account-level cohort retention with confidence intervals
python3 -m pendo_cli query cohort-retention \
  --cohort-type "signup_month" \
  --retention-days "7,30,90" \
  --confidence-interval "95" \
  --last-days 180
```

### SQL: Statistical Testing Templates

**Two-proportion z-test (adoption comparison):**

```sql
-- Test: Did adoption rate change after launch?
-- Returns: z-score, p-value for difference in proportions

WITH pre_post AS (
  SELECT
    CASE WHEN event_date < '2025-02-01' THEN 'pre' ELSE 'post' END as period,
    COUNT(DISTINCT CASE WHEN used_feature THEN account_id END) as adopters,
    COUNT(DISTINCT account_id) as total
  FROM account_events
  WHERE event_date BETWEEN '2025-01-01' AND '2025-03-01'
  GROUP BY period
),
stats AS (
  SELECT
    period,
    adopters,
    total,
    adopters::FLOAT / total as p,
    SQRT(p * (1-p) / total) as se
  FROM pre_post
)
SELECT
  (SELECT p FROM stats WHERE period='post') -
  (SELECT p FROM stats WHERE period='pre') as diff,
  (SELECT p FROM stats WHERE period='post') -
  (SELECT p FROM stats WHERE period='pre') /
  SQRT(POWER((SELECT se FROM stats WHERE period='post'), 2) +
        POWER((SELECT se FROM stats WHERE period='pre'), 2)) as z_score,
  -- For large samples, z > 1.96 indicates p < 0.05
  CASE
    WHEN ABS((SELECT p FROM stats WHERE period='post') -
           (SELECT p FROM stats WHERE period='pre')) /
         SQRT(POWER((SELECT se FROM stats WHERE period='post'), 2) +
               POWER((SELECT se FROM stats WHERE period='pre'), 2)) > 1.96
    THEN 'Significant (p < 0.05)'
    ELSE 'Not significant'
  END as significance
FROM pre_post;
```

**Percentile calculation (account-level benchmarking):**

```sql
-- Calculate percentile ranks for account metrics
-- Useful for identifying top/bottom performers

WITH account_metrics AS (
  SELECT
    account_id,
    COUNT(DISTINCT activity_date) as active_days,
    SUM(CASE WHEN used_feature THEN 1 ELSE 0 END) as features_used
  FROM account_activity
  WHERE activity_date >= CURRENT_DATE - INTERVAL '90 days'
  GROUP BY account_id
),
percentiles AS (
  SELECT
    account_id,
    active_days,
    PERCENT_RANK() OVER (ORDER BY active_days) as days_percentile,
    features_used,
    PERCENT_RANK() OVER (ORDER BY features_used) as features_percentile
  FROM account_metrics
)
SELECT
  account_id,
  active_days,
  ROUND(days_percentile::NUMERIC, 3) as days_pct_rank,
  features_used,
  ROUND(features_percentile::NUMERIC, 3) as features_pct_rank,
  CASE
    WHEN days_percentile >= 0.9 THEN 'Top 10% active'
    WHEN days_percentile <= 0.25 THEN 'Bottom 25% active'
    ELSE 'Middle 50%'
  END as activity_tier
FROM percentiles
ORDER BY active_days DESC;
```

### Spreadsheet: Statistical Functions

**Confidence interval in Excel/Google Sheets:**

```
=CONFIDENCE.NORM(alpha, standard_dev, size)
=CONFIDENCE.T(alpha, standard_dev, size)

For 95% CI of proportion (adoption rate):
= p ± 1.96 * SQRT(p*(1-p)/N

Example: p=35%, N=120
= 0.35 ± 1.96 * SQRT(0.35*0.65/120)
= 0.35 ± 0.085
= [26.5%, 43.5%]
```

**Correlation analysis (feature usage vs retention):**

```
=CORREL(feature_usage_range, retention_rate_range)

For statistical significance:
=T.TEST(adopter_retention_range, non_adopter_retention_range, 2, TAILS)

For effect size (Cohen's d):
=(AVERAGE(adopter_retention) - AVERAGE(non_adopter_retention)) /
  SQRT(((VAR.P(adopter_retention) + VAR.P(non_adopter_retention)) / 2))
```

---

## Common Data Issues & Fixes

| Issue | Symptom | Fix |
|-------|---------|-----|
| **Duplicate events** | Inflated counts | Deduplicate on account_id + event_date + feature_name |
| **Missing events** | Gaps in data | Check tracking implementation; note in methodology |
| **Timezone drift** | Activity at wrong times | Convert to consistent timezone before analysis |
| **Account vs user confusion** | Counts don't match | Clarify aggregation level; prefer account for B2B |
| **Bot traffic** | Suspicious patterns | Filter by activity patterns (>100 events/day) |
| **Test accounts** | Internal users in data | Exclude test/employee accounts explicitly |
| **Seasonality** | Misleading trends | Compare year-over-year, not sequential periods |

---

## Analysis Deliverables Template

```markdown
## Analysis: [Title]

### Executive Summary
[2-3 sentences: finding + impact + action]

### Methodology
- **Data source**: [Pendo/SQL/etc]
- **Time range**: [dates]
- **Segments**: [defined]
- **Metric definitions**: [clear definitions]

### Key Findings
1. [Finding with data]
2. [Finding with data]
3. [Finding with data]

### Data Quality
- **Sample size**: [N accounts]
- **Completeness**: [%]
- **Known issues**: [any limitations]

### Recommendations
| Priority | Action | Expected Impact | Owner |
|----------|--------|-----------------|-------|
| 1 | [action] | [impact] | [owner] |

### Follow-up Questions
- [question 1]
- [question 2]

### Appendix: Queries/Code
[reproducible analysis artifacts]
```
