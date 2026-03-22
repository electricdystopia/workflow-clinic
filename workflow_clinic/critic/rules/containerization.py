"""
Rules that check for containerization gaps.
CONTAINER-001: process has no container directive at all.
CONTAINER-002: container image uses :latest tag or has no tag.
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

    def check(self, process: NextflowProcess, file_path: str) -> Gap | None:
        if process.container is not None:
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
                "    container 'quay.io/biocontainers/tool:1.0.0'"
            ),
            auto_fixable=True,
        )


class ContainerLatestTagRule(BaseRule):

    def check(self, process: NextflowProcess, file_path: str) -> Gap | None:
        if process.container is None:
            # ContainerMissingRule already handles this — don't double-report
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