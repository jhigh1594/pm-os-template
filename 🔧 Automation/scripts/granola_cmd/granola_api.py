"""
Granola API client - reads meetings via the Granola REST API.

Uses credentials from ~/Library/Application Support/Granola/supabase.json
and auto-refreshes the access token when expired.
"""

import gzip
import json
import logging
import os
import ssl
import time
import urllib.request
from datetime import datetime
from pathlib import Path
from typing import Any

logger = logging.getLogger(__name__)

GRANOLA_APP_SUPPORT = Path.home() / "Library" / "Application Support" / "Granola"
SUPABASE_JSON = GRANOLA_APP_SUPPORT / "supabase.json"
STORED_ACCOUNTS_JSON = GRANOLA_APP_SUPPORT / "stored-accounts.json"
WORKOS_CLIENT_ID = "client_01JZJ0XBDAT8PHJWQY09Y0VD61"
API_BASE = "https://api.granola.ai"
PUBLIC_API_BASE = "https://public-api.granola.ai/v1"
WORKOS_AUTH_URL = "https://api.workos.com/user_management/authenticate"
USER_AGENT = "Granola/5.354.0"


def _ssl_ctx() -> ssl.SSLContext:
    ctx = ssl.create_default_context()
    try:
        import certifi
        ctx = ssl.create_default_context(cafile=certifi.where())
    except ImportError:
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE
    return ctx


def _get(url: str, token: str) -> Any:
    ctx = _ssl_ctx()
    req = urllib.request.Request(
        url,
        headers={"Authorization": f"Bearer {token}", "Accept": "application/json"},
    )
    with urllib.request.urlopen(req, timeout=30, context=ctx) as resp:
        raw = resp.read()
        if resp.headers.get("Content-Encoding") == "gzip":
            raw = gzip.decompress(raw)
    return json.loads(raw)


def _post(url: str, payload: dict, token: str) -> dict:
    ctx = _ssl_ctx()
    req = urllib.request.Request(
        url,
        data=json.dumps(payload).encode(),
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate",
            "User-Agent": USER_AGENT,
            "X-Client-Version": USER_AGENT.split("/")[1],
        },
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=30, context=ctx) as resp:
        raw = resp.read()
        if resp.headers.get("Content-Encoding") == "gzip":
            raw = gzip.decompress(raw)
    return json.loads(raw)


