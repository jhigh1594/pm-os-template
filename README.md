# PM Operating System (PM-OS)

A complete AI-powered Product Management workspace that supercharges your PM workflow with Cursor or Claude Code.

## Quick Start

```bash
# Clone this template
git clone https://github.com/jhigh1594/pm-os-template.git
cd pm-os-template

# Customize your workspace
# Edit these files to add your context:
# - GOALS.md           → Your role, goals, stakeholders
# - 🤖 AI/memory/memory.md → Your current focus

# Open in Claude Code
claude
```

## Setup Checklist

After cloning, run `/onboard` in Curosr or Claude Code to be guided through setup, or manually update:

### Required
- [ ] **GOALS.md** - Add your name, role, company, products, and quarterly goals
- [ ] **CLAUDE.md** - Update company name and product references
- [ ] **🤖 AI/memory/memory.md** - Set your current focus

### Optional Integrations
- [ ] **.env** - Add API keys at project root
- [ ] **.mcp.json** - Configure MCP servers

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
| `/today` | Daily planning workflow |
| `/think` | Strategic thinking mode |
| `/brainstorm` | Persona-based brainstorming |
| `/compete` | Competitive intelligence |
| `/granola` | Extract meeting notes |
| `/discover` | Customer discovery workflow |
| `/spec` | Product spec writer |
| `/prioritize` | Prioritization framework |
| `/onboard` | Workspace setup guide |

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
