# AIPMOS Simplification Report
**Date**: 2026-03-30 (revised)
**Type**: System audit — simplification analysis
**Scope**: 58 commands · 57 skills · coaching hooks framework
**Revision note**: v2 incorporated a second-opinion review correcting overstated duplication claims. v3 expands Finding 3 from capture destinations to the full 8-command memory system surface.

---

## Premise

Simplification isn't about making things shorter. It's about making a complex system *elegantly understandable and usable* — fewer choices that are clearer, deeper tools that are better-connected, and a mental model simple enough to hold in one's head without a reference guide.

**The headline finding**: The system has grown by accretion. Each addition was logical in isolation. The aggregate effect is a 58-command, 57-skill system that requires a 1,277-line reference guide to navigate. The simplification opportunity is primarily in **navigation and learning loops**, not in wholesale deletion.

---

## Finding 1: Command/Skill Overlap — One True Duplicate, Two Wrappers, Six Distinct-But-Confusing Pairs

**Severity: High (navigation), Low (deletion)**

*v1 of this report overstated this finding by treating overlap as duplication. A second opinion correctly identified that most commands sharing a name with a skill are serving different jobs. The revised analysis uses three buckets.*

### Bucket A: True Duplicate (delete one copy)

| Command | Skill | Command size | Evidence |
|---|---|---|---|
| `/synthesize` | `synthesize/SKILL.md` | **2,015 lines** | Diff shows cosmetic differences only. Skill adds a 4-question context opener; command jumps straight to the same 3-phase process. Near-identical content loaded into context twice. |

This is the one clear deletion candidate. The skill version is slightly better (consultative opener, clarifying questions before committing to a 2-hour synthesis session).

### Bucket B: True Wrappers (thin or absorb into skill)

| Command | Delegates to | Command size | Added behavior |
|---|---|---|---|
| `/decide` | `decision-quality` skill | 89 lines | Decision journal auto-generation — genuinely valuable, could live in skill |
| `/coach` | `product-coach` skill | 56 lines | Pure delegation, no added behavior |

These two are thin invocation wrappers. `/decide`'s journal step is the one non-trivial addition — that logic should move into the `decision-quality` skill so the wrapper becomes unnecessary.

### Bucket C: Distinct-but-Overlapping (fix routing, not deletion)

