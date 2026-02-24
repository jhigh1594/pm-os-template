# Template Finder

**What this does:** Routes you to the right template/framework based on what you're trying to create.

## Usage

```
/templates [what you want to create]
```

## Common Templates

| I want to... | Use this | Location |
|--------------|----------|----------|
| Write a PRD | `/spec` or `ai-prd.md` | `.claude/commands/` |
| Prioritize work | `/prioritize` or `prioritization-craft` | `.claude/commands/` |
| Daily planning | `/today` | `.claude/commands/` |
| Strategic analysis | `/think` | `.claude/commands/think.md` |
| Brainstorm features | `/brainstorm` | `.claude/commands/` |
| Customer discovery | `/discover` | `.claude/commands/` |
| Synthesize feedback | `/synthesize` | `.claude/commands/` |
| Product critique | `/critique` | `.claude/commands/` |
| Competitive analysis | `/compete` | `.claude/commands/` |
| Stakeholder alignment | `/align` | `.claude/commands/` |
| Strategic narrative | `/narrative` | `.claude/commands/` |
| Launch planning | `/ship` | `.claude/commands/` |
| Executive communication | `/write` | `.claude/commands/` |
| Metrics & measurement | `/measure` | `.claude/commands/` |
| Decision making | `/decide` | `.claude/commands/` |

## How Templates Work

1. **Preflight:** For complex docs (PRD, Strategy), answer 2-3 clarifying questions first
2. **Framework:** Apply structured thinking approach
3. **Template:** Fill in artifact with informed content
4. **Review:** Quality check before finalizing

## Mode Parameters

Some commands support mode modifiers:

```bash
/think --mode=explore    # Curious, open-ended (default)
/think --mode=challenge  # Skeptical, pushback-heavy
/think --mode=verify     # "Check my thinking" validation
```

---

**What are you trying to create?**
