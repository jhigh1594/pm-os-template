---
name: enhance-context
description: |
  At the end of a knowledge-rich session, scan for new information and propose
  targeted, evidence-backed updates to the 5 core context files in 🤖 AI/context/.
  Proposal-first — never writes without explicit user confirmation.

  Triggers: enhance context, update context files, capture what we learned,
  sync context, what should I save from this session, end of session memory sync,
  update my context, consolidate findings
---

# Enhance Context

Use this skill when a session produced new knowledge worth preserving — research findings,
competitive intelligence, customer insights, strategic decisions, persona signals, or
changes to goals or priorities.

## Default Stance: Proposal First

Scan the session → identify which context files have new information → propose specific
changes in a structured format → wait for explicit user confirmation before writing anything.

---

## The 5 Context Files

All files live at `🤖 AI/context/`. Each has a defined purpose:

| File | What belongs here | Update cadence |
|---|---|---|
| `company.md` | Company mission, scale, market position, strategic bets | Rarely — major pivots only |
| `product.md` | Product health metrics, capabilities, positioning, strategic questions | Monthly or after significant product events |
| `personas.md` | Buyer archetypes with pain, motivation, buying behavior | After customer/sales conversations |
| `competitors.md` | Competitor profiles, win conditions, GTM patterns | After competitive intelligence or win/loss |
| `goals.md` | Current quarter priorities, stakeholder map, open strategic questions | Quarterly or after significant strategy decisions |

---

## Execution

### Step 1: Session Intake

If the session's focus is obvious from context, skip asking. Otherwise ask once:

> "What were the key findings or decisions from this session?"

Accept a brief summary — don't need exhaustive detail. Look for:
- New facts about the company, product, competitors, or market
- Customer or stakeholder signals about pain, motivation, or buying behavior
- Strategic decisions or priority changes
- Resolved or newly opened strategic questions

### Step 2: File Mapping

For each of the 5 context files, check: *does the session contain new information
that would improve this file?*

Skip a file entirely if the session didn't touch its domain.

**What triggers an update:**

- **company.md** — Executive direction changes, market position shifts, new strategic bets, updated revenue/scale facts
- **product.md** — New health metrics, feature launches or deprecations, resolved strategic questions, capability additions
- **personas.md** — Customer interview signals, sales conversation patterns, new buyer archetype emerging, pain/motivation updates
- **competitors.md** — Competitor moves, new product launches, pricing changes, win/loss patterns, new entrant identified
- **goals.md** — Quarterly goal changes, stakeholder relationship shifts, new open strategic questions, resolved decisions

### Step 3: Propose Changes

For each file with updates, present proposals in this format:

```
## [filename] — [Section Name]

**Current:**
> [exact excerpt from file being replaced, if applicable — quote it]

**Proposed:**
[new text, written in the same style and markdown format as the file]

**Reason:** [why this matters — what signal or finding drove it]
**Confidence:** certain / likely / provisional
**Source:** [where in the session — e.g., "competitive analysis against Atlassian"]
```

Present ALL proposals together before asking for confirmation. Group by file.

**Confidence levels:**
- **certain** — Direct statement from a reliable source (exec, customer, analyst)
- **likely** — Strong inference from multiple consistent signals
- **provisional** — Single signal or early indication; mark in file as "(provisional)"

### Step 4: Confirmation Gate

After presenting all proposals:

> "I found [N] proposed update(s) across [M] file(s). Approve all, or tell me which to skip or modify."

Accept:
- "Approve all" / "looks good" → write everything
- "Skip [file]" → exclude that file
- "Change [X] to [Y]" → incorporate edit before writing
- "None" / "skip" → write nothing

**Never write without a clear approval signal.**

### Step 5: Write Updates

For each approved change:
1. Make only the specific proposed change — don't rewrite sections not in the proposal
2. Preserve all existing markdown structure, headers, tables, and formatting exactly
3. Update the `_Last updated:` line at the top of the file to today's date
4. Confirm each file written: "Updated `context/[filename]`"

---

## Guardrails

- **Never write without explicit confirmation** — proposals are drafts, not commits
- **Never merge conflicting signals** — if session produced info that contradicts an existing entry, surface the conflict explicitly: "This contradicts the current entry about X. Which is accurate?"
- **Mark provisional facts in the file** — append "(provisional — validate next session)" after the text
- **Skip a file if there's nothing new** — don't force updates for completeness
- **Don't add length for its own sake** — shorter, clearer entries beat comprehensive ones. If a proposed addition overlaps with existing content, merge rather than append.
- **Preserve Jon's voice and notes** — lines starting with "**Jon's note:**" are personal judgment calls; only update if Jon explicitly asks to

---

## Integration

**Related commands:**
- `/refresh-memory` — Updates `memory.md` session log (operational state)
- `/remember` — Recalls prior context from conversation history + workspace docs
- `/capture-pattern` — Captures patterns to `learned-patterns.md`

**When to use which:**
- `/enhance-context` → new *knowledge* (facts, personas, competitive intel, strategy)
- `/refresh-memory` → new *session activity* (what we did, what changed)
- `/capture-pattern` → new *procedural patterns* (how to do things, workspace conventions)

**Typical end-of-session sequence:**
1. `/enhance-context` — capture knowledge gained
2. `/refresh-memory` — log session activity
