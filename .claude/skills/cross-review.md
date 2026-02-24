# Cross-Review: AI×AI Peer Review

**What this is:** Pattern for having different AI models review each other's work

## Workflow

1. **Primary AI** (Claude) creates content
2. **Reviewer AI** (different model) provides feedback
3. **Mediator** (human or Primary AI) evaluates findings:
   - Verify each issue actually exists
   - Assess severity
   - Decide what to act on

## Key Principle

**Don't accept findings blindly.** The reviewer has less context. Verify each issue before acting.

## Usage

```
/cross-review [file-to-review]
```

## Example

```
You: "Create a PRD for feature X"
Claude: [produces PRD]

You: "/cross-review that PRD using GPT-4"
System: [GPT-4 reviews PRD]

You: "Evaluate findings"
System: "Of 12 findings:
- 8 valid (3 critical, 3 medium, 2 low)
- 4 invalid (already handled, misunderstood requirement)"
```

## When to Use

- **Pre-completion**: Get fresh eyes before finalizing
- **Critical decisions**: Validate important work
- **Learning**: Understand different model perspectives

## When NOT to Use

- Quick iterations (adds overhead)
- Well-understood patterns
- Time-sensitive decisions

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0.0 | 2026-02-09 | Initial cross-review pattern |
