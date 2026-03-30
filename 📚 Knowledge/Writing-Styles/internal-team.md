# Writing Guide: Internal Team Audience

**Who this is for:** Cross-functional partners, engineering, design, data, operations — people doing the work or owning a piece of it.

---

## Opening Logic

**Lead with the problem being solved, not the solution being described.**

Sentence 1 must contain: what's broken, what's unclear, or what gap this work addresses.

> ✅ "Customers are abandoning the onboarding flow at step 3 because they don't understand the data model."
> ✅ "We're getting competing requests for the same sprint capacity from two different stakeholders — this doc proposes how to resolve that."
> ❌ "This spec outlines the new onboarding redesign."
> ❌ "Here's the plan for the Q2 initiative."

**Why this works:** Engineers and designers need to understand the *why* to make good micro-decisions during implementation. If you lead with the solution, they can't push back or improve on it — they don't know what success looks like.

---

## Evidence Hierarchy

Order evidence from most to least persuasive for this audience:

1. **Customer or user signal** — what problem are real users experiencing? Quotes, data, support tickets
2. **Business context** — how does this problem affect the company, product, or OKRs?
3. **Constraints and scope** — what's in/out of scope, what's fixed vs. flexible, what's the timeline?
4. **Proposed approach** — solution options or the chosen direction with rationale
5. **Open questions** — what still needs their input? What are you NOT deciding here?

---

## Structure Template

```
## Problem
[What's broken or unclear — 2-4 sentences. Include the user impact]

## Why this matters now
[Business context or urgency — 1-2 sentences. Tie to OKRs, customer feedback, or competitive pressure if relevant]

## Proposed approach
[Your recommendation — 3-5 sentences or bullets. Be specific about what you're building, not building, and why]

## Tradeoffs
[What you're giving up with this approach — be honest. 2-3 bullets]

## Open questions for this team
[Things you need their input on — numbered list, not rhetorical]
1. [Question + why it matters]
2. [Question]

## Success criteria
[How we'll know this worked — specific, measurable if possible]

## Out of scope
[What's explicitly not being addressed here — prevents scope creep and false assumptions]
```

---

## Tone Markers

- **Collaborative, not prescriptive.** "Here's my thinking — push back if you see something I'm missing" not "here's what engineering needs to do"
- **Transparent about tradeoffs.** Don't hide the cost or complexity of your proposal
- **Specific about asks.** "I need your input on X by Thursday" not "let me know your thoughts"
- **Problem-first, always.** If someone asks "why are we doing this?", the answer should be in the first paragraph
- **Short sentences, not PM jargon.** "This will improve adoption" not "this initiative will unlock synergistic value creation"

---

## Anti-Patterns

| Anti-Pattern | Why It Fails | Fix |
|---|---|---|
| Solution-first spec (no problem statement) | Team can't evaluate tradeoffs or push back | Always lead with the problem |
| "The team will need to..." (passive ownership) | Unclear who owns what | Name the owner: "Design will own X, Eng owns Y" |
| Vague success criteria | No one knows when they're done | At minimum: what user behavior changes? |
| No out-of-scope section | Engineers build things they think are implied | Explicit is better than inferred |
| Long background before the ask | Buries what you need from them | State the ask within the first 3 paragraphs |
| No open questions | Signals you've made all decisions without them | Always invite input on the real unknowns |

---

## Context-Specific Variants

### Sprint/Planning Docs
- Lead with what we're trying to learn or prove, not a list of tickets
- Include the "why now" relative to the sprint goal
- Make it obvious what's a commitment vs. stretch

### Design Briefs
- Problem statement before constraints
- Customer jobs-to-be-done before visual requirements
- See `/design-brief` command for the full structure

### Engineering Specs / API Docs
- For technical audience: see `technical.md`
- For mixed PM + Eng audience: use internal-team.md but add a "Technical constraints" section

---

## Integration Notes

- Loaded by `/write --type internal`, `/spec`, `/story`, or when `--to` indicates a cross-functional partner
- Pairs with: `/spec` for full feature specs, `/story` for user stories, `/align` for resolving competing priorities
- Cross-reference: `technical.md` for when the primary audience is engineers or architects
