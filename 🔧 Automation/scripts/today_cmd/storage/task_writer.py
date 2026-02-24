"""TaskWriter writes daily tasks to /tasks/ directory for Claude analysis."""

import logging
import sys
from datetime import datetime, timedelta, date
from pathlib import Path
from typing import Dict, Any, List, Optional
import random

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent))
from shared.aipmos_config import AIPMOSConfig

logger = logging.getLogger(__name__)


# PM and Strategy themed quotes
DAILY_QUOTES = [
    ("The essence of strategy is choosing what not to do.", "Michael Porter"),
    ("Strategy is not about being the best. It's about being unique.", "Michael Porter"),
    ("The aim of marketing is to know and understand the customer so well the product or service fits him and sells itself.", "Peter Drucker"),
    ("People don't buy what you do; they buy why you do it.", "Simon Sinek"),
    ("Your premium brand had better be delivering something special, or it's not going to get the business.", "Jeff Bezos"),
    ("Focus on the user and all else will follow.", "Google Philosophy"),
    ("The best way to predict the future is to create it.", "Peter Drucker"),
    ("Innovation distinguishes between a leader and a follower.", "Steve Jobs"),
    ("Stay hungry, stay foolish.", "Steve Jobs"),
    ("The customer is not a moron; she is your wife.", "David Ogilvy"),
    ("Price is what you pay. Value is what you get.", "Warren Buffett"),
    "Time is the scarcest resource; if it's not managed, nothing else can be.",
    ("What gets measured gets managed.", "Peter Drucker"),
    ("Plans are nothing; planning is everything.", "Dwight D. Eisenhower"),
    ("If you're not embarrassed by the first version of your product, you've launched too late.", "Reid Hoffman"),
    ("Make something people want.", "Paul Graham"),
    ("The way to get startup ideas is not to try to think of startup ideas. It's to look for problems.", "Paul Graham"),
    ("Users don't care about your tech stack; they care about their problems.", "Unknown"),
    ("The best product managers are the ones who can say no most often.", "Unknown"),
    ("Product management is not about building more things; it's about building the right things.", "Unknown"),
    ("Your most unhappy customers are your greatest source of learning.", "Bill Gates"),
    ("Focus on the signal in the noise, and you'll find clarity.", "Unknown"),
    ("The goal is not to build more features. The goal is to build the right features.", "Unknown"),
    ("Strategy without tactics is the slowest route to victory. Tactics without strategy is the noise before defeat.", "Sun Tzu"),
    ("The only sustainable competitive advantage is an organization's ability to learn faster than the competition.", "Peter Senge"),
    ("You can't just ask customers what they want and then try to give that to them. By the time you get it built, they'll want something new.", "Steve Jobs"),
    ("If I had asked people what they wanted, they would have said faster horses.", "Henry Ford"),
]


