# Demo Prep

Generate a customer-ready demo guide for a specific product, persona, and scenario. Translates deep product knowledge into a structured narrative with a clear story arc, feature spotlights, competitive awareness, discovery questions, and traps to avoid.

---

## Relationship

- **`/demo-prep`** is the output layer — takes background knowledge and formats it as a ready-to-use guide
- **`/product-depth --mode demo`** builds the underlying expertise that `/demo-prep` draws from — run first if product context is >30 days old
- **`/prep`** is the strategic meeting layer (attendees, goals, stakes) — pair with `/demo-prep` before high-stakes demos
- **`/granola`** post-meeting captures what worked, what didn't, and new signals — route back to `/signal` immediately after
- **`/product-depth --mode changelog`** should be run before demos if the PM hasn't reviewed product changes in 30+ days

---

## Core Philosophy

**A demo is a narrative, not a tour.**

The fatal flaw: walking through features in the order they appear in the UI, then asking "any questions?" A demo organized around feature menus creates a "that's nice" reaction. A demo organized around the customer's problem creates an "I need this" reaction.

Three things that make a demo land:
1. **Problem first** — the customer recognizes their world before seeing the product
2. **Aha moment first** — design the demo path backward from the most compelling moment
3. **Conversation, not presentation** — discovery questions woven throughout, not saved for the end

The guide generated here is a structure to internalize, not a script to read. The PM should know it well enough to navigate away from it when a customer takes the conversation somewhere unexpected.

---

## Command Syntax

```bash
/demo-prep [--product <name>] [--persona <type>] [--duration <minutes>] [<scenario>]
```

**Arguments**:
- `--product`: `agileplace | okrs | roadmaps | dpd | platform` — if omitted, inferred from scenario or asked
- `--persona`: Target persona type (e.g., `rte | scrum-master | cto | vp-engineering | agile-coach | coo`) — optional; affects which use cases and aha moments to prioritize
- `--duration`: Total demo time in minutes (default: 30) — affects how many features to spotlight and how much to time-box
- `<scenario>`: The demo context — what kind of customer, what they're evaluating, what they've already seen

**Examples**:
```bash
/demo-prep --product agileplace --persona rte --duration 30
/demo-prep --product agileplace --persona cto --duration 45 "enterprise RTE evaluating capacity planning and dependency management"
/demo-prep --product okrs --duration 20 "CS renewal call with champion who hasn't driven exec adoption"
/demo-prep --product roadmaps --persona coo --duration 30 "first demo to portfolio team, strategic alignment angle"
```

---

## Your Approach

### Step 0: Parse Arguments and Check Product Currency

Extract product, persona, duration, and scenario.

**Product context check**: Before generating the guide, check `📦 Products/[product]/product-context/` file modification dates.
- If any ICP or persona file is >60 days old: "⚠️ Product context files for [product] are [N days] old. This guide will be based on the most recent documentation available, but may not reflect recent product changes. Consider running `/product-depth --mode changelog --product [product]` before a high-stakes demo."
- If persona specified but no matching persona file exists: note it and use ICP file as fallback.

If no product specified: infer from scenario. If still unclear, ask.

**Duration math** (internal):
- 30 min demo = 2 feature spotlights maximum (10 min problem/setup, 15 min product, 5 min wrap)
- 45 min demo = 3 feature spotlights (15 min problem/setup, 25 min product, 5 min wrap)
- 60 min demo = 4 feature spotlights (15 min problem/setup, 35 min product, 10 min wrap + Q&A)

### Step 1: Load Source Knowledge

Read in this order:
1. `📦 Products/[product]/product-context/[product]-icp.md` — persona jobs, pains, success metrics
2. `📦 Products/[product]/product-context/[persona]-persona.md` (if it exists)
3. Any PRDs or spec-briefs in `📦 Products/[product]/` matching the scenario topic
4. `📚 Knowledge/Research/signals-[current month].md` — filter for `--product [product]` + ICP fit High — surface any recent praise or confusion signals

If competitor mentioned in scenario: check `📚 Knowledge/Market/battlecard-[competitor-slug].md` and load the Competitive Awareness section.

### Step 2: Generate Demo Guide

Output a 6-section demo guide:

