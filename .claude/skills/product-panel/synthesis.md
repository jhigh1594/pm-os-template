# Multi-Persona Synthesis Framework

When running in council mode (all 7 personas), synthesize their individual responses using this framework.

## Step 1: Surface Agreements

Where do 3+ personas converge? These are high-confidence signals.

Format:
```
### Where the Panel Agrees
- [Agreement 1] — [which personas agree and why]
- [Agreement 2] — [which personas agree and why]
```

Agreements are powerful because these thinkers approach from fundamentally different angles. When a systems thinker (Tobi) and an experience designer (Brian) agree on something, it's worth paying attention to.

## Step 2: Surface Tensions

Where do they disagree? These are the interesting decisions.

Format:
```
### Where the Panel Disagrees
- **[Tension 1]:** [Persona A] says X because [reason]. [Persona B] says Y because [reason].
  - The real question here: [what this tension is actually about]
```

Tensions aren't problems to resolve — they're decision points. The panel surfaces them; the user decides which perspective to weight.

## Step 3: Identify Blind Spots

What did none of them address?

Format:
```
### What Nobody Caught
- [Blind spot 1] — relevant because [why]
```

This often reveals assumptions so deeply held that none of the personas questioned them, or gaps in the topic description itself.

## Step 4: Weighted Recommendation

Which perspective matters most for THIS specific decision?

Format:
```
### Weighted Recommendation

For this specific decision, weight **[persona]**'s perspective most heavily.

**Why:** [context-dependent reasoning — not always the same persona]

**But also consider:** [secondary perspective and why]
```

The weighting depends on context:
- **Scope/prioritization decisions** → Weight Shreyas
- **Architecture/platform decisions** → Weight Tobi
- **Speed/clarity decisions** → Weight Patrick
- **Design/UX decisions** → Weight Jony
- **Customer/experience decisions** → Weight Brian
- **Growth/monetization/retention decisions** → Weight Growth
- **Execution/operations/management decisions** → Weight Grove
- **Strategic risk/inflection point decisions** → Weight Grove
- **Multi-dimensional decisions** → Weight the persona whose domain is most at risk

## Anti-Patterns

Avoid:
- **Forced consensus** — don't smooth over real disagreements
- **Equal weighting** — not every perspective is equally relevant to every decision
- **Synthesis that loses voice** — the synthesis should be clear about WHO thinks WHAT
- **Generic recommendations** — "it depends" is not a weighted recommendation
