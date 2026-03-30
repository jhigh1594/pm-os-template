# Customer Signal Capture

Capture a customer signal at the moment it occurs — from any source — as a structured atomic nugget. Prevents evidence from evaporating between customer touchpoints and monthly synthesis sessions.

---

## Relationship

- **`/signal`** is the top-of-funnel capture step, upstream of everything
- **`/synthesize`** consumes the `signals-YYYY-MM.md` file as its organized input — run monthly
- **`/discover`** names the relevant initiative when a signal validates or contradicts open work
- **`/granola`** is for post-meeting extraction (full meeting → markdown files); `/signal` is for point-of-occurrence capture (one signal → one nugget)
- Not a replacement for synthesis — a feeder to it

---

## Core Philosophy

**Capture first, classify second.**

A weak signal captured is better than a strong signal lost. The goal is zero-friction capture at the moment of occurrence. Don't let perfect formatting block you from writing it down.

The fatal flaw: waiting until the end of the week to write up signals. By then, the exact words are gone and the context is hazy.

---

## Command Syntax

```bash
/signal [--source <type>] [--product <name>] [<raw-signal>]
```

**Arguments**:
- `--source`: Where the signal came from — see full source type list below
- `--product`: Product area tag (`agileplace | okrs | roadmaps | dpd | platform`) — optional
- `<raw-signal>`: The raw signal text — paste verbatim, can be rough or unpolished

**Source types:**

| Source | Description | Default ICP Fit | Default Strength Modifier |
|--------|-------------|-----------------|--------------------------|
| `interview` | Structured customer discovery call | High | Standard |
| `support` | Support ticket or escalation | Medium | Standard |
| `slack` | Internal Slack thread with customer/stakeholder signal | Medium | Standard |
| `call` | Unstructured sales or CS call | High | Standard |
| `email` | Email thread with customer or prospect | Medium | Standard |
| `other` | Any unlisted source | Medium | Low |
| `sales` | From a deal conversation (prospect or customer in evaluation) | High | Standard; flag for `/win-loss` routing if competitive signal |
| `renewal` | From a CS renewal review (existing customer, renewal context) | High | Elevated urgency; default signal type: pain or competitive |
| `cs-escalation` | From an at-risk account escalation | High | High strength by default; near-term routing required |
| `expansion` | From an upsell or expansion conversation | High | Route to value-chain gaps; default type: request or behavior |
| `analyst` | From an analyst report, briefing, or analyst firm publication (Gartner, Forrester, IDC, etc.) | Medium | Standard; flag for `/persona-sync` and `/synthesize` to fold into persona validation — analyst signals represent market-level evidence, not single-customer evidence |
| `market` | From a market-wide signal — earnings calls, industry conference announcements, adjacent market moves, job posting patterns as demand signals | Low | Low by default; elevate to Medium if it directly contradicts an existing Planview strategic assumption or ICP definition |

**B2B revenue-source routing rules:**
- `--source sales` → Flag as deal signal; offer to also run `/win-loss` if competitive signals surface
- `--source renewal` → Add note: "⚠️ Renewal-context signal — elevated urgency; review against active renewal accounts"
- `--source cs-escalation` → Override strength to High; add: "⚠️ At-risk account signal — near-term routing to relevant initiative"
- `--source expansion` → Note expansion opportunity; route to value-chain gaps in product area
- `--source analyst` → Flag with: "Analyst signal — cross-reference with `📦 Products/[product]/product-context/`. Does this confirm or challenge the ICP definition? Consider routing to `/persona-sync` if it directly affects a persona attribute."
- `--source market` → Flag with: "Market signal — low direct ICP fit but may shift strategic context. Elevate to Medium strength if it contradicts an existing strategic assumption. Consider routing to `/think` if it challenges a foundational strategic bet."

**Examples**:
```bash
/signal --source call --product agileplace "Customer said they're manually copying card status into a spreadsheet every Friday because they can't get the view they need"
/signal --source support "Ticket from PNC — third one this month about bulk card operations"
/signal --source slack "Marcus flagged that NatWest asked about dependency visualization in last week's call"
/signal --source sales "NatWest AE said Jira Align claimed real-time sync across 10K+ cards — buyer tested it in trial"
/signal --source renewal "Highmark renewal call — champion said their exec is asking why we can't do portfolio-level reporting"
/signal --source cs-escalation "PNC RTE team not using dependency views — adoption stalled after onboarding"
/signal --source expansion "NatWest wants to expand to 3 more teams but IT is asking about SSO support"
/signal "Heard in demo: prospect said 'this looks like what we built in Jira but couldn't maintain'"
```

---

## Your Approach

### Step 0: Parse Arguments

Extract from the command invocation:
- `--source` value (optional — ask if missing and signal is ambiguous)
- `--product` value (optional — infer from signal content if obvious)
- `<raw-signal>` text

**If no raw signal provided**: Ask one question — "What did you hear and where did it come from? (paste rough is fine)"

**If source is missing but signal is clear**: Infer source from context and note it as `[inferred]`. Don't block on it.

### Step 1: Classify into Atomic Nugget

Apply the atomic nugget structure from the `/synthesize` framework. One observation per nugget — do not bundle multiple signals into one nugget.

Format the nugget:

