# Learned
<!-- Machine-maintained. Keep entries specific, reusable, and evidence-backed. -->

## `get` parameter is `file`, not `path` (2026-03-30)

The MCP tool `mcp__qmd__get` requires parameter **`file`**, not `path`.
The upstream MCP instructions describe it as "path or docid" in English, but the JSON schema
parameter is `file`. Always call it as:

```json
{ "file": "products/foo/bar.md" }
```

Calling with `path:` causes: `MCP error -32602: Invalid input: expected string, received undefined`

## Prefer `query` over `get` for information retrieval (2026-03-30)

**`query`** returns ranked **snippets** — small excerpts, low token cost. This is QMD's purpose.
**`get`** returns the **full document** — can be 10k+ tokens per file.

Correct pattern:
1. Use `query` with `searches` array first → get snippets + file paths
2. Only call `get` if the full document is specifically needed after identifying it via search

Never call `get` as a first-resort document lookup. Use it only when a search result confirms
the document is the right one and full content is required.
