---
description: Run the COMMAND REFERENCE workflow
---
# AIPMOS Command Reference for Intent Detection

This guide helps AI assistants understand when to suggest specific AIPMOS commands based on user intent. Use this to match natural language requests to the most appropriate command.

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

**New modes added**:
- **AI product risk analysis**: Automatically triggered when topic involves AI features — loads `📚 Knowledge/Frameworks/ai-product-risks.md` and runs four dimensions (quality, reliability, trust, adoption risk)
- **Reversibility classification**: Every analysis now opens with Type 1 (one-way door) vs. Type 2 (two-way door) classification — determines rigor level applied

**NOT for**:
- Writing a spec document (use /spec)
- Daily task planning (use /today)
- Making a specific decision (use `decision-quality` skill)
- Research interviews (use /discover)

---

### /templates
**User intent**: Find the right template/framework for what you want to create

**When to suggest**:
- "I want to create a..."
- "What's the template for..."
- "Help me write a..."
- "I need to document..."
- "How do I create a..."
- Unclear which command to use for a task

**NOT for**:
- Already know which command you need (use that command directly)
- General conversation (no command needed)

---

### /workflow
**User intent**: Run a repeatable multi-step process (QPR prep, weekly stakeholder update, research synthesis)

**When to suggest**:
- "Let's run the QPR prep"
- "Prep for quarterly planning review"
- "Do the weekly stakeholder update"
- "Synthesize customer research from meetings"
- "Run the workflow for..."

**How to invoke**: Point at the workflow folder; e.g. "Let's run the QPR prep workflow @Workflows/qpr-prep/" or "Do the weekly update @Workflows/weekly-stakeholder-update/". Claude reads that workflow's CLAUDE.md and workflow.md and follows the step guide. See also the **Idea-to-Delivery Lifecycle** section and the **Workflows** section in this reference.

**Available workflows**: `📁 Workflows/metrics-health-check/`, `📁 Workflows/qpr-prep/`, `📁 Workflows/weekly-stakeholder-update/`, `📁 Workflows/customer-research-synthesis/`

**NOT for**:
- One-off tasks (use /today or project folder)
- Single prompt/skill (use a slash command or skill)

---

### /planview-slides
**User intent**: Create a hosted, animated, shareable Planview deck

**When to suggest**:
- "Build a deck I can send as a link"
- "Create a hosted presentation"
- "Make this a password-protected HTML deck"
- "Set up a live deck with animations"
- "Publish this presentation to the Vercel site"

**NOT for**:
- Editable PowerPoint deliverables (use /planview-deck)
- Legacy PPTX workflows that require html2pptx output

---

### /planview-deck
**User intent**: Create an editable PowerPoint deck

**When to suggest**:
- "I need a PPTX deck"
- "Make this editable in PowerPoint"
- "Use the corporate PowerPoint template"
- "Build title slide + content slides for PPTX handoff"

**NOT for**:
- Hosted HTML decks (use /planview-slides)
- Password-protected live share links

---

### /spec
**User intent**: Create formal specifications, PRDs, documentation; or review existing PRDs for decision quality

**Command syntax**:
```bash
/spec [--type <format>] [--skip-discovery] [--save] [--review <path>] [<feature-description>]
```

**Arguments**:
- `--type full|light|one-pager|context-doc`: PRD format (default: `full`)
- `--skip-discovery`: Skip Socratic questioning
- `--save`: Save PRD to file
- `--review <path>`: Review existing PRD for decision quality (no file edits unless asked)
- `<feature-description>`: Initial feature/idea description

**When to suggest**:
- "Write a spec for..."
- "Create a PRD for..."
- "Document this feature..."
- "Specification for..."
- "Write product requirements for..."
- "Create technical spec..."
- "Review this PRD" / "Score this spec" / "Make this PRD more actionable" — use `/spec --review <path>`
- `/spec "Native Project Milestones in Roadmaps"` - with initial idea
- `/spec --type light "Card blocking improvements"` - lightweight spec
- `/spec --skip-discovery "API rate limiting"` - skip discovery phase
- `/spec --review path/to/prd.md` - review existing PRD for quality

