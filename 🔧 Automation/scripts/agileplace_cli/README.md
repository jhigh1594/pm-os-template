# AgilePlace CLI

A command-line tool for interacting with the AgilePlace API. Used by AI coding agents to create, update, and fetch AgilePlace cards.

## Installation

```bash
cd "{{WORKSPACE_PATH}}/🔧 Automation/scripts"
python -m venv .venv
source .venv/bin/activate
pip install httpx typer python-dotenv markdown
```

## Configuration

Create a `.env` file in `Automation/scripts/` with:

```env
AGILEPLACE_DOMAIN=https://planview.leankit.com
AGILEPLACE_API_TOKEN=your_api_token_here
```

To get an API token:
1. Log into AgilePlace
2. Go to User Settings → API Tokens
3. Generate a new token with appropriate scopes

## Usage

```bash
# From the workspace root
python 🔧/Automation/scripts/agileplace_cli/cli.py <command>

# Or with full path
python "{{WORKSPACE_PATH}}/🔧 Automation/scripts/agileplace_cli/cli.py" <command>
```

## Commands

### Authentication

#### `auth whoami`
Check current authenticated user and verify credentials.

```bash
agileplace auth whoami
agileplace auth whoami --format table
```

### Boards

#### `boards list`
List all boards you have access to.

```bash
agileplace boards list
agileplace boards list --search "roadmap"
agileplace boards list --format table --limit 50
```

Options:
- `--search`: Filter boards by title (partial match)
- `--limit`: Number of boards to return (default: 200)
- `--offset`: Offset for pagination (default: 0)
- `--format`: Output format: `json` or `table` (default: json)

#### `boards get`
Get detailed information about a specific board.

```bash
agileplace boards get <board_id>
agileplace boards get <board_id> --format summary
```

Arguments:
- `board_id`: The board ID (required)

Options:
- `--format`: Output format: `json` (full API response) or `summary` (human-readable)

#### `boards cards`
List all cards on a specific board.

```bash
agileplace boards cards <board_id>
agileplace boards cards <board_id> --lanes "Ready,In Progress"
agileplace boards cards <board_id> --include-archived --format table
```

Arguments:
- `board_id`: The board ID (required)

Options:
- `--lanes`: Filter by lane names (comma-separated)
- `--include-archived`: Include archived cards
- `--limit`: Number of cards to return (default: 1000)
- `--offset`: Offset for pagination (default: 0)
- `--format`: Output format: `json` or `table` (default: json)

### Cards

#### `cards mine`
List cards assigned to the current user.

```bash
agileplace cards mine
agileplace cards mine --limit 50
agileplace cards mine --format table
agileplace cards mine --card-status started
agileplace cards mine --show-blocked-first
agileplace cards mine --out cards.json
```

Options:
- `--limit`: Number of cards to return (default: 200)
- `--offset`: Offset for pagination (default: 0)
- `--format`: Output format: `json` or `table` (default: json)
- `--include-archived`: Include archived cards
- `--card-status`: Filter by status: `started`, `notStarted`, `finished` (csv allowed)
- `--show-blocked-first`: Sort blocked cards first
- `--out`: Write JSON output to a file

#### `cards get`
Get detailed information about a specific card.

```bash
agileplace cards get <card_id>
agileplace cards get <card_id> --format summary
```

Arguments:
- `card_id`: The card ID (required)

Options:
- `--format`: Output format: `json` (full API response) or `summary` (human-readable)

#### `cards search`
Advanced card search with powerful filtering capabilities.

```bash
# Full text search
agileplace cards search --search "dependency"

# Filter by board
agileplace cards search --board 123456789

# Filter by assigned users
agileplace cards search --users "userId1,userId2"

# Filter by lane class (backlog, active, archive)
agileplace cards search --lane-class "active,backlog"

# Include custom fields and parent cards
agileplace cards search --board 123456789 --include "customFields,parentCards"

# Cards updated since a date
agileplace cards search --since "2024-01-01T00:00:00Z" --sort title

# Fetch specific cards by ID
agileplace cards search --cards "123,456,789"
```

