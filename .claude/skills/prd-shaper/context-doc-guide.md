# AI-Era Context Document Guide

Modern product development approach combining short context documents (2-3 pages) with working prototypes for rapid hypothesis validation. Based on principles from leading tech companies embracing AI-multiplied product development.

## When to Use Context Doc Format

Choose this format when:
- **Hypothesis needs validation** before major investment
- **Speed to customer feedback** is critical (days, not months)
- **Working prototype** will clarify requirements better than words
- **Outcome metrics matter more** than feature specifications
- **Willing to pivot** based on experiment results
- **Modern AI-era approach** to product development

**Key Philosophy**: Build to learn, not build to finish.

## Core Principles

### 1. Short Context + Working Prototype
**Traditional**: 20-page PRD → Design → Build → Test (3-6 months)

**AI-Era**: 3-page context + prototype → Validate → Iterate (2-4 weeks)

**Why**: Words fail to capture complexity. Working software teaches faster.

### 2. Hypothesis-Driven
Every feature is an **experiment**, not a commitment.

**Format**: "If we [build X], then [behavior change Y], resulting in [outcome Z]"

**Validation**: Test with 5-10% user cohort before full rollout

### 3. Outcome-Focused
**Not**: "Ship dependency visualization dashboard" (feature)

**But**: "Reduce missed critical dependencies from 30% to <5%, saving program managers 4 hours/week" (outcome)

### 4. Rapid Iteration
**Traditional**: Waterfall planning with long cycles

**AI-Era**: 2-week experiment cycles with learning loops

## Document Structure (Context Doc)

### Header

```markdown
# [Feature Name] - Context Document

**Type**: Hypothesis Validation
**Owner**: [Name/Team]
**Status**: Experiment Design / In Testing / Validated / Rejected
**Last Updated**: [Date]
```

---

### Section 1: Customer Problem

**Purpose**: Establish the job to be done with evidence.

**What to include**:
- Specific job needs to be done
- Current painful workflow (evidence-based)
- Why existing solutions fail
- Quantified impact (time, cost, errors)

**Example**:
```markdown
## Customer Problem

Enterprise program managers coordinating 50+ teams spend 4-6 hours per week
manually tracking dependencies across Jira boards. Current process:
1. Review 15+ team boards individually
2. Manually create dependency spreadsheet
3. Follow up via Slack/email to validate
4. Update spreadsheet weekly (often outdated)

**Impact**:
- 30% of critical dependencies are missed
- Causes downstream delays (avg 2 weeks per missed dependency)
- Teams lose confidence in delivery commitments

**Evidence**:
- 12 customer interviews (Enterprise accounts $500K+ ARR)
- Support ticket analysis: "dependency tracking" mentioned 45 times in Q4
- 3 customer quotes documented in appendix
```

**AI Context**: Be concrete about workflows. Show you understand their pain in detail.

---

### Section 2: Desired Customer Outcome

**Purpose**: Define the behavior change we're targeting with measurable indicators.

**What to include**:
- Specific behavior change expected
- How we'll measure it (leading & lagging indicators)
- Success threshold (not "improve" but specific target)

**Example**:
```markdown
## Desired Customer Outcome

**Behavior change**:
Program managers review auto-discovered dependencies in centralized view (30 min/week)
instead of manually tracking across 15+ boards (4-6 hours/week).

**Leading indicators** (measurable in 2-4 weeks):
- Dependency view opened by 60%+ of program managers daily
- Avg time in view: 20-30 minutes per week
- Manual dependency tracking actions decrease 70%

**Lagging indicators** (measurable in 2-3 months):
- Critical missed dependencies: 30% → <5%
- Time to identify blockers: Reactive (post-issue) → Proactive (2 weeks advance)
- Program manager confidence in delivery dates: 45% → 75%+

**Success threshold**:
At least 2 of 3 lagging indicators hit targets within 90 days.
```

**AI Context**: Outcomes must be observable and measurable. Avoid vague "satisfaction" metrics.

---

### Section 3: Hypothesis

**Purpose**: State the bet we're making explicitly and testably.

**Format**:
```markdown
## Hypothesis

**We believe that** [SOLUTION]
**will cause** [BEHAVIOR CHANGE]
**for** [USER SEGMENT]
**resulting in** [MEASURABLE OUTCOME]

**We'll know we're right when we see**:
- Specific metric 1: Threshold
- Specific metric 2: Threshold

**Key assumptions to validate**:
1. Assumption - How to test
2. Assumption - How to test
3. Assumption - How to test

**Risk factors**:
- What could make hypothesis fail
- How we'll detect early
```

