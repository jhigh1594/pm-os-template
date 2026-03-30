# Meeting Prep Generator

Prepare for stakeholder meetings with structured context, decisions, and talking points.

---

## Relationship

- **`/prep`** is the pre-meeting preparation complement to `/granola` (post-meeting extraction)
- **`/align`** is the broader stakeholder strategy; `/prep` is per-meeting tactical preparation
- **`Knowledge/People/[name].md`** files provide stakeholder context
- **`GOALS.md`** provides current priorities for context
- **`/granola`** is the downstream handoff after the meeting
- Use `/prep` before every significant stakeholder meeting; use `/granola` after

---

## Core Philosophy

**Meeting prep is about decisions, not agendas.**

- Clarify your goal before entering the room
- Surface decisions you need, not topics you want to discuss
- Know stakeholder positions before they speak
- Prepare for objections, not just talking points
- The fatal flaw: Meetings without a clear goal (Decision / Alignment / Information / Relationship)

---

## Command Syntax

```bash
/prep [--meeting <title>] [--people <names>] [--goal <goal>] [<description>]
```

**Arguments**:
- `--meeting <title>`: Meeting title or context (optional — e.g., "Q2 Roadmap Review")
- `--people <names>`: Comma-separated names of attendees (optional — e.g., "Louise, Marcus, Sarah")
- `--goal <goal>`: Your goal for the meeting (optional — e.g., "Align on DPD trade-offs")
- `<description>`: Additional context (optional — can provide interactively)

**Examples**:
```bash
/prep --people "Louise" --goal "align on DPD trade-offs"
/prep --meeting "Q2 Roadmap Review" --people "Louise, Marcus"
/prep --goal "Decision on pricing tier changes"
/prep
```

---

## Your Approach

### Step 0: Parse Arguments

Extract from the command invocation:
- `--meeting` value (optional)
- `--people` value (optional — comma-separated list)
- `--goal` value (optional)
- `<description>` if provided

### Step 1: Clarify Inputs (if missing)

If `--goal` and `--people` are missing, ask **one question**:
> "Who are you meeting with and what do you need to walk away with?"

Wait for answer before proceeding. If both are provided, skip to Step 2.

### Step 2: Assemble Context

Read for stakeholder context:
- `GOALS.md` — Current priorities and company bets
- `📚 Knowledge/People/[name].md` — For each person in `--people` (note if missing)
- `🤖 AI/memory/memory.md` — Current focus
- Relevant `📦 Products/` PRDs or roadmap — For context on topics likely discussed

**For each K/P file read**, assess knowledge freshness by scanning for the most recent date mentioned in the file. Compare to today's date:
- If the most recent date is **within 30 days**: mark as ✅ Fresh
- If the most recent date is **31-60 days ago**: mark as ⚠️ Aging — verify key positions before the meeting
- If the most recent date is **60+ days ago**: mark as 🔴 Stale — treat their current position as unknown; verify before relying on it
- If **no dates appear in the file**: mark as ⚠️ Undated — unknown freshness

Surface this in the Context Brief. Don't silently use stale context as if it's current.

If `Knowledge/People/[name].md` doesn't exist for someone, note: "⚠️ No context file for [name] — add basic notes to `Knowledge/People/[name].md` for better prep"

### Step 2.5: Product Knowledge Check

**Trigger**: Activate when ANY of these conditions are true:
- `--goal` contains "demo", "walk-through", "trial review", "product deep-dive", "product review"
- Any attendee in `--people` is an external customer (not a Planview employee)
- The meeting description includes product evaluation, onboarding, or support escalation context

**When triggered**, run these two checks:

**Check 1: Demo Guide Currency**
Look in `📚 Knowledge/Systems-and-Processes/` for any demo guide for the relevant product:
- If a guide exists created within the last 30 days → Surface it: "✅ Demo guide found: `[path]` — created [date]. Surfacing Competitive Awareness section if relevant."
- If no guide exists or the most recent is >30 days old → Add to Context Gaps: "⚠️ No current demo guide found for [product] — consider `/demo-prep --product [name]` before this meeting to prepare a fresh guide."

**Check 2: Competitive Context**
If a competitor is mentioned in the People file or meeting description:
- Check for `📚 Knowledge/Market/battlecard-[competitor-slug].md`
- If found → Add to Talking Points: "Competitive awareness for [competitor] available — see battlecard for key differentiators."
- If not found → Add to Context Gaps: "⚠️ No battlecard found for [competitor] — consider `/compete [competitor]` to build positioning."

Surface both findings in the prep package under a **Product Knowledge** subsection in the Context Brief (Section 2). Don't block the rest of the prep — this is a flag, not a gate.

---

### Step 3: Generate 7-Section Prep Package

**Section 1: My Goal** (One sentence)
Must be one of four types:
- **Decision**: "Walk away with a decision on [specific choice]"
- **Alignment**: "Get alignment on [specific proposal/direction]"
- **Information**: "Learn [specific information] from [person]"
- **Relationship**: "Build/strengthen relationship with [person]"

Force this choice — don't allow vague goals like "discuss X" or "update on Y".

**Section 2: Context Brief** (Per-person)
For each person in `--people`:
```
**[Name]**: [Role] | [Current position on relevant topics] | Context: [✅ Fresh / ⚠️ Aging (30-60d) — verify / 🔴 Stale (60d+) — treat position as unknown / ⚠️ Undated]
```
Keep to ≤2 sentences per person. If `Knowledge/People/[name].md` is missing, note what you don't know.

If any stakeholder is ⚠️ or 🔴, add: "⚠️ [Name]'s context may be outdated — verify their current position on [topic] before the meeting."

**Section 3: Decisions to Make** (Max 3 rows)
Table format:

