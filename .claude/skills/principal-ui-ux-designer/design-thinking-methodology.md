# Design Thinking Methodology - Deep Dive

## The 5 Stages in Detail

### Stage 1: Empathize

**Goal**: Develop deep understanding of users' needs, barriers, and attitudes

**Core Mindset**: Set aside your assumptions. Approach with genuine curiosity.

**Methods & Techniques**:

```yaml
User Research:
  - 1:1 Interviews (30-60 min, open-ended questions)
  - Contextual Inquiry (observe users in their environment)
  - Diary Studies (capture behaviors over time)
  - Shadowing (day-in-the-life observation)
  - Empathy Mapping (say/think/do/feel)

Synthesis Methods:
  - Affinity Diagramming (cluster patterns)
  - Persona Development (archetypal users)
  - Journey Mapping (experiences over time)
  - Pain Point Identification (frustrations, workarounds)

Good Questions:
  - "Tell me about the last time you [task]..."
  - "Walk me through how you currently [workflow]..."
  - "What makes [situation] frustrating?"
  - "What tools do you wish you had?"
  - "What would make your day easier?"

Bad Questions:
  - "Would you use feature X?" (leading, hypothetical)
  - "Do you like [design]?" (subjective, not actionable)
  - "How much would you pay for...?" (inaccurate)
```

**Empathy Map Template**:
```
┌─────────────────────────────────────┐
│         USER [Persona Name]         │
├─────────────────────────────────────┤
│ SAYS                    │ THINKS    │
│ (What user expresses)   │ (Thoughts,│
│ - "I hate when..."      │  beliefs, │
│ - "I wish I could..."   │  concerns)│
│                         │           │
├─────────────────────────┼───────────┤
│ DOES                    │ FEELS     │
│ (Actions, behaviors)    │ (Emotions,│
│ - Clicks away after...  │  pains,   │
│ - Workarounds: uses...  │  hopes)   │
└─────────────────────────┴───────────┘
         │         INSIGHTS         │
         │ (Synthesis of patterns)  │
         └──────────────────────────┘
```

### Stage 2: Define

**Goal**: Synthesize research into clear, actionable problem statement

**Core Mindset**: Focus on the right problem, not just any problem.

**Methods & Techniques**:

```yaml
Problem Framing:
  - Problem Statements (user + need + insight)
  - Point of View (POV) Statements
  - "How Might We" Questions
  - 5 Whys (root cause analysis)
  - Constraint Identification

Synthesis Tools:
  - Insight Generation (patterns from research)
  - Theme Extraction (common threads)
  - Opportunity Areas (spaces for innovation)
  - User Stories (As a [user], I want [goal] so that [benefit])
```

**Problem Statement Formula**:
```
[User] needs [need] because [insight].

Example:
"Agile Program Managers need visibility into cross-team
dependencies because coordination overhead is the #1
barrier to predictable delivery in organizations with
50+ teams."
```

**How Might We (HMW) Questions**:
```
Narrow → Broad:
"HMW reduce the clicks required to..." (too narrow)
"HMW make dependency management..." (just right)
"HMW make enterprise software better" (too broad)

Generate HMWs:
- HMW show dependencies without overwhelming users?
- HMW make dependency status obvious at a glance?
- HMW enable proactive dependency resolution?
- HMW gamify dependency management compliance?
```

### Stage 3: Ideate

**Goal**: Generate diverse, creative solutions without judgment

**Core Mindset**: Quantity leads to quality. Build on others' ideas.

**Methods & Techniques**:

```yaml
Brainstorming Techniques:
  - Classic Brainstorm (group, verbal, build on ideas)
  - Brainwriting (silent, written, then share)
  - Worst Idea First (reverse psychology, reduces pressure)
  - Crazy 8s (8 sketches in 8 minutes)
  - SCAMPER (Substitute, Combine, Adapt, Modify, Put to other use,
            Eliminate, Reverse)

Idea Selection:
  - Dot Voting (democratic selection)
  - Impact/Effort Matrix (quickest wins, moonshots)
  - Theme Clustering (group similar ideas)
  - Constraint Checking (technical, business, user)
```

