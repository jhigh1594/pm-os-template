# AI-Assisted Analysis Workflow

Source: Caitlin Sullivan, "How to do AI analysis you can actually trust" (Lenny's Newsletter, 2026)

AI output always looks confident — even when it contains fabricated quotes, false insights, and wrong conclusions. These mistakes are invisible until a stakeholder asks a question you can't answer, a decision falls apart three months later, or you realize the "customer evidence" behind a major investment had enormous holes.

Four failure modes break most AI analysis. Each has a reliable fix.

---

## Failure Mode 1: Invented Evidence

### What it looks like
- Completely fabricated quotes (still happens across all major LLMs)
- "Frankenstein quotes" — sentences stitched from multiple sources that sound like the customer but aren't
- Participant IDs and timestamps that look authoritative but point to nothing

### Why it happens
LLMs don't retrieve quotes like a search engine — they *generate* text that is statistically likely given the context. "Verbatim" is ambiguous to a model: exact characters? Can punctuation differ? Where does the quote start and end? The model fills gaps with assumptions you never see.

Triggers that reliably cause mash-up quotes: "max. 100 words," "a punchy representative quote (≤12 words)," or any instruction that trades length for punchiness.

### Fix: Quote selection rules + verification

**Add this to every analysis prompt:**

```
QUOTE SELECTION RULES

- Start where the thought begins, and continue until it ends
- Include reasoning, not just conclusions
- Keep hedges and qualifiers — they signal uncertainty
- Include emotional language when present
- Cite with participant ID and approximate timestamp [P02 ~14:30]
- Do not combine statements from different parts of the interview
- If a quote would exceed 3 sentences, break it into separate quotes
```

**After analysis, run this verification prompt:**

```
QUOTE VERIFICATION

For each quote in the analysis above:
1. Confirm the quote exists verbatim in the source transcript
2. If the quote is a close paraphrase but not exact, flag it and provide the actual wording
3. If the quote cannot be located, mark as NOT FOUND

Output format:
- Quote: [the quote]
- Status: VERIFIED / PARAPHRASE / NOT FOUND
- If paraphrase: Actual wording: [what they said]
- Location: [Participant ID, timestamp, or line number]
```

---

## Failure Mode 2: False or Generic Insights

### What it looks like
Themes that could describe any product in any category:
- "Price is a factor in decisions"
- "People value reliability"
- "Users want more real-time information"

True, probably — but useless for decisions. You can't tell from these whether to invest in a feature, or whether adding it would alienate the customers who chose you for different reasons.

### Why it happens
LLMs default to finding consensus — the patterns that easily rise to the top. They also bring training priors: if the model has seen thousands of churn analyses where "price" is the #1 theme, it weights toward price even when your data doesn't support it.

Survey data compounds this: "It wasn't for me" could mean four completely different things (too expensive, too data-intensive, doesn't fit my workflow, missing a specific feature). Without guidance, AI lumps them all into a generic cluster.

### Fix: Context loading that actually guides interpretation

Context loading requires four specific components — not three lines of background, not four paragraphs of stream-of-consciousness:

**For interviews, add to your analysis prompt:**

```
PROJECT CONTEXT
[What product, what decision is on the table, what type of participants]

BUSINESS GOAL
Determine if [X] would:
(a) [Outcome A]
(b) [Outcome B]
(c) [Outcome C — with conditions]

PRODUCT CONTEXT
Current: [What exists today and its value prop]
Key competitors: [Direct alternatives with screens/features you're comparing against]
Key tension: [The specific trade-off or strategic question]

PARTICIPANT OVERVIEW
All participants are [churned / active / new / trial].
[Any relevant segment data or behavioral profile]
For participant-specific details, see metadata in each file.
```

**For surveys, add data structure context:**

```
DATA STRUCTURE
Column A (response_id): Ignore
Column B (product_tier): "one"/"peak"/"life" — use for segmentation
Column C (response): Customer's voice — primary analysis target
Column D (status): Internal tag — churned or active

INTERPRETATION GUIDANCE
This is an EXIT survey. No current users.
Focus on specificity, segment differences, and whether [feature X] would actually solve the stated need.
Note: Column D coding — 0 = churned, 1 = active
```

If outputs are still generic after context loading, the context wasn't specific enough. Add more detail about the exact decision, where the team is trying to go, and what you already know that you don't want repeated.

---

## Failure Mode 3: Signal That Doesn't Guide Decisions

### What it looks like
AI tells you "22 respondents mentioned wanting a screen." But should you build it? The number can't answer:
- How many of those 22 would truly have been retained by a screen?
- How many said "screen" but meant something a screen alone wouldn't solve?
- Which problems are unrelated to the feature entirely (billing, engagement, competitive loss)?

### Why it happens
LLMs are trained to find patterns and summarize. "Screen" appears 22 times → "screen value is a theme." The model doesn't distinguish between signal that should drive your roadmap and noise that sounds like signal but isn't. Without guidance, it treats all mentions equally.

### Fix: Few-shot calibration

Few-shot calibration means giving the model concrete labeled examples before asking it to analyze your data. Not descriptions of what the labels mean — actual examples with your specific data type, and *why* each label was assigned.

**Structure for any 5-point decision-fit scale:**

```
SOLUTION FIT SCALE (calibrated for [your decision])

1 - [LABEL: Direct fit]: [Specific pain this directly solves]
Example: "[Verbatim quote from your domain]"
Why this is a 1: [Specific friction + direct solution match + what it signals for investment]

2 - [LABEL: Cheaper fix]: [Sounds related but lower-cost solution exists]
Example: "[Verbatim quote]"
Why this is a 2: [Surface complaint but alternative path to solve it without full investment]

3 - [LABEL: Engagement fix needed]: [Stopped using, feature won't change that]
Example: "[Verbatim quote]"
Why this is a 3: [Self-blame or habit framing — feature doesn't address root cause]

4 - [LABEL: Operational fix needed]: [Billing, support, reliability — not features]
Example: "[Verbatim quote]"
Why this is a 4: [Trust/process failure — feature is irrelevant]

5 - [LABEL: Unrelated competitive loss]: [Left for alternative, no complaint about this feature]
Example: "[Verbatim quote]"
Why this is a 5: [No negative language about feature — ecosystem/social/price-driven]
```

Adapt the scale and labels for your decision context: demand for new offers, churn categorization, feature prioritization, or neutral feedback coding all use the same structure.

---

## Failure Mode 4: Contradictory Insights

### What it looks like
The analysis looks great: clean themes, compelling quotes, a summary table ready for the deck. But you never checked whether everything holds together. You never looked for contradictions. You present with confidence, and three weeks later someone asks a question you can't answer.

This is the most common failure mode. Unlike the first three, it happens even when evidence is real and themes are specific — because LLMs don't reconcile contradictions by default. They surface them both as equally valid insights.

### Why it happens
Human expert analysts do multiple passes instinctively. LLMs don't — unless instructed. They produce coherent, helpful responses and flag their own uncertainty only when explicitly asked. The first pass is always a hypothesis. Without a second pass, you're treating a draft as a final answer.

### Fix: Verification pass

Run this as a separate prompt after any analysis:

```
VERIFICATION PASS

Review the analysis above for:

QUOTE VERIFICATION
- Confirm each quote exists verbatim in the source
- Flag any quotes that are paraphrased, combined, or not found

CONTRADICTION CHECK
- For each participant, check if statements at different points conflict
- Look for: stated preferences vs. described behaviors, confidence followed by hedging, strong opinions that soften later in the interview

CONFIDENCE ASSESSMENT
- For any finding based on limited evidence (fewer than 2 independent sources), flag it
- Note participants where the stance is unclear or mixed
- Flag any theme that could apply to almost any product in this category

Output a verification summary with flags and recommended revisions.
```

Running this prompt reliably finds errors — some are major (wrong conclusion), some are minor (slightly overstated quote). Either way, you want to find them before they end up in a deck.

---

## Model Selection

When model choice is available:

| Model | Best for | Trade-off |
|---|---|---|
| **Claude** | Deep analysis, nuanced synthesis | Gives broad coverage; themes need verification that they're all well-evidenced |
| **Gemini** | Highly evidenced themes, grounded patterns | Fewer themes; needs multiple prompts for completeness; stronger for short quotes |
| **ChatGPT** | Final framing, stakeholder communication | Most creative with "verbatim" quotes (unreliable evidence); strong at packaging findings |

**Default recommendation:** Use Claude for analysis. It covers more ground while staying rooted in the data. The trade-off — unfiltered patterns alongside validated ones — is a better starting point than having to prompt repeatedly to get any breadth.

---

## Workflow Summary

1. Load context (project, business goal, product, participants)
2. Add quote selection rules to analysis prompt
3. Run analysis with few-shot calibration if making a scaled judgment
4. Run quote verification prompt
5. Run verification pass (contradiction + confidence check)
6. Produce decision brief from verified, calibrated output

Fifteen minutes of verification now, or six months of building the wrong thing later.
