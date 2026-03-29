#!/bin/bash
# SessionEnd hook - thin wrapper around guarded Python session-end logic.

set -euo pipefail

workspace_root=$(pwd)
while [ "$workspace_root" != "/" ] && [ ! -f "$workspace_root/GOALS.md" ] && [ ! -f "$workspace_root/CLAUDE.md" ]; do
    workspace_root=$(dirname "$workspace_root")
done

VENV_PYTHON="$workspace_root/.venv/bin/python3"
if [ -f "$VENV_PYTHON" ]; then
    PYTHON_CMD="$VENV_PYTHON"
else
    PYTHON_CMD="python3"
fi

"$PYTHON_CMD" "$workspace_root/🔧 Automation/scripts/hooks/session_end.py" \
    --workspace "$workspace_root" \
    --python-cmd "$PYTHON_CMD" 2>&1 || true
