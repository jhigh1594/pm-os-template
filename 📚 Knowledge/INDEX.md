# Knowledge Index

_Router for domain-specific context. Load only the folder(s) relevant to your current task._

---

## Domain Map

| Folder | What's here | Load when... |
|--------|-------------|--------------|
| [Customers/](Customers/) | Customer account research, strategy docs | Account-specific work, customer narrative, QBR prep |
| [Market/](Market/) | Competitive landscape, market frameworks, analyst content | Competitive analysis, positioning, market research |
| [Growth/](Growth/) | Growth signals log, coaching quality gate responses | Growth strategy, usage metrics, retention decisions |
| [People/](People/) | Stakeholder profiles — start from `People/_template.md` | Preparing for conversations, navigating relationships, exec alignment |
| [Frameworks/](Frameworks/) | Product frameworks (AI risk, etc.) | AI feature work, risk assessment, framework selection |
| [Writing-Styles/](Writing-Styles/) | Voice guides per audience (exec, customer, sales, board) | Writing any external or internal communication |
| [Research/](Research/) | Research reports and studies | Validating product decisions, backing claims |
| [Templates/](Templates/) | Reusable doc templates (battlecard, etc.) | Starting competitive or strategic docs |
| [Systems-and-Processes/](Systems-and-Processes/) | Process improvement plans | Workflow changes, operating model work |
| [Patterns/](Patterns/) | Confirmed PM domain patterns worth reusing | Identifying recurring product problems or solutions |
| [Learning/](Learning/) | Learning captures and skill development notes | Skill-building sessions, retrospectives |
| [Thinking/](Thinking/) | Working notes, reasoning artifacts | Complex problem decomposition, strategic thinking |
| [decisions/](decisions/) | Product decision journal | Making or revisiting a significant product decision |

---

## Hypothesis Tracker

Active unvalidated beliefs, by domain. Promote to `🤖 AI/patterns/learned-patterns.md` when confirmed 3+ times.

- [Growth/hypotheses.md](Growth/hypotheses.md)
- [Market/hypotheses.md](Market/hypotheses.md)

---

## How this system works

1. **Load on demand** — read this INDEX first, then load only relevant domain folders (don't preload all)
2. **Hypothesis lifecycle**: unvalidated belief → `hypotheses.md` → confirmed 3x → `🤖 AI/patterns/learned-patterns.md`
3. **Pattern promotion**: when a hypothesis reaches 3 confirmations, apply the 4 quality gates (Actionable, Specific, Durable, Non-obvious) before promoting

---

## Cross-Reference Convention

When adding any new Knowledge file, include a footer:

```markdown
---
**Cross-references:** [related-file.md](path) · [related-file.md](path)
**Confirms hypothesis:** [hypothesis name from hypotheses.md]
**Feeds decision:** [decision or initiative name]
```

---

## Lint Prompt (run weekly or after major research additions)

Run this as a Claude prompt over the knowledge system:

```
Lint pass on 📚 Knowledge/ and 🤖 AI/memory/:
1. List any hypothesis in hypotheses.md not touched in 30+ days — promote, kill, or extend
2. List files referenced in INDEX.md with no corresponding file
3. List files that exist but are not in INDEX.md
4. Flag any fact stated identically across 3+ files (duplication signal)
5. Check the 5 most-referenced strategic claims — do they have a source attribution?
6. Check candidate-patterns.md for PENDING entries older than 14 days — flag for review
```
