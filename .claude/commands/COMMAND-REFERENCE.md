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

**NOT for**:
- Writing a spec document (use /spec)
- Daily task planning (use /today)
- Making a specific decision (use /decide)
- Research interviews (use /discover)

---

### /synthesize
**User intent**: Pattern analysis across multiple data sources

**When to suggest**:
- "Find patterns in..."
- "Synthesize customer feedback"
- "Analyze these interviews/tickets"
- "What patterns do you see in..."
- "Consolidate these requests"
- "Cross-source analysis of..."
- "Pull together insights from multiple sources"

**NOT for**:
- Planning research (use /discover)
- Real-time prioritization/triage (use /prioritize)
- Single document analysis (read it directly)

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

**How to invoke**: Point at the workflow folder; e.g. "Let's run the QPR prep workflow @Workflows/qpr-prep/" or "Do the weekly update @Workflows/weekly-stakeholder-update/". Claude reads that workflow's CLAUDE.md and workflow.md and follows the step guide.

**Available workflows**: `📁 Workflows/qpr-prep/`, `📁 Workflows/weekly-stakeholder-update/`, `📁 Workflows/customer-research-synthesis/`

**NOT for**:
- One-off tasks (use /today or project folder)
- Single prompt/skill (use a slash command or skill)

---

### /spec
**User intent**: Create formal specifications, PRDs, documentation

**Command syntax**:
```bash
/spec [--type <format>] [--skip-discovery] [--save] [<feature-description>]
```

**Arguments**:
- `--type full|light|one-pager`: PRD format (default: `full`)
- `--skip-discovery`: Skip Socratic questioning
- `--save`: Save PRD to file
- `<feature-description>`: Initial feature/idea description

**When to suggest**:
- "Write a spec for..."
- "Create a PRD for..."
- "Document this feature..."
- "Specification for..."
- "Write product requirements for..."
- "Create technical spec..."
- `/spec "Native Project Milestones in Roadmaps"` - with initial idea
- `/spec --type light "Card blocking improvements"` - lightweight spec
- `/spec --skip-discovery "API rate limiting"` - skip discovery phase

**NOT for**:
- Strategic thinking (use /think first)
- Problem discovery (use /discover first)
- Quick documentation (use /write)

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
- Strategic decisions (use /think or /decide)

**Dual-Mode Note**: For complex prioritization requiring raw feedback processing, stakeholder communication, or strategic validation, use the **prioritization-craft skill** instead. The skill provides a 4-phase deep prioritization process (30-45 min) with triage, deduplication, categorization, multiple frameworks, and stakeholder communication packages.

---

### prioritization-craft (Skill)
**User intent**: Deep prioritization with stakeholder communication (30-45 min)

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
- Checking what changed (use /check-progress)
- Daily planning (use /today)
- Viewing memory content (read the file directly)

---

### /decide
**User intent**: Make a specific choice between options

**When to suggest**:
- "Should we do X or Y?"
- "Help me decide between..."
- "Go/no-go decision for..."
- "Choose option A or B"
- "Make a decision on..."

**NOT for**:
- Strategic framing (use /think first)
- Prioritization (use /prioritize)
- Research validation (use /discover or /research)

---

### /discover
**User intent**: Problem exploration and customer research

**When to suggest**:
- "I need to understand the problem space"
- "Research customer needs for..."
- "Discovery for..."
- "Validate problem assumptions"
- "Customer research on..."
- "Explore the opportunity in..."

**NOT for**:
- Writing specs (use /spec after discovery)
- Detailed research planning (use /research)
- Synthesizing existing data (use /synthesize)

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
- Use the **research skill** (via Skill tool) - combines planning framework with automated execution using web search, content fetching, and workspace integrations

**NOT for**:
- Open-ended discovery (use /discover)
- Synthesizing findings (use /synthesize after research)
- Daily planning (use /today)

**Command vs. Skill**:
- `/research` command = Research planning framework (defines scope, methods, success criteria)
- `research` skill = Research execution (fetches sources, analyzes content, synthesizes findings)

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
- Making the decision yourself (use /decide)
- Technical analysis

---

### /write
**User intent**: Draft communication or documentation

**When to suggest**:
- "Draft an email to..."
- "Write executive summary for..."
- "Create announcement for..."
- "Draft customer communication..."
- "Write a blog post about..."
- "Stakeholder update on..."

**NOT for**:
- Strategic analysis (analyze first)
- Full PRD creation (use /spec)
- Technical specifications

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
**User intent**: Competitive intelligence and analysis

**When to suggest**:
- "Analyze [competitor]"
- "Competitive analysis of..."
- "What are competitors doing?"
- "Market positioning vs..."
- "Competitive matrix for..."
- "Intelligence on [competitor]"

**NOT for**:
- Daily competitive briefs (use /daily-brief)
- Pricing research (use /price-intel)

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
- Making a specific decision (use /decide)

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
**User intent**: Capture semantic learning to accumulated wisdom file

**When to suggest**:
- "Remember this decision..."
- "Capture this pattern..."
- "Save this learning..."
- "This is worth remembering..."
- After completing a substantial feature or decision
- When you notice a workspace-specific convention
- After making a mistake that wasted time

**NOT for**:
- Current state updates (use /refresh-memory)
- Daily planning (use /today)
- Strategic analysis (use /think)

---

### /granola
**User intent**: Extract meeting insights from Granola

**When to suggest**:
- "Extract meeting notes..."
- "Summarize meeting from..."
- "Action items from meeting..."

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

## Quick Reference Table

| User Says... | Suggest Command |
|--------------|-----------------|
| "What should I work on today?" | /today |
| "Figure out our Q1 OKRs" | /think |
| "Should we do X or Y?" | /decide |
| "Write a spec for feature X" | /spec |
| "Find patterns in customer feedback" | /synthesize |
| "Score these 5 features" | /prioritize (command) |
| "Rank my Q2 sprint" | /prioritize (command) |
| "Triage 50 customer requests" | prioritization-craft (skill) |
| "Process raw feedback for roadmap" | prioritization-craft (skill) |
| "Build roadmap with stakeholder comms" | prioritization-craft (skill) |
| "Research customer needs" | /discover |
| "Update memory with session" | /refresh-memory |
| "Get stakeholder buy-in" | /align |
| "Write executive brief" | /write |
| "Generate Spec Brief from PRD" | /spec-brief |
| "Validate this assumption" | /research |
| "What metrics to track?" | /measure |
| "Analyze competitor X" | /compete |
| "Daily competitive briefing" | /daily-brief |
| "Help me brainstorm solutions" | /brainstorm |
| "Teach me how this works" | /learning-opportunity |
| "Post-launch learning" | /learn |
| "Plan the launch" | /ship |
| "Create a mockup" | /mockup |
| "Strategic narrative" | /narrative |
| "New to AIPMOS" | /onboard |
| "Report a bug" | /bug-report |
| "Critique this design" | /critique |
| "Pricing research" | /price-intel |
| "Extract meeting notes" | /granola |
| "Remember this decision" | /capture-pattern |
| "Run QPR prep" | /workflow (e.g. @Workflows/qpr-prep/) |
| "Weekly stakeholder update" | /workflow (e.g. @Workflows/weekly-stakeholder-update/) |

**Dual-Mode Commands**: Some capabilities have both a quick command and a deep skill variant:
- **/prioritize** (quick) vs **prioritization-craft skill** (deep): Quick scoring vs. comprehensive prioritization with triage, deduplication, and stakeholder communication
- **/think** (quick) vs **strategic-thinking skill** (deep): Quick strategic framing vs. comprehensive 4-phase decision process

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
