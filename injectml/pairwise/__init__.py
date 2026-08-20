"""
PairWise – Wine–Dish pairing engine and demo knowledge pack.

Usage::

    from injectml.pairwise import PairWiseEngine

    engine = PairWiseEngine()
    result = engine.pair("salmon")
    print(result.wines)        # -> ["Chardonnay", "Pinot Gris", ...]
    print(result.explanation)  # -> human-readable rationale
"""

from .engine import PairWiseEngine, PairingResult
from .wine_dish_pack import build_wine_dish_pack

__all__ = ["PairWiseEngine", "PairingResult", "build_wine_dish_pack"]
