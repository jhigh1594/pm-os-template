# Getting started: PM-OS in Cursor

You already have Cursor. This guide gets the [PM-OS template](https://github.com/jhigh1594/pm-os-template) onto your machine and personalized. Pick a path below.

**You end up with:** a local folder for goals, tasks, and product context, plus slash commands like `/onboard` and `/today` in Cursor Agent.

**Repo URL (both paths):** `https://github.com/jhigh1594/pm-os-template.git`  
Use a different URL only if whoever shared this doc pointed you at a fork.

---

## If you're lazy

Let Claude Code install Git, clone the repo, and tell you what to do next. About 5 minutes of your time if Git is not already on the machine.

### 1. Open a terminal

Either:

- **Cursor:** **Terminal → New Terminal**
- **Mac/Windows:** your normal Terminal or PowerShell app

### 2. Start Claude Code

```bash
claude
```

Don't have Claude Code yet? Install it from [https://docs.anthropic.com/en/docs/claude-code](https://docs.anthropic.com/en/docs/claude-code), then run `claude` again.

### 3. Paste this prompt

Copy everything in the block and send it as your first message:

```
I want to set up the PM-OS template on this computer for use in Cursor.

Do the following for me, step by step, and tell me what you're doing as you go:

1. Check if Git is installed (`git --version`). If not, install it:
   - macOS: try `xcode-select --install` first; if that doesn't work, tell me to install from https://git-scm.com/download/mac
   - Windows: tell me to install from https://git-scm.com/download/win and reopen Cursor after install
   - Linux: use the appropriate package manager (e.g. apt install git)

2. Clone this repo into my Documents folder (create the folder if needed):
   https://github.com/jhigh1594/pm-os-template.git

3. When clone finishes, give me the exact full path to the cloned folder and these next steps:
   - Quit and reopen Cursor if Git was just installed
   - File → Open Folder → select that path
   - Trust the workspace when asked
   - Open Agent and run /onboard

Stop and ask me before anything that needs my password or admin approval.
```

### 4. Finish in Cursor

When Claude Code is done:

1. **File → Open Folder…** and select the folder it created (usually `pm-os-template` inside Documents).
2. Trust the workspace if Cursor asks.
3. Open **Agent** and run:

```
/onboard
```

Answer one question at a time. That personalizes `GOALS.md`, memory, and your task tracker settings.

Optional: run `/today dry` after onboarding to test daily planning. If Jon uses Granola on a Mac, `/onboard` can install a daily meeting export (LaunchAgent) after explicit approval.

---

## If you're slightly more interested

Manual setup in Cursor. About 30 minutes. No terminal required for the clone step.

### What you need

| | |
|---|---|
| **Cursor** | Installed and signed in |
| **Git** | Must be on your computer before clone works |
| **GitHub** | Free account if the clone asks you to sign in |

Save the project somewhere local (e.g. `Documents`). Skip iCloud Desktop or OneDrive if Git acts weird.

---

### Step 1: Install Git

Cursor's **Clone Git Repository** only works if Git is installed. Without it, the command may be missing or clone will error.

**Check first:** In Cursor, **Terminal → New Terminal**, then:

```bash
git --version
```

See `git version 2.x.x`? Jump to Step 2.

See an error? Install Git, then **quit Cursor completely and reopen it.**

| OS | Install |
|----|---------|
| **Mac** | Terminal → `xcode-select --install` (or [git-scm.com/download/mac](https://git-scm.com/download/mac)) |
| **Windows** | [git-scm.com/download/win](https://git-scm.com/download/win), accept defaults, restart Cursor |
| **Linux** | `sudo apt install git` (or your distro's package manager) |

---

### Step 2: Clone in Cursor

1. `Cmd+Shift+P` (Mac) or `Ctrl+Shift+P` (Windows) → **Git: Clone** (or **Clone Git Repository**).
2. Paste: `https://github.com/jhigh1594/pm-os-template.git`
3. Sign in to GitHub if prompted. Password field = [Personal Access Token](https://github.com/settings/tokens), not your GitHub password.
4. Pick a parent folder (e.g. Documents). Cursor creates `pm-os-template` inside it.
5. Click **Open** when clone finishes.
6. Trust the workspace.

Confirm you see `GOALS.md` and folders like `📋 Tasks` and `.cursor` in the file tree. Open the **repo root**, not a subfolder.

---

### Step 3: Run `/onboard`

Open **Agent** and type:

```
/onboard
```

The assistant asks one question at a time (four steps). It updates your goals, memory, and task tracker config. Stub tracker mode is fine if you do not use Jira or Linear yet.

---

### Step 4: Optional smoke test

```
/today dry
```

Dry run of the daily planning workflow. If it fails, you can still use Agent for everything else. Full `/today` may need Python later; `/onboard` will flag that.

**Cursor slash commands in this repo:** `/onboard`, `/today`, `/granola`. More live under `.claude/commands/` (use natural language or copy into `.cursor/commands/` for extra `/` shortcuts).

---

### Stuck?

| Problem | Fix |
|---------|-----|
| No **Clone Git Repository** in palette | Finish Step 1, restart Cursor, confirm `git --version` |
| Clone auth fails | GitHub sign-in or Personal Access Token |
| No `/onboard` | Repo root open? Type `/` in Agent to list commands |
| Agent ignores context | New Agent chat; ask it to read `GOALS.md` first |

More commands: `.claude/commands/COMMAND-REFERENCE.md`  
Workflow map: `📝 Docs/guides/workflow-cheatsheet.md`

---

## After setup

1. Open this folder in Cursor each day.
2. Run **`/today`** for planning.
3. Update **`GOALS.md`** and **`🤖 AI/memory/memory.md`** when priorities shift.
4. Pull updates via **Source Control → Pull** when you want template fixes from upstream.

Template issues: [github.com/jhigh1594/pm-os-template/issues](https://github.com/jhigh1594/pm-os-template/issues)  
Full readme: [README.md](../../README.md)
