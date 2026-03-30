# UX Research Methods - Deep Dive

## Research Methods Matrix

```yaml
GENERATIVE RESEARCH (Discovery Phase):
  Goal: Understand user needs, behaviors, pain points
  When: Before defining product/features
  Methods: Interviews, diary studies, observation, surveys

EVALUATIVE RESEARCH (Validation Phase):
  Goal: Test solutions, measure success
  When: During design/development
  Methods: Usability testing, A/B testing, surveys

QUALITATIVE (Why & How):
  Depth: Rich, detailed insights
  Sample: Small (5-10 participants)
  Analysis: Thematic, patterns

QUANTITATIVE (What & How Much):
  Breadth: Measurable, generalizable
  Sample: Large (100+ participants)
  Analysis: Statistical, trends
```

## Core Research Methods

### 1. User Interviews

```yaml
PURPOSE:
  Understand user needs, behaviors, motivations, pain points
  Exploratory (discovery) or validation (confirmation)

STRUCTURE:
  1. Introduction (5 min): Set context, build rapport
  2. Warm-up (5 min): Background, context setting
  3. Core questions (30-40 min): Main inquiry
  4. Reflection (10 min): "Is there anything else?"
  5. Closing (5 min): Next steps, thank you

QUESTION TYPES:

Open-Ended:
  ✅ "Tell me about the last time you..."
  ✅ "Walk me through how you currently..."
  ✅ "What makes [situation] challenging?"
  ❌ "Do you like feature X?" (leading, hypothetical)
  ❌ "How much would you pay?" (inaccurate)

Probing:
  "Can you say more about that?"
  "What do you mean by...?"
  "Can you give me an example?"
  "Why is that important to you?"

Magic Wand:
  "If you could wave a magic wand, what would you change?"
  "What would make this experience perfect?"

Five Whys:
  "Why?" (repeated 5 times to reach root cause)
  Example:
    "I'm frustrated with this process."
    "Why?" → "It takes too long."
    "Why does it take too long?" → "I have to wait for approvals."
    "Why do you wait?" → "I don't know when they're done."
    "Why don't you know?" → "No status updates."
    "Why no updates?" → "No automated notifications."

BEST PRACTICES:
  - Record with permission (audio, video, notes)
  - 2 interviewers (one leads, one takes notes)
  - Neutral environment (avoid bias)
  - Interview in pairs (diverse perspectives)
  - Debrief immediately (capture insights)
  - 45-60 minutes max (respect participant time)

SAMPLE SIZE:
  - 5-8 interviews per user segment (identifies 80% of themes)
  - More segments = more interviews
  - Saturation point: New interviews don't reveal new themes
```

### 2. Usability Testing

```yaml
PURPOSE:
  Evaluate how easily users can accomplish tasks
  Identify problems, measure success, guide improvements

TYPES:

Moderated (In-Person or Remote):
  - Facilitator guides session
  - Think-aloud protocol (users narrate process)
  - Can ask clarifying questions
  - Rich qualitative data
  - 5-8 participants per user type

Unmoderated (Remote):
  - Users complete tasks independently
  - Automated recording (screen, audio, clicks)
  - Larger sample possible (20-100+)
  - Quantitative metrics (completion rate, time)
  - Tools: UserTesting, Maze, Lookback

SESSION STRUCTURE (60 min):

Welcome (5 min):
  "Thank you for participating. You're helping us evaluate
   [product name]. There are no wrong answers.
   Think aloud as you work through tasks."

Warm-Up (5 min):
  Background questions
  Establish context for their role/experience
  Build rapport

Tasks (35 min):
  3-5 realistic tasks
  "Show me how you would [task]"
  Observe silently, only intervene if truly stuck
  Note: confusion, workarounds, emotions, aha moments

Debrief (15 min):
  "Overall, how was that experience?"
  "What was easiest/most difficult?"
  "What would make this better?"
  "Is there anything else you'd like to share?"

TASK WRITING CHECKLIST:
  ☐ Realistic (based on actual user goals)
  ☐ Specific (clear what success looks like)
  ☐ Self-contained (all info needed to complete)
  ☐ Neutral (doesn't lead toward solution)
  ☐ Testable (can observe completion)

  Example (BAD):
  "Use the dependency feature to manage cross-team
   dependencies." (too instructional, leads to solution)

  Example (GOOD):
  "You need to coordinate a feature that depends on work
   from another team. Show me how you'd handle this."
  (natural, tests real workflow)

METRICS:
  - Task Success Rate (% who complete)
  - Time on Task (efficiency)
  - Error Rate (frequency/severity)
  - Error Recovery (% who recover without help)
  - SUS Score (System Usability Scale, 0-100, 68+ is good)
  - NPS (Net Promoter Score, -100 to +100)
```

