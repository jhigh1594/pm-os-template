# Granola Command

Extract meetings from Granola (local cache) and save as markdown in `🏢 Company/meetings/granola/`.

## Manual run

```bash
cd "{{WORKSPACE_PATH}}/🔧 Automation/scripts"
python3 -m granola_cmd.main --target-date yesterday
```

Or use the Cursor command: `/granola` (yesterday), `/granola today`, `/granola 2026-02-17`.

## Scheduled daily run (LaunchAgent)

The job runs **daily at 11:59 PM** via macOS LaunchAgent. It was not running because:

1. **Plist was missing** – the LaunchAgent was never installed or was removed.
2. **Paths were wrong** – install script pointed at `scripts/automation` instead of `🔧 Automation/scripts`, so the job would have failed even if installed.

### Install or reinstall

From the workspace root:

```bash
bash "🔧 Automation/scripts/granola_cmd/install.sh"
```

This will:

- Create `~/Library/LaunchAgents/com.planview.granola_cmd.plist`
- Set WorkingDirectory to `…/Planview Work/🔧 Automation/scripts`
- Use workspace `.venv/bin/python3` if present
- Log to `Planview Work/.logs/granola_cmd_stdout.log` and `granola_cmd_stderr.log`
- Load the agent so it runs at 23:59 daily

### Uninstall

```bash
launchctl unload ~/Library/LaunchAgents/com.planview.granola_cmd.plist
rm ~/Library/LaunchAgents/com.planview.granola_cmd.plist
```

### Check status

```bash
launchctl list | grep planview.granola
# If installed: shows com.planview.granola_cmd with PID 0 when idle
# If missing: no line
```

Logs after a run: `Planview Work/.logs/granola_cmd_*.log`.
