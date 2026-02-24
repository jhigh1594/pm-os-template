"""
Granola meeting collector - main orchestrator.

ETL workflow for extracting meetings from Granola and storing as markdown files.
"""

import logging
from datetime import datetime, timedelta
from typing import Any

from .mcp_client import GranolaCacheReader
from .storage.meeting_storage import MeetingData, MeetingStorage

logger = logging.getLogger(__name__)


class GranolaCollector:
    """
    Collects and stores Granola meetings.

    Simplified orchestrator for ETL operation:
    1. Extract: Fetch meetings from Granola cache
    2. Transform: Format as markdown with frontmatter
    3. Load: Save to filesystem
    """

    def __init__(self, config: dict[str, Any]):
        """
        Initialize collector.

        Args:
            config: Configuration dictionary with granola, filters, and storage settings
        """
        self.config = config
        self.cache_reader = GranolaCacheReader()
        self.storage = MeetingStorage(output_path=config["storage"]["output_path"])
        logger.info("GranolaCollector initialized")

    def execute(self) -> dict[str, Any]:
        """
        Execute collection workflow.

        Returns:
            Summary dict with meetings saved
        """
        target_date = self._get_target_date()
        logger.info(f"Collecting meetings for {target_date.strftime('%Y-%m-%d')}")

        # Extract: Search for meetings on target date
        search_results = self._search_meetings_by_date(target_date)

        if not search_results:
            logger.info(f"No meetings found for {target_date.strftime('%Y-%m-%d')}")
            return {"date": target_date.strftime("%Y-%m-%d"), "count": 0, "files": []}

        # Transform & Load: Collect details and save each meeting
        saved_files = []
        for result in search_results:
            try:
                meeting_data = self._collect_full_meeting_data(result, target_date)
                file_path = self.storage.save_meeting(meeting_data)
                saved_files.append(file_path)
            except Exception as e:
                logger.error(f"Failed to process meeting {result.get('meeting_id', 'unknown')}: {e}")

        return {
            "date": target_date.strftime("%Y-%m-%d"),
            "count": len(saved_files),
            "files": saved_files,
        }

    def _search_meetings_by_date(self, target_date: datetime) -> list[dict[str, Any]]:
        """
        Search for meetings on a specific date.

        Args:
            target_date: Date to search for meetings

        Returns:
            List of meeting search results
        """
        search_query = target_date.strftime("%Y-%m-%d")
        logger.debug(f"Searching for meetings with query: {search_query}")

        results = self.cache_reader.search_meetings(query=search_query, limit=100)
        logger.info(f"Found {len(results)} meeting(s) for {search_query}")

        return results

    def _collect_full_meeting_data(
        self, search_result: dict[str, Any], target_date: datetime
    ) -> MeetingData:
        """
        Collect complete meeting data including details, transcript, and documents.

        Args:
            search_result: Initial search result with meeting_id
            target_date: Date of the meeting

        Returns:
            Complete MeetingData object
        """
        meeting_id = search_result.get("meeting_id") or search_result.get("id")
        if not meeting_id:
            raise ValueError("Search result missing meeting_id")

        logger.debug(f"Collecting full data for meeting: {meeting_id}")

        # Get meeting details
        details = self.cache_reader.get_meeting_details(meeting_id)

        # Get transcript
        transcript = self.cache_reader.get_meeting_transcript(meeting_id)

        # Get Granola AI summary from documentPanels
        granola_summary = self.cache_reader.get_granola_summary(meeting_id)

        # Get documents (includes overview, notes_plain, notes_markdown, summary)
        documents = self.cache_reader.get_meeting_documents(meeting_id)

        # Extract summary and notes from documents
        summary = None
        notes = None
        for doc in documents or []:
            title = doc.get("title", "").lower()
            if title == "summary" and not summary:
                summary = doc.get("content")
            elif title in ("notes", "notes (markdown)") and not notes:
                notes = doc.get("content")

        # Build MeetingData object
        return MeetingData(
            meeting_id=meeting_id,
            title=details.get("title", search_result.get("title", "Untitled")),
            date=target_date,
            duration_minutes=details.get("duration", search_result.get("duration", 0)),
            participants=details.get("participants", search_result.get("participants", [])),
            transcript=transcript,
            notes=notes,
            summary=summary,
            granola_summary=granola_summary,
            documents=documents if documents else [],
        )

    def _get_target_date(self) -> datetime:
        """
        Get target date from config.

        Returns:
            Target datetime object
        """
        target = self.config.get("target_date", "yesterday")

        if target == "yesterday":
            return datetime.now() - timedelta(days=1)
        elif target == "today":
            return datetime.now()
        else:
            # Parse YYYY-MM-DD
            return datetime.strptime(target, "%Y-%m-%d")
