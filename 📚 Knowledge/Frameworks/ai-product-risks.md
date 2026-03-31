# AI Product Risk Framework

**Source:** Cagan/SVPG + Nika Dharajiya's four AI product risk dimensions, adapted for B2B enterprise planning software context.
**Used by:** `/spec` (AI feature mode), `/think mode=ai-risk`, `/discover` (AI concept phase 3 extension)
**Last updated:** 2026-03-28

---

## Why This Framework Exists

AI features in enterprise software face a higher trust threshold than consumer AI. When an AI recommendation drives a portfolio decision, a PI planning cycle, or a capacity reallocation, the organizational consequences of a wrong or unexplained output are significant. B2B customers need to be able to audit AI outputs, override them, and trust the system will degrade gracefully when data is insufficient.

This framework runs four risk dimensions as a validation gate. Any `[NEEDS INPUT]` flag blocks spec completion until resolved.

---

## Risk Dimension 1: Probabilistic vs. Deterministic Behavior

**The problem:** AI systems produce outputs that vary with inputs, model state, and training data. Enterprise customers expect deterministic systems — the same input produces the same output. This mismatch creates product trust failures.

### Questions to Answer Before Building

1. What is the acceptable error rate, and who has defined it?
2. How will we communicate variance/confidence to the user?
3. What happens at the extremes — when the model is highly uncertain?
4. Have customers been calibrated to expect probabilistic outputs, or will they be surprised?

### Validation Test

Run: "What does the user see when the model outputs two different answers for the same input on two different days?" If no answer exists, this is `[NEEDS INPUT]`.

### B2B-Specific Concern

Enterprise planning decisions are acted on by large teams. An AI-suggested PI risk rating or capacity forecast that changes unexpectedly between sessions undermines PM credibility with engineering and executive stakeholders. Define the acceptable variance threshold explicitly and design for it.

**Design pattern:** Present AI output as: **What** (the recommendation) + **Why** (one sentence explanation) + **Confidence** (% or High/Medium/Low) + **Override** (explicit user control).

---

## Risk Dimension 2: Training Data Quality and Coverage

**The problem:** AI models are only as good as the data they're trained on. If the training data doesn't represent your ICP, the model performs poorly for your best customers.

### Questions to Answer Before Building

1. What is the minimum data threshold required for the model to produce reliable outputs?
2. What happens below that threshold — degraded mode, no output, or false confidence?
3. Does the training data represent our ICP (enterprise, 500+ users, complex portfolios)?
4. Which customer segments are underrepresented, and what's the failure mode for them?

### Validation Test

Run: "For a new customer with 90 days of data, what does this feature do?" If the answer is "it works normally," this is `[NEEDS INPUT]` — the model almost certainly degrades and customers need to know.

### B2B-Specific Concern

Enterprise customers onboard slowly. A dependency risk predictor that requires 6 months of card history will be useless for the first half of a customer's contract. Define the minimum data bar, gate access below it, and design the degraded-state experience. Failure for 40% of accounts in year 1 is a churn driver.

**Design pattern:** Show a data sufficiency indicator. For customers below threshold: "This feature becomes available once [X condition is met]. Here's your current progress: [N/M cards with dependency data]."

---

## Risk Dimension 3: Explainability, Trust, and Human Override

**The problem:** Black-box AI outputs don't drive behavior change in enterprise teams. If users can't understand why the AI produced a recommendation, they either ignore it or follow it blindly — neither is acceptable.

### Questions to Answer Before Building

1. Can we show the user a one-sentence "why" for every AI output?
2. Is there an explicit override mechanism — can the user reject the AI recommendation?
3. What is the recovery path after an override — does the AI learn, or does it keep repeating the same recommendation?
4. Is AI-generated content clearly labeled as such (vs. human-authored) in the UI?

### Validation Test

Run: "Show me the screen where the AI recommends [X]. Can the user understand why, disagree, and override it?" If the override path doesn't exist or the explanation is absent, this is `[NEEDS INPUT]`.

### B2B-Specific Concern

