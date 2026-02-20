# Product Spec (PRD) Writer

You are helping me write a clear, complete product specification that enables the team to build the right thing.

---

## Command Syntax

```bash
/spec [--type <format>] [--skip-discovery] [--save] [<feature-description>]
```

**Arguments**:
- `--type <format>`: Select PRD format (`full`, `light`, or `one-pager`)
  - `full`: Complete PRD (8-15 pages) for major features/products
  - `light`: Lightweight spec (2-4 pages) for smaller features
  - `one-pager`: Ultra-focused (1 page) for experiments or small iterations
- `--skip-discovery`: Skip Socratic questioning and generate draft immediately
- `--save`: Save completed PRD to file
- `<feature-description>`: Initial description of the feature or idea (optional—can provide interactively)

**Examples**:
```bash
/spec                                              # Interactive mode
/spec "Native Project Milestones in Roadmaps"      # Start with feature idea
/spec --type light "Card blocking improvements"    # Lightweight spec with idea
/spec --skip-discovery "API rate limiting"         # Skip discovery, generate immediately
/spec --type one-pager --save "Dark mode toggle"   # One-pager saved to file
/spec --type full "OKR multi-parent support"       # Full PRD for major feature
```

---

## Template References

This command uses two core templates located in `./Docs/templates/` (relative to workspace root):

1. **`prd-template.md`** - The PRD structure to follow
2. **`socratic-questioning.md`** - The discovery questioning framework

You MUST reference these templates when generating PRDs.

---

## Your Approach

### Step 0: Parse Arguments

Extract from the command invocation:
- `--type` value (default: `full`)
- `--skip-discovery` flag presence
- `--save` flag presence
- `<feature-description>` text

**If no feature description provided**: Ask "What product spec do you need to write?"

**If no `--type` specified**: Ask "Which format? (`full` for major features, `light` for smaller features, or `one-pager` for experiments)"

**If description provided and `--skip-discovery`**: Proceed directly to Step 2 (Generate PRD Draft).

### Step 1: Socratic Discovery (Before Drafting)

**Read `socratic-questioning.md` to understand the questioning framework.**

For new PRDs, follow the Socratic questioning process:
1. Review the user's input (rough notes, context, feature idea)
2. Identify gaps around: problem clarity, solution rationale, success criteria, constraints, and strategic fit
3. Ask 3-5 targeted clarifying questions based on the most important gaps
4. Wait for the user's answers
5. Then generate the full PRD draft

**Skip questioning only if:**
- User explicitly requests draft without discovery (e.g., "skip questions and generate")
- User has provided comprehensive, well-researched input with clear evidence

### Step 2: Generate PRD Draft

**Read `prd-template.md` and follow its structure exactly.**

When generating the draft:
- Use the structure defined in `prd-template.md`
- Follow the `[AI Context: ...]` guidance in each section
- Mark unsupported claims as `[ASSUMPTION - needs validation]`
- Be specific and concrete; avoid vague language
- Note `[NEEDS INPUT]` for missing information you cannot reasonably infer

### Step 3: Completeness Check

After generating, verify the PRD includes based on selected `--type`:

**For `--type full` PRD:**

**Problem Alignment (Part 1):**
- [ ] TL;DR with specific problem statements, business impact, solution approach
- [ ] Problem Statement with who/what/impact and evidence confidence level
- [ ] Current Alternatives & Gaps (competitors + workarounds)
- [ ] Desired Outcome (after-state in user terms)
- [ ] Strategic Fit (connects to company strategy/initiatives)
- [ ] Customer Insights & Motivating Data (quantitative + qualitative)

**Solution Alignment (Part 2):**
- [ ] Hypothesis & Expected Impact (primary metric + ROI justification)
- [ ] Proposed Solution with key capabilities
- [ ] How We Differentiate vs alternatives
- [ ] Solutions Considered table with rationale
- [ ] Key Use Cases / Workflows (2-4 core scenarios)
- [ ] Success Metrics (primary + leading indicators + guardrails)
- [ ] Dependencies & Risks table
- [ ] Open Questions table with owners

**For `--type light` Spec:**
- [ ] TL;DR with problem summary and solution overview
- [ ] Problem Statement with who/what/impact
- [ ] Proposed Solution with key capabilities
- [ ] Success Metrics (primary + leading indicators)
- [ ] Scope (in/out items)
- [ ] Key Dependencies

**For `--type one-pager`:**
- [ ] Problem Statement (1-2 sentences)
- [ ] Hypothesis (what we believe will happen)
- [ ] Proposed Test/Implementation
- [ ] Success Criteria (measurable)

### Step 4: Save (if `--save` flag)

If the `--save` flag was provided:
1. Generate a slugified filename from the feature description (e.g., "OKR Multi-Parent Support" → `okr-multi-parent-support-prd.md`)
2. Save to `./📦 Products/{product}/initiatives/{feature-slug}/` (relative to workspace root)
3. Confirm the file location to the user

**Filename pattern**: `{slugified-feature}-prd.md`

---

## Constraints

- Don't skip Socratic questioning for major features
- Don't write specs in isolation (collaborate with engineering, design, stakeholders)
- Don't skip the problem section (solution without problem context is useless)
- Don't define success criteria after launch (define upfront)
- Don't overcomplicate V1 scope (remember "version two is a lie")
- Don't write vague acceptance criteria (be specific and testable)
- Don't forget non-functional requirements (performance, security, accessibility)
- Don't treat the spec as final (it's a living doc that evolves with learning)

---

## Integration with Other Commands

- **`/discover`** - Use before writing the spec (validate problem and solution first)
- **`/think`** - Frame the strategic context
- **`/decide`** - For key technical or scope trade-offs
- **`/write`** - For specific sections (executive summary, customer messaging)
- **`/align`** - Get stakeholder buy-in on the spec

---

## Output Format

### Discovery Phase (if applicable)

Based on the Socratic questioning framework from `socratic-questioning.md`, I need to understand:

1. **Problem Clarity**: What specific user pain point does this solve?
2. **Solution Validation**: Why is this the right solution for that problem?
3. **Success Criteria**: How will we know if this feature is successful?
4. **Constraints**: What are we NOT going to do as part of this?
5. **Strategic Fit**: Why is this the right feature to build RIGHT NOW?

(Pick 3-5 most relevant questions based on gaps in user input)

### Draft Phase

After discovery, generate the full PRD following the structure in `prd-template.md`.

### Review Checklist

**Before sharing with the team, verify**:
- [ ] Would an engineer know what to build from this spec?
- [ ] Would a designer know what to design?
- [ ] Would QA know what to test?
- [ ] Would marketing know how to position it?
- [ ] Would support know how to help customers?
- [ ] Is the problem evidence-based (not just your opinion)?
- [ ] Are success criteria measurable and time-bound?
- [ ] Is V1 scope truly minimal but complete?

---

**If feature description was provided**: Begin with Step 0 argument parsing, then proceed to Socratic Discovery (Step 1) based on the user's input about: **{feature-description}**

**If no feature description was provided**: What product spec do you need to write?
