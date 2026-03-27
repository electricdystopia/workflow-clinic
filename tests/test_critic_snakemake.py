"""
Integration tests: CriticEngine running against parsed Snakemake fixtures.

Validates that all existing rules fire correctly on Snakemake workflows and
that the new CONTAINER-003 rule behaves as expected.  Also includes smoke
tests for CLI auto-detection via the ParserRegistry.
"""

from __future__ import annotations

from pathlib import Path

import pytest
from typer.testing import CliRunner

from workflow_clinic.cli import app
from workflow_clinic.critic.engine import CriticEngine
from workflow_clinic.parsers.snakemake import SnakemakeParser
from workflow_clinic.schema.gap_report import Severity, GapCategory

FIXTURES = Path(__file__).parent / "fixtures" / "snakemake"
parser   = SnakemakeParser()
engine   = CriticEngine()
runner   = CliRunner()


# ── Helpers ───────────────────────────────────────────────────────────────────

def gap_ids(report):
    return [g.gap_id for g in report.gaps]

def gaps_for(report, process_name: str):
    return [g for g in report.gaps if g.process_name == process_name]


# ── Clean workflow — no gaps expected ────────────────────────────────────────

def test_clean_no_gaps():
    wf     = parser.parse_file(FIXTURES / "clean.smk")
    report = engine.run(wf)
    assert report.summary.total_gaps == 0

def test_clean_score_is_perfect():
    wf     = parser.parse_file(FIXTURES / "clean.smk")
    report = engine.run(wf)
    assert report.summary.cloud_readiness_score == 1.0

def test_clean_container_001_silent():
    """Pinned singularity → CONTAINER-001 must not fire."""
    wf     = parser.parse_file(FIXTURES / "clean.smk")
    report = engine.run(wf)
    assert "CONTAINER-001" not in gap_ids(report)

def test_clean_container_002_silent():
    """Pinned tags → CONTAINER-002 must not fire."""
    wf     = parser.parse_file(FIXTURES / "clean.smk")
    report = engine.run(wf)
    assert "CONTAINER-002" not in gap_ids(report)

def test_clean_container_003_silent():
    """No conda → CONTAINER-003 must not fire."""
    wf     = parser.parse_file(FIXTURES / "clean.smk")
    report = engine.run(wf)
    assert "CONTAINER-003" not in gap_ids(report)


# ── Broken workflow — all relevant gap types should fire ──────────────────────

def test_broken_container_001_fires():
    wf     = parser.parse_file(FIXTURES / "broken.smk")
    report = engine.run(wf)
    assert "CONTAINER-001" in gap_ids(report)

def test_broken_container_001_is_critical():
    wf     = parser.parse_file(FIXTURES / "broken.smk")
    report = engine.run(wf)
    c001   = [g for g in report.gaps if g.gap_id == "CONTAINER-001"]
    assert all(g.severity == Severity.CRITICAL for g in c001)

def test_broken_storage_001_fires():
    wf     = parser.parse_file(FIXTURES / "broken.smk")
    report = engine.run(wf)
    assert "STORAGE-001" in gap_ids(report)

def test_broken_storage_001_evidence_contains_path():
    wf     = parser.parse_file(FIXTURES / "broken.smk")
    report = engine.run(wf)
    s001   = [g for g in report.gaps if g.gap_id == "STORAGE-001"]
    assert any("hg38" in g.evidence or "scratch" in g.evidence for g in s001)

def test_broken_io_001_fires():
    wf     = parser.parse_file(FIXTURES / "broken.smk")
    report = engine.run(wf)
    assert "IO-001" in gap_ids(report)

def test_broken_call_variants_missing_output():
    wf     = parser.parse_file(FIXTURES / "broken.smk")
    report = engine.run(wf)
    cv_gaps = gaps_for(report, "CALL_VARIANTS")
    assert any(g.gap_id == "IO-001" for g in cv_gaps)

def test_broken_resource_001_fires():
    wf     = parser.parse_file(FIXTURES / "broken.smk")
    report = engine.run(wf)
    assert "RESOURCE-001" in gap_ids(report)

def test_broken_resource_002_fires():
    wf     = parser.parse_file(FIXTURES / "broken.smk")
    report = engine.run(wf)
    assert "RESOURCE-002" in gap_ids(report)

def test_broken_score_is_low():
    wf     = parser.parse_file(FIXTURES / "broken.smk")
    report = engine.run(wf)
    assert report.summary.cloud_readiness_score < 0.5

def test_broken_summary_counts_are_consistent():
    wf     = parser.parse_file(FIXTURES / "broken.smk")
    report = engine.run(wf)
    s = report.summary
    assert s.total_gaps == s.critical + s.major + s.minor + s.info

def test_broken_container_003_silent_on_broken():
    """broken.smk has no conda at all — CONTAINER-003 must not fire."""
    wf     = parser.parse_file(FIXTURES / "broken.smk")
    report = engine.run(wf)
    assert "CONTAINER-003" not in gap_ids(report)


# ── Partial workflow — CONTAINER-003 logic ────────────────────────────────────

