# Socratic Questioning Framework

Sharpen feature thinking through targeted questions that help move from vague ideas to clear, well-reasoned feature definitions.

## Core Philosophy

**Goal**: Help think more clearly, not challenge or interrogate.

### Good Socratic Questioning
✅ Helps uncover assumptions
✅ Clarifies fuzzy thinking
✅ Surfaces potential issues early
✅ Strengthens the rationale

### Bad Socratic Questioning
❌ Feels like an interrogation
❌ Makes defensive
❌ Asks "gotcha" questions
❌ Questions just to question

---

## How to Use This Framework

### Step 1: Analyze Input
Identify gaps in the user's feature idea:
- Problem clarity - Is the problem well-defined and evidence-based?
- Solution rationale - Why this solution over alternatives?
- Success criteria - How will we measure success?
- Constraints - What are the limitations and trade-offs?
- Strategic fit - Why this feature, why now?

### Step 2: Select Questions
Choose **3-5 questions total** from the five categories below.

Pick the most relevant based on the biggest gaps identified.

**Priority ranking**:
1. Problem clarity (most critical - always ask if unclear)
2. Success criteria (second most critical)
3. Solution validation
4. Constraints & trade-offs
5. Strategic fit

### Step 3: Ask and Listen
- Ask questions one at a time (don't overwhelm)
- Wait for complete answers
- Listen for red flags (vague language, lack of evidence, unclear success)
- Follow up if answers are weak
- Acknowledge strong answers

### Step 4: Coaching Response
If user struggles:
- Offer multiple-choice options
- Share examples from other contexts
- This is a learning tool, not a test

If answer is weak:
- Ask follow-up: "Can you say more about that?"
- Probe gently: "What evidence supports that?"
- Offer alternative: "Some might argue X, how would you respond?"

If answer is great:
- Acknowledge it
- Build on it with next question
- Show how it strengthens the PRD

---

## The Five Question Categories

### 1. Problem Clarity Questions

**Purpose**: Ensure the problem is real and well-understood

**When to use**: Always use if problem is vague, speculative, or lacks evidence

**Questions**:

**"What specific user pain point does this solve?"**
- Look for concrete examples, not abstract statements
- Good: "Users waste 10 minutes finding task context across 5 tools"
- Bad: "Users want better productivity"

**"How do we know this is a real problem?"**
- Push for evidence: user interviews, support tickets, churn reasons, usage data
- Qualitative + quantitative is strongest

**"Who experiences this problem most acutely?"**
- Forces specificity about target users
- Helps prioritize if can't solve for everyone

**"What's the cost of NOT solving this?"**
- Revenue impact? Churn? Competitive loss? Team productivity?
- Helps establish urgency

**"Can you walk me through a specific example of when this problem occurred?"**
- Gets from abstract to concrete
- Often reveals problem is different than initially stated

---

### 2. Solution Validation Questions

**Purpose**: Ensure proposed solution actually solves the problem

**When to use**: If solution feels disconnected from problem, or if alternatives weren't considered

**Questions**:

**"Why is this the right solution for that problem?"**
- Look for logical connection between problem and solution
- Watch for "solutions looking for problems"

**"What alternatives did you consider? Why did you reject them?"**
- Shows depth of thinking
- Reveals trade-offs that were considered
- "This is the only way" is a red flag

**"What's the simplest version that solves the core problem?"**
- Helps avoid over-engineering
- Identifies must-have vs nice-to-have

**"How will users discover this feature?"**
- Great solution that no one finds is useless
- Tests whether it fits naturally into user workflows

**"What would make this solution NOT work?"**
- Forces thinking about failure modes
- Identifies risks and edge cases

---

### 3. Success Criteria Questions

**Purpose**: Ensure we can measure if the solution works

**When to use**: If success is vague or unmeasurable

**Questions**:

**"How will we know if this feature is successful?"**
- Look for specific, measurable outcomes
- Both quantitative (metrics) and qualitative (feedback) matter

**"What would make you consider this feature a failure?"**
- Helps identify risks and edge cases
- Good teams have clear failure criteria

**"What metric are we trying to move? By how much?"**
- Forces specificity
- "Improve engagement" → "Increase weekly active tasks created by 25%"

**"What's the adoption target?"**
- Not all features need 100% adoption
- Different targets for different user segments

**"How will we measure this in the first 2 weeks vs 3 months?"**
- Distinguishes leading indicators from lagging indicators
- Early signals help course-correct quickly

---

### 4. Constraint & Trade-off Questions

**Purpose**: Surface limitations and difficult decisions

**When to use**: If scope is unclear or risks aren't acknowledged

**Questions**:

**"What are the technical constraints or risks?"**
- Helps engineering team provide realistic estimates
- Identifies blockers early

**"What are we NOT going to do as part of this?"**
- Scope management is critical
- Clear non-goals prevent scope creep

**"What existing features or workflows does this affect?"**
- Nothing exists in isolation
- Need to think about system impacts

**"If we had half the time/resources, what would we cut?"**
- Reveals true priorities
- Helps identify MVP vs full vision

**"What happens if we're wrong about [key assumption]?"**
- Tests contingency thinking
- Identifies need for validation experiments

---

### 5. Strategic Fit Questions

**Purpose**: Ensure feature aligns with company goals and strategy

**When to use**: If strategic rationale is missing or unclear

**Questions**:

**"Why is this the right feature to build RIGHT NOW?"**
- Tests urgency and prioritization
- Helps clarify opportunity cost

**"How does this fit into our broader product strategy?"**
- Feature should ladder up to bigger goals
- Helps tell the strategic narrative

**"What happens if we wait 6 months to build this?"**
- Tests true urgency vs perceived urgency
- Helps prioritize against other opportunities

**"How does this affect our competitive position?"**
- Are we playing catch-up or leading?
- Table-stakes features vs differentiators

**"Who are we building this for - existing customers or new market?"**
- Different audiences may require different approaches
- Helps clarify product positioning

---

## Conversation Flow Tips

### Start Broad, Then Narrow

**First question**: Problem clarity (most foundational)
**Middle questions**: Solution validation + success criteria
**Last question**: Strategic fit (connects to bigger picture)

This helps start from user needs and work up to business strategy, not the reverse.

### Listen for Red Flags

**Vague language**:
- "Users want better..." → What specifically?
- "This will improve..." → Improve what, by how much?
- "Everyone needs..." → Really? Everyone?

**Solution-first thinking**:
- Can describe feature but struggles to describe problem
- "Because competitors have it" is not a problem statement
- Jumping to implementation details without problem validation

**Lack of evidence**:
- "I think users would like..." → How do we know?
- No data, no user quotes, no examples
- Relying on assumptions without validation plan

**Unclear success**:
- Can't articulate what success looks like
- No metrics, no qualitative indicators
- "We'll know it when we see it"

**Missing trade-offs**:
- Only discussing upside, no downsides
- No consideration of what's NOT included
- No discussion of risks or constraints

---

## Example Question Sequences

### Example 1: Vague Feature Request
**User**: "I want to improve our reporting dashboard"

**Gap analysis**:
- Problem unclear (what's wrong with current dashboard?)
- Solution vague (improve how?)
- No success criteria

**Question sequence**:
1. **Problem**: "What specific problem are users having with the current dashboard?"
2. **Success**: "How would you know the improved dashboard is working better?"
3. **Solution**: "What's the simplest change that would solve the core problem?"

### Example 2: Solution-First Thinking
**User**: "We should add AI voice chat to our app"

**Gap analysis**:
- Solution presented but problem unclear
- No validation of alternatives
- Missing success criteria

**Question sequence**:
1. **Problem**: "What specific user pain point does voice chat solve that typing doesn't?"
2. **Solution**: "What alternatives did you consider? Why voice over other input methods?"
3. **Success**: "How will we measure if users actually use the voice feature?"
4. **Constraints**: "What are we NOT including in V1? What comes later?"

### Example 3: Unclear Success
**User**: "Build a feature to help teams collaborate better"

**Gap analysis**:
- Problem too vague ("collaborate better")
- Success unmeasurable
- Scope unclear

**Question sequence**:
1. **Problem**: "Can you walk me through a specific example where collaboration broke down?"
2. **Success**: "What specific collaboration metric are we trying to improve? By how much?"
3. **Constraints**: "Which aspect of collaboration are we focusing on? What's out of scope?"

### Example 4: Well-Formed Request
**User**: "Sales reps spend 12 minutes per demo searching for relevant case studies across folders. I want to build a CRM-integrated case study library to reduce this to under 2 minutes."

**Gap analysis**:
- Problem is clear and quantified ✓
- Solution is specific ✓
- Need to validate: success criteria, strategic fit

**Question sequence**:
1. **Success**: "Beyond time savings, what other outcomes would make this successful?"
2. **Strategic fit**: "How does this prioritize against other sales productivity features?"

(Only 2 questions needed - most critical gaps filled in)

---

## Output Goal

After Socratic questioning, feature owner should have:

✅ **Clear, specific problem statement** with evidence
✅ **Rational justification** for why THIS solution
✅ **Concrete success criteria** (quantitative + qualitative)
✅ **Explicit scope boundaries** (what's in, what's out)
✅ **Strategic narrative** for why this matters now

These answers form the foundation of a strong PRD.

---

## Dos and Don'ts

### DO:
- Ask 3-5 most important questions (not everything)
- Focus on biggest gaps first
- Use coaching tone, not interrogation
- Acknowledge strong answers
- Offer examples when they struggle
- Build on their thinking

### DON'T:
- Ask exhaustive checklist of questions
- Challenge just to challenge
- Use "gotcha" questions
- Make them defensive
- Skip follow-up on weak answers
- Move on without clear answers

---

## Adapting by PRD Format

### For Full PRD (5 questions)
- 2 questions on problem clarity
- 1 question on solution validation
- 1 question on success criteria
- 1 question on strategic fit

### For One-Pager (2-3 questions)
- 1 question on problem clarity (if unclear)
- 1 question on success criteria (most critical)
- 1 question on scope (if needed)

### For Context Doc (3-4 questions)
- 1 question on customer problem
- 1 question on desired outcome
- 1 question on hypothesis
- 1 question on experimentation approach

---

## Quality Check for Your Questions

Before asking, verify:
- [ ] Question addresses a genuine gap (not asking to ask)
- [ ] Answer will strengthen the PRD
- [ ] Phrased as coaching, not challenging
- [ ] Focused on one topic (not multi-part)
- [ ] Answerable with available information

---

## Key Reminders

1. **This is not a checklist** - Use judgment, pick 3-5 most important questions
2. **Quality over quantity** - Better to deeply explore 3 questions than superficially cover 10
3. **Coaching mindset** - Help them think clearly, don't interrogate
4. **Evidence matters** - Push for concrete examples and data
5. **Specificity wins** - "25% improvement" beats "better engagement"
6. **Non-goals are critical** - What's OUT of scope matters as much as what's IN