---
description: Run the design brief workflow
---
# Design Brief Generator

Generate a designer-ready design brief from an approved PRD.

---

## Relationship

- **`/design-brief`** scaffolds the 7-section design brief from an approved PRD
- **`prd-shaper`** (`~/.claude/skills/prd-shaper/`) provides the quality gate — only generate from PRDs with ≥5 decisions/page, specific thresholds, explicit non-goals
- **`design-brief-template.md`** (`📝 Docs/templates/`) provides the structural scaffold (7 sections)
- **`/story`** is the downstream handoff for AgilePlace backlog creation
- Use `/design-brief` after `/spec` when engaging a designer; use `/story` when going straight to AgilePlace

---

## Core Philosophy

**Design briefs are about focus, not completeness.**

- Scaffold from approved PRDs, don't start from scratch
- Carry forward key decisions, don't reinvent them
- Surface what's unknown, don't hide it
- Respect the designer's domain — PM owns the problem, designer owns the solution
- The fatal flaw: Design briefs that specify features without design constraints

---

## Command Syntax

```bash
/design-brief [--prd <path>] [--skip-discovery] [--save] [<feature-description>]
```

**Arguments**:
- `--prd <path>`: Path to the PRD file (required)
- `--skip-discovery`: Skip clarifying questions, generate immediately
- `--save`: Save completed design brief to the PRD directory
- `<feature-description>`: Initial description (optional—can provide interactively)

**Examples**:
```bash
/design-brief --prd "📦 Products/AgilePlace/initiatives/bulk-card-move/bulk-card-move-prd.md"
/design-brief --prd path/to/prd.md --save
/design-brief --prd path/to/prd.md --skip-discovery --save
```

---

## Template Reference

This command scaffolds from **`design-brief-template.md`** at `📝 Docs/templates/design-brief-template.md`.

The 7 sections are:
1. **Header metadata** — PM, Designer, PRD link, Due date
2. **The Problem** — Who, quote, evidence, current experience
3. **The Solution** — What we're building, requirements checklist, out of scope
4. **Design Direction** — Patterns to follow/avoid, technical constraints
5. **Deliverables** — Screen checklist, user flows, dates
6. **Before Starting Design** — Validation checklist, PM-owned vs designer-owned
7. **Success Criteria** — Usability bar, standard checklist

---

## Quality Gate

**Design briefs scaffold from approved PRDs.**

Before generating, check the PRD status:
- If status is **"Approved"** → Proceed
- If status is **"Draft"** or missing → Ask: "Design briefs should come from approved PRDs. Is this approved, or should we run `/spec --review [path]` first?"

Reference the **`prd-shaper`** quality standards (`~/.claude/skills/prd-shaper/SKILL.md`):
- ≥5 decisions per page
- Every metric has a specific threshold
- Non-goals are explicit with rationale

If PRD has <3 validated evidence points, add quality warning: "Customer evidence is [Medium/Low] confidence — confirm with 2+ interviews before designing."

---

## Your Approach

### Step 0: Parse Arguments

Extract from the command invocation:
- `--prd` value (required)
- `--skip-discovery` flag presence
- `--save` flag presence
- `<feature-description>` if provided

### Step 1: Load PRD and Template

1. Read the PRD at the provided `--prd` path
2. Check PRD status field (if present)
3. If status is "Draft" or missing, ask: "Design briefs should come from approved PRDs. Is this approved, or should we run `/spec --review [path]` first?"
4. Load the design brief template from `📝 Docs/templates/design-brief-template.md`

### Step 2: Clarifying Questions (max 2, skip with --skip-discovery)

Ask at most **1-2** questions:
1. "Who is the designer? (name or handle — used in header metadata)"
2. "When is the design review date? (used for Due field and Deliverables dates)"

If both are provided in the PRD or previous conversation, skip questions.

### Step 3: Generate Design Brief

Map PRD sections to design brief sections:

**Header Metadata:**
- PM: Author from PRD
- Designer: Answer from Step 2 or `TBD`
- PRD: Relative path link to source PRD
- Due: Design review date from Step 2 or `[NEEDS INPUT]`

