# Plan: Probabilistic Thinking Upgrades to Existing Skills

---

## Annie Duke Concepts to Embed

1. **Resulting avoidance** — A good decision can produce a bad outcome; a bad decision can produce a good outcome. Never evaluate decision quality by outcome alone. Judge the process, not the result.

2. **Calibration** — Assign explicit numerical (or banded) confidence to key assumptions. "I believe this" is not a strategy. "I believe this with 70% confidence, and here's what could move it" is.

3. **Pre-mortem / what would have to be true to fail** — Before committing, project forward: if this fails, what went wrong? Forces the PM to distinguish execution risk from assumption risk.

4. **Bet sizing** — How much you invest (time, headcount, sprint capacity) should track your confidence, not your enthusiasm. Overconfidence = over-investment. Calibrate commitment to evidence level.

5. **Epistemic humility** — Explicitly name what you don't know that matters most. The gaps in your model are as important as the model itself.

6. **Bayesian updating** — When new information arrives (customer interview, A/B result, sales loss), update your stated confidence. Don't explain why the new evidence doesn't count.

---

## Skill-by-Skill Upgrade Plan

---

### decision-frameworks

**Gap:** The skill surfaces reversibility, regret, and uncertainty well — but it never asks the PM to state their confidence level in the key assumptions driving the decision, and it has no mechanism to flag "resulting" (judging the decision by outcome). The "provisional call" step commits to a position without calibrating conviction. The pre-mortem in Decision Lenses is listed but not operationalized — it's a label, not a prompt.

**Proposed additions:**

1. In **Default flow**, insert between steps 3 and 4:
   > Surface the PM's stated confidence: "How confident are you (0-100%) that the main assumption driving this decision is correct? What would change that number up or down?"

2. In **Response Contract**, add a calibration line to the `## What Matters Most` block:
   ```
   ## What Matters Most
   - [stakes]
   - [reversibility]
   - [main uncertainty]
   - **Confidence in key assumption:** [X%] — what would move this?
   ```

3. In **Decision Lenses**, replace the single-word "pre-mortem" entry with:
   > Pre-mortem: "If this decision fails 12 months from now, write the two-sentence post-mortem headline. What assumption was wrong? Was the failure foreseeable — or just unlucky? This test separates decision quality from outcome quality."

4. In **Judgment-Building Rule**, add:
   > Distinguish decision quality from outcome quality. A bad outcome doesn't mean the decision was wrong; a good outcome doesn't mean it was right. After high-stakes calls, record the reasoning and confidence at decision time — not after the outcome is known.

5. In **Guardrails**, add:
   > Do not let the PM collapse outcome into decision quality ("it worked, so it was right" / "it failed, so it was wrong").

**Where in the skill file:** Default flow (step insertion), Response Contract template, Decision Lenses section, Judgment-Building Rule, Guardrails.

---

### prioritization-craft

**Gap:** The skill excels at surfacing constraints, tradeoffs, and opportunity cost — but scoring and ranking items carry zero confidence weighting. Every ranked item is treated as equally certain. The PM could rank #1 with high conviction and rank #2 as a pure guess and the output would look identical. There's no prompt to surface "what would have to be true for this ranking to be wrong?" Bet sizing (investment proportional to confidence) is also absent — a 70% confident item and a 90% confident item would receive the same sprint allocation.

**Proposed additions:**

1. In **Provisional Order** of the Response Contract, add confidence annotation:
   ```
   ## Provisional Order
   1. [item] — Confidence: [High/Med/Low or X%] | Key assumption: [what must be true]
   2. [item] — Confidence: [High/Med/Low or X%] | Key assumption: [what must be true]
   3. [item] — Confidence: [High/Med/Low or X%] | Key assumption: [what must be true]
   ```

2. In **Why / Next Step**, add a standard probe after the main tradeoff:
   > "Which item in this ranking are you least confident about? What's the cheapest signal that would let you reorder — a customer interview, a data pull, a spike? Bet size your investment: the lower your confidence, the more you should stage the commitment rather than all-in."

3. In **Prioritization Lenses**, add:
   > confidence / assumption risk — how well-validated is the value hypothesis for this item? High-confidence items can be committed fully; low-confidence items should be staged or time-boxed to preserve optionality.

