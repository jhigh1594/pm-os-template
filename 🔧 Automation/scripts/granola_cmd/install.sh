#!/bin/bash
# Install Granola command launchd agent (macOS only).
# Resolves workspace from this script's location — no {{WORKSPACE_PATH}} placeholders.

set -e

if [[ "$(uname -s)" != "Darwin" ]]; then
    echo "Granola LaunchAgent install is macOS-only. On other OSes, run /granola manually or see CRON_SETUP.md."
    exit 1
fi

GRANOLA_CMD_DIR="$(cd "$(dirname "$0")" && pwd)"
SCRIPT_DIR="$(cd "${GRANOLA_CMD_DIR}/.." && pwd)"
WORK_DIR="$(cd "${SCRIPT_DIR}/../.." && pwd)"
PLIST_PATH="$HOME/Library/LaunchAgents/com.pm-os.granola_cmd.plist"
LOGS_DIR="${WORK_DIR}/.logs"

mkdir -p "$LOGS_DIR"

PYTHON_BIN="/usr/bin/python3"
if [[ -x "${WORK_DIR}/.venv/bin/python3" ]]; then
    PYTHON_BIN="${WORK_DIR}/.venv/bin/python3"
fi

# Reinstall: unload existing agent if present
if [[ -f "$PLIST_PATH" ]]; then
    launchctl unload "$PLIST_PATH" 2>/dev/null || true
fi

cat > "$PLIST_PATH" << EOF
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.pm-os.granola_cmd</string>

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
        <key>WORKSPACE_PATH</key>
        <string>${WORK_DIR}</string>
    </dict>

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

launchctl load "$PLIST_PATH"

echo "✓ Granola daily sync installed (11:59 PM local time)"
echo "✓ Workspace: ${WORK_DIR}"
echo "✓ Output: ${WORK_DIR}/🏢 Company/meetings/granola/"
echo "✓ Logs: ${LOGS_DIR}/granola_cmd_stdout.log, granola_cmd_stderr.log"
echo ""
echo "Scheduled runs export markdown only. Use /granola in Cursor for AI summaries."
echo ""
echo "Verify: launchctl list | grep pm-os.granola"
echo ""
echo "Manual run:"
echo "  cd '${SCRIPT_DIR}' && python3 -m granola_cmd.main --target-date yesterday"
echo ""
echo "Uninstall:"
echo "  launchctl unload '${PLIST_PATH}' && rm '${PLIST_PATH}'"
