# CSM & Post-Sales JTBD + User Journey Research

*For: ServiceNow Customer Success Platform (CSP) Roadmap*
*Date: 2026-04-06*
*Purpose: Ground product problem definition and roadmap prioritization in a deep, structured model of how B2B CS functions actually work.*

---

## How to Use This Document

This is a living research artifact, not a completed study. It synthesizes:
- Public competitive review data (PlanHat, Gainsight, ChurnZero, Vitally — G2, Gartner, TrustRadius)
- ServiceNow CEG operational context (CSP context.md, PlanHat competitive analysis)
- Domain knowledge of enterprise B2B CS practices

Evidence tiers are noted inline using the same standard as the competitive analysis:
- **[Direct]** — verbatim quote, attributed
- **[Synthesis]** — pattern from aggregated review data
- **[Inference]** — analyst interpretation, presented as hypothesis

Gaps marked **[Needs Validation]** should be tested through CSM interviews, CS Slack communities, or win/loss research.

---

## Personas Overview

| Persona | Primary system | Primary metric | Seat count at 500-CSM org |
|---|---|---|---|
| CSM (High-Touch) | CS Platform + CRM | NRR, health score | ~250 |
| CSM (Tech-Touch / Digital) | CS Platform + email sequencing | NRR, product adoption | ~100 |
| Professional Services / Impl. | PSA + CS Platform | Time-to-value, CSAT | ~75 |
| CS Operations / RevOps | CS Platform + BI tools | Data quality, coverage | ~20 |
| VP Customer Success / CCO | CS Platform + exec dashboards | NRR, churn, GRR | ~5 |

---

## Persona 1: Customer Success Manager — High-Touch

**Context**: Manages 30–150 enterprise accounts. Each account is a named relationship. They are measured on net revenue retention, expansion, and health score. They spend their day triaging signals, running calls, preparing deliverables (QBRs, success plans), and coordinating internally across Renewal, Support, and PS teams.

### JTBDs

1. **When I start my day with 80 accounts to manage, I want to immediately know which ones need attention today, so I can focus my energy where it will prevent the most damage or unlock the most growth.** [Synthesis — "morning health queue" pattern inferred from review behavior; "zero tab-switching for triage" repeatedly mentioned]

2. **When a customer goes quiet or reduces usage, I want early, automatic warning before the renewal conversation, so I have enough time to intervene and course-correct.** [Direct — PlanHat reviewers, G2, TrustRadius; "renewal forecasting" as daily workflow confirmed across sources]

3. **When I prepare for a quarterly business review, I want to pull together product usage, support history, milestone progress, and ROI evidence in one place, so I can show the customer a credible value story instead of spending two days building slides.** [Synthesis — EBR prep mentioned repeatedly in review language; time waste on prep is a universal CSM complaint]

4. **When I inherit a new account or return from leave, I want to get up to speed on context and history in minutes, so I can walk into the call knowing what matters.** [Inference — account handoff failures are a documented pain point; needs direct validation]

5. **When a customer escalates, I want a structured playbook to kick in automatically, so I don't have to improvise under pressure and I can coordinate Support, PS, and leadership without chasing people.** [Synthesis — escalation management cited as critical workflow in Gainsight and Vitally review patterns]

6. **When I identify an expansion opportunity, I want to surface it to Sales with context already attached, so the handoff doesn't require me to repeat the account history on three different calls.** [Inference — CS-to-Sales handoff friction is well-documented in CS practitioner literature; needs validation here]

7. **When my portfolio grows, I want the system to tell me which accounts I haven't touched recently, so I don't accidentally ignore a high-value account because it's been quiet.** [Synthesis — "coverage gaps" and "neglected accounts" surface repeatedly in CS ops complaints]

8. **When I update a success plan, I want the customer to see it in real time and co-own it, so engagement becomes mutual accountability rather than me chasing them to respond.** [Synthesis — PlanHat portal reviews; collaborative success planning as trust-building mechanism]

### Primary Workflows

| Workflow | Frequency | Current tool(s) | Key pain |
|---|---|---|---|
| Morning health triage | Daily | CS platform health queue, spreadsheet backup | Alerts are noisy, signals lack context, requires tool-switching |
| Account prep (calls, QBRs, EBRs) | Weekly / Quarterly | Slides, CS platform, CRM, product analytics | Manual assembly from 4–5 sources; no single source of truth |
| Success plan creation + update | Monthly | CS platform, Google Docs | Plans exist but customers rarely engage with them |
| Escalation management | Ad hoc | Email, Slack, CS platform task | No structured playbook; coordination is manual and inconsistent |
| Renewal pipeline review | Monthly | CS platform, CRM | Risk flags unclear; data currency issues |
| Expansion identification | Monthly | CS platform + product analytics | Usage data often stale or missing; no clear signal threshold |
| Internal handoff to Renewal/AE | Quarterly | Email + CRM notes | Context loss is frequent; timing is reactive |
| CS-to-Support coordination | Ad hoc | Ticketing system + Slack | CSM visibility into open tickets is partial; no shared view |

