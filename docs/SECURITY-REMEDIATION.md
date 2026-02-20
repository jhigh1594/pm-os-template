# Security Remediation Guide

This document provides instructions for securing your PM-OS workspace and rotating any exposed credentials.

## ⚠️ If You're Coming From an Existing Setup

If you've identified exposed credentials in your existing workspace, **rotate them immediately**:

### 1. Rotate Notion API Key

1. Go to https://www.notion.so/my-integrations
2. Find the integration you want to rotate
3. Click on it to open settings
4. Click **"Reset"** next to the Internal Integration Token
5. Copy the new key
6. Update in **both** locations:
   - `.aipmos/environment` → `NOTION_API_KEY=`
   - `.mcp.json` → `"NOTION_API_KEY":`

### 2. Rotate Gamma API Key

1. Go to Gamma.app settings
2. Navigate to API settings
3. Generate a new API key
4. Update `.mcp.json` → `"GAMMA_API_KEY":`

### 3. Rotate Any Other Exposed Keys

For any other services, follow their respective key rotation procedures.

---

## Preventing Future Leaks

### .gitignore Configuration

Your PM-OS workspace includes a `.gitignore` with these entries:

```gitignore
# API Keys and Secrets - NEVER COMMIT THESE
.aipmos/environment
.mcp.json
*.key
```

**Verify this file exists** after installation:
```bash
cat ~/PM-Workspace/.gitignore
```

### Pre-commit Hook (Recommended)

Add a pre-commit hook to catch accidental secret commits:

```bash
# Create the hook
cat > ~/PM-Workspace/.git/hooks/pre-commit << 'EOF'
#!/bin/bash

# Check for potential secrets
if git diff --cached --name-only | xargs grep -l "ntn_\|sk-\|api_key.*=.*[a-zA-Z0-9]\{20,\}" 2>/dev/null; then
    echo "⚠️  Potential secrets detected in staged files!"
    echo "Please review and remove any API keys before committing."
    exit 1
fi
EOF

chmod +x ~/PM-Workspace/.git/hooks/pre-commit
```

### Environment File Best Practices

The `.aipmos/environment` file uses a template pattern:
- `environment.template` - Safe to commit (contains placeholders)
- `environment` - **Never commit** (contains real keys)

This pattern allows you to:
1. Share the template structure in version control
2. Keep your actual keys local and secure

---

## What This Template Protects

The PM-OS template is designed to be **safe to share**:

✅ **Included (Safe):**
- Template files with `{{PLACEHOLDER}}` syntax
- Generic commands and skills
- Configuration structure without credentials
- Documentation

❌ **Excluded (User Data):**
- `.aipmos/environment` (secrets)
- `.mcp.json` (MCP credentials)
- `.aipmos/sessions-archive/` (personal session history)
- `.aipmos/events.db`, `.aipmos/patterns.db` (user data)
- `.aipmos/session-intent.json` (session state)
- `.aipmos/patterns/learned-patterns.md` (personal patterns)

---

## Verification Checklist

After setup, verify your security:

- [ ] `.aipmos/environment` has placeholder values, not real keys
- [ ] `.mcp.json` has placeholder values, not real keys
- [ ] `.gitignore` includes `.aipmos/environment` and `.mcp.json`
- [ ] Pre-commit hook is installed (optional but recommended)
- [ ] All previously exposed keys have been rotated

---

## Questions?

If you find security issues with this template, please report them responsibly.
