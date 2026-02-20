# /capture-pattern - Capture Semantic Learning

Capture a substantial pattern, decision, convention, or mistake to `learned-patterns.md` for future sessions.

---

## When to Use

Invoke this command when you notice:
- A **decision** worth remembering (chose X over Y because Z)
- A **convention** specific to this workspace (always do X before Y)
- A **mistake** that wasted time (don't do X, it breaks Y)
- A **productive pattern** that produces reliable results (sequence: X → Y → Z)

---

## Command Arguments

Parse the command arguments:
1. **Type** (optional): `decision`, `convention`, `mistake`, `pattern`, `tool`
   - If not provided, ask user to select
2. **Description** (optional): Brief description of the pattern
   - If not provided, prompt for details

---

## Execution

### Step 1: Determine Pattern Type

If type not provided, ask:

```
What type of pattern are you capturing?

1. Decision - A choice made with reasoning (chose X over Y)
2. Convention - Workspace-specific pattern (always do X)
3. Mistake - Painful lesson to avoid (don't do X)
4. Pattern - Productive sequence (X → Y → Z)
5. Tool - Tool/domain-specific wisdom (for X, use Y)
```

### Step 2: Gather Pattern Details

Based on type, collect:

**For Decisions**:
- Context: What situation triggered this decision?
- Options: What alternatives were considered?
- Chosen: What did you choose?
- Reasoning: Why this over alternatives?

**For Conventions**:
- Pattern: What should always be done?
- Context: When does this apply?
- Why: What's the reasoning?

**For Mistakes**:
- What happened: What went wrong?
- Why it failed: Root cause
- How to avoid: Prevention steps
- Cost: Time/pain saved

**For Productive Patterns**:
- Trigger: When to use this pattern
- Sequence: Step-by-step workflow
- Why it works: Reasoning

**For Tool-Specific Wisdom**:
- Tool/Domain: What tool or domain
- Pattern: What to do
- Context: When applicable
- Gotchas: What to watch out for

### Step 3: Quality Gate Check

Before capturing, verify the pattern passes **all 4 gates**:

```
Quality Gate Check:
✓ Actionable: Can I do something specific with this?
✓ Specific: Is it tied to my context, not generic advice?
✓ Durable: Will it be useful in 5+ future sessions?
✓ Non-obvious: Is this something I wouldn't naturally know?

Does this pattern pass all 4 gates? (yes/no)
```

If **no** to any gate:
- Explain why it fails
- Suggest how to make it pass, or
- Recommend not capturing (not all learnings become patterns)

### Step 4: Set Confidence Level

```
Confidence level:
- High: Already reinforced multiple times
- Medium: New pattern, needs validation
- Low: Observed once, experimental
```

### Step 5: Write to learned-patterns.md

Use the Edit tool to add the pattern to the appropriate section in:
`./.aipmos/patterns/learned-patterns.md` (relative to workspace root)

Update:
1. Add pattern to correct section
2. Update `_Total patterns: N_` counter
3. Add entry to Validation Log
4. Update `_Last updated: [date]_`

---

## Output Format

After successful capture:

```
✅ Pattern captured: [Pattern Title]

   Type: [Decision/Convention/Mistake/Pattern/Tool]
   Section: [Section Name]
   Confidence: [High/Medium/Low]

   File: .aipmos/patterns/learned-patterns.md
   Total patterns: N
```

---

## Examples

### Example 1: Capture a Decision
```
/capture-pattern decision "Semantic Pattern Capture System"

Context: Old system captured tool invocations, not meaning
Options: Delete, Rebuild with semantic capture, Manual only
Chosen: Rebuild with semantic capture
Reasoning: Best balance of signal and maintainability
Confidence: Medium
```

### Example 2: Capture a Convention
```
/capture-pattern convention "Planview Corporate Template"

Pattern: Always use corporate template for presentations
Context: Any Planview slide deck
Why: Saves 1-2 hours, brand consistency, marketing-approved
Confidence: High
```

### Example 3: Interactive Capture
```
/capture-pattern

> What type of pattern?
> 1. Decision  2. Convention  3. Mistake  4. Pattern  5. Tool
> 3

> What went wrong?
> [User describes mistake]

> Why did it fail?
> [User explains root cause]

> How can this be avoided in the future?
> [User provides prevention steps]

> Estimated time/pain saved?
> ~2 hours per occurrence

> Quality Gate Check:
> ✓ Actionable: yes
> ✓ Specific: yes
> ✓ Durable: yes
> ✓ Non-obvious: yes
>
> Confidence level? (High/Medium/Low)
> Medium

> ✅ Pattern captured: Don't Create Presentations from Scratch
```

---

## Notes

- Patterns should be **substantial** - skip trivial learnings
- When in doubt, don't capture - quality over quantity
- Weekly review will validate and update confidence levels
- Deprecated patterns are kept but marked for reference

---

## Integration

**Related commands**:
- `/refresh-memory` - Updates current state in memory.md
- `/capture-pattern` - Updates accumulated wisdom in learned-patterns.md

**Weekly review**: Use `/capture-pattern` to update confidence levels based on recent sessions
