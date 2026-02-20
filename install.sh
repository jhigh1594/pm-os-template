#!/bin/bash
# PM Operating System Template Installer
# Creates a new PM workspace with all AI assistant configurations

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Default target directory
TARGET_DIR="${1:-$HOME/PM-Workspace}"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

echo -e "${BLUE}╔════════════════════════════════════════════════════════════╗${NC}"
echo -e "${BLUE}║     PM Operating System (PM-OS) Template Installer        ║${NC}"
echo -e "${BLUE}╚════════════════════════════════════════════════════════════╝${NC}"
echo ""

# Check if target directory exists
if [ -d "$TARGET_DIR" ]; then
    echo -e "${YELLOW}⚠️  Directory $TARGET_DIR already exists.${NC}"
    echo -e "${YELLOW}   Please remove it or specify a different location:${NC}"
    echo -e "${YELLOW}   ./install.sh /path/to/new/workspace${NC}"
    exit 1
fi

echo -e "${GREEN}📦 Installing PM-OS to: $TARGET_DIR${NC}"
echo ""

# Step 1: Create workspace skeleton
echo -e "${BLUE}[1/6] Creating workspace directory structure...${NC}"
mkdir -p "$TARGET_DIR"
cp -r "$SCRIPT_DIR/workspace-skeleton/"* "$TARGET_DIR/"
mkdir -p "$TARGET_DIR/.aipmos/memory-bank"
mkdir -p "$TARGET_DIR/.claude"
echo -e "   ${GREEN}✓${NC} Directory structure created"

# Collect product names first (needed for directory renaming)
echo -e "${YELLOW}Please provide the following information:${NC}"
echo ""
read -p "Primary product (e.g., ProductA): " PRODUCT_1
read -p "Second product (or press Enter to skip): " PRODUCT_2
read -p "Third product (or press Enter to skip): " PRODUCT_3
PRODUCT_2="${PRODUCT_2:-Other}"
PRODUCT_3="${PRODUCT_3:-Future}"

# Rename product placeholder directories
if [ -d "$TARGET_DIR/📦 Products/{{PRODUCT_1}}" ]; then
    mv "$TARGET_DIR/📦 Products/{{PRODUCT_1}}" "$TARGET_DIR/📦 Products/$PRODUCT_1"
fi
if [ -d "$TARGET_DIR/📦 Products/{{PRODUCT_2}}" ]; then
    mv "$TARGET_DIR/📦 Products/{{PRODUCT_2}}" "$TARGET_DIR/📦 Products/$PRODUCT_2"
fi
if [ -d "$TARGET_DIR/📦 Products/{{PRODUCT_3}}" ]; then
    mv "$TARGET_DIR/📦 Products/{{PRODUCT_3}}" "$TARGET_DIR/📦 Products/$PRODUCT_3"
fi
echo -e "   ${GREEN}✓${NC} Product directories created: $PRODUCT_1, $PRODUCT_2, $PRODUCT_3"

# Step 2: Copy .claude configuration
echo -e "${BLUE}[2/6] Copying Claude Code configuration...${NC}"
cp -r "$SCRIPT_DIR/template/.claude/"* "$TARGET_DIR/.claude/"
echo -e "   ${GREEN}✓${NC} Commands, skills, and rules copied"

# Step 3: Copy AIPMOS files
echo -e "${BLUE}[3/6] Copying AIPMOS configuration...${NC}"
cp "$SCRIPT_DIR/template/.aipmos/MEMORY.md" "$TARGET_DIR/.aipmos/"
cp "$SCRIPT_DIR/template/.aipmos/version.json" "$TARGET_DIR/.aipmos/"
cp "$SCRIPT_DIR/template/.aipmos/memory-bank/README.md" "$TARGET_DIR/.aipmos/memory-bank/" 2>/dev/null || true
cp "$SCRIPT_DIR/template/.aipmos/.gitignore" "$TARGET_DIR/.aipmos/" 2>/dev/null || true
echo -e "   ${GREEN}✓${NC} AIPMOS core files copied"

# Step 4: Process templates
echo -e "${BLUE}[4/6] Processing templates with your information...${NC}"
echo ""

# Collect remaining user information
read -p "Your name (e.g., Jane Smith): " USER_NAME
read -p "Your role (e.g., Senior Product Manager): " USER_ROLE
read -p "Your company (e.g., Acme Corp): " USER_COMPANY

# Get current date
CURRENT_DATE=$(date +"%B %Y")

# Process GOALS.md.template
echo ""
echo -e "${BLUE}   Processing GOALS.md...${NC}"
sed -e "s|{{YOUR_NAME}}|$USER_NAME|g" \
    -e "s|{{YOUR_ROLE}}|$USER_ROLE|g" \
    -e "s|{{YOUR_COMPANY}}|$USER_COMPANY|g" \
    -e "s|{{PRODUCT_1}}|$PRODUCT_1|g" \
    -e "s|{{PRODUCT_2}}|$PRODUCT_2|g" \
    -e "s|{{PRODUCT_3}}|$PRODUCT_3|g" \
    "$SCRIPT_DIR/template/GOALS.md.template" > "$TARGET_DIR/GOALS.md"
echo -e "   ${GREEN}✓${NC} GOALS.md created"

# Process CLAUDE.md.template
echo -e "${BLUE}   Processing CLAUDE.md...${NC}"
sed -e "s|{{YOUR_NAME}}|$USER_NAME|g" \
    -e "s|{{YOUR_ROLE}}|$USER_ROLE|g" \
    -e "s|{{YOUR_COMPANY}}|$USER_COMPANY|g" \
    -e "s|{{WORKSPACE_PATH}}|$TARGET_DIR|g" \
    -e "s|{{PRODUCT_1}}|$PRODUCT_1|g" \
    -e "s|{{PRODUCT_2}}|$PRODUCT_2|g" \
    -e "s|{{PRODUCT_3}}|$PRODUCT_3|g" \
    "$SCRIPT_DIR/template/CLAUDE.md.template" > "$TARGET_DIR/CLAUDE.md"