| Decision | Options | My Rec | Stakes |
|----------|---------|--------|-------|
| [What needs to be decided] | [A, B, C] | [Your recommendation] | [What happens if we get this wrong] |

If more than 3 decisions, the meeting has too many decision points — flag this and recommend splitting.

**Section 4: Agenda** (3-4 items)
Time allocations totaling meeting length:

```
1. [Topic] — 10 min
2. [Topic] — 15 min
3. [Topic] — 10 min
4. [Topic] — 5 min
```

**Section 5: Anticipated Objections** (Per-person)
For each person, surface their likely concern and your prepared response:

```
**[Name] may object**: "[Their likely concern]"
**Your response**: "[Your prepared counter-argument or data point]"
```

**Section 6: Talking Points** (3-5 bullets)
What they need to understand or agree to before leaving:
- Focus on outcomes, not features
- Lead with evidence, not opinions
- Include specific data points when available

**Section 7: Questions I Need Answered** (2-3)
Specific questions (not open-ended topics):
- "What is your timeline expectation for [initiative]?"
- "What would block your approval of [proposal]?"
- "Who else needs to sign off on this?"

### Step 3.5: Champion Briefing Mode (External Customer Meetings)

**Trigger conditions — activate this mode when ALL of these are true:**
1. At least one attendee in `--people` is an external customer (not a Planview employee)
2. Their `Knowledge/People/[name].md` file indicates a champion relationship (they advocate internally for AgilePlace/Planview)
3. The meeting context suggests they will be acting on your behalf internally (exec review, steering committee, PI planning, renewal discussion)

**When this mode activates:** Replace the standard 7-section format with the Champion Briefing format below. The goal is not to inform the champion — it's to **equip** them.

> **Core principle:** Champions don't just need to understand your product — they need to be able to sell it internally without you in the room. Your job is to give them the story, the data, and the objection responses before the meeting where they'll need them.

---

**Champion Briefing Format:**

**Section 1: Champion Situation**
```
**[Champion Name]**: [Role + how they're positioned internally]
**Their internal audience:** [Who they're navigating — their exec, IT, peers, skeptics]
**What they're trying to accomplish:** [Their internal goal — approval, renewal, expansion, adoption]
**Where they're exposed:** [The question or objection they'll face that you need to help them handle]
```

**Section 2: Equip Their Internal Narrative**

Give them everything they need to represent your product internally:

```
**The story they should tell:**
[2-3 sentence narrative they can use with their executives — outcome-led, not feature-led]
Use the customer.md writing guide: lead with outcome, not capability.

**The data point that wins the room:**
[One specific, credible number — usage data, benchmark, or business outcome from a similar customer]

**The objection they'll face:**
"[Likely skeptical question from their exec or IT]"
→ **Their response:** "[The answer you want them to give — specific, credible, honest]"

**What they should NOT say:**
[Common misrepresentation or oversimplification that could backfire — e.g., overpromising a roadmap item]
```

**Section 3: What We Need From Them**
```
**Our ask at this meeting:**
[Be explicit — what specific action or commitment do we need from them as a result of this meeting?]

**What would help us most in the next 30 days:**
[1-2 specific things the champion could do — intro to their exec, reference customer call, internal testimonial]
```

**Section 4: Relationship Health**
```
**Last contact:** [date or "unknown"]
**Context freshness:** [✅ Fresh / ⚠️ Aging / 🔴 Stale]
**Champion health signal:** [What signals (positive or negative) indicate their advocacy is strong/at-risk]
**Risk:** [What could undermine their advocacy — organizational change, competitor evaluation, internal skeptics]
```

**Section 5: Next Steps**
```
[2-3 specific actions after this meeting — one for us, one for champion, one joint]
```

---

### Step 4: Stress Test (Optional)

After generating, ask:
> "Is there anything specific you're worried about going in? I can stress-test your talking points."

If they share a concern, role-play the objection and help refine the response.

### Step 5: Output Rich Contextual Handoff

```markdown
---
## Meeting Prep Complete

**Goal:** {meeting goal — Decision / Alignment / Information / Relationship}
**Top decision:** "{the most important decision in the Decisions table}"
**Watch for:** {name} on {topic} — most likely source of resistance

**Context gaps:** {list any missing Knowledge/People/ files or unknown positions}
**Staleness flags:** {[Name]: ⚠️ Aging / 🔴 Stale — or "All context fresh" if none flagged}

**After the meeting:**
```
/granola [today's date]
```
Extract insights and save to Knowledge/People/ while context is fresh.

---
```

---

## Key Constraints

- **Don't invent stakeholder positions** — Mark missing `Knowledge/People/[name].md` files explicitly
- **Max 3 decisions per meeting** — More means the meeting is overcrowded; recommend splitting
- **"My Goal" must be one of four types** — Force this choice; don't allow "discuss X" as a goal
- **Context brief ≤2 sentences per person** — Be concise; link to relevant artifacts

---

## Anti-Patterns to Avoid

**Vague Goal** — "Discuss the roadmap" or "Update on progress". Fix: "Walk away with alignment on Q2 top 3 priorities."

**Too Many Decisions** — 5+ decisions in one meeting. Fix: flag this and recommend splitting into two meetings.

**Generic Objections** — "They might have concerns." Fix: specific concern with specific response.

**Missing Stakeholder Context** — Not noting when `Knowledge/People/[name].md` is absent. Fix: always flag gaps.

**Topic Overload** — 6+ agenda items in 30-minute meeting. Fix: 3-4 items max; defer rest.

---

## Pattern References

- `GOALS.md` for current priorities
- `📚 Knowledge/People/[name].md` for stakeholder context
- `🤖 AI/memory/memory.md` for current focus
- `/granola` for post-meeting extraction