### Key Use Cases

- **Health score interpretation**: CSM opens platform and the score has changed. Are the underlying signals visible? Can they drill into what changed and why? Today this often requires a separate analytics query or a conversation with CS Ops.
- **QBR deck generation**: Pulling together product adoption, milestone progress, support history, and financial summary for a 60-minute exec meeting. [Synthesis — this is universally cited as the highest time sink in CSM workflows]
- **Risk escalation playbook**: A customer hits a risk threshold. Does the system automatically create a task, notify the right people, and suggest next actions? Or does the CSM have to manually coordinate via Slack and email?
- **Expansion signal surfacing**: Product usage exceeds a threshold in a feature set the customer doesn't have licensed. Does the system surface this as an opportunity, or does it get buried?
- **Renewal prep package**: 90 days before renewal, generate a summary of value delivered, open risks, and recommended renewal messaging.

### User Journey Map — A Typical Month

**Week 1: Triage and Pulse**
- Open CS platform, review health score changes since last week
- Flag accounts that moved red or yellow
- Run 3–5 account calls, take notes
- Pain: Notes live in 3 places (CS platform, CRM, personal doc). Recalling context from last quarter's call requires digging.

**Week 2: Proactive Outreach**
- Identify accounts with low engagement (no calls, no logins, no response to emails)
- Reach out with relevant content or check-in
- Pain: No automated "dormancy trigger" — CSM has to manually filter; coverage gaps are invisible until something breaks.

**Week 3: Business Review Season**
- Prepare QBR/EBR decks for 4–6 accounts
- Pull product usage from analytics tool, support history from ticketing system, milestones from CS platform
- Pain: This takes 2–4 hours per deck. Data is often stale or requires exporting and reformatting.

**Week 4: Renewal and Expansion Review**
- Review renewal pipeline; flag accounts at risk
- Surface expansion opportunities to Sales
- Update success plans
- Pain: Renewal risk flags are often based on lagging indicators (low NPS, missed milestones) — CSM wants leading indicators earlier.

**Top frustrations, ranked by signal strength:**

1. **Fragmented data requiring manual assembly** — universally documented; product analytics, support tickets, CRM data, and CS activities live in different tools with no unified view. [Synthesis — high confidence]
2. **Health scores that don't explain themselves** — a red score without drill-down context means the CSM still has to investigate. [Synthesis — medium confidence]
3. **QBR/EBR preparation time** — 2–4 hours per deck; consistently cited as the biggest time sink. [Synthesis — high confidence]
4. **Escalation coordination overhead** — no structured playbook triggers in most CS platforms; coordination happens via Slack and email. [Inference — medium confidence; needs validation]
5. **Renewal timing misalignment** — CSMs engage at 90 days, but the risk indicators were visible at 180 days. By the time CS is involved, options are narrowed. [Synthesis — medium confidence]
6. **Customer-visible success plans have low adoption** — portals and shared plans exist in tools like PlanHat but customer engagement is uneven. [Synthesis — medium confidence]

---

## Persona 2: Customer Success Manager — Tech-Touch / Digital

**Context**: Manages 200–2,000 accounts digitally. Relationship is asynchronous — no dedicated calls except for milestone or risk moments. Relies heavily on automation, triggered sequences, and self-service content. Measured on product adoption, health score at scale, and renewal rate across the long tail.

### JTBDs

1. **When I have 500 accounts, I want the system to automatically run the standard playbooks for onboarding, QBRs, and check-ins, so I can focus my limited human time on the accounts that automation can't handle.** [Synthesis — digital CS model depends entirely on playbook automation being reliable and configurable]

2. **When a digital account shows risk signals, I want automated intervention to trigger before I would have noticed manually, so risk doesn't become churn by the time it surfaces.** [Synthesis — early warning triggers are the core value prop of every CS platform for this persona]

