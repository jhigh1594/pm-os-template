---
name: qmd
description: Search your workspace using QMD local semantic search. Use when user asks to: find PRDs, search competitive intel, look up product decisions, find PM frameworks, search AI patterns, query markdown docs, or find past work on a topic.
license: MIT
compatibility: Requires qmd CLI. Install via `npm install -g @tobilu/qmd`.
metadata:
  author: tobi (upstream)
  version: "2.0.0"
allowed-tools: Bash(qmd:*), mcp__qmd__*
---

# QMD - Workspace Search

Local semantic search engine for your PM workspace. Combines BM25 keyword search, vector embeddings, and LLM re-ranking—running completely offline.

## When to Use This Skill

Trigger this skill when:
- User asks to "search" or "find" workspace content
- User needs competitive intelligence or product decisions
- User references past work, decisions, or documentation
- User asks "what did we decide about X"
- User asks to look up frameworks, patterns, or mental models
- `/search` command is invoked
- User queries markdown documentation across the workspace

**Do NOT use for**:
- Web search (use web search tools)
- Current session history (use episodic memory)
- Real-time external data (use APIs/web)
- Non-markdown files (QMD indexes .md files only)

## Collections

| Collection | Content | Files |
|------------|---------|-------|
| `products` | Product strategy, PRDs, designs (AgilePlace, OKRs, Roadmaps, DPD) | 575 |
| `pm-frameworks` | PM frameworks, mental models, decision patterns | 438 |
| `company` | Competitive intel, business context | 165 |
| `ai-toolkit` | AI memory, patterns, prompts | 27 |
| `knowledge` | Stakeholder notes, reference | 10 |
| `workflows` | Repeatable processes | 6 |
| `tasks` | Daily priorities, backlog | 6 |

**Total**: 1,227+ markdown documents indexed locally

## Status

!`qmd status 2>/dev/null || echo "Not installed: npm install -g @tobilu/qmd"`

## Quick Start

```bash
# Semantic search (best for natural language)
qmd query "Global Attributes architecture decision"

# Keyword search (exact terms)
qmd search "Productboard pricing"

# Vector search (semantic similarity)
qmd vsearch "how to communicate tradeoffs to stakeholders"

# Get specific document
qmd get "products/AgilePlace/initiatives/Global attributes/global-attributes-prd.md"

# Multi-get by pattern
qmd multi-get "company/competitive/*.md" --json
```

## Common PM Queries

### Competitive Intelligence
```bash
qmd query "Productboard vs DPD positioning differentiation"
qmd search "Productboard pricing revenue" -c company
qmd vec "portfolio management features Productboard"
```

### Product Decisions
```bash
qmd query "Global Attributes two-tier architecture"
qmd query "board-level hiding decision mandatory fields"
qmd search "Decision Log" -c products --min-score 0.3
```

### Frameworks & Mental Models
```bash
qmd query "product sense vs data driven"
qmd search "Command of the Message" -c pm-frameworks
qmd vec "stakeholder communication patterns"
```

### AI Patterns & Skills
```bash
qmd search "pm-copilot" -c ai-toolkit
qmd query "discovery skill framework"
qmd search "episodic memory" -c ai-toolkit
```

## Query Syntax

### Single Line (Auto-Expand)
A single query automatically generates lex/vec/hyde variations:

```bash
qmd query "authentication flow design patterns"
```

### Multi-Line (Structured)
Combine query types for precision:

```bash
qmd query $'lex: rate limiter\nvec: how does rate limiting work'
```

### Query Types

| Type | Method | Use When |
|------|--------|----------|
| `lex` | BM25 keywords | Know exact terms, code identifiers |
| `vec` | Vector embeddings | Don't know vocabulary, semantic search |
| `hyde` | Hypothetical document | Know what answer looks like |
| (implicit) | Auto-expand | Want LLM to generate variations |

### Lex Syntax

