---
description: Daily competitive intelligence brief — Exa search + firecrawl scraping, synthesized by Claude. No external scripts required.
---

# /ci-brief — Competitive Intelligence Brief

Generates a dated competitive intelligence brief using Exa for signal discovery and firecrawl for full-content extraction. Claude-native — no Python scripts, no external dependencies.

**Replaces:** `/daily-brief` (which depended on an external Python stack that no longer exists at the expected path)

---

## Usage

```
/ci-brief [mode] [--focus <competitor-or-topic>] [--industry]
```

- **mode**: `quick` | `standard` | `deep` (default: `standard`)
- **--focus**: Narrow scope to a specific competitor or topic (e.g., `PlanHat`, `pricing changes`)
- **--industry**: Append a broader market signals section after the main brief

---

## Mode Reference

| Mode | Lookback | Searches | Firecrawl | Max Insights |
|------|----------|----------|-----------|--------------|
| `quick` | 24h | 3 Exa searches, snippets only | None | 3 |
| `standard` | 24h | 5 Exa searches | Scrape top 3 URLs | 5 |
| `deep` | 48h | 8 Exa searches | Scrape top 5 URLs + crawl competitor blogs (limit 5) | 10 |

---

## Execution

### Step 1: Load Tracked Competitors

Read `📚 Knowledge/Market/tracked-competitors.md` if it exists. Extract the competitor list from it.

If the file doesn't exist, ask: "Which competitors should I track for this brief?" then proceed. After the session, suggest creating the file to avoid the prompt next time.

### Step 2: Build Search Queries

For each tracked competitor (or the `--focus` target), construct Exa searches with explicit time bounds:

**Product & feature signals** (lookback window):
- `"[Competitor] product update OR new feature OR launch OR announcement"`
- `"[Competitor] pricing change OR new plan OR enterprise"`

**Customer sentiment** (7-day window regardless of mode):
- `"[Competitor] G2 review OR customer complaint OR feedback"`

**Company signals** (30-day window):
- `"[Competitor] funding OR acquisition OR partnership OR executive"`

**Job posting signals** (14-day window, deep mode only):
- `"[Competitor] site:linkedin.com/jobs OR site:greenhouse.io OR site:lever.co"`

Run 3 searches (quick), 5 searches (standard), or 8 searches (deep). Use `mcp__exa__web_search_exa` with `numResults: 5` per query.

### Step 3: Scrape Full Content (standard + deep only)

From Step 2 results, select the top 3 (standard) or top 5 (deep) most relevant URLs — prioritize primary sources over aggregators.

For each selected URL, run:
```bash
firecrawl scrape "[URL]" --only-main-content
```

Use the scraped full text for analysis, not the Exa snippet. Every claim from a scraped source must be labeled:
```
→ Source: [URL], scraped [today's date], Tier [1|2|3]
```

**Skip scraping if:** the URL is a social media post, requires login, or times out after one retry. Fall back to the Exa snippet and note "snippet only — full content unavailable."

### Step 4: Competitor Blog Crawl (deep mode only)

For each competitor with a known blog or changelog URL:
```bash
firecrawl crawl "[competitor blog or changelog URL]" --limit 5
```

Surface any posts published within the lookback window. Flag posts outside the window as "background context."

### Step 5: Synthesize the Brief

Organize findings into the output format below. Apply the source hierarchy from `/compete`:
- **Tier 1** (High Trust): Earnings calls, regulatory filings, independent analyst reports
- **Tier 2** (Medium Trust): Customer reviews (G2, Capterra), press releases
- **Tier 3** (Low Trust): Competitor marketing sites, vendor blogs

Label every significant claim with its tier and date. Flag single-source claims: `[SINGLE SOURCE — verify before acting]`.

Do not fabricate data. If information is unavailable from sources, say so explicitly.

### Step 6: Industry Signals (--industry flag only)

After the main brief, append 2–3 broader market signals:
- Analyst coverage updates (Gartner, Forrester, G2 category reports)
- Adjacent market moves (enterprise software earnings, platform announcements)
- Macro signals relevant to the product category

Label each signal with confidence: `[High confidence — Tier 1]` or `[Low confidence — Tier 3]`.

### Step 7: Save Output

Create the directory if needed, then write the brief:
```
📚 Knowledge/Market/ci-briefs/YYYY-MM-DD.md
```

Print the saved path when done.

---

## Output Format

```markdown
# CI Brief — [Date]
**Mode:** [quick|standard|deep] | **Competitors:** [list] | **Focus:** [if set]

---

## Top Signals

### 🔴 Urgent (act within 48h)
- [Signal] → Source: [URL], [date], Tier [N]

### 🟡 Watch (worth tracking)
- [Signal] → Source: [URL], [date], Tier [N]

### 🟢 Background (context)
- [Signal] → Source: [URL], [date], Tier [N]

---

## By Competitor

### [Competitor Name]
**What's new:** [1-3 sentences, factual only]
**Customer sentiment shift:** [positive/negative/flat — cite source]
**Roadmap signals:** [job posting patterns, blog themes — label as inference]
**Strategic read:** [1 sentence interpretation — label as our analysis]

---

## Recommended Actions
1. [Specific action] — [why, based on which signal]
2. [Specific action] — [why, based on which signal]

---

## Sources
| # | URL | Type | Tier | Date |
|---|-----|------|------|------|
| 1 | [URL] | Exa snippet / firecrawl scrape | [1-3] | [date] |
```

---

## Scheduling Note

This skill is designed to be run daily, either interactively or via cron. The nightly automation at `🔧 Automation/scripts/skills_learning/nightly.sh` tracks skill performance — each run contributes to its learning signal.

To run headlessly (add to cron or a shell script):
```bash
claude -p "/ci-brief standard --industry" --allowedTools "Bash,Read,Write,mcp__exa__web_search_exa"
```
