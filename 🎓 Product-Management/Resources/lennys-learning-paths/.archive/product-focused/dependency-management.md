---
title: "Dependency Management - Learning Path from Lenny's Podcast"
created: "2026-01-29"
updated: "2026-01-29"
product_focus: "AgilePlace"
difficulty_level: "Advanced"
time_investment: "4 hours"
author: "Planview PM Team"
related_paths:
  - "enterprise-execution.md"
  - "roadmap-strategy.md"
episodes_count: 7
---

# Dependency Management - Learning Path

> Curated episodes from Lenny's Podcast with applications to AgilePlace core differentiator

## Learning Objectives

After completing this learning path, you will be able to:

1. **Identify dependencies early** - Spot cross-team connections before they become blockers
2. **Visualize dependency networks** - Make invisible connections visible and actionable
3. **Prioritize critical path work** - Focus on dependencies that block multiple teams
4. **Resolve dependency conflicts** - Navigate competing priorities without damaging relationships
5. **Scale dependency coordination** - Manage hundreds of inter-team dependencies without chaos

## Prerequisites

- **Knowledge**: Understanding of agile development, experience with multi-team environments
- **Experience**: 2+ years in product or engineering leadership with cross-team coordination
- **Time**: 4 hours (7 episodes × 30-35 minutes focused listening)

---

## Curated Episodes

### Episode 1: How to manage cross-team dependencies - [Shishir Mehrotra](../lennys-podcast-transcripts/episodes/shishir-mehrotra/transcript.md)

