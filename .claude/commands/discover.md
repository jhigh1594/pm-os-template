# Product Discovery Workflow

Guide through a structured product discovery process to identify and validate customer problems worth solving.

---

## Relationship

- **`/discover`** is the validation layer between brainstorming and spec-writing
- **`/brainstorm`** is the upstream handoff — its Problem Statement carries into `/discover --problem "..."`
- **`/signal`** feeds atomic customer signals into discovery continuously — reference the signals file when available
- **`/research`** is the sibling command for designing specific validation studies
- **`/synthesize`** is for consolidating 10+ signals into themes — use after discovery, not during
- **`/spec`** is the downstream handoff — run after Phase 4 when Value Risk is validated and evidence confidence is Medium or higher
- Use `/discover` when you need to validate a problem before committing to a PRD investment

---

## Command Syntax

```bash
/discover [--problem "<statement>"] [--phase <1-4>] [--skip-framing] [--mode external]
```

**Arguments**:
- `--problem "<statement>"`: Carry Problem Statement directly from `/brainstorm` handoff (skips opening orientation question)
- `--phase <1-4>`: Jump directly to a specific phase (1=Problem Discovery, 2=Solution Exploration, 3=Risk Validation, 4=MVP Scoping)
- `--skip-framing`: Skip the "where are you in discovery?" orientation question and proceed immediately
- `--mode external`: Activate Buying Committee Mapping (Step 1.5) before Phase 1 — for external customer discovery on new accounts or expansion opportunities

**Examples**:
```bash
/discover                                                    # Interactive mode — oriented entry question
/discover --problem "Portfolio managers can't see OKR impact of blocked cards"
/discover --phase 3                                          # Jump to risk validation
/discover --phase 2 --problem "Card grouping by custom field"
/discover --mode external "AgilePlace expansion at Highmark"  # External discovery with buying committee map
```

---

## Core Philosophy

Follow the **Continuous Discovery** framework: talk to customers weekly, test assumptions continuously, and involve the whole product trio (PM, Designer, Engineer).

---

## Your Approach

### Step 0: Parse Arguments

Extract from the command invocation:
- `--problem` value (optional — pre-fills Phase 1 if provided)
- `--phase` value (optional — jump to specific phase)
- `--skip-framing` flag presence

**If `--problem` is provided:** Acknowledge the Problem Statement, pre-fill it as the Phase 1 starting frame, and proceed directly to Step 2 (Phase 1) with: "Carrying Problem Statement from brainstorm: '[statement]'. Let me ask one question about your evidence before we map the opportunity."

**If `--phase` is provided without `--problem`:** Jump to that phase and ask what context exists from earlier phases.

**If `--mode external` is provided:** Activate **Step 1.5: Buying Committee Mapping** before proceeding to Phase 1.

**If nothing provided:** Proceed to Step 1.

---

### Step 1.5: Buying Committee Mapping (`--mode external` only)

**Trigger:** Activated when `--mode external` is passed. Fires before Phase 1 problem discovery. Not active on standard internal discovery runs.

**Purpose:** Map the five enterprise buying roles at the target account before beginning problem discovery. These roles have different pain points, different success criteria, and different veto power. Discovery that only surfaces the champion's perspective misses the friction points that block deals.

**Map these five roles:**

| Role | Who They Are | Primary Concern | Key Discovery Questions |
|------|-------------|-----------------|------------------------|
| **Economic Buyer** | Person who controls budget and final approval | ROI, strategic fit, risk | "What business outcome justifies this investment?" "What would make you say no?" |
| **Champion** | Internal advocate who will drive adoption | Their credibility, ease of win, user adoption | "What does success look like for you personally?" "What objection are you most worried about?" |
| **IT / Security / Procurement** | Technical gate-keeper and contract manager | Integration, security, compliance, TCO | "What security review process applies?" "What integration requirements exist?" |
| **Daily User** | The person using the product daily (RTE, ART lead, PM) | Workflow fit, learning curve, reliability | "What does your current process look like?" "What workarounds do you use today?" |
| **Exec Sponsor** | Executive whose team or strategy this supports | Strategic alignment, visibility, accountability | "What does your exec want to see in 90 days?" "Who else needs to support this?" |

