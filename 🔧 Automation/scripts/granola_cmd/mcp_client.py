"""
Granola cache reader - direct file access alternative to MCP server.

Reads Granola meetings directly from the cache file.
This is simpler and more reliable than subprocess MCP communication.
"""

import json
import logging
from datetime import datetime
from pathlib import Path
from typing import Any

logger = logging.getLogger(__name__)


class GranolaCacheReader:
    """Read Granola meetings directly from cache file."""

    def __init__(self, cache_path: str | None = None):
        """
        Initialize cache reader.

        Args:
            cache_path: Path to cache file (defaults to ~/Library/Application Support/Granola/cache-v3.json)
        """
        if cache_path is None:
            cache_path = "~/Library/Application Support/Granola/cache-v3.json"
        self.cache_path = Path(cache_path).expanduser()
        self._cache_data: dict[str, Any] | None = None
        self._state: dict[str, Any] | None = None

    def load_cache(self) -> dict[str, Any]:
        """
        Load Granola cache file.

        Returns:
            Cache data as dictionary
        """
        if self._cache_data is not None:
            return self._cache_data

        if not self.cache_path.exists():
            raise FileNotFoundError(f"Cache not found: {self.cache_path}")

        logger.debug(f"Loading cache from: {self.cache_path}")
        with open(self.cache_path, "r") as f:
            raw_data = json.load(f)

        # The actual cache is nested under 'cache' key as JSON string
        cache_str = raw_data.get("cache", "{}")
        self._cache_data = json.loads(cache_str)
        self._state = self._cache_data.get("state", {})

        documents = self._state.get("documents", {})
        logger.info(f"Loaded cache with {len(documents)} documents")
        return self._cache_data

    def search_meetings(self, query: str, limit: int = 100) -> list[dict[str, Any]]:
        """
        Search meetings by query string.

        Args:
            query: Search query (e.g., date string like "2026-01-14")
            limit: Maximum number of results

        Returns:
            List of meeting summaries with meeting_id
        """
        state = self.load_cache().get("state", {})
        documents = state.get("documents", {})

        query_lower = query.lower()
        results = []

        for doc_id, doc_data in documents.items():
            # Search in created_at (date)
            created_at = doc_data.get("created_at", "")
            if query_lower in created_at.lower():
                results.append({"meeting_id": doc_id, **doc_data})
                if len(results) >= limit:
                    break

            # Also search in title
            title = (doc_data.get("title") or "").lower()
            if query_lower in title:
                if not any(r["meeting_id"] == doc_id for r in results):
                    results.append({"meeting_id": doc_id, **doc_data})
                    if len(results) >= limit:
                        break

        logger.info(f"Found {len(results)} documents matching '{query}'")
        return results

    def get_meeting_details(self, meeting_id: str) -> dict[str, Any]:
        """
        Get meeting details.

        Args:
            meeting_id: Granola document ID

        Returns:
            Meeting metadata
        """
        state = self.load_cache().get("state", {})
        documents = state.get("documents", {})
        doc = documents.get(meeting_id, {})

        # Extract common fields
        details = {
            "meeting_id": meeting_id,
            "title": doc.get("title") or "Untitled",
            "created_at": doc.get("created_at", ""),
            "duration": doc.get("duration", 0),
            "participants": self._extract_participants(doc),
        }

        return details

    def _extract_participants(self, doc: dict[str, Any]) -> list[str]:
        """
        Extract participant names from document.

        Args:
            doc: Document data

        Returns:
            List of participant names
        """
        participants = []

        # Check people field - can be list of dicts or other structures
        people = doc.get("people")
        if people and isinstance(people, list):
            for person in people:
                if isinstance(person, dict):
                    name = person.get("name") or person.get("email", "")
                    if name:
                        participants.append(name)
                elif isinstance(person, str):
                    participants.append(person)

        # Check google_calendar_event attendees
        gcal_event = doc.get("google_calendar_event")
        if gcal_event and isinstance(gcal_event, dict):
            attendees = gcal_event.get("attendees", [])
            if isinstance(attendees, list):
                for attendee in attendees:
                    if isinstance(attendee, dict):
                        email = attendee.get("email", "")
                        name = attendee.get("displayName", "") or email
                        if name and name not in participants:
                            participants.append(name)

        return participants

    def get_meeting_transcript(self, meeting_id: str) -> str:
        """
        Get meeting transcript.

        Args:
            meeting_id: Granola document ID

        Returns:
            Full transcript as string
        """
        state = self.load_cache().get("state", {})
        transcripts = state.get("transcripts", {})

        # Find transcript for this document
        transcript_data = transcripts.get(meeting_id)
        if not transcript_data:
            return ""

        # Handle both list and dict formats
        segments = []
        if isinstance(transcript_data, dict):
            segments = transcript_data.get("segments", [])
        elif isinstance(transcript_data, list):
            # The transcript data itself might be a list of segments
            segments = transcript_data

        if not segments:
            return ""

        # Format transcript with speakers
        transcript_lines = []
        for segment in segments:
            speaker = segment.get("speaker", "Unknown") if isinstance(segment, dict) else "Unknown"
            text = segment.get("text", "") if isinstance(segment, dict) else str(segment)
            transcript_lines.append(f"{speaker}: {text}")

        return "\n".join(transcript_lines)

    def get_meeting_documents(self, meeting_id: str) -> list[dict[str, Any]]:
        """
        Get meeting documents (notes, summaries, etc.).

        Args:
            meeting_id: Granola document ID

        Returns:
            List of document objects
        """
        state = self.load_cache().get("state", {})
        documents = state.get("documents", {})
        doc = documents.get(meeting_id, {})

        result = []

        # Add overview if available
        overview = doc.get("overview")
        if overview:
            result.append({"title": "Overview", "content": overview})

        # Add notes_plain if available
        notes_plain = doc.get("notes_plain")
        if notes_plain:
            result.append({"title": "Notes", "content": notes_plain})

        # Add notes_markdown if available
        notes_markdown = doc.get("notes_markdown")
        if notes_markdown:
            result.append({"title": "Notes (Markdown)", "content": notes_markdown})

        # Add summary if available
        summary = doc.get("summary")
        if summary:
            result.append({"title": "Summary", "content": summary})

        return result

    def get_granola_summary(self, meeting_id: str) -> str | None:
        """
        Get Granola's AI-generated summary from documentPanels.

        Args:
            meeting_id: Granola document ID

        Returns:
            Extracted summary text or None if not found
        """
        state = self.load_cache().get("state", {})
        document_panels = state.get("documentPanels", {})

        if meeting_id not in document_panels:
            return None

        panel_data = document_panels[meeting_id]
        if not panel_data:
            return None

        # Get the first panel (usually the summary panel)
        panel_id = next(iter(panel_data.keys()), None)
        if not panel_id:
            return None

        panel = panel_data[panel_id]
        content = panel.get("content")

        if not content:
            return None

        # Extract text from Tiptap document structure
        text = self._extract_text_from_tiptap(content)
        return text if text else None

    def _extract_text_from_tiptap(self, node: Any) -> str:
        """
        Recursively extract text from Tiptap document structure, preserving formatting.

        Args:
            node: Tiptap node (dict, list, or string)

        Returns:
            Extracted text content with basic markdown formatting
        """
        if isinstance(node, str):
            return node
        elif isinstance(node, dict):
            # Extract text directly if present
            if "text" in node:
                text = node["text"]
                # Add bold formatting if present
                marks = node.get("marks", [])
                if any(mark.get("type") == "bold" for mark in marks):
                    text = f"**{text}**"
                return text
            # Handle headings
            if node.get("type") == "heading":
                level = node.get("attrs", {}).get("level", 1)
                content_text = self._extract_text_from_tiptap(node.get("content", ""))
                return f"\n\n{'#' * level} {content_text}\n\n"
            # Handle bullet points
            if node.get("type") == "bulletList":
                items = node.get("content", [])
                bullet_items = []
                for item in items:
                    item_text = self._extract_text_from_tiptap(item.get("content", ""))
                    bullet_items.append(f"- {item_text.strip()}")
                return "\n" + "\n".join(bullet_items) + "\n"
            # Handle list items
            if node.get("type") == "listItem":
                content_text = self._extract_text_from_tiptap(node.get("content", ""))
                return content_text
            # Handle paragraphs
            if node.get("type") == "paragraph":
                content_text = self._extract_text_from_tiptap(node.get("content", ""))
                if content_text.strip():
                    return f"{content_text}\n\n"
                return ""
            # Recursively handle content
            elif "content" in node:
                return "".join(self._extract_text_from_tiptap(child) for child in node["content"])
            return ""
        elif isinstance(node, list):
            return "".join(self._extract_text_from_tiptap(child) for child in node)
        return ""


# Alias for compatibility with existing code
MCPClient = GranolaCacheReader
