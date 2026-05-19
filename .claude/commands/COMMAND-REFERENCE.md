---
description: Run the COMMAND REFERENCE workflow
---
# AIPMOS Command Reference for Intent Detection

This guide helps AI assistants understand when to suggest specific AIPMOS commands based on user intent. Use this to match natural language requests to the most appropriate command.

**Human-readable summary:** [Workflow cheatsheet](../../📝%20Docs/guides/workflow-cheatsheet.md) — curated activity → command map and idea-to-delivery spine.

## How to Use This Guide

1. **Analyze the user's intent**: What are they trying to accomplish?
2. **Match to command patterns**: Look for matching trigger phrases and intent descriptions
3. **Check negative patterns**: Verify it's NOT something better handled by a different command
4. **Suggest with confidence**: Only suggest when confidence is >70%

---

## Command Intent Reference

### /today
**User intent**: Daily planning, reviewing priorities, checking blockers

**When to suggest**:
- User wants to plan their day
- "What should I work on today?"
- "Help me prioritize my tasks"
- "What are my top priorities?"
- "What's on my agenda for today?"
- "Review my daily tasks"

**NOT for**:
- Creating a plan document (use /spec)
- Strategic planning (use /think)
- Long-term roadmap planning (use /prioritize)

---

### /think
**User intent**: Strategic analysis, complex decisions, mental models

**When to suggest**:
- "I need to figure out..." (strategy, OKRs, positioning)
- "What's your strategy for..."
- "Should we do X or Y?"
- "Help me think through..."
- "Strategic analysis of..."
- "Figure out our Q1 OKRs"
- "Positioning for..."
- Complex decision framing

**Modes**:
- **AI product risk analysis**: Automatically triggered when topic involves AI features — loads `🎓 Product-Management/Frameworks/ai-product-risks.md` and runs four dimensions (quality, reliability, trust, adoption risk)
- **Reversibility classification**: Every analysis opens with Type 1 (one-way door) vs. Type 2 (two-way door) classification — determines rigor level applied

**NOT for**:
- Writing a spec document (use /spec)
- Daily task planning (use /today)
- Making a specific decision (use `decision-quality` skill)
- Research interviews (use /discover)

---

### /spec
**User intent**: Create formal specifications, PRDs, documentation; or review existing PRDs for decision quality

**Command syntax**:
```bash
/spec [--type <format>] [--skip-discovery] [--save] [--review <path>] [--biz-case] [<feature-description>]
```

**Arguments**:
- `--type full|light|one-pager|context-doc`: PRD format (default: `full`)
- `--skip-discovery`: Skip Socratic questioning
- `--save`: Save PRD to file
- `--review <path>`: Review existing PRD for decision quality (no file edits unless asked)
- `--biz-case`: Include Business Case section
- `<feature-description>`: Initial feature/idea description

**When to suggest**:
- "Write a spec for..."
- "Create a PRD for..."
- "Document this feature..."
- "Specification for..."
- "Write product requirements for..."
- "Review this PRD" / "Score this spec" / "Make this PRD more actionable" — use `/spec --review <path>`

**Spec vs product-coach skill**: `/spec --review` is specialized for PRD decision-quality and spec readiness (decision density, thresholds, non-goals, anti-patterns). The `product-coach` skill is for broader doc coaching across artifact types (roadmaps, memos, research).

---

### /roadmap
**User intent**: Create a quarterly roadmap document with themes, now/next/later sequencing, confidence levels

**Command syntax**:
```bash
/roadmap --product <name> --quarter <Q> [--format now-next-later|timeline|themes] [--save]
```

**When to suggest**:
- "Create a Q[N] roadmap for [product]"
- "Document our roadmap themes"
- "Now/next/later plan"
- "Quarterly roadmap with explicit exclusions"
- After `/think` and `/prioritize` when ready to commit to a quarterly plan

