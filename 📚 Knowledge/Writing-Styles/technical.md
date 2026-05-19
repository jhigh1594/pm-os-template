# Writing Guide: Technical Audience

**Who this is for:** Engineers, architects, data scientists, security, infrastructure — people who need to understand, build, or evaluate a technical approach.

---

## Opening Logic

**Lead with the technical problem or constraint, then options with explicit tradeoffs.**

Sentence 1 must contain: the specific technical challenge, constraint, or decision being addressed.

> ✅ "The current card-sync pipeline can't handle 10K+ concurrent events without dropping updates — here are three approaches."
> ✅ "OAuth 2.0 with PKCE is the only flow that satisfies our new SOC 2 Type II requirements for the mobile client."
> ❌ "We want to improve the sync performance."
> ❌ "The mobile team is working on authentication improvements."

**Why this works:** Technical audiences can immediately assess feasibility and spot flaws if you give them the constraint first. Vague problem statements waste time — they have to reverse-engineer what you're actually asking.

---

## Evidence Hierarchy

Order evidence from most to least persuasive for this audience:

1. **Specific constraints** — performance thresholds, SLA requirements, security requirements, platform limits
2. **Options considered with explicit tradeoffs** — not "we looked at X" but "X achieves Y but costs Z"
3. **Benchmarks or data** — latency numbers, error rates, throughput, cost per operation
4. **Dependencies and integration points** — what does this touch? What breaks if it changes?
5. **Business context** — why this matters to the product; don't skip this but don't lead with it

---

## Structure Template

```
## Technical Problem
[The specific constraint or challenge — 2-3 sentences. Include: what's breaking, what threshold we need to hit, or what requirement we need to satisfy]

## Constraints
- [Constraint 1 — e.g., "must complete within 500ms P99"]
- [Constraint 2 — e.g., "cannot require schema migration on existing installations"]
- [Constraint 3 — e.g., "must work in EU data-residency configuration"]

## Options Considered

### Option A: [Name]
- **How it works:** [2-3 sentences]
- **Pros:** [bullets]
- **Cons / risks:** [bullets]
- **Estimated effort:** [days/weeks]

### Option B: [Name]
- [Same structure]

## Recommendation
[Which option and the core reason — 2-3 sentences. Be direct about the tradeoff you're accepting]

## Open Questions for Review
1. [Specific technical question needing input]
2. [Question]

## Out of Scope
[What's explicitly not being addressed]
```

---

## Tone Markers

- **Specific over vague.** "500ms P99 under 2K concurrent users" not "fast enough for production"
- **Honest about complexity.** Don't undersell implementation difficulty to get faster buy-in — it backfires in planning
- **Explicit about assumptions.** "This assumes the data model stays stable through Q2" surfaces hidden dependencies
- **No "easy" or "simple."** These words create false expectations. Describe what it actually takes
- **Tradeoffs, not pitches.** Engineers distrust writeups that only argue one side. Name the real downside of your recommendation

---

## Anti-Patterns

| Anti-Pattern | Why It Fails | Fix |
|---|---|---|
| Underselling complexity ("this should be straightforward") | Creates scope/estimate risk | Describe the actual work required |
| Vague requirements ("needs to be fast") | Can't be validated or measured | Add specific thresholds |
| Option comparisons without tradeoffs | Just a list, not analysis | Every option needs its real cost named |
| No open questions | Implies you've made all decisions unilaterally | Ask what you don't know |
| Business-first framing for a technical decision | Sounds like a PM pitch, not a technical spec | Lead with the constraint |
| "We've decided to use [technology]" with no rationale | Engineers will push back without context | Always include why this was chosen over alternatives |

---

## Context-Specific Variants

### Architecture Decision Records (ADR)
Follow the standard ADR format: Status · Context · Decision · Consequences
Include: alternatives rejected and why, not just the chosen path

### API Documentation
- Lead with the use case, then the endpoint
- Error cases before the success case (engineers care most about what breaks)
- Include authentication, rate limits, and retry behavior upfront

### Security / Compliance Reviews
- State the requirement being satisfied first (GDPR Article X, SOC 2 Control Y)
- Show how the implementation meets it — not just that "we use encryption"
- Include what's explicitly out of scope for this review

---

## Integration Notes

- Loaded by `/write --type technical`, `/spec` in AI feature mode, or when `--to` indicates engineering/architecture role
- Pairs with: `/spec` for full feature specs with technical requirements, `/think mode=challenge` for architecture reviews
- Cross-reference: `internal-team.md` for mixed PM/Eng audiences where the problem framing matters as much as the solution
