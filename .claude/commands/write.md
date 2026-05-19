---
description: Run the write workflow
---
# PM Communication Writer

Write stakeholder communications with PM-specific structure, skill routing, and audience-aware context.

---

## Relationship

- **`/write`** is the PM communication drafting command — routes to the right skill and structure based on communication type
- **`elite-copywriter`** handles general writing quality and style (loaded automatically for most types)
- **`exec-comms`** skill handles executive-level communications (loaded for exec update type)
- **`influence-craft`** skill handles persuasion-framed asks (loaded for stakeholder ask type)
- **`/prep --post`** is the post-meeting follow-up command — use it after a meeting to extract decisions and draft follow-up comms
- **`/align`** is for broader stakeholder strategy; `/write` is for drafting specific communications

---

## Command Syntax

```bash
/write [--type <format>] [--to <name>] [<what-to-write>]
```

**Arguments**:
- `--type`: Communication type (`exec | follow-up | ask | announcement | data`) — auto-detected if not specified
- `--to`: Recipient name(s) — used to load `Knowledge/People/[name].md` context and adjust tone
- `<what-to-write>`: Description of what to write (optional — can provide interactively)

**Examples**:
```bash
/write --type exec --to "Louise" "Q2 roadmap decision update"
/write --type ask --to "[Name]" "approval on [initiative] trade-off recommendation"
/write --type announcement "[Product] [feature] GA launch"
/write "stakeholder update on NatWest capacity discussions"   # auto-detect type
```

---

## Step 0: Classify Communication Type

**Before drafting anything**, identify which of four communication types this is:

**1. Exec update** — Outbound status, decision, or recommendation to executive-level stakeholders (Louise, Zilli, or equivalent VP+). Characterized by: one-way information flow, decision already made, recipient needs to be informed or aligned.

**2. Meeting follow-up** — Communicating decisions made, action items assigned, or outcomes from a specific meeting. Characterized by: references a specific meeting, has decisions + owners + next steps.
> ⚠️ If you have a Granola meeting file, use `/follow-up --meeting "[title]"` instead — it has dedicated extraction logic.

**3. Stakeholder ask** — Seeking a decision, approval, unblocking, or alignment from a specific person. Characterized by: there is a specific ask at the end, requires the recipient to do or decide something.

**4. Announcement/broadcast** — Wider team or customer-facing communication about a launch, change, or initiative. Characterized by: broad audience, informational or celebratory, no specific ask.

**5. Data narrative** — Presenting data, metrics, or analysis to a non-data audience. Characterized by: data is the central input, the goal is insight + implication (not just numbers), audience may not be data-literate.

**If unclear**, ask one question: "Is this informing someone of a decision, asking someone to decide something, following up on a meeting, announcing something broadly, or presenting data/findings?"

---

## Step 1: Load Stakeholder Context

If `--to` is specified (or a person is named in the request), check for their `Knowledge/People/[name].md` file:

- **If file exists**: Read it. Note their known priorities, current position on relevant topics, and communication preferences. Tailor the draft accordingly and note: "Tailoring to [name] based on: [one sentence of context used]."
- **If file doesn't exist**: Note the gap: "⚠️ No context file for [name] in Knowledge/People/ — tailoring based on role context only."

For exec-level recipients, also read `GOALS.md` to ensure the communication aligns with current stated priorities.

---

## Step 1.5: Load Audience Narrative Guide

After resolving the recipient (from `--to`, People/ context, or content description), identify the audience type and load the appropriate guide from `📚 Knowledge/Writing-Styles/`.

**Audience Resolution:**

| Signal | Guide to Load |
|--------|--------------|
| Recipient is VP+, C-suite, or `--type exec` | `executive.md` |
| Recipient is external customer, prospect, or `--type announcement` (external) | `customer.md` |
| Recipient is cross-functional partner, engineer, designer, or `--type follow-up` (internal) | `internal-team.md` |
| Recipient is engineer/architect, or `--type technical` | `technical.md` |
| Recipient is board member, investor, or analyst | `board-analyst.md` |
| Recipient is AE, SE, CSM, or `--type sales` | `sales-se.md` |

**Resolution priority:** Explicit `--type` argument > recipient role from People/ file > content description inference.

**After loading the guide, apply:**
- Its **Opening Logic** — the sentence-1 rule
- Its **Evidence Hierarchy** — order supporting points accordingly
- Its **Structure Template** — as the scaffold for the draft
- Its **Anti-Patterns** — as a final check before output

