"""
Tests for the Doctor engine and fix generators.
LLM calls are mocked — tests run without any API key.
"""

from __future__ import annotations

from pathlib import Path
from unittest.mock import patch

from workflow_clinic.critic.engine import CriticEngine
from workflow_clinic.doctor.engine import DoctorEngine
from workflow_clinic.doctor.fix_generators.base import FixProposal
from workflow_clinic.parsers.nextflow import NextflowParser
from workflow_clinic.schema.gap_report import Gap, GapCategory, CodeLocation, Severity
from workflow_clinic.doctor.fix_generators.nextflow_fixes import (
    ContainerMissingFixer,
    ContainerLatestTagFixer,
)

FIXTURES = Path(__file__).parent / "fixtures" / "nextflow"
parser   = NextflowParser()
critic   = CriticEngine()


# ── Helpers ───────────────────────────────────────────────────────────────────

def _make_container_gap(process_name: str = "ALIGN") -> Gap:
    return Gap(
        gap_id="CONTAINER-001",
        process_name=process_name,
        category=GapCategory.CONTAINERIZATION,
        severity=Severity.CRITICAL,
        location=CodeLocation(
            file="tests/fixtures/nextflow/broken.nf",
            line_start=1,
            line_end=11,
        ),
        description="Missing container.",
        evidence="",
        recommendation="Add container directive.",
        auto_fixable=True,
    )


def _source_lines() -> list[str]:
    return (FIXTURES / "broken.nf").read_text().splitlines(keepends=True)


# ── ContainerMissingFixer ─────────────────────────────────────────────────────

@patch("workflow_clinic.doctor.fix_generators.nextflow_fixes.LLMClient")
def test_container_fixer_returns_proposal(mock_llm_cls):
    mock_llm_cls.return_value.complete.return_value = (
        "quay.io/biocontainers/bwa:0.7.17--h5bf99c6_8"
    )
    fixer    = ContainerMissingFixer()
    proposal = fixer.fix(_make_container_gap(), _source_lines())

    assert isinstance(proposal, FixProposal)


@patch("workflow_clinic.doctor.fix_generators.nextflow_fixes.LLMClient")
def test_container_fixer_diff_is_non_empty(mock_llm_cls):
    mock_llm_cls.return_value.complete.return_value = (
        "quay.io/biocontainers/bwa:0.7.17--h5bf99c6_8"
    )
    fixer    = ContainerMissingFixer()
    proposal = fixer.fix(_make_container_gap(), _source_lines())

    assert proposal.unified_diff != ""
    assert "container" in proposal.unified_diff


@patch("workflow_clinic.doctor.fix_generators.nextflow_fixes.LLMClient")
def test_container_fixer_validation_passes(mock_llm_cls):
    mock_llm_cls.return_value.complete.return_value = (
        "quay.io/biocontainers/bwa:0.7.17--h5bf99c6_8"
    )
    fixer    = ContainerMissingFixer()
    proposal = fixer.fix(_make_container_gap(), _source_lines())

    assert proposal.validation_passed is True
    assert proposal.confidence == 0.85
    assert proposal.human_review_required is False


@patch("workflow_clinic.doctor.fix_generators.nextflow_fixes.LLMClient")
def test_container_fixer_strips_prose_from_llm_response(mock_llm_cls):
    # Simulate a small model that adds prose around the image name
    mock_llm_cls.return_value.complete.return_value = (
        "I recommend using quay.io/biocontainers/bwa:0.7.17--h5bf99c6_8 for this."
    )
    fixer    = ContainerMissingFixer()
    proposal = fixer.fix(_make_container_gap(), _source_lines())

    # The diff should contain the clean image name, not the prose
    assert "quay.io/biocontainers/bwa:0.7.17--h5bf99c6_8" in proposal.unified_diff
    assert "I recommend" not in proposal.unified_diff


@patch("workflow_clinic.doctor.fix_generators.nextflow_fixes.LLMClient")
def test_container_fixer_llm_failure_returns_failed_proposal(mock_llm_cls):
    mock_llm_cls.return_value.complete.side_effect = RuntimeError("timeout")
    fixer    = ContainerMissingFixer()
    proposal = fixer.fix(_make_container_gap(), _source_lines())

    assert proposal.validation_passed is False
    assert proposal.confidence == 0.0
    assert proposal.human_review_required is True


@patch("workflow_clinic.doctor.fix_generators.nextflow_fixes.LLMClient")
def test_container_fixer_unknown_process_returns_failed_proposal(mock_llm_cls):
    mock_llm_cls.return_value.complete.return_value = (
        "quay.io/biocontainers/bwa:0.7.17--h5bf99c6_8"
    )
    fixer = ContainerMissingFixer()
    gap   = _make_container_gap(process_name="NONEXISTENT_PROCESS")
    proposal = fixer.fix(gap, _source_lines())

    assert proposal.validation_passed is False


# ── DoctorEngine ──────────────────────────────────────────────────────────────

