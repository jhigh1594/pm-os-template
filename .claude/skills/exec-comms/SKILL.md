---
description: 'Use when writing executive memos, board updates, or stakeholder communications.
  Triggers: executive memo, board update, 6-pager, BLUF, SCQA, stakeholder email,
  strategic document, exec summary, write for leadership, product pitch, strategic
  narrative, Andy Raskin, presentation story, five-act structure, compelling narrative,
  strategic-storytelling, narrative arc, why-now framing, movement narrative, five-act
  narrative, old world new world, emotional narrative, product narrative, pitch story.'
name: exec-comms
---

# Executive Communication

## When This Skill Activates

Claude uses this skill when:
- Writing executive memos
- Creating board updates
- Drafting stakeholder emails
- Structuring strategic docs
- Writing product pitches or presentations
- Framing features or initiatives as narratives
- Building cross-functional alignment

---

## Mode-Switching Logic — Pick This First

Before writing anything, identify which mode applies:

| Mode | When to use | Key signal |
|------|-------------|------------|
| **BLUF (Decision)** | Audience already cares. They need a decision or update. | They asked for it, or you have a standing reporting relationship. |
| **Narrative (Persuasion)** | Audience isn't bought in yet. They need to care before they'll engage with your recommendation. | Pitches, cross-functional alignment, board presentations where the outcome isn't predetermined, anytime the audience hasn't asked for the communication. |

**The rule:** BLUF assumes the reader cares. If they don't yet, narrative arc first — build context, then reveal.

**Trigger for Narrative mode:** Pitches. Alignment docs. Any communication where your audience hasn't opted in to caring about the topic yet.

**Trigger for BLUF mode:** Decision memos. Status updates. Meeting pre-reads where the audience already has stake in the outcome.

When in doubt: "Did this person ask me for this, or am I asking them to care?" If you're asking them to care, use narrative.

---

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

### 3. Narrative Mode — Andy Raskin's 5-Act Strategic Narrative

Use when the audience needs to be persuaded before they'll engage with your recommendation. The customer or stakeholder is the hero — not your product or initiative.

**Five-Act Structure:**

