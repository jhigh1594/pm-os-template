---
name: user-research-analyst
description: This skill should be used when analyzing user research data (transcripts,
  survey responses, call notes) to produce decision-grade insights for B2B product
  decisions. Trigger phrases include "analyze these interviews", "what patterns do
  you see in this data", "synthesize this research", "help me understand what customers
  are saying", "I have call notes or transcripts", "verify this research analysis",
  "design an interview guide", "what do my users actually want", and "I need to present
  research findings".
---

# User Research Analyst

## Overview

Turn raw customer data into insights you can defend.

This skill bridges the gap between raw interview transcripts, survey responses, and call notes on one side — and decision-grade insights on the other. It enforces rigor at every step: verbatim evidence, disconfirming data, and interpretive positions you could stand behind in a product review.

Use this skill when the work requires turning messy customer data into a specific product or investment decision — not when the goal is to build personas or journey map artifacts (use `/research-users` for that).

## Use This Skill When

Use this skill for any of the following:

- **Analyze** — paste transcripts, survey responses, or call notes; receive a verified decision brief
- **Design** — build a JTBD-clean interview guide or study plan for upcoming research
- **Synthesize** — upgrade a set of findings to insights; produce an interpretive position
- **Verify** — run a verification pass on existing AI-generated analysis to catch fabricated quotes, generic themes, and contradictions

Do not use this skill for:
- Building personas, segments, or journey maps from research artifacts — use `/research-users`
- Designing A/B tests or quantitative experiments — use `/exp-driven-dev`
- Planning what research to do or which assumption is riskiest — use `/discovery`
- Establishing a weekly touchpoint cadence — use `/continuous-discovery`

## Core Idea

**Findings describe what happened. Insights explain what it means and what to do.**

"Six of ten participants mentioned pricing" is a finding. "The pricing objection is a proxy for value uncertainty — buyers don't believe the product will change their workflow, and they're using price as an exit rather than the real reason" is an insight. Only the insight drives a decision.

Three principles that govern this skill:

1. **Evidence must be verbatim, contextual, and sourced.** No paraphrase. No mash-ups. Every claim traces to an exact quote with participant ID and timestamp.

2. **Every insight carries a directional implication.** If the output doesn't tell you what to build, stop, or investigate next — it is a summary, not an insight.

3. **Disconfirmation is not optional.** A brief that only shows supporting evidence is a bias report, not research. At least one finding must cut against the primary insights.

## Default Workflow

Follow these steps unless the mode (analyze / design / synthesize / verify) suggests a shortcut.

### Step 1: Context load (required before any analysis)

Before touching the data, ask three questions:

1. "What decision is this research trying to inform?" (name the specific trade-off or choice)
2. "What do you currently believe is true?" (surfaces the hypothesis to stress-test)
3. "What would change your mind?" (defines the evidence threshold)

If context has already been provided, confirm the decision before proceeding. Do not skip context loading — it is what separates decision-grade analysis from topic summaries.

### Step 2: Quote selection rules

Add these rules to every analysis prompt before sending data to an LLM:

- Start where the thought begins, and continue until it ends
- Include reasoning, not just conclusions
- Keep hedges and qualifiers — they signal uncertainty
- Include emotional language when present
- Cite with participant ID and approximate timestamp [P02 ~14:30]
- Do not combine statements from different parts of the interview
- If a quote would exceed 3 sentences, break it into separate quotes

See `references/analysis_workflow.md` for the complete prompt snippet and quote verification prompt.

### Step 3: Calibrated pattern extraction

Before labeling or categorizing participant responses, provide the model with:
- The decision context (from Step 1)
- 2–3 labeled examples of what a strong vs. weak signal looks like for this specific decision
- Explicit instruction to flag responses that could apply to any product in the category as "generic — do not include"

See `references/analysis_workflow.md` for the few-shot calibration structure.

### Step 4: Finding → insight upgrade

For each pattern identified:
1. State what was observed (the finding)
2. Explain why it happens (the mechanism)
3. Name what it means for the decision (the implication)
4. State what to do differently (the direction)

A pattern that stops at step 1 is not an insight. See `references/insight_synthesis.md` for the full Braun & Clarke 3-stage synthesis and the "so what?" ladder.

### Step 5: Verification pass

After generating analysis, run a separate verification pass:

```
VERIFICATION PASS

Review the analysis above for:

QUOTE VERIFICATION
- Confirm each quote exists verbatim in the source
- Flag any quotes that are paraphrased, combined, or not found

CONTRADICTION CHECK
- For each participant, check if statements at different points conflict
- Look for: stated preferences vs. described behaviors, confidence followed by hedging

CONFIDENCE ASSESSMENT
- For any finding based on fewer than 2 independent sources, flag it
- Flag any theme that could apply to almost any product in this category

Output a verification summary with flags and recommended revisions.
```

### Step 6: Decision brief output

Produce a 1-page brief using the template in `references/decision_brief_template.md`.

Required sections: decision framed, 2–4 insights with verbatim evidence, disconfirming evidence, confidence assessment, recommended action, open questions.

## Mode Selector

| Mode | When to use | Skip to |
|---|---|---|
| **Analyze** | You have raw transcripts or survey data | Step 1 (context load) |
| **Design** | You need an interview guide before research | `references/interview_design.md` directly |
| **Synthesize** | You have a set of findings; need insights | Step 4 (insight upgrade) |
| **Verify** | You have existing AI analysis; need a rigor check | Step 5 (verification pass) |

## Output Contract

Always produce, when sufficient data exists:

- Decision framed in 1–2 sentences
- 2–4 insights with verbatim evidence (participant ID + timestamp)
- At least 1 disconfirming finding
- Confidence assessment (strong / provisional / thin per insight)
- Recommended action with direction
- 1–2 open questions

If data is thin (fewer than 5 participants), produce:
- Provisional hypotheses, not conclusions
- Explicit confidence flags on every statement
- Recommended follow-up research to strengthen the thinnest claims

## Guardrails

Do not:
- Analyze without first establishing what decision the research informs
- Use paraphrased quotes — only verbatim with source
- Produce generic themes that could apply to any product ("price matters," "users want speed")
- Present all evidence as equally confident — distinguish strong from thin
- Skip disconfirming evidence
- Produce a research summary when a decision brief was needed
- Treat stated preferences as equivalent to past behavior
- Let a single source carry an insight

## Bundled Resources

### References (load as needed)

- `references/analysis_workflow.md` — Sullivan's 4 failure modes with exact prompt snippets for quote rules, context loading, few-shot calibration, and verification pass
- `references/interview_design.md` — JTBD switch interview structure, 4 Forces of Progress, Mom Test checklist, Portigal probing techniques
- `references/insight_synthesis.md` — finding→insight upgrade, Braun & Clarke 3-stage synthesis, "so what?" ladder, rigor checklist
- `references/anti_patterns.md` — what 10X researchers actively avoid, organized by failure and fix
- `references/decision_brief_template.md` — 1-page brief template with section guidance

### Assets

- `assets/interview-log.csv` — copy when capturing interviews for synthesis; columns: participant ID, date, segment, status, timestamp, verbatim quote, theme tag, forces mapped, insight vs. finding flag

## Handoff

When the analysis is complete and the decision brief is done — if the next step is building personas, segments, or journey maps from the validated insights: run `/research-users`.

## Self-Learning

Before responding, read `LEARNED.md` in this skill directory when it exists and treat it as compact runtime guidance that sharpens this skill.

Rules for self-improvement:
- Keep `SKILL.md` human-owned; do not rewrite it directly from normal usage.
- Only promote specific, reusable, evidence-backed lessons into `LEARNED.md`.
