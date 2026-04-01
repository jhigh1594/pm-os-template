# PlanHat Competitive Intelligence Report
*For: ServiceNow Customer Success Platform Roadmap*
*Date: 2026-04-01*
*Analyst: AI Research Agent — Principal Product Strategy*

## Confidence Legend
- 🟢 High: Multiple independent sources, customer quotes, corroborated
- 🟡 Medium: Single source or limited corroboration
- 🔴 Low: Inferred or from competitor's own marketing only

---

## Executive Summary

1. **PlanHat is a legitimate Gartner Magic Quadrant Leader** (2025, second consecutive year, strongest year-over-year momentum in vision AND execution). It is not a niche challenger — ServiceNow CSP must treat it as a serious incumbent with growing enterprise credibility, not a lightweight mid-market tool.

2. **The single biggest retention driver is the combination of unlimited-seat pricing + deep configurability.** Customers stay because the cost model removes friction for cross-functional adoption, and the platform bends to their data model rather than forcing them to bend to it. This is the moat to crack.

3. **PlanHat's most praised capability is Health Lab** — segment-aware, multi-signal health scoring with automated routing. Customers describe it as irreplaceable. It is table-stakes for ServiceNow CSP.

4. **The most consistent complaint is configuration complexity.** Metrics setup is described as "like learning to program." Salesforce sync is "quite complicated." Documentation refers to old UI. This is an exploitable gap — time-to-value is PlanHat's Achilles heel.

5. **PlanHat's data model breaks on non-standard B2B use cases.** Reviewers explicitly flag B2B2C, transactional revenue, and product analytics as areas where the platform requires "complex workarounds." ServiceNow's broader data platform is a structural advantage here.

6. **PlanHat's AI features are real but shallow.** AI Workflows, Conversational AI, and an MCP Server exist in production as of late 2025, but independent reviewers score AI depth as limited compared to newer AI-native platforms. ServiceNow's Now Intelligence and agentic AI stack is a genuine differentiator if executed well.

7. **ServiceNow's unique moat is cross-platform data fusion** — ITSM tickets, incident history, change management, and contract data already live in the platform. No standalone CSP can replicate this without a years-long integration project. This is the primary differentiation vector to build toward.

---

## 1. What PlanHat Does Best

### 1a. Segment-Aware Health Scoring (Health Lab)
🟢 **High confidence** | Source: PlanHat product docs, Gartner Peer Insights, CheckThat.ai review synthesis, TrustRadius

PlanHat's Health Lab allows organizations to build separate scoring logic per customer cohort — a strategic account might weight executive sponsorship heavily while a mid-market account weights adoption velocity. Three mechanisms drive this:
- **Layered signal detection**: merges engagement recency, support ticket trends, and conversation frequency with AI-generated sentiment from calls and emails
- **Segment-based scoring logic**: different rules per cohort, configurable weighting
- **Automated routing**: health score changes trigger workflows and alerts automatically without manual triage

This is not generic health scoring. The configurability addresses a real enterprise problem — diverse portfolios with accounts that cannot be measured on a single scale. Customers at firms like Nutanix and Nasdaq run this at scale.

### 1b. Unlimited-Seat Pricing Model
🟢 **High confidence** | Source: Bianca Ker practitioner review (Apr 2025), Vendr marketplace data, CheckThat.ai synthesis

PlanHat prices by customer account volume, not by internal users. This removes the "churn is everyone's problem" blocker — sales, solutions engineers, executives, and support staff can all access customer data without incremental license cost. Multiple reviewers cite this as a primary reason they selected and stayed with PlanHat over Gainsight. One practitioner's exact summary: *"Unlimited Seat model! Because churn is an everyone problem."*

Average contract value: $39,723/year (Vendr data). Range: $18,125–$114,750. Mid-market typically $25,000–$45,000.

### 1c. Customer Portals and Collaborative Success Planning
🟢 **High confidence** | Source: PlanHat feature docs, Gartner Peer Insights reviews, CheckThat.ai synthesis

PlanHat's Portal feature gives end-customers branded, live-data workspaces where they can view health dashboards, shared playbooks, and project timelines. Multiple reviewers note the portal "improved adoption and helped us build trust." The Live Collaboration feature extends this into real-time multiplayer document editing and auto-generated meeting prep summaries. The differentiated claim: customers become "active co-authors of their own success plan."

