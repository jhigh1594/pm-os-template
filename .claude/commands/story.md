---
description: Run the story workflow
---
# Story Breakdown Generator

Generate an Epic → Feature → Story hierarchy from an approved PRD, optionally push to AgilePlace.

---

## Relationship

- **`/story`** generates AgilePlace backlog hierarchy from approved PRDs
- **`prd-shaper`** (`~/.claude/skills/prd-shaper/`) provides the quality gate — only generate from PRDs with Key Use Cases, Success Metrics, and explicit non-goals
- **`prd-template.md`** (`📝 Docs/templates/`) provides the section structure for parsing
- **`/design-brief`** is the sibling handoff for designer engagement
- **`/spec-brief`** is the downstream handoff for engineering
- Use `/story` after `/spec` to create AgilePlace backlog; use `/design-brief` when engaging a designer first

---

## Core Philosophy

**Stories are about execution, not documentation.**

- Parse approved PRDs structurally, don't free-form generate
- Map use cases to features, not stories to features
- Include acceptance criteria with every story,- Never invent personas not present in the PRD
- The fatal flaw: Stories without acceptance criteria (how do we know when it story is done?)

---

## Command Syntax

```bash
/story [--prd <path>] [--board <board_id>] [--dry-run] [--skip-discovery] [--save-only] [<description>]
```

**Arguments**:
- `--prd <path>`: Path to the PRD file (required)
- `--board <board_id>`: AgilePlace board ID to push to (optional — without this, saves locally only)
- `--dry-run`: Generate JSON files but don't push to AgilePlace
- `--skip-discovery`: Skip clarifying questions, generate immediately
- `--save-only`: Save JSON files but skip AgilePlace push (for manual review before pushing)
- `<description>`: Initial description (optional—can provide interactively)

**Examples**:
```bash
/story --prd "📦 Products/AgilePlace/initiatives/in-place-okr-linking/okr-agileplace-integration-prd.md"
/story --prd path/to/prd.md --board 12345
/story --prd path/to/prd.md --dry-run
/story --prd path/to/prd.md --board 12345 --skip-discovery
```

---

## Template Reference

This command parses PRDs using **`prd-template.md`** section structure at `📝 Docs/templates/prd-template.md`.

**Required sections** (all must be present):
- **Problem Statement** → Epic description
- **Key Use Cases / Workflows** → Features (one per use case)
- **Proposed Solution / Key capabilities** → Story scope
- **Success Metrics** → Acceptance criteria context

If any section is missing or contains `[NEEDS INPUT]`, warn before generating.

---

## Quality Gate

**Stories scaffold from approved PRDs with complete sections.**

Before generating:
1. Read the PRD at `--prd` path
2. Validate required sections exist and don't contain `[NEEDS INPUT]`
3. If validation fails: "This PRD is missing {section}. Stories generated without it will be weak. Add it to the PRD or run `/spec --review [path]` first."

Reference **`prd-shaper`** quality standards (`~/.claude/skills/prd-shaper/SKILL.md`):
- A PRD with vague use cases will produce weak features
- A PRD with missing personas will produce generic stories
- A PRD without success metrics will produce stories without measurable ACs

---

## Your Approach

### Step 0: Parse Arguments

Extract from the command invocation:
- `--prd` value (required)
- `--board` value (optional)
- `--dry-run` flag presence
- `--skip-discovery` flag presence
- `--save-only` flag presence
- `<description>` if provided

### Step 1: Load and Validate PRD

1. Read the PRD at the provided `--prd` path
2. Parse using `prd-template.md` section structure:
   - Look for `## Problem Statement` section
   - Look for `## Key Use Cases` or `## Workflows` section
   - Look for `## Proposed Solution` or `## Key Capabilities` section
   - Look for `## Success Metrics` section
3. Validate each section exists and doesn't contain `[NEEDS INPUT]`
4. If validation fails: "This PRD is missing {section}. Stories generated without it will be weak. Add it to the PRD or run `/spec --review [path]` first."

### Step 2: Clarifying Questions (max 2-2, skip with --skip-discovery)

Ask at most **1-2** questions:
1. "What's the primary persona for these stories? (from PRD or specify)"
2. "What's the smallest shippable slice for V1? (to scope the story count)"

If answers are clear from PRD, skip questions.

### Step 3: Generate Hierarchy

**Epic** (1 per PRD):
- `title`: PRD feature/initiative name
- `description`: TL;DR compressed to 3-5 decision-dense bullets (outcome-focused, not capability-focused)
- `cardTypeId`: Use default epic type for the board

