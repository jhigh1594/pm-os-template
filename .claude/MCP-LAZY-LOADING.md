# MCP Lazy Loading - Quick Start

## Overview
Manual lazy loading system for project MCP servers (fetch, notion, etc.) to save tokens.

## Setup Complete ✅

### 1. Notion MCP Added to Project
- Location: `.ruler/ruler.toml`
- **ACTION REQUIRED**: Add your Notion API key:
  ```bash
  # Edit .ruler/ruler.toml and replace:
  env = { NOTION_API_KEY = "your-notion-api-key-here" }
  # with your actual key from https://www.notion.so/my-integrations
  ```

### 2. Toggle Script Created
- Location: `.claude/scripts/toggle-mcp.sh`
- Usage: `./.claude/scripts/toggle-mcp.sh {on|off|toggle|status}`

## How to Use

### Enable MCP Servers (Load Notion, Fetch, etc.)
```bash
./.claude/scripts/toggle-mcp.sh on
# Restart Claude Code to apply
```

### Disable MCP Servers (Save Tokens)
```bash
./.claude/scripts/toggle-mcp.sh off
# Restart Claude Code to apply
```

### Quick Toggle
```bash
./.claude/scripts/toggle-mcp.sh toggle
```

### Check Status
```bash
./.claude/scripts/toggle-mcp.sh status
```

## Workflow Examples

**PM Mode with Notion:**
```bash
./.claude/scripts/toggle-mcp.sh on
# Work with Notion, fetch docs, etc.
./.claude/scripts/toggle-mcp.sh off  # When done
```

**Light Mode (Max tokens):**
```bash
./.claude/scripts/toggle-mcp.sh off
# Only core tools loaded
```

## What's Loaded

**Always (Base Load):**
- ✅ Read, Write, Edit, Bash (core tools)
- ✅ dotai plugins: ctx, dotai, plan, skills
- ✅ Global MCPs from Claude Desktop (agileplace, granola, etc.)

**When Enabled:**
- ✅ Fetch MCP (web content extraction)
- ✅ Notion MCP (pages, databases, docs)
- ✅ Any future project-level MCPs

## Token Savings

**Disabled:** ~5-10k base token cost
**Enabled:** +5-10k for project MCPs

Estimated savings: **40-50k tokens** from disabling unused plugins + **5-10k more** when MCPs disabled.

## Next Steps

1. Add your Notion API key to `.ruler/ruler.toml`
2. Test: `./.claude/scripts/toggle-mcp.sh status`
3. Try enabling: `./.claude/scripts/toggle-mcp.sh on`
4. Restart Claude Code and verify Notion tools work
