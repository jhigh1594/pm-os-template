# Granola Command

Extract meetings from Granola (local cache) and save as markdown in `🏢 Company/meetings/granola/`.

## Manual run

```bash
cd "{{WORKSPACE_PATH}}/🔧 Automation/scripts"
python3 -m granola_cmd.main --target-date yesterday
```

Or use the slash command: **Cursor** `.cursor/commands/granola.md` or **Claude Code** `.claude/commands/granola.md` — `/granola` (yesterday), `/granola today`, `/granola 2026-02-17`.

After a successful run, the CLI prints a machine-readable JSON block between `GRANOLA_AGENT_RESULT_JSON_BEGIN` and `GRANOLA_AGENT_RESULT_JSON_END` so the host agent knows which files were written. Agent-driven `/granola` then inserts a bounded **## AI summary** block at the top of each note (see those command files).

## Scheduled daily run (LaunchAgent)

The job runs **daily at 11:59 PM** (local time) via macOS LaunchAgent. Exports markdown only — use `/granola` in Cursor or Claude Code for AI summaries.

**`/onboard`** can install this after explicit approval (Step 4, Granola = yes).

### Install or reinstall

From the workspace root:

```bash
bash "🔧 Automation/scripts/granola_cmd/install.sh"
```

This will:

- Create `~/Library/LaunchAgents/com.pm-os.granola_cmd.plist`
- Set WorkingDirectory to `…/your-workspace/🔧 Automation/scripts`
- Use workspace `.venv/bin/python3` if present
- Log to `your-workspace/.logs/granola_cmd_stdout.log` and `granola_cmd_stderr.log`
- Load the agent so it runs at 23:59 daily

### Uninstall

```bash
launchctl unload ~/Library/LaunchAgents/com.pm-os.granola_cmd.plist
rm ~/Library/LaunchAgents/com.pm-os.granola_cmd.plist
```

### Check status

```bash
launchctl list | grep pm-os.granola
# If installed: shows com.pm-os.granola_cmd with PID 0 when idle
# If missing: no line
```

Logs after a run: `your-workspace/.logs/granola_cmd_*.log`.
