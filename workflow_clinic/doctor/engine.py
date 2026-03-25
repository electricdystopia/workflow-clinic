"""
DoctorEngine — runs all registered fix generators against a GapReport
and returns a list of FixProposals.
"""

from __future__ import annotations

from workflow_clinic.doctor.fix_generators.base import BaseFixGenerator, FixProposal
from workflow_clinic.doctor.fix_generators.nextflow_fixes import ContainerMissingFixer
from workflow_clinic.schema.gap_report import Gap, GapReport

_GENERATORS: list[BaseFixGenerator] = [
    ContainerMissingFixer(),
]


class DoctorEngine:

    def __init__(self, generators: list[BaseFixGenerator] | None = None) -> None:
        self._generators = generators if generators is not None else _GENERATORS

    def run(self, report: GapReport, source_lines: list[str]) -> list[FixProposal]:
        proposals: list[FixProposal] = []
        for gap in report.gaps:
            if not gap.auto_fixable:
                continue
            for generator in self._generators:
                if generator.can_fix(gap):
                    result = generator.fix(gap, source_lines)
                    if result is not None:
                        proposals.append(result)
                    break
        return proposals