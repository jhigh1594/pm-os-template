from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional

import httpx
import markdown
import typer
from dotenv import load_dotenv


import re


def _description_to_html(text: str) -> str:
    """Convert markdown description to HTML for AgilePlace card body."""
    if not text or not text.strip():
        return ""

    # Preprocess: ensure blank line before lists (markdown requires this)
    # Match: non-blank line followed by list item (- or * or + or numbered)
    text = re.sub(r'([^\n])\n([ \t]*[-*+][ \t])', r'\1\n\n\2', text)
    text = re.sub(r'([^\n])\n([ \t]*\d+\.[ \t])', r'\1\n\n\2', text)

    # Use markdown library with tables and fenced code support
    md = markdown.Markdown(extensions=["tables", "fenced_code"])
    return md.convert(text)

APP = typer.Typer(add_completion=False)
AUTH_APP = typer.Typer(name="auth")
BOARDS_APP = typer.Typer(name="boards")
CARDS_APP = typer.Typer(name="cards")
APP.add_typer(AUTH_APP)
APP.add_typer(BOARDS_APP)
APP.add_typer(CARDS_APP)

def _default_env_path() -> Path:
    # Prefer Automation/scripts/.env (relative to this file: agileplace_cli/cli.py -> scripts/)
    script_dir = Path(__file__).resolve().parent.parent
    return script_dir / ".env"


def _load_env(env_path: Optional[Path]) -> None:
    if env_path and env_path.exists():
        load_dotenv(env_path, override=False)
    load_dotenv(Path.cwd() / ".env", override=False)


def _require(value: Optional[str], label: str) -> str:
    if value:
        return value
    raise typer.BadParameter(f"Missing {label}. Set it in .env or pass a flag.")


def _build_domain(domain: Optional[str], account: Optional[str]) -> str:
    if domain:
        return domain.rstrip("/")
    if account:
        return f"https://{account}.leankit.com"
    raise typer.BadParameter("Missing AgilePlace domain/account.")