**Impact/Effort Matrix**:
```
HIGH IMPACT
  │
  │  [Moonshots]        │ [Quick Wins]
  │  High Impact,       │ High Impact,
  │  High Effort        │ Low Effort
  │  → Strategic bets   │ → Do these first
  │
  ├─────────────────────┼────────────────────→
  │
  │  [Money Pit]        │ [Fill-in Work]
  │  Low Impact,        │ Low Impact,
  │  High Effort        │ Low Effort
  │  → Avoid            │ → Backlog only
  │
  LOW                    HIGH
  EFFORT
```

**Brainstorming Rules**:
```
✅ DO:
  - Defer judgment (no idea is bad in generation)
  - Build on others' ideas ("yes, and...")
  - Encourage wild ideas
  - Be visual (sketch, diagram)
  - Stay focused on topic
  - One conversation at a time

❌ DON'T:
  - Critique ideas during generation
  - Dominated by loudest voices
  - Early convergence on first good idea
  - Problem-solving instead of idea generation
  - Analysis paralysis
```

### Stage 4: Prototype

**Goal**: Make ideas tangible to learn through interaction

**Core Mindset**: Build to think. Fail fast, learn faster.

**Fidelity Spectrum**:
```yaml
Low Fidelity (Hours to create):
  Purpose: Validate concepts, test hypotheses
  - Paper Sketches (napkin drawings)
  - Storyboards (comic-strip narratives)
  - Paper Prototypes (hand-drawn interfaces)
  - Click-Through Mockups (Figma/Sketch links)
  - Role-Playing (act out user journeys)

  Use When: Early validation, many concepts, low risk

Medium Fidelity (Days to create):
  Purpose: Test interactions, information architecture
  - Wireframes (structure without visual design)
  - Interactive Prototypes (limited functionality)
  - Mockups with Real Content (lorem ipsum → real copy)
  - Design System Components (reusable patterns)

  Use When: Refining interactions, stakeholder buy-in

High Fidelity (Weeks to create):
  Purpose: Final validation, handoff to development
  - Pixel-Perfect Designs (production-ready)
  - Working Code Prototypes (HTML/CSS/JS)
  - Interactive Demos (near-final experience)
  - User Testing with Target Audience (real-world validation)

  Use When: Final validation, development handoff
```

**Prototyping Principles**:
```
★ JUST ENOUGH REALISM
  - Test what you need to learn
  - Don't over-invest in unvalidated concepts
  - Users will forgive low fidelity if feedback is welcomed

★ LEARNING OVER PERFECTION
  - What question are you answering?
  - What assumption are you testing?
  - What will invalidate this approach?

★ ITERATE RAPIDLY
  - Version 1 → Test → Version 2 → Test → Version 3
  - Each iteration increases fidelity and confidence
  - Stop when you have clear answers
```

### Stage 5: Test

**Goal**: Validate solutions with real users to inform iteration

**Core Mindset**: Testing early saves money. Testing often ensures quality.

**Methods & Techniques**:

```yaml
Usability Testing:
  - Moderated Sessions (in-person or remote, 5-8 users)
  - Unmoderated Testing (users complete tasks independently)
  - A/B Testing (compare variants with data)
  - Tree Testing (evaluate information architecture)
  - Card Sorting (understand mental models)

Feedback Methods:
  - Think Aloud Protocol (users narrate their process)
  - Retrospective Interviews (reflect on experience)
  - System Usability Scale (SUS) Survey
  - Net Promoter Score (NPS)
  - Task Completion Rates (quantitative)
  - Time-on-Task (efficiency metric)
```

**Usability Test Structure** (60 min session):
```
WELCOME (5 min)
  - Set participant at ease
  - Explain process, "you're not being tested, the design is"
  - Consent forms, recording setup

WARM-UP (5 min)
  - Background questions
  - Establish context for their role/experience
  - Build rapport

TASKS (35 min)
  - 3-5 realistic tasks
  - "Think aloud as you work through this"
  - Observe silently, only intervene if truly stuck
  - Note: confusion, workarounds, emotions, aha moments

DEBRIEF (15 min)
  - "Overall, how was that experience?"
  - "What was easiest/most difficult?"
  - "What would make this better?"
  - "Is there anything else you'd like to share?"
```

**Testing Metrics**:
```yaml
Quantitative:
  - Task Success Rate (% who complete)
  - Time on Task (efficiency)
  - Error Rate (frequency/severity)
  - Error Recovery (% who recover without help)
  - SUS Score (0-100, 68+ is good)

Qualitative:
  - User quotes (verbatim, in context)
  - Observation notes (behaviors, emotions)
  - Pain points (frustrations, workarounds)
  - Delighters (unexpected positive reactions)
  - Feature requests (unmet needs)
```

