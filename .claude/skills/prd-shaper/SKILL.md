---
name: prd-shaper
description: Expert PRD creation with intelligent format selection (Full PRD, One-Pager, or AI-Era Context Doc), Socratic discovery questioning, and evidence-based decision-making for product specifications
---

# PRD Shaper

Create exceptional Product Requirements Documents through intelligent format selection, Socratic discovery, and evidence-based decision-making.

## When to Use This Skill

Use this skill when:
- Reviewing or scoring an existing PRD for quality and decision density
- Refining PRDs that lack clarity, evidence, or explicit decisions
- Applying quality checks, anti-patterns review, or writing rules to a draft
- Conducting discovery to sharpen fuzzy feature ideas before writing

**For creating a new PRD from scratch, use `/spec`** — it is the canonical creation path that incorporates this skill's philosophy, writing rules, and quality checks. This skill is the quality and philosophy layer that `/spec` is built on. When invoked directly for creation, follow the same workflow as `/spec` and apply the full quality checklist, anti-patterns, and writing rules defined here.

## Core Philosophy

**PRDs are about decisions, not documentation.**

Great PRDs in 2025:
- Make explicit decisions at every turn
- Work alongside AI prototyping (not against it)
- Focus on customer outcomes over feature lists
- Use concrete examples, not vague descriptions
- Evolve with the product (living documents)

**The fatal flaw**: PRDs that say a lot without deciding anything.

## How This Skill Works

### Step 1: Format Selection

I'll help you choose the right PRD format based on complexity and context:

**Full PRD** (See `full-prd-guide.md` or use `/spec --type full`)
- Complex features with multiple stakeholders
- Significant investment requiring comprehensive alignment
- Cross-team coordination and dependencies
- Need for detailed success criteria and risk management

**One-Pager** (See `one-pager-guide.md` or use `/spec --type one-pager`)
- Clear problem with bounded solution
- Smaller features or experiments
- Single team ownership
- Quick stakeholder alignment needed

**AI-Era Context Doc** (See `context-doc-guide.md` or use `/spec --type context-doc`)
- Hypothesis-driven experimentation
- Rapid validation with small user cohorts
- Working prototype + short context approach
- Outcome-focused over feature-focused

### Step 2: Socratic Discovery

**Before drafting**, I conduct targeted discovery using the framework in `socratic-framework.md`. Use the same context-gathering protocol as other consultative skills:

1. **Ask one question at a time**; wait for the answer before asking the next
2. **Cap at 3 questions** for the initial discovery phase
3. If your input already covers problem, solution, success criteria, and scope, ask at most 1–2 questions or proceed directly to drafting
4. **Analyze your input** for gaps in: problem clarity, solution rationale, success criteria, constraints, strategic fit
5. Pick the most critical gaps; ask targeted questions (focus on decisions, not documentation; help you think clearly, not interrogate)
6. Once answers are gathered, proceed to drafting

**Skip questioning only if:**
- You explicitly request it
- Your input already covers problem, solution, success criteria, scope clearly

### Step 3: Draft Generation

**Before drafting:** Load `~/.claude/skills/elite-copywriter/SKILL.md` and apply its principles throughout. The PRD must sound like a peer briefing from a sharp PM, not AI output.

Generate PRD draft incorporating:
- Your discovery answers
- Chosen format structure
- Evidence-based approach
- Concrete examples and metrics
- Explicit assumptions marked as `[ASSUMPTION - needs validation]`
- Missing information marked as `[NEEDS INPUT]`

**Copy quality rules (from elite-copywriter):**
- BLUF: lead with the conclusion in every section
- Cut AI-isms: "leverage", "robust", "delving into", "Here's", "Let me show you", "seamless", "comprehensive"
- Sound like a sharp PM writing for other PMs and engineers — direct, specific, opinionated
- Every paragraph earns its place; if it can be a table, make it a table
- Target 30–40% shorter than typical AI-generated prose on exec-facing sections

### Step 4: Quality Validation

Ensure every PRD includes:
- **Strategic clarity**: One-sentence problem + hypothesis
- **Measurability**: Specific thresholds, not "improve X"
- **Actionability**: Engineering can build from this
- **Risk management**: Detection, fallbacks, owners
- **Decision quality**: Every "will" has "how" and "when"
- **Copy quality**: No AI-isms, BLUF throughout, sounds human not generated

## Format Selection Guide

### Choose Full PRD When:
- Feature requires >1 month of engineering time
- Multiple teams involved (design, engineering, analytics, ops)
- Significant technical complexity or dependencies
- Stakeholder alignment is challenging
- Risk of failure is high (revenue, reputation, compliance)
- Need comprehensive documentation for legal/audit

**Output**: 10-part PRD with evidence, alternatives analysis, dependencies, risks

