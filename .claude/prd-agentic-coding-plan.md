# PRD Agentic Coding Enhancement Plan

**Status:** Draft
**Created:** February 11, 2026
**Priority:** P0 (High-leverage 10X impact)

---

## Overview

This plan implements two high-leverage changes to make PRD artifacts ready for agentic coding workflows (Claude Code, GitHub Copilot, hybrid agent workflows).

### Changes

1. **Gherkin Format for Acceptance Criteria** - Refactor acceptance criteria sections in PRD templates to use Given-When-Then format
2. **Spec Brief Handoff Artifact** - Create a new command that generates a concise, agent-ready specification from approved PRDs

---

## What is Gherkin Format?

Gherkin is a structured language for describing test scenarios using **Given-When-Then** format:

```gherkin
SCENARIO: [Brief description]

GIVEN [a context or precondition]
  AND [additional context if needed]
WHEN [the action occurs]
THEN [the expected outcome]
  AND [additional outcomes if needed]
```

### Example

**Traditional:** "Users can filter cards by priority"

**Gherkin:**
```gherkin
SCENARIO: Filter cards by priority

GIVEN a Board Admin is viewing the card list
  AND the board contains 50 cards with various priorities
WHEN they select "High Priority" from the filter dropdown
THEN only cards marked as High Priority are displayed
  AND the count shows "15 cards"
  AND other filters remain available
```

### Benefits

| Benefit | Why It Matters |
|---------|----------------|
| Unambiguous | Clear preconditions, actions, outcomes |
| Executable | Directly maps to automated tests |
| Agent-friendly | Structured format LLMs parse reliably |
| Edge case coverage | GIVEN clause makes context explicit |

---

## Implementation Plan

### Phase 1: Create Spec Brief Command with Gherkin Format

**Note:** The main PRD template (`Docs/templates/prd-template.md`) remains business-focused without Gherkin format. Gherkin acceptance criteria are only generated in the Spec Brief handoff artifact.

**Files to modify:**
- `.cursor/commands/ai-prd.md` (remove Gherkin instructions, keep simple acceptance criteria)
- `.cursor/commands/prd-one-pager.md` (remove Gherkin instructions)

**New file to create:**
- `.claude/commands/spec-brief.md`
- `.cursor/commands/spec-brief.md`

**Changes for `.cursor/commands/ai-prd.md`:**

1. In `ai-prd.md`, revert the Acceptance Criteria section to simple format:

```markdown
## Acceptance Criteria

**[AI Context: Define measurable success conditions. Each criterion should be independently verifiable. The Spec Brief will convert these to Gherkin format during handoff.]**

**Format:**
```
SCENARIO: [Brief description]
GIVEN [context/preconditions]
  AND [additional context]
WHEN [action occurs]
THEN [expected outcome]
  AND [additional outcomes]
```

**Primary Scenarios:**

SCENARIO: [Scenario 1 name]
GIVEN [precondition]
WHEN [action]
THEN [observable outcome]

SCENARIO: [Scenario 2 name]
GIVEN [precondition]
WHEN [action]
THEN [observable outcome]

**Edge Cases to Cover:**
- [Edge case 1]: SCENARIO format
- [Edge case 2]: SCENARIO format

**Error Handling:**
SCENARIO: [Error scenario]
GIVEN [context where error occurs]
WHEN [trigger]
THEN [error handling behavior]
```

2. In `prd-one-pager.md`, replace the success metric section:

```markdown
## Hypothesis & Success Metric

**[AI Context: The bet we're making and how we'll know if we were right. Use Gherkin format for acceptance criteria.]**

**If we** [build X], **then** [users will] [change behavior], **resulting in** [outcome].

**Primary metric:** [Metric]: [Current] → [Target] by [Date]

**Leading indicator:** [What we can measure in 2-4 weeks]

**Acceptance Criteria (Gherkin format):**

SCENARIO: [Primary success scenario]
GIVEN [context]
WHEN [action]
THEN [measurable outcome]

SCENARIO: [Secondary scenario]
GIVEN [context]
WHEN [action]
THEN [measurable outcome]
```

---

### Phase 2: Create Spec Brief Command

**New file:** `.cursor/commands/spec-brief.md`

**Purpose:** Generate a concise, agent-ready specification from an approved PRD

**Usage:** `/spec-brief [path-to-prd]`

**Output:** `Products/{product}/features/{feature}/SPEC_BRIEF.md`

---

## File: `.cursor/commands/spec-brief.md`