**Features** (3-7, max 7 per epic):
- One per Key Use Case from PRD
- `title`: Noun phrase from use case name
- `description`: Include "Feature goal" from use case's "Success looks like" field
- `stories`: Array of 3-6 stories per feature

**Stories** (3-6 per feature):
- Format: `As a [persona], I want [goal], so that [value outcome]`
- Each story has 3-5 Gherkin-lite acceptance criteria:
  ```
  - [ ] Given [context]
  - [ ] When [action]
  - [ ] Then [outcome]
  ```

**Example Story**:
```
As a Portfolio Manager, I want to see which OKRs are impacted by blocked cards,
So that I can proactively communicate risks to leadership before they become critical.

ACs:
- [ ] Given I'm viewing a custom view grouped by OKR
- [ ] When a card becomes blocked
- [ ] Then the OKR group shows a risk indicator with the blocked card highlighted
- [ ] When I click on the OKR group
- [ ] Then I see the blocked card details in context
```

### Step 4: Display Tree View

Show hierarchy as:
```
Epic: [Title]
├── Feature: [Title] (N stories)
│   ├── Story: [Title]
│   ├── Story: [Title]
│   └── Story: [Title]
├── Feature: [Title] (N stories)
│   └── ...
```

### Step 5: Write Files

Write to the same directory as the PRD:
- `epic.json` — Epic definition for AgilePlace CLI
- `features.json` — Features array with embedded stories
- `story-breakdown.md` — Human-readable hierarchy with full story text and ACs

### Step 6: Push to AgilePlace (if --board and not --dry-run/--save-only)

If `--board` is provided and neither `--dry-run` nor `--save-only`:

```bash
cd "/Users/jhigh/Planview Work/🔧 Automation/scripts" && \
python -m agileplace_cli hierarchy create-epic <board_id> \
  --epic @<prd-dir>/epic.json \
  --features @<prd-dir>/features.json
```

### Step 7: Output Rich Contextual Handoff

After generating the hierarchy, output:

```markdown
---
## Story Breakdown Complete

**What we produced:**
- Epic: "{epic title}" ({N} features, {total} stories, {total} acceptance criteria)
- Files: `epic.json`, `features.json`, `story-breakdown.md` → {prd-directory}
- AgilePlace: {Pushed to board {board_id} / Saved locally — use --board to push}

**Context to carry forward:**
- Feature: {feature name}
- Primary persona: {persona used across stories}
- Smallest slice identified: "{feature name}" ({N} stories)
- Stories with complete ACs: {N}/{total}

**[NEEDS INPUT] count:** {N} stories missing 3+ ACs (flagged in story-breakdown.md)

**Next — run this:**
```
/spec-brief {prd-path}
```
Generate the Gherkin acceptance criteria and engineering handoff doc.

---
```

---

## JSON Format Reference

**epic.json**:
```json
{
  "title": "Epic Title",
  "description": "Epic description as HTML or plain text",
  "cardTypeId": "optional-card-type-id"
}
```

**features.json**:
```json
[
  {
    "title": "Feature Title",
    "description": "Feature description",
    "stories": [
      {
        "title": "As a [persona], I want [goal], so that [outcome]",
        "description": "Story details and context"
      }
    ]
  }
]
```

---

## Key Constraints

- **Max 7 features per epic** — Cognitive limit for sprint planning and AgilePlace board readability
- **No sub-tasks** — Epic → Feature → Story only (3-level hierarchy)
- **Never invent personas** — Use only personas present in the PRD Problem Statement
- **Every story needs 3+ ACs** — Stories with fewer are flagged as incomplete
- **Respect non-goals** — Never generate stories for items in PRD "Explicitly out of scope" section

---

## Anti-Patterns to Avoid

**Generic Stories** — "As a user, I want to see data, so that I can make decisions." Fix: specific persona, concrete goal, measurable outcome.

**Feature Bloat** — 10+ features per epic. Fix: consolidate into 3-7 features max.

**Missing Acceptance Criteria** — Stories without ACs. Fix: every story has 3-5 Given/When/Then items.

**Invented Personas** — Personas not in the PRD. Fix: use only validated personas from Problem Statement.

**Non-goal Stories** — Stories for items in "Explicitly out of scope". Fix: check non-goals section before generating.

---

## Pattern References

- PRD template: `📝 Docs/templates/prd-template.md`
- AgilePlace CLI: `🔧 Automation/scripts/agileplace_cli/commands/hierarchy.py`
- Quality gate: `~/.claude/skills/prd-shaper/SKILL.md`
