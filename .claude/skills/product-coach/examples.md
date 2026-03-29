# Product Coach Examples

Complete coaching examples for each artifact type. Read this when you need reference patterns.

---

## Example 1: PRD Review (Quick Mode)

**Input:** User shares a PRD for a new notification feature.

**Output:**

```markdown
## Quick Scorecard: PRD

**Score:** 3/5 | **Confidence:** Medium

| Dimension | Score | Issue |
|-----------|-------|-------|
| Problem Framing | 2 | Problem described as "users want notifications" - not a problem |
| Evidence Quality | 2 | No customer evidence cited |
| Metrics Quality | 3 | Has DAU target but no leading indicators |

**Top Fix:** Rewrite the problem statement to describe what users cannot do today and why that matters. "Users miss time-sensitive updates because they must check the app manually" is a problem; "users want notifications" is a feature request.

**Teaching Point:** Problem statements should describe a pain or inability, not a desired feature. If you can't articulate what's broken, you can't validate the solution.

```json
{"artifact_type":"prd","overall_score":3,"confidence":"medium","dimension_scores":[{"name":"problem framing","score":2,"evidence":"Opening states 'users want real-time notifications' - this is a feature request, not a problem statement"},{"name":"evidence quality","score":2,"evidence":"No customer quotes, support tickets, or research cited in the document"},{"name":"scope discipline","score":4,"evidence":"V1 is limited to push notifications for 3 event types, clearly bounded"},{"name":"metrics quality","score":3,"evidence":"Has '20% increase in DAU' but no leading metrics to validate during development"},{"name":"differentiation","score":3,"evidence":"Mentions competitors have this, but doesn't explain why our approach is better"},{"name":"risk handling","score":3,"evidence":"Lists technical risks but no assumption risks"}],"top_gaps":["Problem statement is feature-first, not user-pain-first","No evidence that users actually need this","Missing leading metrics"],"why_it_matters":["Without a clear problem, you can't validate whether notifications solve it","Feature requests without evidence lead to low-adoption features"],"revision_suggestions":["Rewrite problem as: 'Users in [role] cannot [action] because [barrier], which causes [impact]'","Add 2-3 customer quotes or support tickets showing the pain","Add leading metric: '% of users who enable notifications within 7 days of feature launch'"],"strategic_questions":["What happens if users ignore notifications? Is there a fallback?","Have we validated that the 3 event types are the right 3?"],"teaching_points":["Problem statements describe inability or pain, not solutions","Leading metrics let you course-correct during development, not after launch"],"recommended_next_command":"/discover"}
```

---

## Example 2: Decision Memo Review (Full Mode)

**Input:** User shares a decision memo about build vs. buy for analytics.

**Output:**

```markdown
## Coaching Scorecard

**Artifact Type:** decision_memo
**Overall Score:** 3 / 5
**Confidence:** High

### Dimension Scores

| Dimension | Score | Evidence |
|-----------|-------|----------|
| Decision Framing | 4 | Clear decision: "Should we build custom analytics or integrate Amplitude?" |
| Trade-off Quality | 2 | Lists pros/cons but doesn't show opportunity cost |
| Reversibility Handling | 3 | Acknowledges this is a two-way door, but doesn't discuss migration path |
| Evidence Quality | 3 | Has cost comparison but missing engineering effort estimates |
| Recommendation Strength | 3 | Says "leaning toward Amplitude" but not a clear call |
| Strategic Fit | 4 | Connects to company goal of reducing maintenance burden |

### Top Gaps

1. **No explicit opportunity cost**: The memo lists what each option costs, but not what we're giving up by choosing one over the other
2. **Weak recommendation**: "Leaning toward" is not a decision - the memo should make a clear call
3. **Missing reversibility plan**: If Amplitude doesn't work out, what's the exit strategy?

### Why It Matters

- Decision memos exist to enable decisions, not summarize options
- Stakeholders need to see not just what we gain, but what we forego
- Without a clear call, the memo creates work (another meeting) rather than resolving it

