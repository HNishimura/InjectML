"""
InjectML – Knowledge injection for offline LLMs without training.
"""

from .knowledge_pack import KnowledgePack
from .injector import Injector

__all__ = ["KnowledgePack", "Injector"]
__version__ = "0.1.0"