```markdown
---
description: Generate a concise Spec Brief from an approved PRD for agent handoff
---

## User Input

```text
$ARGUMENTS
```

You **MUST** consider the user input before proceeding (if not empty).

## Outline

1. **Parse input:**
   - If `$ARGUMENTS` is empty, ask: "Which PRD should I generate a Spec Brief from? Please provide the path."
   - Otherwise, use `$ARGUMENTS` as the PRD file path

2. **Read and analyze the PRD:**
   - Read the full PRD file
   - Extract key sections: Problem, Solution, Use Cases, Acceptance Criteria, Technical Notes, Dependencies

3. **Generate Spec Brief:**
   - Transform PRD content into Spec Brief format (see template below)
   - Convert acceptance criteria to Gherkin format if not already done
   - Extract and structure test scenarios
   - Identify dependencies and integration points

4. **Determine output location:**
   - From PRD path, derive feature directory
   - Output to: `{prd-directory}/SPEC_BRIEF.md`

5. **Write Spec Brief:**
   - Create/update SPEC_BRIEF.md with generated content

6. **Report completion:**
   - Confirm file created
   - Provide path to Spec Brief
   - Suggest next steps: "Share this with your engineering team or use it as input for AI coding assistants"

---

## Spec Brief Template

```markdown
# Spec Brief: [Feature Name]

> Generated from: [PRD file path]
> Generated: [Date]
> Author: [PRD Author]

---

## Context (TL;DR)

**Who:** [Primary user persona]

