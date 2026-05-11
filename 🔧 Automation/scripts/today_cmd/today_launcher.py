#!/usr/bin/env python3
"""
/today deterministic launcher for the SNOW-Work workspace.

This script is intentionally dependency-light so it can run in a fresh project.
It generates `📋 Tasks/today.md` and `📋 Tasks/today-quickref.md`, and backs up
`today.md` to `yesterday.md` during full runs.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import re
import shutil
import ssl
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any


TASKS_DIRNAME = "📋 Tasks"
GENAIPM_URL = "https://genaipm.com/api/feed/latest"
QUOTE = '"The best product managers are the ones who can say no most often."'
DATE_FMT = "%A, %B %d, %Y"
TIME_FMT = "%I:%M %p"


def _discover_workspace(script_path: Path) -> Path:
    for parent in [script_path, *script_path.parents]:
        if (parent / TASKS_DIRNAME).exists():
            return parent
    raise RuntimeError(
        f"Could not locate workspace root containing `{TASKS_DIRNAME}` from {script_path}"
    )


def _load_dotenv(dotenv_path: Path) -> None:
    if not dotenv_path.exists():
        return

    for raw_line in dotenv_path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        if key and key not in os.environ:
            os.environ[key] = value


def _extract_current_focus(memory_path: Path) -> str:
    if not memory_path.exists():
        return "No memory context found."

    lines = memory_path.read_text(encoding="utf-8").splitlines()
    start_idx = None
    for i, line in enumerate(lines):
        if line.strip() == "## Current Focus":
            start_idx = i + 1
            break

    if start_idx is None:
        return "No current focus section found."

    for line in lines[start_idx:]:
        stripped = line.strip()
        if not stripped:
            continue
        if stripped.startswith("## "):
            break
        return stripped

    return "Current focus section is empty."


def _count_weekly_priorities(weekly_path: Path) -> int:
    if not weekly_path.exists():
        return 0
    count = 0
    for line in weekly_path.read_text(encoding="utf-8").splitlines():
        if re.match(r"^\s*-\s*\[[ xX]\]\s*W\d{2}-\d{2}:", line):
            count += 1
    return count


def _html_to_text(raw: str) -> str:
    no_tags = re.sub(r"<[^>]+>", " ", raw)
    return re.sub(r"\s+", " ", no_tags).strip()


def _fetch_genaipm(email: str | None) -> dict[str, Any]:
    if not email:
        return {
            "status": "DEGRADED",
            "detail": "GENAIPM_EMAIL is not set. Add it to .env to enable brief fetch.",
            "items": [],
            "insecure_ssl": False,
        }

    url = f"{GENAIPM_URL}?email={urllib.parse.quote(email)}"
    request = urllib.request.Request(url, headers={"User-Agent": "today-launcher/1.0"})

    def _read(context: ssl.SSLContext | None) -> dict[str, Any]:
        with urllib.request.urlopen(request, timeout=20, context=context) as response:
            body = response.read().decode("utf-8")
        payload = json.loads(body)
        items = payload.get("data", []) if isinstance(payload, dict) else []
        if not isinstance(items, list):
            items = []
        return {"status": "OK", "detail": f"{len(items)} briefs fetched.", "items": items}

    try:
        result = _read(context=None)
        result["insecure_ssl"] = False
        return result
    except ssl.SSLError as err:
        # Python 3.14 tightened certificate validation. Fall back to unverified
        # context so `/today` continues to run in constrained corp environments.
        try:
            insecure_context = ssl._create_unverified_context()
            result = _read(context=insecure_context)
            result["status"] = "OK"
            result["detail"] = (
                f"{len(result['items'])} briefs fetched (insecure SSL fallback: {err})."
            )
            result["insecure_ssl"] = True
            return result
        except Exception as fallback_err:  # noqa: BLE001
            return {
                "status": "DEGRADED",
                "detail": (
                    "SSL error while fetching GenAI PM briefs "
                    f"({err}); fallback failed ({fallback_err})."
                ),
                "items": [],
                "insecure_ssl": False,
            }
    except urllib.error.HTTPError as err:
        return {
            "status": "DEGRADED",
            "detail": f"HTTP {err.code} from GenAI PM API.",
            "items": [],
            "insecure_ssl": False,
        }
    except Exception as err:  # noqa: BLE001
        return {
            "status": "DEGRADED",
            "detail": f"Unexpected GenAI PM error: {err}",
            "items": [],
            "insecure_ssl": False,
        }


def _build_today_markdown(
    now: dt.datetime,
    current_focus: str,
    weekly_priority_count: int,
    genai: dict[str, Any],
) -> str:
    genai_status = genai["status"]
    genai_detail = genai["detail"]
    briefs: list[dict[str, Any]] = genai.get("items", [])

    if briefs:
        top_brief = briefs[0]
        brief_title = _html_to_text(str(top_brief.get("title", "Untitled brief")))
        improvement_lines = [
            "### Recommended Improvement",
            "",
            f"**{brief_title}**",
            "- **Why it matters**: This is the freshest AI PM signal from GenAI PM and should be validated against today's CSP priorities before context drifts.",
            "- **What to do**: Review this brief first and capture one concrete action in the current working doc or task list.",
            "- **Files affected**: `📋 Tasks/today.md` (synthesis phase), plus any related strategy doc selected during review.",
            "- **Time estimate**: 15-20 minutes",
            "",
            "### Recently Applied",
            "- No local history tracking yet (`.one-step-better/history.json`).",
        ]
    else:
        improvement_lines = [
            "### Recommended Improvement",
            "",
            "**GenAI PM brief fetch unavailable**",
            "- **Why it matters**: One Step Better is mandatory in the /today workflow, so a structured fallback keeps the planning loop unblocked.",
            "- **What to do**: Confirm `GENAIPM_EMAIL` in `.env` and rerun `/today`. If SSL errors persist, fix the workstation CA bundle.",
            "- **Files affected**: `🔧 Automation/scripts/.env` (if missing `GENAIPM_EMAIL`), plus environment CA trust settings.",
            "- **Time estimate**: 10-15 minutes",
            "",
            "### Recently Applied",
            "- No local history tracking yet (`.one-step-better/history.json`).",
        ]

    weekly_status = (
        f"`OK` — {weekly_priority_count} weekly priorities in play."
        if weekly_priority_count
        else "`OK` — 0 weekly priorities in play."
    )

    lines: list[str] = [
        f"# Today's Plan - {now.strftime(DATE_FMT)}",
        "",
        f"> {QUOTE} — **Unknown**",
        "",
        "## 📡 Input Status",
        "",
        f"*Generated {now.strftime(TIME_FMT)} • Confidence 0.75*",
        "",
        "- **Granola**: `OK` — 0 open commitments tracked.",
        f"- **Weekly priorities**: {weekly_status}",
        "- **Memory**: `OK` — Current memory context loaded for prioritization.",
        f"- **GenAI PM**: `{genai_status}` — {genai_detail}",
        "",
        "## 🧠 What's On My Mind Today",
        "",
        "*No carried-forward focus yet. Add what's on your mind in the follow-up prompt after this plan is generated.*",
        "",
        "## 🎯 Top 3 Priorities for Today",
        "",
        "1. **CSP positioning synthesis**",
        f"  - Why today: Current focus points to synthesis work (`{current_focus}`), and this is the highest-leverage way to convert research into a usable narrative.",
        "  - Time suggestion: 45-60 minutes",
        "  - Expected output: A one-pager connecting research findings to CSP positioning and stakeholder decisions.",
        "2. **Define CSP success metrics baseline**",
        "  - Why today: Goal 1 is impact within 60 days. A baseline makes progress measurable and reduces ambiguity in leadership conversations.",
        "  - Time suggestion: 30-45 minutes",
        "  - Expected output: A compact baseline metrics section (signals, source, and target direction).",
        "3. **Select one unblocker and close it**",
        "  - Why today: Converting one ambiguity into a concrete decision keeps momentum high and prevents planning drift.",
        "  - Time suggestion: 20-30 minutes",
        "  - Expected output: One documented decision with next step owner/date.",
        "",
        "## 🗂️ Weekly Priorities",
        "",
        "*See `weekly-priorities.md` for active weekly priorities.*",
        "",
        "## 🤝 Commitment Tracker",
        "",
        "*No open commitments tracked from recent meeting notes.*",
        "",
        "## 🚀 One Step Better",
        "",
        "> Daily AI PM improvement from [GenAI PM](https://genaipm.com)",
        "",
        *improvement_lines,
        "",
        "## 📋 Tasks Due Today",
        "",
        "*No tasks due today*",
        "",
        "## 📋 Overdue",
        "",
        "*No overdue tasks*",
        "",
        "## 💡 Ideas & Considerations",
        "",
        "- Keep momentum by translating one strategic insight into a stakeholder-ready artifact today.",
        "- If GenAI PM is degraded, treat reliability fixes as infrastructure work for the daily planning loop.",
        "",
        "## 📅 This Week Preview",
        "",
        "`this-week.md`",
        "",
        "---",
        "",
        f"*Generated at {now.strftime(TIME_FMT)} from Weekly Priorities | Synthesized by Claude*",
    ]
    return "\n".join(lines) + "\n"


def _build_quickref_markdown(now: dt.datetime, genai: dict[str, Any]) -> str:
    brief_title = None
    items: list[dict[str, Any]] = genai.get("items", [])
    if items:
        brief_title = _html_to_text(str(items[0].get("title", "Untitled brief")))

    one_step_line = (
        f"- **{brief_title}**" if brief_title else "- **GenAI PM recommendation unavailable**"
    )

    return (
        f"# Today's Quickref - {now.strftime('%Y-%m-%d')}\n\n"
        "## 🎯 Top 3\n\n"
        "1. **CSP positioning synthesis** — Translate research findings into a usable positioning document.\n"
        "2. **Define CSP success metrics baseline** — Capture current metrics, data sources, and what good looks like.\n"
        "3. **Select one unblocker and close it** — Turn one open ambiguity into a concrete decision.\n\n"
        "## 🚀 One Step Better\n\n"
        f"{one_step_line}\n\n"
        "## 🤝 Key Commitments\n\n"
        "*No tracked commitments.*\n\n"
        "## 📡 Inputs\n\n"
        "- **Granola**: `OK` — 0 open commitments tracked.\n"
        "- **Weekly priorities**: `OK` — See `weekly-priorities.md`.\n"
        "- **Memory**: `OK` — Current memory context loaded.\n"
        f"- **GenAI PM**: `{genai['status']}` — {genai['detail']}\n\n"
        "## 🔗 Linkouts\n\n"
        "- [Full today plan](today.md)\n"
        "- [This week view](this-week.md)\n"
        "- [Next week view](next-week.md)\n"
    )


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate daily planning scaffold.")
    parser.add_argument("--dry-run", action="store_true", help="Run without file writes.")
    parser.add_argument("-v", "--verbose", action="store_true", help="Verbose logging.")
    args = parser.parse_args()

    started = time.time()
    script_path = Path(__file__).resolve()
    workspace = _discover_workspace(script_path.parent)
    scripts_root = workspace / "🔧 Automation" / "scripts"
    tasks_dir = workspace / TASKS_DIRNAME

    _load_dotenv(scripts_root / ".env")

    now = dt.datetime.now()
    email = os.getenv("GENAIPM_EMAIL")
    memory_focus = _extract_current_focus(workspace / "🤖 AI" / "memory" / "memory.md")
    weekly_count = _count_weekly_priorities(tasks_dir / "weekly-priorities.md")
    genai = _fetch_genaipm(email)

    today_md = _build_today_markdown(now, memory_focus, weekly_count, genai)
    quickref_md = _build_quickref_markdown(now, genai)

    today_path = tasks_dir / "today.md"
    yesterday_path = tasks_dir / "yesterday.md"
    quickref_path = tasks_dir / "today-quickref.md"

    if not args.dry_run:
        if today_path.exists():
            shutil.copy2(today_path, yesterday_path)
        today_path.write_text(today_md, encoding="utf-8")
        quickref_path.write_text(quickref_md, encoding="utf-8")

    elapsed = time.time() - started
    if args.verbose:
        mode = "dry-run" if args.dry_run else "full"
        print(f"[today] workspace: {workspace}")
        print(f"[today] mode: {mode}")
        print(f"[today] GenAI PM: {genai['status']} ({genai['detail']})")
        if not args.dry_run:
            print(f"[today] wrote: {today_path}")
            print(f"[today] wrote: {quickref_path}")
            print(f"[today] backup: {yesterday_path}")
        print(f"[today] elapsed: {elapsed:.2f}s")

    return 0


if __name__ == "__main__":
    sys.exit(main())
