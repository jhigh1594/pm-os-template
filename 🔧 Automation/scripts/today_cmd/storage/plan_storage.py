"""PlanStorage saves daily plans to memory-bank."""

import json
import logging
import re
from datetime import datetime
from pathlib import Path
from typing import Dict, Any, Optional

from ..models.daily_plan import DailyPlan

logger = logging.getLogger(__name__)


class PlanStorage:
    """
    Saves daily plans to memory-bank for tracking.

    Stores plans as Markdown files in memory-bank/daily-plans/YYYY-MM-DD-plan.md
    Each file contains the plan in human-readable format plus JSON metadata.
    """

    def __init__(self, storage_path: str):
        """
        Initialize PlanStorage.

        Args:
            storage_path: Path to memory-bank directory (e.g., "/path/to/memory-bank")
        """
        self.storage_path = Path(storage_path)
        self.plans_dir = self.storage_path / "daily-plans"
        logger.info(f"PlanStorage initialized with path {self.plans_dir}")

    async def save(self, daily_plan: DailyPlan) -> str:
        """
        Save daily plan to memory-bank.

        Args:
            daily_plan: DailyPlan from SynthesisAgent

        Returns:
            Path to saved file

        Raises:
            IOError: If file cannot be written
        """
        logger.info(f"Saving daily plan for {daily_plan['date']}")

        try:
            # Ensure directory exists
            self.plans_dir.mkdir(parents=True, exist_ok=True)

            # Build file path
            filename = f"{daily_plan['date']}-plan.md"
            file_path = self.plans_dir / filename

            # Generate markdown content
            markdown = self._format_as_markdown(daily_plan)

            # Write file
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(markdown)

            logger.info(f"Daily plan saved to {file_path}")
            return str(file_path)

        except Exception as e:
            logger.error(f"Failed to save daily plan: {e}")
            raise IOError(f"Failed to save daily plan: {e}")

    def _format_as_markdown(self, plan: DailyPlan) -> str:
        """
        Format daily plan as human-readable Markdown.

        Args:
            plan: DailyPlan to format

        Returns:
            Markdown string
        """
        lines = [
            f"# Daily Plan - {plan['date']}",
            "",
            f"**Generated:** {plan['generated_at']}",
            f"**Confidence:** {plan['confidence_score']:.0%}",
            f"**Data Sources:** {', '.join(plan['data_sources_used'])}",
            "",
            "---",
            ""
        ]

        # Top 3 Priorities
        lines.extend([
            "## 🎯 Top 3 Priorities",
            ""
        ])

        for priority in plan['top_priorities']:
            rank = priority.get('rank', '?')
            title = (priority.get('title') or '').strip() or 'Untitled'
            card_url = priority.get('card_url')
            if card_url:
                title = f"[{title}]({card_url})"
            rationale = priority.get('rationale', '')
            time_block = priority.get('time_block', 'Not scheduled')
            prep = priority.get('prep_notes')

            lines.extend([
                f"### {rank}. {title}",
                f"**Time:** {time_block}",
                ""
            ])

            if rationale:
                lines.extend([
                    f"**Why:** {rationale}",
                    ""
                ])

            if prep:
                lines.extend([
                    f"**Prep Needed:** {prep}",
                    ""
                ])

        # 3-Day Rolling View
        if plan['rolling_view']:
            lines.extend([
                "",
                "## 📆 3-Day Rolling View",
                ""
            ])

            for day_view in plan['rolling_view']:
                date = day_view.get('date', 'Unknown')
                items = day_view.get('key_items', [])
                prep_needed = day_view.get('prep_needed', [])
                opportunity = day_view.get('strategic_opportunity')

                lines.extend([
                    f"### {date}",
                    ""
                ])

                if items:
                    lines.extend([
                        "**Key Items:**",
                        ""
                    ])
                    for item in items:
                        lines.append(f"- {item}")
                    lines.append("")

                if prep_needed:
                    lines.extend([
                        "**Prep Needed:**",
                        ""
                    ])
                    for prep in prep_needed:
                        lines.append(f"- {prep}")
                    lines.append("")

                if opportunity:
                    lines.extend([
                        f"**Strategic Opportunity:** {opportunity}",
                        ""
                    ])

        # Insights & Warnings
        if plan['insights_warnings']:
            lines.extend([
                "",
                "## 💡 Insights & Warnings",
                ""
            ])

            for insight in plan['insights_warnings']:
                insight_type = insight.get('type', 'NOTE')
                severity = insight.get('severity', 'INFO')
                message = insight.get('message', '')
                actionable = insight.get('actionable', '')

                # Emoji based on type
                emoji = self._get_emoji_for_type(insight_type, severity)

                lines.extend([
                    f"### {emoji} {insight_type} [{severity}]",
                    ""
                ])

                if message:
                    lines.extend([
                        f"**Message:** {message}",
                        ""
                    ])

                if actionable:
                    lines.extend([
                        f"**Action:** {actionable}",
                        ""
                    ])

        # Time Blocking Recommendations
        if plan['time_blocking_recommendations']:
            lines.extend([
                "",
                "## ⏰ Time Blocking Recommendations",
                ""
            ])

            for rec in plan['time_blocking_recommendations']:
                lines.append(f"- {rec}")

            lines.append("")

        # JSON metadata (hidden but readable)
        lines.extend([
            "",
            "---",
            "",
            "<!--",
            "## Metadata (JSON)",
            "",
            "```json",
            json.dumps(plan, indent=2),
            "```",
            "-->"
        ])

        return "\n".join(lines)

    def _get_emoji_for_type(self, insight_type: str, severity: str) -> str:
        """Get emoji for insight type and severity."""
        type_emoji = {
            "ATTENTION_LEAK": "🚨",
            "PREP_GAP": "⚠️",
            "STRATEGIC_DRIFT": "📉",
            "REPUTATION_RISK": "⚡",
            "SYSTEM_ERROR": "❌",
            "NOTE": "📝"
        }

        return type_emoji.get(insight_type, "💡")

    async def load(self, date: str) -> Optional[DailyPlan]:
        """
        Load daily plan from memory-bank.

        Args:
            date: Date string (YYYY-MM-DD)

        Returns:
            DailyPlan if found, None otherwise
        """
        logger.info(f"Loading daily plan for {date}")

        try:
            file_path = self.plans_dir / f"{date}-plan.md"

            if not file_path.exists():
                logger.warning(f"Plan file not found: {file_path}")
                return None

            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()

            # Extract JSON from markdown
            plan = self._extract_json_from_markdown(content)

            if plan:
                logger.info(f"Loaded daily plan for {date}")
                return plan
            else:
                logger.warning(f"Could not extract JSON from plan file")
                return None

        except Exception as e:
            logger.error(f"Failed to load daily plan: {e}")
            return None

    def _extract_json_from_markdown(self, markdown: str) -> Optional[DailyPlan]:
        """Extract JSON metadata from markdown file."""
        import re

        # Look for JSON code block in <!-- ... --> comment
        match = re.search(r'<!--.*?```json\s*(\{.*?\})\s*```.*?-->', markdown, re.DOTALL)

        if match:
            try:
                return json.loads(match.group(1))
            except json.JSONDecodeError:
                return None

        return None

    def list_plans(self) -> list[str]:
        """
        List all available daily plans.

        Returns:
            List of dates (YYYY-MM-DD) with plans
        """
        if not self.plans_dir.exists():
            return []

        plans = []
        for file_path in self.plans_dir.glob("*-plan.md"):
            # Extract date from filename
            match = re.match(r'(\d{4}-\d{2}-\d{2})-plan\.md', file_path.name)
            if match:
                plans.append(match.group(1))

        return sorted(plans, reverse=True)