Options:
- `--search, -s`: Full text search on card title and external card id
- `--board, -b`: Filter to specified board ID
- `--lanes, -l`: Comma-delimited list of lane IDs
- `--cards, -c`: Comma-delimited list of card IDs to fetch
- `--users, -u`: Comma-delimited list of assigned user IDs
- `--types`: Comma-delimited list of card type IDs
- `--lane-class`: Filter by lane class: `backlog`, `active`, `archive` (comma-delimited)
- `--select`: Return: `cards`, `taskCards`, or `both` (default: cards)
- `--include`: Include additional data: `customFields`, `parentCards`, `connectedCardStats`, `externalAssociations`, `dependencies`
- `--since`: Only return cards updated after this ISO8601 date
- `--sort`: Sort by: `activity`, `rank`, `title` (default: activity)
- `--limit`: Number of cards to return (default: 200)
- `--offset`: Offset for pagination
- `--format`: Output format: `json` or `table` (default: table)
- `--out`: Write JSON output to a file

#### `cards create`
Create a new card on a board.

```bash
agileplace cards create <board_id> --title "Card Title"
agileplace cards create <board_id> -t "Card Title" -d "Card description with **markdown** support"
```

Arguments:
- `board_id`: The board ID (required) - found in board URL

Options:
- `--title, -t`: Card title (required)
- `--description, -d`: Card description (supports markdown)

#### `cards update`
Update an existing card.

```bash
agileplace cards update <card_id> --title "New Title"
agileplace cards update <card_id> --description "Updated description"
agileplace cards update <card_id> -t "Title" -d "Description"
```

Arguments:
- `card_id`: The card ID to update (required)

Options:
- `--title, -t`: New card title
- `--description, -d`: New card description (supports markdown)

Note: At least one of `--title` or `--description` is required.

#### `cards tasks`
List tasks for a card.

```bash
agileplace cards tasks <card_id>
agileplace cards tasks <card_id> --format table --limit 50
```

Arguments:
- `card_id`: The card ID (required)

Options:
- `--limit`: Number of tasks to return (default: 20)
- `--offset`: Offset for pagination (default: 0)
- `--format`: Output format: `json` or `table` (default: json)

## Examples

### Creating a PRD Card

```bash
python cli.py cards create 1234567890 \
  --title "Feature: Global Attributes for Planview Products" \
  --description "
## Problem Statement
Enterprise customers need consistent custom fields across products.

## Proposed Solution
Implement global attributes that sync across AgilePlace, OKRs, and Roadmaps.

## Success Criteria
- [ ] Attributes defined once appear in all products
- [ ] Values sync bi-directionally
- [ ] Admin governance controls available
"
```

### Updating Card Status

```bash
python cli.py cards update 9876543210 \
  --description "
## Status: In Progress

### Completed
- [x] Design spec approved
- [x] API contract defined

### In Progress
- [ ] Frontend implementation

### Blocked
- Waiting on design review
"
```

## Output Formats

### JSON (default)
Full API response with all fields. Best for programmatic processing.

### Table
Human-readable summary with key fields. Best for quick reviews.

## Error Handling

The CLI will exit with an error message if:
- Authentication fails (check your API token)
- Board/card ID is invalid
- Required parameters are missing
- API returns an error

## For AI Agents

When AI coding agents need to interact with AgilePlace:

1. **Always use this CLI** - never make direct API calls
2. **Check auth first** - run `auth whoami` to verify credentials
3. **Use table format** - for human-readable output
4. **Use json format** - for programmatic parsing
5. **Card URLs** - follow pattern `https://planview.leankit.com/card/<id>`

See `.claude/rules/agileplace-cli.mdc` for agent-specific instructions.
