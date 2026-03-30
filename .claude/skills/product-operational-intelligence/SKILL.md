---
name: product-operational-intelligence
description: Use when the PM needs to build deep product knowledge, understand customer confusion patterns, prepare for product demos, or stay current on product changes. Triggers: demo prep, product knowledge gap, what changed in the product, where customers get confused, how does [feature] work, support pattern synthesis, product changelog, product deep dive, I need to know the product better.
---

# Product Operational Intelligence

Build deep, demo-ready product expertise that compounds over time — not just feature lists, but use case fluency, edge knowledge, and confusion awareness.

## When This Skill Activates

Use this skill when:
- PM is preparing a customer demo or product walk-through
- PM asks "what changed recently in [product]"
- PM wants to understand why customers struggle with a specific feature
- PM is onboarding onto a new product area
- PM is preparing for a QBR, renewal, or customer escalation requiring deep product knowledge
- PM needs to handle live product questions without scrambling

## Default Stance: Product Expert Mode

Start from what's documented in the workspace (`📦 Products/[product]/product-context/`, PRDs, spec-briefs, support signals), not from general knowledge. Synthesize upward from evidence to expertise. Always distinguish between what's confirmed in workspace files vs. what's inferred.

## Core Frameworks

### 1. Product Knowledge Depth Model (Three Layers)

Deep product knowledge requires all three layers — shallow knowledge stops at Layer 1:

```
Layer 1: Capability Knowledge
  → What the product can do (feature list, UI workflows, configuration options)
  → Sources: product-context files, PRDs, spec-briefs

Layer 2: Use Case Knowledge
  → How real customers use it: which personas, in which workflows, with what outcome
  → Sources: ICP files, customer interviews, win/loss data, persona files

Layer 3: Edge Knowledge
  → Where the product breaks down: known workarounds, rough edges, undocumented behaviors, demo traps
  → Sources: support signals, cs-escalation signals, customer confusion patterns, actual customer quotes
```

**Most PMs live at Layer 1. Expert PMs operate from Layer 3.**

---

### 2. Demo Storytelling Framework

A product demo is a narrative, not a tour. Structure every demo using this arc:

```
1. Open with the PROBLEM (not the product)
   → Start with the customer's world — pain, friction, workaround they're living with
   → Use the persona's JTBD language, not product feature names

2. Build to the AHA MOMENT
   → The single moment where the customer thinks "oh, that's exactly what I need"
   → Choose this moment first, then design the demo path that leads to it

3. Show VALUE before explaining HOW IT WORKS
   → What the customer gains before you explain the mechanism
   → "Here's what this gets you" before "here's how we built it"

4. Close with a QUESTION, not a feature
   → "Does this match what you're dealing with?" or "What else would you need to see?"
   → Closes the demo as a discovery moment, not a sales pitch
```

---

### 3. Confusion Map Pattern

Support signals cluster into three distinct confusion types — each requires a different response:

| Confusion Type | What It Looks Like | Root Cause | Right Response |
|----------------|-------------------|------------|----------------|
| **Onboarding Gap** | "I don't understand what this is for" | Customer never understood the concept | Better in-app guidance, improved onboarding flow |
| **Workflow Mismatch** | "This works, but not the way I expected" | Product works but mental model diverges | UX clarification, better affordances |
| **Product Gap** | "I'm trying to do X and it won't let me" | Customer has a legitimate use case the product doesn't support | Roadmap candidate, workaround documentation |

When synthesizing support signals, always classify each confusion zone into one of these three types — the response strategy is completely different per type.

---

### 4. Product Currency Rule

A PM's product knowledge decays. Rate of decay:
- New features shipped → old demo flows may be suboptimal (decay: moderate)
- UX changes → old muscle memory creates demo hesitation (decay: fast)
- Pricing/packaging changes → outdated claims in demos (decay: immediate risk)
- Bug fixes → previously avoided areas may now be safe to show (decay: upside opportunity)

**Run `/product-depth --mode changelog` before any high-stakes customer interaction**, especially if >30 days have passed since last reviewing product changes.

---

## Response Contract

When this skill activates, default to:

```markdown
## Product Knowledge: [Product/Feature] — [Mode]

**Layer reached:** [1: Capability / 2: Use Case / 3: Edge Knowledge]

**Sources consulted:**
- [File path 1]
- [File path 2]

**[Mode-specific output — see /product-depth and /demo-prep commands]**

**Knowledge gaps flagged:**
- [Anything undocumented that should be documented]
- [Any product-context file >60 days old]
```

---

## Guardrails

- **Never fabricate product capabilities** — cite only what exists in product-context files, PRDs, or spec-briefs. If undocumented, say so explicitly.
- **When product context is outdated** (>60 days), flag it — don't present stale information as current. Recommend running `/product-depth --mode changelog`.
- **Confusion analysis must be based on actual signals** — not hypothesized friction. Check `📚 Knowledge/Research/signals-YYYY-MM.md` for support-tagged signals before generating a confusion map.
- **Demo gaps are data** — when you identify a demo trap (something that looks bad for a specific persona), route it as a product signal, not just a preparation note.

## Integration

- Use `/product-depth` command to run structured deep-dives (demo background, changelog, confusion synthesis)
- Use `/demo-prep` command to generate a ready-to-use demo guide from this skill's frameworks
- Product confusion signals extracted here feed `/signal --source [support|call]` and eventually `/product-depth --mode confusion`
- Demo resonance/surprise moments from `/granola` post-meeting intelligence also feed this skill's Layer 3 (Edge Knowledge)

## Self-Learning

Before responding, read `LEARNED.md` in this skill directory when it exists and treat it as compact runtime guidance that sharpens this skill.

Rules for self-improvement:
- Keep `SKILL.md` human-owned; do not rewrite it directly from normal usage.
- Only promote specific, reusable, evidence-backed lessons into `LEARNED.md`.
