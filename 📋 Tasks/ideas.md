# Ideas inbox

Capture **new ideas** here before they become backlog items. Triage in weekly review: promote, park, or kill.

## Status key

- **Inbox** — Raw capture, not evaluated
- **Considering** — Worth a conversation or spike
- **Parked** — Good idea, wrong time — add trigger to revisit
- **Promoted** — Moved to `backlog.md` or `this-week.md` — link the item

---

## Inbox

- Build out a pre-mortem/thought experiment skill — captured 2026-04-03
- a library of product demos/snippets for CSMs. Also, how could we automatically generate new product release demos for CSMs to send out to customers
- Internal tools for automatic release notes, newsletter, and change management
- For context I posted about giving Claude Code permanent memory with SQLite months ago. Since then I've added compaction hooks, a launcher for resuming sessions, and project-level config files. Each layer solves a different failure mode. Hooks keep the active session alive. The database keeps long term recall. The config keeps rules loaded. The thread keeps taste. Stack all four and the AI actually remembers. Everyone using Claude Code has the same anxiety. You're deep in a session, context fills up, compaction fires, and suddenly it forgets the plan, the decisions, and the things you already rejected. You spend 20 minutes re-explaining what you were doing. The fix isn't a bigger context window. It's hooks. A simple hook that fires after compaction and injects the last 30-40 messages back into context. That's it. The recent work survives. The plan survives. The corrections survive. No more starting over mid-session. Pair that with a single thread you keep coming back to and you get something most people don't think is possible yet. An AI that actually adopts your taste and decision making over time. Not because you configured it. Because it's seen you correct it hundreds of times and those corrections live in the conversation history. The thread is the training data. Hooks are what keep it from getting wiped. People keep waiting for models to get better at remembering. The models are fine. The infrastructure around them is what's broken. Fix the hooks and the memory problem mostly goes away.

## Considering

- Orchestrator agent for automated PM workflows — see `🤖 AI/orchestrator-workflow-candidates.md` — 2026-04-04

## Parked (revisit when…)

- *Idea* — revisit when: *trigger* — *notes*

## Promoted (archive trail)

- *Idea* — promoted to `backlog.md` (section …) — YYYY-MM-DD