echo -e "   ${GREEN}✓${NC} CLAUDE.md created"

# Process aipmos.yaml.template
echo -e "${BLUE}   Processing aipmos.yaml...${NC}"
sed -e "s|{{YOUR_NAME}}|$USER_NAME|g" \
    -e "s|{{YOUR_COMPANY}}|$USER_COMPANY|g" \
    -e "s|{{PRODUCT_1}}|$PRODUCT_1|g" \
    -e "s|{{PRODUCT_2}}|$PRODUCT_2|g" \
    -e "s|{{PRODUCT_3}}|$PRODUCT_3|g" \
    "$SCRIPT_DIR/template/.aipmos/aipmos.yaml.template" > "$TARGET_DIR/.aipmos/aipmos.yaml"
echo -e "   ${GREEN}✓${NC} aipmos.yaml created"

# Process environment.template
echo -e "${BLUE}   Processing environment file...${NC}"
cp "$SCRIPT_DIR/template/.aipmos/environment.template" "$TARGET_DIR/.aipmos/environment"
echo -e "   ${GREEN}✓${NC} environment created (needs API keys)"

# Process memory.md.template
echo -e "${BLUE}   Processing memory.md...${NC}"
sed -e "s|{{YOUR_NAME}}|$USER_NAME|g" \
    -e "s|{{YOUR_ROLE}}|$USER_ROLE|g" \
    -e "s|{{YOUR_COMPANY}}|$USER_COMPANY|g" \
    -e "s|{{WORKSPACE_PATH}}|$TARGET_DIR|g" \
    -e "s|{{DATE}}|$CURRENT_DATE|g" \
    -e "s|{{PRODUCT_1}}|$PRODUCT_1|g" \
    -e "s|{{PRODUCT_2}}|$PRODUCT_2|g" \
    -e "s|{{PRODUCT_3}}|$PRODUCT_3|g" \
    "$SCRIPT_DIR/template/.aipmos/memory-bank/memory.md.template" > "$TARGET_DIR/.aipmos/memory-bank/memory.md"
echo -e "   ${GREEN}✓${NC} memory.md created"

# Process .mcp.json.template
echo -e "${BLUE}   Processing .mcp.json...${NC}"
cp "$SCRIPT_DIR/template/.mcp.json.template" "$TARGET_DIR/.mcp.json"
echo -e "   ${GREEN}✓${NC} .mcp.json created (needs API keys)"

# Step 5: Initialize git repo
echo ""
echo -e "${BLUE}[5/6] Initializing git repository...${NC}"
cd "$TARGET_DIR"
git init
cat > .gitignore << 'GITIGNORE'
# API Keys and Secrets - NEVER COMMIT THESE
.aipmos/environment
.mcp.json
*.key

# OS files
.DS_Store
Thumbs.db

# IDE
.idea/
.vscode/
*.swp

# Session data (personal)
.aipmos/sessions-archive/
.aipmos/events.db
.aipmos/patterns.db
.aipmos/session-intent.json
GITIGNORE
git add .
git commit -m "Initial commit: PM-OS workspace setup"
echo -e "   ${GREEN}✓${NC} Git repository initialized"

# Step 6: Create initial today.md
echo -e "${BLUE}[6/6] Creating initial task files...${NC}"
mkdir -p "$TARGET_DIR/📋 Tasks"
cat > "$TARGET_DIR/📋 Tasks/today.md" << TODAYMD
# Daily Plan - $(date +"%Y-%m-%d")

## Focus
[What's your main focus today?]

## Priorities
1. [Priority 1]
2. [Priority 2]
3. [Priority 3]

## Notes
- [Any notes or context]
TODAYMD
echo -e "   ${GREEN}✓${NC} Initial task files created"

# Final summary
echo ""
echo -e "${GREEN}╔════════════════════════════════════════════════════════════╗${NC}"
echo -e "${GREEN}║              ✅ Installation Complete!                     ║${NC}"
echo -e "${GREEN}╚════════════════════════════════════════════════════════════╝${NC}"
echo ""
echo -e "${BLUE}Your PM-OS workspace is ready at:${NC}"
echo -e "   $TARGET_DIR"
echo ""
echo -e "${YELLOW}⚠️  REQUIRED: Complete these steps before using:${NC}"
echo ""
echo -e "1. ${YELLOW}Add your API keys${NC} (these were NOT included for security):"
echo -e "   Edit: $TARGET_DIR/.aipmos/environment"
echo -e "   Edit: $TARGET_DIR/.mcp.json"
echo ""
echo -e "2. ${YELLOW}Customize your workspace${NC}:"
echo -e "   - Review and update: $TARGET_DIR/GOALS.md"
echo -e "   - Add your products to: $TARGET_DIR/📦 Products/"
echo -e "   - Add company context to: $TARGET_DIR/🏢 Company/"
echo ""
echo -e "3. ${YELLOW}Open in Claude Code${NC}:"
echo -e "   cd $TARGET_DIR && claude"
echo ""
echo -e "${BLUE}📚 Documentation:${NC}"
echo -e "   - README: $SCRIPT_DIR/README.md"
echo -e "   - Security: $SCRIPT_DIR/docs/SECURITY-REMEDIATION.md"
echo -e "   - Customization: $SCRIPT_DIR/docs/CUSTOMIZATION-GUIDE.md"
echo ""