**Spec vs product-coach skill**: `/spec --review` is specialized for PRD decision-quality and spec readiness (decision density, thresholds, non-goals, anti-patterns). The `product-coach` skill is for broader doc coaching across artifact types (roadmaps, memos, research). Use `/spec --review` when the focus is PRD-specific quality; use the `product-coach` skill for general feedback or non-PRD artifacts.

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

**NOT for**: Strategic prioritization (use `/think` or `/prioritize` first), OKR tracking (use `/okr-progress`)

---

### /design-brief
**User intent**: Generate a designer-ready design brief from an approved PRD

**Command syntax**:
```bash
/design-brief --prd <path> [--save] [<feature-description>]
```

**When to suggest**:
- "Generate a design brief from [PRD path]"
- "Create a design brief for [feature]"
- "Prep the designer handoff"
- After `/spec` with a designer being engaged
- "Scaffold design brief from this PRD"

**Output**: 7-section design brief (Header → Problem → Solution → Design Direction → Deliverables → Before Starting Design → Success Criteria)

**NOT for**: Writing the PRD (use `/spec` first), creating mockups (use `/mockup`), tech specs (use `/spec-brief`)

---

### /story
**User intent**: Generate Epic → Feature → Story hierarchy from an approved PRD; optionally push to AgilePlace

**Command syntax**:
```bash
/story --prd <path> [--board <board_id>] [--dry-run] [--save-only] [<description>]
```

**When to suggest**:
- "Break this PRD into stories"
- "Generate AgilePlace cards from this PRD"
- "Create the backlog for [feature]"
- "Story breakdown for [prd-path]"
- After `/spec` when ready to create development backlog

**Output**: 1 Epic + 3-7 Features + Stories with Gherkin-lite acceptance criteria; optional AgilePlace CLI push

**NOT for**: Writing the PRD (use `/spec` first), single card creation (use AgilePlace CLI directly), Gherkin spec (use `/spec-brief`)

---

### /spec-brief
**User intent**: Generate agent-ready technical specification from approved PRD

**When to suggest**:
- "Create a technical spec from this PRD"
- "Generate implementation brief for..."
- "Handoff to engineering/agents"
- "Convert PRD to developer-ready format"
- "What do engineers need to build this?"
- "Generate Spec Brief from..."

**Output**: Creates `SPEC_BRIEF.md` in the same directory as the source PRD, containing:
- Context (TL;DR)
- Problem statement
- Solution overview
- User flows
- Inputs/Outputs tables
- Core rules (business logic)
- UI states
- Data model
- **Acceptance criteria in Gherkin format (Given-When-Then)**
- Test scenarios (happy path, edge cases, errors)
- Dependencies
- Implementation notes

**NOT for**:
- Creating initial PRD (use /spec)
- Strategic problem definition (use /think or /discover)
- Business stakeholder review (PRD is better for that)

**Workflow**:
```
1. Write and approve PRD (business-focused)
2. Run /spec-brief [path-to-prd]
3. Share SPEC_BRIEF.md with engineering/agents
```

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

**Dual-Mode Note**: For complex prioritization requiring raw feedback processing, stakeholder communication, or strategic validation, use the **prioritization-craft skill** instead. It now starts by clarifying objective, horizon, and constraints, then turns that framing into a ranking and stakeholder-ready tradeoff call.

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

### /refresh-memory
**User intent**: Update memory.md with session activity and git commits

**When to suggest**:
- "Update my memory file"
- "Record this session to memory"
- "Refresh memory with current activity"
- "Capture session progress"
- After completing a feature or milestone
- Before running /check-progress

**NOT for**:
- Checking what changed (use /memory-health)
- Daily planning (use /today)
- Viewing memory content (read the file directly)

---

### /memory-health
**User intent**: Combined memory system diagnostic — is my memory stale and what should I do about it?

**When to suggest**:
- "Is my memory system up to date?"
- "Check my memory health"
- "What changed since I last updated my memory?"
- "Do I need to run /refresh-memory?"
- Weekly maintenance cadence
- Before starting a new session after a break

**Replaces**: Running `/check-progress` then `/memory-audit` separately. Combines activity delta (git commits, file changes since last update) + structural health audit (TTL violations, line count warnings) into one output ending with **one specific recommended action**.

**NOT for**:
- Actually updating memory (use /refresh-memory)
- Capturing new patterns (use /capture-pattern)
- Running the full Python audit in detail (use memory_maintainer.py directly)

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
- Repo-local document search that the cue-triggered hook can handle automatically
- Updating memory files (use /refresh-memory or /capture-pattern)

