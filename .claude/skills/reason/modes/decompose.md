# Mode: Decompose

Break any complex problem into MECE parts using issue trees.

**Load reference:** `problem-framing.md` and `visualization.md`

## Workflow

### 1. Root question
Transform user input into a single clear question.

### 2. MECE tree

```
  [Root question]
  ├── [Branch 1]
  │   ├── [Sub-branch 1a]
  │   └── [Sub-branch 1b]
  ├── [Branch 2]
  └── [Branch 3]
```

### 3. Verify MECE

```
  ☑ Mutually Exclusive: No overlap between branches
  ☑ Collectively Exhaustive: Every possibility covered
```

### 4. Prioritize

```
  Branch 1 [desc]  ████████████  HIGH  ← Start here
  Branch 2 [desc]  ████████░░░░  MED
  Branch 3 [desc]  ████░░░░░░░░  LOW   ← Defer
```

### 5. Actionable output
Workstreams with owners and first steps.

**Go 2-3 levels deep max.** Deeper = guessing.
