---
name: coaching-hooks
description: Central framework for embedded coaching quality gates. Reference this skill to understand which archetype fires at each command, the quality gate format, growth signal schema, and implementation principles. Commands and skills invoke specific archetypes from here — do not hardcode prompts in command files.
---

# Coaching Hooks Framework

Embedded coaching quality gates for the 7 high-judgment AIPMOS commands and 4 analytical skills. Each gate is a required reasoning step that simultaneously improves the current output AND generates a growth signal.

**Design principle (Option C):** The reflection IS the final step of the work — not a learning add-on. Every prompt fires at the commit point, not retrospectively.

---

## Quality Gate Format (Standard Pattern)

Use this structure in every command/skill that invokes a coaching hook:

```markdown
---
## 🎯 Quality Gate: [Archetype Name]

**Before we lock this in:**

> [Archetype-specific prompt below]

_(This is the reasoning step that separates a good [output] from a great one.)_

**Auto-saving to** `📚 Knowledge/Growth/growth-signals-[YYYY-MM].md` — append this entry now. No prompt needed.
```

---

## Growth Signal Output Schema

Each gate response is auto-saved as one entry in the monthly accumulation file (no user confirmation required):

```
---
- Date: YYYY-MM-DD
- Context: [command or skill name] — [brief task description]
- Archetype: [see archetype list below]
- Prompt: [the specific question asked]
- Response: [PM's answer, 1-3 sentences]
- Pattern tag: [single tag from vocabulary below]
```

**Pattern tag vocabulary:**
`assumption-visibility` | `strategy-coherence` | `option-diversity` | `problem-grounding` | `evidence-quality` | `bar-raising` | `opportunity-cost` | `value-mechanism` | `signal-interpretation` | `differentiation-logic` | `story-vs-opinion` | `sequencing-logic`

**Accumulation target:** `📚 Knowledge/Growth/growth-signals-[YYYY-MM].md`

**Synthesis cadence:** `/weekly-review` Step 1.5 reads this file and surfaces pattern clusters.

---

## The 7 Coaching Archetypes

### 1. Judgment / Tradeoffs
**Commands that invoke this:** `/decide`, `/prioritize`
**PM failure mode (Ravi Mehta, Reforge strategy stack):** Choosing between A and B without articulating the strategy principle that makes one better — treating prioritization as math when it's strategy.

**Prompt A — Strategy coherence probe** _(use in `/decide`)_:
> "The choice you just made implies something about your product strategy. What does choosing this over the alternative say about what you believe drives value for customers? If someone read only your prioritization decisions for the last quarter, what strategy would they infer?"

**Prompt B — Opportunity cost excavation** _(use in `/prioritize`)_ _(Marty Cagan, SVPG)_:
> "What is this decision saying no to — not just the alternatives you considered, but the types of problems and customers you're de-prioritizing by going in this direction? Who loses in this tradeoff, and is that the right call?"

**Pattern tags:** `strategy-coherence`, `opportunity-cost`

---

### 2. Generative Thinking
**Commands that invoke this:** `/brainstorm`
**PM failure mode (Teresa Torres):** Jumping to a preferred solution before the problem space is properly structured; generating one option and falling in love with it.

**Prompt A — Problem space grounding:**
> "Before evaluating this solution direction: can you describe one real person in one specific moment where this problem occurs? What are they feeling, what have they tried, what does the friction cost them? If you can't tell that story, you may be solving for a solution you prefer rather than a problem customers have."

**Prompt B — Option diversity test** _(use in `/brainstorm`)_:
> "How many distinct approaches did you consider? Name two meaningfully different alternatives to the direction you've chosen, and what would you need to believe to prefer each over your current choice?"

**Pattern tags:** `problem-grounding`, `option-diversity`

---

### 3. Strategic Framing
**Commands/skills that invoke this:** `/think`, `strategic-thinking` skill
**PM failure mode (Ravi Mehta, strategy stack):** Confusing a feature list for a strategy sequence; not articulating why *this order* of bets creates compounding value.

**Prompt A — Stack coherence test** _(use in `/think`)_:
> "Walk the strategy stack from the top: company mission → product strategy → this roadmap/decision. At which layer does the chain feel weakest or unconnected? If any layer is missing, you may be sequencing features rather than building toward something."

**Prompt B — Sequencing logic probe** _(use in `strategic-thinking` skill)_:
> "Why does this order create leverage that a different order would not? What does each step unlock — capability, learning, or market position — that makes the next step possible? If the answer is 'we start with the most important thing,' you've described a to-do list, not a strategy."

**Pattern tags:** `strategy-coherence`, `sequencing-logic`

---

### 4. Evaluative Judgment
**Commands/skills that invoke this:** `/critique`, `ai-product-patterns` skill
**PM failure mode (Cagan + scorecard-presets):** Reviewing for completeness rather than quality; accepting weak evidence without naming the gap; no clear mental model of what excellent looks like.

**Prompt A — Evidence vs. assertion test** _(use in `ai-product-patterns`)_:
> "For the three strongest claims in what you just reviewed: which are evidence (data/direct observation), which are inferences (conclusions drawn from evidence), and which are assertions (believed without traceable support)? Which category does most of the important work?"