| Command | Skill | Why they look alike | Why they're actually different |
|---|---|---|---|
| `/research` | `research` skill | Same name, same domain | Command: argument-driven validation study design (`--opportunity`, `--evidence-confidence`, `--risk`, `--hypothesis`). Skill: consultative evidence-gathering contract. Different jobs: study planning vs. evidence execution. |
| `/competitive-analysis` | `competitive-analysis` skill | Same name, same domain | Command: 5-step landscape scaffold (identify → analyze → matrix → map → recommend). Skill: broader decision-oriented competitive analysis. However, command also overlaps with `/compete` — see Finding 2. |
| `/biz-case` | `business-reasoning` skill | Both do business reasoning | Command: 4-mode structured surface (model, tradeoff, perspective, review) with specific output formats. Skill: underlying frameworks and consultative stance. Command adds meaningful workflow structure. |
| `/price-intel` | `pricing-intelligence` skill | Both do pricing work | Command: 7-step structured pricing intelligence process. Skill: consultative pricing strategy advisor. Both substantive, different entry expectations. |
| `/narrative` | `strategic-storytelling` skill | Both do storytelling | Command: 358-line full framework (Hero's Journey, SCR, Andy Raskin five-act, SCQA). Skill: five-act structure and product-pitch focus. Command is a complete tool, not a wrapper. |
| `/compete` | `competitive-analysis` skill | Same domain | Command: battlecard mode (`--output battlecard`), focus competitor mode (`--focus`), win/loss integration, signal routing. Distinct from skill's decision-oriented analysis. |

**The real problem**: These pairs create *discoverability confusion* — not redundancy. A user asking "I need competitive analysis" faces `/compete`, `/competitive-analysis`, and the `competitive-analysis` skill, and doesn't know which to use. The fix is better routing and onboarding — making it clear when to use each — not deletion.

**Recommendation**:
- **Bucket A**: Delete `/synthesize` command; keep the skill as single source of truth
- **Bucket B**: Move `/decide`'s journal step into `decision-quality` skill. Delete both wrapper commands.
- **Bucket C**: Add clearer routing in COMMAND-REFERENCE — a decision tree or "if you're doing X, use Y" table. Consider whether `/competitive-analysis` command is sufficiently distinct from `/compete` to justify both (see Finding 2).

---

## Finding 2: The Intelligence Cluster Has a Discovery Problem

**Severity: Medium-High**

*v1 recommended aggressive consolidation (6→3 commands). A second opinion correctly identified that the current commands serve distinct jobs along meaningful dimensions: artifact type, cadence, and source discipline. The revised recommendation simplifies entry and routing rather than merging.*

Six commands cover competitive and market intelligence:

| Command | Job | Dimension |
|---|---|---|
| `/compete` | Deep analysis on known competitor + battlecards | Artifact (battlecard, deep-dive) |
| `/competitive-analysis` | Broad landscape scan across competitors | Artifact (comparison matrix, positioning map) |
| `/win-loss` | Deal outcome root cause extraction | Source (sales deals) |
| `/price-intel` | Pricing-specific intelligence | Discipline (pricing) |
| `/daily-brief` | Automated daily monitoring digest | Cadence (daily) |
| `/industry-brief` | Analyst/market/earnings/job signals | Discipline (market forces) |

These are genuinely different jobs. However, two specific overlaps create confusion:

1. **`/competitive-analysis` vs `/compete`**: Both do competitive analysis. The distinction (landscape scan vs. deep-dive) is real but non-obvious. They share near-identical source hierarchy text. `/competitive-analysis` even ends by offering to route to `/compete` for battlecards — suggesting it knows it's upstream of the same job.

2. **`/industry-brief` vs `/daily-brief --industry`**: The `--industry` flag on `/daily-brief` already does a version of what `/industry-brief` does, with `/industry-brief` going deeper. This is a depth distinction, not a job distinction.

**Recommendation**:
- **Retire** `/competitive-analysis` command. Its landscape-scan job can be handled by `/compete` with a `--mode landscape` flag or by directing the user to invoke the `competitive-analysis` skill for that workflow. One command for "I need competitive intel" is clearer than two.
- **Evaluate** whether `/industry-brief` should become `/daily-brief --mode deep` rather than a standalone command. The cadence dimension should route to one command with depth options.
- **Keep** `/compete`, `/win-loss`, `/price-intel`, `/daily-brief` — these serve distinct enough jobs.
- **Improve routing**: Add an intelligence entry map to COMMAND-REFERENCE and `/onboard`:

```
I need to...
  ...monitor what's happening daily       → /daily-brief
  ...understand a specific competitor     → /compete [--focus name]
  ...generate a sales battlecard          → /compete --output battlecard
  ...analyze a deal we won or lost        → /win-loss
  ...research competitor pricing          → /price-intel
  ...scan market/analyst/earnings trends  → /daily-brief --industry (quick) or /industry-brief (deep)
```

---

## Finding 3: The Memory System Uses 8 Commands for 3 Jobs

**Severity: High**

*v1 focused narrowly on capture destinations. v3 expands to cover the full memory command surface: 8 commands serving 3 distinct jobs (capture, maintain, recall) with meaningful overlap within each job.*

### The full memory command inventory

| Command | Lines | Job | Writes to | Frequency |
|---|---|---|---|---|
| `/signal` | 251 | Capture | `signals-YYYY-MM.md` | Per-occurrence |
| `/capture-pattern` | 205 | Capture | `learned-patterns.md` | When noticed |
| `/refresh-memory` | 117 | Maintain | `memory.md` | Per-session |
| `/check-progress` | 131 | Maintain | (diagnostic — reads, doesn't write) | Ad hoc |
| `/memory-audit` | 18 | Maintain | (diagnostic — reads, doesn't write) | Monthly |
| `/learn-sessions` | 43 | Maintain | `learned-patterns.md` | Weekly |
| `/persona-sync` | 232 | Maintain | `Knowledge/People/*.md` | Monthly |
| `/remember` | 127 | Recall | (reads, doesn't write) | Ad hoc |

Plus: quality gates in 10 analytical commands offer to write to `growth-signals-YYYY-MM.md` (y/n opt-in).

**Total**: 1,124 lines of command definitions · 5 write destinations · 3 distinct jobs.

### Where the overlap lives

**Overlap 1: `/learn-sessions` and `/capture-pattern` both write to `learned-patterns.md`**

`/capture-pattern` captures a pattern in real-time from the current session (interactive: asks type, details, quality gates). `/learn-sessions` batch-extracts patterns from recent `.specstory/history/` sessions using the same 4-gate quality filter. Same destination, same quality bar, different timing. A user who runs `/learn-sessions` weekly may surface the same patterns they could have captured live with `/capture-pattern` — or miss them entirely because session transcripts lack the in-the-moment context.

**Overlap 2: `/check-progress` and `/memory-audit` are both "is my memory healthy?"**

`/check-progress` shows deltas — git commits, modified files, and memory file freshness since the last update. `/memory-audit` runs a Python health checker for TTL violations, line count warnings, and structural issues. Both answer "should I update my memory system?" but through different lenses (activity delta vs. structural health). In practice, a user who wants to know "is my memory stale?" runs one and gets told to run the other.

**Overlap 3: `/signal` and `/capture-pattern` are both "I noticed something important, save it"**

`/signal` captures customer-facing evidence (with source type, ICP fit, strength). `/capture-pattern` captures workspace-internal learning (with type, quality gates, confidence level). The distinction is real (external signal vs internal pattern), but in the moment of noticing something important, the user faces a routing decision: "Is this a signal or a pattern?" Some insights are both — a customer interaction that reveals a workspace convention.

### What the memory system looks like to a user

A PM who wants to "keep their knowledge system working" today needs to:
- Know 8 commands (or at least recognize when to use each)
- Understand 5 write destinations and which command writes where
- Run a maintenance cadence: `/refresh-memory` per session, `/learn-sessions` weekly, `/persona-sync` monthly, `/memory-audit` monthly, `/check-progress` ad hoc
- Handle quality gate y/n prompts at the end of 10 analytical sessions

That's substantial cognitive overhead for a system whose purpose is to *reduce* cognitive load.

### Recommendations

**A. Merge the two diagnostics** — `/check-progress` and `/memory-audit` → one command (call it `/memory-health` or fold delta-checking into `/memory-audit`). The user asks "is my memory system healthy?" and gets both the activity delta AND the structural health check in one output.

**B. Absorb `/learn-sessions` into `/capture-pattern`** — Add a `--from-sessions [days]` flag to `/capture-pattern` that does the batch extraction job. One command for "add to learned-patterns.md" with two modes: real-time capture (default) and batch extraction (flag). Reduces two commands to one.

**C. Consider a unified capture entry** — A `/log` command that routes based on content type: customer insight → `/signal` behavior, workspace learning → `/capture-pattern` behavior, session state → `/refresh-memory` behavior. The user says "log this: [content]" and the system classifies. This doesn't replace the specialized commands (power users can still invoke `/signal` directly), but it reduces the routing burden for the common case.

**D. Evaluate whether `/refresh-memory` should be automatic** — If memory.md updates happened as a session-end hook rather than a manual command invocation, that removes one command from the user's maintenance burden. The `memory_updater.py` script already exists — the question is whether it should be triggered by a hook rather than a slash command.

**E. `/persona-sync` and `/remember` stay as-is** — Both are distinct enough in job-to-be-done. `/persona-sync` is a monthly cadence tool with clear specialized behavior (evidence thresholds, persona hypothesis model). `/remember` is the only recall tool.

**Net result**: 8 commands → 5 commands (or 4 if `/refresh-memory` becomes a hook):
- `/log` or `/signal` + `/capture-pattern` (capture — unified or kept as two with clear routing)
- `/refresh-memory` (maintain session state — or automatic hook)
- `/memory-health` (maintain system health — merged diagnostic)
- `/persona-sync` (maintain personas — monthly cadence)
- `/remember` (recall past conversations)

---

## Finding 4: The Research Cluster Has Murky Boundaries

**Severity: Medium**

*v1 recommended absorbing `/research` into `/discover`. A second opinion correctly identifies that `/research` has a distinct argument-driven validation-study design workflow that is meaningfully different from the `research` skill's consultative evidence-gathering. The revised analysis narrows the boundary problem to the skill layer.*

Five tools cover research and discovery:

| Tool | Type | Distinct job |
|---|---|---|
| `/discover` | Command | 4-phase structured discovery workflow with evidence gates |
| `/research` | Command | Validation study design with `--opportunity`, `--risk`, `--hypothesis` flags |
| `research` skill | Skill | Consultative evidence-gathering (web research, source synthesis) |
| `discovery` skill | Skill | "What to learn next" method selection advisor |
| `continuous-discovery` skill | Skill | Teresa Torres cadence methodology |

The command pair (`/discover` and `/research`) has a clear handoff: `/discover` → Phase 2 evidence gate fails → `/research` designs the study → study runs → signals feed back to `/synthesize`. This is well-architected.

**The real boundary problem** is between the `discovery` skill and `/discover` command — both answer "how do I do discovery?" but at different levels (method advisor vs. full workflow). A user in chat doesn't know whether to invoke the skill or run the command.

**Recommendation**: Clarify that `/discover` is the *workflow* (structured, phased, argument-driven) and the `discovery` skill is the *advisor* (conversational, "which method should I use next?"). Add this distinction to COMMAND-REFERENCE. Consider renaming the skill to `discovery-advisor` for disambiguation.

---

## Finding 5: The Prep/Product Knowledge Cluster Requires Hidden Sequencing Knowledge

**Severity: Medium**

Three commands form a demo and meeting preparation cluster:

```
/prep         → meeting prep (strategic layer)
/demo-prep    → customer-ready demo guide
/product-depth → build product expertise (upstream of /demo-prep)
```

Well-designed individually. The correct sequence (`/product-depth --mode changelog` → `/demo-prep` → `/prep`) is hidden from the user — documented in each command's Relationship section but invisible during invocation. A user who runs `/demo-prep` without `/product-depth` first gets a guide built on potentially stale product knowledge.

**Recommendation**: `/demo-prep` should automatically invoke `/product-depth --mode changelog` as a first step when product context is stale (>30 days old), rather than requiring the user to sequence it manually.

---

## Finding 6: `/prioritize` Is Doing Two Different Jobs

**Severity: Medium**

`/prioritize` at 612 lines has "Adaptive Workflow Detection" running two fundamentally different processes:

- **Clean List Mode**: skip to framework, prioritize directly (~15 min)
- **Raw Feedback Mode (Triage)**: intake, normalize, categorize, then prioritize (~2+ hours)

Different session lengths, inputs, outputs, and rigor levels — unified only because both involve the word "prioritization." The COMMAND-REFERENCE acknowledges this with a **Dual-Mode Note** directing complex cases to `prioritization-craft` skill.

**Recommendation**: `/prioritize` handles clean-list scoring only. `prioritization-craft` skill handles triage and complex sequencing. Remove Raw Feedback Mode from `/prioritize` entirely — the "smart detection" creates the illusion these are one job.

---

## Finding 7: The Quality Gate Opt-In Creates an Inconsistent Coaching System

**Severity: Medium**

The coaching hooks framework (10 commands with quality gates) fires a reflective prompt at the commit point, ending with:

> "Save this response to `📚 Knowledge/Growth/growth-signals-[YYYY-MM].md`? [y/n]"

Three problems:

1. **Selection bias**: Signals captured are the ones you felt good about, not the ones revealing failure modes.

2. **Friction at the wrong moment**: Gate fires when you want to be done, not when you're in learning mode.

3. **Month-by-month reset**: `/weekly-review` only reads the *current* month's growth signals file. A consistent blind spot across six months would never be surfaced. The longitudinal coaching loop is architecturally broken.

**Recommendation**: Auto-save growth signals (remove the y/n prompt), tag with confidence level (`surfaced | reflected | challenged`). Add a `/growth-review` command reading the last 3 months to identify repeating pattern tags — this closes the longitudinal loop.

---

## Finding 8: The 58-Command Flat Namespace Creates Discovery Overhead

**Severity: Medium**

58 commands exceeds working memory (7±2). The system requires its 1,277-line reference guide as a *primary navigation tool*, not an edge-case manual.

Low-frequency commands that clutter the daily namespace:
- `/bug-report`, `/learning-opportunity`, `/persona-sync`, `/check-progress`, `/memory-audit`, `/prototype`, `/ui-refine`

These are legitimate but share a flat namespace with daily drivers (`/today`, `/think`, `/granola`). No visual hierarchy — all 58 appear equivalent.

**Recommendation**: Organize into visible tiers — **daily** (7-10), **situational** (15-20), **specialty** (the rest). Surface the tier structure in `/onboard` and `/today`.

---

## Finding 9: `/critique` Is a Skill Misclassified as a Command

**Severity: Low-Medium**

`/critique` at 269 lines contains a 7-dimension framework, 4 modes, and 3 sub-frameworks. This is a skill's worth of content in a command file. The right pattern is `/coach` → `product-coach` skill: thin wrapper, rich skill.

**Recommendation**: Move framework content into `critique/SKILL.md`. Keep thin `/critique` command as invocation wrapper.

---

## Finding 10: The Lifecycle Table Is an Underused Asset

**Severity: Observation — Highest Leverage**

The Idea-to-Delivery lifecycle table (9 steps, each with command → produces → carries into) is the clearest mental model in the system. It answers "what do I use next?" better than any amount of NOT FOR clauses.

It lives at line 971 of COMMAND-REFERENCE.md. A user encounters 57 commands before seeing the model that explains how they connect.

**Recommendation**: The lifecycle table should be the *primary entry point*. Surface it in `/today` ("You have a PRD at Step 4 — next is `/design-brief`"). Make it the opening frame of `/onboard`. This is probably the highest-leverage simplification move in the entire system.

---

## Revised Simplification Scorecard

| Finding | Impact | Effort | Action Type | Recommendation |
|---|---|---|---|---|
| `/synthesize` true duplicate | High | Low | **Delete** | Remove command; skill is single source |
| `/decide`, `/coach` wrappers | Medium | Low | **Absorb** | Move journal step to skill; delete wrappers |
| 6 distinct-but-confusing Bucket C pairs | Medium | Low | **Route** | Decision tree in COMMAND-REFERENCE; no deletion |
| Intel cluster discovery problem | Medium-High | Low-Medium | **Retire 1 + Route** | Retire `/competitive-analysis`; add intel routing map |
| Memory system: 8 commands for 3 jobs | High | Medium | **Merge + Route** | Merge 2 diagnostics, absorb `/learn-sessions`, consider `/log` router, evaluate `/refresh-memory` as hook |
| Research/discovery skill boundary | Medium | Low | **Rename + Document** | Rename `discovery` skill; clarify in COMMAND-REFERENCE |
| `/prioritize` two-job problem | Medium | Low | **Split** | Remove raw feedback mode; skill handles triage |
| Quality gate opt-in bias | Medium | Low | **Auto-save** | Remove y/n; add `/growth-review` for longitudinal loop |
| 58-command flat namespace | Medium | Medium | **Tier** | Daily/situational/specialty visible tiers |
| `/critique` misclassified | Low-Medium | Low | **Refactor** | Content → skill; thin wrapper stays |
| Lifecycle table buried | High leverage | Low | **Elevate** | Surface in `/today` and `/onboard` |

---

## Target State

The refined target state preserves all capability while reducing cognitive load:

- **~45-50 commands** (down from 58 after removing 1 duplicate, 2 wrappers, 1 retired command, and a few specialty commands absorbed into modes)
- **Tiered visibility**: daily (8-10), situational (18-22), specialty (10-15)
- **Clear routing maps** for overlapping domains (intel, research/discovery, knowledge capture)
- **Lifecycle table as primary navigation** — surfaced in daily workflow, not buried in documentation
- **Auto-captured growth signals** with cross-month synthesis via `/growth-review`
- **Each command-skill pair clearly documented** with "when to use command vs skill" distinction

---

## Root Cause (unchanged)

The system evolved by addition, not by architecture. When a new capability was needed, a new command or skill was added without a pruning pass or consolidation review.

The correction from v1: the fix is primarily *routing and navigation*, not *deletion*. Most overlapping commands exist because they serve distinct but adjacent jobs. The user's confusion isn't "these do the same thing" — it's "I don't know which one to use when." That's a routing problem, not a duplication problem.

**The three highest-leverage moves:**
1. **Elevate the lifecycle table** to primary navigation (Finding 10)
2. **Add routing maps** for overlapping domains (Findings 1C, 2, 4)
3. **Auto-save growth signals** with longitudinal synthesis (Finding 7)

These three changes would make the system significantly more navigable without removing any capability.

---

## Appendix: What Changed in v2

| Section | v1 claim | v2 correction | Source |
|---|---|---|---|
| Finding 1 | 3 exact duplicates, 6 thin wrappers | 1 true duplicate, 2 wrappers, 6 distinct pairs | Second opinion: verified `/research`, `/narrative`, `/biz-case` are substantive |
| Finding 2 | Consolidate 6→3 intel commands | Retire 1 (`/competitive-analysis`), improve routing for rest | Second opinion: current commands serve distinct artifact/cadence/discipline dimensions |
| Finding 3 | 8 knowledge capture destinations (v1) → 5-6 destinations (v2) | 8 memory commands serving 3 jobs with specific overlaps (v3) | User identified full memory command surface; expanded from destinations to command inventory |
| Scope line | 65+ skills | 57 skills (precise count of SKILL.md files under .claude/skills/) | Second opinion: inventory count corrected |
| Target state | ~30 commands | ~45-50 commands with tiered visibility | Follows from corrected duplication analysis |

---

*Generated: 2026-03-30 | Revised: 2026-03-30 | Input: full audit of .claude/commands/ (58 files, 14,638 lines) + .claude/skills/ (57 SKILL.md files, 11,301 lines) + COMMAND-REFERENCE.md + second-opinion review*
