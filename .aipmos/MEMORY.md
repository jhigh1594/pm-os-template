# Sleeping Memory Manifest

**What this is:** Maps conversation triggers to content that lives in the repo but isn't loaded until "woken."

## Always Loaded (Core)

- `.aipmos/version.json` - Version checking
- `.aipmos/MEMORY.md` - This manifest
- `.aipmos/memory-bank/memory.md` - Current focus and active context (keep this lightweight)
- `.claude/commands/COMMAND-REFERENCE.md` - Command intent detection and reference

## Wake on Trigger

| Trigger | Wake (load these) |
|---------|-------------------|
| Product context (AgilePlace, OKRs, Roadmaps) | `Products/{product}/` folder |
| Company context | `Company/planview-comprehensive-overview.md` |
| Strategy frameworks | `Product-Management/Frameworks/` |
| PM mental models | `Product-Management/mental-models.md` |
| Recent sessions | `.specstory/history/` (last 7 days) |
| Command help | `.claude/commands/COMMAND-REFERENCE.md` |
| Lenny's podcast insights | `Product-Management/lennys-learning-paths/` |
| Next.js prototyping | `nextjs-starter-kit/` documentation |

## Memory.md Bloat Prevention

Keep `.aipmos/memory-bank/memory.md` focused on:
- Current focus (what I'm working on NOW)
- Product context summaries (not full docs)
- Active decisions and open questions
- Recent completed work (last 5-10 sessions)

Move detailed/historical content to appropriate folders and link from memory.md.

## Token Efficiency Targets

- **Core load goal**: < 3,000 tokens baseline
- **Full context load**: 8,000-15,000 tokens when needed
- **Wake on demand**: Only load specific domains when triggered

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0.0 | 2026-02-09 | Initial sleeping memory manifest |
