"""Collects tasks and cards from AgilePlace via REST API."""

import logging
import os
from typing import Dict, List, Any

import aiohttp

from .base_collector import BaseCollector

logger = logging.getLogger(__name__)


class AgilePlaceCollector(BaseCollector):
    """Collects assigned tasks and cards from AgilePlace REST API."""

    def __init__(self, domain: str = None, api_token: str = None):
        """
        Initialize collector.

        Args:
            domain: AgilePlace domain URL (e.g., https://planview.leankit.com)
            api_token: AgilePlace API token for authentication
        """
        self.domain = (domain or os.getenv("AGILEPLACE_DOMAIN", "https://planview.leankit.com")).rstrip("/")
        self.api_token = api_token or os.getenv("AGILEPLACE_API_TOKEN")
        logger.info(f"AgilePlaceCollector initialized for domain: {self.domain}")

    async def collect(self) -> Dict[str, Any]:
        """
        Collect tasks, cards, and dependencies from AgilePlace REST API.

        REST API Endpoints Used:
        - /io/user/me/card: Get assigned cards/tasks for the requesting user
        - /io/reporting/export/connections: Get card dependencies/blockers (filtered to assigned cards)

        Returns:
            Dict with "tasks", "cards", "dependencies", "errors" keys
        """
        logger.info("Collecting AgilePlace data via REST API")

        result = {
            "tasks": [],
            "cards": [],
            "dependencies": {},
            "errors": []
        }

        if not self.api_token:
            result["errors"].append("AGILEPLACE_API_TOKEN not configured")
            logger.warning("AgilePlace API token not configured")
            return result

        try:
            # Create HTTP session
            async with aiohttp.ClientSession() as session:
                # Fetch tasks assigned to requesting user (non-archived, not done)
                tasks = await self._fetch_user_cards(session, filter_type="task")
                result["tasks"] = tasks

                # Fetch cards assigned to requesting user (non-archived, not done)
                cards = await self._fetch_user_cards(session, filter_type="card")
                result["cards"] = cards

                # Fetch dependencies for assigned cards
                card_ids = [card.get("id") for card in cards if card.get("id")]
                all_deps = await self._fetch_dependencies(session, card_ids)
                result["dependencies"] = all_deps

                logger.info(f"Collected {len(tasks)} tasks, {len(cards)} cards")

        except Exception as e:
            logger.error(f"AgilePlace collection failed: {e}")
            result["errors"].append(str(e))

        return result

    async def _fetch_user_cards(self, session: aiohttp.ClientSession, filter_type: str) -> List[Dict]:
        """
        Fetch assigned cards or tasks via REST API.

        Endpoint: GET /io/user/me/card
        Returns cards/tasks the requesting user is assigned to.
        """
        try:
            url = f"{self.domain}/io/user/me/card"
            headers = {"Authorization": f"Bearer {self.api_token}"}
            params = {
                "type": "assigned",
                "cardStatus": "started,notStarted",
                "filter": filter_type,
                "limit": 200,
                "offset": 0,
            }

            logger.debug(f"Fetching assigned {filter_type}s from: {url}")

            items: List[Dict] = []
            while True:
                async with session.get(url, params=params, headers=headers) as response:
                    if response.status != 200:
                        error_text = await response.text()
                        logger.error(f"AgilePlace API error {response.status}: {error_text}")
                        return []

                    payload = await response.json()
                    cards = payload.get("cards", [])
                    for item in cards:
                        if item.get("archivedOn"):
                            continue
                        if item.get("isDone"):
                            continue

                        items.append(
                            {
                                "id": str(item.get("id", "")),
                                "title": item.get("title", ""),
                                "description": "",
                                "size": item.get("size", 0),
                                "priority": item.get("priority", ""),
                                "type_id": str(item.get("cardType", {}).get("id", "")),
                                "type_title": item.get("cardType", {}).get("name", ""),
                                "board_id": str(item.get("boardId", "")),
                                "board_name": "",
                                "lane_id": str(item.get("laneId", "")),
                                "lane_name": "",
                                "created_on": item.get("createdOn"),
                                "started_on": item.get("actualStart"),
                                "finished_on": item.get("actualFinish"),
                                "due_date": item.get("plannedFinish"),
                                "is_blocked": item.get("blockedStatus", {}).get("isBlocked", False),
                                "tags": item.get("tags", []),
                                "card_status": item.get("cardStatus", ""),
                                "containing_card_id": item.get("containingCardId"),
                            }
                        )

                    page_meta = payload.get("pageMeta", {})
                    total_records = page_meta.get("totalRecords", 0)
                    offset = page_meta.get("offset", 0)
                    limit = page_meta.get("limit", params["limit"])
                    if offset + limit >= total_records:
                        break
                    params["offset"] = offset + limit

            logger.debug(f"Retrieved {len(items)} assigned {filter_type}s")
            return items

        except Exception as e:
            logger.error(f"Error fetching assigned {filter_type}s: {e}")
            return []

    async def _fetch_dependencies(
        self, session: aiohttp.ClientSession, card_ids: List[str]
    ) -> Dict[str, List[Dict]]:
        """
        Fetch card dependencies via REST API.

        Endpoint: GET /io/reporting/export/connections
        Returns card connections (dependencies/blockers).
        """
        try:
            if not card_ids:
                return {}

            url = f"{self.domain}/io/reporting/export/connections"
            params = {"format": "json"}
            headers = {"Authorization": f"Bearer {self.api_token}"}

            logger.debug(f"Fetching dependencies from: {url}")

            async with session.get(url, params=params, headers=headers) as response:
                if response.status != 200:
                    error_text = await response.text()
                    logger.error(f"AgilePlace API error {response.status}: {error_text}")
                    return {}

                data = await response.json()

                # Group dependencies by card ID
                dependencies = {}
                allowed_ids = set(card_ids)
                for item in data:
                    card_id = str(item.get("cardId", ""))
                    if card_id not in allowed_ids:
                        continue
                    if card_id not in dependencies:
                        dependencies[card_id] = []

                    dependencies[card_id].append({
                        "id": str(item.get("connectionId", "")),
                        "type": item.get("connectionType", ""),  # "Blocks" or "Blocked By"
                        "connected_card_id": str(item.get("connectedCardId", "")),
                        "connected_card_title": item.get("connectedCardTitle", ""),
                        "connected_board_name": item.get("connectedBoardTitle", "")
                    })

                logger.debug(f"Retrieved dependencies for {len(dependencies)} cards")
                return dependencies

        except Exception as e:
            logger.error(f"Error fetching dependencies: {e}")
            return {}
