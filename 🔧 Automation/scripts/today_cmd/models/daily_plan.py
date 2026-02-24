"""Data models for Phase 3: Synthesized daily plan."""

from typing import TypedDict, List, Optional


class TopPriority(TypedDict):
    """Single top 3 priority for today."""
    rank: int  # 1, 2, 3
    title: str
    rationale: str  # Why this is top priority (Four Risks framework)
    time_block: str  # Suggested time block
    prep_notes: Optional[str]
    card_id: Optional[str]
    card_url: Optional[str]


class RollingViewItem(TypedDict):
    """Item in 3-day rolling view."""
    date: str  # YYYY-MM-DD
    title: str
    category: str
    is_confirmed: bool  # True = today, False = future


class InsightWarning(TypedDict):
    """Insight or warning for the user."""
    type: str  # "attention_leak" | "prep_gap" | "context_switch" | "capacity_risk"
    severity: str  # "high" | "medium" | "low"
    message: str
    recommendation: Optional[str]


class DailyPlan(TypedDict):
    """Final synthesized daily plan (Phase 3 output)."""
    date: str
    generated_at: str

    # Core sections
    top_priorities: List[TopPriority]
    rolling_view: List[RollingViewItem]  # Today, tomorrow, day after

    # Insights
    insights_warnings: List[InsightWarning]
    time_blocking_recommendations: List[str]

    # Metadata
    data_sources_used: List[str]  # Which collectors succeeded
    confidence_score: float  # 0.0-1.0 based on data quality