---

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
- Maps five enterprise roles: Economic Buyer, Champion, IT/Security, Daily User, Influencer
- Use when doing discovery on new accounts or expansion opportunities where internal champion ≠ entire buying committee

**NOT for**:
- Writing specs (use /spec after discovery)
- Detailed research planning (use /research)
- Synthesizing existing data (use `synthesize` skill)

**Command vs. Skill**: `/discover` command = structured 4-phase workflow with evidence gates, argument-driven handoff, and explicit phase progression (use when you want a guided discovery process). `discovery` skill = consultative advisor that helps you clarify *what* to learn and *which method* to use next (use in chat when you're not sure how to frame the discovery, or when the full 4-phase workflow is more than the situation needs).

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
- Use the **research skill** (via Skill tool) - starts by clarifying the decision and unknown, then delivers a concise evidence-based readout or expands into fuller research mode when needed

**NOT for**:
- Open-ended discovery (use /discover)
- Synthesizing findings (use `synthesize` skill after research)
- Daily planning (use /today)

**Command vs. Skill**:
- `/research` command = Research planning framework (defines scope, methods, success criteria)
- `research` skill = Research execution and synthesis (consultative framing first, deeper research when warranted)

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
- `follow-up` — Post-meeting decisions communicated (loads structured format; prefer `/follow-up` if you have a granola file)
- `ask` — Stakeholder ask/approval request (WIIFM framing, explicit ask, loads `influence-craft` skill)
- `announcement` — Broad team or customer communication (loads `elite-copywriter` skill)

**When to suggest**:
- "Draft an email to [exec]..."
- "Write executive update for..."
- "Create announcement for..."
- "Draft an ask to [stakeholder]..."
- "Write a stakeholder update on..."
- "Draft exec comms for..."

**Stakeholder-aware**: If `--to` names a person with a `Knowledge/People/[name].md` file, reads it before drafting and tailors communication to their known priorities.

**NOT for**:
- Post-meeting decision extraction (use `/follow-up` with a granola file)
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

### /okr-progress
**User intent**: Analyze OKR progress, risk, and get actionable recommendations

**Canonical source**: `.claude/prompts/okr-progress-analysis.md`

**When to suggest**:
- "Track my OKR progress"
- "Analyze progress on my objectives"
- "Evaluate this objective for the board"
- "Which OKRs need attention?"
- "What's blocking my OKRs?"
- "OKR health check"
- "Get one priority action for this week"

**Behavior**: Prompts user for scope (portfolio vs single objective), date, and audience. Then runs analysis with problem-first ordering and one high-impact action.

**NOT for**:
- Writing new OKRs (use /think or okr-frameworks skill)
- General metrics definition (use /measure)

---

### /compete
**User intent**: All competitive intelligence — single competitor deep dive, landscape scan, or battlecard

**Command syntax**:
```bash
/compete [--mode landscape] [--output battlecard] [--focus <competitor>] [<description>]
```

**When to suggest**:
- "Analyze [competitor]"
- "Competitive analysis of..."
- "What are competitors doing?"
- "Market positioning vs..."
- "Competitive matrix for..."
- "Intelligence on [competitor]"
- "Generate a battlecard for [competitor]"
- "Build a battlecard for sales"
- "Map the market landscape" → use `--mode landscape`
- "Who are all our competitors?" → use `--mode landscape`
- After 3+ losses to same competitor (pattern alert from `/win-loss`)

**Routing map:**
```
I need to understand a specific competitor     → /compete [--focus name]
I need a sales battlecard                      → /compete --output battlecard
I need to scan the full market landscape       → /compete --mode landscape
I need analyst/earnings trend analysis         → /daily-brief --industry
I need pricing competitive research            → /price-intel
```

**Battlecard mode** (`--output battlecard`):
- Loads `📚 Knowledge/Templates/battlecard-template.md` as structure
- Sources intelligence from deal interviews, signals, and research
- Output: `📚 Knowledge/Market/battlecard-[competitor-slug].md`
- Update triggers: `/win-loss` flags specific competitor claims for targeted section updates

**Landscape mode** (`--mode landscape`):
- Auto-identifies 5 direct + 2–3 indirect competitors
- Produces comparison matrix and positioning map
- Use when you don't know which competitors to analyze

**NOT for**:
- Daily competitive briefs (use /daily-brief)
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
- `📚 Knowledge/Research/signals-YYYY-MM.md` via `/signal --source sales`
- `/compete --output battlecard` when 3+ losses to same competitor
- `/prep` champion briefing mode (win/loss learnings inform equipping strategies)

**NOT for**:
- General competitive research (use /compete)
- Customer discovery interviews (use /discover)

---

### /daily-brief
**User intent**: Automated daily competitive intelligence summary

**When to suggest**:
- "Daily competitive briefing"
- "What's happening in our market?"
- "Competitive news summary"

**NOT for**:
- Deep competitive analysis (use /compete)
- General competitive questions

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

### /learning-opportunity
**User intent**: Pause development for a three-level deep dive into technical concepts

**When to suggest**:
- "Can you explain how this works?"
- "Help me understand this pattern"
- "What's happening under the hood?"
- "Teach me about..."
- "Deep dive into..."
- User wants to level up their technical understanding
- Curiosity about architecture or implementation details

**NOT for**:
- Quick explanations (just explain it directly)
- Non-technical questions
- Getting work done (let them work)

**Teaching Approach**:
- Level 1: Core concept - what it is, problem it solves, when to use it
- Level 2: How it works - mechanics, tradeoffs, debugging
- Level 3: Deep dive - production behavior, scaling, senior engineer perspective

---

### /learn
**User intent**: Post-launch analysis and iteration

**When to suggest**:
- "Post-launch review for..."
- "We shipped [feature] 2 weeks ago - how's it doing?"
- "Should we double down or pivot on..."
- "Analyze launch results for..."
- "Iteration planning for..."

**NOT for**:
- Launch planning (use /ship)
- Metrics definition (use /measure)

---

### /ship
**User intent**: Launch planning and execution

**When to suggest**:
- "Plan the launch for..."
- "Launch readiness for..."
- "Create a launch plan..."
- "Go-to-market strategy for..."
- "Phased rollout for..."

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
- "Mockup generator for..."

**NOT for**:
- Full prototype with interactions (use /prototype)
- Technical implementation

---

### /narrative
**User intent**: Strategic storytelling and positioning

**When to suggest**:
- "Create a strategic narrative for..."
- "Positioning story for..."
- "Strategic messaging for..."
- "Narrative around..."

**NOT for**:
- General writing (use /write)
- Feature specs (use /spec)

---

### /onboard
**User intent**: New user onboarding and orientation

**When to suggest**:
- "New to AIPMOS - help me get started"
- "How do I use these commands?"
- "Getting started with..."
- "Introduction to..."

---

### /bug-report
**User intent**: Report issues or problems

**When to suggest**:
- "Report a bug in..."
- "Issue with..."
- "Something's broken..."

---

### /critique
**User intent**: Review and provide feedback

**When to suggest**:
- "Critique this design..."
- "Review this document..."
- "Feedback on..."
- "What do you think of..."

---

### /price-intel
**User intent**: Competitive pricing research

**When to suggest**:
- "Competitor pricing analysis"
- "Pricing intelligence for..."
- "Price comparison with..."

**NOT for**:
- General competitive analysis (use /compete)

---

### /capture-pattern
**User intent**: Capture semantic learning to accumulated wisdom file (real-time or batch from sessions)

**When to suggest**:
- "Remember this decision..."
- "Capture this pattern..."
- "Save this learning..."
- "This is worth remembering..."
- After completing a substantial feature or decision
- When you notice a workspace-specific convention
- After making a mistake that wasted time
- "Extract patterns from recent sessions" → use `--from-sessions [days]` (default 7)

**NOT for**:
- Current state updates (use /refresh-memory)
- Daily planning (use /today)
- Strategic analysis (use /think)

---

### /dex-improve
**User intent**: Evolve the AI OS (hooks, skills, commands), align with **Claude Code**, **Claude Cowork**, and **Claude Desktop** updates, or audit capabilities vs this repo (and workflows outside git where relevant)

**When to suggest**:
- "What's new in Claude Code / Cowork / Desktop for this workspace?"
- "How should we adopt [hooks / subagents / skills / MCP]?"
- "Audit what we're using vs what Claude Code supports"
- "Improve AIPMOS setup" / "upgrade my context engineering"
- Workshop a concrete change to `.claude/`, `AGENTS.md`, or Cursor rules

**NOT for**:
- Scoring or amending individual skills (use /skill-review or skill-review skill)
- One-line learnings and conventions (use /capture-pattern)
- Teaching-style explanations of PM topics (use /learning-opportunity)
- Product specs and strategy (use /spec, /think)

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

**Five sections**: OKR progress check (delegates to `/okr-progress`) → Signal capture review → Decision retrospective (from decision journal) → Relationship health (K/P files) → Next-week priorities

**Core principle**: Calibration ritual, not status report — asks: Are we making good decisions? Capturing signal? Seeing the right people?

**Source files read**:
- `📚 Knowledge/decisions/decision-journal.md` — decision retrospective
- `📚 Knowledge/People/` — relationship health
- `📋 Tasks/today.md` + `GOALS.md` — next-week priority setting

**NOT for**:
- Daily planning (use /today)
- OKR-specific deep analysis (use /okr-progress)
- Post-meeting extraction (use /granola)
- Cross-month growth signal synthesis (use /growth-review)

---

### /growth-review
**User intent**: Cross-month growth signal synthesis — surface repeating PM reasoning patterns across quarters

**When to suggest**:
- "What failure modes keep showing up in my work?"
- "Show me my growth patterns over time"
- "What coaching themes are recurring?"
- "Quarterly PM development review"
- "What am I consistently getting wrong?"

**Distinct from `/weekly-review`**: `/weekly-review` Step 1.5 covers the *current month* only. `/growth-review` aggregates across N months (default: 3) to find patterns that are invisible in a single month.

**Output**: Repeating pattern tags (3+ entries) with verbatim quotes, coverage gaps (archetypes with no entries), and one concrete behavior change to focus on.

**NOT for**:
- Current-month synthesis (use /weekly-review Step 1.5)
- Runs without growth signal files populated

---

### /prep
**User intent**: Pre-meeting preparation — agenda, decisions to make, stakeholder positions, talking points

**Command syntax**:
```bash
/prep [--meeting <title>] [--people <names>] [--goal <goal>] [<description>]
```

**When to suggest**:
- "Prep me for my meeting with [person]"
- "Help me prepare for the [sync]"
- "What decisions do I need to make in this meeting?"
- "I have a meeting with [person] today — help me get ready"
- Before any high-stakes meeting where decisions or alignment is needed

**Output**: 7-section prep package (My Goal → Context Brief → Decisions to Make → Agenda → Anticipated Objections → Talking Points → Questions I Need Answered) + stress-test offer

**Champion Briefing mode** (auto-activates for external customer meetings):
- Triggers when attendee is an external customer champion meeting their exec/renewal/PI planning
- Replaces standard 7-section format with a 5-section champion equipping brief
- Goal: give the champion the story, data, and objection responses to sell internally without you in the room

**NOT for**: Post-meeting extraction (use `/granola`), full stakeholder strategy (use `/align`)

---

### /granola
**User intent**: Extract meeting insights from Granola and surface post-meeting intelligence

**When to suggest**:
- "Extract meeting notes..."
- "Summarize meeting from..."
- "Action items from meeting..."
- "Pull yesterday's meetings"

**Behavior**: After extraction, automatically surfaces decisions made, action items, stakeholder signals, and `Knowledge/People/` update candidates for each meeting. Nothing is written automatically — intelligence is presented and user confirms via `/follow-up`.

**NOT for**: Drafting follow-up communications (use `/follow-up`), full stakeholder strategy (use `/align`)

---

### /follow-up
**User intent**: Draft post-meeting communications and update stakeholder context from a meeting

**Command syntax**:
```bash
/follow-up [--meeting <title-or-path>] [--type <format>] [--people <names>]
```

**When to suggest**:
- "Send follow-up from [meeting]"
- "Communicate what we decided in..."
- "Draft action items from today's sync"
- "Update the team on what was decided"
- After `/granola` surfaces "Run `/follow-up --meeting [title]`"
- Any time decisions from a meeting need to be communicated

**Output**: Structured follow-up (Decision / Action Items / Still Open) + `Knowledge/People/` update prompts for all participants with existing files

**NOT for**: Full post-meeting extraction (use `/granola` first), broader stakeholder strategy (use `/align`), pre-meeting prep (use `/prep`)

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

**Output**: Structured atomic nugget (source, signal verbatim, ICP fit, strength, routing to relevant initiative) + optional append to `Knowledge/Research/signals-YYYY-MM.md`

**NOT for**: Full synthesis (use `synthesize` skill when 10+ signals accumulated), post-meeting extraction (use `/granola`), competitive intelligence (use `/compete`)

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

**Canonical source**: `/Users/jhigh/Planview Work/.claude/prompts/ui-refinement-loop.md`

**When to suggest**:
- "Refine this UI until it's polished"
- "Implement this and iterate until it's good"
- "Build this component with the quality loop"
- "Run the UI refinement loop on..."
- User wants iterative quality assurance on UI work
- UI task that should meet a high quality bar

**Command syntax**:
```
/ui-refine [task-description]
/ui-refine [with file or selection attached]
```

**Behavior**: Read the canonical prompt, resolve task/stack/constraints from context, then implement → rubric → refine → repeat until aggregate ≥9.3 and no dimension <9. Max 5 iterations.

**NOT for**:
- Creating mockups from scratch (use /mockup)
- Interactive prototypes (use /prototype)
- Non-UI work

---

## Idea-to-Delivery Lifecycle

The canonical PM lifecycle. Each step produces outputs carried forward via rich contextual handoffs — context is not reconstructed manually at each transition.

| Step | Command | Produces | Carries Into |
|------|---------|----------|-------------|
| 1. Ideation | `/brainstorm` | Problem Statement, key angles | `/discover` |
| 2. Discovery | `/discover` | Validated Opportunity Statement, SOM sizing | `/spec --type one-pager` |
| 3. One-Pager | `/spec --type one-pager` | Solution hypothesis, stakeholder draft | `/spec --type full` |
| 4. PRD | `/spec --type full` | Approved PRD: capabilities, metrics, risks, personas | `/design-brief` + `/story` |
| 5. Design Brief | `/design-brief` | 7-section brief, screen inventory | Designer kickoff |
| 6. Story Breakdown | `/story` | AgilePlace Epic/Feature/Stories with ACs | `/spec-brief` |
| 7. Dev Handoff | `/spec-brief` | Gherkin ACs, data model, API contract | `/ship` |
| 8. Launch | `/ship` | Launch plan, communications, metrics baseline | `/learn` |
| 9. Learning | `/learn` | Iteration priorities, validated evidence | `/brainstorm` or `/spec` |

**Entry points**: You don't need to start at Step 1. Look at what already exists in `📦 Products/{product}/initiatives/{feature-slug}/` to determine where you are.

**Cross-session state**: Initiative folders are the workflow state indicator. If you see a `story-breakdown.md` but no `design-brief.md`, story breakdown ran before design handoff — flag this to the PM as an ordering issue. The presence of `SPEC_BRIEF.md` means dev handoff is complete; absence of it alongside a story breakdown indicates a gap.

---

## Workflows

Repeatable cadence playbooks — distinct from the idea-to-delivery lifecycle. Each workflow lives in `📁 Workflows/[name]/` with CLAUDE.md (context) + workflow.md (step guide). Invoke by pointing Claude at the folder: "Run @Workflows/metrics-health-check/".

| Workflow | Purpose | Cadence |
|----------|---------|---------|
| `metrics-health-check` | Pendo + OKR + PRD targets → health check + action | Weekly |
| `qpr-prep` | Quarterly deck + trade-off narrative for exec review | Quarterly |
| `weekly-stakeholder-update` | Red/yellow/green status update, under 500 words | Weekly |
| `customer-research-synthesis` | Granola notes → persistent research themes in Knowledge/ | Ongoing |

---

### /product-depth
**User intent**: Build deep operational knowledge of a product — for demo preparation, change awareness, or support signal mapping

**Command syntax**:
```bash
/product-depth [--product <name>] [--mode demo|changelog|confusion]
```

**When to suggest**:
- "I need demo background on [product]"
- "Where do customers get confused with [product]?"
- "What changed in [product] recently?"
- "I'm demoing [product] next week"
- "Product deep dive on [product]"
- "Help me know [product] better before my call"
- "What are the top use cases for [product]?"

**NOT for**:
- Full demo guide preparation for a specific customer (use `/demo-prep`)
- Competitive product knowledge (use `/compete`)

---

### /demo-prep
**User intent**: Create a complete demo guide for a specific product and audience — story arc, feature spotlights, competitive awareness, demo traps

**Command syntax**:
```bash
/demo-prep [--product <name>] [--persona <type>] [--duration <minutes>] [--scenario <description>]
```

**When to suggest**:
- "Prepare a demo guide for [product]"
- "I'm demoing [product] to [persona]"
- "Help me prepare for a customer demo"
- "Demo guide for [product]"
- "I have a demo next [day] — help me prep it"
- "What should I show in my [product] demo?"

**NOT for**:
- General product knowledge building (use `/product-depth`)
- Pre-meeting prep without a demo component (use `/prep`)

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
- "What's the cost-to-serve implication of [feature]?"
- "Help me think through the business model"

**NOT for**:
- Full spec writing (use `/spec`)
- Strategic framing without financial grounding (use `/think`)

---

### /data-story
**User intent**: Package existing data or analysis for a specific audience — executive, product, sales, or customer success

**Command syntax**:
```bash
/data-story [--audience exec|product|sales|cs] [--source <analysis or finding>]
```

**When to suggest**:
- "Turn this finding into a story for [exec|sales|CS]"
- "Package this data for leadership"
- "How do I communicate this Pendo finding to [audience]?"
- "Make this exec-ready"
- "I have this data — help me present it to [person]"
- "Translate this analysis for the sales team"
- "What's the CS-facing version of this insight?"

**NOT for**:
- Running the analysis itself (use `/pendo` or the b2b-data-analyst skill)
- Writing formal documents (use `/write`)

---

### /persona-sync
**User intent**: Close the signal-to-persona feedback loop — surface how recent signals should update persona files, with evidence-based thresholds and explicit confirmation

**Command syntax**:
```bash
/persona-sync [--persona <name>] [--signals-window <days>]
```

**When to suggest**:
- "Update our personas from recent signals"
- "Do my signals change the persona?"
- "Persona refresh based on what we've learned"
- "How has the [RTE|VP Eng|PMO] persona changed?"
- "Signal-to-persona alignment check"
- "Are our personas still accurate?"

**NOT for**:
- Adding individual signals (use `/signal`)
- Auditing customer knowledge coverage (use `/customer-knowledge-audit`)

---

### /customer-knowledge-audit
**User intent**: Score the depth and health of customer knowledge across 5 dimensions — coverage, recency, depth, breadth, and action-linkage

**Command syntax**:
```bash
/customer-knowledge-audit [--depth quick|full] [--persona <name>]
```

**When to suggest**:
- "How well do I know my customers?"
- "Where are my customer knowledge gaps?"
- "Blind spots on [persona] or customers generally?"
- "Audit my customer understanding"
- "Customer knowledge score"
- "Which personas am I weakest on?"
- "Am I using customer evidence in my decisions?"

**NOT for**:
- Signal capture (use `/signal`)
- Persona updates from signals (use `/persona-sync`)

---

### /industry-brief
**User intent**: Run a market intelligence scan — analyst coverage, adjacent market moves, earnings signals, or job posting demand patterns

**Command syntax**:
```bash
/industry-brief [--mode analyst|market|earnings|jobs] [--save]
```

**When to suggest**:
- "What are analysts saying about [SPM|agile planning|our market]?"
- "Industry trends in agile planning"
- "Gartner or Forrester on our market"
- "Adjacent market moves we should watch"
- "Enterprise software earnings signals"
- "Broader market scan"
- "What's happening in the industry?"
- "Job posting signals for [role/capability]"

**NOT for**:
- Direct competitor pricing (use `/price-intel`)
- Head-to-head competitive battlecards (use `/compete`)

---

## Intelligence Command Routing

When you need competitive or market intelligence, use this map:

| I need to… | Use |
|---|---|
| Monitor what's happening in my market today | `/daily-brief` |
| Deep-dive on a specific competitor or generate a battlecard | `/compete [--focus name] [--output battlecard]` |
| Analyze a deal we won, lost, or didn't close | `/win-loss` |
| Research pricing strategy or competitor pricing | `/price-intel` |
| Scan analyst/earnings/market signals (beyond competitors) | `/daily-brief --industry` (quick) or `/industry-brief` (deep) |

**Rule**: Start with `/daily-brief` for ongoing awareness. Escalate to `/compete` when you need depth on a specific competitor. `/win-loss` after every deal close.

---

## Quick Reference Table

| User Says... | Suggest Command |
|--------------|-----------------|
| "What should I work on today?" | /today |
| "Figure out our Q1 OKRs" | /think |
| "Should we do X or Y?" | decision-quality skill |
| "Write a spec for feature X" | /spec |
| "Find patterns in customer feedback" | synthesize skill |
| "Score these 5 features" | /prioritize (command) |
| "Rank my Q2 sprint" | /prioritize (command) |
| "Triage 50 customer requests" | prioritization-craft (skill) |
| "Process raw feedback for roadmap" | prioritization-craft (skill) |
| "Build roadmap with stakeholder comms" | prioritization-craft (skill) |
| "Research customer needs" | /discover |
| "Update memory with session" | /refresh-memory |
| "Search our previous conversations" | /remember |
| "Get stakeholder buy-in" | /align |
| "Write executive brief" | /write |
| "Generate Spec Brief from PRD" | /spec-brief |
| "Validate this assumption" | /research |
| "What metrics to track?" | /measure |
| "Track my OKR progress" | /okr-progress |
| "Analyze competitor X" | /compete |
| "Daily competitive briefing" | /daily-brief |
| "Help me brainstorm solutions" | /brainstorm |
| "Teach me how this works" | /learning-opportunity |
| "Post-launch learning" | /learn |
| "Plan the launch" | /ship |
| "Create a mockup" | /mockup |
| "Refine this UI until polished" | /ui-refine |
| "Strategic narrative" | /narrative |
| "New to AIPMOS" | /onboard |
| "Report a bug" | /bug-report |
| "Critique this design" | /critique |
| "Pricing research" | /price-intel |
| "Extract meeting notes" | /granola |
| "Remember this decision" | /capture-pattern |
| "What's new in Claude Code / Cowork / Desktop for us?" | /dex-improve |
| "Audit our hooks and skills setup" | /dex-improve |
| "Run QPR prep" | /workflow (e.g. @Workflows/qpr-prep/) |
| "Weekly stakeholder update" | /workflow (e.g. @Workflows/weekly-stakeholder-update/) |
| "Generate design brief from PRD" | /design-brief |
| "Break this PRD into stories" | /story |
| "Create a Q2 roadmap document" | /roadmap |
| "Prep me for my meeting with..." | /prep |
| "Equip my champion before their exec review" | /prep (champion briefing mode) |
| "Log a customer signal" | /signal |
| "Customer said X on a call" | /signal |
| "Heard from [customer] that..." | /signal |
| "Send follow-up from meeting" | /follow-up |
| "Communicate what we decided" | /follow-up |
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
| "Demo background on [product]" | /product-depth |
| "What changed in [product] recently?" | /product-depth --mode changelog |
| "Where do customers get confused with [product]?" | /product-depth --mode confusion |
| "Prepare a demo guide for [product]" | /demo-prep |
| "I'm demoing [product] to [persona]" | /demo-prep |
| "Build a business case for [feature]" | /biz-case |
| "What will Finance/CS/Sales say about this?" | /biz-case --mode perspective |
| "Package this data for leadership" | /data-story --audience exec |
| "Translate this analysis for sales" | /data-story --audience sales |
| "Update our personas from recent signals" | /persona-sync |
| "Are our personas still accurate?" | /persona-sync |
| "How well do I know my customers?" | /customer-knowledge-audit |
| "Where are my customer knowledge gaps?" | /customer-knowledge-audit --depth quick |
| "What are analysts saying about our market?" | /industry-brief --mode analyst |
| "Broader market scan" | /industry-brief |

**Dual-Mode Commands**: Some capabilities have both a quick command and a deep skill variant:
- **/prioritize** (quick) vs **prioritization-craft skill** (expanded): Quick scoring vs. prioritization support that starts with outcome/constraint framing and can expand into deeper triage and stakeholder communication
- **/think** (quick) vs **strategic-thinking skill** (expanded): Quick strategic framing vs. strategic decision support that starts consultatively, then makes the call and expands for high-stakes work

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