@patch("workflow_clinic.doctor.fix_generators.nextflow_fixes.LLMClient")
def test_doctor_engine_skips_non_auto_fixable(mock_llm_cls):
    mock_llm_cls.return_value.complete.return_value = (
        "quay.io/biocontainers/bwa:0.7.17--h5bf99c6_8"
    )
    wf       = parser.parse_file(FIXTURES / "broken.nf")
    report   = critic.run(wf)
    lines    = (FIXTURES / "broken.nf").read_text().splitlines(keepends=True)
    proposals = DoctorEngine().run(report, lines)

    # Only CONTAINER-001 gaps are auto_fixable — STORAGE-001 and IO-001 are not
    for p in proposals:
        assert p.gap_id == "CONTAINER-001"


@patch("workflow_clinic.doctor.fix_generators.nextflow_fixes.LLMClient")
def test_doctor_engine_produces_one_proposal_per_auto_fixable_gap(mock_llm_cls):
    mock_llm_cls.return_value.complete.return_value = (
        "quay.io/biocontainers/bwa:0.7.17--h5bf99c6_8"
    )
    wf       = parser.parse_file(FIXTURES / "broken.nf")
    report   = critic.run(wf)
    lines    = (FIXTURES / "broken.nf").read_text().splitlines(keepends=True)

    auto_fixable_count = sum(1 for g in report.gaps if g.auto_fixable)
    proposals          = DoctorEngine().run(report, lines)

    assert len(proposals) == auto_fixable_count

# ── ContainerLatestTagFixer ───────────────────────────────────────────────────

def _make_latest_tag_gap() -> Gap:
    return Gap(
        gap_id="CONTAINER-002",
        process_name="TRIM",
        category=GapCategory.REPRODUCIBILITY,
        severity=Severity.MAJOR,
        location=CodeLocation(
            file="tests/fixtures/nextflow/partial.nf",
            line_start=1,
            line_end=16,
        ),
        description="Uses :latest tag.",
        evidence="container 'quay.io/biocontainers/trimmomatic:latest'",
        recommendation="Pin to a specific version.",
        auto_fixable=False,   # not auto_fixable yet — fixer still works directly
    )


def _partial_source_lines() -> list[str]:
    return (FIXTURES / "partial.nf").read_text().splitlines(keepends=True)


@patch("workflow_clinic.doctor.fix_generators.nextflow_fixes.LLMClient")
def test_latest_tag_fixer_returns_proposal(mock_llm_cls):
    mock_llm_cls.return_value.complete.return_value = (
        "quay.io/biocontainers/trimmomatic:0.39--hdfd78af_2"
    )
    fixer    = ContainerLatestTagFixer()
    proposal = fixer.fix(_make_latest_tag_gap(), _partial_source_lines())
    assert isinstance(proposal, FixProposal)


@patch("workflow_clinic.doctor.fix_generators.nextflow_fixes.LLMClient")
def test_latest_tag_fixer_diff_replaces_latest(mock_llm_cls):
    mock_llm_cls.return_value.complete.return_value = (
        "quay.io/biocontainers/trimmomatic:0.39--hdfd78af_2"
    )
    fixer    = ContainerLatestTagFixer()
    proposal = fixer.fix(_make_latest_tag_gap(), _partial_source_lines())

    assert ":latest" not in proposal.unified_diff or "-" in proposal.unified_diff
    assert "0.39" in proposal.unified_diff


@patch("workflow_clinic.doctor.fix_generators.nextflow_fixes.LLMClient")
def test_latest_tag_fixer_validation_passes(mock_llm_cls):
    mock_llm_cls.return_value.complete.return_value = (
        "quay.io/biocontainers/trimmomatic:0.39--hdfd78af_2"
    )
    fixer    = ContainerLatestTagFixer()
    proposal = fixer.fix(_make_latest_tag_gap(), _partial_source_lines())
    assert proposal.validation_passed is True


@patch("workflow_clinic.doctor.fix_generators.nextflow_fixes.LLMClient")
def test_latest_tag_fixer_llm_failure_returns_failed_proposal(mock_llm_cls):
    mock_llm_cls.return_value.complete.side_effect = RuntimeError("timeout")
    fixer    = ContainerLatestTagFixer()
    proposal = fixer.fix(_make_latest_tag_gap(), _partial_source_lines())
    assert proposal.validation_passed is False
    assert proposal.confidence == 0.0


# ── _clean_image_response ─────────────────────────────────────────────────────

def test_clean_image_response_handles_clean_input():
    fixer = ContainerMissingFixer()
    assert fixer._clean_image_response(
        "quay.io/biocontainers/bwa:0.7.17--h5bf99c6_8"
    ) == "quay.io/biocontainers/bwa:0.7.17--h5bf99c6_8"


def test_clean_image_response_strips_leading_prose():
    fixer = ContainerMissingFixer()
    result = fixer._clean_image_response(
        "I recommend using quay.io/biocontainers/bwa:0.7.17--h5bf99c6_8 for this."
    )
    assert result == "quay.io/biocontainers/bwa:0.7.17--h5bf99c6_8"


def test_clean_image_response_takes_first_line_only():
    fixer = ContainerMissingFixer()
    result = fixer._clean_image_response(
        "quay.io/biocontainers/bwa:0.7.17--h5bf99c6_8\nsome extra prose"
    )
    assert "extra prose" not in result