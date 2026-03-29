---
name: exec-comms
description: Use when writing executive memos, board updates, or stakeholder communications. Triggers: executive memo, board update, 6-pager, BLUF, SCQA, stakeholder email, strategic document, exec summary, write for leadership.
---

# Executive Communication

## When This Skill Activates

Claude uses this skill when:
- Writing executive memos
- Creating board updates
- Drafting stakeholder emails
- Structuring strategic docs

## Core Frameworks

### 1. Amazon 6-Pager Structure

**Format:**
```markdown
# [Title]

## Executive Summary (BLUF - Bottom Line Up Front)
[Key decision/recommendation in 2-3 sentences]

## Context
[Background needed to understand]

## Analysis
[Data, options considered, tradeoffs]

## Recommendation
[What you propose and why]

## Next Steps
[Specific actions, owners, timeline]

## Appendix
[Supporting data, details]
```

### 2. SCQA Framework

**Structure:**
- **Situation:** Current state
- **Complication:** Problem/challenge
- **Question:** What should we do?
- **Answer:** Your recommendation

---

## Action Templates

### Template: Executive Memo

```markdown
# [Title]: [One-line summary]

## Executive Summary
[Bottom line up front - decision needed or announcement]

## Situation
[Current state, context]

## Complication
[Problem or opportunity]

## Question
[What needs to be decided or understood]

## Recommendation
[Your proposal]

## Rationale
[Why this is the right approach]
- Reason 1
- Reason 2
- Reason 3

## Alternatives Considered
| Option | Pros | Cons | Decision |
|--------|------|------|----------|
| A      | ...  | ...  | Not chosen |
| B      | ...  | ...  | **Recommended** |

## Next Steps
1. [Action] - [Owner] - [Date]
2. [Action] - [Owner] - [Date]

## Success Metrics
- [How we'll measure success]

## Risks & Mitigation
- **Risk:** [describe] → **Mitigation:** [how we'll handle]
```

---

## Quick Reference

### 📝 Executive Comms Checklist

**Structure:**
- [ ] BLUF (bottom line first)
- [ ] Context clear
- [ ] Decision/recommendation obvious
- [ ] Next steps specific

**Style:**
- [ ] Concise (no fluff)
- [ ] Scannable (bullets, headers)
- [ ] Data-backed
- [ ] Action-oriented

---

## Key Quotes

**Amazon:**
> "Start with the press release. Work backwards."

**On Executive Writing:**
> "If you can't summarize it in 2 sentences, you don't understand it well enough."

## Self-Learning

Before responding, read `LEARNED.md` in this skill directory when it exists and treat it as compact runtime guidance that sharpens this skill.

Rules for self-improvement:
- Keep `SKILL.md` human-owned; do not rewrite it directly from normal usage.
- Propose broader instruction changes through the central skill-learning review queue.
- Only promote specific, reusable, evidence-backed lessons into `LEARNED.md`.