**Output**: 6-section roadmap (Strategic Themes, Now/Next/Later, Key Bets, What We're NOT Doing, Open Questions, Success Criteria)

**NOT for**: Strategic prioritization (use `/think` or `/prioritize` first)

---

### /memory
**User intent**: Update compiled truth memory or run a health diagnostic on the memory system

**Command syntax**:
```bash
/memory                  # Update memory.md with session activity
/memory --health         # Run structural health audit
/memory --dry-run        # Show what would be updated without writing
```

**When to suggest**:
- "Update my memory file"
- "Record this session to memory"
- "Refresh memory with current activity"
- "Is my memory system up to date?"
- "Check my memory health"
- After completing a feature or milestone
- Before starting a new session after a break

**NOT for**:
- Daily planning (use /today)
- Viewing memory content (read the file directly)

---

### /remember
**User intent**: Search prior Claude Code conversations for chat-only context, decisions, or rationale

**When to suggest**:
- "What did we decide last time?"
- "Search our previous conversations about..."
- "What did we talk about last week?"
- "Find the rationale from earlier sessions"
- After automatic local recall is insufficient because the missing context lives in chat history

**NOT for**:
- Current workspace state already captured in `🤖 AI/memory/memory.md`
- Repo-local document search
- Updating memory files (use /memory)

---

### /discover
**User intent**: Problem exploration, customer research, and buying committee mapping

**Command syntax**:
```bash
/discover [--problem "<statement>"] [--phase <1-4>] [--skip-framing] [--mode external]
```

**When to suggest**:
- "I need to understand the problem space"
- "Research customer needs for..."
- "Discovery for..."
- "Validate problem assumptions"
- "Customer research on..."
- "Explore the opportunity in..."
- "Map the buying committee at [account]"
- "External discovery for [customer/account]" — use `--mode external`

**External mode** (`--mode external`):
- Activates Buying Committee Mapping (Step 1.5) before Phase 1
- Maps five enterprise roles: Economic Buyer, Champion, IT/Security, Daily User, Exec Sponsor
- Use when doing discovery on new accounts or expansion opportunities

**NOT for**:
- Writing specs (use /spec after discovery)
- Detailed research planning (use /research)
- Synthesizing existing data (use `synthesize` skill)

**Command vs. Skill**: `/discover` command = structured 4-phase workflow with evidence gates. `discovery` skill = consultative advisor that helps clarify *what* to learn and *which method* to use next.

---

### /research
**User intent**: Research planning and framework design

**When to suggest**:
- "Create a research plan for..."
- "Design customer interviews for..."
- "Prototype testing for..."
- "Validate this assumption..."
- "Research methodology for..."
- "What should I research about..."

**For research EXECUTION** (actual data gathering, competitive analysis, web research):
- Use the **research skill** (via Skill tool) — starts by clarifying the decision and unknown, then delivers a concise evidence-based readout

**NOT for**:
- Open-ended discovery (use /discover)
- Synthesizing findings (use `synthesize` skill after research)
- Daily planning (use /today)

**Command vs. Skill**:
- `/research` command = Research planning framework (defines scope, methods, success criteria)
- `research` skill = Research execution and synthesis

---

### /align
**User intent**: Get stakeholder buy-in and consensus

**When to suggest**:
- "Get buy-in from..."
- "Align stakeholders on..."
- "Influence leadership to..."
- "Manage objection from..."
- "Build consensus around..."
- "Prepare for stakeholder meeting"

**NOT for**:
- Just drafting communication (use /write)
- Making the decision yourself (use `decision-quality` skill)
- Technical analysis

---

### /write
**User intent**: Draft PM stakeholder communications with type-specific structure and skill routing

**Command syntax**:
```bash
/write [--type <format>] [--to <name>] [<what-to-write>]
```

**Communication types** (auto-detected if not specified):
- `exec` — Executive update (BLUF opening, max 1 page, loads `exec-comms` skill)
- `follow-up` — Post-meeting decisions communicated (structured format; use `/prep --post` if you have raw meeting notes)
- `ask` — Stakeholder ask/approval request (WIIFM framing, explicit ask, loads `influence-craft` skill)
- `announcement` — Broad team or customer communication (loads `elite-copywriter` skill)
- `data` — Data narrative for non-data audiences (context → insight → implication structure)

**When to suggest**:
- "Draft an email to [exec]..."
- "Write executive update for..."
- "Create announcement for..."
- "Draft an ask to [stakeholder]..."
- "Write a stakeholder update on..."
- "Package this data for [audience]"
- "Turn this finding into a story for [exec|sales|CS]"

**Stakeholder-aware**: If `--to` names a person with a `Knowledge/People/[name].md` file, reads it before drafting and tailors communication to their known priorities.

**NOT for**:
- Post-meeting decision extraction (use `/prep --post`)
- Full PRD creation (use `/spec`)
- Strategic analysis (analyze first with `/think`)

---

### /measure
**User intent**: Define metrics and success criteria

**When to suggest**:
- "What metrics should I track for..."
- "Define success criteria for..."
- "How do we measure..."
- "KPIs for..."
- "Dashboard for..."
- "Metrics framework for..."

**NOT for**:
- Post-launch analysis (use /learn)
- Analyzing existing metrics (just analyze them)

---

### /compete
**User intent**: All competitive intelligence — single competitor deep dive, landscape scan, targeted intel brief, or battlecard

**Command syntax**:
```bash
/compete [--mode landscape] [--intel "<topic>"] [--depth quick|standard|deep] [--output battlecard] [--focus <competitor>] [<description>]
```

**When to suggest**:
- "Analyze [competitor]" → `/compete [--focus name]`
- "I need a sales battlecard" → `/compete --output battlecard`
- "Map the full market landscape" → `/compete --mode landscape`
- "Quick scan of [competitor] news" → `/compete --intel "[topic]"`
- "What happened with [competitor] this week?" → `/compete --intel`
- "Intelligence on [competitor]"
- After 3+ losses to same competitor (from `/win-loss`)

**Three modes:**
- **Default** — Full competitor analysis (positioning, capabilities, strengths/weaknesses, strategic opportunities)
- **`--mode landscape`** — Auto-identifies 5 direct + 2–3 indirect competitors, produces positioning map
- **`--intel "<topic>"`** — Targeted quick scan (Exa + optional firecrawl). Outputs urgency-tiered CI brief to `📚 Knowledge/Market/ci-briefs/YYYY-MM-DD-[slug].md`. Depth: `quick` (3 searches), `standard` (5+3 scrapes), `deep` (8+5 scrapes)

**Battlecard mode** (`--output battlecard`):
- Loads `📝 Docs/templates/battlecard-template.md` as structure
- Output: `📚 Knowledge/Market/battlecard-[competitor-slug].md`
- Update triggers: `/win-loss` flags specific competitor claims for targeted section updates

**NOT for**:
- Pricing research (use /price-intel)
- Deal-specific win/loss interviews (use /win-loss)

---

### /win-loss
**User intent**: Structured deal analysis — extract root cause from wins, losses, and no-decisions

**Command syntax**:
```bash
/win-loss [--outcome <win|loss|no-decision>] [--competitor <name>] [<deal-context>]
```

**When to suggest**:
- "Analyze this deal loss"
- "Win/loss analysis on [account]"
- "We lost to [competitor] — understand why"
- "Post-mortem on [deal]"
- "Extract learnings from [deal]"
- "What did we learn from the [account] win?"
- After a deal closes (win, loss, or no-decision)

**Output**: 8-question structured interview → signal extraction → battlecard implication check → win/loss record + pattern detection

**Feeds into**:
- `📚 Knowledge/Market/signals-YYYY-MM.md` via `/signal --source sales`
- `/compete --output battlecard` when 3+ losses to same competitor
- `/prep` champion briefing mode (win/loss learnings inform equipping strategies)

**NOT for**:
- General competitive research (use /compete)
- Customer discovery interviews (use /discover)

---

### /brainstorm
**User intent**: Tactical/pre-PRD brainstorming with expert persona perspectives

**When to suggest**:
- "How might we approach..."
- "I have an idea for..."
- "Help me brainstorm solutions for..."
- "Explore different angles on..."
- "What are some ways we could..."
- "Thinking through approaches to..."
- Pre-PRD exploration of product ideas
- Generating multiple solution concepts

**NOT for**:
- Strategic "should we do this" questions (use /think)
- Formal specification writing (use /spec)
- Customer research interviews (use /discover)
- Making a specific decision (use `decision-quality` skill)

---

### /learn
**User intent**: Post-launch analysis, iteration, experiment design, and growth signal review

**When to suggest**:
- "Post-launch review for..."
- "We shipped [feature] 2 weeks ago - how's it doing?"
- "Should we double down or pivot on..."
- "Analyze launch results for..."
- "Iteration planning for..."
- "Design an experiment for..."
- "Did this change actually work?"
- "Monthly growth signals for this feature"

**NOT for**:
- Launch planning (use /ship)
- Metrics definition (use /measure)

---

### /ship
**User intent**: Launch planning and execution — including in-flight delivery triage and LA/GA decisions

**When to suggest**:
- "Plan the launch for..."
- "Launch readiness for..."
- "Create a launch plan..."
- "Go-to-market strategy for..."
- "Phased rollout for..."
- "What's at risk in my sprint?" → in-flight triage mode
- "We're behind — what are the 3 moves that matter?" → in-flight triage
- "Sales enablement before GA" → LA/GA mode
- "Limited availability vs general availability decision"

**NOT for**:
- Post-launch analysis (use /learn)
- Just writing announcements (use /write)

---

### /mockup
**User intent**: Create UI/UX mockups and designs

**When to suggest**:
- "Create a mockup for..."
- "Design the UI for..."
- "Wireframe for..."
- "Visual design of..."

**NOT for**:
- Full prototype with interactions (use /prototype)
- Technical implementation

---

### /critique
**User intent**: Review and provide feedback

**When to suggest**:
- "Critique this design..."
- "Review this document..."
- "Feedback on..."
- "What do you think of..."

---

### /weekly-review
**User intent**: End-of-week PM calibration — decision retrospective, signal check, relationship health, next-week priorities

**Command syntax**:
```bash
/weekly-review [--week <YYYY-MM-DD of Monday>]
```

**When to suggest**:
- "Let's do the weekly review"
- "End of week PM review"
- "How did this week go?"
- "Set up next week's priorities"
- "Review decisions I made this week"
- Friday afternoon or Monday morning reorientation

**Five sections**: Signal capture review → Decision retrospective (from decision journal) → Relationship health (K/P files) → Next-week priorities

**Source files read**:
- `📚 Knowledge/decisions/decision-journal.md` — decision retrospective
- `📚 Knowledge/People/` — relationship health
- `📋 Tasks/today.md` + `GOALS.md` — next-week priority setting

**NOT for**:
- Daily planning (use /today)
- Post-meeting extraction (use /granola)

---

### /prep
**User intent**: Pre-meeting preparation — agenda, decisions to make, stakeholder positions, talking points; or post-meeting follow-up extraction

**Command syntax**:
```bash
/prep [--meeting <title>] [--people <names>] [--goal <goal>] [<description>]
/prep --post [<meeting-title-or-notes>]
```

**When to suggest**:
- "Prep me for my meeting with [person]" → standard mode
- "Help me prepare for the [sync]" → standard mode
- "What decisions do I need to make in this meeting?" → standard mode
- "Equip my champion before their exec review" → Champion Briefing mode (auto-activates)
- "Extract decisions from today's meeting" → `--post` mode
- "Draft follow-up from the [meeting]" → `--post` mode
- "What were the action items from [meeting]?" → `--post` mode

**Modes**:
- **Standard (pre-meeting)**: 7-section prep package (My Goal → Context Brief → Decisions to Make → Agenda → Anticipated Objections → Talking Points → Questions I Need Answered) + stress-test offer
- **Champion Briefing** (auto-activates for external customer champion meetings): 5-section equipping brief
- **`--post` (post-meeting)**: Extracts decisions, action items, open questions, commitments; drafts follow-up communication; proposes `Knowledge/People/` updates (with confirmation)

**NOT for**: Full stakeholder strategy (use `/align`)

---

### /granola
**User intent**: Extract meeting insights from Granola and surface post-meeting intelligence

**When to suggest**:
- "Extract meeting notes..."
- "Summarize meeting from..."
- "Action items from meeting..."
- "Pull yesterday's meetings"

**Behavior**: After extraction, automatically surfaces decisions made, action items, stakeholder signals, and `Knowledge/People/` update candidates for each meeting. Nothing is written automatically — use `/prep --post` to turn the output into structured follow-up.

**NOT for**: Drafting follow-up communications (use `/prep --post`), full stakeholder strategy (use `/align`)

---

### /signal
**User intent**: Capture a customer signal at the moment it occurs — from any source

**Command syntax**:
```bash
/signal [--source <type>] [--product <name>] [<raw-signal>]
```

**When to suggest**:
- "Log a customer signal"
- "Customer said X on a call"
- "Heard from [customer] that..."
- "Support ticket pattern I want to capture"
- "Add this to the signal file"
- Any time a customer insight occurs that shouldn't be lost before synthesis

**Output**: Structured atomic nugget (source, signal verbatim, ICP fit, strength, routing to relevant initiative) + optional append to `Knowledge/Market/signals-YYYY-MM.md`

**NOT for**: Full synthesis (use `synthesize` skill when 10+ signals accumulated), post-meeting extraction (use `/granola`)

---

### /prototype
**User intent**: Create interactive prototypes

**When to suggest**:
- "Build a prototype for..."
- "Interactive mockup of..."
- "Clickable prototype for..."

**NOT for**:
- Static mockups (use /mockup)

---

### /ui-refine
**User intent**: Implement UI and refine until it scores ≥9.3/10 on an objective rubric

**When to suggest**:
- "Refine this UI until it's polished"
- "Implement this and iterate until it's good"
- "Build this component with the quality loop"
- "Run the UI refinement loop on..."
- User wants iterative quality assurance on UI work

**Command syntax**:
```
/ui-refine [task-description]
```

**Behavior**: Resolve task/stack/constraints from context, then implement → rubric → refine → repeat until aggregate ≥9.3 and no dimension <9. Max 5 iterations.

**NOT for**:
- Creating mockups from scratch (use /mockup)
- Interactive prototypes (use /prototype)
- Non-UI work

---

### /biz-case
**User intent**: Build or pressure-test business reasoning — financial model, cross-functional tradeoffs, stakeholder perspectives, or Business Case section in a spec

**Command syntax**:
```bash
/biz-case [--mode model|tradeoff|perspective|review] [--feature <name>]
```

**When to suggest**:
- "Build a business case for [feature/initiative]"
- "What's the ARR impact of [feature]?"
- "How does CS/Sales/Finance think about [idea]?"
- "Cross-functional tradeoff analysis for [feature]"
- "What will Finance say about [proposal]?"
- "Revenue model for [initiative]"

**NOT for**:
- Full spec writing (use `/spec`)
- Strategic framing without financial grounding (use `/think`)

---

### /prioritize
**User intent**: Quick prioritization of prepared lists (5-15 min)

**When to suggest**:
- "Score these 5 features with RICE"
- "Rank my Q2 sprint"
- "ICE scoring for this list"
- "Prioritize these prepared items"
- Quick scoring with known framework
- Simple ranking decisions

**NOT for**:
- Raw feedback processing (use **prioritization-craft skill**)
- Stakeholder communication needed (use **prioritization-craft skill**)
- Complex triage needed (use **prioritization-craft skill**)
- Daily task planning (use /today)
- Strategic decisions (use /think or `decision-quality` skill)

**Dual-Mode Note**: For complex prioritization requiring raw feedback processing, stakeholder communication, or strategic validation, use the **prioritization-craft skill** instead.

---

### prioritization-craft (Skill)
**User intent**: Prioritization support ranging from quick ranking to deeper triage and stakeholder communication

**When to suggest**:
- "Triage 50 customer requests"
- "Build roadmap with stakeholder buy-in"
- "Process feedback from multiple sources"
- "Need to say NO gracefully"
- Complex trade-offs requiring strategic validation
- Raw customer feedback (quotes, tickets, interviews)

**NOT for**:
- Quick scoring (use /prioritize command)
- Simple ranking (use /prioritize command)

---

## Idea-to-Delivery Lifecycle

The canonical PM lifecycle. Each step produces outputs carried forward via rich contextual handoffs.

| Step | Command | Produces | Carries Into |
|------|---------|----------|-------------|
| 1. Ideation | `/brainstorm` | Problem Statement, key angles | `/discover` |
| 2. Discovery | `/discover` | Validated Opportunity Statement, SOM sizing | `/spec --type one-pager` |
| 3. One-Pager | `/spec --type one-pager` | Solution hypothesis, stakeholder draft | `/spec --type full` |
| 4. PRD | `/spec --type full` | Approved PRD: capabilities, metrics, risks, personas | Design + Engineering handoff |
| 5. Design Handoff | Manual: share PRD with designer | Designer brief via PRD artifacts | Designer kickoff |
| 6. Engineering Handoff | Manual: share with tech lead | Story breakdown via PRD artifacts | `/ship` |
| 7. Launch | `/ship` | Launch plan, communications, metrics baseline | `/learn` |
| 8. Learning | `/learn` | Iteration priorities, validated evidence | `/brainstorm` or `/spec` |

**Entry points**: You don't need to start at Step 1. Look at what already exists in `📦 Products/{product}/initiatives/{feature-slug}/` to determine where you are.

---

## Intelligence Command Routing

When you need competitive or market intelligence, use this map:

| I need to… | Use |
|---|---|
| Quick scan on a competitor move or announcement | `/compete --intel "[topic]"` |
| Deep-dive on a specific competitor or generate a battlecard | `/compete [--focus name] [--output battlecard]` |
| Map the full competitive landscape | `/compete --mode landscape` |
| Analyze a deal we won, lost, or didn't close | `/win-loss` |
| Research pricing strategy or competitor pricing | `/price-intel` |

**Rule**: Start with `--intel` for quick awareness. Escalate to full `/compete` when you need depth. `/win-loss` after every deal close.

---

## Quick Reference Table

| User Says... | Suggest Command |
|--------------|-----------------|
| "What should I work on today?" | /today |
| "Figure out our Q1 OKRs" | /think |
| "Should we do X or Y?" | decision-quality skill |
| "Write a spec for feature X" | /spec |
| "Review this PRD for quality" | /spec --review path/to/prd.md |
| "Find patterns in customer feedback" | synthesize skill |
| "Score these 5 features" | /prioritize (command) |
| "Rank my Q2 sprint" | /prioritize (command) |
| "Triage 50 customer requests" | prioritization-craft (skill) |
| "Process raw feedback for roadmap" | prioritization-craft (skill) |
| "Build roadmap with stakeholder comms" | prioritization-craft (skill) |
| "Research customer needs" | /discover |
| "Update memory with session" | /memory |
| "Check memory health" | /memory --health |
| "Search our previous conversations" | /remember |
| "Get stakeholder buy-in" | /align |
| "Write executive brief" | /write --type exec |
| "Package this data for leadership" | /write --type data |
| "Validate this assumption" | /research |
| "What metrics to track?" | /measure |
| "Analyze competitor X" | /compete |
| "Quick scan of competitor news" | /compete --intel "[topic]" |
| "Map the full market landscape" | /compete --mode landscape |
| "Help me brainstorm solutions" | /brainstorm |
| "Post-launch learning" | /learn |
| "Design an experiment to test X" | /learn (Phase 5.5) |
| "Plan the launch" | /ship |
| "What's at risk in my sprint?" | /ship (in-flight triage) |
| "Sales enablement before GA" | /ship (LA/GA section) |
| "Create a mockup" | /mockup |
| "Refine this UI until polished" | /ui-refine |
| "New to AIPMOS" | Use /today and /spec to get started |
| "Critique this design" | /critique |
| "Pricing strategy / WTP research" | `pricing-intelligence` skill |
| "Removal audit on this spec" | `reduce` skill |
| "Opportunity solution tree" | `opportunity-solution-tree` skill |
| "Extract meeting notes" | /granola |
| "Draft follow-up from meeting" | /prep --post |
| "Extract decisions from today's sync" | /prep --post |
| "What's new in Claude Code for us?" | dex-improve skill |
| "Create a Q2 roadmap document" | /roadmap |
| "Prep me for my meeting with..." | /prep |
| "Equip my champion before their exec review" | /prep (champion briefing mode) |
| "Log a customer signal" | /signal |
| "Customer said X on a call" | /signal |
| "Heard from [customer] that..." | /signal |
| "Draft exec update" | /write --type exec |
| "Draft an ask to [stakeholder]" | /write --type ask |
| "Analyze this deal loss" | /win-loss |
| "Win/loss analysis on [account]" | /win-loss |
| "We lost to [competitor] — why?" | /win-loss --outcome loss --competitor |
| "Generate a battlecard for [competitor]" | /compete --output battlecard |
| "External discovery at [account]" | /discover --mode external |
| "Map the buying committee at [account]" | /discover --mode external |
| "Weekly PM review" | /weekly-review |
| "End of week review" | /weekly-review |
| "Review my decisions this week" | /weekly-review |
| "Demo background on [product]" | `product-operational-intelligence` skill |
| "What changed in [product] recently?" | `product-operational-intelligence` skill |
| "Where do customers get confused with [product]?" | `product-operational-intelligence` skill |
| "Build a business case for [feature]" | /biz-case |
| "What will Finance/CS/Sales say about this?" | /biz-case --mode perspective |

**Dual-Mode Commands**: Some capabilities have both a quick command and a deep skill variant:
- **/prioritize** (quick) vs **prioritization-craft skill** (expanded): Quick scoring vs. prioritization support with outcome/constraint framing
- **/think** (quick) vs **strategic-thinking skill** (expanded): Quick strategic framing vs. strategic decision support for high-stakes work

---

## Suggestion Format Template

When suggesting a command, use this format:

```markdown
💡 **Command Suggestion**

Your request sounds like {intent description}.

Consider using **/{command}** for {what the command does}.

**What it will help you with**:
- {Benefit 1}
- {Benefit 2}
- {Benefit 3}

[Invoke /{command}] or [Continue conversation]
```

## Important Notes

1. **Don't over-suggest**: Only suggest when a command would clearly be more effective than direct conversation
2. **Trust user intent**: If they want to just talk, let them talk
3. **Explain the value**: Briefly explain WHY this command is better than conversation
4. **Always offer choice**: Never auto-invoke; always suggest with opt-out
5. **Be confident but humble**: "Consider using" not "You must use"
