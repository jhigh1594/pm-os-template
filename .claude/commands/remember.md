---
description: Run the remember workflow
---
# /remember - Search Conversation History

Search past Claude Code conversations for discussions, decisions, and patterns using the episodic-memory skill.

This command is the explicit conversation-recall path. Local repo and canonical memory context may now be injected automatically for cue-driven prompts such as "continue", "what did we decide", or "recap". Use `/remember` when you specifically need chat history, session-to-session rationale, or details that are not captured in repo files.

> **Note**: This command uses the `episodic-memory` skill from superpowers-marketplace, which searches Claude Code conversation history. This is distinct from `claude-mem` MCP tools that search stored observations.

---

## Command Arguments

Parse the command arguments:
1. **Query** (required): What to search for
2. **--recent** (optional, flag): Limit to last 7 days
3. **--decisions** (optional, flag): Focus on decision-type observations

---

## Execution

### Step 1: Parse Arguments

Extract query and flags from the command input.

If no query provided, ask: "What would you like me to remember?"

### Step 2: Search Conversation History

Use the Skill tool to invoke the episodic-memory search:

```
Skill tool:
  skill: "episodic-memory:search-conversations"
  args: "[query]"
```

**If --recent flag**: Append " (last 7 days)" to the args.

**If --decisions flag**: Append " - focus on decisions" to the args.

**If the automatic hook already injected local repo context**:
- Keep that context separate from conversation recall
- Use `/remember` only for prior chat details, decisions, or rationale not present in `🤖 AI/...` or repo files

### Step 3: Format Results

Present the search findings in this format:

```
🔍 **Found in [N] conversations:**

**Summary**: [Synthesized insight from results]

**Key Findings**:
• [Finding 1] (Session #[id])
• [Finding 2] (Session #[id])
• [Finding 3] (Session #[id])

**Related Context**: [Timeline or connections if available]
```

### Step 4: Offer Follow-up

Ask the user:
"Would you like me to fetch full details from any of these sessions, or search for something else?"

---

## Error Handling

**If no results found:**
```
🔍 **No relevant context found** for "[query]"

Try:
- Different keywords
- Broader search terms
- /remember --recent (last 7 days only)
```

**If episodic-memory skill is unavailable:**
```
⚠️ **Memory Unavailable**

The episodic-memory skill is not accessible. This may be because:
- The episodic-memory plugin is not installed
- The skill failed to initialize

Fallback: Use claude-mem MCP tools directly with mcp__plugin_claude-mem_claude-mem-search__search
```

---

## Examples

```
/remember dependency mapping feature
→ Returns discussions about dependency mapping work

/remember --recent
→ Returns all conversations from last 7 days

/remember --decisions authentication
→ Returns decisions made about authentication

/remember "like we discussed last week"
→ Searches for recent discussions

/remember "what did we decide about memory hooks"
→ Searches prior conversations for decision rationale beyond local repo context
```

---

## Integration

**Related commands**:
- `/refresh-memory` - Updates current session in memory.md
- `/capture-pattern` - Captures patterns to learned-patterns.md
- `/check-progress` - Shows deltas since last memory update

**Automatic complement**:
- Cue-triggered `UserPromptSubmit` hook injects local context from `🤖 AI/memory/memory.md`, `🤖 AI/patterns/learned-patterns.md`, and selected repo folders
- That hook does **not** search conversation history directly; it only nudges Claude to use `episodic-memory:search-conversations` when earlier chat history matters

**Skill used**: `episodic-memory:search-conversations` from superpowers-marketplace for token-efficient search of Claude Code conversation history.
