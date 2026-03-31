---
description: Run the roadmap workflow
---
# Roadmap Generator

Create a quarterly roadmap document with themes, now/next/later sequencing, and explicit exclusions.

---

## Relationship

- **`/roadmap`** creates the primary strategic artifact from which initiatives are prioritized
- **`/think`** should run first for strategic framing
- **`/prioritize`** feeds into roadmap sequencing decisions
- **`/align`** is the downstream handoff for stakeholder socialization
- **`/narrative`** is the alternative handoff for building the strategic story first
- Use `/roadmap` after `/think` and `/prioritize` when you're ready to commit to a quarterly plan

---

## Core Philosophy

**Roadmaps are about bets, not backlogs.**

- Strategic themes before initiative lists
- Confidence levels differentiate commitment from exploration
- Explicit exclusions prevent scope creep
- Key bets have measurable outcomes
- The fatal flaw: Roadmaps that say "we'll do all of these" without differentiation

---

## Command Syntax

```bash
/roadmap [--product <name>] [--quarter <Q>] [--format now-next-later|timeline|themes] [--save]
```

**Arguments**:
- `--product <name>`: Product name (required) — e.g., "AgilePlace", "Roadmaps", "DPD"
- `--quarter <Q>`: Quarter to plan (required) — e.g., "Q2", "Q3"
- `--format <format>`: Output format (default: `now-next-later`)
  - `now-next-later`: Three-column with confidence indicators
  - `timeline`: Month-by-month timeline view
  - `themes`: Organized by strategic theme
- `--save`: Save to `📦 Products/{product}/roadmap-{quarter}-{year}.md`
- `<description>`: Initial context (optional—can provide interactively)

**Examples**:
```bash
/roadmap --product AgilePlace --quarter Q2
/roadmap --product "DPD" --quarter Q3 --format themes --save
/roadmap --product OKRs --quarter Q2 --format now-next-later
```

---

## Your Approach

### Step 0: Parse Arguments

Extract from the command invocation:
- `--product` value (required)
- `--quarter` value (required)
- `--format` value (default: `now-next-later`)
- `--save` flag presence
- `<description>` if provided

If product or quarter missing, ask for them before proceeding.

### Step 1: Load Context

Read for strategic alignment:
- `GOALS.md` — Current objectives and company bets
- `📦 Products/{product}/` — Existing PRDs and initiatives
- `🤖 AI/memory/memory.md` — Current focus

Build initiative inventory from PRD directory structure.

### Step 2: Clarifying Questions (max 3)

Ask at most **3** questions:
1. "What are the 2-3 strategic themes this quarter?" (e.g., "AI-First Productivity", "Enterprise Readiness")
2. "What's the confidence level for each initiative — what could slip?" (Surface risks early)
3. "What is explicitly NOT on the roadmap this quarter and why?" (Force exclusion decisions)

If answers are clear from context, skip questions.

### Step 3: Generate 6-Section Roadmap

**Section 1: Strategic Themes** (2-3)
For each theme:
- Theme name
- One-sentence bet: "If we [deliver X], then [outcome]"
- Example: "**AI-First Productivity**: If we ship AI-assisted workflow suggestions, then power users adopt at 2x rate"

**Section 2: Now / Next / Later Table**

| Initiative | Theme | Confidence | Target |
|------------|-------|------------|--------|
| [Name] | [Theme] | 🟢 committed / 🟡 likely / 🔴 exploratory | [Date] |

Rules:
- **🟢 committed**: Resourced, no blockers expected
- **🟡 likely**: Resourced, some dependency risk
- **🔴 exploratory**: Unresourced or high uncertainty — may slip

**Section 3: Key Bets** (per theme)
Format: "If we [deliver X], then [outcome], measured by [metric with threshold]"

Example:
```
**AI-First Productivity bets:**
- If we ship AI-assisted workflow suggestions, then power user adoption increases 25%, measured by weekly active usage of AI features from 8% → 10%
- If we integrate with Claude Code, then developer NPS improves, measured by developer segment NPS from 42 → 48+
```

**Section 4: What We're NOT Doing** (MANDATORY)
Format: Initiative + explicit rationale

Example:
```
- ❌ **Mobile app redesign** — Requires 3+ engineers for 6+ weeks; desktop usage is 94% of sessions; mobile not in top 3 customer requests
- ❌ **Custom reporting API** — Depends on new data layer architecture; deferred to Q3 pending foundation work
```

**Section 5: Open Questions**
Table: Question | Owner | Target Date

**Section 6: Success Criteria**
- Leading indicators (what we'll see in 4-6 weeks)
- Lagging metrics with targets

### Step 4: Save (if --save)

If `--save`:
1. Generate filename: `roadmap-{quarter}-{year}.md`
2. Save to `📦 Products/{product}/roadmap-{quarter}-{year}.md`
3. Confirm: "Roadmap saved to: `{path}`"

### Step 5: Output Rich Contextual Handoff

```markdown
---
## Roadmap Complete

**What we produced:**
- Roadmap: `{saved-path or "displayed above"}` ({quarter} {year}, {N} initiatives)
- Themes: {list theme names, e.g., "AI-First Productivity, Enterprise Readiness"}
- Confidence: {N} 🟢 committed / {N} 🟡 likely / {N} 🔴 exploratory
- Explicit exclusions: {N} documented

**Context to carry forward:**
- Product: {product name}
- Quarter: {quarter} {year}
- Top committed initiative: "{initiative with highest confidence}"
- Biggest risk: "{initiative with lowest confidence or most dependencies}"

**[NEEDS INPUT] count:** {N} — questions in Open Questions section require owners

**Next — socialize or build:**
```
/align --context "{quarter} {product} roadmap" --stakeholders "[names]"
```
Or `/narrative` to build the strategic story before stakeholder review.

---
```

---

## Key Constraints

- **No roadmap without explicit strategic themes** — Theme-first, not initiative-first
- **Differentiate confidence levels** — Don't mark everything 🟢; force honesty about risk
- **"What We're NOT Doing" is MANDATORY** — Every roadmap must have explicit exclusions
- **Every Key Bet has a measurable outcome** — No bet without a metric and threshold
- **Roadmap contains initiatives, not user stories** — Stories belong in `/story` output

---

## Anti-Patterns to Avoid

**Theme-Free Roadmap** — Just a list of initiatives. Fix: start with 2-3 strategic themes.

**All-Green Confidence** — Everything marked 🟢. Fix: differentiate honestly; at least 1-2 🟡 or 🔴.

**Missing Exclusions** — No "What We're NOT Doing" section. Fix: force explicit exclusions with rationale.

**Vague Bets** — "If we ship X, then users will be happier." Fix: specific metric with threshold.

**Story-Level Roadmap** — Individual stories instead of initiatives. Fix: aggregate into initiatives.

---

## Pattern References

- GOALS.md for strategic context
- `📦 Products/{product}/` for existing initiatives and PRDs
- `/think` for strategic framing before roadmap
- `/prioritize` for sequencing decisions
