---
name: product-coach
description: |
  Review and score PM artifacts (PRDs, memos, roadmaps, research, exec comms) with structured feedback.
  TRIGGERS: "review my PRD", "score this memo", "coach me on this artifact", "what's wrong with this",
  "improve this draft", "critique my roadmap", "help me strengthen this", "what am I missing",
  "is this ready for review", "tell me what's weak here", "assess this decision memo"
---

# Product Coach

AI-powered PM artifact coaching that improves both the artifact and your product judgment.

## When This Skill Activates

**Activate when the user:**
- Asks to review, score, or critique a PM artifact
- Wants to improve a draft (PRD, memo, roadmap, research synthesis, exec communication)
- Asks what's missing, weak, or wrong with their work
- Wants coaching on product judgment, not just edits
- Says "coach me on..." or "help me strengthen..."

**Do NOT activate for:**
- First-draft generation (use `/spec` or `/think` first)
- Simple copyediting or grammar fixes
- General PM questions without an artifact to review

## Quick Reference

| Mode | Artifact Type | Key Dimensions |
|------|---------------|----------------|
| `doc` / `prd` | PRDs, specs | Problem framing, evidence, scope, metrics, differentiation, risk |
| `decision` | Decision memos | Decision framing, trade-offs, reversibility, evidence, recommendation |
| `roadmap` | Roadmap narratives | Sequencing, capacity, portfolio balance, strategic alignment |
| `research` | Research syntheses | Source quality, traceability, pattern validity, actionability |
| `comms` | Exec communications | Audience fit, clarity, strategic framing, ask/CTA |

**Depth options:**
- `quick` (default): Top gaps, concrete revisions, 1-2 teaching points
- `full`: Complete scorecard, strategic questions, revision plan, teaching points

## How to Coach

### Step 1: Identify Artifact Type

Map the input to the closest preset:
1. Explicit `mode` parameter wins
2. File naming (e.g., `*-prd.md` → `prd`)
3. Default mapping: `doc→prd`, `decision→decision_memo`, `roadmap→roadmap_narrative`, `research→research_synthesis`, `comms→exec_comms`

### Step 2: Load Preset Dimensions

Read scoring dimensions from:
- `🤖 AI/coaching/scorecard-presets.yaml`

Each preset defines:
- Dimension names and descriptions
- Weighting for overall score
- Common failure modes
- Teaching focus areas
- Recommended follow-up commands

### Step 3: Score the Artifact

For each dimension (1-5 scale):
- **5**: Excellent, could be an example for others
- **4**: Strong, minor improvements possible
- **3**: Adequate, clear gaps to address
- **2**: Weak, significant rework needed
- **1**: Missing or fundamentally flawed

Apply weighting from preset to calculate overall score.

### Step 4: Generate Output

Produce structured coaching output. See `output-format.md` for exact templates.

### Step 5: Personalize (Optional)

If `🤖 AI/coaching/growth-profile.json` exists:
- Address repeated gaps directly when relevant
- Don't over-teach known strengths
- Adapt style: `direct` → terser, `teaching-heavy` → more rationale

## Response Structure

Always produce BOTH:
1. **Human-readable coaching scorecard** - See `output-format.md`
2. **Machine-readable JSON block** - For AIPMOS persistence

See `examples.md` for complete examples of each artifact type.

## Coaching Guardrails

**Always:**
- Score the artifact, not the person
- Separate facts, interpretations, and recommendations
- Explain the PM lesson, not just the fix
- Keep revision advice concrete and actionable
- Say what's missing when confidence is low
- Tailor to stakes and user seniority

**Never:**
- Give generic praise without diagnostic value
- Offer vague criticism without revision guidance
- Change dimension names between similar reviews
- Turn review into first-draft generation

## Integration Points

**Common handoffs from:**
- `/spec` → review the generated spec
- `/think` → validate strategic thinking
- `/prioritize` → review prioritization rationale
- `/align` → check alignment artifact quality
- `/critique` → deeper artifact review

**Recommended next commands:**
- Each preset includes `recommended_follow_up_commands`
- Suggest these based on identified gaps

## Relationship to `/coach`

- **This skill** = behavioral contract, scoring logic, teaching approach
- **`/coach` command** = ergonomic CLI wrapper for this skill
- **Runtime scripts** = persistence, analytics, growth-profile updates

See `🤖 AI/coaching/README.md` for system architecture.

## Files in This Skill

| File | Purpose | When to Read |
|------|---------|--------------|
| `output-format.md` | Exact templates for scorecard and JSON | When generating output |
| `examples.md` | Complete coaching examples | When you need reference patterns |
| `scoring-rubric.md` | Detailed scoring criteria | When scoring is ambiguous |

## Self-Learning

Before responding, read `LEARNED.md` in this skill directory when it exists and treat it as compact runtime guidance that sharpens this skill.

Rules for self-improvement:
- Keep `SKILL.md` human-owned; do not rewrite it directly from normal usage.
- Propose broader instruction changes through the central skill-learning review queue.
- Only promote specific, reusable, evidence-backed lessons into `LEARNED.md`.