### Revision Suggestions

1. **Strengthen recommendation**: Change "leaning toward Amplitude" to "Recommend: Amplitude" with explicit conditions
2. **Add opportunity cost section**: "Choosing Amplitude means we forego [X]. We accept this because [Y]."
3. **Add reversibility section**: "If Amplitude doesn't meet our needs by [date], we will [specific action]."

### Strategic Questions

1. What would have to be true for build to be the right choice? Is that plausible?
2. What's the cost of delaying this decision another month?

### Teaching Points

- **Make the call**: A decision memo that doesn't recommend has failed its purpose. Be explicit.
- **Show what you're saying no to**: Trade-offs aren't just pros/cons - they're about what you're giving up
- **Calibrate confidence to reversibility**: Two-way doors can have lighter analysis; one-way doors need more rigor

### Next Best Move

- [ ] Strengthen recommendation to explicit "Recommend: X"
- [ ] Add opportunity cost paragraph
- [ ] Run `/think` to pressure-test the recommendation

```json
{"artifact_type":"decision_memo","overall_score":3,"confidence":"high","dimension_scores":[{"name":"decision framing","score":4,"evidence":"Decision question is explicit and bounded"},{"name":"trade-off quality","score":2,"evidence":"Lists pros/cons but never states what we give up by choosing either option"},{"name":"reversibility handling","score":3,"evidence":"Calls it a two-way door but provides no exit criteria or migration plan"},{"name":"evidence quality","score":3,"evidence":"Has vendor pricing but missing build effort estimate from engineering"},{"name":"recommendation strength","score":3,"evidence":"'Leaning toward Amplitude' is not a recommendation"},{"name":"strategic fit","score":4,"evidence":"Clearly connects to strategic goal of reducing maintenance surface area"}],"top_gaps":["No explicit opportunity cost stated","Recommendation is weak ('leaning toward' not a call)","No reversibility plan with criteria"],"why_it_matters":["Decision memos should resolve, not summarize","Stakeholders need to see trade-offs, not just features","Without clear calls, you create more work (another meeting)"],"revision_suggestions":["Change 'leaning toward' to 'Recommend: Amplitude because X, Y, Z'","Add: 'Choosing Amplitude means we forego custom analytics. We accept this because...'","Add reversibility section: 'If Amplitude doesn't meet [criteria] by [date], we will [action]'"],"strategic_questions":["What would have to be true for build to be right? Is that plausible?","What's the cost of another month of analysis?"],"teaching_points":["Decision memos must recommend, not summarize","Opportunity cost is what you give up, not just pros/cons","Calibrate analysis depth to reversibility"],"recommended_next_command":"/think"}
```

---

## Example 3: Executive Communication Review

**Input:** User shares a QBR update for executives.

**Output:**

```markdown
## Quick Scorecard: exec_comms

**Score:** 2/5 | **Confidence:** High

| Dimension | Score | Issue |
|-----------|-------|-------|
| Brevity Discipline | 1 | 4 pages for exec audience - should be 1-2 max |
| Ask / Call to Action | 1 | No explicit ask - what do you want them to do? |
| Clarity | 2 | Key metrics buried in paragraph 3 |

**Top Fix:** Cut to 1 page. Lead with: "Here's what we shipped, here's what it drove, here's what we need from you." Make the ask explicit in the first paragraph.

**Teaching Point:** Executives scan, they don't read. Your key point and ask should be visible in the first 30 seconds of reading. If they have to hunt for it, you've lost them.

```json
{"artifact_type":"exec_comms","overall_score":2,"confidence":"high","dimension_scores":[{"name":"audience fit","score":3,"evidence":"Some content is right altitude but buried"},{"name":"clarity","score":2,"evidence":"Key metrics in paragraph 3, not lead"},{"name":"strategic framing","score":3,"evidence":"Connects to goals but late in document"},{"name":"trustworthiness","score":3,"evidence":"Has specific numbers but some claims lack evidence"},{"name":"ask / call to action","score":1,"evidence":"No explicit ask - document describes status without requesting anything"},{"name":"brevity discipline","score":1,"evidence":"4 pages for exec audience; target is 1-2 pages max"}],"top_gaps":["No explicit ask - what do you need from this audience?","Too long - 4 pages when exec target is 1-2","Key point buried - lead with outcome, not process"],"why_it_matters":["Without an ask, execs don't know what to do with this information","Long documents get skipped - you're not being thorough, you're being ignored","If the point isn't obvious immediately, it won't be found"],"revision_suggestions":["Cut to 1 page maximum","Add explicit ask in paragraph 1: 'We need [X] from you by [date]'","Restructure: Lead with outcome (metrics), then context, then ask"],"strategic_questions":["What decision or action do you want from this audience?","If they only read the first paragraph, what should they take away?"],"teaching_points":["Exec comms need an explicit ask - 'for information' is not a purpose","Lead with the outcome and ask; context comes after","Brevity is respect for your audience's time"],"recommended_next_command":"/align"}
```

---

## Example 4: Roadmap Narrative Review

**Input:** User shares a quarterly roadmap.

**Output:**

```markdown
## Coaching Scorecard

