#!/bin/bash
#
# Granola meeting sync wrapper for cron
#
# Purpose: Extract yesterday's meetings from Granola and save as markdown
# Scheduled: 9 PM PST daily via cron
#

set -euo pipefail

# Configuration (workspace uses 🔧 Automation/scripts)
WORKSPACE="/Users/jon.high/SNOW-Work"
AUTOMATION_DIR="${WORKSPACE}/🔧 Automation/scripts"
LOG_DIR="${WORKSPACE}/.logs"
LOG_FILE="${LOG_DIR}/granola_sync_$(date +%Y%m%d).log"
PYTHON_BIN="${PYTHON_BIN:-/opt/homebrew/bin/python3.12}"

# Ensure log directory exists
mkdir -p "${LOG_DIR}"

# Logging function
log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $*" | tee -a "${LOG_FILE}"
}

log "========================================="
log "Starting Granola meeting sync"
log "========================================="

# Change to automation directory
cd "${AUTOMATION_DIR}" || {
    log "ERROR: Failed to cd to ${AUTOMATION_DIR}"
    exit 1
}

# Run the granola collector
log "Running: ${PYTHON_BIN} -m granola_cmd.main"

if ${PYTHON_BIN} -m granola_cmd.main >> "${LOG_FILE}" 2>&1; then
    log "SUCCESS: Granola sync completed"
    exit 0
else
    EXIT_CODE=$?
    log "ERROR: Granola sync failed with exit code ${EXIT_CODE}"
    exit ${EXIT_CODE}
fi