**For each role, assess:**

```
**[Role]: [Name or "Unknown" if not identified]**
- Position: [Supporter / Neutral / Skeptic / Unknown]
- Primary concern: [What they most care about]
- Discovery gap: [What we don't yet know about them]
- Access: [Do we have direct access? Who can get us there?]
```

**Output feeds:**
- Phase 1 customer interviews: prioritize roles where position = Unknown or Skeptic
- `/signal --source sales` for any insights captured during mapping
- `/prep` champion briefing when champion role is identified
- `/spec` stakeholder sections when solution moves to build

**After completing the buying committee map, proceed to Step 1 (Orient Entry Point) → Phase 1.**

**Standard `/discover` (without `--mode external`):** This step does not fire. No change to existing flow.

---

### Step 1: Orient Entry Point

Before any framework, ask **one** question:

> "Where are you in discovery right now?
>
> **(a)** Vague idea — need to validate whether this problem is real
> **(b)** Talked to customers — have problem evidence, need to explore solutions
> **(c)** Have a solution concept — need to validate the four risks
> **(d)** Ready to scope the MVP — need to define in/out"

Map answer to entry phase:
- **(a)** → Phase 1: Problem Discovery
- **(b)** → Phase 2: Solution Exploration (with evidence summary first)
- **(c)** → Phase 3: Risk Validation
- **(d)** → Phase 4: Scoping & Sequencing

If the user provides context that makes the answer obvious, infer the entry point and state it: "Based on what you've shared, it sounds like you're at Phase 2. Let's map what you've learned and explore solutions."

---

### Step 2: Phase 1 — Problem Discovery

**Goal:** Identify a real customer problem worth solving, backed by evidence.

**Activities:**

**Customer Interviews** (JTBD-focused):
- "Tell me about the last time you [did relevant activity]"
- "What were you trying to accomplish?"
- "Why was that important?"
- "What made that hard/frustrating?"
- "What did you try instead?"

**Opportunity Mapping:**
- Map the customer journey
- Identify pain points and friction
- Quantify frequency and severity
- Look for workarounds (signals of unmet needs)

**Data Analysis:**
- Support tickets and feature requests (what are customers complaining about?)
- Analytics (where are customers dropping off?)
- User testing (where do customers get stuck?)
- `/signal` captures (check `📚 Knowledge/Research/signals-YYYY-MM.md` for relevant nuggets)

**Opportunity Sizing** (TAM/SAM/SOM — rough order of magnitude):
- **TAM**: All customers globally with this job-to-be-done
- **SAM**: Customers reachable given product scope, geography, and GTM model
- **SOM**: Realistic capture in 1-3 years given competition and current resources
- Use ROM estimates only — precision is false confidence at discovery stage
- Decision gate: If SOM is below the company's minimum investment threshold, surface this explicitly before proceeding to Phase 2. Deprioritize regardless of qualitative excitement.

**Output: Opportunity Statement**
```
For [target customer]
Who [context/situation]
The problem is [specific pain point]
Which impacts them by [consequence/cost]
Unlike [current workarounds/alternatives]
Our insight is [what we learned that others missed]
```

**Evidence Confidence Assessment** (REQUIRED before moving to Phase 2):

After drafting the Opportunity Statement, score the evidence:

```
**Evidence assessment:**
- Confidence: [High = 5+ ICP interviews or strong quantitative data / Medium = 2-4 interviews or mixed data / Low = 0-1 interviews or assumption-only]
- Sources consulted: [list: interviews, analytics, support tickets, signal file, etc.]
- Value Risk status: [Validated = customers confirmed they have this problem and it matters / Uncertain = mixed signals / Not yet tested = no direct validation]
```

**Phase 1 complete?** Check before advancing:
- [ ] Opportunity Statement drafted
- [ ] Evidence confidence scored
- [ ] SOM sizing done (even rough)
- [ ] Workarounds/alternatives identified

Advance to Phase 2 when all items are checked or the user explicitly requests to proceed.

---

### Step 3: Phase 2 — Solution Exploration

