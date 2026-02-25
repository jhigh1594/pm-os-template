# PM Operating System (PM-OS)

A complete AI-powered Product Management workspace that supercharges your PM workflow with Cursor or Claude Code.

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
2. **Configure your memory** — Update memory.md with your current focus and product context
3. **Plan your first 30 days** — Get a structured learning plan for your new role/product
4. **Identify quick wins** — Find opportunities to build credibility early

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

---

## What's Included

### AI Assistant Configuration
- **35+ slash commands** for PM tasks (`/today`, `/think`, `/brainstorm`, `/compete`, etc.)
- **6 PM rule files** defining how to operate as a 10X Product Leader
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
├── 🔧 Automation/        # Scripts and tools
├── 🤖 AI/                # AI memory and patterns
│   ├── memory/           # Context persistence
│   └── patterns/         # Learned patterns
├── .claude/              # Claude Code configuration
└── .ruler/               # Multi-AI sync (Ruler)
```

### PM Rules System

The rules system uses progressive disclosure:

| Rule | Purpose |
|------|---------|
| `pm-core.mdc` | **Always loaded** - Quick references, conflict resolution |
| `pm-mental-models.mdc` | Strategic thinking, investment decisions |
| `pm-decision-detail.mdc` | Decision documentation, reviews |
| `pm-frameworks.mdc` | Framework selection, when to abandon |
| `pm-communication.mdc` | Audience patterns, stakeholder alignment |
| `pm-product-sense.mdc` | Product critiques, taste development |

## Available Commands

| Command | Purpose |
|---------|---------|
| `/onboard` | **START HERE** - Workspace setup guide |
| `/today` | Daily planning workflow |
| `/think` | Strategic thinking mode |
| `/brainstorm` | Persona-based brainstorming |
| `/compete` | Competitive intelligence |
| `/granola` | Extract meeting notes |
| `/discover` | Customer discovery workflow |
| `/spec` | Product spec writer |
| `/prioritize` | Prioritization framework |

See `.claude/commands/COMMAND-REFERENCE.md` for the full list.

## Ruler Integration

This workspace uses [Ruler](https://github.com/jhigh1594/ruler) for multi-AI configuration sync:

- Edit `.ruler/AGENTS.md` to update AI instructions
- Run `ruler apply` to sync to Claude Code, Cursor, etc.
- Keeps all AI tools reading from the same source of truth

## Security Notes

**Never commit these files to version control:**
- `.env` - Contains API keys
- `.mcp.json` - Contains API keys

Both are already in `.gitignore`.

## Customization

This is your workspace. Make it yours:
- Add your own commands in `.claude/commands/`
- Add your PM frameworks in `Product-Management/`
- Add your product docs in `Products/`
- Customize the automation scripts in `Automation/`

---

Built for Product Managers who want to work smarter, not harder.
