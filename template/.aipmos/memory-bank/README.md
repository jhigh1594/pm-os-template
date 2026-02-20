# Memory Bank - AI Persistent Context System

## Purpose

This memory system enables AI assistants to maintain context across sessions. After each context reset, the AI reads `memory.md` to immediately understand:
- What this project is and why it exists
- Current work focus and recent changes
- Product context (AgilePlace, OKRs, Roadmaps, DPD)
- Technical notes and workspace organization
- Active decisions and known gaps
- Key value theses

## File Structure

### Core File

**`memory.md`** - Unified Memory File
- Current focus and role context
- Product portfolio (all four products)
- Technical notes (AIPMOS, APIs, MCP integrations)
- Workspace organization
- Working principles
- Active decisions and open questions
- Known gaps and value theses

### Directories

- **`daily-plans/`** - Generated daily planning outputs from /today command
- **`bugs/`** - Bug tracking and triage
- **`mockups/`** - UI/UX mockups and designs
- **`triage/`** - Issue triage and prioritization

## How to Use

### For AI Assistants (Automatic)
- Reads `memory.md` at session start via `session-start.sh` hook
- Applies context automatically during work
- Updates memory when significant changes occur

### For You (Manual)
- Update `memory.md` when priorities shift significantly
- Review when starting new major initiatives
- Add new sections as needed for complex domains

## Update Triggers

**When to Update Memory:**
- After completing major milestones
- When strategic direction changes
- After significant product decisions
- When context feels stale or outdated

## Quality Standards

### Memory.md Should
- Use clear, simple language
- Prefer specifics over generalities
- Stay current with actual work
- Flag assumptions and unknowns
- Be concise and scannable

### Memory.md Should NOT
- Contain outdated information
- Become overly long (aim for ~100-150 lines)
- Include sensitive/confidential data without labeling
- Duplicate content unnecessarily

## Philosophy

**Start simple, add complexity only when needed.**

A single well-structured file that you actually update beats an automated system that's too complex to use. Git already remembers everything - this memory file provides the essential context for AI assistance.

---

**Simplified**: January 26, 2026 - Replaced 7-file memory bank with single unified file
