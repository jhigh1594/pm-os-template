# Analysis Patterns

Detailed methodologies for common B2B product analytics tasks.

---

## 1. Cohort Analysis

### What Questions It Answers
- Do newer users retain better than older users?
- How has product quality changed over time?
- Which acquisition cohorts are most valuable?

### How to Structure

**Time-Based Cohorts:**
```
Users grouped by signup/acquisition week/month
Track their behavior over time (D1, D7, D30, etc.)
Compare curves across cohorts
```

**Behavior-Based Cohorts:**
```
Users grouped by action taken (e.g., "used feature X")
Compare retention of users who did vs didn't
Identifies high-value behaviors
```

### B2B Nuance
- Group by **account creation date**, not user signup
- Track **account-level retention**, not individual user
- Consider **contract renewal cycles** (monthly vs annual)

---

## 2. Funnel Analysis

### What Questions It Answers
- Where are users dropping off?
- Which step has the biggest conversion opportunity?
- How does conversion vary by segment?

### How to Structure

**Define the Funnel:**
```
Step 1: Landing page view
Step 2: Sign up
Step 3: First login
Step 4: Key action (activation)
Step 5: Repeat usage
```

**Calculate Conversion:**
- **Step-to-step conversion**: % who complete next step
- **Overall conversion**: % who complete entire funnel
- **Drop-off rate**: % lost at each step

### B2B Nuance
- Funnel may span **multiple users** in same account (evaluator → purchaser → end user)
- Track **account-level conversion**, not just user
- Consider **sales-assisted** vs **self-serve** funnels separately

---

## 3. Retention Curve Analysis

### What Questions It Answers
- Is retention improving over time?
- When do users typically churn?
- What does "stable" retention look like for us?

### How to Structure

**Plot Retention Over Time:**
```
X-axis: Days since first use (0, 1, 7, 14, 30, 60, 90)
Y-axis: % of cohort still active
Multiple lines for different cohorts
```

**Interpret the Curve:**
- **Steep initial drop**: Onboarding/activation problem
- **Gradual decline**: Engagement decay
- **Flattening curve**: Healthy long-term retention
- **Secondary drop**: Feature fatigue or contract renewal

### B2B Nuance
- Retention curves may show **renewal bumps** (annual contracts)
- **Power user curve** (L30/L7 ratio) indicates engagement depth
- Track by **account tier** (enterprise vs SMB curves differ)

---

## 4. Feature Adoption Analysis

### What Questions It Answers
- Is this feature being used?
- Who is using it (power users vs casual)?
- Does feature usage correlate with retention?

### How to Structure

**Adoption Metrics:**
- **Adoption Rate**: % of users who used feature
- **Frequency**: How often it's used
- **Depth**: How much of the feature is used
- **Breadth**: % of features used per account

**Segment Analysis:**
- By user role (admin, end user, viewer)
- By account tier (enterprise, SMB)
- By tenure (new vs legacy users)

### B2B Nuance
- Track **account-level adoption** (did ANYONE in account use it?)
- Measure **breadth** across account (how many users per account?)
- Correlate with **account retention**, not user retention

---

## 5. Account Health Scoring

### What Questions It Answers
- Which accounts are at risk of churning?
- Which accounts are ready for expansion?
- What behaviors predict healthy accounts?

### How to Structure

**Define Health Signals:**
```
Usage signals: Login frequency, feature breadth, user growth
Support signals: Ticket volume, CSAT, escalation count
Payment signals: On-time payment, contract value, growth
Engagement signals: NPS response, webinar attendance, champion activity
```

**Weight and Score:**
```
Health Score = Σ(Signal × Weight)
Typical weights: Usage 40%, Support 25%, Payment 20%, Engagement 15%
```

### B2B Nuance
- Different health models for **different segments** (enterprise vs SMB)
- Include **champion tracking** (key user engagement)
- Factor in **contract timeline** (90 days before renewal = higher weight)

### See Full Template in `templates.md`

---

## 6. A/B Test Analysis

### What Questions It Answers
- Did the treatment perform better than control?
- Is the difference statistically significant?
- What is the business impact?

### How to Structure

**Define the Test:**
```
Hypothesis: [What we believe will happen]
Primary metric: [The key success metric]
Secondary metrics: [Other metrics to watch]
Sample size: [N per variant]
Test duration: [X days]
```

**Analyze Results:**
```
1. Calculate metric for each variant
2. Compute statistical significance (p-value)
3. Calculate confidence interval
4. Estimate business impact
```

### B2B Nuance
- Account-level randomization often better than user-level
- Longer test duration needed (lower volume)
- Watch for **network effects** (users in same account in different variants)

---

## 7. Trend Analysis

### What Questions It Answers
- Are we growing, stable, or declining?
- Is this a seasonal pattern or real change?
- How do we compare to last period/year?

### How to Structure

**Time Comparisons:**
```
Week-over-week (WoW): Short-term momentum
Month-over-month (MoM): Medium-term trend
Year-over-year (YoY): Long-term growth, accounts for seasonality
```

**Calculate Growth:**
```
Growth Rate = (Current - Previous) / Previous × 100%
CAGR = (End/Start)^(1/Years) - 1
```

### B2B Nuance
- Track **account growth** not just user growth
- Seasonal patterns may align with **fiscal years** or **budget cycles**
- Watch for **cohort effects** (new vs legacy customer behavior)