```bash
lex: "exact phrase"              # Exact phrase match
lex: prefix -exclude            # Prefix match, exclude term
lex: "machine learning" -"deep learning"  # Phrase with exclusion
```

## Output Formats

```bash
# JSON for scripting/agents
qmd query "API design" --json

# File list (docid, score, path)
qmd search "authentication" --files

# Markdown for LLM context
qmd query "error handling" --md

# Full document content
qmd get "docs/api.md" --full
```

## Collection Filtering

```bash
# Search specific collection
qmd query "quarterly planning" -c products

# Multiple collections
qmd query "stakeholders" -c pm-frameworks,company

# Exclude collection (search all but X)
qmd query "meetings" --collections-ignore tasks
```

## MCP Tools

Configured via `.mcp.json` (`qmd mcp`). Tools as of v2.x:

| Tool | Parameters | Purpose |
|------|-----------|---------|
| `query` | `searches[]` (required), `intent`, `collections`, `limit`, `minScore`, `candidateLimit` | Hybrid search — returns ranked snippets. Primary tool. |
| `get` | `file` (required), `fromLine`, `maxLines` | Full document by path or docid. Use after `query` identifies the file. |
| `multi_get` | `pattern` (required), `maxBytes`, `maxLines` | Batch retrieval by glob or comma-separated list |
| `status` | *(none)* | Index health, collection info, model status |

**Note**: `qmd_search`, `qmd_vector_search`, `qmd_deep_search` were removed in v1.1.0. Use `query` with typed sub-queries instead.

**Agent best practices:**
- Always include `intent` to disambiguate queries across the full pipeline
- Set `minScore: 0.5` to drop noise before reranking
- Lower `candidateLimit` (e.g. 10) if only top results matter (default 30, reduces token cost)
- Use `get` with `maxLines` when you only need part of a document

## Performance

- **Keyword search**: < 100ms
- **Vector search**: ~500ms (first query warms model)
- **Hybrid + rerank**: ~4-5s (Qwen3-Reranker)
- **HTTP daemon mode**: Models stay loaded across sessions (recommended for repeated use)

## Setup

For complete installation, collection configuration, and context setup, see `.checkpoints/qmd-integration-plan.md`.

**Quick status check**:
```bash
qmd status  # Verify installation and collections
```

**Quick test query**:
```bash
qmd query "Global Attributes architecture decision"
```

## HTTP Daemon

For persistent model loading (faster repeated queries):

```bash
# Start HTTP server on localhost:8181
qmd mcp --http --daemon

# Stop daemon
qmd mcp stop

# Check status
qmd status  # Shows "MCP: running (PID ...)" when active
```

## Maintenance

```bash
# Re-index after adding documents
qmd update

# With git pull for remote content
qmd update --pull

# Clean up cache
qmd cleanup
```

## Examples by Use Case

### Before Writing a PRD
```bash
# Find related decisions and context
qmd query "authentication authorization decisions" --collections products,company -n 10
```

### Competitive Prep
```bash
# Get all competitive intel on a competitor
qmd multi-get "company/competitive/*productboard*.md" --json
```

### Framework Lookup
```bash
# Find mental model for current situation
qmd query "product sense data judgment tradeoffs"
```

### Session Continuation
```bash
# Find past work on a topic
qmd query "episodic memory implementation decisions"
```

## See Also

- Upstream docs: https://github.com/tobi/qmd
- QMD integration plan: `.checkpoints/qmd-integration-plan.md`
- `/search` command for workspace-specific queries

## Self-Learning

Before responding, read `LEARNED.md` in this skill directory when it exists and treat it as compact runtime guidance that sharpens this skill.

Rules for self-improvement:
- Keep `SKILL.md` human-owned; do not rewrite it directly from normal usage.
- Propose broader instruction changes through the central skill-learning review queue.
- Only promote specific, reusable, evidence-backed lessons into `LEARNED.md`.
