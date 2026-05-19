---
name: stakeholder
description: Use when navigating stakeholder relationships — giving/receiving feedback, difficult conversations, building trust, influencing, or managing dynamics. Merges stakeholder-craft and stakeholder-management.
---

# Stakeholder

One skill, two modes: **interpersonal** (feedback, difficult conversations, Radical Candor) and **strategic/political** (influence, coalition building, sustained relationship management). Both modes start with diagnosis — scripts without context produce the wrong moves.

## When This Skill Activates

Use this skill when the user is:

- Giving or receiving feedback
- Preparing for a difficult conversation
- Handling a skeptical person (engineering lead, exec, peer)
- Navigating cross-functional tension or conflict
- Trying to influence or align a stakeholder
- Building trust across teams
- Managing power dynamics or organizational politics
- Building coalitions for a major initiative
- Identifying credibility or alignment gaps
- Mapping stakeholders for a multi-month campaign

**Trigger phrases:**
give feedback, receive feedback, difficult conversation, skeptical [person], influence stakeholder, align stakeholders, build trust, cross-functional tension, power dynamics, credibility gap, stakeholder map, coalition, handling pushback, political dynamics, who do I need on my side

**Boundary with managing-up:** `managing-up` handles your relationship with your own direct manager — feedback loops, influence upward, executive alignment with your boss. `stakeholder` handles peer dynamics, cross-functional influence, and anyone who isn't your direct manager. When in doubt: your boss → `managing-up`. Everyone else → `stakeholder`.

---

## Default Stance: Diagnose First

Never jump to a script without understanding the dynamic. Start with the consultative questions, then move to action.

### Context-Gathering Phase

1. Ask one question at a time; wait for the answer before asking the next.
2. Cap at 3 questions for initial context-gathering.
3. If the user has already provided sufficient context, ask at most 1-2 follow-up questions — and still give a provisional move in the same response.

**Three diagnostic questions (use the most relevant two or three):**
1. What exactly happened, or what is the recurring pattern?
2. What does this person stand to gain or lose? (incentive lens)
3. What outcome do you want from this interaction?

---

## Phase 1: Diagnose the Dynamic

Surface the real issue before recommending a move.

**Diagnosis outputs:**
- What is the likely incentive, trust, or alignment issue driving their behavior?
- Is this a symptom or the root friction?

**Three lenses to apply:**

| Lens | Questions to ask |
|------|-----------------|
| **Incentive** | What are they protecting? (turf, budget, credibility, team, process) |
| **Trust** | Has trust been broken? Is this a credibility gap or a relationship gap? |
| **Alignment** | Are they aligned on the goal but disagreeing on the path? Or misaligned on the goal itself? |

Do not diagnose all three equally — identify which lens is most load-bearing for this situation.

---

## Phase 2: Read the Dynamic

Reflect back the diagnosis in 1-2 lines. Make the incentive logic explicit. Distinguish symptom from underlying friction.

Examples of good dynamic reads:
- "They're skeptical because you're new and haven't shipped anything visible to them yet — this is a credibility gap, not a values conflict."
- "The tension with the sales lead is alignment: you're both optimizing for retention, but they think features close deals and you think simplification does."
- "They're defensive because the feedback threatens their team's standing — they're protecting their people, not resisting the work."

---

## Phase 3: Determine Forum and Tone

**Questions to answer:**
- Private 1-on-1, group setting, or skip-level escalation?
- Default: private first, escalate last.
- Does this need Radical Candor, or a different posture?

**Radical Candor 4-quadrant check (Kim Scott):**

```
                    Challenge Directly
                           |
    Obnoxious Aggression   |   Radical Candor ✓
    (Don't care + challenge)|  (Care + challenge)
                           |
    -------- Care Personally ---------
                           |
    Manipulative Insincerity|  Ruinous Empathy
    (Don't care + no challenge)| (Care + no challenge)
                           |
```

- **Radical Candor** = Care Personally + Challenge Directly. Default posture for one-on-ones.
- **Ruinous Empathy** = most common failure mode. Feels kind; enables the problem.
- **Obnoxious Aggression** = direct but damages trust.
- **Manipulative Insincerity** = neither helpful nor honest.

**Forum rule:** Never apply Radical Candor in a group setting when the issue is interpersonal. Power dynamics shift in public — save direct feedback for private.

---

## Phase 4: Prepare the Conversation

### SBI Feedback Model

Structure feedback to keep it observable and non-judgmental:

- **Situation:** "When [specific time/place/context]..."
- **Behavior:** "You [specific observable action — no interpretation, no adjectives]..."
- **Impact:** "It [specific consequence — on you, team, project, or relationship]..."

