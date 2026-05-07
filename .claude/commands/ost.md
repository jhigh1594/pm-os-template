---
description: Build an Opportunity Solution Tree to connect outcomes to structured discovery
---

# /ost — Opportunity Solution Tree

**Purpose**: Map Teresa Torres' Opportunity Solution Tree — from a desired outcome to opportunities (unmet needs) to solutions to the assumptions that must be true for each solution to work.

Use this when you need to see the discovery landscape before committing to a direction. The tree keeps the outcome visible and prevents the team from falling in love with a solution before understanding the opportunity space.

---

## Relationship

- **`/ost`** is the structural map layer — use it to see the full space before drilling in
- **`/brainstorm`** is upstream for idea generation — its Problem Statement feeds `/ost --outcome "..."`
- **`/discover`** is the validation layer — run it on a specific branch of the OST to validate individual opportunities
- **`/experiment`** is downstream — OST surfaces the riskiest assumptions; `/experiment` designs tests for them
- **`/spec`** is the terminal output — run after an opportunity branch is validated and a solution chosen
- **`/think`** is for strategic framing — use before `/ost` when the outcome itself is unclear

---

## Command Syntax

```bash
/ost [--outcome "<statement>"] [--depth <1-3>] [--save] [--update]
```

**Arguments**:
- `--outcome "<statement>"`: Seed the tree with a known outcome (skips Step 1)
- `--depth <1-3>`: Build to a specific depth (1=Outcome only, 2=Opportunities, 3=Full tree with solutions and assumptions)
- `--save`: Write the completed tree to `📋 Tasks/ost-YYYY-MM-DD-[topic].md`
- `--update`: Load an existing OST file and resume adding branches

**Examples**:
```bash
/ost                                                      # Interactive — orient and build together
/ost --outcome "Increase ART-level plan confidence"       # Seed with known outcome
/ost --outcome "Reduce time-to-first-value for new users" --depth 2   # Map opportunities only
/ost --save "dependency visibility"                       # Build and save to file
/ost --update "📋 Tasks/ost-2026-04-01-q2-planning.md"          # Resume an existing tree
```

---

## Core Philosophy

Teresa Torres' OST principle: **hold the outcome constant, explore the opportunity space wide, then narrow to solutions.** Most teams jump to the first solution that comes to mind. The tree forces breadth at the opportunity layer before any solution commitment — the goal is to find the *best* opportunity to pursue, not merely *an* opportunity.

The three rules:
1. **Outcomes before opportunities** — never build the tree without a clear, measurable desired outcome
2. **Opportunities before solutions** — generate 3+ opportunities before naming a single solution
3. **Assumptions before experiments** — name what must be true before designing a test

---

## Workflow

### Step 0: Parse Arguments

Extract from the command invocation:
- `--outcome` value (optional — pre-seeds Step 1 if provided)
- `--depth` value (optional — sets build depth target)
- `--save` flag presence
- `--update` file path (optional — resumes an existing OST)

**If `--outcome` is provided:** Acknowledge it, display it at the top of the tree, and proceed directly to Step 2 (Opportunity Layer): "Outcome locked: '[statement]'. Let me map the opportunity space."

**If `--update` is provided:** Read the referenced file, display the current tree state, and ask: "Which branch would you like to expand — opportunities, solutions, or assumptions?"

**If nothing provided:** Proceed to Step 1.

---

### Step 1: Define the Outcome

Ask **one** question:

> "What outcome is the team trying to move? This is the north star for the tree — a metric, behavior change, or customer result you want to achieve.
>
> Examples:
> - 'Increase plan confidence for ARTs after PI Planning'
> - 'Reduce time-to-first-value for new users under 7 days'
> - 'Improve forecast accuracy for portfolio-level capacity'
>
> What's yours?"

**Outcome quality check** — before proceeding, verify the outcome statement has:
- [ ] A direction (increase, reduce, improve, achieve)
- [ ] A subject (who or what changes?)
- [ ] A measurable signal (what would indicate success, even roughly?)

