"""
Rules that check for hardcoded local storage paths.
STORAGE-001: script block contains a hardcoded absolute path.
"""

from __future__ import annotations

import re

from workflow_clinic.critic.rules.base import BaseRule
from workflow_clinic.parsers.nextflow import NextflowProcess
from workflow_clinic.schema.gap_report import (
    Gap, GapCategory, CodeLocation, Severity,
)

# Matches absolute paths like /data/ref/hg38.fa or /scratch/tmp/
# Ignores shell special vars like ${task.cpus} or $PWD
_RE_HARDCODED_PATH = re.compile(r'(?<!\$\{)["\']?(/[\w/.\-]+)')


class HardcodedPathRule(BaseRule):

    def check(self, process: NextflowProcess, file_path: str) -> Gap | None:
        script = process.script.raw
        if not script:
            return None

        matches = _RE_HARDCODED_PATH.findall(script)
        if not matches:
            return None

        # Show up to 3 offending paths in the evidence field
        evidence = ", ".join(matches[:3])
        if len(matches) > 3:
            evidence += f" ... ({len(matches) - 3} more)"

        return Gap(
            gap_id="STORAGE-001",
            process_name=process.name,
            category=GapCategory.STORAGE,
            severity=Severity.MAJOR,
            location=CodeLocation(
                file=file_path,
                line_start=process.line_start,
                line_end=process.line_end,
            ),
            description=(
                f"Process '{process.name}' contains hardcoded absolute paths "
                "in its script block. These paths will not exist on cloud "
                "execution environments."
            ),
            evidence=evidence,
            recommendation=(
                "Replace hardcoded paths with Nextflow input parameters. "
                "Reference files should be declared in the input: block and "
                "passed in via a params file or the workflow's input channel."
            ),
            auto_fixable=False,
        )