4. In **Judgment-Building Rule**, add:
   > Surface confidence explicitly — the constraint doing the real work is often not capacity or strategy, but evidence quality. A tie between two items usually means you need a signal, not a framework.

5. In **Guardrails**, add:
   > Do not rank items at equal confidence when evidence quality differs sharply — flag the gap and recommend a validation step before committing capacity.

**Where in the skill file:** Response Contract (Provisional Order + Why/Next Step), Prioritization Lenses, Judgment-Building Rule, Guardrails.

---

### business-reasoning

**Gap:** The financial modeling is solid on mechanism but light on confidence labeling across individual steps of the value chain. The Revenue Impact Pathway assumes all steps are equally certain — but adoption rate, ARR mechanism, and segment size may each carry wildly different confidence levels. The Quality Gate at the bottom asks "at which step is your confidence lowest" — this is good — but the model itself doesn't enforce confidence tagging upstream, so the gate becomes the first time probability enters the conversation. Also: the Go/no-go criteria in the Business Case template are observable thresholds but not stated as bets ("we believe X will happen; if wrong, we stop").

**Proposed additions:**

1. In the **Revenue Impact Pathway**, annotate each step with a confidence prompt:
   ```
   Feature → Adoption rate (% of ICP accounts using it) [Confidence: ?%]
     → Affected account segment [Confidence: ?%]
     → ARR mechanism [Confidence: ?%]
     → ARR impact [Combined confidence: ?%]
   ```
   Add instruction: "Label confidence at each step before multiplying. A 70% × 70% × 70% chain produces ~34% confidence in the output, not 70%. Own that math."

2. In the **Business Case Section Template**, reframe the revenue impact hypothesis as an explicit bet:
   ```
   **Revenue impact hypothesis (stated as a bet):**
   - We believe [X behavior] will happen in [Y accounts] within [Z months].
   - Confidence: [%] — based on [evidence type: interview/data/analogy/assumption]
   - What would change this estimate: [specific new information]
   - Conservative case: [estimate]
   - Expected case: [estimate]
   ```

3. In the **Go/no-go criteria**, add disconfirmation language:
   > Frame criteria as bets, not metrics: "We believe adoption will reach 20% in 90 days. If it doesn't, the assumption about [X] was wrong — stop or pivot. If it does, update confidence and increase investment."

4. In the **Quality Gate: Financial Reasoning**, add one sentence before the existing prompt:
   > "First: state your confidence (0-100%) in the value mechanism you're about to trace. Then trace it. If your confidence in the full chain is below 40%, this is a hypothesis requiring a discovery phase, not a business case."

5. In **Guardrails**, add:
   > Do not compound uncertain estimates without flagging the probability degradation — a chain of assumptions multiplies uncertainty, it doesn't average it.

**Where in the skill file:** Revenue Impact Pathway, Business Case Section Template (revenue hypothesis + go/no-go), Quality Gate (prefix sentence), Guardrails.

---

### coaching-hooks

**Gap:** The 7 archetypes are excellent but probabilistic reasoning has no dedicated archetype — it's distributed as fragments across others. Archetype 1 (Judgment/Tradeoffs) touches opportunity cost but not decision quality vs. outcome quality. Archetype 5 (Financial Reasoning) asks "at what confidence" but only in the value chain trace — not as a standalone calibration prompt. Archetype 7 (Discovery) asks about assumption confidence but frames it as binary (test or not) rather than Bayesian (how does new information update my belief?). There is no hook for resulting avoidance or Bayesian updating anywhere.

**Proposed additions:**

