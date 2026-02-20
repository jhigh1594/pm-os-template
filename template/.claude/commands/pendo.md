---
description: Query Pendo data and segments
---

# Pendo Query

Quick access to Pendo analytics and segmentation data via the Pendo CLI.

## Prerequisites

The Pendo CLI must be installed before using this command.

### Installation

```bash
# Clone the pendo-cli repository
cd ~/
git clone https://github.com/jhigh1594/pendo-cli.git

# Configure credentials
cd pendo-cli
cp .env.example .env
# Edit .env with your Pendo credentials

# Install dependencies (if needed)
pip install -r requirements.txt
```

### Required Credentials

Add these to `~/pendo-cli/.env`:
- `PENDO_SUBSCRIPTION_ID` - Your Pendo subscription ID
- `PENDO_APP_ID` - Your Pendo app ID

## Usage

`/pendo <action>`

## Actions

| Action | Description | Example |
|--------|-------------|---------|
| `segments` | List all segments | `/pendo segments` |
| `visitors <days>` | Query visitors from last N days | `/pendo visitors 30` |
| `accounts <days>` | Query accounts from last N days | `/pendo accounts 30` |
| `activity` | Query activity metrics | `/pendo activity` |

## Examples

```
/pendo segments
# Lists all Pendo segments with IDs and names

/pendo visitors 30
# Shows visitor data from the last 30 days

/pendo accounts 7
# Shows account data from the last week
```

## Troubleshooting

If the command fails:
1. Verify pendo-cli is installed at `~/pendo-cli/`
2. Check that `.env` exists with valid credentials
3. Ensure Python dependencies are installed