class GranolaCacheReader:
    """Fetch Granola meetings from the REST API, with auto token refresh."""

    def __init__(self, cache_path: str | None = None):
        self._token: str | None = None
        self._token_expiry: float = 0
        self._docs_cache: list[dict] | None = None

    def _load_token(self) -> str:
        # Try stored-accounts.json first (Granola v6+), fall back to supabase.json
        if STORED_ACCOUNTS_JSON.exists():
            with open(STORED_ACCOUNTS_JSON) as f:
                data = json.load(f)
            accounts = json.loads(data["accounts"])
            if accounts:
                wt = json.loads(accounts[0]["tokens"])
                token = wt["access_token"]
                obtained_at = wt.get("obtained_at", 0)
                expires_in = wt.get("expires_in", 21600)
                self._token_expiry = obtained_at / 1000 + expires_in
                self._token = token
                return token
        with open(SUPABASE_JSON) as f:
            data = json.load(f)
        wt = json.loads(data["workos_tokens"])
        token = wt["access_token"]
        obtained_at = wt.get("obtained_at", 0)
        expires_in = wt.get("expires_in", 21600)
        self._token_expiry = obtained_at / 1000 + expires_in
        self._token = token
        return token

    def _refresh_token(self) -> str:
        logger.info("Refreshing Granola access token")
        ctx = _ssl_ctx()
        # Load refresh token from stored-accounts.json (v6+) or supabase.json
        if STORED_ACCOUNTS_JSON.exists():
            with open(STORED_ACCOUNTS_JSON) as f:
                sa_data = json.load(f)
            accounts = json.loads(sa_data["accounts"])
            wt = json.loads(accounts[0]["tokens"]) if accounts else {}
        else:
            with open(SUPABASE_JSON) as f:
                sa_data = None
                sb_data = json.load(f)
            wt = json.loads(sb_data["workos_tokens"])
        req = urllib.request.Request(
            WORKOS_AUTH_URL,
            data=json.dumps({
                "client_id": WORKOS_CLIENT_ID,
                "grant_type": "refresh_token",
                "refresh_token": wt["refresh_token"],
            }).encode(),
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        with urllib.request.urlopen(req, timeout=15, context=ctx) as resp:
            raw = resp.read()
            if resp.headers.get("Content-Encoding") == "gzip":
                raw = gzip.decompress(raw)
            new_tokens = json.loads(raw)
        wt["access_token"] = new_tokens["access_token"]
        wt["obtained_at"] = int(time.time() * 1000)
        if new_tokens.get("refresh_token"):
            wt["refresh_token"] = new_tokens["refresh_token"]
        # Write back to whichever file we read from
        if STORED_ACCOUNTS_JSON.exists() and sa_data is not None:
            accounts[0]["tokens"] = json.dumps(wt)
            accounts[0]["savedAt"] = wt["obtained_at"]
            sa_data["accounts"] = json.dumps(accounts)
            with open(STORED_ACCOUNTS_JSON, "w") as f:
                json.dump(sa_data, f)
        else:
            sb_data["workos_tokens"] = json.dumps(wt)
            with open(SUPABASE_JSON, "w") as f:
                json.dump(sb_data, f)
        self._token = None
        self._token_expiry = 0
        return self._load_token()

    def _get_token(self) -> str:
        api_key = os.environ.get("GRANOLA_API_KEY")
        if api_key:
            return api_key
        if not self._token or time.time() >= self._token_expiry - 300:
            try:
                self._load_token()
            except Exception:
                pass
        if not self._token:
            raise RuntimeError("Could not load Granola credentials from stored-accounts.json or supabase.json")
        if time.time() >= self._token_expiry - 300:
            self._token = self._refresh_token()
        return self._token

    def _normalize_public_doc(self, note: dict) -> dict:
        """Map public API note shape to internal doc shape."""
        attendees = note.get("attendees") or []
        return {
            "id": note["id"],
            "title": note.get("title") or "Untitled",
            "created_at": note.get("created_at", ""),
            "updated_at": note.get("updated_at", ""),
            "duration": 0,
            "notes_markdown": note.get("summary_markdown") or "",
            "notes_plain": note.get("summary_text") or "",
            "people": [{"name": a.get("name", ""), "email": a.get("email", "")} for a in attendees],
            "_transcript_segments": note.get("transcript") or [],
            "_public_api": True,
        }

    def _fetch_all_docs_public(self, created_after: str | None = None) -> list[dict]:
        token = self._get_token()
        all_notes: list[dict] = []
        url = f"{PUBLIC_API_BASE}/notes?include=transcript&limit=100"
        if created_after:
            url += f"&created_after={created_after}"
        while url:
            result = _get(url, token)
            for note in result.get("notes", []):
                all_notes.append(self._normalize_public_doc(note))
            url = result.get("cursor") if result.get("hasMore") else None
            if url:
                url = f"{PUBLIC_API_BASE}/notes?include=transcript&limit=100&cursor={result['cursor']}"
                if created_after:
                    url += f"&created_after={created_after}"
        return all_notes

    def _fetch_all_docs(self) -> list[dict]:
        if self._docs_cache is not None:
            return self._docs_cache
        if os.environ.get("GRANOLA_API_KEY"):
            all_docs = self._fetch_all_docs_public()
        else:
            token = self._get_token()
            all_docs = []
            offset = 0
            limit = 100
            while True:
                result = _post(
                    f"{API_BASE}/v2/get-documents",
                    {"limit": limit, "offset": offset, "include_last_viewed_panel": True},
                    token,
                )
                docs = result.get("docs", [])
                if not docs:
                    break
                all_docs.extend(docs)
                logger.debug(f"Fetched {len(all_docs)} docs so far (offset {offset})")
                offset += limit
                if offset > 10000:
                    break
        logger.info(f"Fetched {len(all_docs)} total documents from Granola API")
        self._docs_cache = all_docs
        return all_docs

    def search_meetings(self, query: str, limit: int = 100) -> list[dict[str, Any]]:
        """Search documents by date string (YYYY-MM-DD) in created_at."""
        if os.environ.get("GRANOLA_API_KEY") and len(query) == 10:
            # Use created_after for efficient date filtering on public API
            docs = self._fetch_all_docs_public(created_after=f"{query}T00:00:00Z")
            self._docs_cache = (self._docs_cache or []) + [d for d in docs if d["id"] not in {x["id"] for x in (self._docs_cache or [])}]
        else:
            docs = self._fetch_all_docs()
        results = []
        for doc in docs:
            created = doc.get("created_at", "")
            if query in created:
                results.append({"meeting_id": doc["id"], **doc})
            if len(results) >= limit:
                break
        logger.info(f"Found {len(results)} documents matching '{query}'")
        return results

    def get_meeting_details(self, meeting_id: str) -> dict[str, Any]:
        docs = self._fetch_all_docs()
        doc = next((d for d in docs if d["id"] == meeting_id), {})
        return {
            "meeting_id": meeting_id,
            "title": doc.get("title") or "Untitled",
            "created_at": doc.get("created_at", ""),
            "duration": doc.get("duration", 0),
            "participants": self._extract_participants(doc),
        }

    def _extract_participants(self, doc: dict[str, Any]) -> list[str]:
        participants: list[str] = []
        people = doc.get("people")
        if people and isinstance(people, list):
            for person in people:
                if isinstance(person, dict):
                    name = person.get("name") or person.get("email", "")
                    if name:
                        participants.append(name)
                elif isinstance(person, str):
                    participants.append(person)
        gcal = doc.get("google_calendar_event")
        if gcal and isinstance(gcal, dict):
            for attendee in gcal.get("attendees", []):
                if isinstance(attendee, dict):
                    name = attendee.get("displayName") or attendee.get("email", "")
                    if name and name not in participants:
                        participants.append(name)
        return participants

    def get_meeting_transcript(self, meeting_id: str) -> str:
        """Fetch transcript via API."""
        # Use cached segments if available from public API fetch
        docs = self._docs_cache or []
        doc = next((d for d in docs if d["id"] == meeting_id), None)
        if doc and doc.get("_transcript_segments") is not None:
            segments = doc["_transcript_segments"]
        elif os.environ.get("GRANOLA_API_KEY"):
            try:
                token = self._get_token()
                note = _get(f"{PUBLIC_API_BASE}/notes/{meeting_id}?include=transcript", token)
                segments = note.get("transcript") or []
            except Exception as e:
                logger.warning(f"Transcript fetch failed for {meeting_id}: {e}")
                return ""
        else:
            try:
                token = self._get_token()
                result = _post(
                    f"{API_BASE}/v1/get-document-transcript",
                    {"document_id": meeting_id},
                    token,
                )
                segments = result if isinstance(result, list) else result.get("segments", [])
            except Exception as e:
                logger.warning(f"Transcript fetch failed for {meeting_id}: {e}")
                return ""
        lines = []
        for seg in segments:
            if isinstance(seg, dict):
                speaker = seg.get("speaker", "Unknown")
                if isinstance(speaker, dict):
                    speaker = speaker.get("name") or speaker.get("source", "Unknown")
                text = seg.get("text", "")
                lines.append(f"{speaker}: {text}")
        return "\n".join(lines)

    def get_meeting_documents(self, meeting_id: str) -> list[dict[str, Any]]:
        docs = self._fetch_all_docs()
        doc = next((d for d in docs if d["id"] == meeting_id), {})
        result = []
        if doc.get("overview"):
            result.append({"title": "Overview", "content": doc["overview"]})
        if doc.get("notes_plain"):
            result.append({"title": "Notes", "content": doc["notes_plain"]})
        if doc.get("notes_markdown"):
            result.append({"title": "Notes (Markdown)", "content": doc["notes_markdown"]})
        if doc.get("summary"):
            result.append({"title": "Summary", "content": doc["summary"]})
        return result

    def get_granola_summary(self, meeting_id: str) -> str | None:
        docs = self._fetch_all_docs()
        doc = next((d for d in docs if d["id"] == meeting_id), {})
        return doc.get("notes_markdown") or doc.get("summary_markdown") or doc.get("notes_plain") or doc.get("summary_text") or None


MCPClient = GranolaCacheReader
