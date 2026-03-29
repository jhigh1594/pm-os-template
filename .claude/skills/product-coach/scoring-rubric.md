# Scoring Rubric

Detailed scoring criteria for each artifact dimension. Read this when scoring is ambiguous.

---

## Scoring Philosophy

### What Scores Measure

Scores assess **artifact quality**, not the PM's intelligence or effort. A low score means "this artifact has gaps that weaken its ability to achieve its purpose," not "you are bad at this."

### Score Distribution

Not every artifact should be a 4 or 5. Use the full range:

| Score | Frequency | Meaning |
|-------|-----------|---------|
| 5 | ~10% | Exceptional - publication-ready, teaches others |
| 4 | ~25% | Strong - minor revisions only |
| 3 | ~35% | Adequate - needs focused work on 1-2 dimensions |
| 2 | ~20% | Weak - significant gaps, needs rework |
| 1 | ~10% | Critical - fundamental problems, restart recommended |

### Evidence Requirements

- **Score 4-5**: Must cite specific, positive evidence from the artifact
- **Score 2-3**: Must cite specific gaps or weaknesses
- **Score 1**: Must explain the fundamental problem and why it blocks the artifact's purpose

---

## PRD Dimensions

### Problem Framing (Weight: 1.2)

**What it means:** Is the core user problem clear, specific, and separated from the proposed solution?

| Score | Criteria |
|-------|----------|
| 5 | Problem is specific, measurable, and clearly separated from solution. Includes who, what, and why it matters. |
| 4 | Problem is clear with minor ambiguity. Solution is mostly separate from problem statement. |
| 3 | Problem exists but mixes with solution, or is somewhat vague about who/what/why. |
| 2 | Problem is feature-shaped ("users want X") or buried in solution language. |
| 1 | No problem statement, or problem is indistinguishable from the feature description. |

**Diagnostic questions:**
- Can you state the problem without mentioning the solution?
- Does it specify who has this problem and how often?
- Would a skeptic understand why this matters?

### Evidence Quality (Weight: 1.1)

**What it means:** Does the artifact use credible customer, product, market, or delivery evidence?

| Score | Criteria |
|-------|----------|
| 5 | Multiple evidence types (customer quotes, data, research) with clear sourcing. Evidence directly supports the problem and approach. |
| 4 | Good evidence with minor gaps in sourcing or relevance. |
| 3 | Some evidence but thin (1-2 sources) or not clearly connected to claims. |
| 2 | Minimal evidence, or evidence is anecdotal without acknowledgment. |
| 1 | No evidence, or evidence contradicts the claims. |

**Diagnostic questions:**
- Can you trace each major claim to specific evidence?
- Is the evidence recent and from relevant sources?
- Does the evidence actually support what it claims to?

### Scope Discipline (Weight: 1.0)

**What it means:** Is the v1 boundary explicit, defensible, and appropriately constrained?

| Score | Criteria |
|-------|----------|
| 5 | V1 is sharply bounded with clear in/out list. Rationale for scope is explicit and defensible. |
| 4 | V1 is mostly clear with minor fuzziness at edges. |
| 3 | V1 exists but rationale is weak or boundaries are ambiguous. |
| 2 | V1 is mentioned but reads as "everything important" without trade-offs. |
| 1 | No V1 definition, or V1 is clearly too large to execute. |

**Diagnostic questions:**
- Could you ship this in the stated timeline with the stated team?
- Is there an explicit "what we're not doing" section?
- Does V1 prove the core hypothesis, or is it feature creep?

### Metrics Quality (Weight: 1.0)

**What it means:** Are success metrics leading, measurable, and tied to the problem?

| Score | Criteria |
|-------|----------|
| 5 | Has leading metrics that can be measured during development, tied directly to problem validation. |
| 4 | Good metrics with minor issues (some lagging, or weak connection to problem). |
| 3 | Has metrics but they're all lagging (ship-then-measure) or disconnected from problem. |
| 2 | Metrics exist but are vanity metrics or not actionable. |
| 1 | No metrics, or metrics that can't be measured. |

**Diagnostic questions:**
- Can you measure progress before launch?
- Do the metrics prove you solved the problem?
- Are the targets specific and time-bound?

### Differentiation (Weight: 0.9)

