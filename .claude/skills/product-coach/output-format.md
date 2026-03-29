# Output Format Templates

This file contains the exact output templates for Product Coach. Read this when generating coaching output.

## Human-Readable Scorecard Template

```markdown
## Coaching Scorecard

**Artifact Type:** [prd | decision_memo | roadmap_narrative | research_synthesis | exec_comms]
**Overall Score:** [1-5] / 5
**Confidence:** [high | medium | low]

### Dimension Scores

| Dimension | Score | Evidence |
|-----------|-------|----------|
| [dimension 1] | [1-5] | [specific quote or observation] |
| [dimension 2] | [1-5] | [specific quote or observation] |
| ... | ... | ... |

### Top Gaps

1. **[Gap 1]**: [Brief description of what's missing or weak]
2. **[Gap 2]**: [Brief description of what's missing or weak]
3. **[Gap 3]**: [Brief description of what's missing or weak]

### Why It Matters

- [Business consequence if gap isn't addressed]
- [User/stakeholder consequence]
- [PM skill development consequence]

### Revision Suggestions

1. **[Specific revision 1]**: [Exact change to make, with location if applicable]
2. **[Specific revision 2]**: [Exact change to make, with location if applicable]
3. **[Specific revision 3]**: [Exact change to make, with location if applicable]

### Strategic Questions

1. [Question that prompts deeper thinking about the artifact]
2. [Question that challenges assumptions]

### Teaching Points

- **[Lesson 1]**: [The underlying PM principle and how to apply it]
- **[Lesson 2]**: [How to avoid this pattern in future work]

### Next Best Move

- [ ] [Immediate action: revise section X, add evidence Y, run /discover, etc.]
```

---

## Machine-Readable JSON Template

**Rules:**
- Must be valid, compact JSON
- Must be the LAST element in the response
- No prose after the JSON block
- `artifact_type` must match preset family exactly
- Dimension names must match preset exactly
- All scores are integers 1-5

```json
{
  "artifact_type": "prd|decision_memo|roadmap_narrative|research_synthesis|exec_comms",
  "overall_score": 0,
  "confidence": "high|medium|low",
  "dimension_scores": [
    {
      "name": "dimension name from preset",
      "score": 0,
      "evidence": "specific observation from artifact"
    }
  ],
  "top_gaps": ["gap 1", "gap 2", "gap 3"],
  "why_it_matters": ["consequence 1", "consequence 2"],
  "revision_suggestions": ["revision 1", "revision 2", "revision 3"],
  "strategic_questions": ["question 1", "question 2"],
  "teaching_points": ["lesson 1", "lesson 2"],
  "recommended_next_command": "/command-name"
}
```

---

## Quick Mode Output (Abbreviated)

When `depth=quick`, use this abbreviated format:

```markdown
## Quick Scorecard: [Artifact Type]

**Score:** [X]/5 | **Confidence:** [high|medium|low]

| Dimension | Score | Issue |
|-----------|-------|-------|
| [top gap dimension] | [1-5] | [one-line issue] |

**Top Fix:** [Single most important revision]

**Teaching Point:** [One key lesson]

[JSON block]
```

---

## Revision Delta Template

When the same artifact was previously reviewed:

```markdown
### Revision Delta

| Metric | Before | After | Change |
|--------|--------|-------|--------|
| Overall Score | X | Y | +/-Z |
| [Improved Dimension] | X | Y | +/-Z |

**Improved:** [dimension names that got better]
**Still Weak:** [dimension names that didn't improve]
**Judgment Assessment:** [Did the PM demonstrate learning? Yes/No + brief explanation]
```

---

## Formatting Rules

### Score Interpretation

| Score | Meaning |
|-------|---------|
| 5 | Exceptional - publication-ready, teaches others |
| 4 | Strong - minor revisions only |
| 3 | Adequate - needs focused work on 1-2 dimensions |
| 2 | Weak - significant gaps, needs rework |
| 1 | Critical - fundamental problems, restart recommended |

### Evidence Quality

- **Good evidence:** Direct quotes, specific sections, observable patterns
- **Weak evidence:** Vague references, "seems like", "generally"

### Confidence Levels

- **High:** Artifact is complete, clearly scoped, enough context to evaluate
- **Medium:** Some ambiguity, missing context, or partial artifact
- **Low:** Significant gaps in understanding, draft stage, or unusual format

### Teaching Point Quality

- **Good:** Principle + application + how to avoid the pattern
- **Weak:** Generic advice without context ("be more specific")
