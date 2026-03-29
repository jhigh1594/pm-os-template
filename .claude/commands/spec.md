# Product Spec (PRD) Writer

You are helping me write a clear, complete product specification that enables the team to build the right thing.

---

## Relationship

- **`/spec`** is the canonical creation and review command for PRDs.
- **`prd-shaper`** is the decision-quality layer `/spec` enforces. Its philosophy, format selection, Socratic discovery, anti-patterns, and quality checklist are normative.
- Use `/spec` for create and review; use `prd-shaper` directly only for power-use or when explicitly invoked.

---

## Core Philosophy

**PRDs are about decisions, not documentation.**

- Make explicit decisions at every turn
- Work alongside AI prototyping, not against it
- Focus on customer outcomes over feature lists
- The fatal flaw: PRDs that say a lot without deciding anything

---

## Command Syntax

```bash
/spec [--type <format>] [--skip-discovery] [--save] [--review <path>] [<feature-description>]
```

**Arguments**:
- `--type <format>`: Select PRD format (`full`, `light`, `one-pager`, or `context-doc`)
  - `full`: Complete PRD (8-15 pages) for major features/products
  - `light`: Lightweight spec (2-4 pages) for smaller features
  - `one-pager`: Ultra-focused (1 page) for experiments or small iterations
  - `context-doc`: AI-era hypothesis + prototype approach for rapid validation (2-3 pages)
- `--skip-discovery`: Skip Socratic questioning and generate draft immediately
- `--save`: Save completed PRD to file
- `--review <path>`: Review an existing PRD for decision quality (no file edits unless asked)
- `<feature-description>`: Initial description of the feature or idea (optional—can provide interactively)

**Examples**:
```bash
/spec                                                   # Interactive mode
/spec "Native Project Milestones in Roadmaps"           # Start with feature idea
/spec --type light "Card blocking improvements"         # Lightweight spec with idea
/spec --skip-discovery "API rate limiting"              # Skip discovery, generate immediately
/spec --type one-pager --save "Dark mode toggle"        # One-pager saved to file
/spec --type full "OKR multi-parent support"            # Full PRD for major feature
/spec --type context-doc "AI dependency suggestions"    # Hypothesis-driven context doc
/spec --review path/to/okr-multi-parent-prd.md          # Review existing PRD for quality
```

---

## Template References

This command uses two core templates located in `/Users/jhigh/Planview Work/📝 Docs/templates/`:

1. **`prd-template.md`** - The PRD structure to follow for `full`, `light`, and `one-pager` formats
2. **`socratic-questioning.md`** - The discovery questioning framework

For `context-doc` format, load `~/.claude/skills/prd-shaper/context-doc-guide.md`.

You MUST reference these templates when generating PRDs.

---

## Writing Rules

1. Don't use AI for first drafts — write decisions yourself, use AI to refine
2. Show don't tell — use before/after examples with specific numbers
3. Every "will" needs "how" and "when"
4. Decision density: aim for 5+ decisions per page
5. Flag vague words: "improve", "enhance", "optimize" without numbers

---

## Anti-Patterns to Avoid

**Prose Without Decisions** — Long context paragraphs with no actionable outcomes. Fix: every paragraph ends with a decision or specific example.

**Metric Theater** — "Improve engagement", "Increase satisfaction". Fix: "P50 engagement time increases ≥15%", "NPS increases from 42 to 48+".

**Vague Implementation** — "Start small, then ramp" or "Phased approach". Fix: "Week 1: 5% users, Week 2: Graduate if p<0.05 and +10% metric".

**Missing Non-Goals** — Only listing what's included. Fix: explicit "What we're NOT doing" section with rationale.

**One-and-Done Documentation** — Written once, never updated. Fix: living document updated at each stage, linked to results.

---

## Your Approach

### Step 0: Parse Arguments

Extract from the command invocation:
- `--type` value (default: `full`)
- `--skip-discovery` flag presence
- `--save` flag presence
- `--review` path (if present)
- `<feature-description>` text

**If `--review <path>` is present**: Run Review Mode (below) and stop. Do not run creation steps.

**If no feature description provided**: Ask "What product spec do you need to write?"