**What it means:** Does the artifact clarify why this approach is better than alternatives or status quo?

| Score | Criteria |
|-------|----------|
| 5 | Clear comparison to alternatives with explicit advantages. Acknowledges competitive context. |
| 4 | Differentiation exists but could be sharper or more specific. |
| 3 | Mentions alternatives but comparison is weak or one-sided. |
| 2 | No alternatives considered, or "we're better" without evidence. |
| 1 | Ignores alternatives entirely, or differentiation contradicts evidence. |

**Diagnostic questions:**
- What would the user do if this didn't exist?
- Why is this approach better than the obvious alternatives?
- What trade-offs does this approach accept?

### Risk Handling (Weight: 0.8)

**What it means:** Does it identify assumptions, dependencies, and failure modes that matter?

| Score | Criteria |
|-------|----------|
| 5 | Identifies key assumptions with validation plan. Lists dependencies and failure modes with mitigation. |
| 4 | Good risk identification with minor gaps in mitigation planning. |
| 3 | Lists risks but no validation plan, or risks are generic rather than specific. |
| 2 | Minimal risk discussion, or only technical risks (no assumption risks). |
| 1 | No risk discussion, or risks are dismissed without reason. |

**Diagnostic questions:**
- What has to be true for this to work?
- What could cause this to fail, and how would you know early?
- Are the risks specific to this feature or generic boilerplate?

---

## Decision Memo Dimensions

### Decision Framing (Weight: 1.1)

**What it means:** Is the actual decision explicit, bounded, and free of hidden assumptions?

| Score | Criteria |
|-------|----------|
| 5 | Decision is a clear question with explicit scope, stakeholders, and timeline. |
| 4 | Decision is mostly clear with minor ambiguity about scope or stakeholders. |
| 3 | Decision exists but is fuzzy about what's being decided or by whom. |
| 2 | Decision is buried or stated as a topic rather than a question. |
| 1 | No clear decision, or multiple decisions conflated. |

### Trade-off Quality (Weight: 1.2)

**What it means:** Does the memo make real opportunity costs and alternatives visible?

| Score | Criteria |
|-------|----------|
| 5 | Shows explicit opportunity cost: "Choosing X means we cannot do Y." Alternatives fairly represented. |
| 4 | Good trade-off analysis with minor gaps. |
| 3 | Lists pros/cons but doesn't show what's being given up. |
| 2 | Weak trade-off analysis, or alternatives are strawmen. |
| 1 | No trade-off analysis, or pretends there are no downsides. |

### Reversibility Handling (Weight: 0.9)

**What it means:** Does it distinguish one-way vs two-way doors and act accordingly?

| Score | Criteria |
|-------|----------|
| 5 | Explicitly categorizes decision as reversible/irreversible. Analysis depth matches reversibility. |
| 4 | Reversibility addressed but could be more explicit. |
| 3 | Mentions reversibility but doesn't adjust analysis accordingly. |
| 2 | Ignores reversibility. |
| 1 | Treats reversible decision as irreversible (over-analysis) or vice versa. |

### Evidence Quality (Weight: 1.0)

**What it means:** Is the recommendation supported by decision-relevant evidence?

| Score | Criteria |
|-------|----------|
| 5 | Evidence directly supports the specific decision at hand. Sourced and recent. |
| 4 | Good evidence with minor gaps in relevance or sourcing. |
| 3 | Some evidence but not clearly connected to this decision. |
| 2 | Minimal evidence, or evidence that doesn't support the recommendation. |
| 1 | No evidence, or evidence contradicts the recommendation. |

### Recommendation Strength (Weight: 1.0)

**What it means:** Is there a clear call rather than a soft summary of options?

| Score | Criteria |
|-------|----------|
| 5 | Clear, explicit recommendation with rationale. Acknowledges uncertainty appropriately. |
| 4 | Recommendation exists but could be more direct. |
| 3 | "Leaning toward" or soft recommendation without full commitment. |
| 2 | Summarizes options without making a call. |
| 1 | No recommendation, or recommendation is contradicted by analysis. |

### Strategic Fit (Weight: 1.0)

**What it means:** Does the recommendation advance the product and company strategy?