### 3. Surveys

```yaml
PURPOSE:
  Gather quantitative data from many users
  Validate findings from qualitative research
  Track satisfaction over time

SURVEY DESIGN:

Length:
  - 5-10 questions (max 5 minutes to complete)
  - Longer surveys see dramatic drop-off
  - Pilot test first (catch issues)

Question Order:
  1. Easy, warm-up questions
  2. Main inquiry
  3. Demographics (personal questions last)
  4. Open-ended feedback

Question Types:

Multiple Choice (Single Answer):
  "Which role best describes you?"
  ○ Product Manager
  ○ Engineer
  ○ Designer
  ○ Other: _______

Multiple Choice (Select All):
  "Which features do you use regularly? (Select all)"
  ☐ Dashboard
  ☐ Reports
  ☐ Team Management
  ☐ Integrations

Likert Scale:
  "How satisfied are you with the dashboard?"
  Very Dissatisfied ○ ○ ○ ○ ○ Very Satisfied
  (5-7 point scale recommended)

Open-Ended:
  "What would make this product better for you?"
  [Text box for free response]

BEST PRACTICES:
  - One question at a time (avoid double-barreled)
  - Neutral wording (no leading questions)
  - Avoid jargon (speak user's language)
  - Provide "Other" option (capture unanticipated answers)
  - Required vs optional (mark required clearly)
  - Progress indicator (how many questions remain)

DISTRIBUTION:
  - In-app (contextual, relevant)
  - Email (broad reach, lower response rate)
  - Website (general audience)
  - Incentives (gift cards, discounts improve response)

RESPONSE RATES:
  - In-app: 10-30% (good context)
  - Email: 5-15% (depends on relationship)
  - Incentives: Can double response rate
```

### 4. Card Sorting

```yaml
PURPOSE:
  Understand how users organize information
  Inform information architecture, navigation, categories

TYPES:

Open Card Sorting:
  - Users group items into categories they create
  - Users name their own categories
  - Discover: Mental models, natural groupings

Closed Card Sorting:
  - Users group items into predefined categories
  - Test: Proposed category structure
  - Validate: Does organization make sense?

HYBRID APPROACH:
  1. Open sort (5-10 users): Discover natural groupings
  2. Create proposed structure based on findings
  3. Closed sort (10-15 users): Validate proposed structure

CONDUCTING CARD SORTS:

In-Person:
  - Physical index cards (one item per card)
  - 30-60 items max (cognitive load)
  - Think aloud while sorting
  - 15-20 sessions (reveals 80% of patterns)

Remote (Tools):
  - OptimalSort, UserTesting, XMind
  - Larger sample possible (50-100+)
  - Quantitative analysis (dendrograms, similarity matrices)

ANALYSIS:

Dendrogram (Tree Diagram):
  - Visual representation of how often items grouped together
  - Identify: Clear clusters, ambiguous items

Standardization (Agreement):
  - Percent of users who grouped items together
  - High agreement = clear mental model
  - Low agreement = multiple valid approaches

Qualitative Insights:
  - User comments during sorting
  - Confusion about items
  - Suggested category names
  - "Would put this in two places" (cross-linking)

CHECKLIST:
  ☐ Items are clear (no jargon, ambiguous terms)
  ☐ Items are comprehensive (covering key content)
  ☐ Items are scannable (short, descriptive labels)
  ☐ Instructions are clear
  ☐ Pilot test first (catch confusing items)
```

### 5. Tree Testing

