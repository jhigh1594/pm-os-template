# Decision Brief Template

A decision brief is a 1-page output, not a research report. Its job is to answer a specific decision with evidence you can defend. It does not summarize all the themes from your data. It answers the question on the table.

**Rule:** If someone could read your brief and still not know what to do, it is not a brief — it is a summary. Start over.

---

## Template

```markdown
# Research Brief: [Decision on the table — be specific and narrow]

**Date:** [YYYY-MM-DD]
**Data sources:** [N interviews / survey responses / call notes — type and volume]
**Participants:** [Who was interviewed — segment, status, relevant context]

---

## Decision This Informs
[The specific decision in 1–2 sentences. Name the trade-off or choice.
"Should we add a screen to the device?" not "User needs research."]

---

## What We Learned

**Insight 1: [Statement with a direction — not a finding]**
> "[Verbatim quote]" — P03, ~18:40

[1–2 sentences explaining what this means and why it matters for the decision]

---

**Insight 2: [Statement with a direction]**
> "[Verbatim quote]" — P07, ~22:15

[1–2 sentences]

---

**Insight 3: [Statement with a direction]**
> "[Verbatim quote]" — P01, ~09:30

[1–2 sentences]

---

## Disconfirming Evidence
[At least one finding that cuts against the insights above. Required — not optional.
"3 of 10 participants mentioned screen directly but described problems a screen wouldn't solve (navigation, GPS, trail routing). A screen without those features would not retain them."]

---

## Confidence Assessment
| Insight | Evidence strength | Note |
|---|---|---|
| Insight 1 | Strong (7/10 participants) | Consistent across segments |
| Insight 2 | Provisional (3/10 participants) | Skewed toward churned Garmin switchers |
| Insight 3 | Thin (2/10 participants) | Needs validation with broader cohort |

---

## Recommended Action
[One recommendation tied directly to the decision. Take a position.
Not "more research needed" unless that genuinely is the answer.
"Do not invest in screen hardware until GPS/navigation is scoped — screen alone would retain ~30% of churned users but would not address the 45% who left for competitor feature sets a screen can't deliver."]

---

## What We Still Don't Know
1. [Top open question — what research should come next, and why it matters]
2. [Optional second question if genuinely important]

---

## Source Index
| Participant | Role / Segment | Status | Key signal |
|---|---|---|---|
| P01 | [Role] | Churned | [One-line summary of their primary theme] |
| P02 | [Role] | Active | [One-line summary] |
| ... | | | |
```

---

## What Belongs in Each Section

### Decision This Informs
Name the trade-off. "Whether to build X" is better than "understanding user needs." The narrower the decision, the more useful the brief. If the decision has already been made and the research is post-hoc, name that honestly.

### What We Learned (Insights)
- Each insight is a statement with a direction — someone could reasonably disagree with it
- Each insight is supported by at least one verbatim quote with source (participant ID + timestamp)
- Insights are sequenced by decision relevance, not by how many people mentioned them
- 2–4 insights is the right range; more than 4 usually means you haven't synthesized

### Disconfirming Evidence
This section is non-negotiable. If you can't find evidence that cuts against your main insights, you haven't looked hard enough. The section exists to demonstrate rigor — and to protect you when a stakeholder raises the counterargument.

### Confidence Assessment
Be honest about evidence quality. "7 of 10 participants" vs. "2 of 10 participants" is not the same confidence level. Staking everything on thin evidence is worse than flagging the gap and recommending follow-up.

### Recommended Action
Take a position. If the evidence genuinely doesn't support a recommendation, say so and specify what additional data would move you. "We need more research" without specifying exactly what and why is not a useful answer.

### What We Still Don't Know
Limits the scope of the brief. Signals to stakeholders that you're not overclaiming. Suggests the next research investment. Keep this to 1–2 items — the ones that would most change the recommendation if answered.

---

## Common Brief Failures

| Failure | Sign | Fix |
|---|---|---|
| Summary masquerading as brief | Insights are just themes listed without a direction | Add "which means we should..." to each insight |
| Missing disconfirmation | All evidence points one direction | Look at outlier participants; recruit contrary cases |
| Overclaimed confidence | "Users want X" when 2 of 10 mentioned it | Add participant count to every insight |
| Undirected recommendation | "Consider investing in X" | Name the specific decision: build / don't build / test before building |
| No quotes | Brief uses paraphrase or summary | Return to transcript; extract verbatim with timestamp |
| Brief too long | More than one page | Cut to the three insights most relevant to the decision |