This is meaningfully ahead of most CSP competitors on external-facing collaboration.

### 1d. Flexible Data Model and Open API
🟢 **High confidence** | Source: TrustRadius reviews, Gartner Peer Insights, CheckThat.ai

PlanHat's data architecture is built for B2B SaaS subscription businesses. It supports custom data pipelines, time-series analytics for trend analysis, data transformation from raw events to metrics, and an open API for custom integrations. Reviewers with complex custom objects consistently describe PlanHat as more adaptable than Gainsight or ChurnZero for standard B2B models.

### 1e. Automation Engine (Playbooks / Workflows)
🟢 **High confidence** | Source: PlanHat docs, TrustRadius, Gartner Peer Insights

PlanHat's automation layer handles the full CS workflow lifecycle — onboarding sequences, renewal triggers, escalation routing, and expansion plays. Projects (structured playbooks) and Sequences (automated communication flows) are the two primary primitives. Users describe automation as a core reason for retention: it operationalizes institutional CS knowledge into repeatable processes without code.

---

## 2. What Customers Love (Voice of Customer)

### Theme: Flexibility and Customization
🟢 **High confidence** | Source: CheckThat.ai (G2 synthesis, 2026-01-29), Gartner Peer Insights (45 reviews, accessed 2026-04-01)

- *"Complete customisability enables implementation of complex use cases around expansion"* — CheckThat.ai synthesis of G2 reviews
- *"The platform is flexible and adapts easily to our specific requirements"* — Director of Operations, Finance, $3B–$10B company (using since 2018), Gartner Peer Insights
- *"I have never had a better partner to drive my business than Planhat"* — VP, Customer Service & Support, Telecom, $50M–$1B, Gartner Peer Insights (5 stars)

Underlying JTBD: *I need a CS system that reflects how my business actually works, not how the vendor thinks CS should work.*

### Theme: Single Source of Truth / Cross-Team Visibility
🟢 **High confidence** | Source: TrustRadius (8/10, 43 reviews), CheckThat.ai

- Serves as "single source of truth for customer data" — TrustRadius pattern across multiple reviews
- CSM teams, Solutions Architects, and executives all use read-only or full access to prepare for customer interactions
- "It's all kind of integrated into one place rather than scattered across communication channels" — Health Lab feature page, corroborated by reviewer sentiment

Underlying JTBD: *I need my whole commercial team aligned on a single view of the customer before any interaction.*

### Theme: Customer-Facing Portals and Trust-Building
🟡 **Medium confidence** | Source: CheckThat.ai synthesis, PlanHat feature docs

- "Portal functionality improved adoption and helped us build trust" — CheckThat.ai G2 synthesis
- Customers specifically call out the ability to share playbooks and usage dashboards directly with their end customers

Underlying JTBD: *I need my customers to see the progress and value we're delivering, not just take my word for it.*

### Theme: Support Quality
🟢 **High confidence** | Source: Gartner Peer Insights (multiple reviewers), Bianca Ker practitioner blog (Apr 2025)

Support is praised across nearly every review source. Specifically: quick live chat response, proactive assistance during complex configuration, and dedicated CSM relationships. This matters because the product complexity requires implementation hand-holding — support quality compensates for the steep learning curve.

### Theme: Pricing Fairness and Per-Seat Absence
🟢 **High confidence** | Source: Bianca Ker practitioner review, CheckThat.ai, Vendr data

Customers consistently call the pricing model "fair" and "cost-effective compared to competitors." The absence of per-seat fees for internal users is the single most frequently cited commercial advantage in practitioner reviews.

---

## 3. Key Workflows and Use Cases That Drive Retention

These are the daily workflows users build operational muscle memory around — the habits that make switching costly:

### 3a. Morning Health Queue
CSMs start the day in a filtered view of accounts whose health scores changed overnight. Automated routing has already created tasks or triggered plays for red accounts. The CSM reviews, adjusts priority, and proceeds — all within PlanHat. Zero tab-switching to Salesforce or spreadsheets for the core triage loop.

### 3b. Renewal Pipeline Management
120-day renewal pipeline tracked inside PlanHat with risk flags, engagement health, and product usage data consolidated. Reviewers at TrustRadius specifically cite "renewal forecasting" as a daily workflow that replaced manual Salesforce pipeline management. The Value Realization and Success Insights AI agents (built into the platform) augment this workflow.