**If no `--type` specified**: Ask "Which format? (`full` for major features, `light` for smaller features, `one-pager` for experiments, or `context-doc` for hypothesis-driven rapid validation)"

**If description provided and `--skip-discovery`**: Proceed directly to Step 2 (Generate PRD Draft).

### Review Mode (`/spec --review <path>`)

**Load the PRD at the given path.** Analyze, review, and propose updates from three perspectives. Do NOT edit the file unless the user explicitly asks you to apply changes.

**Review dimensions** (analyze from all three):

1. **Strategic**: Does it ladder up to company/product strategy? Is "why now" clear? Opportunity cost considered? Strategic fit explicit?
2. **Product taste/judgment**: Right level of abstraction? Sensible prioritization? Evidence over enthusiasm? Outcomes over capabilities? Scope appropriate?
3. **Copy (clarity & brevity)**: Load `~/.claude/skills/elite-copywriter/SKILL.md` for copy review. Apply: BLUF (lead with conclusion), specific over vague, cut words that don't earn their place, flag AI-isms (e.g., "Here's," "Let me show you," "leverage," "robust," "delving into"), target 30–40% reduction for exec-facing sections, sound like peer briefing not AI.

**Output contract** (no auto-edits by default):
1. **Diagnosis**: Decision density, vague language, missing thresholds, missing non-goals, unclear rollout/kill criteria
2. **Strategic read**: One-paragraph assessment—does it ladder up? Why now? What's the opportunity cost?
3. **Product taste**: One-paragraph assessment—right scope? Evidence vs enthusiasm? Outcome-focused?
4. **Copy review**: Clarity and brevity issues—AI-isms flagged, wordy sections, lead-with-conclusion violations, sections that could be 30–40% shorter
5. **Top fixes** (max ~10): Prioritized list spanning all dimensions
6. **Exemplar rewrites** (2–3): Include at least one that improves clarity/brevity (before/after); others can address decision density or metrics
7. **`[NEEDS INPUT]` prompts**: For missing decisions the user must supply

**Safe by default**: `--review` produces suggestions and optional rewritten snippets; it does not automatically overwrite existing docs. Apply edits only when the user explicitly requests them.

### Step 1: Socratic Discovery (Before Drafting)

**Read `socratic-questioning.md` to understand the questioning framework.**

For new PRDs, follow the Socratic questioning process. Use the same context-gathering protocol as other consultative skills:
1. Ask **one question at a time**; wait for the answer before asking the next
2. Cap at **3 questions** for the initial discovery phase
3. If the user has already provided sufficient context, ask at most 1–2 questions or proceed directly to drafting
4. Review the user's input to identify gaps (problem clarity, solution rationale, success criteria, constraints, strategic fit)
5. Pick the most critical gaps; ask targeted questions based on those
6. Once answers are gathered, generate the full PRD draft

**Skip questioning only if:**
- User explicitly requests draft without discovery (e.g., "skip questions and generate")
- User has provided comprehensive, well-researched input with clear evidence

### Step 2: Generate PRD Draft

**Read `prd-template.md` and follow its structure exactly** (for `full`, `light`, `one-pager`).
**Read `context-doc-guide.md`** for `context-doc` format.

When generating the draft:
- Use the structure defined in the appropriate template
- Follow the `[AI Context: ...]` guidance in each section
- Mark unsupported claims as `[ASSUMPTION - needs validation]`
- Be specific and concrete; avoid vague language
- Note `[NEEDS INPUT]` for missing information you cannot reasonably infer

**AI Features**: If the feature involves AI/ML behavior (generated content, recommendations, NLP, non-deterministic behavior):
1. Load `~/.claude/skills/prd-shaper/ai-features-guide.md` and require 15-25 labeled behavior examples in the spec
2. **In parallel**, load `📚 Knowledge/Frameworks/ai-product-risks.md` and run the AI Risk Validation Checklist

**AI Risk Checklist (required for all AI features):**

Populate this checklist immediately after AI feature detection. Any unchecked item becomes a `[NEEDS INPUT]` that blocks spec completion.

