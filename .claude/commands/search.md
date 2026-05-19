---
description: Run the search workflow
---
# Search the workspacespace

Search across all product strategy, competitive intelligence, PM frameworks, and AI patterns using QMD local semantic search.

**When to use**: Finding PRDs, searching competitive intel, looking up product decisions, finding PM frameworks, searching AI patterns, querying markdown docs, or finding past work on a topic.

## Usage

```
/search "what did we decide about Global Attributes architecture?"
/search "[your product] competitive positioning vs [competitor]"
/search "product sense mental models"
/search "Command of the Message value proposition"
```

## What It Searches

| Collection | Content | Documents |
|------------|---------|-----------|
| `products` | PRDs, product strategy, designs (folders under `📦 Products/`) | varies |
| `pm-frameworks` | Mental models, decision frameworks, communication patterns | 438 |
| `company` | Competitive analysis, business intelligence | 165 |
| `ai-toolkit` | AI patterns, prompts, memory | 27 |

**Total**: 1,227+ markdown documents indexed locally

## How It Works

1. Converts your query to semantic embeddings
2. Searches using BM25 (keywords) + vector similarity
3. Expands query using local LLM (generates variations)
4. Re-ranks results by relevance
5. Returns top matches with context snippets

All runs completely offline—no API calls, data stays local.

## Examples

### Competitive Intelligence
```
/search "Productboard portfolio management capabilities"
/search "Competitive differentiation for [your product]"
/search "[competitor] vs [your product]"
```

### Product Decisions
```
/search "Global Attributes mandatory fields decision"
/search "Board-level hiding removal justification"
/search "Two-tier attribute architecture rationale"
```

### Frameworks & Mental Models
```
/search "Product sense vs data driven decision making"
/search "Command of the Message commercial framework"
/search "Stakeholder communication for bad news"
```

### AI Patterns
```
/search "Discovery skill usage patterns"
/search "PM copilot prompt templates"
/search "Episodic memory implementation"
```

## Search by Collection

To search specific collections, use QMD directly:

```bash
# Products only
qmd query "API design patterns" -c products

# PM frameworks only
qmd search "decision framework" -c pm-frameworks

# Competitive intel only
qmd query "Productboard pricing" -c company
```

## Output Options

```bash
# More results
qmd query "topic" -n 20

# JSON output
qmd query "topic" --json

# File list only
qmd search "topic" --files

# Minimum score threshold
qmd query "topic" --min-score 0.4
```

## Not Finding What You Expect?

1. **Check collections are indexed**: `qmd status`
2. **Try simpler query**: Fewer words, focus on core concept
3. **Use keyword search**: `qmd search "exact phrase" -c products`
4. **Update index**: `qmd update`

## Behind the Scenes

Runs: `qmd query "<user query>"` with automatic query expansion and LLM re-ranking.

First query in a session is slower (~1-2s) as models load. Subsequent queries are faster.
