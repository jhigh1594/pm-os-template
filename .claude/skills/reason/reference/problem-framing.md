# Problem Framing Reference

The most valuable thing you can do is reframe the problem. A well-framed problem is half-solved.

## Framing Checklist

```
  ☐ Is this the REAL problem or a symptom?
  ☐ Who experiences it? (Be specific)
  ☐ What happens if we do nothing?
  ☐ What does "solved" look like? (Measurable)
  ☐ What constraints are non-negotiable?
  ☐ What has already been tried?
```

## Cynefin: What Kind of Problem Is This?

```
             ┌──────────────────────┬──────────────────────┐
             │  COMPLEX             │  COMPLICATED         │
             │  Can't predict       │  Experts can solve   │
             │  → Run experiments   │  → Analyze, then     │
             │  → Safe-to-fail      │    best practice     │
             │    probes            │  → Bring experts     │
             │  Ex: Market strategy │  Ex: Scaling infra   │
             ├──────────────────────┼──────────────────────┤
             │  CHAOTIC             │  CLEAR               │
             │  No time to analyze  │  Obvious cause/effect│
             │  → Act NOW           │  → Follow standard   │
             │  → Stabilize first   │    process           │
             │  Ex: Prod is down    │  Ex: Password reset  │
             └──────────────────────┴──────────────────────┘
```

## 5 Whys (Root Cause)

Keep asking "why?" until you hit a structural cause, not a symptom.

```
  Problem: Users churn after week 1
  Why? → They don't complete setup
  Why? → Setup has 12 steps
  Why? → We designed for power users
  Why? → No user research before launch
  Why? → Pressure to ship → ROOT CAUSE
```

## Jobs To Be Done

Focus on progress, not features: what they SAY → what they NEED → simplest solution.

## Phoenix Checklist (CIA)

Systematic reframing: What IS/ISN'T the problem? What assumptions? Who solved similar?
Unlimited resources? Must solve by tomorrow? Total outsider view?