1. **Add a new Archetype 8: Probabilistic Reasoning** — fires in `/decide` and `/prioritize` as a secondary prompt after the primary Archetype 1 prompt, and in `/biz-case` after the financial reasoning gate:

   ```
   ### 8. Probabilistic Reasoning
   **Commands that invoke this:** `/decide` (secondary), `/prioritize` (secondary), `/biz-case` (secondary)
   **PM failure mode (Annie Duke):** Judging decision quality by outcome; treating conviction as confidence; over-investing in poorly-calibrated beliefs; failing to update when new evidence arrives.

   **Prompt A — Calibration and bet sizing** _(use in `/decide` and `/prioritize`)_:
   > "Before you commit: state your confidence in the key assumption driving this decision or ranking — a number, not a feeling. What's the single most important thing you don't know that, if you knew it, would most change your answer? And: are you investing in proportion to your confidence, or in proportion to your enthusiasm?"

   **Prompt B — Resulting avoidance** _(use after /decide outcomes are known)_:
   > "Now that you know the outcome: was this a good decision or a lucky one? Reconstruct what you knew at the time you decided. If you knew then what you know now, would the decision still have been correct? Separate the quality of the reasoning from the quality of the result — otherwise you'll repeat bad processes that happened to work and abandon good processes that happened to fail."

   **Prompt C — Bayesian update trigger** _(use when new data arrives after a decision or ranking)_:
   > "You now have new information. What does it do to your stated confidence? Name a specific number: did your confidence in the original assumption go up or down, and by how much? If the answer is 'the new evidence doesn't really change anything,' explain why — don't let confirming evidence inflate your confidence and disconfirming evidence get explained away."

   **Pattern tags:** `assumption-visibility`, `calibration`, `bayesian-update`
   ```

2. **Update the Pattern tag vocabulary** to add:
   `calibration` | `bayesian-update` | `resulting-avoidance` | `bet-sizing`

3. **In Archetype 1 (Judgment/Tradeoffs)**, add a sentence to the failure mode:
   > Also: confusing outcome quality with decision quality — evaluating whether the call was right based on what happened, rather than what was known at decision time (Annie Duke: "resulting").

4. **In Archetype 7 (Discovery)**, extend Prompt A:
   After "at what confidence level would you stop or pivot?" add:
   > "And: if early signals come back negative, what's your plan for updating your confidence — not explaining away the signal?"

5. **In Implementation Principles**, add item 8:
   > **Calibrate, don't convince** (Annie Duke) — the PM should be able to put a number on their confidence at any decision point. "I'm confident" is not a statement; "I'm 75% confident, and here's what would move it" is. Every coaching prompt that touches uncertainty should push toward a number and a named updating mechanism.

**Where in the skill file:** Add Archetype 8 (after Archetype 7), expand Pattern tag vocabulary, add to Archetype 1 failure mode, extend Archetype 7 Prompt A, add Implementation Principle 8.

---

## Implementation Order

1. **coaching-hooks** — first, because it defines the archetype framework that the other skills reference. Adding Archetype 8 here means subsequent skill edits can point to it rather than each embedding duplicate logic. The pattern tag vocabulary expansion also needs to happen here before it gets referenced downstream.

2. **decision-frameworks** — second, because decisions are the highest-stakes, lowest-volume moments where probabilistic thinking has the most leverage. The pre-mortem operationalization and confidence annotation in the provisional call are quick wins with high signal.

3. **business-reasoning** — third, because the financial value chain is where miscalibrated confidence does the most damage (stacked assumptions compound into false precision). The confidence annotation in the Revenue Impact Pathway is the single highest-leverage edit across all 4 files.

4. **prioritization-craft** — fourth. The confidence annotation in Provisional Order is an easy add, but prioritization sessions are higher-frequency and lower-stakes than the other two — so slightly lower urgency to get exactly right.

---

## What NOT to Add

- **Explicit probability math in prioritization** — forcing PMs to assign numerical probabilities to every backlog item adds cognitive overhead without proportional value. Use confidence bands (High/Med/Low) or a single number only for the top assumption per item, not full expected-value calculations for every row.

- **Full Bayesian notation or formula references** — this is a PM workflow, not a statistics class. The concept is: update your beliefs when new evidence arrives. The label "Bayesian" doesn't need to appear in the skill files; the behavior does.

- **Separate "run pre-mortem" command prompts** — pre-mortem already exists as a Decision Lens label. The upgrade is to operationalize it in place (add the actual question), not add a new command or section.

- **Resulting avoidance as a real-time gate** — the resulting avoidance prompt (Archetype 8, Prompt B) only fires after an outcome is known, not at decision time. Embedding it in the default decision flow would be premature and confusing.

- **Repeating calibration prompts in both decision-frameworks and coaching-hooks** — the coaching-hooks archetype is the source of truth; decision-frameworks adds the annotation to the Response Contract template only. Don't duplicate the full reasoning question in both places.