### 3c. Onboarding Project Management
Structured playbooks (Projects) guide new customers through implementation milestones. Portals let the customer see their own progress. This creates a "visible proof of value" loop early in the relationship — reducing early churn without requiring CSM calls for every status update.

### 3d. Expansion Identification
Automated filters surface accounts with high engagement + low product adoption breadth, flagging upsell candidates. The Revenue Analytics module tracks subscription-level data to identify expansion signals. CSMs describe this as replacing a quarterly manual audit with a continuous, automated signal feed.

### 3e. Executive Business Reviews (EBR) Preparation
Live Collaboration + auto-generated AI meeting summaries + presentation sync'd to live data means CSMs prepare EBR decks inside PlanHat rather than building PowerPoint from scratch. This workflow reduces EBR prep time and is frequently mentioned as a time-saving differentiator.

---

## 4. The 20% Driving 80% of Value (Pareto Analysis)

| Capability | JTBD It Solves | Table-Stakes or Differentiator for SNOW CSP? |
|---|---|---|
| **Health Lab (segment-aware scoring)** | "Know which of my 200 accounts needs attention today — and make the answer different per segment" | **Table-stakes.** Must match this. ServiceNow has health/risk framework in Zurich release; needs segment-aware scoring parity. |
| **Unlimited-seat pricing model** | "Get my whole company looking at customer data without a budget fight" | **Differentiator opportunity.** SNOW sells enterprise seats differently; the pricing architecture question is whether CSP can enable broad access without per-seat friction. |
| **Customer Portals** | "Show my customers their own progress and make them co-owners of outcomes" | **Differentiator opportunity.** ServiceNow's existing Service Portal infrastructure + Now Experience could enable this faster than PlanHat; significant UX investment needed to close the quality gap. |
| **Playbook Automation Engine** | "Encode my best CSM's instincts into repeatable workflows every CSM executes perfectly" | **Table-stakes.** ServiceNow's Flow Designer and workflow automation are adjacent; needs CS-specific playbook templates, not just generic flows. |
| **Flexible/Open Data Model** | "Map the platform to MY data structure, not force my data into your schema" | **ServiceNow advantage IF leveraged.** SNOW has a far richer data model across ITSM, HR, Finance. The risk is that CSP is too rigid in what data it surfaces for CS use cases. |

---

## 5. Gaps, Complaints, and Unmet Needs

### Gap 1: Configuration Complexity and Time-to-Value
🟢 **High confidence** | Source: Gartner Peer Insights (3-star review), CheckThat.ai G2 synthesis, Oliv.ai evaluation (52/80 score, accessed 2026-02-10)

- *"Really find their system of setting up metrics difficult to say the least"* — Gartner Peer Insights reviewer
- *"Took me a hard time when it comes to learning and adapting"* — CheckThat.ai G2 synthesis
- Advanced features described as "like learning to program" — CheckThat.ai
- Metrics setup requires "reading really long-form articles just to understand their system"
- 2–3 hour wait times to identify formula errors
- Implementation timeline: 4–8 weeks for standard deployments

**ServiceNow CSP Opportunity Signal:** Design for guided configuration with smart defaults. Pre-built industry templates for health scoring, playbooks, and dashboards would leapfrog PlanHat's setup experience. The CSM who buys should see value in day one, not week four.

### Gap 2: Salesforce Integration Complexity
🟢 **High confidence** | Source: CheckThat.ai G2 synthesis, Gartner Peer Insights

- Salesforce sync described as "quite complicated to manage and solve basic use cases"
- Data ingestion rules assume clean Salesforce data — "poorly handles bad data"
- Extended data cleanup required post-implementation
- Configuration described as "unexpectedly complex"

**ServiceNow CSP Opportunity Signal:** ServiceNow already IS the system of record for many enterprise customers (or has native Salesforce connectors via IntegrationHub). A CSP that eliminates the sync problem entirely — because the data already lives in SNOW — is a structural advantage, not a feature comparison.

### Gap 3: Product Analytics Depth
🟡 **Medium confidence** | Source: Gartner Peer Insights (Product Manager, Banking), Oliv.ai evaluation

- *"Lacks capability to scale Product Analytics for tracking user behavior"* — Product Manager, Banking, Gartner Peer Insights
- Oliv.ai evaluation flagged limited generative AI capabilities vs newer platforms
- PlanHat's product usage tracking is passive (ingestion via API) rather than active instrumentation