def test_partial_container_003_fires_on_trim():
    """TRIM has conda but no singularity → CONTAINER-003 fires."""
    wf     = parser.parse_file(FIXTURES / "partial.smk")
    report = engine.run(wf)
    trim_gaps = gaps_for(report, "TRIM")
    assert any(g.gap_id == "CONTAINER-003" for g in trim_gaps)

def test_partial_container_003_is_major():
    wf     = parser.parse_file(FIXTURES / "partial.smk")
    report = engine.run(wf)
    c003   = [g for g in report.gaps if g.gap_id == "CONTAINER-003"]
    assert all(g.severity == Severity.MAJOR for g in c003)

def test_partial_container_003_category_is_reproducibility():
    wf     = parser.parse_file(FIXTURES / "partial.smk")
    report = engine.run(wf)
    c003   = [g for g in report.gaps if g.gap_id == "CONTAINER-003"]
    assert all(g.category == GapCategory.REPRODUCIBILITY for g in c003)

def test_partial_container_001_not_fires_on_trim():
    """TRIM has conda — CONTAINER-001 must be suppressed (CONTAINER-003 handles it)."""
    wf     = parser.parse_file(FIXTURES / "partial.smk")
    report = engine.run(wf)
    trim_gaps = gaps_for(report, "TRIM")
    assert not any(g.gap_id == "CONTAINER-001" for g in trim_gaps)

def test_partial_container_001_fires_on_fastqc():
    """FASTQC has no container AND no conda → CONTAINER-001 fires."""
    wf     = parser.parse_file(FIXTURES / "partial.smk")
    report = engine.run(wf)
    fq_gaps = gaps_for(report, "FASTQC")
    assert any(g.gap_id == "CONTAINER-001" for g in fq_gaps)

def test_partial_container_003_not_fires_on_fastqc():
    """FASTQC has no conda → CONTAINER-003 must not fire."""
    wf     = parser.parse_file(FIXTURES / "partial.smk")
    report = engine.run(wf)
    fq_gaps = gaps_for(report, "FASTQC")
    assert not any(g.gap_id == "CONTAINER-003" for g in fq_gaps)

def test_partial_resource_002_fires_on_trim():
    wf     = parser.parse_file(FIXTURES / "partial.smk")
    report = engine.run(wf)
    trim_gaps = gaps_for(report, "TRIM")
    assert any(g.gap_id == "RESOURCE-002" for g in trim_gaps)

def test_partial_resource_001_not_fires_on_trim():
    """TRIM declares threads — RESOURCE-001 must be silent."""
    wf     = parser.parse_file(FIXTURES / "partial.smk")
    report = engine.run(wf)
    trim_gaps = gaps_for(report, "TRIM")
    assert not any(g.gap_id == "RESOURCE-001" for g in trim_gaps)

def test_partial_score_between_zero_and_one():
    wf     = parser.parse_file(FIXTURES / "partial.smk")
    report = engine.run(wf)
    assert 0.0 < report.summary.cloud_readiness_score < 1.0


# ── Regression: Nextflow clean.nf still scores 1.00 after CONTAINER-001 change ─

def test_nextflow_clean_still_scores_perfect_after_day8():
    """
    The CONTAINER-001 modification (skip when conda present) must not affect
    Nextflow workflows.  All Nextflow processes have conda=None, so the guard
    is a no-op for them.
    """
    from workflow_clinic.parsers.nextflow import NextflowParser
    nf_fixtures = Path(__file__).parent / "fixtures" / "nextflow"
    wf     = NextflowParser().parse_file(nf_fixtures / "clean.nf")
    report = engine.run(wf)
    assert report.summary.total_gaps == 0
    assert report.summary.cloud_readiness_score == 1.0


# ── CLI auto-detection smoke tests ────────────────────────────────────────────

def test_cli_parse_detects_smk_extension():
    result = runner.invoke(app, ["parse", str(FIXTURES / "clean.smk")])
    assert result.exit_code == 0
    assert "ALIGN"   in result.output
    assert "SORT_BAM" in result.output

def test_cli_critic_detects_smk_extension():
    result = runner.invoke(app, ["critic", str(FIXTURES / "broken.smk")])
    assert result.exit_code == 0
    assert "CONTAINER-001" in result.output

def test_cli_critic_snakemake_json_is_valid():
    import json
    result = runner.invoke(
        app, ["critic", str(FIXTURES / "broken.smk"), "--format", "json"]
    )
    assert result.exit_code == 0
    data = json.loads(result.output)
    assert "gaps"    in data
    assert "summary" in data

def test_cli_critic_snakemake_clean_shows_no_gaps():
    result = runner.invoke(app, ["critic", str(FIXTURES / "clean.smk")])
    assert result.exit_code == 0
    assert "No gaps found" in result.output

def test_cli_critic_snakemake_score_flag():
    result = runner.invoke(
        app, ["critic", str(FIXTURES / "clean.smk"), "--score"]
    )
    assert result.exit_code == 0
    assert float(result.output.strip()) == 1.0

def test_cli_critic_container_003_in_partial_output():
    result = runner.invoke(app, ["critic", str(FIXTURES / "partial.smk")])
    assert result.exit_code == 0
    assert "CONTAINER-003" in result.output