**Note in the final output:**
```
Narrative guide applied: [audience] — opening rule: [one sentence from the guide]
```

**If audience is ambiguous or unknown:** Proceed without a guide; apply type-specific structure from Step 2 only. Note: "No narrative guide loaded — type structure applied."

---

## Step 2: Apply Type-Specific Structure and Skill

### Exec Update
**Load:** `exec-comms` skill

**Structure:**
- BLUF in sentence 1 — the decision, status, or recommendation up front, before any context
- Context (1-2 sentences max) — why this matters or what happened
- Implication for them — what they need to know or do
- Length: 1 page max, ideally 5-8 sentences

**Example opening:** "We're moving forward with Option B on [initiative] — here's what that means for Q2."

**Not:** "Thank you for your continued partnership. I wanted to update you on recent developments regarding..."

### Meeting Follow-Up
> If you have a Granola meeting file, use `/prep --post` instead — it has dedicated extraction logic.

If proceeding here:

**Structure:**
```
Subject: [Meeting title] — Decisions + Next Steps

**Decision:** [What was decided — be explicit]

**Action items:**
- [Owner]: [Action] by [Date]

**Still open:** [What's unresolved + who owns it]
```

Never write "great discussion" or similar pleasantries as the opener. Lead with the decision.

### Stakeholder Ask
**Load:** `influence-craft` skill

**Structure:**
- Context: One sentence on why this is coming up now
- WIIFM framing: What's in it for the recipient (or their team) to say yes
- The ask: Single, explicit ask stated clearly — "I need a decision on X by [date]"
- Options (if applicable): Make it easy to decide — "Option A is [X], Option B is [Y], I recommend A"

Do not bury the ask. It should be unmissable.

### Announcement/Broadcast
**Load:** `elite-copywriter` skill

**Structure:** Context-dependent. Follow elite-copywriter's audience-first approach with:
- Hook: Why this matters to this audience
- What's changing/launching and when
- What they need to do (if anything)
- Where to learn more

### Data Narrative
**When**: Presenting metrics, research findings, or analysis to stakeholders who aren't data-literate. Goal is insight + implication — not a data dump.

**Structure:**
- Context: What were we measuring and why? (1 sentence)
- Insight: The single most important thing the data shows — lead with this
- Evidence: 2-3 supporting data points that back the insight
- Implication: What this means for decisions, priorities, or action

**Rules:**
- One headline insight — don't bury it in charts or tables
- Numbers need context: "34% adoption" means nothing; "34% adoption, vs. 18% benchmark for comparable launches" means something
- If presenting 3 numbers, the audience retains 0. Pick 1.
- End with a clear "so what" — what should they do or believe differently because of this data?

**Length:** 5-8 sentences for narrative framing; attach raw data or charts separately

---

## Step 3: Draft Communication

Apply the type-specific structure from Step 2. Keep drafts concise:

- **Exec update**: 5-8 sentences, max 1 page
- **Meeting follow-up**: Decision + 1-3 action items + still open — no filler
- **Stakeholder ask**: 4-6 sentences with explicit ask
- **Announcement**: Appropriate for audience; err on the side of shorter

After drafting, note:
```
Type: [exec update / meeting follow-up / stakeholder ask / announcement]
Skill applied: [exec-comms / influence-craft / elite-copywriter]
Tailored to: [name + one sentence of context used]
```

---

## Quick Reference for PM Context

When applicable, draw from `GOALS.md`, `📦 Products/<slug>/`, and `🏢 Company/` — do not invent product or company names.

**ICP / personas / competitors:** Load from the relevant product `context.md`, `ICP.md`, or `🏢 Company/competitive/` files. If missing, ask once before drafting.

**Available Frameworks:**
- **Executives**: BLUF, Minto Pyramid (SCQA), MECE
- **Engineers/ICs**: Problem → Solution → Outcome, Jobs to Be Done
- **Customers**: Before/After/Bridge, PAS, StoryBrand
- **Stakeholders**: Narrative structure, Data + story

---

## Anti-Patterns to Avoid

**"Great meeting, let's follow up!"** — Fix: Lead with the decision or ask, always.

**Burying the BLUF** — Fix: If writing to an exec, the most important sentence is sentence 1, not sentence 5.

**Vague asks** — "Let me know your thoughts." Fix: "I need a yes/no on Option A by Friday."

**Generic opener to exec** — "I hope this finds you well." Fix: Skip pleasantries; they're busy.

**Over-contexting before the point** — Three paragraphs of background before the actual ask. Fix: Ask first, context second for exec communications.

---

**What do you need to write?**