**Goal:** Generate multiple possible solutions, not just the first idea.

**Activities:**

**Working Backwards:** Start from perfect customer experience, work back to MVP

**Sketching Multiple Concepts:** Force at least 3 different approaches before converging

**Apply Mental Models:**
- Solve the whole customer experience (not just the feature)
- Experiment/Feature/Platform (what type of build is this?)
- Confidence → Speed/Quality (how confident are we? How fast should we move?)

**Output: Solution Concepts** (at least 3 different approaches)

For each concept, capture:
- Approach name
- Core mechanism (how does it solve the problem?)
- Key assumptions this concept relies on
- Estimated risk level: Value / Usability / Feasibility / Viability

**Phase 2 complete?** Check before advancing:
- [ ] 3+ solution concepts generated
- [ ] Key assumptions per concept identified
- [ ] Rough risk assessment per concept done

Advance to Phase 3 when all items are checked.

---

### Step 4: Phase 3 — Risk Validation

**Goal:** Validate the Four Risks before committing to build.

**The Four Risks:**

**1. Value Risk (HIGHEST PRIORITY):** Will customers find this valuable?
- Test: Prototype testing, fake door tests, landing pages
- Question: "Would you use this? Why/why not?"

**2. Usability Risk:** Can customers figure out how to use it?
- Test: Prototype walkthroughs, task-based testing
- Question: "Can you show me how you'd [accomplish task]?"

**3. Feasibility Risk:** Can we build this?
- Test: Technical spike, proof of concept
- Question: "What would it take to build this?"

**4. Viability Risk:** Does this work for our business?
- Test: Pricing research, unit economics, strategic fit
- Question: "Will customers pay? Does this fit our strategy?"

**ALWAYS validate Value Risk first.** Don't spend time on usability/feasibility/viability if customers don't want it.

**Output: Validation Summary**
- Value Risk: ✅ Validated / ⚠️ Uncertain / ❌ Invalid
- Usability Risk: ✅ / ⚠️ / ❌
- Feasibility Risk: ✅ / ⚠️ / ❌
- Viability Risk: ✅ / ⚠️ / ❌

**AI Feature Extension (fires automatically when solution concept involves AI/ML behavior):**

If the solution concept in Phase 2 involves AI recommendations, generated content, NLP, predictions, probabilistic outputs, or any non-deterministic behavior — add the following block to the Validation Summary:

Load `📚 Knowledge/Frameworks/ai-product-risks.md` and run all four dimensions as an additional validation layer.

```
**AI Risk Extension — [Solution Concept Name]**

Risk 1 — Probabilistic Behavior: ✅ / ⚠️ Needs definition / ❌ Not addressed
Risk 2 — Training Data Quality: ✅ / ⚠️ Needs definition / ❌ Not addressed
Risk 3 — Explainability & Override: ✅ / ⚠️ Needs definition / ❌ Not addressed
Risk 4 — Viability, Ethics, Legal: ✅ / ⚠️ Needs definition / ❌ Not addressed

Highest AI risk dimension: [1 / 2 / 3 / 4]
Primary constraint: [One sentence on what must be resolved before build]
```

Any ⚠️ or ❌ in the AI Risk Extension must be resolved or explicitly deferred before proceeding to Phase 4. These become open questions in `/spec` if the feature advances.

**Decision:** Ship / Pivot / Kill

**Phase 3 complete?** Check before advancing:
- [ ] Value Risk status determined (must be Validated or explicitly accepted as Uncertain)
- [ ] Remaining three risks assessed (even if not fully validated)
- [ ] Ship/Pivot/Kill decision made

---

### Step 5: Phase 4 — Scoping & Sequencing

**Goal:** Define the minimum complete product that solves the customer problem.

**Principles:**
- **Version Two is a Lie:** Don't count on iteration; make V1 complete
- **Time Value of Shipping:** Ship sooner if valuable
- **Working Backwards:** Start from ideal experience, cut to minimum complete