**Artifact Type:** roadmap_narrative
**Overall Score:** 3 / 5
**Confidence:** Medium

### Dimension Scores

| Dimension | Score | Evidence |
|-----------|-------|----------|
| Sequencing Logic | 2 | Lists features in priority order but doesn't explain why this sequence |
| Capacity Realism | 2 | No capacity assumptions stated - assumes team can do everything |
| Portfolio Balance | 4 | Good mix of strategic bets and maintenance work |
| Strategic Alignment | 4 | Each item traces to Q1 OKRs |
| Narrative Clarity | 3 | Clear structure but the "why this order" is missing |
| Learning/Measurement Logic | 2 | Has ship dates but no validation checkpoints |

### Top Gaps

1. **No sequencing rationale**: Why is Feature A before Feature B? What does doing A first enable?
2. **No capacity validation**: Roadmap lists 8 major items with no team capacity context
3. **No learning checkpoints**: All measurement happens at ship, nothing during development

### Why It Matters

- Roadmaps without sequencing rationale appear as wish lists, not strategic plans
- Capacity invisibility leads to missed commitments and eroded trust
- Learning checkpoints let you course-correct before ship

### Revision Suggestions

1. **Add sequencing rationale**: "Feature A ships first because it de-risks Feature B's API dependency"
2. **Add capacity context**: "Based on [team velocity], we can deliver [X] scope points. This roadmap has [Y]."
3. **Add learning checkpoints**: "After Milestone 1, we will validate [assumption] before proceeding to Milestone 2"

### Strategic Questions

1. If you had to cut 2 items, which would they be and why?
2. What will you learn by end of Q1 that you don't know today?

### Teaching Points

- **Sequence for leverage**: The order should create compounding value, not just reflect priority
- **Make capacity explicit**: Invisible capacity assumptions become broken promises
- **Build in learning**: Roadmaps are hypotheses; build checkpoints to validate them

### Next Best Move

- [ ] Add one-sentence sequencing rationale for each item
- [ ] Add capacity assumptions section at the top
- [ ] Run `/prioritize` to validate the sequencing

