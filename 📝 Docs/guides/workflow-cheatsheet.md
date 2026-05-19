# PM-OS workflow cheatsheet

Human-readable entry points for common PM activities. This is a **curated map**, not a full command list. For every slash command, triggers, and “when not to use,” see the [command reference](../../.claude/commands/COMMAND-REFERENCE.md).

**When the right starting point is unclear:** use `/templates`, or skim the [Quick Reference Table](../../.claude/commands/COMMAND-REFERENCE.md#quick-reference-table) in the command reference.

---

## Feature and initiative spine (idea → delivery)

Canonical lifecycle. Each step hands context to the next; initiative state lives under `📦 Products/{product}/initiatives/{feature-slug}/`.

| Step | Command | Produces | Typical next step |
|------|---------|----------|-------------------|
| 1. Ideation | `/brainstorm` | Problem statement, key angles | `/discover` |
| 2. Discovery | `/discover` | Validated opportunity statement, SOM sizing | `/spec --type one-pager` |
| 3. One-pager | `/spec --type one-pager` | Solution hypothesis, stakeholder draft | `/spec --type full` |
| 4. PRD | `/spec --type full` | Approved PRD: capabilities, metrics, risks, personas | `/design-brief` and `/story` |
| 5. Design brief | `/design-brief` | Seven-section brief, screen inventory | Designer kickoff |
| 6. Story breakdown | `/story` | Epic / feature / stories with acceptance criteria | `/spec-brief` |
| 7. Dev handoff | `/spec-brief` | Gherkin ACs, data model, API contract | `/ship` |
| 8. Launch | `/ship` | Launch plan, comms, metrics baseline | `/learn` |
| 9. Learning | `/learn` | Iteration priorities, validated evidence | `/brainstorm` or `/spec` |

**Entry points:** No need to start at step 1—inspect existing artifacts in the initiative folder to see where work left off. If `story-breakdown.md` exists without `design-brief.md`, order may be off. `SPEC_BRIEF.md` indicates dev handoff is in place.

---

## Activity → start here (curated)

| Activity | Start with | Go deeper (skill) |
|----------|------------|-------------------|
| **Daily** | | |
| Plan the day, priorities, blockers | `/today` | — |
| End-of-week PM review | `/weekly-review` | — |
| Triage in-flight initiatives, sprint risk | `/deliver` | — |
| **Discovery and research** | | |
| Research customer needs | `/discover` | continuous-discovery |
| External discovery, buying committee | `/discover --mode external` | — |
| Validate an assumption | `/research` | — |
| Log a customer signal | `/signal` | — |
| Extract meeting notes | `/granola` | synthesize |
| Find patterns in lots of feedback | synthesize skill | prioritization-craft |
| Audit customer knowledge gaps | `/customer-knowledge-audit` | — |
| Refresh personas from signals | `/persona-sync` | — |
| **Spec, design, and engineering handoff** | | |
| Write or extend a spec | `/spec` | See [SKILLS-INDEX](../../.claude/skills/SKILLS-INDEX.md) for PRD/spec skills |
| Design brief from PRD | `/design-brief` | — |
| Break PRD into stories | `/story` | — |
| Engineering handoff / Gherkin / contracts | `/spec-brief` | — |
| Static mockup | `/mockup` | design-first-dev |
| Interactive prototype | `/prototype` | — |
| Polish UI to a high bar | `/ui-refine` | — |
| Critique a design | `/critique` | — |
| **Stakeholder communication** | | |
| Alignment and buy-in | `/align` | stakeholder-craft |
| Executive brief or narrative doc | `/write` | exec-comms |
| Exec update | `/write --type exec` | — |
| Structured ask to a stakeholder | `/write --type ask` | — |
| Post-meeting follow-up | `/follow-up` | — |
| Prep for a specific meeting | `/prep` | — |
| Champion briefing before exec review | `/prep` (champion mode) | — |
| Strategic narrative | `/narrative` | strategic-storytelling |
| Business case / cross-functional pushback | `/biz-case` | — |
| Package analysis for leadership or sales | `/data-story` | — |
| **Competitive and market intelligence** | | |
| Daily market pulse | `/ci-brief` | — |
| Deep competitor or battlecard | `/compete` | competitive-analysis |
| Win / loss on a deal | `/win-loss` | — |
| Pricing research | `/price-intel` | pricing-intelligence |
| Analyst / industry scan | `/industry-brief` | — |
| **Strategy, roadmap, prioritization** | | |
| OKRs, positioning, strategic tradeoffs | `/think` | strategic-thinking |
| Two-way door vs one-way door decisions | `/think` | decision-quality |
| Roadmap document | `/roadmap` | — |
| Quick scoring of a short list | `/prioritize` | — |
| Heavy triage, constraints, stakeholder comms | prioritization-craft skill | — |
| **Launch and post-launch** | | |
| Launch plan and comms | `/ship` | launch-execution |
| Sales enablement, launch tiers | `/launch` | — |
| Post-launch learning | `/learn` | — |
| **Product fluency and demos** | | |
| Deep product context (demo, changelog, confusion) | `/product-depth` | — |
| Demo guide for a specific audience | `/demo-prep` | — |
| **Workspace and memory** | | |
| First-time workspace setup | `/onboard` | — (optional Granola LaunchAgent on macOS) |
| Persist session context | `/refresh-memory` | — |
| Search prior conversations | `/remember` | — |
| Capture a durable decision pattern | `/capture-pattern` | — |
| AI toolchain / hooks / skills audit | `/dex-improve` | — |
| Structured learning on a topic | `/learning-opportunity` | — |
| Report a tooling bug | `/bug-report` | — |

More phrase → command rows: [Quick Reference Table](../../.claude/commands/COMMAND-REFERENCE.md#quick-reference-table).

**Intelligence routing (competitive / market):**

| Need | Use |
|------|-----|
| Ongoing market awareness | `/ci-brief` |
| Specific competitor or battlecard | `/compete` |
| Deal win or loss analysis | `/win-loss` |
| Pricing | `/price-intel` |
| Broader analyst / industry scan | `/ci-brief --industry` or `/industry-brief` |

Rule of thumb: start with `/ci-brief` for cadence; escalate to `/compete` for depth. Run `/win-loss` after deal outcomes.

---

## Cadence workflows (`/workflow`)

Repeatable playbooks live under `📁 Workflows/[name]/` (see [Workflows README](../../📁 Workflows/README.md)). When a folder contains `CLAUDE.md` and `workflow.md`, run **`/workflow`** and point the assistant at that path (for example `@📁 Workflows/qpr-prep/`).

Until a folder is fully populated, use the **substitute commands** below.

| Workflow | Folder | Substitute commands | Cadence |
|----------|--------|---------------------|---------|
| Metrics health check | `metrics-health-check` (when present) | `/measure` + `b2b-data-analyst` skill | Weekly |
| QPR prep | `qpr-prep` | `/think --mode okr`, `/roadmap`, `/write --type exec` | Quarterly |
| Weekly stakeholder update | `weekly-stakeholder-update` | `/write --type announcement` | Weekly |
| Customer research synthesis | `customer-research-synthesis` | `/granola` + `synthesize` skill | Ongoing |

---

## Skill bundles (natural-language hints)

Telling the assistant the work mode often activates overlapping skills. Examples below use skill folders **present in this repo’s** `.claude/skills/`; the full catalog (including optional installs) is [SKILLS-INDEX.md](../../.claude/skills/SKILLS-INDEX.md).

| Working on | Typical skills (installed here) |
|------------|----------------------------------|
| New AI feature | `zero-to-launch`, `discovery`, `ai-product-patterns`, `strategic-build` |
| Executive presentation | `exec-comms`, `strategic-storytelling` |
| Roadmap prioritization | `prioritization-craft`, `decision-frameworks` |
| Learning loops / PMF-style measurement | `metrics-frameworks`, `exp-driven-dev`, `opportunity-solution-tree` |
| Stakeholder tension | `stakeholder-craft`, `stakeholder-management` |
| New product launch | `launch-execution`, `positioning-craft`, `growth-embedded` |
| Career / operating style | `managing-up`, `strategic-thinking` |

Narrative “how skills stack” (may name skills not yet installed): [.claude/skills/README.md](../../.claude/skills/README.md).

---

## Commands vs skills

Some areas offer a **fast slash command** and a **deeper skill** for the same theme:

- **`/prioritize`** (quick scoring) vs **`prioritization-craft`** (outcomes, constraints, stakeholder-heavy triage).
- **`/think`** (quick strategic framing) vs **`strategic-thinking`** (consultative, expandable for high-stakes decisions).

Use the command for speed; ask for the skill by name when the problem needs more structure.

---

## Related links

| Doc | Purpose |
|-----|---------|
| [COMMAND-REFERENCE.md](../../.claude/commands/COMMAND-REFERENCE.md) | Full intent map, per-command guidance |
| [SKILLS-INDEX.md](../../.claude/skills/SKILLS-INDEX.md) | Installable skills list |
| [📁 Workflows/README.md](../../📁 Workflows/README.md) | Workflow folder conventions |