```yaml
PURPOSE:
  Evaluate information architecture (navigation, labels)
  Test: Can users find content using proposed structure?

METHOD:
  - Users complete tasks: "Find where to [X]"
  - Tree structure only (no visual design)
  - Click through navigation to find item
  - Success, wrong path, or abandonment

METRICS:
  - Success Rate (% who find correct item)
  - Time on Task (how long to find)
  - Directness (% who took optimal path)
  - First Click (where users start, predicts 80% of success)

TOOLS:
  - TreeJack (OptimalWorkshop)
  - UserTesting
  - Maze

SAMPLE SIZE:
  - 30-50 users per tree
  - Identifies major navigation issues

ANALYSIS:

First Click Analysis:
  - Most common first click = expected location
  - Low agreement = unclear categorization

Success Rate:
  - 80%+ success = Good structure
  - 50-80% = Needs improvement
  - <50% = Major restructuring needed

Path Analysis:
  - Where do users go wrong?
  - Which labels confuse?
  - Are there dead ends?

COMPARISON:
  Test multiple tree structures:
  - Proposed structure vs current
  - Different label variations
  - Different grouping approaches
```

### 6. A/B Testing

```yaml
PURPOSE:
  Compare two versions to measure which performs better
  Data-driven decisions, validate design choices

EXPERIMENT DESIGN:

Hypothesis:
  "If we [change], then [metric] will [improve]
   because [rationale]"

  Example:
  "If we add example projects to onboarding,
   then activation rate will increase by 10%
   because users will understand value faster."

Variants:
  - Control (current design)
  - Variant A (proposed improvement)
  - Variant B (alternative approach, optional)

Metrics:
  - Primary: Key success metric (activation, conversion)
  - Secondary: Supporting metrics (engagement, retention)
  - Guardrail: Negative indicators (churn, errors)

Sample Size:
  - Minimum: 1,000 users per variant (statistical power)
  - Duration: 2-4 weeks (full user lifecycle)
  - Significance: 95% confidence (p < 0.05)

TOOLS:
  - Optimizely, VWO, LaunchDarkly (feature flags)
  - Amplitude, Mixpanel, Google Analytics (analysis)

WHAT TO TEST:
  - Call-to-action text ("Sign Up" vs "Get Started")
  - Button placement (above fold vs below)
  - Form length (3 fields vs 5 fields)
  - Visual design (color, size, layout)
  - Content (short vs long description)
  - Onboarding flow (with vs without sample data)

WHAT NOT TO TEST:
  - Don't test big changes (A/B for incremental optimization)
  - Don't test without hypothesis (data exploration ≠ validation)
  - Don't stop test early (wait for statistical significance)
  - Don't ignore segments (win for one segment may lose for another)

ANALYSIS:

Statistical Significance:
  - P-value < 0.05 (95% confidence not due to chance)
  - Confidence interval (range of likely true effect)

Practical Significance:
  - Is the difference meaningful for business?
  - 1% improvement may not be worth implementation cost

Segment Analysis:
  - Break down by user type, company size, geography
  - Overall win may hide segment losses
  - Personalization may be better than one-size-fits-all
```

### 7. Diary Studies

```yaml
PURPOSE:
  Understand behaviors over time (longitudinal)
  Capture: Context, frequency, routines, pain points

METHOD:
  - Users record experiences over days/weeks
  - Daily entries (structured prompts)
  - Photos/screenshots encouraged
  - Check-ins from researcher (maintain engagement)

PROMPTS:
  - "Describe a time when you felt [frustration/success]"
  - "What tools did you use today?"
  - "What problems did you encounter?"
  - "How did you solve [problem]?"
  - "Screenshot what you're working on"

DURATION:
  - 1-2 weeks (enough to see patterns)
  - Daily entries (maintain habit)
  - Weekly reflection (synthesize learning)

RECRUITMENT:
  - 8-12 participants (attrition expected)
  - Incentive for completion (gift card)
  - Regular check-ins (maintain motivation)

ANALYSIS:
  - Patterns over time (routines, frequency)
  - Context dependencies (when/where problems occur)
  - Workarounds (how users cope with problems)
  - Evolution (sentiment, learning curve)
```

### 8. Field Studies