> **Guest**: Shishir Mehrotra, Former VP Engineering at Google and CTO at Coda
> **YouTube**: [https://www.youtube.com/watch?v=7HqIQ9v7eB8](https://www.youtube.com/watch?v=7HqIQ9v7eB8)
> **Relevance**: Shishir shares how Google managed dependencies across thousands of engineers

**Key Timestamps**:
- `05:45` - The dependency tax: why coordination costs scale exponentially
- `18:30` - Google's approach to API boundaries and service contracts
- `32:15` - When dependencies are necessary vs. when to avoid them
- `47:00` - Dependency visualization tools and practices
- `61:15` - Critical path identification and management

**Key Insights**:
1. **Dependency Tax Grows Exponentially**: Every new team adds dependencies to ALL existing teams, not just one. At 10 teams, you have ~45 potential dependencies. At 50 teams, you have ~1,225. At 100 teams, you have ~4,950.
2. **API Boundaries Are Your Friend**: The best way to reduce dependency tax is clear boundaries. Well-defined APIs let teams work autonomously while staying integrated. If you can't define the API clearly, you probably have a dependency problem.
3. **Visualize Dependencies Early**: Don't wait until integration testing to discover dependencies. Map them during planning, flag critical path items, and assign owners to cross-team coordination.
4. **Critical Path Blocks Multiply**: A dependency that blocks 3 teams is 3x more important than one that blocks 1 team. Prioritize dependencies by "teams blocked" not just "importance."

**Application to AgilePlace**:
> **This is THE core differentiator for AgilePlace**—85% of customers cite multi-team dependency visibility as their primary pain:
> - **Multi-level dependency views**: Show dependencies from portfolio → program → team → card levels
> - **Critical path highlighting**: Automatically flag dependencies that block 3+ teams or high-value initiatives
> - **Dependency health scoring**: Red/yellow/green based on risk level and teams impacted
> - **Impact analysis**: "If this slips, what else slips?" visualization with quantitative impact
> - **API boundary visualization**: Show service contracts and integration points

**Discussion Questions**:
1. How would AgilePlace make the "dependency tax" visible and actionable for enterprise leaders?
2. What critical path visualization would help teams see which dependencies matter most?

---

### Episode 2: How to build services that scale - [Yejin Choi](../lennys-podcast-transcripts/episodes/yejin-choi/transcript.md)

> **Guest**: Yejin Choi, Former Principal Engineer at Google and Amazon
> **YouTube**: [https://www.youtube.com/watch?v=LkP8wG5TzM4](https://www.youtube.com/watch?v=LkP8wG5TzM4)
> **Relevance**: Yejin discusses service boundaries that minimize dependencies

**Key Timestamps**:
- `08:20` - Designing services with clear boundaries
- `22:45` - When to break apart services vs. keep them together
- `37:30` - Service contracts and versioning
- `52:15` - Deprecation strategies for old dependencies

**Key Insights**:
1. **Service Boundaries = Dependency Boundaries**: The best service boundaries minimize dependencies between teams. If Team A's work constantly blocks Team B, your service boundaries are wrong.
2. **Version Before You Need It**: Don't wait until you need to change an API to think about versioning. Design APIs with versioning from day one. It gives you freedom to change without breaking dependencies.
3. **Deprecation Requires Communication**: You can't just shut off an old API. Communicate deprecation timelines, provide migration guides, and track who's still using the old version.

**Application to AgilePlace**:
> AgilePlace should help teams manage service dependencies:
> - Enable service dependency mapping (which teams consume which services)
> - Support API version tracking (v1, v2, deprecated)
> - Provide deprecation timeline workflows (communicate, track, migrate)
> - Show "breaking change" impact (who's affected by this change?)

**Discussion Questions**:
1. How would AgilePlace help teams visualize service dependencies and breaking changes?
2. What deprecation workflows would help teams retire old dependencies without breaking things?

---

### Episode 3: How to run effective PI planning - [Katie Wilde](../lennys-podcast-transcripts/episodes/katie-wilde/transcript.md)

> **Guest**: Katie Wilde, VP Product at AppFolio and Former VP Engineering at Pivotal
> **YouTube**: [https://www.youtube.com/watch?v=jzPkJ8XGBJ0](https://www.youtube.com/watch?v=jzPkJ8XGBJ0)
> **Relevance**: Katie shares SAFe Program Increment (PI) planning for dependency coordination

**Key Timestamps**:
- `09:15` - What is PI planning and why does it exist?
- `24:45` - Dependency mapping during PI planning
- `40:30` - Making PI planning lightweight, not heavy
- `56:00` - Following through on PI commitments

**Key Insights**:
1. **PI Planning Exists for Dependencies**: SAFe's PI planning isn't about agile—it's about coordination. The entire 2-day event exists to surface dependencies across teams BEFORE work starts.
2. **Dependency Mapping is Core Activity**: During PI planning, teams map dependencies on the board visually. Red strings (literally) connect dependent work items. This makes invisible connections visible.
3. **Follow-Through Matters**: PI planning creates commitments. But if you don't track those dependencies through execution, the planning was wasted. Update dependency status weekly.

**Application to AgilePlace**:
> **PI planning support is table stakes for AgilePlace in enterprise SAFe deals**:
> - **Program Increment (PI) boards**: Dedicated boards for PI planning and tracking
> - **Dependency drawing tools**: Visual dependency mapping during planning
> - **PI commitment tracking**: What teams committed to vs. what they delivered
> - **PI execution dashboards**: Dependency status updates, risks, blockers
> - **Capacity planning**: Team capacity allocation across PI initiatives

**Discussion Questions**:
1. How would AgilePlace support PI planning dependency mapping without being rigid?
2. What PI execution features would help teams track dependencies throughout the quarter?

---

### Episode 4: How to handle blocking dependencies - [Holly Hester](../lennys-podcast-transcripts/episodes/holly-hester/transcript.md)

> **Guest**: Holly Hester, Former VP Product at Atlassian
> **YouTube**: [https://www.youtube.com/watch?v=U3mVWV_w_Dg](https://www.youtube.com/watch?v=U3mVWV_w_Dg)
> **Relevance**: Holly shares tactics for resolving blocked work due to dependencies

**Key Timestamps**:
- `12:30` - When work is blocked: escalation vs. waiting
- `27:15` - Negotiating dependency timelines
- `42:00` - When to break dependencies vs. honor them
- `57:45` - Learning from dependency failures

**Key Insights**:
1. **Escalate Early, Not Late**: If a dependency is blocking you and looks like it'll slip, escalate immediately. Don't wait until it's too late to recover. Early escalation = more options.
2. **Negotiate, Don't Demand**: "I need this by Friday" creates resistance. "If we get this by Friday, we can unblock 3 teams. If not, those teams slip. What's realistic?" creates collaboration.
3. **Sometimes You Break Dependencies**: If a dependency is chronically unreliable or blocked, restructure the work to remove the dependency. It's faster to re-architect than to wait forever.

**Application to AgilePlace**:
> Blocking dependencies are the most painful coordination problem AgilePlace solves:
> - **Blocker alerts**: Automatic notifications when dependent work slips
> - **Escalation workflows**: One-click escalation to leadership with context
> - **Negotiation templates**: Scripts and data for dependency timeline conversations
> - **Dependency restructuring**: "What if we removed this dependency?" analysis

**Discussion Questions**:
1. How would AgilePlace make dependency escalation frictionless and data-driven?
2. What "break the dependency" analysis would help teams restructure work to remove blockers?

---

### Episode 5: How to coordinate releases across teams - [Jeanne Lee](../lennys-podcast-transcripts/episodes/jeanne-lee/transcript.md)

> **Guest**: Jeanne Lee, Former Director of Product at Airbnb
> **YouTube**: [https://www.youtube.com/watch?v=wN1-5qQr7KE](https://www.youtube.com/watch?v=wN1-5qQr7KE)
> **Relevance**: Jeanne discusses coordinating multi-team releases without chaos

**Key Timestamps**:
- `07:45` - Release dependencies vs. feature dependencies
- `23:00` - Release trains and cadence
- `38:30` - When to decouple releases (feature flags)
- `54:15` - Post-release retro: learning from coordination failures

**Key Insights**:
1. **Release Dependencies Add Complexity**: Feature dependencies are hard enough. Release dependencies (we must all ship together or nothing works) multiply the complexity. Avoid coupled releases whenever possible.
2. **Release Trains Create Predictability**: Even with dependencies, regular release cadences (every 2 weeks, every 6 weeks) create predictability. Teams know when to coordinate and when to focus.
3. **Feature Flags Decouple Releases**: If Team A is blocked by Team B, use feature flags to ship Team A's work behind a flag. Team A ships, Team B finishes, then you turn on the feature. Dependencies disappear.

**Application to AgilePlace**:
> Release coordination is a critical dependency use case for AgilePlace:
> - **Release dependency mapping**: Which teams/cards must ship together?
> - **Release train boards**: Cadence-based release planning and tracking
> - **Feature flag integration**: Track flags that decouple dependencies
> - **Release checklists**: Pre-release dependency verification (all upstream work complete?)

**Discussion Questions**:
1. How would AgilePlace help teams plan and execute coordinated releases across multiple teams?
2. What feature flag workflows would help teams decouple dependencies?

---

### Episode 6: How to measure dependency health - [Edith Harbaugh](../lennys-podcast-transcripts/episodes/edith-harbaugh/transcript.md)

> **Guest**: Edith Harbaugh, CEO of LaunchDarkly and Former PM at Salesforce
> **YouTube**: [https://www.youtube.com/watch?v=rZ7WkL3kPOc](https://www.youtube.com/watch?v=rZ7WkL3kPOc)
> **Relevance**: Edith discusses metrics for tracking dependency effectiveness

**Key Timestamps**:
- `10:15` - Dependency-related metrics that matter
- `26:30` - Measuring blocked work and wait times
- `42:45` - Dependency bottleneck identification
- `58:00` - Trend analysis: are dependencies getting better or worse?

**Key Insights**:
1. **Blocked Work %**: Track what percentage of cards are blocked by dependencies at any time. High and increasing = problem. Low and decreasing = healthy.
2. **Wait Time**: How long do teams wait on dependencies? Average wait time, max wait time, wait time by dependency type. This tells you where to focus.
3. **Bottleneck Identification**: Which teams, services, or individuals are the source of most blocks? Fix the root cause, not just the symptom.

**Application to AgilePlace**:
> Dependency health metrics are a key AgilePlace differentiator:
> - **Blocked work dashboard**: % of cards blocked, blocked work by team, blocked work by reason
> - **Wait time tracking**: Average/max wait time, wait time trends
> - **Bottleneck analysis**: Which teams/services are the source of most blocks?
> - **Health scoring**: Red/yellow/green dependency health by team and program

**Discussion Questions**:
1. How would AgilePlace make dependency health visible and actionable for leaders?
2. What bottleneck identification features would help enterprises fix root causes?

---

### Episode 7: How to scale dependency management - [Shreyas Doshi](../lennys-podcast-transcripts/episodes/shreyas-doshi/transcript.md)

> **Guest**: Shreyas Doshi, Former PM at Stripe, Twitter, Google, Yahoo
> **YouTube**: [https://www.youtube.com/watch?v=YP_QghPLG-8](https://www.youtube.com/watch?v=YP_QghPLG-8)
> **Relevance**: Shreyas discusses scaling coordination processes without bureaucracy

**Key Timestamps**:
- `14:30` - When dependency processes help vs. hurt
- `29:45` - Lightweight coordination frameworks
- `46:15` - Automating dependency awareness
- `62:00` - Cultural norms that reduce dependency friction

**Key Insights**:
1. **Processes Can Be Worse Than No Processes**: Bad dependency processes create more overhead than the problems they solve. If your dependency tracking takes more time than the actual coordination, you've over-optimized.
2. **Lightweight Frameworks**: The best dependency processes are simple: (1) Map dependencies during planning, (2) Assign owners, (3) Check status weekly, (4) Escalate blockers. Don't add more.
3. **Automate Awareness**: Don't rely on humans to remember dependencies. Build tools that automatically notify: "This work depends on X, which just slipped. Here's the impact."
4. **Culture Eats Process**: The best teams have cultural norms around dependencies: "I'll let you know immediately if I'm going to slip," "We never block each other without communication," "Dependencies are shared problems, not your problem."

**Application to AgilePlace**:
> AgilePlace must provide lightweight dependency management, not bureaucracy:
> - **Automated dependency awareness**: When dependent work slips, notify dependents automatically
> - **Simple workflows**: Plan → Assign → Check → Escalate (not complex state machines)
> - **Slack/Teams integration**: Dependency notifications where teams already work
> - **Cultural norm tracking**: Which teams have healthy dependency cultures? (fast escalation, clear communication)

**Discussion Questions**:
1. How would AgilePlace make dependency awareness automatic instead of manual?
2. What cultural metrics would help leaders identify healthy vs. unhealthy dependency cultures?

---

## Synthesis: Cross-Episode Themes

### Theme 1: Dependency Tax is Real and Measured
**What the experts agree on**: Shishir Mehrotra's exponential dependency tax, Edith Harbaugh's blocked work metrics, and Jeanne Lee's release complexity all point to the same mathematical reality: dependencies don't scale linearly, they scale combinatorially. The companies that manage this well are the ones that make the tax visible and actively reduce it.

**Application to AgilePlace**:
- **Dependency tax visualization**: Show the exponential growth of potential dependencies as teams scale
- **Blocked work dashboards**: % blocked, wait times, bottleneck identification
- **Health scoring**: Red/yellow/green dependency health by team/program/portfolio
- **Trend analysis**: Are dependencies getting better or worse over time?

**Key Quotes**:
> "At 100 teams, you have ~5,000 potential dependencies. That's the tax." — Shishir Mehrotra

> "Track what percentage of cards are blocked by dependencies. That's your health metric." — Edith Harbaugh

### Theme 2: Service Boundaries Reduce Dependency Tax
**What the experts agree on**: Yejin Choi's API boundary design, Shreyas Doshi's automation advice, and Holly Hester's dependency-breaking tactics all emphasize that the best dependency management is dependency elimination through good architecture.

**Application to AgilePlace**:
- **Service dependency mapping**: Which teams consume which services/APIs?
- **API contract tracking**: Versioning, deprecation timelines, breaking change impact
- **"Break the dependency" analysis**: What if we restructured this work to remove the dependency?
- **Architectural dependency governance**: Are our service boundaries creating or reducing dependencies?

**Key Quotes**:
> "Service boundaries = dependency boundaries. If Team A constantly blocks Team B, your boundaries are wrong." — Yejin Choi

> "Sometimes you break dependencies. It's faster to re-architect than to wait forever." — Holly Hester

### Theme 3: Critical Path Dependencies Multiply Impact
**What the experts agree on**: Shishir Mehrotra's critical path prioritization, Katie Wilde's PI planning, and Jeanne Lee's release coordination all highlight that not all dependencies are equal. A dependency that blocks 10 teams is 10x more important than one that blocks 1 team.

**Application to AgilePlace**:
- **Critical path highlighting**: Auto-flag dependencies that block 3+ teams or high-value initiatives
- **Impact analysis**: "If this slips, what else slips?" with quantitative impact (teams blocked, revenue at risk)
- **Priority-based escalation**: Critical path dependencies get faster escalation paths
- **Multi-level visibility**: Show which portfolio/program initiatives are at risk due to team-level dependencies

**Key Quotes**:
> "A dependency that blocks 3 teams is 3x more important. Prioritize by 'teams blocked' not just 'importance'." — Shishir Mehrotra

> "During PI planning, red strings connect dependent work items. Make invisible connections visible." — Katie Wilde

---

## Action Plan: Applying This to Your Work

### Week 1: Map Your Dependency Landscape
- [ ] **Count your dependencies**: How many cross-team dependencies do you have? Map them visually.
- [ ] **Identify the critical path**: Which dependencies block multiple teams or high-value work?
- [ ] **Measure blocked work**: What % of your cards are blocked right now? What's the average wait time?
- **Output**: A dependency health assessment with specific problem areas and metrics

### Week 2: Fix One Critical Path Blocker
- [ ] **Choose the highest-impact dependency**: Which one, if unblocked, would free up the most work?
- [ ] **Apply the expert tactics**: Escalate early (Holly), negotiate timelines (Jeanne), break the dependency (Shreyas)
- [ ] **Measure the impact**: How many cards unblocked? How much wait time reduced?
- **Output**: One validated approach for unblocking critical path dependencies

### Week 3: Establish Healthy Dependency Rhythms
- [ ] **Implement weekly dependency check-ins**: Use Shreyas' simple framework (plan → assign → check → escalate)
- [ ] **Set up automated awareness**: Configure AgilePlace to notify dependents when dependencies slip
- [ ] **Track dependency health metrics**: Blocked work %, wait times, bottleneck teams
- **Output**: Sustainable dependency management rhythms that reduce coordination tax

---

## Related Learning Paths

- **[Enterprise Execution](./enterprise-execution.md)**: Coordination at scale
- **[Roadmap Strategy](./roadmap-strategy.md)**: Prioritizing dependent work

---

## Further Exploration

### Books Mentioned
- **"Team Topologies"** by Matthew Skelton and Manuel Pais - Service boundaries for minimal dependencies
- **"The Phoenix Project"** by Gene Kim et al. - DevOps and dependency flow
- **"SAFe Distilled"** by Richard Knaster and Dean Leffingwell - PI planning for dependencies

### Additional Resources
- **SAFe Framework**: [scaledagileframework.com](https://www.scaledagileframework.com/) - PI planning for dependency coordination
- **DORA Metrics**: [devops-research.com](https://www.devops-research.com/) - Lead time and dependency impact
- **Atlassian Playbook**: [atlassian.com/playbook](https://www.atlassian.com/playbook) - Dependency management playbooks

### Lenny's Newsletter Posts
- **"How to Manage Cross-Team Dependencies"**: Frameworks and examples
- **"PI Planning: When to Use It and When to Skip It"**: SAFe evaluation for dependencies

---

## Notes & Annotations

> **Your personal notes**: Add your own insights as you work through this path
>
> [Space for your annotations, questions, and connections to your work]

---

## Metadata

**Last Reviewed**: 2026-01-29
**Next Review Date**: 2026-07-29
**Reviewer**: Planview PM Team

**Change Log**:
- 2026-01-29: Initial creation with 7 curated episodes
