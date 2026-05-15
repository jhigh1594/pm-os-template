---
description: Fetch and analyze web page content using Browserless cloud browser
---

# /scrape

Fetch live page content from any URL using Browserless, then summarize or extract for research.

## Usage

```
/scrape <url>                         — fetch and summarize page content
/scrape <url> --stealth               — use stealth mode (bot detection bypass)
/scrape <url> --screenshot            — capture screenshot instead
/scrape <url> --selector "h1,.price"  — extract specific elements
```

## What this does

1. Calls Browserless cloud browser to render the page (JavaScript executed)
2. Returns clean text or structured data
3. Summarizes or formats for downstream use in `/compete`, `/research`, or `/ci-brief`

## Instructions

When `/scrape` is invoked:

1. Identify the URL and any flags from the user's message
2. Choose the right operation:
   - Default → `bql` (BrowserQL text extraction, faster)
   - `--stealth` → `bql --stealth` (use `/stealth/bql` endpoint)
   - `--screenshot` → `screenshot` command
   - `--selector` → `scrape` command with the selector(s)
3. Run via the CLI:
   ```bash
   cd "$(git rev-parse --show-toplevel)"
   PYTHONPATH="🔧 Automation/scripts" .venv/bin/python -m browserless_cmd.main bql <url> [--stealth]
   ```
4. If content is long, summarize the key facts relevant to the user's research goal
5. Cite the URL and note it was fetched live (date: today)

## Error handling

- `BROWSERLESS_API_KEY not set` → check `.claude/settings.local.json` has the env block
- HTTP 429 → rate limited; wait 10s and retry once
- HTTP 401 → API key invalid; ask user to verify key in settings.local.json
- Empty content → try `--stealth` mode (site may block default browser fingerprint)

## Integration

- Feed output into `/compete` for competitive analysis
- Feed output into `/synthesize` for multi-source research synthesis
- Feed output into `/ci-brief` for CI report generation