**Iteration Loop**:
```
                    ┌─────────┐
                    │  Learn  │
                    └────┬────┘
                         │
                    ┌────▼────┐
          ┌─────────│  Ideate │◄────────┐
          │         └────┬────┘         │
          │              │              │
    ┌─────▼─────┐   ┌───▼────┐   ┌────▼────┐
    │  Test     │───│ Prototype│───│ Define  │
    └─────┬─────┘   └─────────┘   └─────────┘
          │
      ┌───▼────┐
      │Empathize│
      └────────┘

Non-linear, iterative. Cycle through stages as needed.
```

## Design Thinking in Practice

### Applied to SaaS Products

**Example: AgilePlace Dependency Management**

```
EMPATHIZE:
  - Interviewed 20 Agile Program Managers
  - Observed PI Planning sessions
  - Analyzed support tickets (dependency issues = 23% of volume)
  - Key insight: "I don't know who to talk to until it's too late"

DEFINE:
  - Problem Statement: "Agile Program Managers need proactive
    dependency visibility because reactive coordination causes
    delivery delays in 78% of cross-team features"
  - HMW Questions:
    - HMW surface dependencies without manual entry?
    - HMW make dependency status obvious at a glance?
    - HMW enable coordination before work begins?

IDEATE:
  - Generated 47 concepts
  - Selected 3 for prototyping:
    1. Dependency Graph Visualization
    2. Automated Dependency Detection
    3. Cross-Team Dependency Kanban Board

PROTOTYPE:
  - Click-through prototypes for all 3 concepts
  - 6 usability testing sessions
  - Concept 1 (Graph) found confusing by 5/6 users
  - Concept 2 (Auto-detection) most exciting, "this would save hours"
  - Concept 3 (Kanban) familiar but didn't solve proactive problem

TEST:
  - Built working prototype of Concept 2
  - Beta test with 5 customers
  - Results: 67% reduction in dependency-related delays
  - Feedback: "Need manual override for AI detection"

ITERATE:
  - Added manual dependency links
  - Released to market
  - Adoption: 84% of enterprise customers in first 6 months
```

### Facilitation Tips

**Design Thinking Workshop Structure** (Half-day):

```
INTRO (30 min)
  - Welcome, goals, agenda
  - Icebreaker (get creative juices flowing)
  - Explain design thinking, set expectations

EMPATHY (60 min)
  - Share research findings (if done beforehand)
  - Or: Quick empathy interviews with stakeholders
  - Create empathy maps in small groups

DEFINE (45 min)
  - Synthesize into problem statements
  - Group to identify themes
  - Select 1-2 core problems to solve

IDEATE (60 min)
  - Individual brainstorm (10 min)
  - Group share and build-on (30 min)
  - Cluster and vote (20 min)

PROTOTYPE (60 min)
  - Form teams around top ideas
  - Sketch or build rough prototypes
  - Prepare to share

SHARE & DEBRIEF (45 min)
  - Gallery walk (teams present concepts)
  - Feedback and discussion
  - Next steps, action items
```

**Common Pitfalls**:
```
❌ Solution-first thinking ("we need a dashboard")
   → Fix: Start with user need, not solution

❌ Research as afterthought ("we already know what users want")
   → Fix: Make empathy non-negotiable

❌ Brainstorming without constraints ("anything goes")
   → Fix: Clear problem statement, technical/business constraints

❌ Hi-fidelity first pass (pixel-perfect mockups)
   → Fix: Start with sketches, iterate fidelity upward

❌ Testing only at the end ("users will see it at launch")
   → Fix: Test early, test often, learn continuously

❌ Linear thinking ("must finish empathy before define")
   → Fix: Iterate nonlinearly, revisit stages as needed
```

## Resources

**Books**:
- *Change by Design* by Tim Brown
- *Designing for Growth* by Jeanne Liedtka
- *The Design of Everyday Things* by Don Norman

**Tools**:
- Miro, Mural (collaborative whiteboarding)
- Figma, Sketch (prototyping)
- Maze, UserTesting (unmoderated testing)
- Optimal Workshop (card sorting, tree testing)

**Templates**:
- See `templates/` directory for:
  - empathy-map-template.md
  - problem-statement-template.md
  - usability-test-script-template.md
  - retrospective-synthesis-template.md