3. **When a new customer onboards, I want a structured sequence of automated touchpoints that guides them to first value without CSM involvement, so the onboarding experience is consistent regardless of my capacity.** [Synthesis — onboarding automation is the #1 use case cited by tech-touch CS teams]

4. **When a digital customer is ready to expand, I want an automated signal and templated outreach to go out without manual intervention, so no expansion opportunity falls through because I didn't have time to review it.** [Inference — confirmed by expansion automation features in all major CS platforms]

5. **When I look at my portfolio, I want to see which segments are healthy vs. at risk at a glance, so I can make portfolio management decisions without pulling a report every time.** [Synthesis — portfolio health views are the primary UX pattern for digital CSMs]

6. **When I want to improve my playbooks, I want to see which automations are working and which ones customers are ignoring, so I can iterate on sequences the way I would iterate on a product.** [Inference — playbook analytics are underbuilt in most CS platforms; needs validation]

### Primary Workflows

| Workflow | Frequency | Current tool(s) | Key pain |
|---|---|---|---|
| Playbook configuration and tuning | Monthly | CS platform | Complex setup; technical user required for most platforms |
| Segment health review | Weekly | CS platform | Aggregated views are coarse; drill-down requires queries |
| Automated sequence monitoring | Weekly | CS platform + email tool | Deliverability and engagement data often lives in separate system |
| Manual interventions on triggered accounts | Ad hoc | CS platform + email | No clear handoff protocol from automation to human |
| Cohort analysis (adoption by segment) | Monthly | CS platform + BI tool | Requires SQL or analyst involvement in most orgs |

### Key Use Cases

- **Onboarding automation**: A new account is provisioned. Trigger: send welcome email, schedule first adoption check-in at day 7, flag for human review at day 30 if adoption score is below threshold. Does the system do this reliably without manual configuration per account?
- **Churn risk automation**: An account drops below a usage threshold for 14 consecutive days. Trigger: automated executive-summary email, task created for CSM review, play initiated. How configurable is the trigger logic? How many conditions can be combined?
- **Expansion automation**: An account has high adoption in module A and low adoption in module B. Trigger: expansion-opportunity flag surfaced to CSM, templated outreach sent. How reliably is the product data feeding this signal?
- **Playbook performance analytics**: "Of the 200 accounts in my onboarding sequence, 60% completed step 3 but only 30% completed step 4. What is the drop-off point?" — can the CSM get this without an analyst?

### User Journey Map — A Typical Month

**Continuous (Automated)**:
- Playbooks running for 400+ accounts across onboarding, milestone check-ins, renewal triggers
- Health scores updating daily
- Alerts firing for accounts crossing thresholds

**Week 1: Portfolio Review**
- Review aggregated health by segment and cohort
- Identify accounts automation flagged for human intervention
- Pain: The list of "needs human attention" is often too long (low precision alerts) or too short (missed genuine risk). Threshold tuning is trial-and-error.

**Week 2: Playbook Maintenance**
- Review which sequences are completing vs. stalling
- Adjust email content and timing based on engagement data
- Pain: Sequence analytics are often in the email system, not the CS platform — requires context-switching to understand what's working.

**Week 3: Manual Outreach on Risk Accounts**
- Work through the escalation queue from automation flags
- Prioritize by risk tier and ARR
- Pain: At 500 accounts, even 5% risk rate = 25 active interventions simultaneously. Prioritization tools are often underpowered.

**Week 4: Reporting and Cohort Analysis**
- Pull adoption and health metrics by segment for leadership review
- Identify cohorts for targeted campaigns or feature drives
- Pain: This often requires CS Ops involvement because the platform doesn't have sufficient self-serve analytics.

**Top frustrations:**

1. **Playbook setup complexity** — configuring triggered sequences requires technical knowledge most CSMs don't have; reliance on CS Ops or platform admin. [Direct — PlanHat reviews: "like learning to program"]
2. **Alert noise** — too many false-positive alerts degrade trust in the system; CSMs start ignoring them. [Inference — high likelihood; needs validation with actual signal/noise ratio data]
3. **Product usage data currency** — the "low adoption" trigger fires on stale data because the product event pipeline has a 24–48 hour lag. [Synthesis — cited across CS platform reviews]
4. **No playbook A/B testing** — CSMs can't test which sequence performs better without manually splitting lists. [Inference — needs validation]
5. **Lack of cross-functional visibility into digital accounts** — when a support ticket or escalation happens on a digital account, CS is often the last to know. [Synthesis — medium confidence]

---

## Persona 3: Professional Services / Implementation

**Context**: Responsible for onboarding new customers from contract signature through "go-live" and initial value realization. Works across 5–20 active projects simultaneously. Measured on time-to-go-live, project CSAT, and milestones achieved. Interfaces with Sales (handoff), CSM (transition), and customer-side project leads.

### JTBDs

1. **When I take ownership of a new account at contract close, I want to receive a complete, structured handoff from Sales including use case context, stakeholder map, and agreed success criteria, so I don't spend the first two weeks re-discovering what was sold.** [Synthesis — Sales-to-PS handoff failures are the most consistently cited source of early customer frustration across B2B SaaS]

2. **When I'm running 12 implementations simultaneously, I want to see the status of every project at a glance without opening each one, so I can identify which ones are at risk before they miss their milestones.** [Inference — PSA and project management patterns; needs CS-platform-specific validation]

3. **When a customer hits a blocker during implementation, I want to log it, trigger an escalation path, and get internal resources engaged without losing the thread in email, so blockers get resolved within the SLA and don't cascade into delays.** [Synthesis — implementation blocker management is a documented pain in enterprise PS orgs]

4. **When I close an implementation, I want to hand the account to the CSM with full context — milestones, open items, key stakeholder relationships, adoption baseline — in one structured package, so the CSM doesn't start from zero.** [Synthesis — PS-to-CSM handoff quality directly impacts early adoption and first-year retention]

5. **When I want to improve our implementation methodology, I want to see which milestones consistently slip and why, so I can update the playbook proactively instead of reacting to each incident.** [Inference — methodology analytics are underused in most PS orgs; needs validation]

6. **When a customer asks me how their implementation compares to similar companies, I want benchmark data on time-to-go-live and adoption milestones, so I can set credible expectations and build trust.** [Inference — plausible; customer benchmarking in implementation context is valuable but rarely available]

### Primary Workflows

| Workflow | Frequency | Current tool(s) | Key pain |
|---|---|---|---|
| Project kickoff (post-Sales handoff) | Per engagement | CRM + project tool + email | Handoff quality inconsistent; missing context from Sales |
| Milestone tracking | Weekly | PSA / project tool + CS platform | Often lives in separate system from CS health data |
| Customer communication and status updates | Weekly | Email + project portal | Status updates are manual; customer visibility is limited |
| Risk and blocker management | Ad hoc | Email, Slack, project tool | No structured escalation path; coordination is reactive |
| PS-to-CSM handoff at go-live | Per engagement | Email + CRM + handoff doc | Context loss; CSM often re-interviews customer |
| Methodology retrospective | Quarterly | Manual analysis | No system-generated milestone analytics; ad hoc |

### Key Use Cases

- **Structured kickoff checklist**: Triggered automatically at contract close; populates stakeholder fields from CRM, imports agreed success criteria from the sales process, generates the standard project plan. How much of this is manual today?
- **Milestone dashboard**: PM can see all 12 active implementations, current milestone, days-ahead/behind, and next action in one view. Does the CS platform support this natively, or does PS use a separate PSA?
- **Escalation playbook**: Customer's IT team is unavailable for 3 weeks, blocking go-live. How does PS log this, notify CSM and leadership, and track resolution without it living in email?
- **PS-to-CSM handoff package**: At go-live, auto-generate a transition document: milestones achieved, open items, adoption baseline, key contacts, agreed next steps. Does the CS platform produce this, or is it manual?

### User Journey Map — A Typical Implementation (12 Weeks)

**Weeks 1–2: Discovery and Kickoff**
- Receive handoff from Sales; chase missing context
- Run kickoff call; establish project plan and stakeholder alignment
- Pain: Handoff quality from Sales varies widely. Context about why the customer bought, what was promised, and what success looks like is often incomplete or verbal.

**Weeks 3–6: Build and Configure**
- Execute technical implementation tasks
- Weekly status calls with customer project lead
- Pain: Changes in customer scope or personnel are hard to track systematically. Risk flags live in the PM's head or in email threads.

**Weeks 7–10: Testing and Adoption**
- User acceptance testing, training
- Address blockers; escalate to internal teams as needed
- Pain: Visibility into adoption baseline at this stage is limited. PS rarely has access to product telemetry during implementation.

**Weeks 11–12: Go-Live and Handoff to CS**
- Final sign-off; go-live execution
- Transition to CSM
- Pain: Handoff package is created manually (slide deck or email summary). CSM may not be aligned. Customer often has to re-explain their context to a new person.

**Top frustrations:**

1. **Sales-to-PS handoff quality** — most consistently cited source of friction; missing use case context, no agreed success criteria, verbal promises not documented. [Synthesis — high confidence]
2. **No system-of-record for implementation risk** — risk lives in email and PM judgment; no structured escalation path. [Inference — high likelihood; needs platform validation]
3. **PS-to-CSM handoff creates customer re-discovery work** — CSMs and customers repeat the same onboarding conversations. [Synthesis — medium confidence]
4. **Milestone analytics are not available for methodology improvement** — PS organizations lack data on which steps consistently slip and why. [Inference — medium confidence]
5. **Limited customer visibility during implementation** — customers can't self-serve on project status; every status inquiry requires a sync. [Synthesis — PlanHat portal adoption pattern applies here]

---

## Persona 4: CS Operations / RevOps

**Context**: Owns the CS platform infrastructure, data model, health scoring logic, playbook configuration, and reporting. Usually 1–5 people supporting 50–200 CSMs. The invisible persona — everything the CSM does well depends on CS Ops having set it up correctly. Measured on data quality, platform adoption, and the reliability of health signals.

### JTBDs

1. **When CSMs complain that health scores are wrong, I want to trace the signal back to its source, identify the data gap, and fix it, so the health model regains trust and CSMs don't build shadow spreadsheets.** [Synthesis — "health score mistrust" is a documented pattern; CSMs reverted to spreadsheets when automated scores are unreliable]

2. **When leadership asks for a custom health report by segment, vertical, or region, I want to generate it without writing SQL, so I'm not a bottleneck for every data question. [Inference — analyst bottleneck is a near-universal CS Ops pain; needs validation]

3. **When we onboard a new CS platform or update our data model, I want a test environment and a data validation workflow, so I can verify that signals are clean before CSMs see them.** [Inference — data ops maturity in CS is low across most orgs; needs validation]

4. **When playbooks need to be updated, I want to make changes without needing an engineer or platform vendor support, so we can iterate on CS processes at the same pace as the business.** [Direct — PlanHat review: "like learning to program"; configuration dependency on vendor support is a documented complaint]

5. **When I want to measure whether a playbook intervention is working, I want to compare outcomes for accounts that received the intervention versus those that didn't, so I can prove (or disprove) the playbook's value and get buy-in for process changes.** [Inference — playbook A/B testing and attribution is an underdeveloped capability across CS platforms]

6. **When renewal managers need pipeline data and CSMs need health signals, I want a single data model that serves both without maintaining two separate systems, so we don't have the same customer represented differently in different tools.** [Synthesis — data fragmentation between CS and Renewal is a recurring structural problem]

### Primary Workflows

| Workflow | Frequency | Current tool(s) | Key pain |
|---|---|---|---|
| Health scoring model maintenance | Monthly | CS platform + data pipeline | Rule changes require deep platform knowledge; limited testing tools |
| Playbook creation and configuration | Per initiative | CS platform | High complexity; technical barrier to self-service editing |
| Data pipeline management | Ongoing | ETL + CS platform | Product usage data ingestion is fragile; lag is a constant issue |
| Reporting and dashboard builds | Weekly | CS platform + BI tool | Custom reports require analyst or SQL; can't be self-served by CS leadership |
| Platform configuration and user management | Monthly | CS platform | Admin tasks are time-consuming and poorly documented |
| CS metrics definition and alignment | Quarterly | Spreadsheet + CS platform | Health metrics aren't consistently defined across regions or segments |

### Key Use Cases

- **Health score debugging**: A CSM notices that Account X has a green score but is clearly at risk. CS Ops traces the signal: product usage API is returning stale data because an ETL job failed 3 days ago. How long did it take to detect this? Is there an alert for pipeline failures?
- **Segment-aware scoring setup**: Leadership wants different health logic for Strategic (top 50), Enterprise, and Commercial segments. Can CS Ops configure three separate health models without engineering support? [Synthesis — this is the PlanHat "Health Lab" capability gap for CSP]
- **Self-service dashboard**: VP of CS wants a regional NRR dashboard by segment, by CSM cohort, by product line. Does CS Ops build this once and publish it, or does the VP ask for a custom export every quarter?
- **Playbook effectiveness measurement**: "The 90-day renewal risk playbook ran on 200 accounts last quarter. Did it improve renewal rates?" — Can CS Ops answer this without involving a data analyst?

### User Journey Map — A Typical Quarter

**Month 1: Foundation Maintenance**
- Review health scoring model accuracy (compare predicted risk to actual outcomes)
- Update signal weights based on last quarter's outcomes
- Address backlog of CSM requests ("why is this account red?")
- Pain: Signal debugging is time-consuming because data lineage is opaque. Understanding why a score changed requires tracing through multiple data sources.

**Month 2: New Initiative Configuration**
- Build playbooks for upcoming product launch or segment-specific initiative
- Test playbook triggers in staging (if staging exists)
- Publish and train CSMs
- Pain: Playbook configuration is complex enough that most CS Ops people consider platform expertise a specialized skill. Changes require significant testing time.

**Month 3: Reporting and Quarter-Close**
- Produce quarterly CS scorecard for leadership
- Pull NRR actuals, health distribution, playbook performance
- Prepare segment-level analysis for CS leadership review
- Pain: Significant manual work pulling from multiple systems. Reporting takes 2–3 days per quarter even with BI tools.

**Top frustrations:**

1. **Health model opacity** — when a score changes, tracing "why" is difficult; data lineage is not surfaced in the platform. [Synthesis — medium confidence]
2. **Playbook configuration complexity** — making changes requires deep platform expertise; ops teams can't iterate quickly. [Direct — high confidence]
3. **Data pipeline fragility** — product usage data pipelines break silently; stale data feeds wrong health signals before anyone notices. [Synthesis — medium confidence]
4. **Reporting bottleneck** — CS Ops becomes the single point of failure for every leadership data question. [Inference — high likelihood]
5. **No cross-system single data model** — CS data, renewal data, support data, and product data exist in separate systems with inconsistent customer IDs and conflicting records. [Synthesis — high confidence; documented in PlanHat and Gainsight reviews]

---

## Persona 5: VP of Customer Success / CCO

**Context**: Owns the full post-sales motion from implementation through renewal and expansion. Accountable to the board and CEO for NRR, GRR, and logo retention. Manages a team of 50–300 people. Needs strategic visibility — not individual account management — but must be able to drill into at-risk situations quickly. Measured on NRR, churn rate, expansion rate, CS team efficiency (accounts per CSM), and customer health distribution.

### JTBDs

1. **When I walk into a board meeting or QBR with my CEO, I want a single, credible view of portfolio health — by segment, region, and risk tier — so I can answer any question without a 24-hour data request.** [Synthesis — executive visibility is the stated first use case for every CS platform; reliability of the data is the actual problem]

2. **When I need to forecast renewal risk for the quarter, I want a model based on leading indicators (engagement, adoption, support burden, relationship quality), not just lagging ones (NPS, renewal date proximity), so I can course-correct while there's still time.** [Synthesis — forecasting accuracy is consistently cited as a gap across CS platforms; PlanHat Gap 7]

3. **When I'm building the case for CS headcount investment, I want data showing the correlation between CSM coverage, engagement frequency, and renewal outcomes, so I can make a ROI argument, not just a capacity argument.** [Inference — CS ROI measurement is a documented organizational challenge; needs validation]

4. **When I set up the CS team for a new fiscal year, I want segment-level health benchmarks, playbook standards, and team performance targets that the platform enforces, so I don't have to manage consistency through PowerPoint and email.** [Inference — operating model standardization in CS is underdeveloped without a strong platform]

5. **When a major account is at risk, I want to be notified automatically at the right moment — not too late, not too early — with enough context to decide whether to get personally involved, so I'm using my time on the right interventions.** [Synthesis — executive alert calibration is a recurring CS platform design problem]

6. **When I review CS team performance, I want to see activity quality, not just activity volume — did the CSM have the right conversation, not just how many calls they made.** [Inference — activity quality measurement is emerging in AI-enabled CS tools like Cust]

7. **When I report to the CRO or CFO, I want to show the correlation between CS investment and revenue outcomes in terms they understand, so CS is seen as a revenue driver, not a cost center.** [Direct — this framing is the defining strategic goal of most CS leadership; universally documented]

### Primary Workflows

| Workflow | Frequency | Current tool(s) | Key pain |
|---|---|---|---|
| Executive portfolio review | Weekly | CS platform + BI dashboard | Reliability of data; often requires CS Ops to validate before the meeting |
| Renewal forecast | Monthly | CS platform + CRM + spreadsheet | Multiple competing forecasts; no single authoritative number |
| CS team performance review | Monthly | CS platform + HRIS | Activity data is volume-focused; quality indicators are absent |
| CS budget and headcount planning | Quarterly/Annual | Spreadsheet + CRM | ROI data for CS investment is not available in most platforms |
| Risk escalation (major accounts) | Ad hoc | CS platform + Slack + email | Alert timing and context quality is inconsistent |
| Board and executive reporting | Monthly/Quarterly | Slide deck manually built | 2–3 days of work per deck; data often stale by presentation |

### Key Use Cases

- **Segment-level health dashboard**: VP wants to see health distribution (% green/yellow/red) broken out by Strategic, Enterprise, Commercial, and Digital segments — and drill into any cohort within 2 clicks. Is this available out-of-box, or does it require a CS Ops build?
- **Renewal risk forecast**: 90 days before quarter close, VP needs a forecast of renewal ARR at risk. Does the platform produce this automatically from health signals, or is it assembled from multiple sources?
- **CSM performance benchmarking**: "Which CSMs have the highest adoption and expansion rates in their book of business?" — Can the VP answer this without running a manual analysis?
- **Executive escalation briefing**: A $2M account drops to red. The VP needs a one-page brief with account history, relationship map, open tickets, financial exposure, and recommended action before their call with the customer's C-suite. Does the CS platform generate this?

### User Journey Map — A Typical Quarter

**Month 1 (Quarter Start): Planning and Reset**
- Review prior quarter performance — where did we miss? Where did we win?
- Set segment-level health targets and renewal forecast
- Review CSM book assignments for portfolio balance
- Pain: Prior quarter analysis requires significant manual work; platform reports are often not detailed enough to understand root cause of churn or expansion patterns.

**Month 2: Execution Review**
- Mid-quarter check: Is the health distribution moving in the right direction?
- Review risk escalation queue; intervene on top accounts
- Review team performance metrics
- Pain: Mid-quarter course corrections are hard because leading indicators are unclear. Most data shows what happened, not what will happen.

**Month 3: Renewal Close and Reporting**
- Work through at-risk renewals; involve executives on key accounts
- Compile quarterly CS report for CRO/CFO/board
- Pain: Board reporting still requires 2–3 days of manual slide construction; data is often assembled by CS Ops and then re-formatted by the VP's team.

**Top frustrations:**

1. **Renewal forecasting unreliability** — "nearly impossible" language in PlanHat reviews; forecasts driven by lagging indicators. [Synthesis — medium confidence; validated across multiple CS platforms]
2. **Board reporting manual effort** — executive reporting is not productized; significant manual work to produce quarterly slides. [Synthesis — high confidence]
3. **No leading indicator model** — platforms score current health but do not predict future state with confidence; CSPs would need a proprietary model trained on outcomes data. [Inference — high-leverage product opportunity for platforms with enough account history]
4. **CS ROI is unmeasurable in the platform** — VP cannot produce an ROI report correlating CS investment (coverage, engagement, QBR frequency) with renewal outcomes from the platform alone. [Inference — high confidence based on absence of this feature across CS platforms]
5. **Alert calibration failure** — too many low-quality alerts trains executives to ignore them; too few means escalations happen reactively. [Synthesis — medium confidence]

---

## Cross-Cutting Themes

These themes cut across all personas and represent the highest-leverage problem areas for a CS platform roadmap.

### 1. Manual Work Dominates Where Data Is Fragmented

The most consistent pattern across all personas is manual assembly of information from multiple systems. The CSM assembles QBR decks from 4–5 tools. The PS lead manually creates the handoff package. The VP spends 2–3 days building board slides. CS Ops runs SQL to answer routine questions.

**Root cause**: CS activities, product usage, support tickets, CRM data, and contract data live in separate systems. No CS platform has solved the ingestion and unification problem at the enterprise level. The winner who solves it — or who already has the data unified (see: ServiceNow) — gets to remove this friction.

**What CSMs say**: [Synthesis] "It's all kind of integrated into one place rather than scattered across communication channels" — this is *aspirational* language, not a description of current reality. It is what buyers hope the platform will deliver.

### 2. Data Fragmentation and Siloing

| Data type | Where it lives | Why it matters for CS |
|---|---|---|
| Product usage/adoption | Product analytics (Amplitude, Mixpanel, Pendo, or custom) | Core health signal; often has 24–48h lag |
| Support history | Ticketing system (Zendesk, Jira, ServiceNow) | Risk indicator; CSMs often have limited visibility |
| Contract and billing data | CRM (Salesforce) + billing system | Renewal risk, ARR exposure |
| Relationship quality | CS platform (call notes, NPS, EBR history) | Hardest to quantify; often the most predictive |
| Engagement data | Email, CS platform, customer portal | Leading indicator of health direction |
| ITSM/operational data | ServiceNow (unique to SNOW accounts) | Change requests, incident frequency, SLA breaches |

For ServiceNow CSP specifically: the ITSM + contract + support data is already in the platform. This eliminates the most painful integration work. The product advantage is real — but only if CSP surfaces these signals in CS-relevant workflows.

### 3. Visibility Gaps

| Visibility gap | Who feels it | Severity |
|---|---|---|
| Account health direction (is it improving or declining?) | CSM, VP | High |
| Renewal risk 180 days out | VP, Renewal | High |
| Adoption by feature and user segment | CSM, CS Ops | High |
| Which accounts haven't been touched | CSM, CS Ops | Medium |
| What Support is working on for my accounts | CSM | Medium |
| What Sales promised in the deal | PS, CSM | High |
| How our CSM coverage affects renewal outcomes | VP, CFO | High |

### 4. Handoff Failures — The Three Critical Transitions

**Transition 1: Sales → Professional Services**
- What breaks: use case context, promised features, stakeholder relationships, agreed success criteria
- Impact: First 30 days feel like rework; customer loses confidence early
- What good looks like: Structured handoff object in the CS platform with required fields, populated from CRM opportunity, flagged as incomplete until PS acknowledges
- [Synthesis — high confidence; most consistently cited source of customer frustration in early post-sale]

**Transition 2: Professional Services → Customer Success**
- What breaks: implementation decisions, open items, adoption baseline, relationship context
- Impact: CSM re-discovers the account; customer has to repeat themselves
- What good looks like: Auto-generated transition brief at go-live; PS-originated context persists in the CSM's account record
- [Synthesis — medium confidence; well-documented in CS practitioner communities]

**Transition 3: Customer Success → Renewal**
- What breaks: health context, expansion opportunities, relationship risk, deal history
- Impact: Renewal conversation starts without the strategic context the CSM has built; risk of misaligned renewal conversation
- What good looks like: CS health score, relationship map, and expansion notes are visible to Renewal without requiring a separate CSM briefing
- [Synthesis — medium confidence; documented in CS-to-Sales collaboration patterns]

### 5. Reporting and Proving Value

This is a universal pain across all personas, but the specific version differs:

- **CSM**: proves value to the *customer* (QBR/EBR readiness, success plan evidence)
- **CS Ops**: proves value of *CS programs* (playbook attribution, coverage model effectiveness)
- **VP CS**: proves value of *CS investment* to CRO/CFO/board

None of these are well-served by current CS platforms. The "prove value" problem is ultimately a data problem (what data do you need?) and a presentation problem (how do you tell the story?). The platform that automates both gets embedded in the highest-stakes conversations the CS team has.

**For ServiceNow CSP specifically**: the "40% churn risk mitigated" stat from the Now on Now case study is exactly this proof point. The product can generate this stat for its own users. That is the QBR and board slide of the future for every CEG CS leader.

---

## Implications for ServiceNow CSP Roadmap

*These implications are derived from the JTBD and journey research above. They are not ranked — use the competitive analysis and discovery work to prioritize.*

### High-Signal Problem Areas (multiple personas feel this)

1. **Unified account view (across CS, Support, ITSM, and contract data)** — ServiceNow has a structural data advantage here. The problem to solve is surfacing these signals in CS-relevant workflows, not integration.

2. **QBR/EBR preparation automation** — highest time-sink for CSMs; addressed by combining product usage, support history, milestone tracking, and financial summary in one shareable artifact.

3. **Segment-aware health scoring with leading indicators** — the standard is Health Lab (PlanHat); the differentiated version uses ITSM operational signals no standalone CSP can match.

4. **Structured handoff objects at transition points** — Sales→PS, PS→CSM, CSM→Renewal. Three transitions, each with documented failure modes. A structured handoff object that propagates context across transitions would be uniquely valuable.

5. **Renewal risk forecast using leading indicators** — 180-day horizon; combine engagement trend, product adoption trajectory, support burden, and contract signals into a confidence-scored forecast.

6. **Executive and board-ready reporting** — auto-generated portfolio health summary by segment, NRR trend, churn attribution. The VP should not spend 2–3 days building slides.

### Areas Where ServiceNow Has Structural Advantages

- **ITSM + support + contract data already in platform** → eliminates the data fragmentation problem for SNOW-native accounts
- **Cross-functional visibility without seat licensing friction** → addresses the PlanHat unlimited-seat advantage natively
- **Workflow automation (Flow Designer)** → the playbook engine exists; needs CS-specific templates and configuration UX
- **Mobile (Now Mobile)** → enterprise-grade mobile story that PlanHat lacks

### Areas Needing Discovery Before Building

- **What does "good health score" actually predict at ServiceNow scale?** — the model needs to be trained on CEG's actual churn and expansion outcomes, not generic signals
- **What is the actual adoption rate of PS-to-CSM handoff packages today?** — if CSMs aren't reading them, the problem is different from what we assume
- **How do CSMs at ServiceNow's CEG actually spend their time today?** — a time-and-motion study of the top 10 CSM activities would ground every priority decision
- **Where do digital/tech-touch accounts break down in the current platform?** — 1:many CS at ServiceNow's scale is a specific problem worth separate discovery

---

*Last updated: 2026-04-06. Research should be validated with primary CSM interviews. Priority validation gaps are marked [Needs Validation] throughout. Promote confirmed patterns to `🤖 AI/patterns/learned-patterns.md` at 3+ confirmations.*

---
**Cross-references:** [csm-icp-market-research.md](csm-icp-market-research.md) · [hypotheses.md](hypotheses.md)
**Confirms hypothesis:** CS Investment Paradox · Cross-Functional Orchestration Whitespace
**Feeds decision:** CSP product roadmap prioritization
