---
description: Run the follow up workflow
---
# Meeting Follow-Up Generator

Transform a meeting into communicated decisions, tracked action items, and updated stakeholder context — closing the post-meeting dead zone.

---

## Relationship

- **`/follow-up`** is the post-meeting execution step, downstream of `/granola`
- **`/granola`** extracts meetings and surfaces follow-up candidates — it triggers the prompt to run `/follow-up`
- **`/prep`** is the pre-meeting counterpart — together they bookend every significant meeting
- **`/write`** is the drafting engine for exec-level follow-up communications — `/follow-up` invokes it when needed
- **`Knowledge/People/[name].md`** files are updated by `/follow-up` (on confirmation) — never auto-written
- **`/align`** is for broader stakeholder strategy; `/follow-up` is for per-meeting execution

---

## Core Philosophy

**The decision communicated is the decision that sticks.**

Meeting prep without follow-up is a sunk cost. Decisions evaporate within 48 hours if they aren't written down and sent. Action items without owners are wishes. The follow-up is where the meeting becomes work.

The fatal flaw: sending "great meeting, let's follow up!" with no substance. Fix: always name the decision, the owner, and what's still open.

---

## Command Syntax

```bash
/follow-up [--meeting <title-or-path>] [--type <format>] [--people <names>]
```

**Arguments**:
- `--meeting <title-or-path>`: Meeting title (searched in granola directory) or absolute file path
- `--type`: Communication type override (`decisions | action-items | update | ask`) — default: auto-detect
- `--people`: Comma-separated recipient names (optional — inferred from participants if not provided)

**Examples**:
```bash
/follow-up                                                    # Interactive — asks for meeting context
/follow-up --meeting "Q2 Roadmap Review"                     # Find by title in granola directory
/follow-up --meeting "26-03-26-q2-roadmap-review.md"        # Specific file
/follow-up --meeting "DPD Trade-offs" --people "Louise, Marcus"
/follow-up --meeting "NatWest sync" --type decisions
```

---

## Your Approach

### Step 0: Parse Arguments and Load Meeting

Extract from the command invocation:
- `--meeting` value (required — ask if not provided)
- `--type` value (optional — auto-detect from meeting content if not specified)
- `--people` value (optional — infer from participants list in meeting file)

**If `--meeting` is a file path:** Read that file directly.

**If `--meeting` is a title:** Search `🏢 Company/meetings/granola/` for the most recent file whose title matches. Case-insensitive, partial match is fine.

**If no `--meeting` provided:** Ask: "Which meeting do you want to follow up on? (title or date, e.g. 'DPD sync today' or '2026-03-26')"

### Step 1: Extract Follow-Up Material

Read the meeting file and extract:

**Decisions:** Look for explicit decisions ("we decided", "agreed to", "going with", "confirmed") and implicit decisions (where discussion resolved and moved on). If unclear, mark as `[VERIFY — may need confirmation]`.

**Action items:** Look for commitments ("will do", "I'll", "owner:", "by [date]", "follow up on"). Assign owners as named in the meeting. If no date stated, note `[date TBD]`.

**Open questions:** Items explicitly deferred, unresolved disagreements, or questions asked with no answer given in the meeting.

**Commitments:** Promises made to external parties (customers, leadership) that now have delivery expectations attached.

**Stakeholder signals:** Any notable shift in position, new concern surfaced, or alignment that didn't exist before this meeting.

If the meeting notes are sparse (e.g., only a transcript with no structured notes), do your best and flag: "⚠️ Notes were thin — verify these extractions before sending."

### Step 2: Classify Follow-Up Type

If `--type` was not specified, determine the primary follow-up need:

- **decisions**: Decisions were made that need to be communicated to inform stakeholders
- **action-items**: Specific tasks were assigned that each owner needs to see
- **update**: Status update — meeting was informational, outcomes need to be shared broadly
- **ask**: Something was left unresolved; a specific person needs to make a call

If multiple types apply, default to **decisions** and note the others.

### Step 3: Draft Communication

Draft the follow-up using the structured format below. Load `Knowledge/People/[name].md` for each recipient if the file exists — note their known priorities and tailor accordingly.

**Standard follow-up format:**