"AI thinks your PI is at risk" requires explanation to be actionable. An RTE needs to understand *what* risk factor drove the assessment to take it to their ARTe or VP. Without explainability, AI recommendations become noise that gets ignored after the first surprise.

**Design pattern:** Every AI output surface follows: `[WHAT the AI recommends] — [WHY in one sentence] — [Confidence: H/M/L] — [Override: Yes/No/Snooze]`

---

## Risk Dimension 4: Viability, Ethics, and Legal

**The problem:** AI features that process personal data, produce decisions that affect employees, or operate in regulated industries carry legal and ethical obligations that product teams often discover late.

### Questions to Answer Before Building

1. Does this feature process PII, and if so, under which data processing agreements?
2. Which ICP industry regulations apply? (SR 11-7 for financial services, GDPR Article 22 for automated decisions affecting individuals, HIPAA for health)
3. Has Legal and Privacy signed off on the data use?
4. Is there an opt-out mechanism for customers who can't or won't use AI features?
5. Can the system produce an audit trail of AI outputs and human overrides?

### Validation Test

Run: "Can a customer in financial services or insurance deploy this feature and pass their internal AI governance review?" If the answer requires investigation, this is `[NEEDS INPUT]`.

### B2B-Specific Concern

Financial services and insurance customers (a significant part of the target ICP) require auditability and opt-out capability for AI features that affect staffing, capacity, or risk decisions. A feature that doesn't support audit trails will fail their procurement review or trigger retroactive remediation. Build for auditability from the start.

**Design pattern:** Maintain an immutable log of AI outputs with timestamps, confidence scores, and human override decisions. Make it exportable.

---

## AI Risk Validation Checklist

Run this checklist for any AI feature before spec completion. Each `[ ]` = `[NEEDS INPUT]`.

```
### AI Risk Validation — [Feature Name]

**Risk 1: Probabilistic Behavior**
[ ] Acceptable error rate defined (by whom? by when?)
[ ] Variance/confidence communicated to user in UX
[ ] Behavior at high-uncertainty edge case designed
[ ] Customer expectation calibration plan exists

**Risk 2: Training Data**
[ ] Minimum data threshold for reliable output defined
[ ] Degraded-state experience designed (below threshold)
[ ] ICP representativeness of training data validated
[ ] New customer / low-data-volume experience designed

**Risk 3: Explainability & Override**
[ ] One-sentence "why" exists for every AI output
[ ] Explicit user override mechanism implemented
[ ] AI-generated content labeled in UI
[ ] Override recovery path designed (what happens after override?)

**Risk 4: Viability, Ethics, Legal**
[ ] PII processing mapped to data processing agreements
[ ] Applicable industry regulations identified and reviewed
[ ] Legal/Privacy sign-off obtained or scheduled
[ ] Opt-out mechanism exists for customers who decline AI features
[ ] Audit trail of AI outputs and overrides available

**Highest-risk dimension:** [1 / 2 / 3 / 4]
**Primary strategic constraint:** [One sentence on what most limits this feature's viability]
```

---

## B2B Enterprise AI Trust Pattern

Every AI feature output surface should follow this pattern:

```
[WHAT]    The AI recommendation or output — specific, actionable
[WHY]     One sentence: the primary factor driving this recommendation
[CONF]    Confidence: High / Medium / Low (or %)
[OVERRIDE] User control: Accept / Override / Snooze / Flag
```

Example:
> **PI Risk: High** — Dependency between Card 4821 and Card 4832 is unresolved with 3 sprints remaining. [High confidence — 8 of 8 historical similar dependencies resulted in slip] [Override: Mark as mitigated | Snooze 1 sprint | Escalate to RTE]

---

## Integration Notes

- **`/spec`**: After loading `ai-features-guide.md`, load this framework and run the checklist. Any unchecked item → `[NEEDS INPUT]` that blocks spec completion.
- **`/think mode=ai-risk`**: Load this framework. Run all four dimensions. Surface highest-risk dimension as primary constraint. Output checklist status.
- **`/discover`**: When solution concept involves AI/ML behavior, add this framework's checklist to Phase 3 validation summary alongside the standard four-risk table.