```yaml
PURPOSE:
  Observe users in their natural environment
  Context: Where work happens, real-world constraints

TYPES:

Contextual Inquiry:
  - User works while researcher observes
  - Interrupt to ask "why are you doing that?"
  - Real-time observation + inquiry

Shadowing:
  - Observe without interruption
  - Take notes on behaviors, environment
  - Debrief after observation session

 ethnography:
  - Immersive observation (days/weeks)
  - Understand culture, social dynamics
  - Rare for software (more common for physical products)

BENEFITS:
  - See real-world context (missed in interviews)
  - Discover unexpected behaviors
  - Understand environmental constraints
  - Identify workarounds (reveal design gaps)

CHALLENGES:
  - Access (must go to user location)
  - Time (travel + observation)
  - Cost (higher than lab research)
  - Analysis (lots of qualitative data)

SAMPLE SIZE:
  - 5-10 site visits (80% of patterns)
  - More for diverse contexts (different environments)

ANALYSIS:
  - Affinity diagramming (cluster observations)
  - Journey mapping (experiences over time)
  - Pain point themes
  - Environmental constraints
```

## Choosing the Right Method

### Decision Framework

```yaml
DISCOVERY PHASE (Before Design):
  Goal: Understand problem space, user needs

  Methods:
    - User Interviews (deep understanding)
    - Field Studies (context, environment)
    - Diary Studies (behaviors over time)
    - Surveys (broad sample, validate assumptions)

  Sample: 10-20 interviews, 50-200 surveys

DEFINITION PHASE (Framing Problem):
  Goal: Synthesize research, define opportunity

  Methods:
    - Affinity Diagramming (cluster patterns)
    - Persona Development (archetypal users)
    - Journey Mapping (experiences over time)
    - Problem Statements (clear articulation)

  Sample: Analysis of discovery research

DESIGN PHASE (Creating Solutions):
  Goal: Generate and validate concepts

  Methods:
    - Card Sorting (information architecture)
    - Tree Testing (navigation validation)
    - Concept Testing (value proposition)
    - Wireframe Testing (interaction feedback)

  Sample: 15-30 card sorts, 30-50 tree tests

VALIDATION PHASE (Testing Solutions):
  Goal: Measure success, iterate improvements

  Methods:
    - Usability Testing (task completion)
    - A/B Testing (measure improvement)
    - Surveys (satisfaction, NPS)
    - Analytics (usage patterns, funnel analysis)

  Sample: 5-8 usability tests, 1,000+ for A/B

LAUNCH PHASE (Post-Launch):
  Goal: Measure real-world performance, identify improvements

  Methods:
    - Analytics (feature usage, retention)
    - Surveys (satisfaction, feedback)
    - Support Analysis (pain points, common issues)
    - Interviews (deep dive on specific topics)

  Sample: All users (analytics), 50-200 surveys
```

### Research Plan Template

```yaml
RESEARCH OBJECTIVES:
  What do we want to learn?
  What decisions will this inform?

RESEARCH QUESTIONS:
  Specific questions to answer
  Hypotheses to validate

METHODS:
  Which methods and why?
  How do methods complement each other?

PARTICIPANTS:
  Who to recruit?
  How many per user segment?
  Screening criteria?

TIMELINE:
  When will research happen?
  How long for each method?

BUDGET:
  Tools (software licenses)
  Incentives (gift cards, payments)
  Recruiting (services, time)
  Travel (if field studies)

DELIVERABLES:
  What will be produced?
  (Report, presentation, video highlights, recommendations)

TEAM:
  Who is involved?
  (Researcher, designer, PM, stakeholders)

ETHICS:
  Informed consent
  Data privacy and storage
  Participant compensation
```

## Data Analysis & Synthesis

### Affinity Diagramming

```yaml
PURPOSE:
  Cluster research data into themes
  Identify patterns across participants

PROCESS:
  1. Capture observations (notes, quotes, behaviors)
  2. Write each on sticky note (physical or digital)
  3. Group notes into clusters (affinities)
  4. Label clusters with themes
  5. Super-clusters (group themes)

TOOLS:
  - Physical: Sticky notes, whiteboard, sharpies
  - Digital: Miro, Mural, FigJam, FunRetro

BEST PRACTICES:
  - Cross-functional team (diverse perspectives)
  - 2-3 hours (sufficient data, avoids fatigue)
  - Silent grouping first (avoid bias)
  - Discuss disagreements (different interpretations)
  - Photo evidence (share with stakeholders)
```

