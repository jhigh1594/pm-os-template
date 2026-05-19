---
name: product-panel
description: 'Product thinking panel — invoke world-class product personas for perspective,
  critique, and guidance.

  TRIGGERS: "product panel", "what would shreyas think", "get the council", "product
  council",

  "council review", "multi-perspective review", "product thinkers", "panel review",

  "shreyas on this", "tobi on this", "patrick on this", "jony on this", "brian on

  this", "growth on this", "grove on this", "andy on this", "growth strategy"'
---

# Product Thinking Panel

Invoke world-class product personas for perspective, critique, and guidance. Each persona embodies a distinct dimension of product thinking — together they create a complete advisory panel.

## Modes

Parse `$ARGUMENTS` for persona name(s) and topic. The first word(s) determine mode; the rest is the topic.

```
/product-panel shreyas [topic]        → Shreyas Doshi only
/product-panel tobi [topic]           → Tobi Lutke only
/product-panel patrick [topic]        → Patrick Collison only
/product-panel jony [topic]           → Jony Ive only
/product-panel brian [topic]          → Brian Chesky only
/product-panel growth [topic]         → Product Growth Strategist only
/product-panel grove [topic]          → Andy Grove only
/product-panel shreyas+growth [topic] → Duo mode (any combination with +)
/product-panel full [topic]           → All 7 personas, individual responses
/product-panel council [topic]        → All 7 + synthesized agreement/tension analysis
```

**Default:** If no persona name is detected, use `council` mode.

## Available Personas

| Short Name | Agent Name | Specialty | Best For |
|------------|-----------|-----------|----------|
| `shreyas` | shreyas-doshi | Product sense & prioritization | Scoping, prioritization, "is this obviously good?" |
| `tobi` | tobi-lutke | Systems & platform thinking | Architecture, platform vs feature, craft |
| `patrick` | patrick-collison | Speed & strategic clarity | Strategy review, speed audit, what to cut |
| `jony` | jony-ive | Taste, simplicity & reduction | UI/UX review, simplicity audit, taste check |
| `brian` | brian-chesky | Customer empathy & experience | Customer journey, experience design, storytelling |
| `growth` | product-growth | Growth loops, PLG & monetization | Growth strategy, retention, activation, pricing, GTM |
| `grove` | andy-grove | Operational excellence & strategic paranoia | Execution, leverage, bottlenecks, inflection points, management discipline, decision-making |

## Routing Logic

### Step 1: Parse Arguments

1. Extract persona names from the start of arguments
2. Everything after the persona name(s) is the topic
3. If topic is empty, ask the user what they want the panel to weigh in on

### Step 2: Spawn Agent(s)

**Single persona:**
- Spawn the named agent with the topic as its prompt
- Return the agent's response directly

**Duo mode (persona1+persona2):**
- Spawn both agents in parallel with the same topic
- Present both responses, then add a brief tension/synthesis note

**Full mode:**
- Spawn all 7 agents in parallel with the same topic
- Present each response under a clear header

**Council mode:**
- Spawn all 7 agents in parallel with the same topic
- Present individual responses, then apply the synthesis framework from `synthesis.md`

### Step 3: Context Guidance

When spawning each agent, include this context in the prompt:

```
You are being invoked as part of a product thinking panel. The user needs your perspective on:

[TOPIC]

Respond in your characteristic voice and apply your frameworks. Be opinionated. The user will [also receive other perspectives / use your response directly].
```

For council mode, add:
```
After all panelists respond, I will synthesize your collective perspectives into agreements, tensions, blind spots, and a weighted recommendation. Don't worry about consensus — say what you actually think.
```

## Synthesis Framework (Council Mode)

Consult `synthesis.md` for the complete framework. In brief:

1. **Agreements** — Where 3+ personas align (this is likely correct)
2. **Tensions** — Where they disagree (this is where the interesting decisions live)
3. **Blind spots** — What none of them addressed
4. **Weighted recommendation** — Which perspective to weight most for THIS specific decision, and why

## Error Handling

- If a persona name is ambiguous (e.g., "s" or "t"), ask for clarification
- If the topic is a file path, read the file and include its contents in the agent prompt
- If the topic references an existing document in the workspace, read it first before spawning agents

## Quality Check

Before presenting results:

- [ ] Each persona sounds distinct — not interchangeable
- [ ] Advice is actionable, not just analytical
- [ ] Council synthesis surfaces real tensions, not forced agreement
- [ ] The weighted recommendation is justified (not arbitrary)
