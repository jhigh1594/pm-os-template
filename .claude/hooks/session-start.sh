#!/bin/bash
# SessionStart hook - lightweight session initialization.
# This hook intentionally avoids continuation-cue logic because
# Bash hooks run before the user message is available.

set -euo pipefail

workspace_root="$(pwd)"
while [ "$workspace_root" != "/" ] && [ ! -f "$workspace_root/GOALS.md" ] && [ ! -f "$workspace_root/CLAUDE.md" ]; do
    workspace_root=$(dirname "$workspace_root")
done

session_intent_file="$workspace_root/🤖 AI/session-intent.json"
retrieval_config_file="$workspace_root/🤖 AI/retrieval/retrieval-config.yaml"
mkdir -p "$(dirname "$session_intent_file")"

if [ -n "${CLAUDE_ENV_FILE:-}" ]; then
    {
        echo "export AIPMOS_WORKSPACE_ROOT='$workspace_root'"
        echo "export AIPMOS_SESSION_INTENT_FILE='$session_intent_file'"
        echo "export AIPMOS_RETRIEVAL_CONFIG='$retrieval_config_file'"
    } >> "$CLAUDE_ENV_FILE"
fi

python3 - "$session_intent_file" <<'PY' >/dev/null 2>&1 || true
import json
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

intent_file = Path(sys.argv[1])
now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

data = {}
if intent_file.exists():
    try:
        data = json.loads(intent_file.read_text())
    except json.JSONDecodeError:
        data = {}

if not data.get("intent", "").strip():
    data["session_id"] = f"{int(time.time())}"
    data["start_time"] = now
else:
    data.setdefault("session_id", f"{int(time.time())}")
    data.setdefault("start_time", now)
data.setdefault("intent", "")
data.setdefault("user_description", "")

intent_file.write_text(json.dumps(data, indent=2))
PY

# --- Compact recovery: emit precompact snapshot if one exists ---
python3 - "$workspace_root" <<'PY' 2>/dev/null || true
import json, sys, os
from pathlib import Path

workspace = Path(sys.argv[1])
snapshot_file = workspace / ".cache" / "claude" / "hooks" / "precompact-state.json"

if not snapshot_file.exists():
    sys.exit(0)

try:
    snapshot = json.loads(snapshot_file.read_text(encoding="utf-8"))
    if not snapshot.get("intent") and not snapshot.get("user_description") and not snapshot.get("modified_files"):
        sys.exit(0)

    lines = ["[COMPACT RECOVERY] Previous session context before compaction:"]
    if snapshot.get("intent"):
        lines.append(f"  Intent: {snapshot['intent']}")
    if snapshot.get("user_description"):
        lines.append(f"  Context: {snapshot['user_description']}")
    if snapshot.get("branch"):
        lines.append(f"  Branch: {snapshot['branch']}")
    if snapshot.get("modified_files"):
        files = snapshot["modified_files"][:5]
        lines.append(f"  Modified: {', '.join(files)}")
    lines.append("  Use this as recovery context. Reload canonical memory as needed.")
    print("\n".join(lines))
except (OSError, json.JSONDecodeError):
    pass
PY

# --- Clear recovery: emit rolling state if one exists and is recent (< 4h) ---
python3 - "$workspace_root" <<'PY' 2>/dev/null || true
import json, sys, time
from pathlib import Path
from datetime import datetime, timezone

workspace = Path(sys.argv[1])
rolling_file = workspace / ".cache" / "claude" / "hooks" / "rolling-state.json"

if not rolling_file.exists():
    sys.exit(0)

try:
    state = json.loads(rolling_file.read_text(encoding="utf-8"))
    # Only show if written within the last 4 hours (stale state isn't helpful)
    ts_str = state.get("ts", "")
    if ts_str:
        try:
            ts = datetime.fromisoformat(ts_str)
            if ts.tzinfo is None:
                ts = ts.replace(tzinfo=timezone.utc)
            age_hours = (datetime.now(timezone.utc) - ts).total_seconds() / 3600
            if age_hours > 4:
                sys.exit(0)
        except ValueError:
            pass

    has_content = state.get("intent") or state.get("user_description") or state.get("transcript")
    if not has_content:
        sys.exit(0)

    lines = ["[CLEAR RECOVERY] Context from session before /clear:"]
    if state.get("intent"):
        lines.append(f"  Intent: {state['intent']}")
    if state.get("user_description"):
        lines.append(f"  Context: {state['user_description']}")
    if state.get("transcript") and not state.get("intent"):
        lines.append(f"  Transcript: {state['transcript']}")
    lines.append("  Session file written to 🤖 AI/memory/sessions/ at session end.")
    print("\n".join(lines))
except (OSError, json.JSONDecodeError):
    pass
PY

# --- Memory freshness check ---
memory_file="$workspace_root/🤖 AI/memory/memory.md"
if [ -f "$memory_file" ]; then
    if [[ "$OSTYPE" == "darwin"* ]]; then
        epoch_modified=$(stat -f %m "$memory_file" 2>/dev/null || echo "0")
    else
        epoch_modified=$(stat -c %Y "$memory_file" 2>/dev/null || echo "0")
    fi
    now_epoch=$(date +%s)
    age_days=$(( (now_epoch - epoch_modified) / 86400 ))
    if [ "$age_days" -gt 7 ]; then
        echo "[MEMORY WARNING] memory.md is $age_days days old. Consider running /refresh-memory."
    fi
fi

# Background: extract summaries for recent sessions that ended via terminal close
# (Stop hook never fires on SIGHUP, so this catches up retroactively)
python3 "$workspace_root/🔧 Automation/scripts/hooks/jsonl_extractor.py" \
    --workspace "$workspace_root" --max-sessions 3 >/dev/null 2>&1 &

# Hook completed successfully
exit 0