class AgilePlaceClient:
    def __init__(self, base_url: str, token: Optional[str]) -> None:
        self.base_url = base_url.rstrip("/")
        self.token = token

    def _headers(self) -> Dict[str, str]:
        if not self.token:
            return {}
        return {"Authorization": f"Bearer {self.token}"}

    def get(self, path: str, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        url = f"{self.base_url}{path}"
        with httpx.Client(timeout=30.0) as client:
            response = client.get(url, headers=self._headers(), params=params)
        response.raise_for_status()
        return response.json()

    def post(self, path: str, json: Dict[str, Any]) -> Dict[str, Any]:
        url = f"{self.base_url}{path}"
        with httpx.Client(timeout=30.0) as client:
            response = client.post(url, headers=self._headers(), json=json)
        response.raise_for_status()
        return response.json()

    def patch(self, path: str, json: List[Dict[str, Any]]) -> Dict[str, Any]:
        url = f"{self.base_url}{path}"
        with httpx.Client(timeout=30.0) as client:
            response = client.patch(url, headers=self._headers(), json=json)
        response.raise_for_status()
        return response.json()

def _print_table(rows: Iterable[Dict[str, Any]], columns: List[str]) -> None:
    rows_list = list(rows)
    col_widths = {col: len(col) for col in columns}
    for row in rows_list:
        for col in columns:
            value = str(row.get(col, ""))
            col_widths[col] = max(col_widths[col], len(value))

    header = "  ".join(col.ljust(col_widths[col]) for col in columns)
    typer.echo(header)
    typer.echo("  ".join("-" * col_widths[col] for col in columns))
    for row in rows_list:
        line = "  ".join(str(row.get(col, "")).ljust(col_widths[col]) for col in columns)
        typer.echo(line)


# =============================================================================
# AUTH COMMANDS
# =============================================================================

@AUTH_APP.command("whoami")
def auth_whoami(
    env_file: Optional[Path] = typer.Option(None, help="Path to .env file (default: Automation/scripts/.env)"),
    format: str = typer.Option("json", help="Output format: json|table"),
) -> None:
    """Check current authenticated user and verify credentials."""
    _load_env(env_file or _default_env_path())
    base_url = _build_domain(os.getenv("AGILEPLACE_DOMAIN"), os.getenv("AGILEPLACE_ACCOUNT"))
    token = _require(os.getenv("AGILEPLACE_API_TOKEN"), "AGILEPLACE_API_TOKEN")
    client = AgilePlaceClient(base_url, token)
    try:
        result = client.get("/io/user/me")
    except httpx.HTTPError as exc:
        raise typer.BadParameter(f"Whoami failed: {exc}") from exc

    if format == "table":
        _print_table(
            [
                {
                    "id": result.get("id"),
                    "fullName": result.get("fullName"),
                    "emailAddress": result.get("emailAddress"),
                    "username": result.get("username"),
                }
            ],
            ["id", "fullName", "emailAddress", "username"],
        )
    else:
        typer.echo(json.dumps(result, indent=2))


# =============================================================================
# BOARDS COMMANDS
# =============================================================================

@BOARDS_APP.command("list")
def boards_list(
    search: Optional[str] = typer.Option(None, "--search", "-s", help="Filter boards by title search"),
    limit: int = typer.Option(200, help="Number of boards to return"),
    offset: int = typer.Option(0, help="Offset for pagination"),
    format: str = typer.Option("table", help="Output format: json|table"),
    env_file: Optional[Path] = typer.Option(None, help="Path to .env file"),
) -> None:
    """List all boards you have access to."""
    _load_env(env_file or _default_env_path())
    base_url = _build_domain(os.getenv("AGILEPLACE_DOMAIN"), os.getenv("AGILEPLACE_ACCOUNT"))
    token = _require(os.getenv("AGILEPLACE_API_TOKEN"), "AGILEPLACE_API_TOKEN")
    client = AgilePlaceClient(base_url, token)

    params: Dict[str, Any] = {"limit": limit, "offset": offset}
    if search:
        params["search"] = search

    try:
        result = client.get("/io/board", params=params)
    except httpx.HTTPError as exc:
        raise typer.BadParameter(f"Boards fetch failed: {exc}") from exc

    boards = result.get("boards", [])
    page_meta = result.get("pageMeta", {})

    if format == "table":
        typer.echo(f"Found {page_meta.get('totalRecords', len(boards))} boards")
        typer.echo("")
        rows = [
            {
                "id": board.get("id"),
                "title": (board.get("title") or "")[:60],
                "role": board.get("boardRole", ""),
            }
            for board in boards
        ]
        _print_table(rows, ["id", "title", "role"])
    else:
        typer.echo(json.dumps(result, indent=2))


@BOARDS_APP.command("get")
def boards_get(
    board_id: str = typer.Argument(..., help="Board ID to get details for"),
    format: str = typer.Option("json", help="Output format: json|summary"),
    env_file: Optional[Path] = typer.Option(None, help="Path to .env file"),
) -> None:
    """Get detailed information about a specific board."""
    _load_env(env_file or _default_env_path())
    base_url = _build_domain(os.getenv("AGILEPLACE_DOMAIN"), os.getenv("AGILEPLACE_ACCOUNT"))
    token = _require(os.getenv("AGILEPLACE_API_TOKEN"), "AGILEPLACE_API_TOKEN")
    client = AgilePlaceClient(base_url, token)

    try:
        result = client.get(f"/io/board/{board_id}")
    except httpx.HTTPError as exc:
        raise typer.BadParameter(f"Board fetch failed: {exc}") from exc

    if format == "summary":
        typer.echo(f"Board: {result.get('title')}")
        typer.echo(f"ID: {result.get('id')}")
        typer.echo(f"Description: {result.get('description') or '(none)'}")
        typer.echo(f"Archived: {result.get('isArchived', False)}")
        typer.echo("")

        # Lane summary
        lanes = result.get("lanes", [])
        active_lanes = [l for l in lanes if l.get("laneClassType") == "active"]
        backlog_lanes = [l for l in lanes if l.get("laneClassType") == "backlog"]
        archive_lanes = [l for l in lanes if l.get("laneClassType") == "archive"]

        typer.echo(f"Lanes: {len(active_lanes)} active, {len(backlog_lanes)} backlog, {len(archive_lanes)} archive")

        # Card types
        card_types = result.get("cardTypes", [])
        typer.echo(f"Card Types: {', '.join([ct.get('name', '') for ct in card_types if ct.get('isCardType')])}")

        # Users
        users = result.get("users", [])
        typer.echo(f"Users with access: {len(users)}")

        # Custom fields
        custom_fields = result.get("customFields", [])
        if custom_fields:
            typer.echo(f"Custom Fields: {', '.join([cf.get('label', '') for cf in custom_fields])}")
    else:
        typer.echo(json.dumps(result, indent=2))


@BOARDS_APP.command("cards")
def boards_cards(
    board_id: str = typer.Argument(..., help="Board ID to list cards from"),
    lanes: Optional[str] = typer.Option(None, "--lanes", "-l", help="Comma-delimited list of lane IDs to filter"),
    limit: int = typer.Option(200, help="Number of cards to return"),
    offset: int = typer.Option(0, help="Offset for pagination"),
    format: str = typer.Option("table", help="Output format: json|table"),
    include_archived: bool = typer.Option(False, "--include-archived", help="Include archived cards"),
    out: Optional[Path] = typer.Option(None, help="Write JSON output to a file"),
    env_file: Optional[Path] = typer.Option(None, help="Path to .env file"),
) -> None:
    """List cards on a specific board."""
    _load_env(env_file or _default_env_path())
    base_url = _build_domain(os.getenv("AGILEPLACE_DOMAIN"), os.getenv("AGILEPLACE_ACCOUNT"))
    token = _require(os.getenv("AGILEPLACE_API_TOKEN"), "AGILEPLACE_API_TOKEN")
    client = AgilePlaceClient(base_url, token)

    params: Dict[str, Any] = {"limit": limit, "offset": offset}
    if lanes:
        params["lanes"] = lanes
    if include_archived:
        params["ignoreArchiveDate"] = "true"

    try:
        result = client.get(f"/io/board/{board_id}/card", params=params)
    except httpx.HTTPError as exc:
        raise typer.BadParameter(f"Cards fetch failed: {exc}") from exc

    cards = result.get("cards", [])
    page_meta = result.get("pageMeta", {})

    if out:
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(json.dumps(result, indent=2))
        typer.echo(f"Wrote {len(cards)} cards to {out}")

    if format == "table":
        typer.echo(f"Showing {len(cards)} of {page_meta.get('totalRecords', len(cards))} cards on board {board_id}")
        typer.echo("")
        rows = [
            {
                "id": card.get("id"),
                "title": (card.get("title") or "")[:50],
                "laneId": card.get("laneId"),
                "priority": card.get("priority", ""),
                "size": card.get("size", ""),
                "blocked": "BLOCKED" if card.get("blockedStatus", {}).get("isBlocked") else "",
            }
            for card in cards
        ]
        _print_table(rows, ["id", "title", "laneId", "priority", "size", "blocked"])
    else:
        typer.echo(json.dumps(result, indent=2))


# =============================================================================
# CARDS COMMANDS
# =============================================================================

@CARDS_APP.command("mine")
def cards_mine(
    limit: int = typer.Option(200, help="Number of cards to return"),
    offset: int = typer.Option(0, help="Offset for pagination"),
    format: str = typer.Option("json", help="Output format: json|table"),
    include_archived: bool = typer.Option(False, help="Include archived cards"),
    card_status: Optional[str] = typer.Option(
        None, help="Filter by status: started, notStarted, finished (csv allowed)"
    ),
    show_blocked_first: bool = typer.Option(False, help="Sort blocked cards first"),
    out: Optional[Path] = typer.Option(None, help="Write JSON output to a file"),
    env_file: Optional[Path] = typer.Option(None, help="Path to .env file"),
) -> None:
    """List all cards assigned to you."""
    _load_env(env_file or _default_env_path())
    base_url = _build_domain(os.getenv("AGILEPLACE_DOMAIN"), os.getenv("AGILEPLACE_ACCOUNT"))
    token = _require(os.getenv("AGILEPLACE_API_TOKEN"), "AGILEPLACE_API_TOKEN")
    client = AgilePlaceClient(base_url, token)

    params = {"type": "assigned", "limit": limit, "offset": offset}
    if card_status:
        params["cardStatus"] = card_status
    if show_blocked_first:
        params["showBlockedFirst"] = "true"
    try:
        result = client.get("/io/user/me/card", params=params)
    except httpx.HTTPError as exc:
        raise typer.BadParameter(f"Cards fetch failed: {exc}") from exc

    cards = result.get("cards", [])
    if not include_archived:
        cards = [card for card in cards if not card.get("archivedOn")]
    output = dict(result)
    output["cards"] = cards

    if out:
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(json.dumps(output, indent=2))
        typer.echo(f"Wrote {len(cards)} cards to {out}")
    if format == "table":
        rows = [
            {
                "id": card.get("id"),
                "title": (card.get("title") or "")[:50],
                "boardId": card.get("boardId"),
                "laneId": card.get("laneId"),
                "priority": card.get("priority"),
                "blocked": str(card.get("blockedStatus", {}).get("isBlocked", False)),
            }
            for card in cards
        ]
        _print_table(rows, ["id", "title", "boardId", "laneId", "priority", "blocked"])
    else:
        typer.echo(json.dumps(output, indent=2))


@CARDS_APP.command("get")
def cards_get(
    card_id: str = typer.Argument(..., help="Card ID to get details for"),
    format: str = typer.Option("json", help="Output format: json|summary"),
    exclude_comments: bool = typer.Option(False, help="Exclude comments from response"),
    env_file: Optional[Path] = typer.Option(None, help="Path to .env file"),
) -> None:
    """Get detailed information about a specific card."""
    _load_env(env_file or _default_env_path())
    base_url = _build_domain(os.getenv("AGILEPLACE_DOMAIN"), os.getenv("AGILEPLACE_ACCOUNT"))
    token = _require(os.getenv("AGILEPLACE_API_TOKEN"), "AGILEPLACE_API_TOKEN")
    client = AgilePlaceClient(base_url, token)

    params: Dict[str, Any] = {}
    if exclude_comments:
        params["excludeComments"] = "true"

    try:
        result = client.get(f"/io/card/{card_id}", params=params)
    except httpx.HTTPError as exc:
        raise typer.BadParameter(f"Card fetch failed: {exc}") from exc

    if format == "summary":
        typer.echo(f"Card: {result.get('title')}")
        typer.echo(f"ID: {result.get('id')}")
        typer.echo(f"Board: {result.get('board', {}).get('title', '')} ({result.get('board', {}).get('id', '')})")
        typer.echo(f"Lane: {result.get('lane', {}).get('title', '')} ({result.get('lane', {}).get('cardStatus', '')})")
        typer.echo(f"Priority: {result.get('priority')}")
        typer.echo(f"Size: {result.get('size')}")
        typer.echo(f"Type: {result.get('type', {}).get('title', '')}")
        typer.echo("")

        # Dates
        if result.get('plannedStart'):
            typer.echo(f"Planned Start: {result.get('plannedStart')}")
        if result.get('plannedFinish'):
            typer.echo(f"Planned Finish: {result.get('plannedFinish')}")
        if result.get('actualStart'):
            typer.echo(f"Actual Start: {result.get('actualStart')}")
        if result.get('actualFinish'):
            typer.echo(f"Actual Finish: {result.get('actualFinish')}")
        typer.echo("")

        # Blocked status
        blocked = result.get("blockedStatus", {})
        if blocked.get("isBlocked"):
            typer.echo(f"BLOCKED: {blocked.get('reason', 'No reason given')}")
            typer.echo("")

        # Assigned users
        assigned = result.get("assignedUsers", [])
        if assigned:
            typer.echo(f"Assigned: {', '.join([u.get('fullName', '') for u in assigned])}")

        # Tags
        tags = result.get("tags", [])
        if tags:
            typer.echo(f"Tags: {', '.join(tags)}")

        # Task board stats
        task_stats = result.get("taskBoardStats", {})
        if task_stats:
            typer.echo(f"Tasks: {task_stats.get('completedCount', 0)}/{task_stats.get('totalCount', 0)} completed")

        # Description preview
        desc = result.get("description", "")
        if desc:
            # Strip HTML for preview
            import re
            desc_clean = re.sub(r'<[^>]+>', '', desc)
            preview = desc_clean[:200] + "..." if len(desc_clean) > 200 else desc_clean
            typer.echo(f"\nDescription:\n{preview}")

        typer.echo(f"\nURL: https://planview.leankit.com/card/{card_id}")
    else:
        typer.echo(json.dumps(result, indent=2))


@CARDS_APP.command("search")
def cards_search(
    search: Optional[str] = typer.Option(None, "--search", "-s", help="Full text search on card title and external card id"),
    board: Optional[str] = typer.Option(None, "--board", "-b", help="Filter to specified board ID"),
    lanes: Optional[str] = typer.Option(None, "--lanes", "-l", help="Comma-delimited list of lane IDs to filter"),
    cards: Optional[str] = typer.Option(None, "--cards", "-c", help="Comma-delimited list of card IDs to fetch"),
    assigned_users: Optional[str] = typer.Option(None, "--users", "-u", help="Comma-delimited list of assigned user IDs"),
    card_types: Optional[str] = typer.Option(None, "--types", help="Comma-delimited list of card type IDs"),
    lane_class: Optional[str] = typer.Option(None, "--lane-class", help="Filter by lane class: backlog, active, archive (comma-delimited)"),
    select: str = typer.Option("cards", help="Return: cards, taskCards, or both"),
    include: Optional[str] = typer.Option(None, help="Include: customFields, parentCards, connectedCardStats, externalAssociations, dependencies"),
    since: Optional[str] = typer.Option(None, help="Only return cards updated after this ISO8601 date"),
    sort: str = typer.Option("activity", help="Sort by: activity, rank, title"),
    limit: int = typer.Option(200, help="Number of cards to return"),
    offset: int = typer.Option(0, help="Offset for pagination"),
    format: str = typer.Option("table", help="Output format: json|table"),
    out: Optional[Path] = typer.Option(None, help="Write JSON output to a file"),
    env_file: Optional[Path] = typer.Option(None, help="Path to .env file"),
) -> None:
    """Search cards with advanced filtering using POST /io/card/list."""
    _load_env(env_file or _default_env_path())
    base_url = _build_domain(os.getenv("AGILEPLACE_DOMAIN"), os.getenv("AGILEPLACE_ACCOUNT"))
    token = _require(os.getenv("AGILEPLACE_API_TOKEN"), "AGILEPLACE_API_TOKEN")
    client = AgilePlaceClient(base_url, token)

    # Build request body
    body: Dict[str, Any] = {"limit": limit, "offset": offset, "select": select, "sort": sort}

    if search:
        body["search"] = search
    if board:
        body["board"] = board
    if lanes:
        body["lanes"] = [l.strip() for l in lanes.split(",")]
    if cards:
        body["cards"] = [c.strip() for c in cards.split(",")]
    if assigned_users:
        body["assignedUserIds"] = [u.strip() for u in assigned_users.split(",")]
    if card_types:
        body["types"] = [t.strip() for t in card_types.split(",")]
    if lane_class:
        body["lane_class_types"] = [lc.strip() for lc in lane_class.split(",")]
    if include:
        body["include"] = [i.strip() for i in include.split(",")]
    if since:
        body["since"] = since

    try:
        result = client.post("/io/card/list", body)
    except httpx.HTTPError as exc:
        raise typer.BadParameter(f"Card search failed: {exc}") from exc

    cards_list = result.get("cards", [])
    page_meta = result.get("pageMeta", {})

    if out:
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(json.dumps(result, indent=2))
        typer.echo(f"Wrote {len(cards_list)} cards to {out}")

    if format == "table":
        typer.echo(f"Found {page_meta.get('totalRecords', len(cards_list))} cards")
        typer.echo("")
        rows = [
            {
                "id": card.get("id"),
                "title": (card.get("title") or "")[:40],
                "board": (card.get("board", {}).get("title", ""))[:25],
                "lane": (card.get("lane", {}).get("title", ""))[:20],
                "status": card.get("lane", {}).get("cardStatus", ""),
                "blocked": "BLOCKED" if card.get("blockedStatus", {}).get("isBlocked") else "",
            }
            for card in cards_list
        ]
        _print_table(rows, ["id", "title", "board", "lane", "status", "blocked"])
    else:
        typer.echo(json.dumps(result, indent=2))


@CARDS_APP.command("create")
def cards_create(
    board_id: str = typer.Argument(..., help="Board ID (e.g. from board URL)"),
    title: str = typer.Option(..., "--title", "-t", help="Card title"),
    description: Optional[str] = typer.Option(None, "--description", "-d", help="Card description (supports markdown)"),
    env_file: Optional[Path] = typer.Option(None, help="Path to .env file"),
) -> None:
    """Create a new card on a board."""
    _load_env(env_file or _default_env_path())
    base_url = _build_domain(os.getenv("AGILEPLACE_DOMAIN"), os.getenv("AGILEPLACE_ACCOUNT"))
    token = _require(os.getenv("AGILEPLACE_API_TOKEN"), "AGILEPLACE_API_TOKEN")
    client = AgilePlaceClient(base_url, token)
    body: Dict[str, Any] = {
        "destination": {"boardId": board_id},
        "title": title,
    }
    if description:
        body["description"] = _description_to_html(description)
    try:
        result = client.post("/io/card/", body)
    except httpx.HTTPError as exc:
        raise typer.BadParameter(f"Create card failed: {exc}") from exc
    card_id = result.get("id")
    typer.echo(f"Created card {card_id}: https://planview.leankit.com/card/{card_id}")


@CARDS_APP.command("update")
def cards_update(
    card_id: str = typer.Argument(..., help="Card ID to update"),
    title: Optional[str] = typer.Option(None, "--title", "-t", help="New card title"),
    description: Optional[str] = typer.Option(None, "--description", "-d", help="New card description (converted to HTML)"),
    env_file: Optional[Path] = typer.Option(None, help="Path to .env file"),
) -> None:
    """Update an existing card's title and/or description."""
    if not title and description is None:
        raise typer.BadParameter("Provide at least one of --title or --description.")
    _load_env(env_file or _default_env_path())
    base_url = _build_domain(os.getenv("AGILEPLACE_DOMAIN"), os.getenv("AGILEPLACE_ACCOUNT"))
    token = _require(os.getenv("AGILEPLACE_API_TOKEN"), "AGILEPLACE_API_TOKEN")
    client = AgilePlaceClient(base_url, token)
    patches: List[Dict[str, Any]] = []
    if title is not None:
        patches.append({"op": "replace", "path": "/title", "value": title})
    if description is not None:
        patches.append({"op": "replace", "path": "/description", "value": _description_to_html(description)})
    try:
        client.patch(f"/io/card/{card_id}", patches)
    except httpx.HTTPError as exc:
        raise typer.BadParameter(f"Update card failed: {exc}") from exc
    typer.echo(f"Updated card {card_id}: https://planview.leankit.com/card/{card_id}")


@CARDS_APP.command("tasks")
def cards_tasks(
    card_id: str = typer.Argument(..., help="Card ID"),
    limit: int = typer.Option(20, help="Number of tasks to return"),
    offset: int = typer.Option(0, help="Offset for pagination"),
    format: str = typer.Option("json", help="Output format: json|table"),
    env_file: Optional[Path] = typer.Option(None, help="Path to .env file"),
) -> None:
    """List tasks for a specific card."""
    _load_env(env_file or _default_env_path())
    base_url = _build_domain(os.getenv("AGILEPLACE_DOMAIN"), os.getenv("AGILEPLACE_ACCOUNT"))
    token = _require(os.getenv("AGILEPLACE_API_TOKEN"), "AGILEPLACE_API_TOKEN")
    client = AgilePlaceClient(base_url, token)

    params = {"limit": limit, "offset": offset}
    try:
        result = client.get(f"/io/card/{card_id}/tasks", params=params)
    except httpx.HTTPError as exc:
        raise typer.BadParameter(f"Tasks fetch failed: {exc}") from exc

    tasks = result.get("cards", [])
    if format == "table":
        rows = [
            {
                "id": task.get("id"),
                "title": (task.get("title") or "")[:50],
                "priority": task.get("priority"),
                "isDone": str(task.get("isDone", False)),
            }
            for task in tasks
        ]
        _print_table(rows, ["id", "title", "priority", "isDone"])
    else:
        typer.echo(json.dumps(result, indent=2))


def main() -> None:
    APP()


if __name__ == "__main__":
    main()
