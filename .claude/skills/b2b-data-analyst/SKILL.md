---
name: b2b-data-analyst
description: Use when analyzing B2B SaaS product data - usage metrics, retention cohorts, account health, funnel analysis, A/B testing, and connecting product usage to business outcomes. Tool-agnostic with patterns for Pendo, Amplitude, PostHog, SQL, and spreadsheets.
---

# B2B Data Analyst

Extract actionable insights from B2B product data to drive product decisions.

## When This Skill Activates

Use this skill when:
- Analyzing usage trends (MAU/WAU/DAU, feature adoption)
- Running cohort or retention analysis
- Investigating funnel drop-off and conversion
- Measuring feature adoption and activation
- Building account health scores
- Analyzing A/B test results
- Creating dashboards for stakeholders
- Connecting usage data to revenue/business outcomes

## Core Philosophy

| Principle | What It Means |
|-----------|---------------|
| **Insights over reports** | Focus on "so what?" not just "what" |
| **Action over observation** | Every analysis should lead to a decision |
| **B2B mindset** | Accounts matter more than individual users |
| **Tool-agnostic** | Work with whatever data source is available |

---

## Quick Start

### Step 1: Clarify the Question
Before querying data, answer:
1. **What decision** will this analysis inform?
2. **Who is the audience** (exec, product team, sales/CS)?
3. **What metric** best answers the question?
4. **What comparison** provides context (trend, cohort, segment)?

### Step 2: Choose the Right Analysis
| Question Type | Analysis Pattern | See |
|---------------|------------------|-----|
| "Are users sticking around?" | Retention/Cohort | `analysis-patterns.md` |
| "Where are users dropping off?" | Funnel Analysis | `analysis-patterns.md` |
| "Is this feature being used?" | Feature Adoption | `analysis-patterns.md` |
| "Which accounts are at risk?" | Account Health | `templates.md` |
| "Did the experiment work?" | A/B Test Analysis | `analysis-patterns.md` |
| "How are we trending?" | Trend Analysis | `analysis-patterns.md` |

### Step 3: Execute with Appropriate Tool
| Data Source | Tool Pattern | See |
|-------------|--------------|-----|
| Pendo (product analytics) | CLI commands | `tool-patterns.md` |
| Database/warehouse | SQL queries | `tool-patterns.md` |
| Exported data | Spreadsheet | `tool-patterns.md` |

### Step 4: Tell the Story
Match output to audience — and always consider which audience would act on this finding before choosing the format:
- **Executives**: Business impact, one insight per slide, action-oriented — use `/data-story --audience exec` for BLUF format
- **Product Teams**: Methodology, segments, follow-up hypotheses — use `/data-story --audience product` for narrative arc format
- **Sales/CS**: Account-level insights, at-risk signals, expansion opportunities — use `/data-story --audience sales|cs` for quotable proof points or account briefs

**Audience packaging**: After completing any substantive analysis, ask: "Which audience needs to act on this?" If the answer isn't "the PM alone," offer to route via `/data-story --audience [type]` to format it for that audience.

### Step 4.5: Proactive Monitoring — What Else I Noticed

At the end of any analysis, apply the "What would I want to know that I wasn't asked?" lens:

```
Proactive checks (flag any that apply):
- Metric drift: Is any metric 2+ standard deviations from the prior 30-day baseline?
  → If yes: surface it as "Unexpected movement detected: [metric] moved [N]% vs. baseline"
- Cohort divergence: Are newer cohorts behaving differently from older cohorts?
  → If yes: surface as "Cohort shift: [description] — may indicate impact from [recent change]"
- Account concentration risk: Is the top 5 account share of usage changing?
  → If rising: surface as "Concentration risk increasing — [top accounts] represent [X]% of usage"
- Feature adoption plateau: Is any feature adoption curve that was growing now flat (30+ days)?
  → If yes: surface as "Adoption plateau detected: [feature] — worth investigating"
```