| Score | Criteria |
|-------|----------|
| 5 | Clear line to strategic goals with explicit connection. |
| 4 | Strategic connection exists but could be sharper. |
| 3 | Mentions strategy but connection is weak or generic. |
| 2 | No strategic connection, or contradicts stated strategy. |
| 1 | Ignores strategic context entirely. |

---

## Roadmap Narrative Dimensions

### Sequencing Logic (Weight: 1.2)

**What it means:** Does the plan explain why this order creates leverage or learning?

| Score | Criteria |
|-------|----------|
| 5 | Each item has sequencing rationale: "A before B because A enables/derisks B." |
| 4 | Good sequencing with minor gaps in rationale. |
| 3 | Items are in an order, but rationale is implied rather than stated. |
| 2 | Priority list without sequencing logic. |
| 1 | Random order or no order explanation. |

### Capacity Realism (Weight: 1.0)

**What it means:** Are team bandwidth, dependencies, and execution constraints credible?

| Score | Criteria |
|-------|----------|
| 5 | Explicit capacity assumptions (velocity, headcount, dependencies). Roadmap fits constraints. |
| 4 | Capacity addressed with minor gaps. |
| 3 | Implies capacity but doesn't state assumptions explicitly. |
| 2 | No capacity context, or roadmap clearly exceeds realistic capacity. |
| 1 | Ignores capacity entirely. |

### Portfolio Balance (Weight: 1.0)

**What it means:** Does the roadmap balance core, strategic, and risk-reduction work?

| Score | Criteria |
|-------|----------|
| 5 | Clear mix of work types with rationale for the balance. |
| 4 | Good balance with minor issues. |
| 3 | Some balance but one type dominates without reason. |
| 2 | All one type of work (e.g., all features, no maintenance). |
| 1 | No balance consideration. |

### Strategic Alignment (Weight: 1.1)

**What it means:** Is the roadmap traceable to product or business goals?

| Score | Criteria |
|-------|----------|
| 5 | Each item traces to specific OKR or strategic goal. |
| 4 | Good alignment with minor gaps. |
| 3 | Some items aligned, others unconnected. |
| 2 | Alignment is claimed but not demonstrated. |
| 1 | No strategic alignment. |

### Narrative Clarity (Weight: 0.9)

**What it means:** Can stakeholders quickly understand the story and rationale?

| Score | Criteria |
|-------|----------|
| 5 | Clear narrative arc: here's where we are, here's where we're going, here's why. |
| 4 | Good clarity with minor confusion points. |
| 3 | Information is there but hard to extract the story. |
| 2 | Just a list without narrative. |
| 1 | Confusing or contradictory. |

### Learning/Measurement Logic (Weight: 0.8)

**What it means:** Does the roadmap show what will be learned or measured along the way?

| Score | Criteria |
|-------|----------|
| 5 | Checkpoints with explicit learning goals: "After M1, we'll know X." |
| 4 | Some learning checkpoints with minor gaps. |
| 3 | Has milestones but no learning goals attached. |
| 2 | Measurement only at the end. |
| 1 | No measurement or learning plan. |

---

## Research Synthesis Dimensions

### Source Quality (Weight: 1.0)

**What it means:** Are sources credible, representative, and current enough for the conclusion?

| Score | Criteria |
|-------|----------|
| 5 | Sources are credible, recent, and representative. Biases acknowledged. |
| 4 | Good sources with minor gaps. |
| 3 | Sources exist but have quality or recency issues. |
| 2 | Sources are weak, biased, or outdated. |
| 1 | No sources or sources are not credible. |

### Evidence Traceability (Weight: 1.1)

**What it means:** Can a reader trace the claims back to specific evidence?

| Score | Criteria |
|-------|----------|
| 5 | Every claim links to specific evidence (quotes, data points, sources). |
| 4 | Good traceability with minor gaps. |
| 3 | Some claims traceable, others asserted without evidence. |
| 2 | Mostly assertions without evidence links. |
| 1 | No traceability. |

### Pattern Validity (Weight: 1.2)

**What it means:** Are patterns real rather than anecdotes or confirmation bias?

| Score | Criteria |
|-------|----------|
| 5 | Patterns appear across multiple sources. Counterexamples acknowledged. |
| 4 | Good patterns with minor issues. |
| 3 | Patterns based on limited data or potential confirmation bias. |
| 2 | Patterns are anecdotes generalized. |
| 1 | No patterns, or patterns contradicted by evidence. |