If any element is missing, probe: "How would you know in 90 days whether you achieved that outcome?"

---

### Step 2: Map the Opportunity Layer

**Goal:** Generate a wide opportunity space — all the customer needs, pain points, and desires that, if addressed, could move the outcome.

**Definition:** An opportunity is an unmet customer need — not a solution, not a feature. If it sounds like a feature, push back: "That sounds like a solution. What customer problem or desire is underneath it?"

**Format each opportunity as:**
```
[Customer segment] [context/situation] → [specific pain, need, or desire]
```

**Examples:**
- Release Train Engineers during PI Planning → can't communicate cross-ART dependencies in real time
- Portfolio leaders after a planning cycle → lack confidence that ARTs are working on the highest-priority work
- New team members in Week 1 → don't know how to connect their daily work to team OKRs

**Facilitation:**
Ask for their first opportunity, then push for more:
1. "What else? What other customer need, if addressed, could contribute to this outcome?"
2. "Who else experiences a version of this problem?"
3. "Are there any workarounds customers use today that signal unmet needs?"

**Target:** 4–8 distinct opportunities before proceeding to Step 3.

---

## 🎯 Quality Gate: Opportunity Breadth

**Before mapping solutions:**

> "You've named [N] opportunities. Before we pick one, let's stress-test the map:
>
> 1. **Coverage**: Are there customer segments or workflow stages you haven't addressed yet?
> 2. **Prioritization signal**: Which opportunity, if solved, would have the most impact on the outcome — and what's your evidence?
> 3. **Forced ranking**: If you could only pursue one opportunity this quarter, which one and why?
>
> Your answer shapes which branch we develop next."

_(This is the reasoning step that separates systematic discovery from the "obvious idea." The best opportunity is rarely the loudest one in the room.)_

**After quality gate:** Ask user to nominate 1–2 priority opportunities to develop further. Mark remaining branches as `[Parked]` — they're preserved, not abandoned.

---

### Step 3: Map the Solution Layer

**Goal:** Generate multiple solution concepts for each priority opportunity — don't converge yet.

**Rule:** At least 3 solutions per opportunity. If only one comes to mind, force a constraint: "What's a solution 10x cheaper? What's a solution that requires no engineering? What would a competitor do differently?"

**Format each solution:**
```
Solution: [Name]
Mechanism: [How does it address the opportunity in 1-2 sentences?]
Customer experience: [What does the customer actually do or see?]
Build signal: [Experiment / Feature / Platform change]
```

**Build Signal Legend:**
- **Experiment**: Fast, cheap test — fake door, prototype, concierge MVP
- **Feature**: Targeted capability addition to existing product
- **Platform**: Structural change enabling multiple solutions downstream

For each solution, label the build signal. Experiments should be explored before committing to features or platform changes.

---

### Step 4: Surface Assumptions

**Goal:** For each priority solution, name the assumptions that must be true for it to work and move the outcome.

**Three assumption categories (Teresa Torres):**

| Category | Question | Example |
|----------|----------|---------|
| **Desirability** | Will customers want this? | "RTEs check dependency status more than once per sprint" |
| **Viability** | Does this work for our business? | "This can be delivered without dedicated platform eng time" |
| **Feasibility** | Can we build it? | "Cross-ART dependency data exists and is machine-readable" |

**Format each assumption:**
```
Assumption: [Specific belief that must be true]
Category: Desirability / Viability / Feasibility
Risk if wrong: [What breaks?]
Cheapest test: [How would you verify this with minimal investment?]
Current confidence: High / Medium / Low
```

**Prioritization rule:** Sort assumptions by (Risk if wrong) × (1 / Current confidence). Start testing the highest-risk, lowest-confidence assumptions first.

---

### Step 5: Render the Full Tree

Output the complete OST in a scannable tree format:

