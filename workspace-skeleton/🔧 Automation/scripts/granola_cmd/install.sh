#!/bin/bash
# Install Granola command launchd agent

set -e

# Configuration (use 🔧 Automation/scripts; workspace root has emoji-prefixed dirs)
WORK_DIR="{{WORKSPACE_PATH}}"
SCRIPT_DIR="${WORK_DIR}/🔧 Automation/scripts"
PLIST_PATH="$HOME/Library/LaunchAgents/com.planview.granola_cmd.plist"
LOGS_DIR="${WORK_DIR}/.logs"

# Ensure logs directory exists
mkdir -p "$LOGS_DIR"

# Prefer workspace venv Python if present
PYTHON_BIN="/usr/bin/python3"
if [[ -x "${WORK_DIR}/.venv/bin/python3" ]]; then
    PYTHON_BIN="${WORK_DIR}/.venv/bin/python3"
fi

# Create plist file (WorkingDirectory must be 🔧 Automation/scripts so granola_cmd runs)
cat > "$PLIST_PATH" << EOF
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.planview.granola_cmd</string>

    <key>ProgramArguments</key>
    <array>
        <string>${PYTHON_BIN}</string>
        <string>-m</string>
        <string>granola_cmd.main</string>
        <string>--target-date</string>
        <string>yesterday</string>
    </array>

    <key>WorkingDirectory</key>
    <string>${SCRIPT_DIR}</string>

    <key>StandardOutPath</key>
    <string>${LOGS_DIR}/granola_cmd_stdout.log</string>

    <key>StandardErrorPath</key>
    <string>${LOGS_DIR}/granola_cmd_stderr.log</string>

    <key>EnvironmentVariables</key>
    <dict>
        <key>PYTHONPATH</key>
        <string>${SCRIPT_DIR}</string>
    </dict>

    <!-- Run daily at 11:59 PM -->
    <key>StartCalendarInterval</key>
    <dict>
        <key>Hour</key>
        <integer>23</integer>
        <key>Minute</key>
        <integer>59</integer>
    </dict>

    <key>RunAtLoad</key>
    <false/>

    <key>KeepAlive</key>
    <false/>
</dict>
</plist>
EOF

# Load the agent
launchctl load "$PLIST_PATH"

echo "✓ Granola command scheduled to run daily at 11:59 PM"
echo "✓ Logs: ${LOGS_DIR}/granola_cmd_*.log"
echo ""
echo "To run manually:"
echo "  cd '${SCRIPT_DIR}'"
echo "  python3 -m granola_cmd.main"
echo ""
echo "To uninstall:"
echo "  launchctl unload '$PLIST_PATH'"
echo "  rm '$PLIST_PATH'"
