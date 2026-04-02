#!/bin/bash
#
# Nightly skill learning pipeline
# Evaluates accumulated runs, auto-applies LEARNED.md updates for qualified candidates.
# Runs daily after work hours via cron.
#
# Cron entry (runs at 23:00 daily — update path to match your workspace):
#   0 23 * * * "/path/to/your/workspace/🔧 Automation/scripts/skills_learning/nightly.sh"
#

WORKSPACE="$(cd "$(dirname "$0")/../../.." && pwd)"
cd "$WORKSPACE" || exit 1

VENV_PYTHON="$WORKSPACE/.venv/bin/python3"
PYTHON_CMD="${VENV_PYTHON:-python3}"

export PYTHONPATH="$WORKSPACE/🔧 Automation/scripts:${PYTHONPATH}"

LOG_FILE="${HOME}/tmp/skills-learning-nightly-$(date +%Y%m%d).log"
mkdir -p "$(dirname "$LOG_FILE")"

echo "=== Skill Learning Nightly: $(date) ===" >> "$LOG_FILE"

echo "--- ingest-session ---" >> "$LOG_FILE"
$PYTHON_CMD -m skills_learning --workspace "$WORKSPACE" ingest-session >> "$LOG_FILE" 2>&1

echo "--- nightly cycle ---" >> "$LOG_FILE"
$PYTHON_CMD -m skills_learning --workspace "$WORKSPACE" nightly >> "$LOG_FILE" 2>&1

find "${HOME}/tmp" -name "skills-learning-nightly-*.log" -mtime +30 -delete 2>/dev/null || true
exit 0