class TaskWriter:
    """
    Writes daily tasks to /tasks/ directory for Claude analysis.

    Unlike PlanStorage (which writes analyzed plans to memory-bank),
    TaskWriter writes raw task data for Claude to analyze.
    """

    def __init__(self, tasks_path: str):
        """
        Initialize TaskWriter.

        Args:
            tasks_path: Path to tasks directory
        """
        self.tasks_path = Path(tasks_path)
        self._config = AIPMOSConfig()
        logger.info(f"TaskWriter initialized with path {self.tasks_path}")

    def backup_today_to_yesterday(self) -> None:
        """
        Backup today.md to yesterday.md before regenerating.

        This preserves yesterday's focus areas and priorities for the
        interactive carry-forward triage workflow.

        Only backs up once per day - if yesterday.md already exists
        and is from the same date, skip backup to preserve original input.
        """
        today_path = self.tasks_path / "today.md"
        yesterday_path = self.tasks_path / "yesterday.md"

        if not today_path.exists():
            logger.info("No today.md exists yet, nothing to backup")
            return

        # Check if yesterday.md already exists and is from today
        if yesterday_path.exists():
            try:
                content = yesterday_path.read_text(encoding='utf-8')
                # Check if the file contains today's date
                today_date = datetime.now().strftime("%B %d, %Y")
                if today_date in content:
                    logger.info("yesterday.md already exists from today, preserving original backup")
                    return
            except Exception:
                pass  # Continue with backup if read fails

        try:
            # Copy today.md to yesterday.md
            content = today_path.read_text(encoding='utf-8')
            yesterday_path.write_text(content, encoding='utf-8')
            logger.info(f"Backed up today.md to yesterday.md")

        except Exception as e:
            logger.error(f"Failed to backup today.md: {e}")

    def read_yesterday_content(self) -> Dict[str, List[str]]:
        """
        Read yesterday.md (backup of today.md) to extract focus areas and priorities.

        Returns:
            Dict with 'focus' (List[str]) and 'priorities' (List[str])
        """
        yesterday_path = self.tasks_path / "yesterday.md"

        if not yesterday_path.exists():
            return {'focus': [], 'priorities': []}

        try:
            content = yesterday_path.read_text(encoding='utf-8')

            result = {'focus': [], 'priorities': []}

            # Parse "## 🧠 What's On My Mind Today" section
            focus_section = self._extract_section(content, "## 🧠 What's On My Mind Today", "## 🎯")
            if focus_section:
                result['focus'] = self._parse_focus_items(focus_section)

            # Parse "## 🎯 Top 3 Priorities for Today" section
            priority_section = self._extract_section(content, "## 🎯 Top 3 Priorities for Today", "## 📋")
            if priority_section:
                result['priorities'] = self._parse_priority_items(priority_section)

            logger.info(f"Read {len(result['focus'])} focus items, {len(result['priorities'])} priorities from yesterday")
            return result

        except Exception as e:
            logger.error(f"Failed to read yesterday's content: {e}")
            return {'focus': [], 'priorities': []}

    def _extract_section(self, content: str, start_marker: str, end_marker: str) -> str:
        """
        Extract a section from markdown content between two markers.

        Args:
            content: Full markdown content
            start_marker: Section heading to start from
            end_marker: Section heading to end at

        Returns:
            Section content without markers
        """
        try:
            start_idx = content.find(start_marker)
            if start_idx == -1:
                return ""

            end_idx = content.find(end_marker, start_idx)
            if end_idx == -1:
                return content[start_idx + len(start_marker):]

            section = content[start_idx + len(start_marker):end_idx].strip()
            return section

        except Exception:
            return ""

    def _parse_focus_items(self, section: str) -> List[str]:
        """
        Parse focus items from "What's On My Mind Today" section.

        Args:
            section: Section content

        Returns:
            List of focus item strings
        """
        items = []
        lines = section.split('\n')

        for line in lines:
            line = line.strip()
            # Skip empty lines, comments, and notes
            if not line or line.startswith('<!--') or line.lower().startswith('note:'):
                continue

            # Look for numbered items like "**1.**" or "**1. "
            if line.startswith('**') and '.' in line:
                # Extract the text after the number
                parts = line.split('.', 1)
                if len(parts) > 1:
                    item = parts[1].strip()
                    # Remove trailing bold markers
                    item = item.rstrip('*').strip()
                    if item:
                        items.append(item)

        return items

    def _parse_priority_items(self, section: str) -> List[str]:
        """
        Parse priority items from "Top 3 Priorities" section.

        Args:
            section: Section content

        Returns:
            List of priority strings
        """
        items = []
        lines = section.split('\n')

        for line in lines:
            line = line.strip()
            # Skip empty lines, comments, notes, and non-priority lines
            if not line or line.startswith('<!--'):
                continue

            # Look for numbered priorities like "**1.**" or "**2.**"
            # Must start with **, followed by a digit, then .
            if line.startswith('**') and any(line.startswith(f'**{i}.') for i in range(1, 10)):
                # Extract the text after the number
                parts = line.split('.', 1)
                if len(parts) > 1:
                    item = parts[1].strip()
                    # Get just the first line (the priority title, before any asterisk)
                    if '*' in item:
                        item = item.split('*')[0].strip()
                    if item:
                        items.append(item)

        return items

    def format_carried_forward_focus(self, focus_items: List[str]) -> str:
        """
        Format carried-forward focus areas for insertion into today.md.

        Args:
            focus_items: List of focus area strings to carry forward

        Returns:
            Formatted markdown string for the "What's On My Mind Today" section
        """
        if not focus_items:
            return "<!-- User input captured after /today workflow completes -->"

        lines = []
        for idx, item in enumerate(focus_items, 1):
            lines.append(f"**{idx}.** {item}")

        return "\n\n".join(lines)

    def get_triage_items(self) -> List[Dict[str, str]]:
        """
        Get all items from yesterday for interactive triage.

        Returns:
            List of dicts with 'type', 'text', and 'id' for each item
        """
        yesterday = self.read_yesterday_content()

        items = []

        # Add focus areas
        for idx, focus in enumerate(yesterday['focus']):
            items.append({
                'type': 'focus',
                'id': f'focus-{idx}',
                'text': focus
            })

        # Add priorities
        for idx, priority in enumerate(yesterday['priorities']):
            items.append({
                'type': 'priority',
                'id': f'priority-{idx}',
                'text': priority
            })

        return items

    def append_to_completed(self, focus_items: List[str], priority_items: List[str]) -> None:
        """
        Append completed items to completed.md.

        Args:
            focus_items: Focus areas that were completed
            priority_items: Priorities that were completed
        """
        if not focus_items and not priority_items:
            return

        completed_path = self.tasks_path / "completed.md"

        try:
            # Read existing or create new
            if completed_path.exists():
                content = completed_path.read_text(encoding='utf-8')
            else:
                content = "# Completed Items\n\nItems marked as complete in daily triage.\n\n"

            # Get today's date
            today = datetime.now().strftime("%a %b %d, %Y")

            # Append today's completions
            content += f"## {today}\n\n"

            if focus_items:
                content += "### Focus Areas Completed\n\n"
                for item in focus_items:
                    content += f"- {item}\n"
                content += "\n"

            if priority_items:
                content += "### Priorities Completed\n\n"
                for item in priority_items:
                    content += f"- {item}\n"
                content += "\n"

            # Write back
            completed_path.write_text(content, encoding='utf-8')
            logger.info(f"Appended {len(focus_items)} focus items and {len(priority_items)} priorities to completed.md")

        except Exception as e:
            logger.error(f"Failed to write completed.md: {e}")

    async def write_today(
        self,
        collected_data: Dict[str, Any],
        tasks_due_today: List[Dict],
        overdue_tasks: List[Dict],
        granola_action_items: Optional[List[str]] = None,
        meetings_for_ai: Optional[List[Dict]] = None
    ) -> str:
        """
        Write today.md with raw task data for Claude analysis.

        Args:
            collected_data: Raw data from collectors (AgilePlace, Granola, etc.)
            tasks_due_today: List of tasks due today
            overdue_tasks: List of overdue tasks
            granola_action_items: List of formatted action item strings from meetings
            meetings_for_ai: List of meeting dicts for embedded AI analysis

        Returns:
            Path to written file
        """
        logger.info("Writing today.md")

        # Backup today.md to yesterday.md before regenerating
        self.backup_today_to_yesterday()

        try:
            # Ensure directory exists
            self.tasks_path.mkdir(parents=True, exist_ok=True)

            # Build file path
            file_path = self.tasks_path / "today.md"

            # Get today's date
            today = datetime.now()
            date_str = today.strftime("%A, %B %d, %Y")

            # Get daily quote
            quote = self._get_daily_quote(today)

            # Generate markdown content
            markdown = self._format_today_md(
                date_str=date_str,
                quote=quote,
                tasks_due_today=tasks_due_today,
                overdue_tasks=overdue_tasks,
                collected_data=collected_data,
                granola_action_items=granola_action_items or [],
                meetings_for_ai=meetings_for_ai or []
            )

            # Write file
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(markdown)

            logger.info(f"today.md written to {file_path}")
            return str(file_path)

        except Exception as e:
            logger.error(f"Failed to write today.md: {e}")
            raise IOError(f"Failed to write today.md: {e}")

    async def write_weekly_views(
        self,
        all_tasks: List[Dict],
        all_cards: List[Dict]
    ) -> Dict[str, str]:
        """
        Write this-week.md and next-week.md with weekly task views.

        Args:
            all_tasks: All tasks from AgilePlace
            all_cards: All cards from AgilePlace

        Returns:
            Dict with paths to written files
        """
        logger.info("Writing weekly views")

        try:
            # Ensure directory exists
            self.tasks_path.mkdir(parents=True, exist_ok=True)

            # Combine tasks and cards
            all_items = all_tasks + all_cards

            # Filter items with due dates
            dated_items = [
                item for item in all_items
                if item.get('due_date') and not item.get('finished_on')
            ]

            # Group by date
            items_by_date = self._group_by_due_date(dated_items)

            # Calculate date ranges
            today = date.today()
            this_week_start = today
            this_week_end = today + timedelta(days=6)
            next_week_start = today + timedelta(days=7)
            next_week_end = today + timedelta(days=13)

            # Filter for this week and next week
            this_week_items = {}
            next_week_items = {}

            for date_str, items in items_by_date.items():
                try:
                    item_date = datetime.strptime(date_str, "%Y-%m-%d").date()
                    if this_week_start <= item_date <= this_week_end:
                        this_week_items[date_str] = items
                    elif next_week_start <= item_date <= next_week_end:
                        next_week_items[date_str] = items
                except ValueError:
                    continue

            # Write this-week.md
            this_week_path = self.tasks_path / "this-week.md"
            this_week_markdown = self._format_week_md(
                title="This Week",
                date_range=f"{this_week_start.strftime('%b %d')}-{this_week_end.strftime('%b %d, %Y')}",
                items_by_date=this_week_items,
                total_count=sum(len(items) for items in this_week_items.values())
            )
            with open(this_week_path, 'w', encoding='utf-8') as f:
                f.write(this_week_markdown)

            # Write next-week.md
            next_week_path = self.tasks_path / "next-week.md"
            next_week_markdown = self._format_week_md(
                title="Next Week",
                date_range=f"{next_week_start.strftime('%b %d')}-{next_week_end.strftime('%b %d, %Y')}",
                items_by_date=next_week_items,
                total_count=sum(len(items) for items in next_week_items.values())
            )
            with open(next_week_path, 'w', encoding='utf-8') as f:
                f.write(next_week_markdown)

            logger.info(f"Weekly views written: {this_week_path}, {next_week_path}")

            return {
                "this_week": str(this_week_path),
                "next_week": str(next_week_path)
            }

        except Exception as e:
            logger.error(f"Failed to write weekly views: {e}")
            raise IOError(f"Failed to write weekly views: {e}")

    def _get_daily_quote(self, date: datetime) -> tuple:
        """
        Get a daily quote based on the date.

        Uses day of year to select quote consistently.

        Args:
            date: Current date

        Returns:
            Tuple of (quote, author) or just quote string
        """
        day_of_year = date.timetuple().tm_yday
        index = day_of_year % len(DAILY_QUOTES)
        quote = DAILY_QUOTES[index]

        # Convert string to tuple if needed
        if isinstance(quote, str):
            return (quote, "")
        return quote

    def _format_today_md(
        self,
        date_str: str,
        quote: tuple,
        tasks_due_today: List[Dict],
        overdue_tasks: List[Dict],
        collected_data: Dict[str, Any],
        granola_action_items: Optional[List[str]] = None,
        meetings_for_ai: Optional[List[Dict]] = None
    ) -> str:
        """
        Format today.md content.

        Args:
            date_str: Date string (e.g., "Monday, January 15, 2026")
            quote: Tuple of (quote, author)
            tasks_due_today: List of tasks due today
            overdue_tasks: List of overdue tasks
            collected_data: Raw collected data
            granola_action_items: List of formatted action item strings from meetings
            meetings_for_ai: List of meeting dicts for embedded AI analysis

        Returns:
            Markdown string
        """
        quote_text, quote_author = quote
        if quote_author:
            quote_block = f'> "{quote_text}" — **{quote_author}**'
        else:
            quote_block = f'> "{quote_text}"'

        # Determine data sources for footer
        data_sources = ["AgilePlace"]
        granola_data = collected_data.get("granola", {})
        if granola_data.get("meetings"):
            data_sources.append("Granola")

        lines = [
            f"# Today's Plan - {date_str}",
            "",
            quote_block,
            "",
            "## 🧠 What's On My Mind Today",
            "<!-- User input captured after /today workflow completes -->",
            "",
            "",
            "## 🎯 Top 3 Priorities for Today",
            "<!-- Claude/Cursor populates this with analysis -->",
            "",
            "",
            "## 📋 Tasks Due Today",
            ""
        ]

        # Tasks due today from AgilePlace
        if tasks_due_today:
            for task in tasks_due_today:
                lines.append(self._format_task(task))
        else:
            lines.append("*No AgilePlace tasks due today*")

        # Add Granola action items to Tasks Due Today
        if granola_action_items:
            for item in granola_action_items:
                lines.append(f"- [ ] {item}")  # item already formatted with (granola - Title)

        lines.extend([
            "",
            "",
            "## 📋 Overdue",
            ""
        ])

        # Overdue tasks
        if overdue_tasks:
            for task in overdue_tasks:
                lines.append(self._format_task(task, show_overdue=True))
        else:
            lines.append("*No overdue tasks*")

        # Ideas & Considerations section
        lines.extend([
            "",
            "",
            "## 💡 Ideas & Considerations",
            ""
        ])

        # Add meeting context for AI analysis
        if meetings_for_ai:
            lines.extend([
                "<!-- Meeting summaries for AI strategic analysis -->",
                ""
            ])
            for meeting in meetings_for_ai:
                title = meeting.get("title", "Untitled")
                summary = meeting.get("summary", "") or meeting.get("notes", "")
                if summary:
                    lines.append(f"### {title}")
                    lines.append("")
                    lines.append(summary)
                    lines.append("")
            lines.extend(["<!-- End meeting context -->", ""])
        else:
            lines.append("<!-- Claude/Cursor populates this with insights -->")
            lines.append("")

        # Count this week's tasks for preview
        agileplace = collected_data.get("agileplace", {})
        all_tasks = agileplace.get("tasks", [])
        all_cards = agileplace.get("cards", [])
        all_items = all_tasks + all_cards

        this_week_count = self._count_tasks_this_week(all_items)

        lines.extend([
            f"## 📅 This Week Preview",
            f"[{this_week_count} cards due this week] → `this-week.md`",
            "",
            "",
            "---",
            "",
            f"*Generated at {datetime.now().strftime('%I:%M %p')} from {', '.join(data_sources)}*"
        ])

        return "\n".join(lines)

    def _format_week_md(
        self,
        title: str,
        date_range: str,
        items_by_date: Dict[str, List[Dict]],
        total_count: int
    ) -> str:
        """
        Format weekly view content (this-week.md or next-week.md).

        Args:
            title: Title (e.g., "This Week" or "Next Week")
            date_range: Date range string
            items_by_date: Dict mapping dates to lists of items
            total_count: Total number of items in the week

        Returns:
            Markdown string
        """
        lines = [
            f"# {title} - {date_range}",
            "",
            f"**Total:** {total_count} cards due",
            "",
            "---",
            ""
        ]

        if not items_by_date:
            lines.append("*No cards due this period*")
            return "\n".join(lines)

        # Sort dates
        sorted_dates = sorted(items_by_date.keys())

        for date_str in sorted_dates:
            try:
                date_obj = datetime.strptime(date_str, "%Y-%m-%d")
                day_name = date_obj.strftime("%A")
                formatted_date = date_obj.strftime("%b %d")

                lines.append(f"## {day_name}, {formatted_date}")
                lines.append("")

                items = items_by_date[date_str]
                for item in items:
                    lines.append(self._format_task(item))

                lines.append("")

            except ValueError:
                continue

        lines.extend([
            "---",
            "",
            f"*Generated at {datetime.now().strftime('%I:%M %p')} from AgilePlace*"
        ])

        return "\n".join(lines)

    def _format_task(self, task: Dict, show_overdue: bool = False) -> str:
        """
        Format a single task as markdown.

        Args:
            task: Task dict from AgilePlace
            show_overdue: Whether to show overdue info

        Returns:
            Markdown string
        """
        title = task.get("title", "Untitled").strip()
        task_id = task.get("id", "")

        # Build AgilePlace URL from config
        domain = self._config.get("integrations.agileplace.domain", "https://planview.leankit.com")
        if not domain.startswith("https://"):
            domain = f"https://{domain}"
        if task_id:
            url = f"{domain}/card/{task_id}"
            title = f"[{title}]({url})"

        # Add overdue info
        if show_overdue:
            due_date = task.get("due_date")
            if due_date:
                try:
                    due_obj = datetime.fromisoformat(due_date.replace('Z', '+00:00'))
                    day_name = due_obj.strftime("%A")
                    title = f"{title} *(was due {day_name})*"
                except:
                    pass

        return f"- [ ] {title}"

    def _group_by_due_date(self, items: List[Dict]) -> Dict[str, List[Dict]]:
        """
        Group items by due date.

        Args:
            items: List of tasks/cards with due_date

        Returns:
            Dict mapping YYYY-MM-DD to list of items
        """
        grouped = {}

        for item in items:
            due_date = item.get("due_date")
            if not due_date:
                continue

            try:
                # Parse date and convert to YYYY-MM-DD
                dt = datetime.fromisoformat(due_date.replace('Z', '+00:00'))
                date_key = dt.strftime("%Y-%m-%d")

                if date_key not in grouped:
                    grouped[date_key] = []

                grouped[date_key].append(item)

            except (ValueError, AttributeError):
                continue

        return grouped

    def _count_tasks_this_week(self, items: List[Dict]) -> int:
        """
        Count tasks due this week (next 7 days).

        Args:
            items: List of tasks/cards

        Returns:
            Count of tasks due this week
        """
        today = date.today()
        week_end = today + timedelta(days=6)

        count = 0
        for item in items:
            due_date = item.get("due_date")
            if not due_date:
                continue

            try:
                dt = datetime.fromisoformat(due_date.replace('Z', '+00:00')).date()
                if today <= dt <= week_end:
                    count += 1
            except (ValueError, AttributeError):
                continue

        return count
