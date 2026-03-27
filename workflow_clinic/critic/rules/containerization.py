"""
Rules that check for containerization gaps.

CONTAINER-001: process has no container directive and no conda environment.
               (Day 8: skipped when conda is present — CONTAINER-003 handles that case.)
CONTAINER-002: container image uses :latest tag or has no tag.
CONTAINER-003: process uses conda without a singularity/container wrapper.
               (Snakemake-specific; fires for any language that populates process.conda.)
"""

from __future__ import annotations

import re

from workflow_clinic.critic.rules.base import BaseRule
from workflow_clinic.parsers.nextflow import NextflowProcess
from workflow_clinic.schema.gap_report import (
    Gap, GapCategory, CodeLocation, Severity,
)

_RE_HAS_TAG = re.compile(r".+:.+")   # image:tag — at least one char each side


class ContainerMissingRule(BaseRule):
    """
    CONTAINER-001 — no container directive and no conda environment.

    Day 8 change: the rule now returns None when ``process.conda`` is set.
    In that case, CONTAINER-003 reports the more specific "conda without
    singularity isolation" gap instead.  For all existing Nextflow tests
    ``process.conda`` is always None, so their behaviour is unchanged.
    """

    def check(self, process: NextflowProcess, file_path: str) -> Gap | None:
        if process.container is not None:
            return None
        # Defer to CONTAINER-003 when a conda environment is declared —
        # avoids double-reporting and gives each gap a single, actionable ID.
        if process.conda is not None:
            return None

        return Gap(
            gap_id="CONTAINER-001",
            process_name=process.name,
            category=GapCategory.CONTAINERIZATION,
            severity=Severity.CRITICAL,
            location=CodeLocation(
                file=file_path,
                line_start=process.line_start,
                line_end=process.line_end,
            ),
            description=(
                f"Process '{process.name}' has no container directive. "
                "It cannot run portably on any WES-compliant cloud platform."
            ),
            evidence="",
            recommendation=(
                "Add a container directive with a pinned image, e.g.:\n"
                "    container 'quay.io/biocontainers/tool:1.0.0'\n\n"
                "For Snakemake, use a singularity directive:\n"
                '    singularity: "docker://quay.io/biocontainers/tool:1.0.0"'
            ),
            auto_fixable=True,
        )


class ContainerLatestTagRule(BaseRule):
    """CONTAINER-002 — container image uses :latest tag or has no tag."""

    def check(self, process: NextflowProcess, file_path: str) -> Gap | None:
        if process.container is None:
            return None

        image = process.container
        has_valid_tag = (
            _RE_HAS_TAG.match(image) is not None
            and not image.endswith(":latest")
        )

        if has_valid_tag:
            return None

        tag = "latest" if image.endswith(":latest") else "missing"

        return Gap(
            gap_id="CONTAINER-002",
            process_name=process.name,
            category=GapCategory.REPRODUCIBILITY,
            severity=Severity.MAJOR,
            location=CodeLocation(
                file=file_path,
                line_start=process.line_start,
                line_end=process.line_end,
            ),
            description=(
                f"Process '{process.name}' uses a container image with a "
                f"{tag} tag ('{image}'). This is not reproducible — the same "
                "tag can point to a different image over time."
            ),
            evidence=f"container '{image}'",
            recommendation=(
                "Pin to a specific version tag or SHA digest, e.g.:\n"
                "    container 'quay.io/biocontainers/tool:1.0.0'\n"
                "    container 'quay.io/biocontainers/tool@sha256:abc123'"
            ),
            auto_fixable=False,
        )


class ContainerCondaIsolationRule(BaseRule):
    """
    CONTAINER-003 — conda environment present but no singularity wrapper.

    Introduced in Day 8 to support Snakemake workflows.

    Conda alone does not provide OS-level isolation:

    * Conda environments depend on the host OS's glibc, system libraries,
      and compilers — meaning the same ``environment.yaml`` can produce
      different results on different machines or cloud images.
    * Without a container, WES runners that mandate Docker / Singularity
      will refuse to execute the rule entirely.
    * Even a perfectly pinned conda-lock file cannot reproduce results if
      the host kernel ABI differs between runs.

    Best practice: wrap the conda environment in a ``singularity:`` directive
    pointing to a pinned Biocontainers image, or replace conda with a
    singularity image entirely.

    Fires when ``process.conda is not None`` AND ``process.container is None``.
    Does NOT fire when singularity is also present (that is the correct
    Snakemake pattern).
    """

    def check(self, process: NextflowProcess, file_path: str) -> Gap | None:
        if process.conda is None:
            return None
        if process.container is not None:
            # singularity + conda is the correct Snakemake pattern — no gap
            return None

        return Gap(
            gap_id="CONTAINER-003",
            process_name=process.name,
            category=GapCategory.REPRODUCIBILITY,
            severity=Severity.MAJOR,
            location=CodeLocation(
                file=file_path,
                line_start=process.line_start,
                line_end=process.line_end,
            ),
            description=(
                f"Rule '{process.name}' uses a conda environment "
                f"('{process.conda}') without a singularity container. "
                "Conda alone does not provide OS-level isolation and cannot "
                "run on WES platforms that require container images."
            ),
            evidence=f"conda: '{process.conda}'",
            recommendation=(
                "Add a singularity directive to wrap the conda environment:\n"
                "    singularity:\n"
                '        "docker://quay.io/biocontainers/tool:1.0.0"\n\n'
                "Or replace conda with a pinned Biocontainers image entirely:\n"
                "    singularity:\n"
                '        "docker://quay.io/biocontainers/tool:1.0.0"'
            ),
            auto_fixable=False,
        )