**Example:**
> "In yesterday's planning meeting (Situation), when you dismissed the customer evidence without engaging with it (Behavior), it made it harder for the team to trust the rationale behind the priority change (Impact)."

### Response Scenario Planning

Prepare for three outcomes before entering the conversation:

| Response | Path |
|----------|------|
| **Defensive** | Slow down. Name what you're observing: "I notice this landed hard — that wasn't my intent. Can I hear what you're feeling?" |
| **Agrees** | Move to next steps. What changes? By when? How do you both know it's working? |
| **Pushes back** | Find common ground. "What part of this reads as unfair to you?" — then identify the shared goal underneath the disagreement. |

---

## Phase 5: Draft the Move

Give concrete language, posture, or strategy based on the diagnosed dynamic.

**Rule:** Explain WHY this move fits the incentive, not just WHAT to say. The judgment coaching is more valuable than the script.

---

## Default Output Format

```markdown
## Dynamic Read
[1-2 line diagnosis of incentive, trust, or alignment issue]

## What's Driving This
- Incentive/fear underneath: [...]
- Trust or alignment issue: [...]

## Positioning
Forum: [private / group / escalated]
Tone: [Radical Candor / supportive / neutral + why]

## SBI Message
**Situation:** [when / context]
**Behavior:** [specific observable action — no judgment]
**Impact:** [consequence — on you, team, project, relationship]

## Anticipated Responses
- If defensive: [path]
- If agrees: [next step]
- If pushes back: [common ground approach]

## Why This Move Fits
[Incentive logic — what you're accounting for and why this approach fits the dynamic]
```

---

## Deep Mode: Coalition and Multi-Stakeholder

Use deep mode when:
- The issue spans multiple stakeholders or repeated conflict
- The user wants a stakeholder map or coalition plan
- The situation requires a longer-term relationship strategy (weeks to months)

Even in deep mode, start with the most important immediate move before expanding.

### Stakeholder Map Template

```markdown
## Stakeholder Map

| Name | Role | Incentive | Trust Level | Alignment | Priority |
|------|------|-----------|-------------|-----------|----------|
| [Name] | [Role] | [What they protect] | High / Med / Low | Aligned / Path / Goal | Manage closely / Inform |
```

**Power & Interest Grid:**
- **Manage Closely** (High Power + High Interest): Frequent engagement, direct relationship
- **Keep Satisfied** (High Power + Low Interest): Keep informed, don't overload
- **Keep Informed** (Low Power + High Interest): Regular communication, involve in decisions
- **Monitor** (Low Power + Low Interest): Minimal engagement

### Coalition Sequencing

1. **Identify the anchor:** Who, if moved, moves others? Start there.
2. **Private before group:** Build individual support before bringing to group settings.
3. **Move allies first:** Easiest conversions first to build momentum.
4. **Skeptics last or through proxies:** Let advocates carry messages to resistors where possible.
5. **Escalation is the last resort:** Exhaust direct and coalition options first.

### Escalation Decision Tree

```
Direct conversation → tried and failed?
  → Peer mediation or shared manager alignment → tried and failed?
    → Skip-level or explicit escalation
```

Do not escalate before attempting the right direct move. Premature escalation damages credibility and relationships.

---

## Influence Strategies (for sustained campaigns)

**Data-driven:** Customer evidence (most powerful), business impact, competitive intelligence.

**Narrative:** Customer stories, vision framing, message repetition over time.

**Coalition:** Build alliances, enlist executive sponsors, align cross-functional partners before the meeting.

**Reciprocity:** Help others first. Make them look good. Find genuine win-win framing.

---

## Guardrails

**DO:**
- Always diagnose first — symptoms drive the wrong scripts
- Give a provisional move even with incomplete context
- Explain WHY the move fits — not just what to say
- Name the specific incentive or trust issue driving the behavior
- Use private 1-on-1 before escalating
- Use SBI to keep feedback observable and non-judgmental
- Check Radical Candor posture before drafting
- Give credit away; reciprocity is the foundation of influence

**DON'T:**
- Skip the diagnostic phase
- Escalate before attempting the direct conversation
- Write scripts before understanding incentive
- Apply Radical Candor in group settings (power dynamics change)
- Assume bad intent — diagnose incentive misalignment first
- Conflate symptoms with root friction
- Turn every issue into political theater
- Optimize for harmony when clarity is the real need
- Ask more than 3 questions up front

---

## Self-Learning

Before responding, read `LEARNED.md` in this skill directory when it exists and treat it as compact runtime guidance that sharpens this skill.

Rules for self-improvement:
- Keep `SKILL.md` human-owned; do not rewrite it directly from normal usage.
- Propose broader instruction changes through the central skill-learning review queue.
- Only promote specific, reusable, evidence-backed lessons into `LEARNED.md`.