```
Subject: [Meeting title] — Decisions + Next Steps

Hi [name(s)],

[One sentence context if needed: "Following our [meeting] today on [topic]."]

**Decision:** [What was decided — be specific]

**Action items:**
- [Owner]: [Action] by [Date]
- [Owner]: [Action] by [Date]

**Still open:** [What's unresolved — who owns resolution and by when]

[Optional closing sentence if relationship or stakes warrant it]
```

**Type-specific rules:**

- **Exec-level recipients** (Louise, Zilli, or identified exec): Load `exec-comms` skill. Lead with BLUF — the decision or ask in the first sentence, before any context. Max 5 sentences total.
- **Peer / cross-functional**: Standard format above. Professional, direct.
- **Stakeholder ask**: End with a single, explicit ask — "I need a decision on X by [date]." Load `influence-craft` skill for framing if position is uncertain.
- **Action-item-only**: One line per owner, no narrative. Just names, actions, dates.

**Constraints:**
- Max 3 action items per follow-up — if there are more, it means the meeting had too many decisions; flag this: "⚠️ This meeting had 5+ action items — consider splitting follow-ups by workstream."
- Always include "Still open" section — never imply all loose ends are resolved
- Never fabricate a decision — mark uncertain decisions as `[VERIFY before sending]`

### Step 4: Knowledge/People/ Updates

For each participant who has a file in `📚 Knowledge/People/`, surface one specific update candidate based on what was learned:

```
Update candidate — [name].md:
Add: "[One sentence: new position, concern, commitment, or relationship signal from this meeting]"

Confirm to write? (yes / skip)
```

Ask for each person individually — don't batch. Write only on confirmation.

If a meeting participant does **not** have a `Knowledge/People/` file, offer:
```
No file exists for [name]. Create one from this meeting? (Adds basic context: role, key concern from meeting)
```

### Step 5: Output Handoff Block

```markdown
---
## Follow-Up Complete

**Meeting:** [title] — [date]
**Follow-up type:** [decisions / action-items / update / ask]
**Drafted for:** [recipient names]
**Action items tracked:** [N] (owners + dates assigned)
**Still open:** [N] items — [who owns resolution]

**Knowledge/People/ updates:**
- [name].md: [Updated / Skipped / Created]

**Prep context utilized:** [Yes — /prep was run for this meeting / No — no prep file found]

---
```

---

## Key Constraints

- **Never auto-write** to `Knowledge/People/` — always confirm before writing
- **Max 3 action items per email** — flag if more; don't silently include all of them
- **Always include "Still open"** — a follow-up without open items is usually incomplete
- **Never fabricate decisions** — if notes are ambiguous, mark `[VERIFY before sending]` and flag it
- **Exec format = BLUF** — decision or ask in the first sentence, always
- **Don't manufacture urgency** — if no deadline was stated, don't invent one

---

## Anti-Patterns to Avoid

**"Great meeting!" opener** — Adds nothing. Fix: open with the decision or ask.

**Burying the decision** — Decision is in paragraph 3. Fix: lead with it (BLUF for execs; clear subject line for peers).

**Missing "still open"** — Implies everything was resolved. Fix: always name what's open and who owns it.

**Action items without owners** — "We'll look into X" with no name. Fix: surface it explicitly as unassigned: "⚠️ Owner needed: [action]."

**Writing to Knowledge/People/ without confirmation** — Fix: always ask before writing; context may be sensitive.

---

## Integration Points

**Entry from:**
- `/granola` — which auto-surfaces the prompt "Run `/follow-up --meeting "[title]"`"
- Direct invocation after any significant meeting, call, or decision conversation
- `/prep` reference: if /prep was run before this meeting, reference it to check whether goal was achieved

**Exit to:**
- Updated `Knowledge/People/[name].md` files (on confirmation)
- Communication drafted for sending
- `/align` — if follow-up reveals a stakeholder is still unaligned after the meeting
- `/prep` — next meeting prepped with updated stakeholder context

---

## Meeting Follow-Up Quality Checklist

Before finalizing the draft, verify:
- [ ] Decision is stated explicitly (not implied)
- [ ] Every action item has an owner and a date (or date TBD flagged)
- [ ] "Still open" section is present
- [ ] Exec recipients get BLUF opening
- [ ] Sensitive commitments are marked `[VERIFY]` not stated as fact
- [ ] Knowledge/People/ update candidates surfaced for all known participants