```json
{"artifact_type":"roadmap_narrative","overall_score":3,"confidence":"medium","dimension_scores":[{"name":"sequencing logic","score":2,"evidence":"Lists items in priority order but never explains why this sequence creates leverage"},{"name":"capacity realism","score":2,"evidence":"No capacity context - 8 major items with no velocity or headcount assumptions"},{"name":"portfolio balance","score":4,"evidence":"Good mix: 3 strategic bets, 3 maintenance, 2 tech debt items"},{"name":"strategic alignment","score":4,"evidence":"Each item has explicit OKR traceability"},{"name":"narrative clarity","score":3,"evidence":"Clear structure but missing the 'why this order' story"},{"name":"learning/measurement logic","score":2,"evidence":"Has ship dates but no validation checkpoints between now and ship"}],"top_gaps":["No sequencing rationale - why this order?","No capacity validation - can the team actually do this?","No learning checkpoints - all measurement at ship"],"why_it_matters":["Roadmaps without rationale read as wish lists","Capacity invisibility leads to broken commitments","Learning checkpoints enable course-correction"],"revision_suggestions":["Add sequencing rationale: 'A before B because A de-risks B's dependency'","Add capacity section: 'Team velocity is X, roadmap scope is Y'","Add checkpoints: 'After M1, validate [assumption] before M2'"],"strategic_questions":["If you had to cut 2 items, which would they be?","What will you know at end of Q1 that you don't know today?"],"teaching_points":["Sequence for leverage, not just priority","Explicit capacity prevents overcommitment","Build in learning checkpoints"],"recommended_next_command":"/prioritize"}
```

---

## Example 5: Research Synthesis Review

**Input:** User shares a synthesis of customer interviews.

**Output:**

```markdown
## Quick Scorecard: research_synthesis

**Score:** 4/5 | **Confidence:** High

| Dimension | Score | Issue |
|-----------|-------|-------|
| Evidence Traceability | 2 | Themes stated but can't trace back to specific quotes |
| Actionability | 3 | Good insights but weak "so what" for decisions |

**Top Fix:** Add a "Decision Implications" section that explicitly states: "Based on this research, we should [action]." Link each theme to at least one verbatim quote.

**Teaching Point:** Research syntheses fail when they stop at observations. The value is in the decision implications - what should we do differently because we learned this?

```json
{"artifact_type":"research_synthesis","overall_score":4,"confidence":"high","dimension_scores":[{"name":"source quality","score":5,"evidence":"12 interviews, good role/segment mix, recent (last 2 weeks)"},{"name":"evidence traceability","score":2,"evidence":"Themes are stated but no direct quotes or interview references to back them"},{"name":"pattern validity","score":4,"evidence":"Patterns appear in multiple interviews, not just one"},{"name":"uncertainty handling","score":4,"evidence":"Explicitly calls out where confidence is low and why"},{"name":"actionability","score":3,"evidence":"Insights are clear but decision implications are implied, not stated"},{"name":"decision relevance","score":5,"evidence":"Framed around specific product decision we're making"}],"top_gaps":["Themes not traceable to specific evidence","Decision implications are implied, not explicit"],"why_it_matters":["Without traceability, stakeholders can't assess confidence","Research that doesn't drive decisions is entertainment, not insight"],"revision_suggestions":["Add direct quotes under each theme to show evidence","Add 'Decision Implications' section: 'Based on this, we should...'"],"strategic_questions":["Which themes are you most confident in? Least?","What would you need to see to change your conclusion?"],"teaching_points":["Syntheses need evidence traceability - show your work","End with decision implications, not just observations"],"recommended_next_command":"/discover"}
```

---

## Pattern Reference

### Common Failure Modes by Artifact

| Artifact | Common Failure | Fix Pattern |
|----------|---------------|-------------|
| PRD | Feature-first framing | Rewrite as user pain |
| PRD | No evidence | Add customer quotes/tickets |
| PRD | Lagging-only metrics | Add leading indicators |
| Decision | Options without call | Make explicit recommendation |
| Decision | No opportunity cost | "Choosing X means forego Y" |
| Roadmap | Priority list, not sequence | "A before B because..." |
| Roadmap | No capacity | Add velocity/assumptions |
| Research | Observations, no decisions | Add "Decision Implications" |
| Research | Untraceable themes | Add verbatim quotes |
| Exec Comms | No ask | "We need X from you by Y" |
| Exec Comms | Too long | Cut to 1-2 pages |

### Score Calibration

- **5**: Exceptional, publication-quality, teaches others
- **4**: Strong, minor revisions only
- **3**: Adequate, needs 1-2 focused improvements
- **2**: Weak, significant rework needed
- **1**: Critical issues, recommend restart