---

## 8. Statistical Rigor (Deep Dive Mode)

When small sample sizes or executive scrutiny requires extra rigor.

### Sample Size Assessment

**For statistical validity in B2B:**
```
- N ≥ 100 accounts: Can use parametric tests, report precise CIs
- N 30-99 accounts: Use parametric tests, report wide CIs, flag limitations
- N < 30 accounts: Use non-parametric tests, or report as "descriptive only"
- N < 10 accounts: No statistical claims - present as case studies
```

**B2B sample size reality:**
- Enterprise segment: Often N < 50 (need longer time windows)
- Mid-market: N 50-200 (adequate for most tests)
- SMB: N 200+ (good statistical power)
- Feature adopters: Often skewed - use median, not mean

### Effect Size Reporting

**Don't just say "statistically significant" - report practical impact:**

**For retention differences:**
```
"D30 retention increased 5 percentage points (from 20% to 25%, p=0.03, N=120)"

Better: Add effect size
"D30 retention +5pp (20%→25%, p=0.03, Cohen's h=0.22, small effect, N=120)"
```

**For revenue impact:**
```
"Expansion revenue +$15K ARR per account (95% CI: $8K-$22K, p=0.01, N=87)"
```

**For feature adoption:**
```
"Feature adoption: 35% of accounts (95% CI: 26%-44%, N=120, vs 20% baseline)"
```

### Confidence Intervals for B2B Metrics

**When N is small (common in B2B), always report CI:**

**Quick CI approximation (95%):**
```
For proportions: CI = p ± 1.96 × √(p(1-p)/N)

Example: Adoption = 35%, N=120
SE = √(0.35 × 0.65 / 120) = 0.043
CI = 35% ± 1.96 × 4.3% = 35% ± 8.5% = [26.5%, 43.5%]
```

**For means (revenue, ARR per account):**
```
CI = x̄ ± t × (s/√N)

Use t-table for N-1 degrees of freedom:
- N=30, t=2.04
- N=50, t=2.01
- N=100+, t≈1.96
```

### Sensitivity Analysis

**Test how robust findings are to assumptions:**

```markdown
## Sensitivity Analysis: [Finding]

### Base Result
- Finding: D30 retention 25% (vs 20% baseline, +5pp)
- Sample: N=120 accounts

### Sensitivity Tests

| Variation | Result | Change |
|-----------|--------|--------|
| Exclude top 1% ARR | 24.5% | -0.5pp |
| Use median instead of mean | 24.8% | -0.2pp |
| Extend cohort window by 1 week | 24.2% | -0.8pp |
| Exclude enterprise segment | 23.1% | -1.9pp |

### Conclusion
Finding is robust to outliers and cohort definition, but driven by enterprise segment. Report by segment.
```

### Statistical Testing Templates

**Two-group comparison (e.g., feature adopters vs non-adopters):**

```sql
-- Test: Does feature adoption correlate with retention?
-- Compare D30 retention between adopters and non-adopters

WITH segment_metrics AS (
  SELECT
    account_id,
    CASE WHEN feature_adopted THEN 'adopter' ELSE 'non_adopter' END as segment,
    CASE WHEN last_activity >= cohort_date + 30 THEN 1 ELSE 0 END as retained_d30
  FROM account_cohorts
)
SELECT
  segment,
  COUNT(*) as n,
  AVG(retained_d30) as retention_rate,
  -- Approximate 95% CI for proportion
  AVG(retained_d30) + 1.96 * SQRT(AVG(retained_d30) * (1 - AVG(retained_d30)) / COUNT(*)) as ci_upper,
  AVG(retained_d30) - 1.96 * SQRT(AVG(retained_d30) * (1 - AVG(retained_d30)) / COUNT(*)) as ci_lower
FROM segment_metrics
GROUP BY segment
```

---

## Safety & Data Quality

### Data Privacy

**Never analyze PII without authorization:**
- Exclude employee/test accounts from analysis
- Aggregate before sharing outside organization
- Don't log user emails or personal identifiers in analysis artifacts

### Statistical Validity Flags

**Always flag these issues:**

| Issue | When It Occurs | How to Flag |
|-------|----------------|-------------|
| **Small sample** | N < 30 for statistical tests | "N=XX accounts, descriptive only" |
| **Singular data** | One account dominates metric | "Excluding top 1% ARR: [before]→[after]" |
| **Skewed distribution** | Median ≠ mean by 2x+ | "Reported median; mean=[X]" |
| **Sparse data** | < 5 data points per group | "Insufficient data for comparison" |
| **Time range too short** | < 2 full cycles | "Data covers [X] weeks; interpret with caution" |

### Causal Claims

**Correlation ≠ causation:**

```
OK: "Accounts using feature X have 25% higher retention"
NOT OK: "Feature X causes 25% higher retention"

OK: "A/B test showed feature X increased activation by 15% (p=0.02)"
NOT OK: "Launch drove activation" (without pre/post comparison to control)

OK: "After implementing feature X, support tickets decreased 30%"
NOT OK: "Feature X reduced support tickets" (could be seasonal, other changes)
```

**When you can claim causality:**
- Randomized A/B tests (properly powered)
- Pre/post with control group (difference-in-differences)
- Natural experiments with clear treatment/control
- Never from observational data alone