**ServiceNow CSP Opportunity Signal:** Deep integration with product telemetry — especially for ServiceNow customers using the platform as a managed service — is an area where SNOW can offer native product usage data that PlanHat would require an API integration to replicate.

### Gap 4: Data Model Limitations for Non-Standard B2B Models
🟢 **High confidence** | Source: Gartner Peer Insights (multiple reviewers), Oliv.ai evaluation (2026-02-10)

- Reviewers explicitly cite B2B2C as unsupported without complex workarounds
- Transactional revenue models require significant custom configuration
- Per-object pricing discourages optimal configurations
- One reviewer called the data model "the most bizarre one I have faced"

**ServiceNow CSP Opportunity Signal:** Enterprises operating multi-tier or hybrid customer models (common in tech, telecom, and financial services) are underserved by PlanHat. ServiceNow's flexible CMDB-based data model can natively represent these hierarchies.

### Gap 5: Outdated Documentation and Self-Service Onboarding
🟡 **Medium confidence** | Source: Oliv.ai evaluation, Gartner Peer Insights

- *"Documentation is outdated and refers to the old UI, making self-service difficult"* — Oliv.ai, citing user feedback
- New customers need more best practices guidance from the platform team
- Heavy reliance on professional services or CSM support to achieve full configuration

**ServiceNow CSP Opportunity Signal:** A product-led onboarding path with contextual in-app guidance and a robust, always-current knowledge base would be a credible differentiator — especially for enterprise customers who expect platform self-sufficiency at scale.

### Gap 6: Mobile Functionality
🟡 **Medium confidence** | Source: Bianca Ker practitioner review (Apr 2025)

- Limited mobile app functionality compared to desktop experience
- Reduces field CSM utility

**ServiceNow CSP Opportunity Signal:** ServiceNow's mobile capabilities (Now Mobile) are already enterprise-grade. A CSP mobile experience built on Now Mobile would surpass PlanHat's mobile story without additional development investment.

### Gap 7: Forecasting Accuracy
🟡 **Medium confidence** | Source: CheckThat.ai G2 synthesis

- Revenue forecasting capabilities described as "nearly impossible" by some reviewers
- Renewal forecasting is available but accuracy at enterprise scale is questioned

**ServiceNow CSP Opportunity Signal:** ServiceNow's combination of contract management data, ITSM engagement signals, and Now Intelligence predictive models creates a richer forecasting substrate than PlanHat can build from CS signals alone.

---

## 6. Strategic Implications for ServiceNow CSP

### SI-1: Because PlanHat's configuration complexity is its #1 complaint, ServiceNow CSP should invest in guided setup, pre-built industry playbook templates, and a "time-to-first-insight" metric as a primary product KPI.

PlanHat loses deals and post-sale goodwill on implementation friction. The 4–8 week setup timeline and "like learning to program" metrics configuration are documented in multiple independent reviews. ServiceNow's enterprise customer base expects fast time-to-value. A CSP that surfaces a meaningful health dashboard within 48 hours of provisioning — using existing SNOW data — would be a category-defining differentiator. **Build-note:** Flow Designer templates for CS playbooks already partially exist; the gap is CS-specific, pre-configured health score defaults that work out of the box.

### SI-2: Because PlanHat's Salesforce data dependency is a recurring integration pain point, ServiceNow CSP should position "no sync required" as a primary value prop for customers already on the ServiceNow platform.

The Salesforce → PlanHat sync is consistently cited as complex, fragile, and assumption-heavy (requires clean data). ServiceNow CSP customers who already have accounts, contracts, service tickets, and entitlements in SNOW get a CSP with zero data synchronization overhead. This is not a feature — it is a structural cost advantage that eliminates an entire category of implementation risk. **Marketing implication:** The battlecard headline writes itself: "Your customer data is already here."

### SI-3: Because PlanHat's unlimited-seat model is its single most-cited commercial advantage, ServiceNow CSP should explore pricing architecture that minimizes internal adoption barriers across CS, Sales, and Support personas.

