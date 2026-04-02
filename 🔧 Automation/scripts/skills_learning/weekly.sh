#!/bin/bash
#
# Weekly skill learning pipeline
# Full cycle: evaluates all runs, generates revision proposals, writes maintainer report.
# Runs every Sunday at 23:00 via cron.
#
# Cron entry (update path to match your workspace):
#   0 23 * * 0 "/path/to/your/workspace/🔧 Automation/scripts/skills_learning/weekly.sh"
#

WORKSPACE="$(cd "$(dirname "$0")/../../.." && pwd)"
cd "$WORKSPACE" || exit 1

VENV_PYTHON="$WORKSPACE/.venv/bin/python3"
PYTHON_CMD="${VENV_PYTHON:-python3}"

export PYTHONPATH="$WORKSPACE/🔧 Automation/scripts:${PYTHONPATH}"

LOG_FILE="${HOME}/tmp/skills-learning-weekly-$(date +%Y%m%d).log"
mkdir -p "$(dirname "$LOG_FILE")"

echo "=== Skill Learning Weekly: $(date) ===" >> "$LOG_FILE"
$PYTHON_CMD -m skills_learning --workspace "$WORKSPACE" weekly >> "$LOG_FILE" 2>&1
echo "Report written to: 🤖 AI/skills/review-queue/" >> "$LOG_FILE"

find "${HOME}/tmp" -name "skills-learning-weekly-*.log" -mtime +60 -delete 2>/dev/null || true
exit 0