**Example**:
```markdown
## Hypothesis

**We believe that** auto-discovering dependencies using team naming conventions +
Jira API analysis + ML pattern detection

**will cause** program managers to identify critical dependencies proactively
(2 weeks in advance) instead of reactively after issues surface

**for** Enterprise customers with 50-500+ teams using Jira

**resulting in** 70% reduction in missed critical dependencies and 80% reduction
in manual tracking time

**We'll know we're right when we see**:
- Dependency view DAU: 60%+ of program managers
- Critical missed dependencies: <5% (from 30%)
- Manual tracking time: <30 min/week (from 4-6 hours)

**Key assumptions to validate**:
1. Team naming conventions are consistent enough for auto-discovery
   - Test: Analyze naming patterns across 10 customer Jira instances
2. Program managers will trust auto-discovered dependencies
   - Test: Show confidence scores + manual override option
3. Jira API rate limits won't block analysis
   - Test: Load testing with realistic data volumes

**Risk factors**:
- Low trust in automation → users ignore suggestions
- Naming convention variance too high → poor accuracy
- Performance issues with large Jira instances → slow load times
```

**AI Context**: Make hypothesis falsifiable. Be explicit about what would prove it wrong.

---

### Section 4: Experimentation Plan

**Purpose**: Define how we'll test the hypothesis before full rollout.

**What to include**:
- Test cohort selection (5-10% of users)
- Duration (2-4 weeks typical)
- Success criteria for graduation
- Rollback plan if hypothesis fails

**Example**:
```markdown
## Experimentation Plan

**Phase 1: Small Cohort Test** (Weeks 1-4)

**Cohort selection**:
- 5 Enterprise customers (representative mix):
  - 2 customers: 50-100 teams
  - 2 customers: 100-300 teams
  - 1 customer: 300-500 teams
- Total: ~50 program managers
- Exclude: Trial accounts, customer-facing demos

**Duration**: 4 weeks

**Success criteria** (to graduate to Phase 2):
- **Primary**: 3+ of 5 customers report >70% time savings
- **Secondary**: Dependency detection accuracy >85%
- **Guardrail**: No degradation in Jira performance

**Data collection**:
- Daily: Usage metrics (DAU, time in view, actions taken)
- Weekly: User surveys (trust, value, issues)
- Bi-weekly: 1:1 interviews with 10 program managers

**Phase 2: Gradual Rollout** (if Phase 1 succeeds)
- Week 5-6: 10% of customers
- Week 7-8: 25% of customers
- Week 9-12: 50% → 100% if metrics hold

**Rollback plan**:
- If accuracy <70%: Rollback to manual mode within 24 hours
- If performance degrades: Throttle API calls, notify users
- If adoption <30%: Pause rollout, investigate root cause

**Root cause analysis** (if hypothesis fails):
Required investigation before moving on:
- Why didn't behavior change occur?
- Was feature discoverable? (analytics + user testing)
- Did users understand value prop? (interview 10 users)
- Were there technical issues? (log analysis)
- Was hypothesis fundamentally wrong? (revisit assumptions)

**Decision gates**:
- End of Week 2: Continue or pivot based on early signals
- End of Week 4: Graduate, iterate, or kill based on success criteria
```

**AI Context**: Be specific about cohorts, timelines, metrics. Rollback plan is not optional.

---

### Section 5: Working Prototype

**Purpose**: Show what to build through code/interaction, not just words.

**What to include**:
- Link to interactive prototype
- Key workflows demonstrated
- Technology choices
- Implementation notes

**Example**:
```markdown
## Working Prototype

**Prototype link**: [Figma prototype] or [Deployed preview environment]

**Technology**:
- Built with production design system
- React + TypeScript
- Mock data from representative customer (anonymized)

**Key workflows demonstrated**:
1. **Auto-discovery onboarding**:
   - Connect Jira → analyze naming patterns → show confidence scores
   - Allow manual pattern adjustment before activation

2. **Dependency review dashboard**:
   - Hierarchical view (team → epic → feature → task)
   - Filter by: risk level, team, time horizon
   - Confidence indicator for each dependency (High/Med/Low)

3. **Dependency validation**:
   - Click dependency → see auto-discovery reasoning
   - Approve, reject, or modify dependency
   - Feedback loop improves future detection

4. **Risk indicators**:
   - Color-coded by risk: Red (blocked), Yellow (at-risk), Green (on-track)
   - Time-based: "Dependency due in 3 days, blocking team not started"

**Implementation notes**:
- Jira API rate limit: 100 calls/min (tested with 500-team instance)
- Pattern matching: Regex + ML embeddings for team name similarity
- Caching: Daily refresh for historical data, hourly for active sprints
- Performance: <2s load time for 500-team dependency graph

**User testing plan**:
- 5 program managers test prototype over 1 week
- Tasks: Connect Jira, review dependencies, validate 10 suggestions
- Measure: Task completion time, trust ratings, issues encountered
```

**AI Context**: Prototype should be testable with real users, not just a visual mockup.

---

## Integration with AI Prototyping Tools

### Tools for Rapid Prototyping
- **Figma**: Interactive components with variables
- **v0.dev**: AI-generated React components
- **Claude Code / Cursor**: Coded prototypes with production design system
- **Replit**: Quick full-stack prototypes

### Workflow with AI Tools

**Step 1: Context Doc First** (4-8 hours)
- Write 2-3 page context document
- Define hypothesis and success criteria
- Validate with 1-2 stakeholders