### Choose One-Pager When:
- Feature scope is clear and bounded
- Single team can execute
- Problem is well-understood
- Timeline is 2-4 weeks
- Stakeholder alignment is straightforward
- Low-to-medium risk

**Output**: 6-section concise PRD focusing on essentials

### Choose Context Doc When:
- Hypothesis needs validation before major investment
- Speed to customer feedback is critical
- Working prototype will clarify requirements
- Outcome metrics matter more than feature specs
- Willing to pivot based on experiment results
- Modern AI-era product development approach

**Output**: 3-page context doc + working prototype + experimentation plan

## Key Principles

### 1. Evidence Over Assumptions
- Customer quotes trump opinions
- Usage data beats intuition
- Competitive analysis grounds reality
- Mark all assumptions explicitly

### 2. Specificity Over Vagueness
- **Bad**: "Improve engagement"
- **Good**: "Increase weekly active users by 25% (from 1,200 to 1,500)"

- **Bad**: "Fast response time"
- **Good**: "P95 latency <200ms for 95% of queries"

### 3. Decisions Over Descriptions
Every section must decide something:
- **Not**: "We will consider various approaches"
- **But**: "We're using approach B because it's 40% faster than A with acceptable 5% accuracy trade-off"

### 4. Outcomes Over Features
Focus on behavior change:
- **Not**: "Build dependency visualization dashboard"
- **But**: "Reduce missed critical dependencies from 30% to <5%, saving program managers 4 hours/week"

### 5. Non-Goals Are Mandatory
What you're NOT doing is as important as what you are:
- Prevents scope creep
- Clarifies trade-offs
- Sets expectations
- Enables faster decisions

## Writing Best Practices

### Critical Rule #1: Don't Use AI for First Drafts

**Why**: AI creates verbose, decision-free documentation that says a lot without deciding anything.

**Instead**:
- Write the first draft yourself with clear decisions
- Use AI as copilot to improve and polish
- Think of AI as teammate for refinement, not ghostwriter for creation

### Critical Rule #2: Show, Don't Tell

Use concrete before/after examples:

**Vague → Specific**:
- ❌ "Improve user engagement"
- ✅ "P50 reply time drops ≥10% vs control group (from 47s to <42s)"

**Generic → Actionable**:
- ❌ "Generate helpful replies"
- ✅ "For questions <10 words, respond within 2s with contextually relevant suggestions based on last 3 messages"

**Hopeful → Measurable**:
- ❌ "Reduce support tickets"
- ✅ "Decrease returns-related support tickets by 15-20% (from 18% baseline to 14.4-14.8%) measured over 30-day window"

### Critical Rule #3: Every "Will" Needs "How" and "When"

**Not**: "We will test the feature"
**But**: "A/B test with 5% user-level randomization for 2 weeks, graduating at p<0.05 with ≥10% metric lift"

**Not**: "We will improve performance"
**But**: "Reduce P95 latency from 300ms to <200ms by implementing Redis caching, measured over 7 days post-deployment"

### Writing Checklist

Before finalizing any PRD section:
- [ ] Count decisions per page (aim for 5+)
- [ ] Flag vague words ("improve", "enhance", "optimize", "better")
- [ ] Verify every metric has a number, not a direction
- [ ] Check that non-goals are explicit
- [ ] Ensure each "will" has "how" and "when"

## AI Features Guidance

**When writing PRDs for AI/ML features**, see `ai-features-guide.md` for:
- Behavior contract format (15-25 labeled examples required)
- Good/Bad/Reject pattern specification
- Offline evaluation requirements
- Red team scenarios
- Safety and cost considerations

**Key difference**: Traditional features specify behavior with requirements; AI features require extensive examples to show desired behavior patterns.

## Socratic Discovery Framework

See `socratic-framework.md` for detailed questioning system.

**Five Question Categories:**
1. **Problem Clarity**: Is the problem real and well-understood?
2. **Solution Validation**: Does this solution actually solve the problem?
3. **Success Criteria**: How will we measure success?
4. **Constraints & Trade-offs**: What are the limitations?
5. **Strategic Fit**: Why this feature, why now?

**Coaching Approach:**
- Ask 3-5 most important questions (not everything)
- Help clarify thinking, not interrogate
- Offer examples when PM struggles
- Build on strong answers

