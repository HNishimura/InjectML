"""
PairWiseEngine – offline wine–dish pairing using InjectML.

The engine uses the built-in wine–dish knowledge pack together with the HCMD
extensions (MeaningStabilizer + DomainNarrower) to match dish ingredients /
keywords to appropriate wine recommendations **without** calling an external
LLM.  An optional ``build_prompt`` method constructs a ready-to-use prompt
string for LLMs that need richer natural-language output.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from typing import List, Optional

from ..knowledge_pack import KnowledgePack, KnowledgeEntry
from ..hcmd.meaning_stabilization import MeaningStabilizer
from ..hcmd.domain_narrowing import DomainNarrower
from ..injector import Injector
from .wine_dish_pack import build_wine_dish_pack


@dataclass
class PairingResult:
    """Result returned by :meth:`PairWiseEngine.pair`.

    Attributes
    ----------
    dish:
        The input dish or ingredient string.
    query_tokens:
        Stabilized tokens extracted from *dish*.
    matched_entries:
        Knowledge entries selected by DomainNarrower.
    wines:
        Deduplicated list of wine names inferred from matched entries.
    explanation:
        Human-readable summary of the pairing rationale.
    prompt:
        LLM-ready prompt string (only set when ``build_prompt=True``).
    """

    dish: str
    query_tokens: List[str] = field(default_factory=list)
    matched_entries: List[KnowledgeEntry] = field(default_factory=list)
    wines: List[str] = field(default_factory=list)
    explanation: str = ""
    prompt: Optional[str] = None


# Tags that represent wine variety names (used to extract wine names from tag lists).
_WINE_TAGS = {
    "chardonnay", "sauvignon_blanc", "pinot_gris", "pinot_grigio", "riesling",
    "viognier", "cabernet_sauvignon", "pinot_noir", "merlot", "shiraz", "syrah",
    "zinfandel", "malbec", "champagne", "prosecco", "cava", "rose", "rosé",
    "sauternes", "port",
}

# Tags that should be excluded from token extraction (stop-tag set).
_STOP_TAGS = {"principle", "white_wine", "red_wine", "sparkling", "dessert_wine"}


def _tag_to_label(tag: str) -> str:
    """Convert a snake_case tag to a human-readable wine label."""
    return tag.replace("_", " ").title()


class PairWiseEngine:
    """Offline wine–dish pairing engine.

    Parameters
    ----------
    pack:
        Custom :class:`~injectml.knowledge_pack.KnowledgePack`.  Defaults to
        the built-in wine–dish pack.
    threshold:
        DomainNarrower relevance threshold (0.0–1.0).
    max_results:
        Maximum number of knowledge entries to include in a pairing.
    """

    def __init__(
        self,
        pack: Optional[KnowledgePack] = None,
        threshold: float = 0.0,
        max_results: int = 5,
    ) -> None:
        self.pack = pack if pack is not None else build_wine_dish_pack()
        self.stabilizer = MeaningStabilizer(self.pack)
        self.narrower = DomainNarrower(self.pack, threshold=threshold, max_results=max_results)
        self._injector = Injector(self.pack, max_entries=max_results)

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------

    def pair(self, dish: str, build_prompt: bool = False) -> PairingResult:
        """Return wine pairing recommendations for *dish*.

        Parameters
        ----------
        dish:
            Dish name or comma-separated ingredient list
            (e.g. ``"grilled salmon"`` or ``"steak, mushroom sauce"``).
        build_prompt:
            If ``True``, populate ``PairingResult.prompt`` with an LLM-ready
            prompt string using :class:`~injectml.injector.Injector`.

        Returns
        -------
        PairingResult
        """
        tokens = self._tokenize(dish)
        stable_tokens = self.stabilizer.stabilize_tokens(tokens)
        entries = self.narrower.narrow(stable_tokens)

        wines = self._extract_wines(entries)
        explanation = self._build_explanation(dish, entries, wines)

        prompt: Optional[str] = None
        if build_prompt:
            tag_set = list({t for e in entries for t in e.tags} | set(stable_tokens))
            prompt = self._injector.build_prompt(
                user_query=f"Which wines pair best with {dish}?",
                tags=tag_set,
            )

        return PairingResult(
            dish=dish,
            query_tokens=stable_tokens,
            matched_entries=entries,
            wines=wines,
            explanation=explanation,
            prompt=prompt,
        )

    # ------------------------------------------------------------------
    # Internal helpers
    # ------------------------------------------------------------------

    @staticmethod
    def _tokenize(text: str) -> List[str]:
        """Split *text* into lowercase alpha-numeric tokens."""
        return [t for t in re.split(r"[\s,;/]+", text.lower()) if t]

    @staticmethod
    def _extract_wines(entries: List[KnowledgeEntry]) -> List[str]:
        """Deduplicate and label wine names found in entry tags."""
        seen: dict[str, None] = {}
        for entry in entries:
            for tag in entry.tags:
                if tag in _WINE_TAGS and tag not in seen:
                    seen[tag] = None
        return [_tag_to_label(w) for w in seen]

    @staticmethod
    def _build_explanation(dish: str, entries: List[KnowledgeEntry], wines: List[str]) -> str:
        if not entries:
            return f"No specific pairings found for '{dish}'."
        wine_list = ", ".join(wines) if wines else "the wines listed above"
        rationale_lines = [e.text for e in entries if "principle" not in e.tags]
        principles = [e.text for e in entries if "principle" in e.tags]
        parts = [f"Recommended wines for '{dish}': {wine_list}."]
        if rationale_lines:
            parts.append("\nPairing rationale:")
            for line in rationale_lines:
                parts.append(f"  • {line}")
        if principles:
            parts.append("\nGeneral principles:")
            for line in principles:
                parts.append(f"  • {line}")
        return "\n".join(parts)