### Uncertainty Handling (Weight: 0.8)

**What it means:** Does the artifact make confidence and open questions explicit?

| Score | Criteria |
|-------|----------|
| 5 | Explicit confidence levels. Open questions stated. Limitations acknowledged. |
| 4 | Good uncertainty handling with minor gaps. |
| 3 | Some acknowledgment of uncertainty. |
| 2 | Overconfident without acknowledging limitations. |
| 1 | Pretends certainty where none exists. |

### Actionability (Weight: 1.0)

**What it means:** Does the synthesis enable a concrete next decision or action?

| Score | Criteria |
|-------|----------|
| 5 | Ends with explicit decision implications and recommended next steps. |
| 4 | Actionable with minor gaps. |
| 3 | Insights are clear but implications are implied, not stated. |
| 2 | Observations without decision relevance. |
| 1 | No actionability. |

### Decision Relevance (Weight: 0.9)

**What it means:** Is the research framed around a product decision that matters?

| Score | Criteria |
|-------|----------|
| 5 | Research directly addresses a specific product decision. |
| 4 | Relevant with minor gaps. |
| 3 | Tangentially relevant to decisions. |
| 2 | Interesting but not decision-relevant. |
| 1 | No decision relevance. |

---

## Exec Comms Dimensions

### Audience Fit (Weight: 1.1)

**What it means:** Is the message tuned to what this audience actually needs to know?

| Score | Criteria |
|-------|----------|
| 5 | Tailored to audience's concerns, knowledge level, and decision authority. |
| 4 | Good fit with minor issues. |
| 3 | Some audience awareness but not fully tuned. |
| 2 | Generic content not tailored to audience. |
| 1 | Wrong audience entirely. |

### Clarity (Weight: 1.2)

**What it means:** Is the message easy to scan, understand, and act on?

| Score | Criteria |
|-------|----------|
| 5 | Key point and ask visible in first 30 seconds. Structure enables scanning. |
| 4 | Clear with minor confusion points. |
| 3 | Information is there but requires work to extract. |
| 2 | Unclear structure, key points buried. |
| 1 | Confusing or impenetrable. |

### Strategic Framing (Weight: 1.0)

**What it means:** Does it explain why this matters at the right altitude?

| Score | Criteria |
|-------|----------|
| 5 | Connects to strategic context at appropriate altitude for audience. |
| 4 | Good framing with minor gaps. |
| 3 | Some strategic context but weak connection. |
| 2 | Tactical focus without strategic context. |
| 1 | No strategic framing. |

### Trustworthiness (Weight: 1.0)

**What it means:** Are claims precise, balanced, and credible?

| Score | Criteria |
|-------|----------|
| 5 | Claims are specific, sourced, and acknowledge limitations. |
| 4 | Trustworthy with minor issues. |
| 3 | Some vague or unsupported claims. |
| 2 | Overconfident or imprecise claims. |
| 1 | Claims that damage credibility. |

### Ask / Call to Action (Weight: 0.9)

**What it means:** Is the desired response or decision explicit?

| Score | Criteria |
|-------|----------|
| 5 | Explicit ask: "We need X from you by Y." |
| 4 | Ask exists with minor ambiguity. |
| 3 | Implied ask but not explicit. |
| 2 | No ask, or "for information only" without purpose. |
| 1 | Confusing or missing ask. |

### Brevity Discipline (Weight: 0.8)

**What it means:** Is the document concise without hiding critical context?

| Score | Criteria |
|-------|----------|
| 5 | 1-2 pages for exec audience. Every sentence earns its place. |
| 4 | Concise with minor bloat. |
| 3 | Could be shorter without losing meaning. |
| 2 | Clearly too long for audience. |
| 1 | Excessive length that will cause readers to skip. |

---

## Confidence Assessment

### High Confidence

- Artifact is complete (not a fragment)
- Context is sufficient to evaluate all dimensions
- Artifact type is clear
- No unusual format or ambiguity

### Medium Confidence

- Artifact may be partial or draft
- Some context is missing
- Format is unusual but interpretable

### Low Confidence

- Significant ambiguity about artifact type or scope
- Missing critical context
- Unable to assess multiple dimensions fairly

**Rule:** When confidence is low, explicitly state what you cannot assess and why.