**Red Flags to Watch For:**
- Vague language ("better", "improve", "enhance")
- Solution-first thinking (can't describe problem)
- Lack of evidence (no data, quotes, examples)
- Unclear success criteria

## Common PRD Antipatterns

### Antipattern 1: Prose Without Decisions
**Symptom**: Long context paragraphs with no actionable outcomes

**Fix**: Every paragraph ends with a decision or specific example

### Antipattern 2: Metric Theater
**Symptom**: "Improve engagement", "Increase satisfaction"

**Fix**: "P50 engagement time increases ≥15%", "NPS increases from 42 to 48+"

### Antipattern 3: Vague Implementation
**Symptom**: "Start small, then ramp" or "Phased approach"

**Fix**: "Week 1: 5% users, Week 2: Graduate if p<0.05 and +10% metric"

### Antipattern 4: Missing Non-Goals
**Symptom**: Only listing what's included

**Fix**: Explicit "What we're NOT doing" section with rationale

### Antipattern 5: One-and-Done Documentation
**Symptom**: Written once, never updated, gathering dust

**Fix**: Living document updated at each stage, linked to results

## Integration with AI Prototyping

PRDs work alongside prototypes, not instead of them:

**Before Prototyping:**
- PRD speclet defines problem + hypothesis
- Strategic fit validated
- Success metrics established

**During Prototyping:**
- Prototypes test PRD hypotheses
- Learnings feed back into PRD
- Edge cases documented

**After Prototyping:**
- PRD reflects prototype insights
- Behavior examples from prototypes
- Rollout plan accounts for findings

## Quality Checklist

Before considering complete, verify:

**Strategic Clarity**
- [ ] TL;DR separates What/Why/How clearly (Full PRD only)
- [ ] Problem statement is specific with evidence
- [ ] Hypothesis is one sentence and testable
- [ ] Strategy fit is explicit

**Measurability**
- [ ] Success metrics have specific thresholds
- [ ] Guardrail metrics defined
- [ ] Graduation criteria clear

**Actionability**
- [ ] Engineering knows what to build
- [ ] Behavior specified with examples
- [ ] Edge cases enumerated

**Risk Management**
- [ ] Detection mechanisms defined
- [ ] Fallback strategies exist
- [ ] Kill switch specified with owner

**Decision Quality**
- [ ] Decision density: ≥5 decisions per page (not just descriptions)
- [ ] Every "will" has "how" and "when"
- [ ] Non-goals explicit with rationale
- [ ] Owners named for all open questions

**Language Quality**
- [ ] No vague words: "improve", "enhance", "optimize", "better" without numbers
- [ ] All metrics have specific thresholds (not just directions)
- [ ] Concrete examples used (not abstract principles)
- [ ] Before/after comparisons show specific change

**AI Features (if applicable)**
- [ ] 15-25 labeled examples provided (see `ai-features-guide.md`)
- [ ] Good/Bad/Reject patterns documented
- [ ] Offline evaluation plan with golden set
- [ ] Red team scenarios covered
- [ ] Safety and cost monitoring specified

## Usage Examples

### Creating New PRD
```
User: "I want to build a feature for dependency tracking"

Assistant (using prd-shaper):
1. Analyzes input → identifies gaps (no problem evidence, unclear success criteria)
2. Asks 3-4 targeted questions from socratic-framework.md
3. Waits for answers
4. Suggests format: "Based on complexity, I recommend Full PRD"
5. Generates draft using full-prd-guide.md structure
6. Marks assumptions, includes evidence, sets specific metrics
```

### Refining Existing PRD
```
User: "Review this PRD and make it more actionable"

Assistant (using prd-shaper):
1. Assesses decision density (flags vague language)
2. Identifies missing thresholds on metrics
3. Points out lack of non-goals
4. Suggests specific improvements with examples
5. Offers to redraft sections
```

### Format Selection Help
```
User: "Should I write a full PRD or one-pager for this experiment?"

Assistant (using prd-shaper):
1. Asks about scope, timeline, stakeholders, risk
2. Recommends format based on criteria
3. Explains trade-offs
4. Offers to generate in chosen format
```

## Key Reminders

1. **Decisions over documentation** - Every section decides something
2. **Evidence over assumptions** - Mark speculation explicitly
3. **Specificity wins** - "≥10%" not "improve"
4. **Non-goals matter** - Explicit boundaries prevent scope creep
5. **Outcomes over features** - Behavior change, not capabilities
6. **Living documents** - Update through product lifecycle
7. **Work with prototypes** - PRDs and prototypes iterate together

## Next Steps After Using This Skill

Once PRD is complete:
1. **Socialize with stakeholders** - Get alignment on decisions
2. **Create prototypes** - Test hypotheses with AI tools
3. **Update PRD** - Incorporate prototype learnings
4. **Track decisions** - Use decision log for changes
5. **Measure outcomes** - Validate success criteria post-launch
6. **Capture learnings** - Update PRD with results

## Reference Files

- **full-prd-guide.md** - Comprehensive 10-part PRD structure and workflow
- **one-pager-guide.md** - Streamlined 6-section PRD for smaller features
- **context-doc-guide.md** - AI-era short context + prototype approach
- **socratic-framework.md** - Discovery questioning system with 5 categories
- **ai-features-guide.md** - AI/ML feature PRDs with behavior contracts and examples