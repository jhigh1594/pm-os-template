# PM-OS Customization Guide

This guide helps you tailor the PM Operating System template to your specific needs.

## Quick Customization Checklist

After running `install.sh`, complete these steps:

- [ ] Add API keys to `.aipmos/environment` and `.mcp.json`
- [ ] Update `GOALS.md` with your quarterly goals
- [ ] Add your products to `📦 Products/`
- [ ] Add company context to `🏢 Company/`
- [ ] Customize `CLAUDE.md` for your workflow
- [ ] Set up your task system in `📋 Tasks/`

---

## 1. API Keys and Integrations

### .aipmos/environment

Add your integration credentials:

```bash
# AgilePlace Integration
AGILEPLACE_API_KEY=your_actual_key_here
AGILEPLACE_USER_ID=your_user_id

# Slack Integration
SLACK_WEBHOOK_URL=https://hooks.slack.com/services/XXX/YYY/ZZZ
SLACK_USER_ID=U123456

# Notion Integration
NOTION_API_KEY=ntn_your_actual_key_here
```

### .mcp.json

Add MCP server credentials:

```json
{
  "mcpServers": {
    "notion": {
      "env": {
        "NOTION_API_KEY": "ntn_your_actual_key_here"
      }
    }
  }
}
```

---

## 2. Goals Configuration (GOALS.md)

### Personal Information

```markdown
**Your Name** | Your Role | Your Company (Product A, Product B, Product C)
```

### Quarterly Goals

Structure each goal with:
- **Target**: Specific, measurable outcome
- **Key initiatives**: 3-5 supporting actions
- **Status**: 🟢 On track / 🟡 At risk / 🔴 Blocked

### Stakeholder Map

Document your key relationships:

| Name | Role | Relationship | Communication Notes |
|------|------|--------------|---------------------|
| Jane | VP Product | Skip-level | Monthly 1:1, prefers executive summaries |
| Mike | Engineering | Partner | Daily standup, async for decisions |

---

## 3. Product Strategy (📦 Products/)

### Directory Structure

```
📦 Products/
├── ProductA/
│   ├── README.md           # Product overview
│   ├── ICP.md              # Ideal customer profile
│   ├── competitive/        # Competitive analysis
│   └── designs/            # Design mockups
├── ProductB/
└── ...
```

### Key Documents to Create

1. **ICP.md** - Ideal Customer Profile
   ```markdown
   # Ideal Customer Profile

   ## Firmographics
   - Company size: 500-10,000 employees
   - Industry: Technology, Financial Services
   - Geography: North America, Europe

   ## Pain Points
   - Challenge 1
   - Challenge 2

   ## Buying Behavior
   - [How they buy]
   ```

2. **ROI-framework.md** - Return on Investment framework
   ```markdown
   # ROI Framework

   ## Value Metrics
   - Time saved: X hours/week
   - Revenue impact: $Y increase
   - Cost reduction: $Z savings

   ## Proof Points
   - Customer A: [Specific result]
   - Customer B: [Specific result]
   ```

---

## 4. Company Context (🏢 Company/)

### competitive-analysis.md

```markdown
# Competitive Landscape

## Primary Competitors
| Competitor | Strength | Weakness | Our Response |
|------------|----------|----------|--------------|
| Competitor A | [Strength] | [Weakness] | [Response] |

## Market Position
- Our differentiator: [X]
- Key messaging: [Y]
```

### customer-research/

Store customer interviews, surveys, and insights:

```
🏢 Company/
├── customer-research/
│   ├── interviews/
│   ├── surveys/
│   └── insights-summary.md
```

---

## 5. Memory Bank (.aipmos/memory-bank/memory.md)

### Current Focus Section

Update this at the start of significant work:

```markdown
## Current Focus

**Active Task**: [What you're working on NOW]

**Recent Completed Work**:
- [Latest accomplishment]
- [Previous accomplishment]
```

### Session History

After important sessions, add entries:

```markdown
### [Date] Session: [Title]
**Planned**: [What was planned]
**Completed**: [What was done]
**Outcome**: [Result/impact]
```

---

## 6. Task System (📋 Tasks/)

### today.md Template

```markdown
# Daily Plan - YYYY-MM-DD

## Focus
[One sentence: What's the main thing today?]

## Priorities
1. [ ] Priority 1
2. [ ] Priority 2
3. [ ] Priority 3

## Meetings
- [Meeting 1] - [Time]

## Notes
- [Any context or blockers]
```

### backlog.md Template

```markdown
# Backlog

## This Week
- [ ] [Task]

## This Month
- [ ] [Task]

## Someday
- [ ] [Task]

## Icebox
- [ ] [Task] - [Reason for deprioritization]
```

---

## 7. Adding Custom Commands

Create new slash commands in `.claude/commands/`:

```markdown
---
name: my-command
description: What this command does
---

# My Custom Command

Instructions for Claude on how to execute this command...
```

---

## 8. Adding Custom Skills

Create skills in `.claude/skills/`:

```markdown
---
name: my-skill
description: When to use this skill
---

# My Custom Skill

Detailed instructions for Claude...
```

---

## Example: Filled-Out GOALS.md

```markdown
# GOALS.md

## Who I Am

**Alex Chen** | Senior Product Manager | TechCorp (Platform, Analytics, Mobile)

Systems-thinking PM focused on developer tools and platform products...

## What I Own

| Product | Description | Key Metrics |
|---------|-------------|-------------|
| **Platform** | Developer platform for API integrations | API calls, developer adoption |
| **Analytics** | Real-time analytics dashboard | DAU, query latency |

## Q1 2026 Goals

### Goal 1: Launch Platform v2 with new API gateway

**Target:** 50% of traffic on new gateway by end of Q1

**Key initiatives:**
- Complete gateway migration (Week 4)
- Developer documentation refresh (Week 6)
- Partner migration program (Week 8)

**Status:** 🟢 On track

## Key Stakeholders

| Name | Role | Relationship | Notes |
|------|------|--------------|-------|
| Sarah | VP Eng | Partner | Weekly sync, technical decisions |
| Tom | CEO | Skip-level | Quarterly review only |
```

---

## Maintenance

### Weekly
- Update `today.md` each morning
- Review and close completed tasks
- Update `memory.md` if focus changed

### Monthly
- Review `backlog.md` and priorities
- Update `GOALS.md` goal status
- Clean up old files

### Quarterly
- Full `GOALS.md` refresh with new goals
- Archive completed work
- Review and update stakeholder map