```
---
**Signal captured:** [today's date]
**Source:** [source type] | [inferred]
**Customer/Context:** [company or role if known — "unknown" if not]
**Product area:** [product tag]

**Signal:** "[verbatim or close paraphrase — preserve exact words when possible]"

**Signal type:** [pain | praise | request | behavior | competitive]
**ICP fit:** [High = known ICP customer or target segment / Medium = unclear fit / Low = edge case or out-of-ICP]
**Strength:** [High / Medium / Low]

Strength guide:
- High: Specific, ICP-fit customer, unprompted, describes real behavior
- Medium: Vague or prompted, medium ICP fit, or secondhand
- Low: Hypothetical ("would be nice if..."), out-of-ICP, or very generic
---
```

### Step 2: Route the Signal

Determine where this signal belongs in the current product landscape:

**Check open initiatives** — Scan `📦 Products/` directory structure mentally (AgilePlace, OKRs, Roadmaps, DPD) for any initiative this signal validates, contradicts, or is adjacent to.

Output one of:
- **Validates**: "This signal supports [initiative name] — confirms [specific assumption]"
- **Contradicts**: "This signal pushes back on [initiative name] — challenges [specific assumption]"
- **Adjacent**: "This signal is adjacent to [initiative] but not directly in scope — may be worth flagging"
- **New territory**: "This signal doesn't map to any open initiative — candidate for next `/synthesize` session"

**Monthly signals file**: Suggest appending to `📚 Knowledge/Research/signals-[YYYY-MM].md` (rolling monthly file — create if it doesn't exist for this month).

### Step 2.5: Persona Impact Check

After routing the signal (Step 2), check whether this signal directly informs a persona attribute in `📦 Products/[product]/product-context/`.

**If the signal validates, contradicts, or adds to a persona attribute**:
> "📝 Persona touchpoint: this signal is relevant to the **[persona name]** persona in `📦 Products/[product]/product-context/[file].md`. Consider adding to `/persona-sync` queue — run `/persona-sync --product [name]` after 3+ signals accumulate for this persona."

**If no matching persona exists for this segment**:
> "No persona defined for this segment — if this pattern repeats (3+ signals), it's a candidate for a new persona via the `b2b-icp-positioning-craft` skill."

**If source is `analyst` or `market`**: Cross-reference with existing ICP definitions — analyst and market signals represent market-level evidence. If the signal challenges a key ICP assumption, elevate the note: "⚠️ This analyst/market signal may affect ICP definition — flag for `/persona-sync`."

This step is **non-blocking** — it's a suggestion, not a required action. The signal is saved regardless.

---

### Step 3: Confirm and Append

Present the formatted nugget and routing assessment. Offer:

> "Append this to `Knowledge/Research/signals-[YYYY-MM].md`? (y to confirm, or paste edits first)"

If confirmed: Append the nugget to the file with a blank line separator. Confirm: "Signal saved to `{path}`."

If declined: Display the nugget for manual use. No further action.

**Always display the nugget** regardless of save decision — the PM may want to paste it elsewhere.

---

## Output Format

### Nugget Display
```
📌 Signal captured — [date]

Source: [type] | Customer: [company/role] | Product: [area]
Type: [pain/praise/request/behavior/competitive] | ICP fit: [H/M/L] | Strength: [H/M/L]

"[Signal verbatim]"

→ [Routing assessment: validates / contradicts / adjacent / new territory]
→ [Initiative name if applicable]
```

### File Entry (appended to signals-YYYY-MM.md)
```markdown
---
**Signal captured:** YYYY-MM-DD
**Source:** [type]
**Customer/Context:** [company or role]
**Product area:** [tag]

**Signal:** "[verbatim]"

**Signal type:** [type]
**ICP fit:** [H/M/L]
**Strength:** [H/M/L]
**Initiative:** [name or "unsorted"]
---
```

---

## Key Constraints

- **One signal per nugget** — Never bundle "they said X and Y and Z" into one entry. Run `/signal` three times.
- **Preserve exact words** — Paraphrase only when you must; mark paraphrases with `[paraphrased]`
- **Don't over-classify** — If ICP fit or strength is unclear, use Medium. Capture over precision.
- **No invented context** — If you don't know the company or role, write "unknown" — never guess
- **Rolling monthly file** — Each month gets its own signals file; `/synthesize` can consume one month at a time

---

## Anti-Patterns to Avoid

**Waiting to batch** — "I'll log these five signals at end of day." Fix: log each one immediately; memory degrades fast.

**Over-writing** — Spending 5 minutes formatting one signal. Fix: rough paste is valid input; Step 1 structures it.

**Bundling multiple signals** — "Customer complained about X, Y, and Z." Fix: three separate `/signal` calls — each gets its own nugget.

**Skipping weak signals** — "It was just one person saying maybe." Fix: log it with Low strength. Patterns emerge from weak signals too.

---

## Integration Points

**Entry from:**
- Customer call (during or immediately after)
- Support ticket review
- Slack thread where a customer or stakeholder said something meaningful
- Demo debrief
- Sales call notes
- `/granola` extraction (if a specific signal inside a meeting deserves its own nugget)

**Exit to:**
- `📚 Knowledge/Research/signals-YYYY-MM.md` (primary destination)
- `/synthesize` — consumes the signals file at synthesis time
- `/discover` — names the relevant initiative for validation/contradiction tracking

---

## Signals File Format Reference

`📚 Knowledge/Research/signals-YYYY-MM.md` structure:

```markdown
# Customer Signals — [Month YYYY]

Atomic signal nuggets captured throughout the month. Fed into /synthesize at month-end or when sufficient volume accumulates (typically 10+ signals).

---

[nugget 1]

---

[nugget 2]

---
```
