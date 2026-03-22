"""
Abstract base class for all critic rules.
Every rule takes a single NextflowProcess and either returns
a Gap if the rule fires, or None if the process is clean.
"""

from __future__ import annotations

from abc import ABC, abstractmethod

from workflow_clinic.parsers.nextflow import NextflowProcess
from workflow_clinic.schema.gap_report import Gap


class BaseRule(ABC):

    @abstractmethod
    def check(self, process: NextflowProcess, file_path: str) -> Gap | None:
        """
        Run the rule against a single process.
        Return a Gap if the rule fires, None if the process passes.
        """
        ...