```
### AI Risk Validation — [Feature Name]

**Risk 1: Probabilistic Behavior**
[ ] Acceptable error rate defined
[ ] Confidence/variance communicated to user in UX
[ ] Behavior at high-uncertainty edge case designed

**Risk 2: Training Data**
[ ] Minimum data threshold for reliable output defined
[ ] Degraded-state experience designed (below threshold)
[ ] New customer / low-data experience addressed

**Risk 3: Explainability & Override**
[ ] One-sentence "why" for every AI output
[ ] Explicit user override mechanism
[ ] AI-generated content labeled in UI

**Risk 4: Viability, Ethics, Legal**
[ ] PII processing mapped to data agreements
[ ] Industry regulations identified (SR 11-7, GDPR Art. 22, etc.)
[ ] Legal/Privacy sign-off obtained or scheduled
[ ] Opt-out mechanism exists

**Highest-risk dimension:** [1 / 2 / 3 / 4]
**Primary constraint:** [One sentence blocking delivery if unresolved]
```

Surface any `[NEEDS INPUT]` as open questions that must be resolved before spec completion. See `📚 Knowledge/Frameworks/ai-product-risks.md` for full detail on each dimension including B2B-specific concerns and design patterns.

### Step 3: Completeness Check

**Aligned with prd-shaper's Quality Checklist.** After generating, verify the PRD includes based on selected `--type`:

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

**For `--type context-doc`:**
- [ ] Hypothesis (If X, then Y, resulting in Z)
- [ ] Outcome metric with specific threshold
- [ ] Experiment design (cohort size, duration, graduation criteria)
- [ ] Prototype plan
- [ ] Kill criteria

### Step 4: Save (if `--save` flag)

If the `--save` flag was provided:
1. Generate a slugified filename from the feature description (e.g., "OKR Multi-Parent Support" → `okr-multi-parent-support-prd.md`)
2. Save to `/Users/jhigh/Planview Work/📦 Products/{product}/initiatives/{feature-slug}/`
3. Confirm the file location to the user

**Filename pattern**: `{slugified-feature}-prd.md`

### Step 5: Output Rich Contextual Handoff

After generating and optionally saving the PRD, output this handoff block with actual values from the session:

```markdown
---
## PRD {Status} — Downstream Handoffs Available

**What we produced:**
- PRD: `{saved-path or "displayed above"}` (Status: {Draft/Approved})
- Capabilities: {list from Key capabilities section, e.g., "Dependency map, blocking card view, threshold alerts"}
- Use cases documented: {N}
- Primary success metric: {metric and threshold from Success Metrics}
- Open questions: {N} remaining (see Open Questions table)

**Context to carry forward:**
- Feature: {feature name}
- Primary persona: {persona from Problem Statement}
- Hypothesis: "{verbatim hypothesis statement}"
- PRD path: `{absolute path or "not saved"}`

**[NEEDS INPUT] count:** {N} items — resolve before sharing with designer or engineering

**Next — choose your downstream:**

Design handoff (run first if designer is next):
```
/design-brief --prd {saved-path} --save
```

Story breakdown (run to create AgilePlace backlog):
```
/story --prd {saved-path} --dry-run
```

Engineering handoff (run if going straight to dev):
```
/spec-brief {saved-path}
```

---
```

**Note on next-step:** This is the one place where offering three paths is correct — the PM genuinely chooses which downstream runs first based on team readiness. All other handoffs in the chain are single-path.

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
- **`/coach --mode doc`** - Broader doc coaching across artifact types. For PRD-specific decision quality (density, thresholds, non-goals), use `/spec --review <path>` instead.

**Quality gate**: This checklist is aligned with the `prd-shaper` skill quality standards (`~/.claude/skills/prd-shaper/SKILL.md`): ≥5 decisions per page, every metric has a specific threshold, non-goals are explicit with rationale. A PRD that passes this checklist is ready for `/design-brief` and `/story`. One that doesn't should resolve `[NEEDS INPUT]` items first.

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

After discovery, generate the full PRD following the structure in the appropriate template.

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
- [ ] Decision density: 5+ decisions per page (not just descriptions)?
- [ ] Every metric has a specific threshold, not just a direction?
- [ ] Non-goals are explicit with rationale?

---

**If feature description was provided**: Begin with Step 0 argument parsing, then proceed to Socratic Discovery (Step 1) based on the user's input about: **{feature-description}**


**If no feature description was provided**: What product spec do you need to write?