**Prompt B — Bar-raising question** _(use in `/critique`)_:
> "What would this look like if it were genuinely excellent, not just adequate? Name one specific change that moves this from 'good enough' to 'something the team would be proud of in a year.' If you can't name it, you may not have a clear enough mental model of excellent in this domain."

**Pattern tags:** `evidence-quality`, `bar-raising`

---

### 5. Financial Reasoning
**Commands/skills that invoke this:** `/price-intel`, `business-reasoning` skill
**PM failure mode (Ravi Mehta, business outcomes competency):** Measuring delivery rather than business outcomes; not tracing the mechanism by which a feature creates financial value; treating an ARR number as a business case.

**Prompt A — Value mechanism trace** _(primary, use in both)_:
> "Trace the financial logic explicitly: this feature/decision → what customer behavior changes → what metric moves → what revenue or cost impact follows → over what time horizon → at what confidence. At which step is your confidence lowest, and what would increase it? If you can't trace it, you have a feature, not an investment."

**Prompt B — Opportunity cost sizing:**
> "What are you implicitly choosing not to invest in? Express the opportunity cost in the same currency as the investment — not in abstract terms, but what else could have been built or bought with this time and money. Is this still the highest-expected-value use of these resources?"

**Pattern tags:** `value-mechanism`, `opportunity-cost`

---

### 6. Competitive Intelligence
**Commands that invoke this:** `/price-intel` (secondary prompt)
**PM failure mode (Ravi Mehta, Tinder/Hinge example):** Describing what competitors do without articulating what it means for your strategy; treating feature parity as the goal; mistaking competitor moves for directives.

**Prompt A — Signal interpretation:**
> "What does this competitor move tell you about what they believe about the market — their theory of who wins and why? Is their theory correct? If so, what does that mean for your strategy? If not, where are they wrong, and what does your strategy exploit that they're ignoring?"

**Prompt B — Differentiation stress test:**
> "If a customer asked why they should choose your product over this competitor's, what would you say that isn't a feature comparison? What is the underlying value bet your product makes that the competitor isn't? If your differentiation argument is 'we do what they do but better,' you're in a features race."

**Pattern tags:** `signal-interpretation`, `differentiation-logic`

---

### 7. Discovery / Assumption Testing
**Commands/skills that invoke this:** `/discover` (Phase 1 exit gate), `continuous-discovery` skill
**PM failure mode (Teresa Torres):** Building without surfacing assumptions; treating conviction as validated learning; asking customers what to build rather than testing what needs to be true.

**Prompt A — Assumption log excavation** _(use in `/discover` Phase 1 exit)_:
> "Before this moves to Phase 2: name the three highest-risk assumptions — not technical risks, but customer behavior assumptions. For each: how confident are you it's true, what is the cheapest test that would change your confidence, and at what confidence level would you stop or pivot?"

**Prompt B — Story vs. opinion diagnostic** _(use in `continuous-discovery`)_:
> "Is the customer insight behind this based on stories — specific customers, specific moments, specific behaviors you observed — or on opinions — things customers told you they want when asked directly? Opinions are fast to collect and unreliable. Stories are slow to collect and durable. Which type of evidence is this built on, and what would it take to upgrade the weakest evidence?"

**Pattern tags:** `assumption-visibility`, `story-vs-opinion`

---

## Implementation Principles

From Ravi Mehta (Reforge), Teresa Torres (Continuous Discovery Habits), Marty Cagan (SVPG/EMPOWERED), and Ericsson deliberate practice:

1. **Fire at the decision point, not retrospectively** — the teachable moment is when the PM is committing, not after the artifact is shipped
2. **Ask questions, don't answer them** (Cagan) — every prompt ends with a question, not a recommendation; the PM must produce the reasoning
3. **Name the failure mode, not the person** (Ravi, scorecard-presets) — frame around reasoning error patterns, not PM judgment
4. **One specific thing** (Ericsson) — each prompt targets one reasoning micro-skill; "be more strategic" is not a coaching prompt
5. **Build mental representation** (product-sense.md) — the prompt should help the PM calibrate against what excellent looks like, not just catch mistakes
6. **Prediction → outcome feedback loop** (Ericsson + Torres) — assumption logging in `/discover` creates the PM equivalent of Ericsson's feedback loop
7. **Be archetype-aware** (Ravi Mehta) — growth PMs and discovery PMs need different coaching emphasis; the archetype must match the reasoning being exercised

---

## How Commands Reference This Skill

Each command or skill that invokes a coaching hook includes a closing section formatted as:

```markdown
---
## 🎯 Quality Gate: [Archetype Name]

**Before we lock this in:**

> "[Paste the exact prompt from the archetype above]"

_(This is the reasoning step that separates a good [output type] from a great one.)_

**Auto-saving to** `📚 Knowledge/Growth/growth-signals-[YYYY-MM].md` — append this entry now. No prompt needed.
```

The prompt text lives in this file — commands reference the archetype, not the prompt text. When the coaching philosophy evolves, edit this file; all commands benefit automatically.

---

## Self-Learning

This file is human-owned. When coaching prompts are refined based on PM feedback or new PM frameworks, update the archetype prompts here rather than in individual command files. The LEARNED.md pattern does not apply to this framework skill — changes are intentional and deliberate.
