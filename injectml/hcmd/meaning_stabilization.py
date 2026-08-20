"""
Meaning Stabilization – resolves variant and ambiguous terms to their
canonical form using the alias table embedded in a KnowledgePack.

Example::

    from injectml import KnowledgePack
    from injectml.hcmd import MeaningStabilizer

    pack = KnowledgePack.load("wine_pairing.json")
    stabilizer = MeaningStabilizer(pack)

    canonical = stabilizer.stabilize("Chardonnay")
    # -> "chardonnay" (lowercased canonical form)

    tokens = stabilizer.stabilize_tokens(["Chard", "with", "salmon"])
    # -> ["chardonnay", "with", "salmon"]
"""

from __future__ import annotations

import re
from typing import Dict, List, Optional

from ..knowledge_pack import KnowledgePack


class MeaningStabilizer:
    """Resolves term variants to their canonical forms.

    Term resolution follows these steps (in order):

    1. Exact match against the alias table (case-insensitive).
    2. If no alias is found, return the original term unchanged.

    Parameters
    ----------
    pack:
        Knowledge pack whose ``aliases`` dict is used for resolution.
    extra_aliases:
        Additional alias mappings that extend (and may override) the pack's
        built-in aliases.
    """

    def __init__(
        self,
        pack: KnowledgePack,
        extra_aliases: Optional[Dict[str, str]] = None,
    ) -> None:
        self.pack = pack
        self._aliases: Dict[str, str] = {
            k.lower(): v for k, v in pack.aliases.items()
        }
        if extra_aliases:
            self._aliases.update({k.lower(): v for k, v in extra_aliases.items()})

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------

    def stabilize(self, term: str) -> str:
        """Return the canonical form of *term*.

        Parameters
        ----------
        term:
            A potentially ambiguous or variant term.

        Returns
        -------
        str
            The canonical form, or *term* itself if no alias is found.
        """
        return self._aliases.get(term.lower(), term)

    def stabilize_tokens(self, tokens: List[str]) -> List[str]:
        """Apply :meth:`stabilize` to each token in *tokens*.

        Parameters
        ----------
        tokens:
            List of word/token strings.

        Returns
        -------
        List[str]
            New list with each token replaced by its canonical form.
        """
        return [self.stabilize(t) for t in tokens]

    def stabilize_text(self, text: str) -> str:
        """Replace all known variant terms in *text* with their canonical
        forms, preserving surrounding punctuation.

        Parameters
        ----------
        text:
            Free-text string (e.g. a user query).

        Returns
        -------
        str
            Text with variant terms replaced by canonical forms.
        """
        for variant, canonical in self._aliases.items():
            pattern = re.compile(re.escape(variant), re.IGNORECASE)
            text = pattern.sub(canonical, text)
        return text

    def add_alias(self, variant: str, canonical: str) -> None:
        """Register a new alias at runtime."""
        self._aliases[variant.lower()] = canonical

    def known_aliases(self) -> Dict[str, str]:
        """Return a copy of the current alias table."""
        return dict(self._aliases)
