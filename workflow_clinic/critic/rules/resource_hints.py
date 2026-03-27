"""
Rules that check for missing resource declaration hints.

RESOURCE-001: process has no cpus directive.
RESOURCE-002: process has no memory directive.

Cloud schedulers (AWS Batch, Google Life Sciences, Azure Batch) rely on these
hints to provision the right instance type. Without them the platform falls
back to defaults that are either wastefully large (cost) or dangerously small
(OOM kills on big datasets). Both rules fire at MINOR severity — they are not
portability blockers in the strict sense, but they are a reproducibility and
cost-efficiency concern that affects cloud users immediately.

Design note — two rules instead of one
───────────────────────────────────────
We could merge these into a single "ResourceHintsMissingRule" that fires once
per process and lists whichever hints are absent. We keep them separate for the
same reason CONTAINER-001 and CONTAINER-002 are separate: the gap_id must map
1-to-1 to a remediation action. A fixer for "missing cpus" and a fixer for
"missing memory" are different operations; they need distinct identifiers.
"""

from __future__ import annotations

from workflow_clinic.critic.rules.base import BaseRule
from workflow_clinic.parsers.nextflow import NextflowProcess
from workflow_clinic.schema.gap_report import (
    Gap, GapCategory, CodeLocation, Severity,
)


class CpusMissingRule(BaseRule):
    """
    RESOURCE-001 — no cpus directive.

    Without an explicit cpu count the scheduler cannot place the job on an
    instance with sufficient cores, and the tool cannot parallelise itself
    via ${task.cpus}. This is a MINOR gap because the workflow will still run
    (on one core) but will be slow and potentially cost-inefficient.
    """

    def check(self, process: NextflowProcess, file_path: str) -> Gap | None:
        if process.cpus is not None:
            return None

        return Gap(
            gap_id="RESOURCE-001",
            process_name=process.name,
            category=GapCategory.RESOURCE_HINTS,
            severity=Severity.MINOR,
            location=CodeLocation(
                file=file_path,
                line_start=process.line_start,
                line_end=process.line_end,
            ),
            description=(
                f"Process '{process.name}' has no cpus directive. "
                "Cloud schedulers cannot allocate the correct number of CPU "
                "cores without an explicit declaration, leading to either "
                "over-provisioning (wasted cost) or under-provisioning "
                "(slow or failed runs). The tool cannot parallelise itself "
                "via ${task.cpus} without this value."
            ),
            evidence="",
            recommendation=(
                "Add a cpus directive appropriate for the tool's parallelism:\n"
                "    cpus 4\n\n"
                "Reference the allocation in the script block so the tool "
                "actually uses the provisioned cores:\n"
                "    bwa mem -t ${task.cpus} ...\n\n"
                "For workflows that need to scale, consider a dynamic "
                "expression:\n"
                "    cpus { reads.size() > 5.GB ? 8 : 4 }"
            ),
            auto_fixable=False,
        )


class MemoryMissingRule(BaseRule):
    """
    RESOURCE-002 — no memory directive.

    Without a memory hint the scheduler cannot reserve sufficient RAM. Many
    bioinformatics tools (GATK, STAR, BWA-MEM2) require several GB for their
    index structures; running them on an instance with inadequate RAM causes
    silent or confusing OOM kills on cloud WES platforms.
    """

    def check(self, process: NextflowProcess, file_path: str) -> Gap | None:
        if process.memory is not None:
            return None

        return Gap(
            gap_id="RESOURCE-002",
            process_name=process.name,
            category=GapCategory.RESOURCE_HINTS,
            severity=Severity.MINOR,
            location=CodeLocation(
                file=file_path,
                line_start=process.line_start,
                line_end=process.line_end,
            ),
            description=(
                f"Process '{process.name}' has no memory directive. "
                "Cloud schedulers cannot reserve sufficient RAM without an "
                "explicit declaration. Memory-hungry bioinformatics tools "
                "(aligners, variant callers) will be killed by OOM errors on "
                "instances with inadequate RAM, with no meaningful error message."
            ),
            evidence="",
            recommendation=(
                "Add a memory directive sized for the tool's peak usage:\n"
                "    memory '8 GB'\n\n"
                "For resilient pipelines, combine with an error strategy "
                "that increases memory on retry:\n"
                "    errorStrategy 'retry'\n"
                "    maxRetries 2\n"
                "    memory { (8.GB * task.attempt).clamp(null, 32.GB) }"
            ),
            auto_fixable=False,
        )