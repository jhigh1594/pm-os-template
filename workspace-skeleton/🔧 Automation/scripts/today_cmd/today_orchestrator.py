"""TodayOrchestrator runs the /today command workflow."""

import logging
import os
import re
import sys
from datetime import datetime, date, timedelta
from pathlib import Path
from typing import Dict, Any, Optional, List

# Add parent directory to path for imports when running as module
sys.path.insert(0, str(Path(__file__).parent.parent))

from shared.base_orchestrator import BaseOrchestrator
from shared.aipmos_config import AIPMOSConfig

from today_cmd.collectors.agileplace_collector import AgilePlaceCollector
from today_cmd.collectors.granola_collector import GranolaCollector
from today_cmd.storage.task_writer import TaskWriter

logger = logging.getLogger(__name__)


class TodayOrchestrator(BaseOrchestrator):
    """
    Orchestrates the /today command workflow.

    Workflow:
    1. Collect: Gather data from AgilePlace and Granola
    2. Categorize: Sort tasks into due today, overdue, and upcoming
    3. Analyze: Extract action items and insights from meetings
    4. Write: Generate today.md, this-week.md, next-week.md for Claude analysis
    """

    def __init__(self, config_path: str = None):
        """
        Initialize TodayOrchestrator.

        Args:
            config_path: Path to config.yaml (default: today_cmd/config.yaml)
        """
        if config_path is None:
            # Default to today_cmd/config.yaml
            config_path = str(Path(__file__).parent / "config.yaml")

        super().__init__(config_path)

        # Initialize components
        self._init_collectors()
        self._init_storage()

    def _init_collectors(self):
        """Initialize data collectors based on config."""
        config = self.config

        # AgilePlace collector (REST API)
        agile_config = config.get("agileplace", {})
        self.agileplace_collector = AgilePlaceCollector(
            domain=agile_config.get("domain") or os.getenv("AGILEPLACE_DOMAIN"),
            api_token=agile_config.get("api_token") or os.getenv("AGILEPLACE_API_TOKEN")
        )

        # Granola collector (meeting notes)
        granola_config = config.get("granola", {})
        granola_enabled = granola_config.get("enabled", True)

        if granola_enabled:
            self.granola_collector = GranolaCollector(
                granola_path=granola_config.get("storage_path"),
                auto_fetch=granola_config.get("auto_fetch", True),
                days_back=granola_config.get("days_back", 1)
            )
            logger.info("GranolaCollector initialized")
        else:
            self.granola_collector = None
            logger.info("GranolaCollector disabled")

    def _init_storage(self):
        """Initialize TaskWriter for /tasks/ directory."""
        config = self.config
        storage_config = config.get("storage", {})

        # Use AIPMOSConfig to resolve tasks path
        aipmos_config = AIPMOSConfig()
        default_path = str(aipmos_config.paths["tasks_output"])
        tasks_path = storage_config.get("tasks_path", default_path)

        self.task_writer = TaskWriter(tasks_path=tasks_path)
        logger.info(f"TaskWriter initialized for {tasks_path}")

    async def _collect_data(self) -> Dict[str, Any]:
        """
        Collect data from all sources in parallel.

        Returns:
            CollectedData dict with agileplace and granola
        """
        logger.info("Collecting data from all sources")

        # Run collectors in parallel
        import asyncio

        collectors = [self.agileplace_collector.collect()]
        if self.granola_collector:
            collectors.append(self.granola_collector.collect())

        results = await asyncio.gather(*collectors, return_exceptions=True)

        # Unpack results
        agileplace_data = results[0]
        granola_data = results[1] if len(results) > 1 and self.granola_collector else {"meetings": [], "errors": []}

        # Handle exceptions
        if isinstance(agileplace_data, Exception):
            logger.error(f"AgilePlace collector failed: {agileplace_data}")
            agileplace_data = {"tasks": [], "cards": [], "dependencies": {}, "errors": [str(agileplace_data)]}

        if isinstance(granola_data, Exception):
            logger.error(f"Granola collector failed: {granola_data}")
            granola_data = {"meetings": [], "errors": [str(granola_data)]}

        # Combine into CollectedData structure
        collected = {
            "timestamp": datetime.now().isoformat(),
            "date": datetime.now().strftime("%Y-%m-%d"),
            "agileplace": agileplace_data,
            "granola": granola_data
        }
        self._last_collected = collected

        # Log summary
        logger.info(
            f"Collected: {len(agileplace_data.get('tasks', []))} tasks, "
            f"{len(agileplace_data.get('cards', []))} cards, "
            f"{len(granola_data.get('meetings', []))} meetings"
        )

        # Collect all errors
        all_errors = []
        for source, data in [
            ("agileplace", agileplace_data),
            ("granola", granola_data),
        ]:
            all_errors.extend([f"{source}: {e}" for e in data.get("errors", [])])

        if all_errors:
            logger.warning(f"Collection errors: {all_errors}")

        return collected

    async def _analyze_data(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Categorize collected data into due today, overdue, and upcoming.

        Args:
            data: CollectedData from _collect_data()

        Returns:
            CategorizedData with tasks_due_today, overdue_tasks, all_tasks, all_cards,
            and granola_action_items, granola_insights
        """
        logger.info("Categorizing tasks by due date")

        today = date.today()
        tasks_due_today = []
        overdue_tasks = []

        # Get all tasks and cards from AgilePlace
        agileplace = data.get("agileplace", {})
        all_tasks = agileplace.get("tasks", [])
        all_cards = agileplace.get("cards", [])

        # Categorize each item
        for item in all_tasks + all_cards:
            due_date_str = item.get("due_date")
            if not due_date_str:
                continue

            try:
                # Parse due date
                due_date = datetime.fromisoformat(due_date_str.replace('Z', '+00:00')).date()

                if due_date < today:
                    # Overdue
                    overdue_tasks.append(item)
                elif due_date == today:
                    # Due today
                    tasks_due_today.append(item)

            except (ValueError, AttributeError):
                continue

        logger.info(f"Categorized: {len(tasks_due_today)} due today, {len(overdue_tasks)} overdue")

        # Analyze granola meetings
        granola_analysis = self._analyze_granola_meetings(data)

        return {
            "tasks_due_today": tasks_due_today,
            "overdue_tasks": overdue_tasks,
            "all_tasks": all_tasks,
            "all_cards": all_cards,
            "granola_action_items": granola_analysis.get("action_items", []),
            "meetings_for_ai": granola_analysis.get("meetings_for_ai", []),
            "collected_data": data
        }

    def _analyze_granola_meetings(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Analyze granola meeting notes to extract action items and meeting context.

        Uses structured parsing for action items (Next Steps section).
        Passes meeting context to today.md for AI analysis by /today skill.

        Args:
            data: CollectedData with granola meetings

        Returns:
            Dict with action_items and meetings_for_ai (context for embedded AI)
        """
        granola_data = data.get("granola", {})
        meetings = granola_data.get("meetings", [])

        action_items = []

        # Extract action items from each meeting
        for meeting in meetings:
            title = meeting.get("title", "Untitled")
            summary = meeting.get("summary", "") or meeting.get("notes", "")

            # Extract action items from Next Steps section
            items = self._parse_next_steps_from_summary(summary, title)
            action_items.extend(items)

        logger.info(f"Granola analysis: {len(action_items)} action items")

        return {
            "action_items": action_items,
            "meetings_for_ai": meetings  # Pass meeting context for embedded AI
        }

    def _parse_next_steps_from_summary(self, summary_text: str, meeting_title: str) -> List[str]:
        """
        Extract action items from ## Next Steps section.

        Uses config settings for quality filters (min_item_length, max_items_per_meeting).

        Args:
            summary_text: Meeting summary markdown text
            meeting_title: Title of the meeting for context tagging

        Returns:
            List of formatted action strings: "Action description (granola - Meeting Title)"
        """
        action_items = []

        # Get extraction config
        granola_config = self.config.get("granola", {})
        extraction_config = granola_config.get("extraction", {})
        min_item_length = extraction_config.get("min_item_length", 10)
        max_items = extraction_config.get("max_items_per_meeting", 10)

        # Find Next Steps or Action Items section (case-insensitive)
        # Try multiple heading patterns
        # Use ###?[^#] to properly match heading levels (### without matching ####)
        section_patterns = [
            r'###?\s*Next Steps\s*\n+(.*?)(?=\n##?[^#]|\n---|\Z)',
            r'###?\s*Action Items?\s*\n+(.*?)(?=\n##?[^#]|\n---|\Z)',
            r'###?\s*Actions?\s*\n+(.*?)(?=\n##?[^#]|\n---|\Z)',
        ]

        content = None
        for pattern in section_patterns:
            match = re.search(pattern, summary_text, re.DOTALL | re.IGNORECASE)
            if match:
                content = match.group(1)
                break

        if not content:
            return []

        # Parse lines: "- Name: action" or "- action"
        lines = content.strip().split('\n')

        for line in lines:
            # Check max items limit
            if len(action_items) >= max_items:
                break

            line = line.strip()

            # Skip empty lines and non-bullet points
            if not line or not line.startswith('-'):
                continue

            # Remove bullet and whitespace
            item_content = line[1:].strip()

            # Quality filter: minimum length (from config)
            if len(item_content) < min_item_length:
                continue

            # Skip meta-text
            if any(skip in item_content.lower() for skip in ['tbd', 'n/a', 'none', 'pending']):
                continue

            # Format with meeting context
            formatted = f"{item_content} (granola - {meeting_title})"
            action_items.append(formatted)

        return action_items

    async def _synthesize_output(self, categorized: Dict[str, Any]) -> Dict[str, Any]:
        """
        Write task files using TaskWriter.

        Args:
            categorized: CategorizedData from _analyze_data()

        Returns:
            Result dict with file paths and counts
        """
        logger.info("Writing task files")

        # Check if task_writer is available (might be None with --skip-storage)
        if not self.task_writer:
            logger.warning("TaskWriter disabled (--skip-storage), skipping file writes")
            return {
                "tasks_due_today_count": len(categorized["tasks_due_today"]),
                "overdue_count": len(categorized["overdue_tasks"]),
                "data_sources_used": ["agileplace"],
                "confidence_score": 1.0
            }

        try:
            # Write today.md with granola data
            today_path = await self.task_writer.write_today(
                collected_data=categorized["collected_data"],
                tasks_due_today=categorized["tasks_due_today"],
                overdue_tasks=categorized["overdue_tasks"],
                granola_action_items=categorized.get("granola_action_items", []),
                meetings_for_ai=categorized.get("meetings_for_ai", [])
            )

            # Write weekly views
            weekly_paths = await self.task_writer.write_weekly_views(
                all_tasks=categorized["all_tasks"],
                all_cards=categorized["all_cards"]
            )

            # Determine which sources were used
            data_sources = ["agileplace"]
            if categorized.get("granola_action_items") or categorized.get("meetings_for_ai"):
                data_sources.append("granola")

            result = {
                "today_path": today_path,
                "this_week_path": weekly_paths.get("this_week"),
                "next_week_path": weekly_paths.get("next_week"),
                "tasks_due_today_count": len(categorized["tasks_due_today"]),
                "overdue_count": len(categorized["overdue_tasks"]),
                "data_sources_used": data_sources,
                "confidence_score": 1.0  # Always confident since we're just formatting
            }

            logger.info(f"Task files written: today.md, this-week.md, next-week.md")

            return result

        except Exception as e:
            logger.error(f"Failed to write task files: {e}")
            return {
                "error": str(e),
                "confidence_score": 0.0
            }

    async def _store_output(self, output: Dict[str, Any]) -> bool:
        """
        Storage is now handled by TaskWriter - this is a no-op.

        Args:
            output: Result dict from _synthesize_output()

        Returns:
            True (storage handled in _synthesize_output)
        """
        # Storage is now handled in _synthesize_output via TaskWriter
        return True