**Step 2: Prototype with AI** (1-2 days)
- Use AI coding assistant to generate initial prototype
- Iterate based on key workflows from context doc
- Test with 3-5 internal users

**Step 3: Refine Context Doc** (2-4 hours)
- Update based on prototype learnings
- Add edge cases discovered
- Adjust hypothesis if needed

**Step 4: User Testing** (1 week)
- Test prototype with 5-10 target users
- Capture feedback on workflows
- Validate assumptions from hypothesis

**Step 5: Finalize Experiment Plan** (2-4 hours)
- Define cohort and success criteria
- Set up instrumentation
- Prepare rollback mechanisms

**Total time**: 2-3 weeks from idea to customer validation (vs 3-6 months traditional)

---

## Measuring Success of AI-Era Approach

### Speed Metrics
- **Time from idea to customer validation**: <30 days (target)
- **Prototype creation time**: <1 week per PM
- **Experiment cycle time**: 2-4 weeks (not 3-6 months)

### Quality Metrics
- **Hypothesis validation rate**: >40% (healthy failure rate = learning)
- **Root cause analysis completion**: 100% of failed experiments
- **Customer-reported value**: >50% of participants report improvement

### Efficiency Metrics
- **PM time on documentation**: <20% (down from 40%+)
- **PM time with customers**: >30% (up from 20%)
- **Cross-functional meetings**: -50% (prototypes eliminate confusion)

---

## Quality Checklist for Context Docs

### Customer Problem
- [ ] Specific job to be done identified
- [ ] Current workflow documented with evidence
- [ ] Impact quantified (time, cost, errors)
- [ ] Customer quotes or data included

### Desired Outcome
- [ ] Behavior change explicitly stated
- [ ] Leading indicators defined (2-4 weeks)
- [ ] Lagging indicators defined (2-3 months)
- [ ] Success thresholds are specific numbers

### Hypothesis
- [ ] Hypothesis is testable and falsifiable
- [ ] Key assumptions listed with validation methods
- [ ] Risk factors identified
- [ ] Clear criteria for "right" vs "wrong"

### Experimentation
- [ ] Test cohort specific (5-10% users)
- [ ] Duration planned (2-4 weeks)
- [ ] Success criteria clear
- [ ] Rollback plan exists
- [ ] Root cause analysis process defined

### Prototype
- [ ] Link to working prototype provided
- [ ] Key workflows demonstrated
- [ ] Can be tested with real users
- [ ] Built with production design system

---

## Common Pitfalls

### Pitfall 1: Context Doc Becomes Full PRD
Creeping back to 10-20 page specifications

**Fix**: Hard limit of 3 pages. If longer, you're over-specifying. Build prototype instead.

### Pitfall 2: Prototype Becomes Production Code
Over-engineering the prototype before validation

**Fix**: Prototype quality = "good enough to test hypothesis", not "production-ready". Ship fast, learn, then build properly.

### Pitfall 3: Skipping Root Cause Analysis
Moving to next experiment without understanding failures

**Fix**: Mandatory root cause analysis for every failed hypothesis. Document learnings.

### Pitfall 4: No Rollback Plan
Committing to full rollout regardless of results

**Fix**: Every experiment needs rollback criteria. Be willing to kill features that don't work.

### Pitfall 5: Vanity Metrics
"Increased engagement" without behavior change

**Fix**: Measure behavior change, not activity. "Users do X differently" not "users clicked Y more".

---

## Template Summary

```markdown
# [Feature Name] - Context Document

**Type**: Hypothesis Validation
**Owner**: [Name]
**Status**: Experiment Design
**Last Updated**: [Date]

## Customer Problem
[Job to be done]
[Current painful workflow]
[Why existing solutions fail]
[Impact with evidence]

## Desired Customer Outcome
[Specific behavior change]
[Leading indicators (2-4 weeks)]
[Lagging indicators (2-3 months)]
[Success threshold]

## Hypothesis
**We believe that** [solution]
**will cause** [behavior change]
**for** [user segment]
**resulting in** [outcome]

**We'll know we're right when**:
- Metric 1: Threshold
- Metric 2: Threshold

**Key assumptions**:
1. Assumption — Test method
2. Assumption — Test method

**Risk factors**: [What could make this fail]

## Experimentation Plan
**Cohort**: [5-10% users, specific selection]
**Duration**: [2-4 weeks]
**Success criteria**: [Specific thresholds]
**Rollback plan**: [If fails, what happens]
**Root cause process**: [If fails, how we investigate]

## Working Prototype
[Link to prototype]
[Key workflows demonstrated]
[Technology choices]
[User testing plan]
```

---

## Key Reminders

1. **3 pages max** - If longer, build prototype instead of writing more
2. **Hypothesis-driven** - Every feature is an experiment
3. **Outcomes over features** - Measure behavior change, not activity
4. **Rapid cycles** - 2-4 weeks per experiment, not months
5. **Learn from failures** - Root cause analysis mandatory
6. **Rollback ready** - Every experiment needs exit criteria
7. **Prototype with AI** - Use tools to build 10x faster
8. **Customer validation** - Test with 5-10 users before broader rollout