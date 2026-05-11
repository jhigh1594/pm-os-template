---
description: Run the weekly review workflow
---
# Weekly PM Review

**Usage:** `/weekly-review [--week <YYYY-MM-DD of Monday>]`

A structured end-of-week PM operating rhythm. Five sections, ~30 minutes total.
The decision retrospective is the most important section — don't skip it when entries are due.

---

## Relationship

- `/okr-progress` handles OKR-specific deep analysis — delegated to in Step 3
- `/signal` feeds the signals section
- `📚 Knowledge/decisions/decision-journal.md` is the source for decision retrospectives
- `📚 Knowledge/People/` provides relationship health data in Step 4
- `📋 Tasks/today.md` and `GOALS.md` inform next-week priority setting

---

## Core Philosophy

**The weekly review is a calibration ritual, not a status report.**

Its job is to ask: Are we making good decisions? Are we capturing signal? Are we in front of the right people? Are we spending time on the right outcomes? A weekly review that just recaps completed tasks is a wasted 30 minutes.

---

## Command Syntax

```bash
/weekly-review [--week <YYYY-MM-DD>]
```

- `--week`: Monday of the week to review (default: current week)

---

## Step 0: Set the Scope

Default: current week (Monday–Friday).
If `--week` is provided, scope to that week.
State the week range: "Reviewing week of [Mon date] – [Fri date]."

---

## Step 1: Decision Retrospective (~10 min)

**Read `📚 Knowledge/decisions/decision-journal.md`.**

**Surface entries where review-date ≤ today AND outcome field is empty.**

For each due entry:
1. Display the original decision, date, type, and success criteria
2. Ask: "What happened? Did [success criteria] get met?"
3. After the answer: write a one-sentence outcome + what-we-learned into the journal entry
4. Classify: Was our Type 1/Type 2 assessment right? Was our confidence level calibrated?

Format for update:
```
**Outcome:** [Met | Missed | Exceeded | Reversed] — [one sentence of what actually happened]
**What we learned:** [One to three sentences. Focus on what to do differently or the same.]
```

**If no entries are due:** State the next upcoming review date and move to Step 2.

**Pattern check (after 5+ completed entries exist):**
Surface: "Looking at the last 5 decisions reviewed — any patterns in calibration?"
Examples: "Consistently overconfident on Type 2 reversibility" / "Underestimated stakeholder friction" / "Strong record on customer-driven decisions, weaker on internal process changes"

---

## Step 1.5: Growth Signal Synthesis (~5 min)

**Read `📚 Knowledge/Growth/growth-signals-[current-month].md`** (e.g., `growth-signals-2026-03.md`).
_(For cross-month pattern analysis — which failure modes recur across quarters — run `/growth-review` separately.)_

**If file has entries**, surface patterns:
- Count entries by archetype type
- Identify any archetype appearing 3+ times: flag as a **development theme**
- Surface the most recent response for each archetype

**Report:**
```
**GROWTH SIGNALS**
This month: N entries | Archetypes: [list with counts]
Development theme: [archetype with 3+ entries, or "No dominant theme yet"]
Most recent insight: "[quote from most recent entry, 1 sentence]"
```

**Pattern coaching** (after 5+ entries exist):
Surface: "Looking at your last 5 growth signals — [pattern observation, e.g., 'your strategy-coherence responses consistently identify the gap at the company mission layer' or 'assumption-visibility responses show strong identification but weak test design']."

**If file is empty or doesn't exist yet:**
State: "No growth signals captured this month yet. Quality gates in `/decide`, `/think`, `/brainstorm`, `/discover`, `/prioritize`, `/critique`, and `/price-intel` generate entries when you respond to the coaching questions."

---

## Step 2: Signal Review (~5 min)

Scan `📚 Knowledge/Research/signals-[current-month].md` for signals captured this week.

Report:
- N signals captured this week
- N signals total this month
- Top recurring theme (one phrase)
- If the same pain surfaced 3+ times this month: flag it as a pattern candidate for `/synthesize`

**Low-signal flag:** If fewer than 3 signals this week:
"⚠️ Below weekly signal target (3+). Were there customer conversations, support escalations, or sales calls this week that haven't been captured? Consider running `/signal` for any uncaptured observations."

---

## Step 3: OKR Health (~5 min)

Delegate to `/okr-progress` behavior for a fast portfolio read.

Focus questions:
- What's at risk heading into next week?
- Is any key result going to miss without a course correction?
- Are there dependencies blocking OKR progress that need escalation?

---

## Step 4: Relationship Health (~5 min)

Scan `📚 Knowledge/People/` files.

For each stakeholder in the "Manage Closely" or "Engage Actively" tier (high influence):
- Check last-contact date in their file
- Flag anyone where last contact > 14 days

Surface: "[Name] — last contact [date] ([N days ago]). Consider a brief touchpoint."

If no People/ files have dates, note: "Relationship health tracking requires last-contact dates in Knowledge/People/ files. Consider updating after this week's interactions."

---

## Step 5: Next-Week Planning (~5 min)

Ask: "What are the top 3 **outcomes** you need to drive next week?"

Framing — outcomes, not tasks:
- ✅ "Get Louise aligned on Q3 roadmap scope before the PI planning prep begins"
- ✅ "Validate the dependency view use case with 2 enterprise customers"
- ❌ "Send email to Louise" (that's a task, not an outcome)
- ❌ "Work on roadmap" (not specific enough)

Force-rank: 3 outcomes only. If more than 3 are named, ask: "If you could only accomplish one of these, which would move the needle most?"

---

## Output Format

```
### Weekly Review — Week of [Mon Date]

**DECISIONS**
Reviewed: N entries | Pending review: N entries
[Key learning from retrospective, or "No entries due this week"]

**SIGNALS**
This week: N | Month total: N
Top theme: [One phrase, or "No dominant theme yet"]
[Low-signal flag if applicable]

**OKR HEALTH**
[Green 🟢 / Yellow 🟡 / Red 🔴] — [One sentence on biggest risk or win]

**RELATIONSHIP FLAGS**
[Name(s) needing touchpoint, or "None — all key stakeholders contacted within 14 days"]

**NEXT WEEK — TOP 3 OUTCOMES**
1. [Outcome]
2. [Outcome]
3. [Outcome]
```

---

## Anti-Patterns

- **Don't skip the decision retrospective when entries are due** — this is the learning loop that improves judgment over time
- **Don't report task completion** — report outcomes driven
- **Don't add more than 3 next-week priorities** — force rank ruthlessly
- **Don't treat the signal check as optional** — the signal cadence is how continuous discovery actually stays continuous
- **Don't skip relationship health** — B2B PM leverage comes from relationships, not just artifacts

---

## Integration with Other Commands

- Use `/okr-progress` for deep OKR analysis (Step 3 delegates to this behavior)
- Use `/signal` to capture any uncaptured signals surfaced in Step 2
- Use `/decide` to log any decisions made during or as a result of the review
- Use `/today` for daily planning; `/weekly-review` is the Friday/Monday rhythm counterpart
