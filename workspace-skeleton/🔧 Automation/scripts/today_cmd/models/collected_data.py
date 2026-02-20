"""Data models for Phase 1: Collected raw data."""

from typing import TypedDict, List, Optional, Dict, Any


class AgilePlaceTask(TypedDict):
    """Single task from AgilePlace."""
    id: str
    title: str
    description: str
    size: int
    priority: str
    type_id: str
    type_title: str
    board_id: str
    board_name: str
    lane_id: str
    lane_name: str
    created_on: Optional[str]
    started_on: Optional[str]
    finished_on: Optional[str]
    due_date: Optional[str]
    is_blocked: bool
    tags: List[str]
    card_status: str
    containing_card_id: Optional[str]


class AgilePlaceDependency(TypedDict):
    """Dependency information for a task/card."""
    id: str
    type: str  # "Blocks" | "Blocked By"
    connected_card_id: str
    connected_card_title: str
    connected_board_name: str


class CollectedData(TypedDict):
    """Aggregate of all collected data from Phase 1."""
    timestamp: str  # ISO 8601 of collection time
    date: str       # YYYY-MM-DD for the plan
    agileplace: Dict[str, Any]
