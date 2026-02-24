# PM Operating System (PM-OS)

A complete AI-powered Product Management workspace that supercharges your PM workflow with Cursor or Claude Code.

## Quick Start

```bash
# Clone this template
git clone https://github.com/jhigh1594/pm-os-template.git
cd pm-os-template

# Customize your workspace
# Edit these files to add your context:
# - GOALS.md         → Your role, goals, stakeholders
# - .aipmos/environment → Your API keys
# - .aipmos/memory-bank/memory.md → Your current focus

# Open in Claude Code
claude
```

## Setup Checklist

After cloning, run `/onboard` in Curosr or Claude Code to be guided through setup, or manually update:

### Required
- [ ] **GOALS.md** - Add your name, role, company, products, and quarterly goals
- [ ] **CLAUDE.md** - Update company name and product references
- [ ] **.aipmos/memory-bank/memory.md** - Set your current focus

### Optional Integrations
- [ ] **.aipmos/environment** - Add API keys (AgilePlace, Slack, Notion, etc.)
- [ ] **.mcp.json** - Configure MCP servers

## What's Included

### AI Assistant Configuration
- **20+ slash commands** for PM tasks (`/today`, `/think`, `/brainstorm`, `/compete`, etc.)
- **6 PM rule files** defining how to operate as a 10X Product Leader
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
├── .aipmos/              # AI memory and configuration
└── .claude/              # Claude Code configuration
```

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

## Security Notes

**Never commit these files to version control:**
- `.aipmos/environment` - Contains API keys
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
