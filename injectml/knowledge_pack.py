"""
KnowledgePack – loads and stores structured domain knowledge for injection.

A knowledge pack is a JSON file with the following schema::

    {
        "name": "<pack name>",
        "version": "1.0",
        "domain": "<domain string>",
        "entries": [
            {
                "id": "<unique id>",
                "tags": ["<tag1>", ...],
                "text": "<knowledge statement>"
            },
            ...
        ],
        "aliases": {
            "<term>": "<canonical form>",
            ...
        }
    }
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Dict, List, Optional


class KnowledgeEntry:
    """A single fact or rule stored in a KnowledgePack."""

    def __init__(self, entry_id: str, tags: List[str], text: str) -> None:
        self.id = entry_id
        self.tags = tags
        self.text = text

    def matches_tags(self, tags: List[str]) -> bool:
        """Return True if *any* of the given tags are present in this entry."""
        return bool(set(tags) & set(self.tags))

    def to_dict(self) -> dict:
        return {"id": self.id, "tags": self.tags, "text": self.text}

    def __repr__(self) -> str:  # pragma: no cover
        return f"KnowledgeEntry(id={self.id!r}, tags={self.tags!r})"


class KnowledgePack:
    """Container for offline domain knowledge.

    Parameters
    ----------
    name:
        Human-readable name of the knowledge pack.
    domain:
        Domain identifier (e.g. ``"wine_pairing"``).
    version:
        Pack version string (semver recommended).
    entries:
        List of :class:`KnowledgeEntry` objects.
    aliases:
        Mapping from alternative term spellings to their canonical form,
        used by :mod:`injectml.hcmd` Meaning Stabilization.
    """

    def __init__(
        self,
        name: str,
        domain: str = "",
        version: str = "1.0",
        entries: Optional[List[KnowledgeEntry]] = None,
        aliases: Optional[Dict[str, str]] = None,
    ) -> None:
        self.name = name
        self.domain = domain
        self.version = version
        self.entries: List[KnowledgeEntry] = entries or []
        self.aliases: Dict[str, str] = aliases or {}

    # ------------------------------------------------------------------
    # Serialisation
    # ------------------------------------------------------------------

    def to_dict(self) -> dict:
        return {
            "name": self.name,
            "version": self.version,
            "domain": self.domain,
            "entries": [e.to_dict() for e in self.entries],
            "aliases": self.aliases,
        }

    def save(self, path: str | Path) -> None:
        """Persist the knowledge pack to *path* as JSON."""
        path = Path(path)
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("w", encoding="utf-8") as fh:
            json.dump(self.to_dict(), fh, indent=2, ensure_ascii=False)

    @classmethod
    def load(cls, path: str | Path) -> "KnowledgePack":
        """Load a knowledge pack from a JSON file."""
        path = Path(path)
        with path.open("r", encoding="utf-8") as fh:
            data = json.load(fh)
        return cls.from_dict(data)

    @classmethod
    def from_dict(cls, data: dict) -> "KnowledgePack":
        entries = [
            KnowledgeEntry(
                entry_id=e["id"],
                tags=e.get("tags", []),
                text=e["text"],
            )
            for e in data.get("entries", [])
        ]
        return cls(
            name=data["name"],
            domain=data.get("domain", ""),
            version=data.get("version", "1.0"),
            entries=entries,
            aliases=data.get("aliases", {}),
        )

    # ------------------------------------------------------------------
    # Querying
    # ------------------------------------------------------------------

    def query(self, tags: List[str]) -> List[KnowledgeEntry]:
        """Return all entries whose tag set overlaps with *tags*."""
        return [e for e in self.entries if e.matches_tags(tags)]

    def get_by_id(self, entry_id: str) -> Optional[KnowledgeEntry]:
        """Return the entry with the given *entry_id*, or ``None``."""
        for e in self.entries:
            if e.id == entry_id:
                return e
        return None

    def add_entry(self, entry: KnowledgeEntry) -> None:
        """Append a new entry to the pack."""
        self.entries.append(entry)

    def __len__(self) -> int:
        return len(self.entries)

    def __repr__(self) -> str:  # pragma: no cover
        return (
            f"KnowledgePack(name={self.name!r}, domain={self.domain!r}, "
            f"entries={len(self.entries)})"
        )
