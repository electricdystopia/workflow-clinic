"""
Rules that check for missing or incomplete I/O declarations.
IO-001: process has no output block, or the output block is empty.
"""

from __future__ import annotations

from workflow_clinic.critic.rules.base import BaseRule
from workflow_clinic.parsers.nextflow import NextflowProcess
from workflow_clinic.schema.gap_report import (
    Gap, GapCategory, CodeLocation, Severity,
)


class UndeclaredOutputRule(BaseRule):

    def check(self, process: NextflowProcess, file_path: str) -> Gap | None:
        if process.output.raw:
            return None

        return Gap(
            gap_id="IO-001",
            process_name=process.name,
            category=GapCategory.IO_DECLARATION,
            severity=Severity.MAJOR,
            location=CodeLocation(
                file=file_path,
                line_start=process.line_start,
                line_end=process.line_end,
            ),
            description=(
                f"Process '{process.name}' has no output declaration. "
                "Workflow engines cannot chain this process to downstream "
                "steps or track its results without explicit outputs."
            ),
            evidence="",
            recommendation=(
                "Add an output: block declaring all files this process "
                "produces, e.g.:\n"
                '    output:\n        path "*.bam"'
            ),
            auto_fixable=False,
        )