Reviewers praise PlanHat explicitly for enabling company-wide access to customer data without per-seat cost fights. ServiceNow's enterprise licensing model (platform seats) may create internal friction for broad CSP adoption. The product team should work with pricing to define a CSP access model that lets adjacent teams — renewals managers, support engineers, account executives — view CS data without triggering additional license costs. **Risk:** If SNOW CSP is perceived as "CS team only" while PlanHat is "company-wide," the commercial story will lose to PlanHat at procurement stage.

### SI-4: Because PlanHat's Health Lab is the #1 retention driver, ServiceNow CSP's health scoring must support segment-level configurability, multi-signal fusion (including ITSM signals), and automated routing — not just a single weighted score.

PlanHat's Health Lab is not just a health score — it is a segment-aware, AI-augmented, auto-routing engine. The Zurich release introduced the Success Risk Solution AI Agent and Product Usage Dashboard; these are directionally correct but need to match PlanHat's flexibility in allowing different scoring logic per customer cohort. **Unique SNOW advantage:** ServiceNow CSP can incorporate ITSM signals (incident volume, CSAT from support tickets, SLA breaches, change request frequency) that PlanHat can only access via API integration. This creates a richer, more accurate health signal that PlanHat structurally cannot match without a ServiceNow integration.

### SI-5: Because PlanHat's Customer Portal is a top-rated capability that drives external trust and adoption, ServiceNow CSP should build a differentiated customer-facing experience leveraging Now Experience and ServiceNow's existing Service Portal infrastructure.

PlanHat's portal gives customers a branded window into their own health data, success plans, and project progress. This is not a table-stakes feature — it is a relationship-building capability that reduces churn by making customers co-owners of their outcomes. ServiceNow has the platform infrastructure (Now Experience, Service Portal, ServiceNow App Engine) to build a richer version of this, potentially including self-service value realization dashboards tied to business outcomes that PlanHat cannot surface. **Build-vs-extend:** This is an extend opportunity; the experience layer needs CS-specific design, not infrastructure investment.

### SI-6: Because PlanHat's data model breaks on B2B2C, transactional, and multi-tier customer structures, ServiceNow CSP should explicitly target enterprise customers with complex customer hierarchies as a beachhead differentiation segment.

Multiple independent reviewers call out PlanHat's data model limitations for non-standard B2B structures. Enterprises in telecom, financial services, and technology often manage multi-tier customer hierarchies (parent company → subsidiary → end user) that PlanHat handles poorly. ServiceNow's CMDB natively represents these relationships. A CSP that surfaces health scoring and playbooks across account hierarchies — including inherited risk from sub-entities — would serve a segment that PlanHat actively frustrates today. **ICP implication for CSP:** Prioritize the 250–5,000 employee enterprise SaaS and tech companies that have outgrown standard B2B models.

### SI-7: Because PlanHat's AI capabilities are real but shallow, ServiceNow CSP should invest in workflow-embedded AI that produces measurable, attributable outcomes — not AI features that exist as checkboxes.

PlanHat has AI Workflows, Conversational AI, Writing Assistant, and an MCP Server in production (as of late 2025). Independent evaluators score its generative AI depth as limited compared to AI-native platforms. ServiceNow's Now Intelligence, AI Agents (Success Health Monitor, Success Trend, Success Risk Solution — Zurich release), and platform-wide Copilot infrastructure represent a genuine capability advantage — but only if the product surfaces outcomes customers can attribute to AI, not just AI-flavored features. The Nutanix quote is instructive: *"Planhat's AI capabilities... give us the ability to measure impact — which is critical to how we steer our overall strategy."* Impact measurement is the standard. Meet it or exceed it.

---

## 7. Open Questions and Hypotheses to Validate

### Questions Requiring Primary Research

**Q1: Does PlanHat's Health Lab have a configurable model limit per tier?**
Reports suggest segment-based scoring is available on all paid plans, but there may be limits on number of health models or scoring variables at lower tiers. If true, this is a commercial wedge for large portfolios.

**Q2: How does PlanHat handle multi-product health scoring?**
Customers managing multiple products per account (e.g., a platform + add-ons) may need separate health scores per product line. PlanHat's support for this is unclear from available sources. Important for ServiceNow's multi-product enterprise customers evaluating CSP.

**Q3: What is PlanHat's true implementation time for enterprise customers vs. mid-market?**
Published range is 4–8 weeks, but enterprise accounts with complex Salesforce configurations and custom data models likely run 3–5 months. Validating this in win/loss interviews would confirm the time-to-value gap size.