### Insight Generation

```yaml
FROM DATA TO INSIGHTS:

Observations (Raw Data):
  "Users click Settings then immediately click back"

Pattern (Multiple Observations):
  "8 of 10 users click Settings then back"

Insight (Interpretation):
  "Users expect profile settings in a different location"
  "Settings doesn't signal what's inside"

Implication (Action):
  "Rename Settings to 'Profile & Preferences'"
  "Or move profile to top-level navigation"

INSIGHT FRAMEWORKS:

"Why" Ladder:
  What did users do?
  Why did they do it?
  What does that tell us?
  So what? (implications)
  Now what? (actions)

Problem Statement:
  [User] needs [need] because [insight]

  Example:
  "Agile Program Managers need proactive dependency
   visibility because reactive coordination causes delivery
   delays in 78% of cross-team features"

Opportunity Statement:
  How might we [enable user] to [outcome]?

  Example:
  "How might we surface dependencies without manual entry?"
```

### Communicating Findings

```yaml
RESEARCH REPORT STRUCTURE:

Executive Summary (1 page):
  - Key findings (3-5 bullets)
  - Recommendations (prioritized)
  - Business impact

Background:
  - Research objectives
  - Methods used
  - Participants (who, how many)

Key Findings:
  - Themed insights (with supporting data)
  - Direct quotes (bring users to life)
  - Photos/videos (when available)
  - Pain points and opportunities

Recommendations:
  - Prioritized by impact/effort
  - Specific and actionable
  - Rationale (linked to findings)
  - Success metrics

Appendices:
  - Detailed methodology
  - Full transcript excerpts
  - Participant profiles
  - Additional data

PRESENTATION TIPS:
  - Start with user stories (emotional hook)
  - Use quotes and photos (humanize data)
  - Visualize data (charts, clusters)
  - Clear recommendations (what to do next)
  - Keep to 30 minutes (stakeholder attention)
```

## Ethics & Professional Practice

```yaml
INFORMED CONSENT:
  - Explain research purpose
  - Describe what will happen
  - Explain recording (audio, video, screen)
  - Clarify voluntary participation
  - Offer opportunity to ask questions
  - Allow withdrawal at any time

PRIVACY:
  - Anonymize data (remove identifying information)
  - Secure storage (encrypted, access controlled)
  - Retention policy (delete after X days/months)
  - Share only aggregated findings

COMPENSATION:
  - Fair payment for time (typically $50-150/hour)
  - Gift cards or direct payment
  - Offer regardless of completion (if they show up)

INCLUSIVITY:
  - Recruit diverse participants
  - Accessibility accommodations
  - Respect cultural differences
  - Avoid bias in recruiting (e.g., all-male panels)

PROFESSIONALISM:
  - Be on time (respect participant's time)
  - Follow through (send promised compensation)
  - Say thank you (build goodwill)
  - Share findings (optional, participants curious)
```

## Resources

**Books**:
- *Just Enough Research* by Erika Hall
- *Interviewing Users* by Steve Portigal
- *Rocket Surgery Made Easy* by Steve Krug
- *Handbook of Usability Testing* by Jeff Rubin

**Tools**:
- User Research: UserTesting, Lookback, Maze
- Card Sorting: OptimalSort, UserZoom
- Tree Testing: TreeJack, UserTesting
- Surveys: Typeform, SurveyGizmo, Google Forms
- Analysis: Dovetail, Aurelius, Notion

**Organizations**:
- Nielsen Norman Group (nngroup.com)
- User Experience Professionals Association (uxpa.org)
- Interaction Design Association (interaction-design.org)

**Templates**:
- See `templates/` directory for:
  - research-plan-template.md
  - interview-guide-template.md
  - usability-test-script-template.md
  - survey-question-bank.md
  - research-report-template.md
