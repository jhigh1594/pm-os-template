# Visualization Reference

Every response MUST include visual elements.

## Pattern Library

### 2x2 Matrix
Categorize on two dimensions.

```
              HIGH VALUE
                  │
  FILL-INS   ├─────┤ DO FIRST
                  │
              LOW VALUE
     LOW EFFORT       HIGH EFFORT
```

### Funnel
Conversion or process loss at each stage.

```
  100%  ┌──────────────┐
   60%  ├──────────────┤  ← 40% drop here
   30%  ├──────────────┤  ← 30% drop here
   10%  └──────────────┘  ← 20% drop here
```

### Before/After
Show transformation clearly.

```
  BEFORE                AFTER
  ──────────────────────────────
  47 words of           12 words.
  corporate fog.        Clear.
```

### Stack / Layer Diagram
Show architecture or system layers.

```
  ┌─────────────────────────────────┐
  │         Presentation Layer       │
  ├─────────────────────────────────┤
  │         Logic Layer              │
  ├─────────────────────────────────┤
  │         Data Layer               │
  └─────────────────────────────────┘
```

### Decision Record
Structured decisions with rationale.

```
  ┌─────────────────────────────────────────┐
  │  DECISION: [What we decided]            │
  │                                         │
  │  CONTEXT: [Why we needed to decide]     │
  │  OPTIONS: [What we considered]          │
  │  RATIONALE: [Why we chose this]         │
  │  CONSEQUENCES: [What happens next]      │
  └─────────────────────────────────────────┘
```

### Trade-off Triangle
Pick two of three.

```
         FAST
        ╱    ╲
       ╱      ╲
     GOOD ──── CHEAP
```

### Progress Bars
Inline status or magnitude.

```
  Progress:  ████████░░ 80%
  Confidence: ██████░░░░ 60%
  Risk:       ██░░░░░░░░ 20%
```

## Unicode Character Reference

```
  BOXES:   ┌ ┐ └ ┘ ─ │ ├ ┤ ┬ ┴ ┼
  DOUBLE:  ╔ ╗ ╚ ╝ ═ ║
  ARROWS:  → ← ↑ ↓ ▶ ◀ ▲ ▼
  TREES:   ├── └── │
  BLOCKS:  ░ ▓ █
  CHECKS:  ✓ ✗ ☐ ☑
  STARS:   ★ ☆
  MATH:    ± × ÷ ≠ ≤ ≥ ≈
```

## Principles

1. **One visual per concept** — don't overload
2. **Label everything** — unlabeled diagrams are useless
3. **Consistent alignment** — align on meaningful boundaries
4. **Use whitespace** — breathing room improves readability
5. **Progressive detail** — simple overview first, detail on demand
6. **Every character matters** — if it doesn't convey information, remove it
