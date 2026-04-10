# PM Operating System (PM-OS)

A complete AI-powered Product Management workspace that supercharges your PM workflow with Cursor or Claude Code.

## Why this exists

PM work scatters across trackers, decks, docs, and meeting notes. Context drops between tools and between sessions, so the same story gets re-explained and decisions get re-derived. This repo is a **single place** to hold product context, goals, and rituals so assistants and humans share one source of truth.

## What it is

**PM-OS** is a **git-backed workspace template**: a folder system plus Cursor/Claude Code configuration—commands, rules, skills, automation, and optional MCP hooks. It is not a hosted product; it is the environment Jon clones and fills in for a role, product, and company.

## So what

- **Onboarding and focus** — structured setup (`/onboard`) so the first 30–90 days have explicit goals and context files.
- **Daily execution** — `/today` and related automation pull tracker and notes data into a repeatable planning loop.
- **Consistent PM judgment** — shared rules and memory so AI help aligns with how Jon wants to decide, communicate, and ship.

**[Workflow cheatsheet](📝%20Docs/guides/workflow-cheatsheet.md)** — activity → command and skill entry points (feature lifecycle, cadence workflows, intel routing).

## Quick Start

```bash
# 1. Clone this template
git clone https://github.com/jhigh1594/pm-os-template.git
cd pm-os-template

# 2. Open in Claude Code or Cursor
claude    # for Claude Code
# or
cursor .  # for Cursor IDE

# 3. Run the onboarding command
/onboard
```

That's it! The `/onboard` command will guide you through setting up your workspace.

## What `/onboard` Does

The `/onboard` command provides an interactive 30-60-90 day framework to:

1. **Set up your context** — Customize GOALS.md with your role, products, and stakeholders
2. **Configure your task tracker** — Choose from Jira, Linear, Asana, GitHub Issues, or AgilePlace
3. **Set up your memory** — Update memory.md with your current focus and product context
4. **Plan your first 30 days** — Get a structured learning plan for your new role/product

Just run `/onboard` and answer the questions to get started.

---

## Manual Setup (Alternative)

If you prefer to manually configure without `/onboard`, update these files:

### Required
- [ ] **GOALS.md** — Add your name, role, company, products, and quarterly goals
- [ ] **CLAUDE.md** — Update company name and product references
- [ ] **🤖 AI/memory/memory.md** — Set your current focus

### Optional Integrations
- [ ] **.env** — Add API keys at project root (see `.env.example`)
- [ ] **.mcp.json** — Configure MCP servers
- [ ] **🔧 Automation/scripts/today_cmd/config.yaml** — Set task tracker type and credentials

---

## What's Included

### AI Assistant Configuration
- **54 slash commands** for PM tasks (`/today`, `/think`, `/brainstorm`, `/compete`, etc.)
- **7 PM rule files** defining how to operate as a 10X Product Leader
- **59 installable skills** via the skills library (`/spec`, `/discover`, `/design-brief`, etc.)
- **Ruler integration** for multi-AI sync (Claude Code, Cursor, etc.)
- **Automation scripts** for daily planning and meeting notes

### Workspace Structure
```
├── GOALS.md              # Your identity, goals, stakeholders
├── CLAUDE.md             # AI assistant instructions
├── 📦 Products/          # Product strategy, ICP, ROI
├── 📁 Workflows/         # Repeatable processes
├── 📋 Tasks/             # Daily planning and backlog
├── 📚 Knowledge/         # Research and reference
├── 🏢 Company/           # Business context
├── 📊 Analytics/         # Data and dashboards
├── 🔧 Automation/        # Scripts and tools
├── 📝 Docs/              # Memos and documentation
├── 📽️ Presentations/    # Corporate deck templates
├── 🚀 Prototypes/        # Interactive mockups
├── 🤖 AI/                # AI memory and patterns
│   ├── memory/           # Context persistence
│   └── patterns/         # Learned patterns
├── .claude/              # Claude Code configuration
│   ├── commands/         # 54 slash commands
│   ├── rules/            # 7 PM rule files
│   └── skills/           # 59 installable skills
└── .ruler/               # Multi-AI sync (Ruler)
```

### PM Rules System

The rules system uses progressive disclosure:

