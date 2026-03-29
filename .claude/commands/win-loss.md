# Win/Loss Analysis

**Usage:** `/win-loss [--outcome <win|loss|no-decision>] [--competitor <name>] [<deal-context>]`

A structured interview and signal extraction workflow for B2B deal analysis. Turns individual deal outcomes into durable product intelligence.

---

## Relationship

- `/win-loss` feeds signal data into `📚 Knowledge/Research/signals-YYYY-MM.md` via `/signal --source sales`
- Battlecard update triggers route to `/compete --output battlecard`
- Pattern alerts (3+ losses to same competitor in 90 days) escalate to `/compete --focus [competitor]`
- `/prep` champion briefing mode uses win/loss learnings to update champion equipping strategies

---

## Core Philosophy

**Win/loss analysis is the richest product signal in B2B — and the most underutilized.**

Most win/loss processes capture the stated reason (price, features, relationship) and miss the real reason (buying committee dysfunction, wrong champion, integration requirement we don't meet). This command is designed to go deeper — extract root cause, not just surface label.

**Rule:** Stated reason ≠ real reason. Always look for both.

---

## Command Syntax

```bash
/win-loss [--outcome <win|loss|no-decision>] [--competitor <name>] [<deal-context>]
```

**Arguments:**
- `--outcome`: `win` | `loss` | `no-decision` (status quo, deferred, or budget freeze)
- `--competitor`: Named competitor evaluated in this deal (optional — enter if known)
- `<deal-context>`: Deal name, account, vertical, deal size, or any known context

**Examples:**
```bash
/win-loss --outcome loss --competitor "Jira Align" "NatWest Q1, $400K ARR"
/win-loss --outcome win "PNC Insurance, dependency view was the wedge"
/win-loss --outcome no-decision "Highmark — budget freeze, decision pushed to H2"
```

---

## Step 1: Structured 8-Question Interview

Work through these questions — they're sequenced to move from surface to root cause.

**Q1. What reason did the prospect (or champion) give for their decision?**
[Capture verbatim if possible — this is the stated reason]

**Q2. What do you think the real reason was?**
[Your read on the underlying cause — buying committee dynamics, product gap, competitive claim that landed, etc.]

**Q3. Who was the actual decision maker? Did we have access to them?**
[Economic buyer / champion / IT / exec sponsor — and whether we were in front of the right person]

**Q4. What capabilities came up during the evaluation?**
[Which product areas were evaluated, demoed, or asked about in depth]

**Q5. What claims did the competitor make that resonated with the buyer?**
[Specific claims, not general "they said they were better" — what *specifically* did they say?]

**Q6. What would have changed the outcome?**
[Be specific: "If we had X feature" / "If we had executive access earlier" / "If pricing was different"]

**Q7. What did we do well? Where did we create real value in the evaluation?**
[Not for morale — this is signal for what's working and should be repeated]

**Q8. One sentence: what's the single learning from this deal?**
[Distill the insight — this is what gets written into the record]

---

## Step 2: Signal Extraction

After the interview, extract 2–5 signals and offer to append them to `📚 Knowledge/Research/signals-[YYYY-MM].md`.

**Signal extraction rules:**
- Each signal = one discrete, quotable observation (not a summary)
- Route as `--source sales` with ICP-fit: High (if deal matched ICP) or Medium/Low
- Pain signals → tag with the relevant product area (dependency management, capacity planning, etc.)
- Competitive signals → tag with competitor name for `/synthesize` pattern detection

**Offer to batch-append:**
> "I've extracted [N] signals from this deal. Append to signals-[month].md? (y/n)"

---

## Step 3: Battlecard Implication Check

After signal extraction, check if this deal has competitive implications.

**Check:** Does `📚 Knowledge/Market/battlecard-[competitor-slug].md` exist?

- **If yes:** Flag specific sections that need updating based on what surfaced in Q4–Q5
  - "The [Capability] row in 'The Real Difference' table may need updating based on their [specific claim]"
  - "Consider adding '[Question text]' to Discovery Questions that Expose Their Gaps"

- **If no:** Note: "No battlecard exists for [Competitor]. If this is the 2nd+ loss to them, consider running `/compete --output battlecard [competitor]`"

- **3+ losses trigger:** If 3 or more losses to the same competitor are detected in `signals-[YYYY-MM].md`, output: "⚠️ Pattern alert: 3+ losses to [Competitor] detected in 90 days. Consider running `/compete --focus [competitor]` for a full competitive update."

---

## Step 4: Win/Loss Record

Output a compact, structured record for reference and pattern detection:

```
### Win/Loss Record — [Account] | [Date]

**Outcome:** [Win / Loss / No-Decision]
**Competitor:** [Name or "None identified"]
**Deal context:** [Vertical, size, key personas]

**Stated reason:** [What they said]
**Real reason (hypothesis):** [Your read]

**Buying committee:** [Who was in the deal, who we had / didn't have access to]
**Product gap identified:** [Specific capability or limitation, if any]
**Positioning / process gap:** [What we said or didn't say, process mistake, if any]

**Signals extracted:** [N signals → signals-YYYY-MM.md]
**Battlecard update needed:** [Yes — [competitor]/[section] | No]

**One-line learning:**
[The sentence worth keeping — specific enough to change future behavior]
```

---

## Step 5: Pattern Check

After writing the record, scan the current month's signals file for patterns:

- 3+ losses to same competitor in 90 days → recommend `/compete --focus [competitor]`
- Same product gap surfaced 3+ times → recommend `/signal --synthesize` and flag for roadmap
- Same buying committee role missing 3+ times → recommend `/prep` champion briefing update for that role

---

## Anti-Patterns

- **Don't stop at the stated reason** — "lost on price" almost always has a product or relationship root cause
- **Don't skip wins** — win/loss analysis of losses only misses what's working and worth doubling down on
- **Don't capture at a summary level** — "customer liked competitor better" is not a signal. "Competitor claimed real-time sync across 10K+ cards with no degradation — buyer tested it in trial" is a signal
- **Don't let signals expire** — if you don't append within the week, the context is gone
- **Don't treat no-decisions as neutral** — they often reveal the most about product-market fit gaps or ICP targeting mistakes

---

## Integration with Other Commands

- `/signal --source sales` — for individual signal capture outside a win/loss interview
- `/compete` — for battlecard generation and competitive positioning
- `/prep` — use win/loss learnings to update champion equipping strategies
- `/synthesize` — for cross-deal pattern detection once signals accumulate
