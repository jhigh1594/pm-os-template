"""Data models for Phase 2: Analyzed data."""

from typing import TypedDict, List, Dict


class PriorityItem(TypedDict):
    """Single prioritized item."""
    title: str
    category: str  # STRATEGIC, REACTIVE, BLOCKED, PREP_NEEDED
    source: str    # "agileplace"
    urgency_score: float  # 0.0-1.0
    strategic_alignment: float  # 0.0-1.0 (aligned to OKRs)
    time_estimate: str | None  # "30m", "1h", "2h"
    dependencies: List[str]  # Titles of blocking items
    prep_needed: str | None  # Description if PREP_NEEDED


class AnalyzedData(TypedDict):
    """Output of Phase 2 analysis."""
    date: str
    priorities: List[PriorityItem]
    blocked_items: List[PriorityItem]
    prep_gaps: List[PriorityItem]
    strategic_alignment: Dict[str, float]  # OKR ID -> alignment score
    time_distribution: Dict[str, float]  # category -> total hours
    warnings: List[str]  # Insight warnings (context switching, etc.)