| Rule | Purpose |
|------|---------|
| `pm-operating-principles.mdc` | **Always loaded** - Core operating principles, quick references |
| `mental-models.mdc` | Strategic thinking, investment decisions |
| `decision-framework.mdc` | Decision documentation, reviews |
| `frameworks-as-tools.mdc` | Framework selection, when to abandon |
| `communication-standards.mdc` | Audience patterns, stakeholder alignment |
| `product-sense.mdc` | Product critiques, taste development |
| `agileplace-cli.mdc` | Task tracker CLI integration |

### `/today` Daily Workflow

The `/today` command runs an automated daily planning workflow:

1. **Backup** yesterday's plan → `yesterday.md`
2. **Collect** data from your task tracker, meetings (Granola), RSS feeds, and weekly priorities
3. **Analyze** using LLM synthesis to surface insights and commitments
4. **Interactive triage** — carry forward, complete, or archive yesterday's items
5. **Generate** your daily plan with Top 3 Priorities, insights, and one-step-better recommendations

**Configurable task tracker** — supports multiple backends:
- **stub** (demo mode with example tasks)
- **AgilePlace**, **Jira**, **Linear**, **Asana**, **GitHub Issues**
- **Custom** — write your own collector

Configure via `🔧 Automation/scripts/today_cmd/config.yaml` or during first `/today` run.

### Skills Library

59 installable skills covering the full PM spectrum:

| Category | Examples |
|----------|----------|
| **Product Strategy** | `/strategic-thinking`, `/positioning-craft`, `/business-reasoning` |
| **Discovery** | `/discovery`, `/continuous-discovery`, `/customer-knowledge-audit` |
| **Execution** | `/execution-delivery`, `/ship-decisions`, `/mvp` |
| **AI Product** | `/ai-product-patterns`, `/ai-startup-building`, `/dex-improve` |
| **Communication** | `/strategic-storytelling`, `/confident-speaking`, `/exec-comms` |
| **Growth** | `/growth-embedded`, `/pricing-intelligence`, `/metrics-frameworks` |
| **Leadership** | `/stakeholder-craft`, `/influence-craft`, `/culture-craft` |

Skills live in `.claude/skills/` — see `SKILLS-INDEX.md` for the full catalog.

## Available Commands

| Command | Purpose |
|---------|---------|
| `/onboard` | **START HERE** - Workspace setup guide |
| `/today` | Daily planning workflow with task tracker integration |
| `/think` | Strategic thinking mode |
| `/brainstorm` | Persona-based brainstorming |
| `/compete` | Competitive intelligence |
| `/granola` | Extract meeting notes |
| `/discover` | Customer discovery workflow |
| `/spec` | Product spec writer |
| `/prioritize` | Prioritization framework |
| `/research` | Deep research synthesis |
| `/narrative` | Strategic storytelling |
| `/ship` | Launch planning |
| `/learn` | Post-launch learning |

See `.claude/commands/COMMAND-REFERENCE.md` for the full list of 54 commands.

## Ruler Integration

This workspace uses [Ruler](https://github.com/jhigh1594/ruler) for multi-AI configuration sync:

- Edit `.ruler/AGENTS.md` to update AI instructions
- Run `ruler apply` to sync to Claude Code, Cursor, etc.
- Keeps all AI tools reading from the same source of truth

### MCP Server Templates

The `.ruler/ruler.toml` includes pre-configured MCP servers:
- **Fetch** — Web content fetching
- **Notion** — Notion workspace integration
- **EXA** — AI-powered web search and research

Uncomment and configure the ones you need.

## Security Notes

**Never commit these files to version control:**
- `.env` - Contains API keys
- `.mcp.json` - Contains API keys
- `config.yaml` with real credentials (use the template version)

All are already in `.gitignore`.

## Customization

This is your workspace. Make it yours:
- Add your own commands in `.claude/commands/`
- Install skills from the library in `.claude/skills/`
- Add your PM frameworks in `🎓 Product-Management/`
- Add your product docs in `📦 Products/`
- Customize the automation scripts in `🔧 Automation/`
- Add your own task tracker collector in `🔧 Automation/scripts/today_cmd/collectors/`

---

Built for Product Managers who want to work smarter, not harder.
