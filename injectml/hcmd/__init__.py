"""
HCMD – Hierarchical Context Management and Disambiguation extensions.

Sub-modules
-----------
meaning_stabilization
    Resolves ambiguous or variant terms to their canonical form before
    knowledge retrieval.
domain_narrowing
    Filters knowledge entries to the most specific sub-domain relevant to
    the query.
"""

from .meaning_stabilization import MeaningStabilizer
from .domain_narrowing import DomainNarrower

__all__ = ["MeaningStabilizer", "DomainNarrower"]