**Activities:**
1. Define "done" for the customer (what's the minimum complete solution?)
2. Apply Kano Model:
   - Must-haves (Basic needs — if missing, customers won't use it)
   - Performance features (Satisfiers — more is better)
   - Delighters (Exciters — unexpected wow)
3. Sequence from must-haves → performance → delighters

**Output: MVP Definition**
```
## Customer Problem
[One sentence: what problem are we solving?]

## Success Criteria
- Leading metric: [usage/adoption metric]
- Lagging metric: [business outcome metric]
- Customer satisfaction: [qualitative bar]

## In Scope (V1)
- [Must-have 1]
- [Must-have 2]
- [Must-have 3]

## Out of Scope (Future)
- [Feature that can wait]
- [Nice-to-have]

## Open Questions
- [What we still need to figure out]
```

---

## Discovery Artifacts I Can Help Create

1. **Opportunity Statement**: Problem definition with customer context
2. **Interview Scripts**: JTBD-focused questions for customer conversations
3. **Prototype Test Plan**: How to validate solution concepts
4. **Risk Validation Plan**: Testing the Four Risks systematically
5. **MVP Scoping Doc**: What's in/out for first version
6. **Discovery Summary**: One-pager capturing problem, solution, validation, scope

---

## Constraints

- Don't skip talking to customers (PMs don't have the answers, customers do)
- Don't fall in love with your first solution (generate at least 3 alternatives)
- Don't build before validating value risk (most expensive mistake)
- Don't confuse customer requests with customer problems
- Don't do discovery once at the start (continuous discovery = talk to customers weekly)
- Don't discover alone (involve your designer and tech lead)
- Don't analyze forever (after 5-8 interviews, diminishing returns — ship something small and learn)

---

## Mental Models Applied

- **Four Risks**: Systematic framework for validating assumptions
- **Time Value of Shipping**: Bias toward learning fast with small experiments
- **Working Backwards**: Start from perfect, scope down to minimal complete
- **Confidence → Speed/Quality**: Low confidence = cheap experiments before expensive builds
- **Version Two is a Lie**: Make V1 complete enough to be useful forever
- **Expected Value**: Discovery reduces uncertainty, improving our odds of success

---

## Integration with Other Commands

- Use **/brainstorm** (or `--problem` arg) to carry the problem frame into discovery
- Use **/signal** to capture customer signals continuously between sessions
- Use **/research** for designing specific validation studies (interviews, prototypes)
- Use **/synthesize** when you have 10+ signals ready to consolidate into themes
- Use **/think** for strategic problem framing
- Use **/spec** once Value Risk is validated and evidence confidence is Medium or higher
- Use **/decide** when choosing between multiple solution approaches

---

## Rich Contextual Handoff

After completing Phase 4 (MVP Scoping), output this handoff block with actual values from the session:

```markdown
---
## Discovery Complete

**What we produced:**
- Validated Opportunity Statement: "{verbatim Opportunity Statement from Phase 1}"
- Evidence confidence: {High/Medium/Low} — {N interviews, Y data points}
- Opportunity sizing: TAM ~{X}, SAM ~{Y}, SOM ~{Z}
- Personas confirmed: {list persona names}
- Riskiest assumption: "{assumption from Phase 3 risk validation}"
- MVP scope: "{minimum shippable definition from Phase 4}"

**SVPG Four Risks:**
- Value: {Validated / Uncertain / Not yet tested — with reason}
- Usability: {Addressed / Open}
- Feasibility: {Addressed / Open}
- Viability: {Addressed / Open}

**[NEEDS INPUT] count:** {N} open risks or validation gaps before committing to full PRD

**Next:**
```

If Value Risk is **Validated** and evidence confidence is **Medium or High**:
```
/spec --type one-pager --save "{Feature Name}"
```
Document the solution hypothesis as a one-pager for stakeholder alignment before committing to a full PRD investment.

If Value Risk is **Uncertain** or evidence confidence is **Low**:
```
⚠️ Evidence gate: Value Risk is not yet validated. Recommend 2-3 customer
conversations before committing to a PRD. Use /research to design the study.

/research "{Feature Name} — validate value risk with {N} ICP customers"
```

---
```

---

**Ready to start?** Tell me where you are in discovery, or use `--problem "..."` to carry a problem statement in from `/brainstorm`.
