"""
Injector – injects knowledge from a KnowledgePack into an LLM prompt.

Usage::

    from injectml import KnowledgePack, Injector

    pack = KnowledgePack.load("wine_pairing.json")
    injector = Injector(pack)

    prompt = injector.build_prompt(
        user_query="Which wine goes with grilled salmon?",
        tags=["salmon", "white_wine"],
    )
    # `prompt` is a ready-to-use string you can pass to any LLM.
"""

from __future__ import annotations

from typing import List, Optional

from .knowledge_pack import KnowledgePack


_DEFAULT_SYSTEM_HEADER = (
    "You are an expert assistant. Use the following domain knowledge to answer "
    "the user's question accurately. Do not rely on information outside this "
    "knowledge pack.\n"
)


class Injector:
    """Builds LLM prompts with injected knowledge context.

    Parameters
    ----------
    pack:
        The :class:`~injectml.knowledge_pack.KnowledgePack` to draw knowledge
        from.
    system_header:
        Introductory text prepended to the injected knowledge block.  Defaults
        to :data:`_DEFAULT_SYSTEM_HEADER`.
    max_entries:
        Maximum number of knowledge entries to include.  ``None`` means no
        limit.
    """

    def __init__(
        self,
        pack: KnowledgePack,
        system_header: Optional[str] = None,
        max_entries: Optional[int] = None,
    ) -> None:
        self.pack = pack
        self.system_header = system_header if system_header is not None else _DEFAULT_SYSTEM_HEADER
        self.max_entries = max_entries

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------

    def build_prompt(
        self,
        user_query: str,
        tags: Optional[List[str]] = None,
        extra_context: str = "",
    ) -> str:
        """Construct a prompt string ready to send to an LLM.

        Parameters
        ----------
        user_query:
            The end-user's question or instruction.
        tags:
            Subset of knowledge tags to retrieve.  Pass ``None`` or ``[]`` to
            include *all* entries.
        extra_context:
            Additional free-text context to append before the user query.

        Returns
        -------
        str
            A formatted prompt string.
        """
        entries = self._select_entries(tags)
        knowledge_block = self._format_knowledge_block(entries)
        parts = [self.system_header.rstrip("\n")]
        if knowledge_block:
            parts.append("\n--- Knowledge Pack: {} ---\n{}".format(
                self.pack.name, knowledge_block
            ))
        if extra_context:
            parts.append("\n" + extra_context.strip())
        parts.append("\nUser: " + user_query.strip())
        return "\n".join(parts)

    def inject_into(self, messages: List[dict], tags: Optional[List[str]] = None) -> List[dict]:
        """Prepend a system message containing the knowledge context to a
        chat-style *messages* list (OpenAI / Ollama format).

        Parameters
        ----------
        messages:
            List of ``{"role": ..., "content": ...}`` dicts.
        tags:
            Knowledge tags to filter entries.

        Returns
        -------
        List[dict]
            New messages list with the system knowledge message prepended.
        """
        entries = self._select_entries(tags)
        knowledge_block = self._format_knowledge_block(entries)
        system_content = self.system_header.rstrip("\n")
        if knowledge_block:
            system_content += "\n\n--- Knowledge Pack: {} ---\n{}".format(
                self.pack.name, knowledge_block
            )
        system_msg = {"role": "system", "content": system_content}
        return [system_msg] + list(messages)

    # ------------------------------------------------------------------
    # Internal helpers
    # ------------------------------------------------------------------

    def _select_entries(self, tags: Optional[List[str]]):
        if tags:
            entries = self.pack.query(tags)
        else:
            entries = list(self.pack.entries)
        if self.max_entries is not None:
            entries = entries[: self.max_entries]
        return entries

    @staticmethod
    def _format_knowledge_block(entries) -> str:
        if not entries:
            return ""
        lines = []
        for i, entry in enumerate(entries, start=1):
            lines.append(f"{i}. [{', '.join(entry.tags)}] {entry.text}")
        return "\n".join(lines)
