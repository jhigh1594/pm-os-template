#!/bin/bash
#
# Autonomous CI Brief — daily competitive intelligence
# Runs /ci-brief standard --industry using claude -p, saves output to
# 📚 Knowledge/Market/ci-briefs/YYYY-MM-DD.md
#
# Cron entry (runs at 6:00am daily):
#   0 6 * * * "/Users/jhigh/SNOW-Work/🔧 Automation/scripts/ci_brief_cmd/run.sh" >> ~/tmp/ci-brief.log 2>&1
#

# ── Setup ──────────────────────────────────────────────────────────────────
WORKSPACE="$(cd "$(dirname "$0")/../../.." && pwd)"
CLAUDE="$HOME/.local/bin/claude"
DATE="$(date +%Y-%m-%d)"
LOG_PREFIX="=== CI Brief $DATE: $(date '+%H:%M:%S')"

echo "$LOG_PREFIX — starting ===" >> ~/tmp/ci-brief.log

# Verify claude binary exists
if [[ ! -x "$CLAUDE" ]]; then
  echo "$LOG_PREFIX — ERROR: claude not found at $CLAUDE" >> ~/tmp/ci-brief.log
  exit 1
fi

# ── Run ci-brief via claude -p ─────────────────────────────────────────────
cd "$WORKSPACE" || exit 1

# Load yesterday's brief for delta comparison (if it exists)
YESTERDAY="$(date -v-1d +%Y-%m-%d 2>/dev/null || date -d 'yesterday' +%Y-%m-%d 2>/dev/null)"
YESTERDAY_FILE="$WORKSPACE/📚 Knowledge/Market/ci-briefs/$YESTERDAY.md"

if [[ -f "$YESTERDAY_FILE" ]]; then
  YESTERDAY_CONTEXT="

---
## Yesterday's Brief (for delta comparison)

The following is yesterday's CI brief ($YESTERDAY). Use it to identify what is genuinely new today.
At the top of today's output, before the main brief, add a **## What's New Since Yesterday** section:
- List only signals that did not appear in yesterday's brief
- If a story is the same but has a meaningful update (e.g. new detail, customer reaction, pricing confirmed), note it as an update
- If nothing material has changed, write: 'No material changes since yesterday — brief below for full context'
- Keep this section to 5 bullet points max

<yesterday>
$(cat "$YESTERDAY_FILE")
</yesterday>"
  echo "$LOG_PREFIX — yesterday's brief found, delta comparison enabled ===" >> ~/tmp/ci-brief.log
else
  YESTERDAY_CONTEXT=""
  echo "$LOG_PREFIX — no yesterday brief found, running without delta ===" >> ~/tmp/ci-brief.log
fi

# Pass the full skill content so it works reliably in headless mode.
# Append the mode + flag inline so claude processes it correctly.
SKILL_CONTENT="$(cat "$WORKSPACE/.claude/commands/ci-brief.md")"
PROMPT="$SKILL_CONTENT

---
Run this skill now in **standard** mode with the **--industry** flag.
Today's date is $DATE.$YESTERDAY_CONTEXT"

"$CLAUDE" -p "$PROMPT" \
  --allowedTools "Bash,Read,Write,Glob,Grep,mcp__exa__web_search_exa,mcp__exa__web_search_advanced_exa,mcp__exa__company_research_exa,mcp__exa__crawling_exa" \
  >> ~/tmp/ci-brief.log 2>&1

EXIT_CODE=$?

# ── Report ─────────────────────────────────────────────────────────────────
OUTPUT_FILE="$WORKSPACE/📚 Knowledge/Market/ci-briefs/$DATE.md"

if [[ $EXIT_CODE -eq 0 ]]; then
  if [[ -f "$OUTPUT_FILE" ]]; then
    echo "$LOG_PREFIX — success, brief saved to: $OUTPUT_FILE ===" >> ~/tmp/ci-brief.log
  else
    echo "$LOG_PREFIX — claude exited 0 but brief file not found at expected path ===" >> ~/tmp/ci-brief.log
  fi
else
  echo "$LOG_PREFIX — ERROR: claude exited with code $EXIT_CODE ===" >> ~/tmp/ci-brief.log
fi

exit $EXIT_CODE