**Q4: How strong is PlanHat's renewal forecasting accuracy at scale?**
"Nearly impossible" forecasting was cited in one review source (🟡 medium confidence). This is a high-value claim if confirmed — forecasting accuracy is a top buying criterion for VP CS buyers. Needs validation via customer interviews or analyst research.

**Q5: Is PlanHat's unlimited-seat model profitable at enterprise scale?**
At $39K average contract value with unlimited internal users, their unit economics may compress at large enterprises. Understanding their true pricing floor would inform ServiceNow's competitive pricing strategy.

### Hypotheses to Test

**H1:** ServiceNow enterprise customers who already use SNOW for ITSM would reduce CS platform implementation time by 60%+ vs. a PlanHat implementation that requires Salesforce sync configuration. *Test: Count ITSM data objects already mappable to CSP health signals in a reference architecture design.*

**H2:** PlanHat's customer portal adoption rate is lower than their marketing suggests, because portal configuration is as complex as the rest of the platform. *Test: Ask in CS community forums how many PlanHat customers actively use portals vs. have them configured but unused.*

**H3:** The "data model is bizarre" complaint correlates with customers who came from Gainsight, not customers who started with PlanHat as their first CSP. *Test: Segment negative reviews by prior tool to understand if this is a migration friction problem vs. inherent design problem.*

---

## Sources and Confidence Notes

| Source | Content Used | Access Date | Reliability Tier |
|---|---|---|---|
| PlanHat product docs (planhat.com/platform, /features/health-lab, /features/ai-automations, /features/live-collaboration) | Feature surface mapping, capability details | 2026-04-01 | Tier 1 (vendor, treat as marketing) |
| Gartner Peer Insights (gartner.com/reviews/product/planhat-customer-success-platform) | 45 reviews, 4.6/5 overall, verbatim quotes | 2026-04-01 | Tier 1 (verified enterprise reviewers) |
| CheckThat.ai G2 review synthesis | Positive/negative theme analysis, quote patterns | 2026-01-29 | Tier 2 (aggregated G2 data) |
| TrustRadius (43 reviews, 8/10) | Use case patterns, reviewer roles, business problems | 2026-04-01 | Tier 2 (verified B2B reviewers) |
| Bianca Ker practitioner blog (biancaker.com) | Pros/cons from active practitioner user | 2025-04-28 | Tier 3 (practitioner, single voice) |
| Oliv.ai platform evaluation (52/80 rubric score) | Independent scored evaluation, weakness identification | 2026-02-10 | Tier 2 (third-party research) |
| Vendr marketplace (vendr.com/marketplace/planhat) | Pricing data, contract values, negotiation patterns | 2026-04-01 | Tier 2 (procurement platform data) |
| PlanHat Gartner MQ announcement (prnewswire.com) | Market positioning, customer quotes (Nutanix) | 2025-11-07 | Tier 1 (verified press release with named quotes) |
| PlanHat "State of CSP Market 2025" editorial | Competitive landscape framing | 2025-09-05 | Tier 4 (vendor-authored, treat with skepticism) |
| ServiceNow Community — Zurich CSM release notes | SNOW CSP feature parity assessment | 2025-10-10 | Tier 1 (official product documentation) |
| ServiceNow Community — AI Agents for CS | SNOW AI agent capabilities | 2025-05-07 | Tier 1 (official product documentation) |
| Oliv.ai "Best CS Platforms 2026" | Third-party scoring methodology | 2026-02-10 | Tier 2 (independent evaluation) |

### Known Data Gaps
- **G2 direct access blocked (403):** Could not pull raw G2 review text; relied on third-party G2 syntheses (CheckThat.ai, Oreate AI). Confidence in quote attribution is moderate, not high.
- **Reddit r/CustomerSuccess:** Could not access directly. Community sentiment from this source is absent; it is a known signal source that warrants a manual research pass.
- **Capterra direct access:** Did not return usable PlanHat-specific review content in this research pass.
- **Pricing tiers:** PlanHat does not publish tier pricing. All pricing data is from Vendr procurement platform data and practitioner anecdote ($1,500/month starting point cited by one practitioner). These numbers should be validated in a competitive deal scenario.
- **Win/loss data:** All findings are based on public review data and analyst content. No first-party win/loss interview data against PlanHat was available for this analysis. Prioritize this in upcoming sales cycle debriefs.