```
## Opportunity Solution Tree
**Outcome:** [Outcome statement]
**Date:** [YYYY-MM-DD]

├── 🎯 [Opportunity 1] ⭐ PRIORITY
│   ├── 💡 Solution A — [Mechanism] [Experiment]
│   │   └── ⚠️ Assumption: [Top assumption] — Confidence: Low
│   ├── 💡 Solution B — [Mechanism] [Feature]
│   │   └── ⚠️ Assumption: [Top assumption] — Confidence: Medium
│   └── 💡 Solution C — [Mechanism] [Experiment]
│       └── ✅ Assumption: [Top assumption] — Confidence: High
│
├── 🎯 [Opportunity 2] ⭐ PRIORITY
│   ├── 💡 Solution A — ...
│   └── 💡 Solution B — ...
│
├── [Opportunity 3] [Parked]
├── [Opportunity 4] [Parked]
└── [Opportunity 5] [Parked]

**Recommended next experiment:**
Test: [Assumption name]
Why: [Highest risk × lowest confidence]
Method: [Cheapest test]
```

**Symbols:**
- 🎯 Priority opportunity (actively being pursued)
- 💡 Solution concept
- ⚠️ High-risk assumption (needs testing)
- ✅ Low-risk assumption (sufficient confidence to proceed)
- [Parked] Branch preserved but not being actively developed

---

## Auto-Save Behavior

**Auto-saving to** `📚 Knowledge/Growth/growth-signals-[YYYY-MM].md` — append this OST summary entry now. No prompt needed.

If `--save` was passed: Write full tree to `📋 Tasks/ost-[YYYY-MM-DD]-[slugified-outcome].md`.

---

## Integration with Other Commands

**Entry from:**
- `/think` → "What's the outcome we're trying to move?" feeds directly into `/ost --outcome "..."`
- `/brainstorm` → Problem Statement becomes the seed outcome for OST
- `/discover --phase 1` → Validated opportunity statements map directly into OST opportunity layer

**Exit to:**
- `/discover --problem "[opportunity]"` → Validate the priority opportunity with customer evidence
- `/experiment "[assumption]"` → Design the cheapest test for the highest-risk assumption
- `/spec` → Once an opportunity is validated and a solution selected, spec it out
- `/think` → If the outcome itself is unclear, return upstream to reframe

---

## Constraints

- Don't name solutions before mapping at least 3 opportunities (breadth first)
- Don't build without knowing the outcome — a feature roadmap is not an OST
- Don't park opportunities dismissively — they may be the right answer when the priority opportunity fails
- Don't mistake customer requests for opportunities — "add a Gantt view" is a solution; "can't see what's due this sprint" is an opportunity
- Don't skip assumption mapping — solutions without named assumptions can't be tested
- Keep the outcome fixed for the duration of the tree — if it changes, start a new tree

---

## Rich Contextual Handoff

After completing Step 5 (or when the user signals they're done), output this handoff block with actual values from the session:

```markdown
---
## OST Complete

**What we produced:**
- Outcome: "{verbatim outcome statement}"
- Opportunities mapped: {N} total — {N} priority, {N} parked
- Solutions per priority opportunity: {N} avg
- Assumptions surfaced: {N} total — {N} high-risk (⚠️)
- Recommended experiment: "{assumption name}" — Method: "{cheapest test}"

**Priority branch to develop:**
- Opportunity: "{verbatim opportunity statement — this becomes /discover's problem frame}"
- Solution leading to experiment: "{solution name}"
- Highest-risk assumption: "{assumption that most needs testing}"

**[NEEDS VALIDATION] count:** {N} high-risk assumptions before committing to build

**Next — run this:**
```
/discover --problem "{verbatim opportunity statement}"
```
Carries your priority opportunity into discovery. Claude will use it as the Phase 1 starting frame.

Or, if assumptions need testing first:
```
/experiment "{highest-risk assumption}"
```
---
```

---

**Ready to start?** Tell me what outcome you're trying to move, or use `--outcome "..."` to seed the tree directly.
