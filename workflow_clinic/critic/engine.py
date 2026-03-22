"""
CriticEngine — runs all registered rules against a ParsedWorkflow
and returns a GapReport.
"""

from __future__ import annotations

from datetime import datetime, timezone

from workflow_clinic.critic.rules.base import BaseRule
from workflow_clinic.critic.rules.containerization import (
    ContainerLatestTagRule,
    ContainerMissingRule,
)
from workflow_clinic.critic.rules.io_declaration import UndeclaredOutputRule
from workflow_clinic.critic.rules.storage import HardcodedPathRule
from workflow_clinic.parsers.nextflow import ParsedWorkflow
from workflow_clinic.schema.gap_report import (
    Gap, GapReport, GapSummary, Severity,
)

# Registry of all active rules — add new ones here as you build them
_RULES: list[BaseRule] = [
    ContainerMissingRule(),
    ContainerLatestTagRule(),
    HardcodedPathRule(),
    UndeclaredOutputRule(),
]

# Severity weights used to compute the cloud readiness score.
# A workflow with only INFO gaps scores close to 1.0.
# A workflow with CRITICAL gaps is penalised heavily.
_SEVERITY_PENALTY: dict[Severity, float] = {
    Severity.CRITICAL: 0.25,
    Severity.MAJOR:    0.10,
    Severity.MINOR:    0.03,
    Severity.INFO:     0.01,
}


def _compute_score(gaps: list[Gap]) -> float:
    penalty = sum(_SEVERITY_PENALTY.get(g.severity, 0.0) for g in gaps)
    return round(max(0.0, 1.0 - penalty), 2)


class CriticEngine:

    def __init__(self, rules: list[BaseRule] | None = None) -> None:
        # Allow injecting a custom rule list in tests
        self._rules = rules if rules is not None else _RULES

    def run(self, workflow: ParsedWorkflow) -> GapReport:
        file_path = str(workflow.path)
        gaps: list[Gap] = []

        for process in workflow.processes:
            for rule in self._rules:
                result = rule.check(process, file_path)
                if result is not None:
                    gaps.append(result)

        summary = GapSummary(
            total_gaps=len(gaps),
            critical=sum(1 for g in gaps if g.severity == Severity.CRITICAL),
            major=sum(1 for g in gaps if g.severity == Severity.MAJOR),
            minor=sum(1 for g in gaps if g.severity == Severity.MINOR),
            info=sum(1 for g in gaps if g.severity == Severity.INFO),
            auto_fixable_count=sum(1 for g in gaps if g.auto_fixable),
            cloud_readiness_score=_compute_score(gaps),
        )

        return GapReport(
            generated_at=datetime.now(timezone.utc),
            workflow_path=file_path,
            gaps=gaps,
            summary=summary,
        )