**The Problem:**
- Who: Extract from PRD "Who is affected" or "Target Personas" section
- Quote: Lift verbatim from Customer Insights section. If absent: `[NEEDS INPUT — add real customer quote]`
- Evidence: Extract quantitative data points from Customer Insights section
- Current experience: `[NEEDS INPUT — add screenshot or Loom link]`

**The Solution:**
- What we're building: 1-2 sentences from PRD "Proposed Solution" section
- Requirements: Convert PRD "Key capabilities" to `- [ ]` checklist items
- Out of scope: Convert PRD "Non-goals" to `❌ [item] — [why]` format

**Design Direction:**
- Patterns to follow: `✅ [NEEDS INPUT — designer to fill]` placeholder bullets (respect designer's domain)
- Patterns to avoid: `❌ [NEEDS INPUT]` placeholder bullets
- Technical constraints: Extract from PRD "Dependencies & Risks" or "Technical Considerations" section

**Deliverables:**
- Screen checklist: Derive from PRD Key Use Cases (one screen per major workflow step per use case)
- User flows: One per use case
- Dates: From Step 2 or `[NEEDS INPUT]`

**Before Starting Design:**
- Validation items: Pull from PRD "Open Questions" table
- Label each: PM-owned (decisions, data) vs designer-owned (patterns, interactions)
- Quality flag: If PRD has <3 validated evidence points, add "⚠️ Validate: Customer evidence is [Medium/Low] confidence — confirm with 2+ interviews before designing."

**Success Criteria:**
- Usability bar: Derive from PRD primary success metric
- Standard checklist: Stakeholder sign-off, A11y (WCAG 2.1 AA), responsive behavior confirmed

### Step 4: Save (if --save)

If `--save` flag:
1. Generate filename: `design-brief-{feature-slug}.md` in same directory as PRD
2. Write the design brief to file
3. Confirm: "Design brief saved to: `{path}`"

### Step 5: Output Rich Contextual Handoff

After generating the design brief, output:

```markdown
---
## Design Brief Complete

**What we produced:**
- Brief: `{saved-path}` (7 sections)
- Screen inventory: {list screens identified from use cases, e.g., "Dependency map view, Card detail panel, Filter sidebar"}
- PM-owned gaps: Customer quote, screenshot of current state, design review date
- Designer-owned gaps: Patterns to follow/avoid (Design Direction section)

**Context to carry forward:**
- Feature: {feature name from PRD}
- Primary persona: {persona from PRD Problem Statement}
- Key capability: {top capability from Proposed Solution}
- Success metric: {primary metric and threshold from PRD}

**[NEEDS INPUT] count:** {N} items — resolve before sharing with designer

**Next — run this:**
```
/story --prd {prd-path} --dry-run
```
Preview the AgilePlace story hierarchy before pushing to the board.

---
```

---

## Key Constraints

**Never invent customer quotes** — Always mark `[NEEDS INPUT — add real customer quote]`

**Never fill in Design Direction** — That's the designer's domain; use placeholder bullets only

**Only generate from approved PRDs** — Surface prd-shaper quality warning if PRD is weak

**Always link back to source PRD** — Header must include relative path to PRD

**Respect the designer's ownership** — PM owns the problem and requirements; designer owns the patterns and interactions

---

## Pattern References

- Template: `📝 Docs/templates/design-brief-template.md`
- Quality gate: `~/.claude/skills/prd-shaper/SKILL.md`
- Real examples:
  - `📦 Products/AgilePlace/initiatives/bulk-card-move/design-brief-bulk-card-move.md`
  - `📦 Products/DPD/initiatives/ensemble-custom-views/design-brief-ensemble-custom-views.md`

---

## Anti-Patterns to Avoid

**Inventing Quotes** — Making up customer quotes instead of marking `[NEEDS INPUT]`. Fix: always mark gaps explicitly.

**Filling Design Direction** — Specifying patterns to follow/avoid as the PM. Fix: placeholder bullets only — designer fills these in.

**Skipping Quality Gate** — Generating from weak PRDs without warning. Fix: always check prd-shaper quality standards and surface warnings.

**Complete Requirements** — Design briefs with every requirement specified. Fix: scaffold key requirements, mark what's unknown — designer fills gaps.

**No PRD Link** — Design brief without connection to source PRD. Fix: always include relative path link in header.