```markdown
## Demo Guide: [Product] — [Persona] — [Duration] min — [Date]

**Scenario:** [One sentence — who this customer is, what they're evaluating, what success looks like for them]
**Sources:** [Files consulted — flag any that were >60 days old]

---

### 1. Opening Hook (Target: first [2-3] minutes)

**Start here, not with the product:** Open in the customer's world — describe the pain they're living with using their language, not product feature names.

**Problem narrative (30-60 seconds):**
"[Verbatim or near-verbatim opening — JTBD framing, specific enough to feel true, generic enough to resonate across the segment]"

**Why this lands for [persona]:** [Brief note on why this problem narrative connects — what job it maps to, what emotion it surfaces]

**Transition into product:** "[One sentence that moves from problem to demo — sets up the aha moment without explaining what they're about to see]"

---

### 2. Demo Flow — Story Arc

Design path: **open in their world → build to aha moment → show value before explaining how**

```
[Problem established] → [Feature A: early context] → [★ AHA MOMENT] → [Feature B: depth] → [Discovery + wrap]
```

**Why this order, not feature-menu order:** [Brief explanation of the narrative logic — what each step is building toward]

**Time budget:**
- Opening + problem setup: [X min]
- [Feature A]: [X min]
- ★ AHA MOMENT ([Feature/workflow name]): [X min — this is the demo's center of gravity]
- [Feature B if time allows]: [X min]
- Discovery questions + next steps: [X min]

---

### 3. Feature Spotlights

#### ★ Aha Moment: [Feature or Workflow Name]
**Why lead the demo here (even if it's not shown first):** [What makes this the "that's exactly what I need" moment for this persona]
**Setup needed:** [The minimal amount of context a customer needs to see this moment correctly]
**What to show:** [Specific workflow or interaction — be concrete, not "show the dependency view"]
**What to say:** "[Narrative framing while showing it — value-before-how]"
**The reaction you're looking for:** [What a positive signal looks like — lean forward, specific question, "can it also do..."]

#### Feature Spotlight 2: [Feature Name]
**Why include this:** [What job or pain it addresses for this persona]
**Time allocation:** [X minutes]
**What to show:** [Specific workflow]
**What to say:** "[Value framing]"
**If they want to dig deeper:** "[What to say if they want to extend this section — how to either satisfy or timebox the depth]"

[Add Feature Spotlight 3 only if duration >= 45 min]

---

### 4. Competitive Awareness
[Include only if competitor mentioned in scenario — pulled from battlecard]

**[Competitor] is likely in this evaluation because:** [Most common reason this competitor appears in this scenario]

**Differentiation to weave in naturally (not as a comparison):**
- [Point 1]: "[Natural language framing — how to make the contrast without naming the competitor directly in the demo]"
- [Point 2]: "[Natural language framing]"

**If they name [competitor] directly:** "[Response — acknowledge, differentiate, move on. Don't linger on competitor comparisons mid-demo.]"

**Avoid:** [The demo trap that plays into the competitor's strength — what NOT to show in this context]

[If no competitor in scenario: omit this section entirely]

---

### 5. Discovery Questions to Weave In

Don't save all questions for the end. These belong mid-demo — they signal listening, generate signal, and often open the conversation to topics more important than what you planned to show.

1. "[Question 1]" — ask after [which demo section] — listens for [what job or pain]
2. "[Question 2]" — ask after [which demo section] — listens for [what job or pain]
3. "[Question 3]" — ask before wrapping — listens for [what's missing, what's next]

**The closing question (always last):**
"Does this match what you're dealing with, or is there a different version of this problem we should be exploring?"
— This closes the demo as a discovery moment, not a pitch.

---

### 6. Demo Traps to Navigate

Known rough edges for this persona on this product. Know these before you walk in.

- **[Feature/area 1]**: [What goes wrong if you show it to this persona — known UX rough edge, missing capability, or confusing interaction. How to route around it or set expectations correctly.]
- **[Feature/area 2]**: [Same format]
- **[Feature/area 3 if applicable]**: [Same format]

**If a customer asks about [known gap]:** "[Suggested response — honest, forward-looking, doesn't overpromise or dismiss]"
```

---

### Step 3: Close with Signal Capture Reminder

After generating the guide, always append:
> "**After the demo**: Log any signals immediately — customer reactions, questions asked, rough edges hit. Run `/signal --source call --product [product] "[signal]"` before the context fades."
>
> If the demo hits a rough edge that surfaces a product gap: flag it for routing to `/spec` or `/signal --source call --product [product] "demo gap: [description]"`

---

## Key Constraints

- **Never fabricate product capabilities** — guide can only reference what exists in product-context files, PRDs, or spec-briefs. If something is unknown or undocumented, flag the gap rather than inventing the capability.
- **Demo mode is for internalization, not distribution** — this guide is for the PM, not a leave-behind for the customer.
- **Respect the duration constraint** — a 30-minute demo with 4 feature spotlights is not a 30-minute demo. Time-box ruthlessly.
- **Competitive section only when warranted** — don't add competitive framing to demos where no competitor is in the picture. It creates defensiveness the customer didn't bring in.
- **If product context files are >60 days old**: flag prominently. Insights from the guide may not reflect current product state.

---

## Anti-Patterns to Avoid

**Feature-menu demos** — "Here's the board view, here's the card detail, here's the reporting section." Structure demos around the customer's problem, not the navigation structure.

**Saving discovery for the end** — by then, the customer has mentally checked out or has 2 minutes left. Discovery questions mid-demo produce better signal.

**Showing everything** — a 30-minute slot with 8 features shown shallowly is worse than 3 features shown deeply. Depth creates conviction; breadth creates overwhelm.

**Demo from admin/setup screens** — start in the "day in the life" view of the persona, not the admin configuration. Getting to the good stuff shouldn't require explaining how to set it up first.

---

## Integration Points

**Entry from:**
- `/prep` — surfaces this command when a demo meeting is detected without a current demo guide
- `/product-depth --mode demo` — builds the background knowledge; this command formats it as a guide
- Any demo meeting detected in meeting prep workflow

**Exit to:**
- `/signal --source call` — log what worked, what didn't, what surprised you
- `/product-depth --mode confusion` — if the demo revealed a confusion pattern, add it to the signals file
- `/spec` — if demo exposed a product gap that's a roadmap candidate
- `/granola` — post-meeting intelligence extraction