Output proactive observations at end of any analysis in a **"What else I noticed"** section. Keep it brief — one sentence per observation + a suggested next action. If nothing notable detected, skip this section (don't say "nothing found" — just omit it).

---

## B2B Metrics Framework

### Usage Metrics
| Metric | Definition | B2B Nuance |
|--------|------------|------------|
| **MAU/WAU/DAU** | Active users in period | Track by account, not just user |
| **Feature Adoption Rate** | % using specific feature | Measure breadth across account |
| **Activation Rate** | % completing key action | Define account-level activation |
| **Session Frequency** | How often users return | Higher = stickier product |

### Retention Metrics
| Metric | Definition | Target |
|--------|------------|--------|
| **N-Day Retention** | % returning after N days | D1: 40%+, D7: 20%+, D30: 10%+ |
| **Cohort Retention Curve** | Retention over time by cohort | Curve should flatten, not drop to zero |
| **GRR** | Gross Revenue Retention | 85%+ for B2B SaaS |
| **NRR** | Net Revenue Retention | 100%+ (expansion > churn) |

### Revenue Metrics
| Metric | Definition | Why It Matters |
|--------|------------|----------------|
| **MRR/ARR** | Monthly/Annual Recurring Revenue | Core business health |
| **Expansion Revenue** | Revenue from existing customers | Growth without acquisition cost |
| **Contraction** | Revenue lost from downgrades | Early warning signal |
| **Churn** | Revenue lost from cancellations | Ultimate health metric |

### Account Metrics (B2B-Specific)
| Metric | Definition | Use Case |
|--------|------------|----------|
| **Account Health Score** | Composite of usage + support + payment | At-risk identification |
| **Champion Identification** | Key user engagement level | Relationship strength |
| **Seat Utilization** | % of purchased seats used | Expansion/contraction signal |

---

## Reference Files

- **`analysis-patterns.md`**: Detailed analysis methodologies (cohort, funnel, retention, A/B test)
- **`tool-patterns.md`**: Tool-specific patterns (Pendo CLI, SQL, spreadsheets)
- **`templates.md`**: B2B-specific templates (account health, retention analysis, executive summaries)

---

## Common Pitfalls

| Pitfall | Problem | Fix |
|---------|---------|-----|
| **Vanity metrics** | Total signups don't indicate health | Focus on active, retained users |
| **Correlation ≠ causation** | Two things move together | Look for controlled experiments |
| **Small sample size** | B2B often has small N | Use statistical significance tests |
| **Activity ≠ value** | Users clicking doesn't mean succeeding | Track outcome metrics |
| **User vs account** | Individual user data misleads | Always aggregate to account level |

---

## Deep Dive Mode: When Statistical Rigor Matters

Use **Deep Dive Mode** when:
- Statistical significance matters (A/B tests, experiments, executive reviews)
- Sample size is small (common in B2B, N < 100 accounts)
- Executive requires confidence intervals
- Building reproducible analysis for ongoing use
- Making high-stakes decisions (pricing, product changes, strategic bets)

**Deep Dive adds to standard analysis:**
- Statistical testing (p-values, effect sizes, confidence intervals)
- Sensitivity analysis (what if assumptions change?)
- Reproducible documentation (queries, parameters, data provenance)
- Data quality assessment with explicit limitations

To activate Deep Dive, start your request with: "Deep dive analysis on..." or "Statistical analysis of..."

---

## Quick Reference

### Standard Analysis Checklist
- [ ] Question clearly defined
- [ ] Right metric selected
- [ ] Comparison/segment chosen
- [ ] Account-level view (for B2B)
- [ ] Insight translated to action
- [ ] Audience-appropriate format

### Deep Dive Checklist (add for rigor)
- [ ] Sample size adequate (N ≥ 30 for statistical tests)
- [ ] Statistical significance tested (p-value reported)
- [ ] Effect size calculated (practical significance)
- [ ] Confidence intervals provided
- [ ] Sensitivity analysis performed
- [ ] Data quality flags documented
- [ ] Analysis reproducible (query/code saved)

### Tool Quick Commands

**Pendo CLI** (see `tool-patterns.md` for details):
```bash
# WAU for last 7 days
python -m pendo_cli query wau --last-days 7

# Account activity
python -m pendo_cli query accounts --last-days 30
```

**SQL Pattern** (see `tool-patterns.md` for details):
```sql
-- Cohort retention query template
SELECT
  cohort_week,
  COUNT(DISTINCT user_id) as cohort_size,
  SUM(CASE WHEN activity_date >= cohort_date + INTERVAL '7 days' THEN 1 ELSE 0 END) as retained_d7
FROM user_activity
GROUP BY cohort_week
```

---

## Integration with Workspace

- Use **`metrics-frameworks`** skill for metric selection (North Star, AARRR)
- Reference **`.claude/commands/pendo.md`** for Pendo CLI commands
- Follow **`learned-patterns.md`** for documentation conventions

## Self-Learning

Before responding, read `LEARNED.md` in this skill directory when it exists and treat it as compact runtime guidance that sharpens this skill.

Rules for self-improvement:
- Keep `SKILL.md` human-owned; do not rewrite it directly from normal usage.
- Propose broader instruction changes through the central skill-learning review queue.
- Only promote specific, reusable, evidence-backed lessons into `LEARNED.md`.
