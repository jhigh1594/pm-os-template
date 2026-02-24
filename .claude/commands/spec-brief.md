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
   - Transform PRD content into Spec Brief format
   - Convert acceptance criteria to Gherkin format if not already done
   - Extract and structure test scenarios
   - Identify dependencies and integration points

4. **Determine output location:**
   - From PRD path, derive feature directory
   - Output to: `{prd-directory}/SPEC_BRIEF.md`

5. **Write Spec Brief:**
   - Create/update SPEC_BRIEF.md with generated content

6. **Report completion:**
   - Confirm file created with path
   - Suggest next steps

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

---

## Outputs

| Output | Format | Destination | Trigger |
|--------|--------|-------------|---------|
| [name] | [type/schema] | [where goes] | [when created] |

---

## Core Rules (Business Logic)

**Rule 1: [Name]**
- IF: [condition]
- THEN: [action/result]
- ELSE: [fallback behavior]

**Edge cases:**
- [Edge case 1]: [how to handle]
- [Edge case 2]: [how to handle]

---

## UI States

| State | Description | Entry Condition | Exit Condition |
|-------|-------------|-----------------|----------------|
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
```

---

## Usage Examples

**Example 1: Generate from PRD in current directory**
```
/spec-brief 📦 Products/AgilePlace/features/dependency-intelligence/prd.md
```

**Example 2: Generate with explicit path**
```
/spec-brief ./📦 Products/OKRs/features/bulk-import/full-prd.md (relative to workspace root)
```

**Example 3: Interactive mode (no argument)**
```
/spec-brief
```
Prompts: "Which PRD should I generate a Spec Brief from?"

---

## Success Criteria

1. **Completeness:** Spec Brief contains all sections from template
2. **Fidelity:** Key information from PRD is preserved
3. **Clarity:** Brief is concise (target: 2-3 pages max)
4. **Actionability:** Implementation notes provide clear starting point
5. **Testability:** All acceptance criteria use Gherkin format
