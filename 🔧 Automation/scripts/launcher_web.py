#!/usr/bin/env python3
"""
Session Launcher — web UI for Claude Code session management.

Pairs with the `csession` shell function to resume sessions in the current terminal.

Usage (via shell function):
    csession

Direct:
    python3 launcher_web.py [--port 7329] [--choice-file /tmp/.csession]
"""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
import threading
import webbrowser
from datetime import datetime, timezone
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path
from urllib.parse import urlparse

WORKSPACE = Path(__file__).parent.parent.parent
SESSIONS_DIR = WORKSPACE / "🤖 AI" / "memory" / "sessions"
CLAUDE_PROJECTS_DIR = Path.home() / ".claude" / "projects"
DEFAULT_PORT = 7329
MAX_SESSIONS = 9

# ──────────────────────────────────────────────
# Session data
# ──────────────────────────────────────────────

def _claude_project_dir(workspace: Path) -> Path:
    key = str(workspace).replace("/", "-")
    return CLAUDE_PROJECTS_DIR / key


def _parse_session_file(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    meta: dict[str, str] = {}
    fm = re.search(r"^---\s*\n(.*?)\n---", text, re.DOTALL | re.MULTILINE)
    block = fm.group(1) if fm else text[:500]
    for line in block.splitlines():
        line = re.sub(r"^##\s*", "", line).strip()
        if ":" in line and not line.startswith("#"):
            k, _, v = line.partition(":")
            meta[k.strip()] = v.strip()

    def section(name: str) -> str:
        m = re.search(rf"## {re.escape(name)}\s*\n(.*?)(?=\n## |\Z)", text, re.DOTALL)
        return m.group(1).strip() if m else ""

    return {
        "date": meta.get("date", ""),
        "claude_session_id": meta.get("claude_session_id", ""),
        "start_time": meta.get("start_time", ""),
        "summary": section("Summary"),
        "focus": section("Focus"),
        "open_questions": section("Open Questions"),
    }


def _find_resume_uuid(session: dict, proj_dir: Path) -> str | None:
    stored = session.get("claude_session_id", "").strip()
    if stored and (proj_dir / f"{stored}.jsonl").exists():
        return stored

    start_str = session.get("start_time", "")
    if not start_str:
        return None
    try:
        start_ts = datetime.fromisoformat(start_str.replace("Z", "+00:00")).timestamp()
    except ValueError:
        return None

    end_ts = start_ts + 8 * 3600
    all_files = list(proj_dir.glob("*.jsonl"))
    if not all_files:
        return None

    most_recent = max(all_files, key=lambda f: f.stat().st_mtime)
    candidates = [
        (f.stat().st_size, f.stem)
        for f in all_files
        if f != most_recent and start_ts <= f.stat().st_mtime <= end_ts
    ]
    if not candidates:
        return None
    candidates.sort(reverse=True)
    return candidates[0][1]


MIN_JSONL_BYTES = 40_000   # ignore stub sessions (hook-only, no real work)


_SKIP_PREFIXES = ("<local-command-caveat>", "<command-", "<system-reminder>")


def _first_user_message(jsonl_path: Path) -> tuple[str, str]:
    """Return (first_real_user_text, iso_timestamp) from a JSONL file.

    Skips messages that are slash-command artifacts or system injections.
    """
    try:
        for line in jsonl_path.read_text(encoding="utf-8", errors="ignore").splitlines()[:50]:
            obj = json.loads(line)
            if obj.get("type") != "user":
                continue
            ts = obj.get("timestamp", "")
            content = obj.get("message", {}).get("content", "")
            text = ""
            if isinstance(content, list):
                for c in content:
                    if isinstance(c, dict) and c.get("type") == "text":
                        text = c["text"].strip()
                        break
            elif isinstance(content, str):
                text = content.strip()
            if text and not any(text.startswith(p) for p in _SKIP_PREFIXES):
                return text[:300], ts
    except Exception:
        pass
    return "", ""


def load_sessions() -> list[dict]:
    """Load sessions from JSONL files (ground truth), enriched with MD summaries where available."""
    proj_dir = _claude_project_dir(WORKSPACE)

    # Build UUID → rich MD data index
    md_by_uuid: dict[str, dict] = {}
    if SESSIONS_DIR.exists():
        for md_path in SESSIONS_DIR.glob("*.md"):
            try:
                s = _parse_session_file(md_path)
                uuid = s.get("claude_session_id", "").strip()
                if not uuid:
                    # Try fallback match — store by start_time for later correlation
                    uuid = _find_resume_uuid(s, proj_dir) or ""
                if uuid:
                    oq = ""
                    if s.get("open_questions"):
                        oq = s["open_questions"].split("\n")[0].lstrip("- ").strip()
                    focus = s.get("focus", "")
                    if focus == "Not captured.":
                        focus = ""
                    md_by_uuid[uuid] = {
                        "summary": s.get("summary", ""),
                        "focus": focus,
                        "open_question": oq,
                        "date": s.get("date", ""),
                    }
            except Exception:
                continue

    # Collect real JSONL sessions, newest first (skip the active session)
    all_jsonl = sorted(proj_dir.glob("*.jsonl"), key=lambda f: f.stat().st_mtime, reverse=True)
    active_uuid = all_jsonl[0].stem if all_jsonl else ""
    result = []
    for jf in all_jsonl:
        if len(result) >= MAX_SESSIONS:
            break
        if jf.stem == active_uuid:
            continue  # skip current session
        if jf.stat().st_size < MIN_JSONL_BYTES:
            continue  # skip stubs

        uuid = jf.stem
        first_msg, ts = _first_user_message(jf)
        if not first_msg:
            continue

        # Parse date from JSONL timestamp
        date = ""
        if ts:
            try:
                dt = datetime.fromisoformat(ts.replace("Z", "+00:00"))
                date = dt.strftime("%Y-%m-%d")
            except ValueError:
                pass

        # Enrich with MD data if available
        md = md_by_uuid.get(uuid, {})
        result.append({
            "uuid": uuid,
            "date": md.get("date") or date,
            "summary": md.get("summary") or first_msg,
            "focus": md.get("focus", ""),
            "open_question": md.get("open_question", ""),
        })

    return result


# ──────────────────────────────────────────────
# HTML UI — Technical Minimalist
# ──────────────────────────────────────────────

HTML = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Sessions</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
  <style>
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

    :root {
      --paper:        #F7F7F5;
      --forest:       #1A3C2B;
      --forest-hi:    #254f3a;
      --coral:        #FF8C69;
      --mint:         #9EFFBF;
      --gold:         #F4D35E;
      --grid:         #3A3A38;
      --border:       rgba(58,58,56,0.18);
      --border-mid:   rgba(58,58,56,0.4);
      --text-1:       #1A1A18;
      --text-2:       rgba(26,26,24,0.5);
      --text-3:       rgba(26,26,24,0.28);
      --head:         'Space Grotesk', system-ui, sans-serif;
      --mono:         'JetBrains Mono', 'Courier New', monospace;
      --t:            110ms;
    }

    html, body {
      background: var(--paper);
      color: var(--text-1);
      font-family: var(--head);
      font-size: 14px;
      line-height: 1.5;
      min-height: 100vh;
      -webkit-font-smoothing: antialiased;
    }

    /* ── Page shell ── */
    .page {
      max-width: 1120px;
      margin: 0 auto;
      padding: 48px 40px 80px;
    }

    /* ── Header ── */
    .hdr {
      display: flex;
      justify-content: space-between;
      align-items: flex-end;
      margin-bottom: 40px;
      padding-bottom: 24px;
      border-bottom: 1px solid var(--border-mid);
    }
    .hdr-left {}
    .wordmark {
      font-family: var(--head);
      font-size: 72px;
      font-weight: 700;
      line-height: 0.88;
      letter-spacing: -0.04em;
      color: var(--forest);
    }
    .hdr-sub {
      margin-top: 10px;
      font-family: var(--mono);
      font-size: 12px;
      letter-spacing: 0.12em;
      text-transform: uppercase;
      color: var(--text-3);
    }
    .hdr-sub em { font-style: normal; color: var(--forest); }
    .hdr-right {
      font-family: var(--mono);
      font-size: 12px;
      letter-spacing: 0.12em;
      text-transform: uppercase;
      color: var(--text-3);
      text-align: right;
      padding-bottom: 6px;
    }

    /* ── Grid — shared hairline borders ── */
    /* Outer container supplies top + left edges.
       Each cell supplies its own right + bottom edge.
       This gives a clean CSS-grid "spreadsheet" look. */
    .grid {
      border-top: 1px solid var(--border-mid);
      border-left: 1px solid var(--border-mid);
      display: grid;
      grid-template-columns: repeat(3, 1fr);
    }

    @media (max-width: 760px) { .grid { grid-template-columns: repeat(2, 1fr); } }
    @media (max-width: 480px) { .grid { grid-template-columns: 1fr; } }

    /* ── Card ── */
    .card {
      border-right: 1px solid var(--border-mid);
      border-bottom: 1px solid var(--border-mid);
      padding: 22px 22px 0;
      display: flex;
      flex-direction: column;
      cursor: pointer;
      outline: none;
      transition: background var(--t) ease-out;
      position: relative;
      min-height: 220px;
    }
    .card:hover  { background: rgba(26,60,43,0.04); }
    .card.active { background: rgba(158,255,191,0.14); }
    .card.no-uuid { cursor: default; }
    .card.launched { background: rgba(158,255,191,0.22); }

    /* Top row: index + date */
    .card-top {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 14px;
    }
    .card-idx {
      font-family: var(--mono);
      font-size: 12px;
      font-weight: 500;
      letter-spacing: 0.14em;
      text-transform: uppercase;
      color: var(--text-3);
    }
    .card-date {
      font-family: var(--mono);
      font-size: 12px;
      letter-spacing: 0.1em;
      text-transform: uppercase;
      color: var(--text-1);
    }

    /* Summary */
    .card-summary {
      font-family: var(--head);
      font-size: 16px;
      font-weight: 500;
      line-height: 1.45;
      color: var(--text-1);
      flex: 1;
      display: -webkit-box;
      -webkit-line-clamp: 3;
      -webkit-box-orient: vertical;
      overflow: hidden;
      margin-bottom: 14px;
      letter-spacing: -0.01em;
    }
    .card:hover .card-summary { color: var(--forest); }

    /* Meta tags */
    .card-meta {
      display: flex;
      flex-direction: column;
      gap: 4px;
      margin-bottom: 18px;
    }
    .meta-row {
      font-family: var(--mono);
      font-size: 12px;
      letter-spacing: 0.04em;
      line-height: 1.4;
      color: var(--text-2);
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }
    .meta-focus::before  { content: '↳  '; color: var(--text-3); }
    .meta-q { color: var(--forest); }
    .meta-q::before { content: '?  '; opacity: 0.7; }

    /* Resume button — flush to card edges, no radius */
    .btn {
      display: block;
      width: calc(100% + 44px);
      margin-left: -22px;
      background: var(--forest);
      color: #fff;
      font-family: var(--mono);
      font-size: 12px;
      font-weight: 500;
      letter-spacing: 0.16em;
      text-transform: uppercase;
      border: none;
      padding: 11px 22px;
      border-radius: 0;
      cursor: pointer;
      text-align: left;
      transition: background var(--t) ease-out, color var(--t) ease-out;
      margin-top: auto;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }
    .btn:hover { background: var(--forest-hi); }
    .card.active .btn { background: var(--forest); }
    .btn.loading { background: var(--mint); color: var(--forest); }
    .btn.loading .btn-arrow { opacity: 1; }
    .no-uuid .btn {
      background: transparent;
      color: var(--text-3);
      border-top: 1px solid var(--border);
      cursor: default;
    }
    .btn-arrow {
      opacity: 0.5;
      transition: transform var(--t) ease-out, opacity var(--t) ease-out;
    }
    .card:hover .btn-arrow { transform: translateX(3px); opacity: 1; }

    /* ── Empty state ── */
    .empty-cell {
      grid-column: 1 / -1;
      border-right: 1px solid var(--border-mid);
      border-bottom: 1px solid var(--border-mid);
      padding: 80px 40px;
      text-align: center;
    }
    .empty-label {
      font-family: var(--mono);
      font-size: 10px;
      letter-spacing: 0.14em;
      text-transform: uppercase;
      color: var(--text-3);
      margin-bottom: 10px;
    }
    .empty-msg {
      font-family: var(--head);
      font-size: 22px;
      font-weight: 500;
      color: var(--text-2);
      letter-spacing: -0.02em;
    }

    /* ── Keyboard bar ── */
    .kb {
      margin-top: 20px;
      display: flex;
      gap: 24px;
      flex-wrap: wrap;
    }
    .kb-item {
      display: flex;
      align-items: center;
      gap: 6px;
      font-family: var(--mono);
      font-size: 12px;
      letter-spacing: 0.08em;
      text-transform: uppercase;
      color: var(--text-3);
    }
    kbd {
      font-family: var(--mono);
      font-size: 11px;
      border: 1px solid var(--border-mid);
      border-radius: 2px;
      padding: 1px 5px;
      color: var(--text-2);
    }

    /* ── Launch overlay ── */
    .overlay {
      position: fixed;
      inset: 0;
      background: rgba(247,247,245,0.95);
      display: flex;
      align-items: center;
      justify-content: center;
      z-index: 100;
      opacity: 0;
      pointer-events: none;
      transition: opacity 180ms ease-out;
    }
    .overlay.show { opacity: 1; pointer-events: all; }
    .overlay-inner { text-align: left; }
    .overlay-label {
      font-family: var(--mono);
      font-size: 10px;
      letter-spacing: 0.16em;
      text-transform: uppercase;
      color: var(--text-3);
      margin-bottom: 12px;
    }
    .overlay-title {
      font-family: var(--head);
      font-size: 68px;
      font-weight: 700;
      line-height: 0.88;
      letter-spacing: -0.04em;
      color: var(--forest);
    }
    .overlay-dots {
      margin-top: 28px;
      display: flex;
      gap: 7px;
    }
    .dot {
      width: 6px; height: 6px;
      background: var(--forest);
      border-radius: 50%;
      animation: pulse 1.1s infinite ease-out;
    }
    .dot:nth-child(2) { animation-delay: 0.18s; }
    .dot:nth-child(3) { animation-delay: 0.36s; }
    @keyframes pulse {
      0%, 100% { opacity: 0.15; transform: scale(0.7); }
      40%       { opacity: 1;    transform: scale(1); }
    }
  </style>
</head>
<body>
<div class="page">

  <div class="hdr">
    <div class="hdr-left">
      <div class="wordmark">sessions</div>
      <div class="hdr-sub"><em id="ws">—</em>&nbsp;&nbsp;claude code</div>
    </div>
    <div class="hdr-right" id="count-lbl"></div>
  </div>

  <div class="grid" id="grid"></div>

  <div class="kb" id="kb" style="display:none">
    <div class="kb-item"><kbd>←→↑↓</kbd>&nbsp;navigate</div>
    <div class="kb-item"><kbd>enter</kbd>&nbsp;resume</div>
    <div class="kb-item"><kbd>esc</kbd>&nbsp;close</div>
  </div>

</div>

<div class="overlay" id="overlay">
  <div class="overlay-inner">
    <div class="overlay-label">Launching session</div>
    <div class="overlay-title">resuming<br>session</div>
    <div class="overlay-dots">
      <div class="dot"></div>
      <div class="dot"></div>
      <div class="dot"></div>
    </div>
  </div>
</div>

<script>
  let sessions = [], active = 0;

  const esc = s => s
    .replace(/&/g,'&amp;').replace(/</g,'&lt;')
    .replace(/>/g,'&gt;').replace(/"/g,'&quot;');
  const clip = (s, n) => s && s.length > n ? s.slice(0,n)+'…' : (s||'');

  function fmtDate(d) {
    if (!d) return '';
    return new Date(d+'T12:00:00')
      .toLocaleDateString('en-US',{month:'short',day:'numeric'})
      .toUpperCase();
  }

  function cols() {
    return window.innerWidth > 760 ? 3 : (window.innerWidth > 480 ? 2 : 1);
  }

  function render() {
    const grid = document.getElementById('grid');
    if (!sessions.length) {
      grid.innerHTML = `<div class="empty-cell">
        <div class="empty-label">No sessions found</div>
        <div class="empty-msg">Sessions appear after each Claude Code session ends</div>
      </div>`;
      return;
    }

    grid.innerHTML = sessions.map((s, i) => {
      const hasUuid = !!s.uuid;
      return `
      <div class="card${i===active?' active':''}${!hasUuid?' no-uuid':''}"
           data-i="${i}" tabindex="0"
           onclick="resume(${i})"
           onmouseenter="setActive(${i})"
           onkeydown="cardKey(event,${i})">
        <div class="card-top">
          <span class="card-idx">#${String(i+1).padStart(2,'0')}</span>
          <span class="card-date">${fmtDate(s.date)}</span>
        </div>
        <div class="card-summary">${esc(s.summary||'No summary')}</div>
        <div class="card-meta">
          ${s.focus?`<div class="meta-row meta-focus">${esc(clip(s.focus,82))}</div>`:''}
          ${s.open_question?`<div class="meta-row meta-q">${esc(clip(s.open_question,72))}</div>`:''}
        </div>
        <button class="btn" id="btn-${i}" onclick="event.stopPropagation();resume(${i})">
          <span id="btn-lbl-${i}">${hasUuid?'Resume':'No resume ID'}</span>
          <span class="btn-arrow" id="btn-arr-${i}">${hasUuid?'→':''}</span>
        </button>
      </div>`;
    }).join('');

    document.getElementById('kb').style.display = 'flex';
  }

  function setActive(i) {
    if (active === i) return;
    active = i;
    document.querySelectorAll('.card').forEach((c,ci) =>
      c.classList.toggle('active', ci===i));
  }

  async function resume(i) {
    const s = sessions[i];
    if (!s.uuid) return;

    const btn  = document.getElementById('btn-'+i);
    const lbl  = document.getElementById('btn-lbl-'+i);
    const arr  = document.getElementById('btn-arr-'+i);
    const card = document.querySelector(`.card[data-i="${i}"]`);

    btn.classList.add('loading');
    lbl.textContent = 'Launching';
    arr.textContent = '…';
    card.classList.add('launched');
    document.getElementById('overlay').classList.add('show');

    try {
      await fetch('/api/resume', {
        method: 'POST',
        headers: {'Content-Type':'application/json'},
        body: JSON.stringify({uuid: s.uuid}),
      });
    } catch(_) {}

    setTimeout(() => window.close(), 1500);
  }

  function cardKey(e, i) {
    if (e.key==='Enter'||e.key===' ') { e.preventDefault(); resume(i); }
  }

  document.addEventListener('keydown', e => {
    if (e.key==='Escape') { window.close(); return; }
    if (!sessions.length) return;
    const c = cols();
    const map = {
      ArrowRight: 1, l: 1,
      ArrowLeft: -1, h: -1,
      ArrowDown: c, j: c,
      ArrowUp: -c, k: -c,
    };
    if (e.key in map) {
      e.preventDefault();
      const next = Math.max(0, Math.min(sessions.length-1, active+map[e.key]));
      setActive(next);
      document.querySelectorAll('.card')[next]?.scrollIntoView({block:'nearest'});
    } else if (e.key==='Enter') {
      resume(active);
    }
  });

  (async () => {
    try {
      const d = await (await fetch('/api/sessions')).json();
      sessions = d.sessions || [];
      document.getElementById('ws').textContent = d.workspace || '';
      const n = sessions.length;
      document.getElementById('count-lbl').textContent =
        n + (n===1?' session':' sessions');
    } catch(_) {
      document.getElementById('ws').textContent = 'error';
    }
    render();
  })();
</script>
</body>
</html>"""


# ──────────────────────────────────────────────
# Terminal launcher (macOS)
# ──────────────────────────────────────────────

def _open_in_new_terminal(uuid: str) -> None:
    """Open a new tab in the running terminal app and run claude --resume <uuid>.

    Priority: Warp → Cursor → iTerm2 → Terminal.app
    """
    cmd = f"cd '{WORKSPACE}' && claude --resume {uuid}"
    # Escape for embedding in an AppleScript string literal
    cmd_esc = cmd.replace("\\", "\\\\").replace('"', '\\"')

    script = f'''
set termCmd to "{cmd_esc}"
tell application "System Events"
    set procs to name of every process
end tell

if procs contains "Warp" then
    tell application "Warp" to activate
    delay 0.4
    tell application "System Events"
        keystroke "t" using command down
        delay 0.5
        keystroke termCmd
        key code 36
    end tell
else if procs contains "Cursor" then
    tell application "Cursor" to activate
    delay 0.4
    tell application "System Events"
        keystroke "`" using {{control down, shift down}}
        delay 0.5
        keystroke termCmd
        key code 36
    end tell
else if procs contains "iTerm2" then
    tell application "iTerm2"
        create window with default profile
        tell current session of current window
            write text termCmd
        end tell
        activate
    end tell
else
    tell application "Terminal"
        do script termCmd
        activate
    end tell
end if
'''
    try:
        subprocess.Popen(["osascript", "-e", script])
    except Exception as exc:
        sys.stderr.write(f"launcher_web: could not open terminal: {exc}\n")


# ──────────────────────────────────────────────
# HTTP server
# ──────────────────────────────────────────────

_shutdown_event = threading.Event()
_choice_file: str | None = None


class _Handler(BaseHTTPRequestHandler):
    def log_message(self, *_):
        pass

    def do_GET(self):
        path = urlparse(self.path).path

        if path in ("/", "/index.html"):
            body = HTML.encode()
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", len(body))
            self.end_headers()
            self.wfile.write(body)

        elif path == "/api/sessions":
            data = json.dumps({
                "workspace": WORKSPACE.name,
                "sessions": load_sessions(),
            }).encode()
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", len(data))
            self.end_headers()
            self.wfile.write(data)

        else:
            self.send_response(404)
            self.end_headers()

    def do_POST(self):
        if urlparse(self.path).path == "/api/resume":
            length = int(self.headers.get("Content-Length", 0))
            body = json.loads(self.rfile.read(length) or b"{}")
            uuid = body.get("uuid", "").strip()

            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(b'{"ok":true}')

            if uuid:
                threading.Timer(0.2, lambda: _open_in_new_terminal(uuid)).start()

            threading.Timer(0.6, _shutdown_event.set).start()
        else:
            self.send_response(404)
            self.end_headers()


# ──────────────────────────────────────────────
# Entry point
# ──────────────────────────────────────────────

def main() -> int:
    global _choice_file

    parser = argparse.ArgumentParser(description="Claude session launcher UI")
    parser.add_argument("--port", type=int, default=DEFAULT_PORT)
    parser.add_argument("--choice-file", default="", help="Path to write selected UUID")
    parser.add_argument("--no-browser", action="store_true")
    args = parser.parse_args()

    _choice_file = args.choice_file or None

    try:
        server = HTTPServer(("127.0.0.1", args.port), _Handler)
    except OSError as e:
        sys.stderr.write(f"launcher_web: could not bind port {args.port}: {e}\n")
        return 1

    if not args.no_browser:
        threading.Timer(0.25, lambda: webbrowser.open(f"http://localhost:{args.port}")).start()

    server.timeout = 0.5
    while not _shutdown_event.is_set():
        server.handle_request()

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