1. **Old World** — How things used to be (relatable, honest about the past — don't dramatize)
2. **Insight** — What changed? (the why-now — a shift in technology, market, or behavior that makes the old way no longer viable)
3. **New World** — What's now possible (the vision of the future state — make it concrete and desirable)
4. **Stakes** — Win big or lose (urgency — why acting matters, what teams that figure this out gain vs. what teams that don't lose)
5. **Your Role** — How you help them win (your product or initiative as the enabler — you're the guide, not the hero)

**Key principle (Nancy Duarte):** "Tune your message to the audience, not the other way around."

**Example:**
```markdown
## Act 1: Old World
"For years, teams coordinated through email..."

## Act 2: Insight
"But remote work changed everything. What worked in-office doesn't work distributed."

## Act 3: New World
"Now, the best teams coordinate in real-time, asynchronously..."

## Act 4: Stakes
"Companies that figure this out will attract best talent and move faster. Those that don't will lose to competitors."

## Act 5: Your Role
"That's where [Product] comes in. We help teams..."
```

### Building Each Act: From Skeleton to Persuasion

The structure above is the skeleton. Here's how to make each act land.

**Act 1: The Old World — Make It Real**
The audience must FEEL the problem before they'll care about the solution.
- Specificity beats universality: one vivid moment > "many customers experience..."
- Honest diagnosis: acknowledge what worked about the old way; don't strawman it
- No judgment: describe, don't editorialize
- Anti-patterns: Too much setup (boring). Exaggeration ("everything was broken") — loses credibility.
- Template: [Specific person] was [specific context], trying to [accomplish X], and [Y got in the way]. They felt [frustrated/stuck/resigned].

**Act 2: The Insight — Make It Inevitable**
Don't just state what changed. Make the audience see why the old way CANNOT work anymore.
- Name the specific shift: technology-driven ("the cloud made X possible"), behavior-driven ("remote work became default"), market-driven ("competitors figured this out first")
- Show causality: "because X happened, Y is no longer viable"
- Anti-patterns: Too abstract ("the world is changing"). Overstating the shift loses credibility.
- Template: But [specific shift happened]. And suddenly, [old approach] [specific failure mode]. The old way required [condition]. The new reality requires [different condition].

**Act 3: The New World — Make It Desirable**
Paint a future so concrete the audience can see themselves in it.
- Before-and-after comparison (show the delta, not just the destination)
- Emotional resonance: what does Tuesday look like now?
- Believable: grounded in reality, not aspirational fantasy
- Anti-patterns: "Imagine a world where..." (disconnected). Feature-focused ("you'll see a button") vs experience-focused ("your morning is different").
- Template: Now, [specific person] [does new thing] because [why it's possible]. [Specific time saved / friction removed / new capability]. They feel [different].

**Act 4: The Stakes — Make It Urgent**
Win big or lose. Why does timing matter?
- Real stakes (not manufactured fear)
- Competitive consequence: companies that figure this out gain [X]; those that don't face [Y]
- Time-sensitive: why now, not later?
- Anti-patterns: Doomsday predictions ("you'll fail") — sounds desperate. Making it about YOUR urgency, not theirs.

**Act 5: Your Role — Make It Inevitable (not self-serving)**
You're Gandalf, not Frodo. You remove the obstacle; the audience is the hero.
- Specific: "here's what we do and how it works" (not "we help teams...")
- Understated: it should be obvious you're the solution
- Next step is clear: what does the hero do Monday morning?
- Anti-patterns: Leading with your product features. Making promises you can't keep.

### Audience-Specific Narrative Tuning
- **Board:** Emphasize Acts 2 (market shift) + 4 (stakes) → why this, why now
- **Engineering:** Emphasize Act 1 (pain their customers feel) + Act 3 (better future feels like progress)
- **Sales field:** Emphasize Acts 1 + 5 (here's the pain, here's how you position it)
- **Customers:** Acts 1 (you know my pain) + 3 (better future) + 5 (here's how)

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

### Template: Product Pitch (Narrative Mode)

```markdown
## The Old World (Problem)
[How things worked before — honest about pain, not dramatized]

## The Insight (Why Now)
[What changed that makes this possible or necessary — be specific about the shift]

## The New World (Vision)
[What's now achievable — make it concrete and desirable]

## The Stakes (Urgency)
[What teams that figure this out gain; what teams that don't lose]

## Our Role
[How your initiative/product enables the new world — you're the guide, not the hero]

## Proof
- [Signal, metric, or early evidence]

## Ask
[Single clear call to action]
```

---

## Quick Reference

### 📝 Executive Comms Checklist

**Mode:**
- [ ] Mode selected: BLUF (decision) or Narrative (persuasion)?
- [ ] If narrative: stakeholder is the hero, not the product
- [ ] If BLUF: recommendation appears in first 2 sentences

**Structure:**
- [ ] BLUF (bottom line first) — if in BLUF mode
- [ ] Context clear
- [ ] Decision/recommendation obvious
- [ ] Next steps specific

**Style:**
- [ ] Concise (no fluff)
- [ ] Scannable (bullets, headers)
- [ ] Data-backed
- [ ] Action-oriented

**Narrative (if applicable):**
- [ ] Old world (relatable problem)
- [ ] Insight (why now)
- [ ] New world (vision)
- [ ] Stakes (urgency)
- [ ] Your role (you're the guide, not the hero)
- [ ] Emotional + logical
- [ ] Concrete examples
- [ ] Clear next steps

---

## Key Quotes

**Amazon:**
> "Start with the press release. Work backwards."

**On Executive Writing:**
> "If you can't summarize it in 2 sentences, you don't understand it well enough."

**Andy Raskin:**
> "The best product stories make the customer the hero, not your product."

**Nancy Duarte:**
> "The audience doesn't need to tune themselves to you — you need to tune your message to them."

---

## What Makes This Skill Different

Claude's default for executive communications is beautifully structured prose with too much detail. This skill forces BLUF (Bottom Line Up Front), assumes the reader has 90 seconds, and optimizes for decisions — not information transfer. The critical difference: an exec memo that doesn't make a recommendation or request a decision is a status update, not a communication. Every output must pass the "so what" test — not just what happened, but what it means and what action is needed.

For persuasion contexts (pitches, alignment moments), the failure mode is the opposite: leading with the recommendation before the audience cares about the problem. In these cases, narrative arc is required — build the old world, surface the insight, paint the new world, raise the stakes, then position yourself as the guide. The audience must feel the problem before they'll engage with the solution.

---

## Gotchas & Common Pitfalls

- **Using BLUF structure for a pitch where the audience isn't bought in yet.** BLUF assumes the reader cares — if they don't, leading with the recommendation before building context will lose them. Read the room: is this a decision memo or a persuasion moment? If persuasion, use narrative arc. The tell: did they ask for this communication, or are you asking them to care about something new?

- **Writing a 3-page memo when the exec needs 3 bullets and an ask.** Root cause: Claude defaults to thoroughness and treats every communication as a document. Fix: decide the format (email, 1-pager, 6-pager) before writing. If no format is specified, default to the shortest form that conveys the decision. When in doubt, ask: "Does this reader need the full memo or just the BLUF?"

- **Burying the recommendation in the middle.** Root cause: SCQA tempts a narrative buildup that places the answer after context and complication. Fix: the recommendation or ask must appear in the first 2 sentences of the document, regardless of structure. Repeat it at the end if the document is long. No executive should have to hunt for the point. (Exception: narrative mode — the ask comes last, after the stakes are felt.)

- **Hedging every claim instead of making confident assertions.** Root cause: Claude defaults to qualifiers like "we believe this could potentially" to avoid being wrong. Fix: execs need evidence-backed confidence. State the claim directly ("X will drive Y"), then attach the evidence. If confidence is genuinely low, flag it explicitly as a risk rather than diluting the entire memo with hedging language.

- **Producing the right memo for the wrong audience.** Root cause: treating all executive communications the same. Fix: before writing, confirm the audience. A board update is backward-looking and governance-oriented. A VP-level pitch is forward-looking and resource-oriented. A skip-level email to a C-suite needs even more compression and zero internal jargon. Adjust depth, vocabulary, and framing accordingly.

- **Reporting what happened without explaining the "so what."** Root cause: confusing information transfer with executive communication. Fix: every section must answer "what does this mean for the business and what action is needed?" If a section only describes a state of affairs with no implication, cut it or rewrite it to surface the implication. Exec comms that inform without enabling a decision are status reports — use a different format.

- **Making your product or initiative the hero of a pitch.** Root cause: it's natural to lead with what you built. Fix: the customer or stakeholder must be the hero — they're the one who needs to win. Your product is the guide (Gandalf, not Frodo). Lead with their world, their problem, their stakes — then show how you help them win.

## Self-Learning

Before responding, read `LEARNED.md` in this skill directory when it exists and treat it as compact runtime guidance that sharpens this skill.

Rules for self-improvement:
- Keep `SKILL.md` human-owned; do not rewrite it directly from normal usage.
- Propose broader instruction changes through the central skill-learning review queue.
- Only promote specific, reusable, evidence-backed lessons into `LEARNED.md`.
