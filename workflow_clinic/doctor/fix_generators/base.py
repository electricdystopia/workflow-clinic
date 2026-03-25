"""
Abstract base class for all fix generators.
Mirrors the BaseRule pattern from the Critic — one Gap in, one
optional FixProposal out. None means the generator can't handle this gap.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass

from workflow_clinic.schema.gap_report import Gap


@dataclass
class FixProposal:
    gap_id:                str
    process_name:          str
    description:           str    # one-line human summary of what was changed
    unified_diff:          str    # ready to print or apply with `patch`
    validation_passed:     bool
    validation_output:     str
    confidence:            float  # 0.0–1.0
    human_review_required: bool


class BaseFixGenerator(ABC):

    @abstractmethod
    def can_fix(self, gap: Gap) -> bool:
        """Return True if this generator handles this gap_id."""
        ...

    @abstractmethod
    def fix(self, gap: Gap, source_lines: list[str]) -> FixProposal | None:
        """
        Attempt to generate a fix for the gap.
        source_lines is the full file split into lines.
        Returns None if the fix attempt fails completely.
        """
        ...