**What:** [One-sentence description of what we're building]

**Why:** [Business value/user outcome in 1-2 sentences]

**When:** [Target release/timeframe]

---

## Problem Statement

**Who is affected:** [Specific user persona or segment]

**The problem:** [What's broken, missing, or painful - 2-3 sentences]

**Impact:** [Quantified if possible: time lost, errors made, revenue at risk]

---

## Proposed Solution

**What we're building:** [High-level description - 2-3 sentences]

**Key capabilities:**
1. [Capability 1]
2. [Capability 2]
3. [Capability 3]

**Explicitly out of scope:**
- [Not building: X]
- [Deferred to future: Y]

---

## User Flow (Happy Path)

1. **[Step 1]** - [User action, expected outcome]
2. **[Step 2]** - [User action, expected outcome]
3. **[Step 3]** - [User action, expected outcome]
4. **[Step 4]** - [User action, expected outcome]

---

## Inputs

| Input | Format | Validation | Required | Source |
|-------|--------|------------|----------|--------|
| [name] | [type/schema] | [rules] | [yes/no] | [where from] |
| [name] | [type/schema] | [rules] | [yes/no] | [where from] |

---

## Outputs

| Output | Format | Destination | Trigger |
|--------|--------|-------------|---------|
| [name] | [type/schema] | [where goes] | [when created] |
| [name] | [type/schema] | [where goes] | [when created] |

---

## Core Rules (Business Logic)

**Rule 1: [Name]**
- IF: [condition]
- THEN: [action/result]
- ELSE: [fallback behavior]

**Rule 2: [Name]**
- IF: [condition]
- THEN: [action/result]

**Edge cases:**
- [Edge case 1]: [how to handle]
- [Edge case 2]: [how to handle]

---

## UI States

| State | Description | Entry Condition | Exit Condition |
|-------|-------------|-----------------|----------------|
| [state] | [what user sees] | [when shown] | [what advances] |
| [state] | [what user sees] | [when shown] | [what advances] |

---

## Data Model

**Entities:**

### [Entity 1]
```
[Entity Name]
├── [field_1]: [type] - [description]
├── [field_2]: [type] - [description]
└── [field_3]: [type] - [description]
```

**Relationships:**
- [Entity A] → [Entity B]: [relationship type]

---

## Acceptance Criteria (Gherkin Format)

### Primary Scenarios

SCENARIO: [Scenario name]
GIVEN [context/preconditions]
  AND [additional context]
WHEN [action occurs]
THEN [expected outcome]
  AND [additional outcomes]

SCENARIO: [Scenario name]
GIVEN [context/preconditions]
WHEN [action occurs]
THEN [expected outcome]

### Edge Cases

SCENARIO: [Edge case scenario]
GIVEN [context where edge case applies]
WHEN [action occurs]
THEN [expected handling]

### Error Cases

SCENARIO: [Error scenario]
GIVEN [context where error occurs]
WHEN [error trigger]
THEN [error handling and user communication]

---

## Test Scenarios

### Happy Path Tests
1. [Test case with steps]
2. [Test case with steps]

### Edge Case Tests
- [What happens when X is at boundary/missing/invalid?]
- [What happens at scale?]

### Integration Tests
- [Must work with: existing feature/system]
- [Must not break: existing feature/system]

---

## Dependencies

**Technical dependencies:**
- [Dependency]: [Owner/Status] - [What we need from them]

**Cross-team dependencies:**
- [Team]: [What we need] - [Status]

**External APIs/Services:**
- [Service]: [Integration notes]

---

## Technical Considerations

**Performance:**
- [Requirement: e.g., "Response time < 500ms for list load"]

**Security:**
- [Considerations: e.g., "PII must be encrypted at rest"]

**Accessibility:**
- [Requirements: e.g., "WCAG 2.1 AA compliance"]

**Error handling:**
- [Strategy: user-facing messages, logging, recovery]

---

## Success Metrics

**Primary metric:** [Metric]: [Current] → [Target] by [Date]

**Leading indicators:**
- [Metric]: [Target]
- [Metric]: [Target]

**Guardrail metrics (don't break):**
- [Metric]: Must not decrease below [threshold]

---

## Open Questions

| Question | Owner | Target Date | Status |
|----------|-------|-------------|--------|
| [Question] | [Name] | [Date] | Open/Resolved |

---

## Design Artifacts

- [ ] Mockups: [Link]
- [ ] Prototypes: [Link]
- [ ] User flows: [Link]

---

## Implementation Notes

**Suggested starting point:** [Component/endpoint to build first]

**Key files to modify:**
- [File path]: [What to add/change]
- [File path]: [What to add/change]

**Integration points:**
- Connects to: [existing system/component]
- Pattern to follow: [reference similar feature]

---

## Decision Log

| Date | Decision | Rationale | Decided By |
|------|----------|-----------|------------|
| | | |
```

---

## Testing Checklist

After generating Spec Brief, verify:

- [ ] Context section is clear and concise (≤5 sentences)
- [ ] All acceptance criteria use Gherkin format
- [ ] Input/Output tables include format and validation
- [ ] Test scenarios cover happy path, edge cases, errors
- [ ] Dependencies include ownership and status
- [ ] Success metrics are specific and measurable
- [ ] Implementation notes provide concrete starting point

---

## Usage Examples

**Example 1: Generate from PRD in current directory**
```
/spec-brief Products/AgilePlace/features/dependency-intelligence/prd.md
```
Output: `Products/AgilePlace/features/dependency-intelligence/SPEC_BRIEF.md`

**Example 2: Generate with explicit path**
```
/spec-brief /Users/jhigh/Planview\ Work/Products/OKRs/features/bulk-import/full-prd.md
```

**Example 3: Interactive mode (no argument)**
```
/spec-brief
```
Prompts: "Which PRD should I generate a Spec Brief from?"
```

---

## Success Criteria

1. **Completeness:** Spec Brief contains all sections from template
2. **Fidelity:** Key information from PRD is preserved
3. **Clarity:** Brief is concise (target: 2-3 pages max)
4. **Actionability:** Implementation notes provide clear starting point
5. **Testability:** All acceptance criteria use Gherkin format
```

---

## Implementation Steps

### Step 1: Update PRD Templates (30 minutes)

- [ ] Edit `.cursor/commands/ai-prd.md`
  - Locate "Acceptance Criteria" section in Feature template
  - Replace with Gherkin format instructions and examples
  - Add SCENARIO template block

- [ ] Edit `.cursor/commands/prd-one-pager.md`
  - Locate "Success Metric" section
  - Add Gherkin format for acceptance criteria
  - Include SCENARIO example

### Step 2: Create Spec Brief Command (45 minutes)

- [ ] Create `.cursor/commands/spec-brief.md`
  - Copy template from this plan
  - Test with sample PRD
  - Verify output formatting

### Step 3: Test and Validate (15 minutes)

- [ ] Run `/spec-brief` on a sample PRD
- [ ] Verify generated SPEC_BRIEF.md
- [ ] Check Gherkin format is correct
- [ ] Share with engineering team for feedback

---

## Success Metrics

| Metric | Target |
|--------|--------|
| PRD templates updated with Gherkin | 100% (2/2 files) |
| Spec Brief command functional | Yes |
| First Spec Brief generated | Within 1 week |
| Engineering team adoption | TBD |
| Reduction in PRD→implementation ambiguity | Measure after 3 specs |

---

## Next Steps After P0

Once P0 is complete, consider P1 items:

1. **Test Scenarios Section** - Add dedicated test scenario section to PRD templates
2. **Handoff Command** - Automate full handoff workflow (Spec Brief + tasks + test cases)
3. **Codebase Patterns Doc** - Document conventions for AI agents

---

## References

- Gherkin Syntax: https://cucumber.io/docs/gherkin/reference/
- Behavior-Driven Development: https://cucumber.io/docs/bdd/
- Cucumber (Testing Framework): https://cucumber.io/
