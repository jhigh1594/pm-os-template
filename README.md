# PM Operating System (PM-OS) Template

A complete AI-powered Product Management workspace template that supercharges your PM workflow with Claude Code and intelligent automation.

## What's Included

### 🤖 AI Assistant Configuration
- **20+ slash commands** for common PM tasks (`/today`, `/think`, `/brainstorm`, `/compete`, etc.)
- **45+ specialized skills** for PRD writing, competitive analysis, strategic thinking, and more
- **6 PM rule files** defining how to operate as a 10X Product Leader

### 📁 Workspace Structure
```
PM-Workspace/
├── GOALS.md              # Identity, ownership, quarterly goals
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

### 🧠 AIPMOS (AI Product Management Operating System)
- **Memory system** for persistent context across sessions
- **Pattern learning** from your workflow habits
- **Predictive suggestions** based on your work patterns
- **Executive intelligence** for goal alignment

## Quick Start

### Prerequisites
- [Claude Code](https://claude.ai/code) installed
- Git
- (Optional) API keys for Notion, Slack, or other integrations

### Installation

```bash
# Clone or download this template
git clone <repository-url> pm-os-template
cd pm-os-template

# Run the installer
./install.sh

# Or specify a custom location
./install.sh ~/My-PM-Workspace
```

The installer will prompt you for:
- Your name and role
- Your company
- Your products

### After Installation

1. **Add your API keys** (see [Security Notes](#security-notes)):
   ```bash
   # Edit these files with your keys
   vim ~/PM-Workspace/.aipmos/environment
   vim ~/PM-Workspace/.mcp.json
   ```

2. **Install optional integrations**:

   **Pendo CLI** (for `/pendo` command):
   ```bash
   cd ~/
   git clone https://github.com/jhigh1594/pendo-cli.git
   cd pendo-cli
   cp .env.example .env
   # Edit .env with your Pendo credentials
   ```

3. **Customize your goals**:
   ```bash
   vim ~/PM-Workspace/GOALS.md
   ```

4. **Open in Claude Code**:
   ```bash
   cd ~/PM-Workspace
   claude
   ```

## Available Commands

Once in Claude Code, use these slash commands:

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

And 40+ more skills for every PM need.

## Security Notes

⚠️ **This template does NOT include any API keys or personal data.**

The following files require your own credentials:
- `.aipmos/environment` - API keys for integrations
- `.mcp.json` - MCP server credentials

**Never commit these files to version control.** They're already in `.gitignore`.

## Documentation

- [Customization Guide](docs/CUSTOMIZATION-GUIDE.md) - How to tailor the template
- [Security Remediation](docs/SECURITY-REMEDIATION.md) - If you're rotating keys from an existing setup

## Contributing

This template is designed to be forked and customized. Feel free to:
- Add your own commands and skills
- Modify the workspace structure
- Share improvements with the community

## License

MIT License - Use freely for personal and commercial purposes.

---

Built with ❤️ for Product Managers who want to work smarter, not harder.
