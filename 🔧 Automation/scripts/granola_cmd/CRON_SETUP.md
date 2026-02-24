# Granola Sync Cron Job Setup

## Cron Entry

To run the granola sync every night at 9 PM PST, add this to your crontab:

```cron
0 21 * * * {{WORKSPACE_PATH}}/scripts/automation/granola_cmd/run_granola_sync.sh
```

## Setup Instructions

### 1. Edit crontab
```bash
crontab -e
```

### 2. Add the cron entry
Paste the line above into your crontab file.

### 3. Save and exit
- In vim: `:wq` and press Enter
- In nano: `Ctrl+O`, `Enter`, then `Ctrl+X`

### 4. Verify cron job is installed
```bash
crontab -l
```

## Cron Format Explained

```
┌───────────── minute (0 - 59)
│ ┌───────────── hour (0 - 23)
│ │ ┌───────────── day of month (1 - 31)
│ │ │ ┌───────────── month (1 - 12)
│ │ │ │ ┌───────────── day of week (0 - 7) (0 or 7 = Sunday)
│ │ │ │ │
* * * * * command
```

`0 21 * * *` = At 9:00 PM (21:00) every day

## Logs

Logs are written to:
```
{{WORKSPACE_PATH}}/.logs/granola_sync_YYYYMMDD.log
```

## Testing

Test the script manually before relying on cron:
```bash
{{WORKSPACE_PATH}}/scripts/automation/granola_cmd/run_granola_sync.sh
```

## Troubleshooting

### Check if cron is running
```bash
# Check cron service status (macOS)
sudo launchctl list | grep cron
```

### View recent logs
```bash
# Latest log
tail -50 {{WORKSPACE_PATH}}/.logs/granola_sync_$(date +%Y%m%d).log

# All logs
ls -la {{WORKSPACE_PATH}}/.logs/
```

### Debugging cron job
Add logging to crontab to capture cron's output:
```cron
0 21 * * * {{WORKSPACE_PATH}}/scripts/automation/granola_cmd/run_granola_sync.sh >> {{WORKSPACE_PATH}}/.logs/cron.log 2>&1
```

## Removing the cron job

```bash
crontab -e
# Delete the line, save, and exit
```
