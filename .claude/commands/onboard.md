# PM-OS Workspace Onboarding

Set up your PM Operating System workspace by filling out the template skeleton with your context, then tackle your first task.

---

## Overview

This command guides you through:

1. **Phase 1: Configure Your Context** — Fill out GOALS.md, memory.md, and CLAUDE.md with your company, role, and goals
2. **Phase 2: Your First Task** — Pick something to work on and get started

---

## Phase 1: Configure Your Context

Let's set up your workspace with your information.

### Step 1: Basic Information

I need to understand your situation:

1. **Your name and role**: What's your title? (e.g., "Senior PM", "Product Director")
2. **Your company**: Where do you work?
3. **Your products**: What products do you own? (List 1-3)
4. **Your manager**: Who do you report to?

### Step 2: Your Goals

Tell me about your current priorities:

1. **This quarter's goals**: What are you trying to accomplish in the next 3 months?
2. **Current focus**: What's the most important thing you're working on right now?
3. **Key stakeholders**: Who do you need to align with regularly?

### Step 3: Product Context

For each product you own, tell me:

1. **What it does**: One-sentence description
2. **Who it's for**: Your target customer/ICP
3. **Key metrics**: What numbers matter most?
4. **Current priorities**: What are you building/improving?

---

## Output: Files I'll Update

Based on your answers, I'll update these files:

### GOALS.md
```markdown
# GOALS.md

## Who I Am

**[Your Name]** | [Your Role] | [Your Company] ([Product 1], [Product 2])

[Brief bio - what kind of PM are you? What energizes you?]

**Core beliefs:** [Your core beliefs about product management]

---

## What I Own

| Product | Description | Key Metrics |
|---------|-------------|-------------|
| **[Product 1]** | [Description] | [Metrics] |
| **[Product 2]** | [Description] | [Metrics] |

---

## Current Quarter Goals

### Goal 1: [Goal Title]

**Target:** [Specific outcome]

**Key initiatives:**
- [Initiative 1]
- [Initiative 2]

**Status:** 🟢 On track / 🟡 At risk / 🔴 Blocked

---

## Key Stakeholders

| Name | Role | Relationship | Notes |
|------|------|--------------|-------|
| [Name] | [Role] | [Relationship] | [Communication preferences] |
```

### memory.md
```markdown
# Workspace Memory

## Current Focus

**Role**: [Your role at company]

**Product Vision**: [Your product vision]

**Active Task**: [What you're working on now]

**Recent Completed Work**:
- [Recent accomplishment]

## Product Context

### [Product Name]

**What is [Product]**: [Description]

**Value Proposition**: [Core value prop]

**Core Differentiators**:
- [Differentiator 1]
- [Differentiator 2]

**Target Market**: [ICP, market size]

## Active Decisions

**Strategic Questions**:
1. [Question you're wrestling with]

**Open Questions**:
- [Things you need to figure out]

---

**Last Updated**: [Today's date]
```

### CLAUDE.md (Company References)
I'll update any `[UPDATE THIS]` placeholders with your company info.

---

## Phase 2: Your First Task

Now that your workspace is configured, let's pick something to work on.

### Options

Pick one:

**A. Quick Win** — Something you can complete in 1-2 hours
- Process your latest meeting notes (`/granola`)
- Write a spec for a small feature (`/spec`)
- Analyze competitor pricing (`/price-intel`)
- Capture a pattern you've noticed (`/capture-pattern`)

**B. Strategic Work** — Bigger thinking
- Brainstorm solutions to a problem (`/brainstorm`)
- Think through a strategic decision (`/think`)
- Plan your week (`/today`)
- Research a topic (`/research`)

**C. Communication** — Stakeholder alignment
- Draft a memo or update (`/write`)
- Prepare for a presentation (`/narrative`)
- Plan stakeholder alignment (`/align`)

### How I'll Help

Once you pick a task type, I'll:

1. **Guide you through it** using the relevant command
2. **Create the output** in the right location
3. **Update your memory** with what we accomplished
4. **Suggest next steps** based on what we learned

---

## Onboarding Flow

```
┌─────────────────────────────────────────────────────┐
│  START: Tell me about yourself                      │
│  (Name, role, company, products)                    │
└─────────────────────┬───────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────────┐
│  PHASE 1: I update your files                       │
│  ✓ GOALS.md — Your identity and goals               │
│  ✓ memory.md — Your current context                 │
│  ✓ CLAUDE.md — Company references                   │
└─────────────────────┬───────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────────┐
│  PHASE 2: Pick your first task                      │
│  A. Quick win (1-2 hrs)                             │
│  B. Strategic work (deeper thinking)                │
│  C. Communication (stakeholder alignment)           │
└─────────────────────┬───────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────────┐
│  COMPLETE: Workspace ready, first task done         │
│  → Run /today to plan your next session             │
└─────────────────────────────────────────────────────┘
```

---

## Constraints

- **Keep it simple**: Don't over-engineer the setup - you can always update later
- **Start small**: Pick a task you can complete in one session
- **Learn by doing**: The best way to learn PM-OS is to use it
- **Iterate**: Your GOALS.md and memory.md are living documents - update them as you learn

---

## After Onboarding

Once you're set up, here are your most useful commands:

| Command | Purpose |
|---------|---------|
| `/today` | Daily planning workflow |
| `/think` | Strategic thinking mode |
| `/brainstorm` | Generate ideas with different perspectives |
| `/spec` | Write product specs/PRDs |
| `/granola` | Extract meeting notes |
| `/compete` | Competitive intelligence |
| `/refresh-memory` | Update your memory.md |

---

**Ready to set up your workspace?**

Tell me:
1. Your name and role
2. Your company
3. Your products
4. Your current quarter goals (1-3)
5. What you'd like to work on first
