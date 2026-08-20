"""
Domain Narrowing – restricts knowledge retrieval to the sub-domain most
relevant to a given query.

Relevance is computed as the fraction of query tokens that appear in an
entry's tag set.  Entries below the relevance threshold are excluded.

Example::

    from injectml import KnowledgePack
    from injectml.hcmd import DomainNarrower

    pack = KnowledgePack.load("wine_pairing.json")
    narrower = DomainNarrower(pack, threshold=0.3)

    relevant = narrower.narrow(["salmon", "grilled", "white"])
    # Returns KnowledgeEntry objects whose tags overlap with query tokens.
"""

from __future__ import annotations

from typing import List, Optional

from ..knowledge_pack import KnowledgePack, KnowledgeEntry


class DomainNarrower:
    """Filters knowledge entries to those most relevant to a query.

    Parameters
    ----------
    pack:
        The knowledge pack to narrow.
    threshold:
        Minimum relevance score (0.0–1.0) for an entry to be included.
        A score of 0.0 (default) means every entry with *any* tag overlap
        is returned.
    max_results:
        Maximum number of entries to return, ranked by relevance.
        ``None`` means no limit.
    """

    def __init__(
        self,
        pack: KnowledgePack,
        threshold: float = 0.0,
        max_results: Optional[int] = None,
    ) -> None:
        if not (0.0 <= threshold <= 1.0):
            raise ValueError("threshold must be between 0.0 and 1.0")
        self.pack = pack
        self.threshold = threshold
        self.max_results = max_results

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------

    def narrow(self, query_tokens: List[str]) -> List[KnowledgeEntry]:
        """Return entries relevant to *query_tokens*, sorted by relevance.

        Parameters
        ----------
        query_tokens:
            List of terms extracted from the user query (after optional
            :class:`~injectml.hcmd.MeaningStabilizer` pre-processing).

        Returns
        -------
        List[KnowledgeEntry]
            Entries sorted in descending order of relevance score.
        """
        if not query_tokens:
            return []
        query_set = {t.lower() for t in query_tokens}
        scored: List[tuple[float, KnowledgeEntry]] = []
        for entry in self.pack.entries:
            score = self._score(query_set, entry)
            if score > 0 and score >= self.threshold:
                scored.append((score, entry))

        scored.sort(key=lambda x: x[0], reverse=True)
        results = [entry for _, entry in scored]
        if self.max_results is not None:
            results = results[: self.max_results]
        return results

    def relevance_scores(self, query_tokens: List[str]) -> List[tuple[float, KnowledgeEntry]]:
        """Return ``(score, entry)`` pairs for *all* entries, sorted by score.

        Useful for debugging which entries are considered relevant.
        """
        query_set = {t.lower() for t in query_tokens}
        scored = [(self._score(query_set, e), e) for e in self.pack.entries]
        scored.sort(key=lambda x: x[0], reverse=True)
        return scored

    # ------------------------------------------------------------------
    # Internal helpers
    # ------------------------------------------------------------------

    @staticmethod
    def _score(query_set: set, entry: KnowledgeEntry) -> float:
        """Jaccard-like relevance: |query ∩ tags| / |query|."""
        if not query_set:
            return 0.0
        tag_set = {t.lower() for t in entry.tags}
        overlap = query_set & tag_set
        return len(overlap) / len(query_set)
