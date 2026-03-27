from pathlib import Path

from workflow_clinic.parsers.nextflow import NextflowParser
from workflow_clinic.critic.engine import CriticEngine
from workflow_clinic.schema.gap_report import Severity

FIXTURES = Path(__file__).parent / "fixtures" / "nextflow"
parser = NextflowParser()
engine = CriticEngine()


# ── Helper ────────────────────────────────────────────────────────────────────

def gap_ids(report):
    return [g.gap_id for g in report.gaps]

def gaps_for_process(report, name):
    return [g for g in report.gaps if g.process_name == name]


# ── Clean workflow — no gaps expected ────────────────────────────────────────

def test_clean_no_gaps():
    wf = parser.parse_file(FIXTURES / "clean.nf")
    report = engine.run(wf)
    assert report.summary.total_gaps == 0

def test_clean_score_is_perfect():
    wf = parser.parse_file(FIXTURES / "clean.nf")
    report = engine.run(wf)
    assert report.summary.cloud_readiness_score == 1.0


# ── Broken workflow — all gap types should fire ───────────────────────────────

def test_broken_container_missing_fires():
    wf = parser.parse_file(FIXTURES / "broken.nf")
    report = engine.run(wf)
    assert "CONTAINER-001" in gap_ids(report)

def test_broken_container_missing_is_critical():
    wf = parser.parse_file(FIXTURES / "broken.nf")
    report = engine.run(wf)
    critical_gaps = [g for g in report.gaps if g.gap_id == "CONTAINER-001"]
    assert all(g.severity == Severity.CRITICAL for g in critical_gaps)

def test_broken_hardcoded_path_fires():
    wf = parser.parse_file(FIXTURES / "broken.nf")
    report = engine.run(wf)
    assert "STORAGE-001" in gap_ids(report)

def test_broken_hardcoded_path_evidence_contains_path():
    wf = parser.parse_file(FIXTURES / "broken.nf")
    report = engine.run(wf)
    storage_gaps = [g for g in report.gaps if g.gap_id == "STORAGE-001"]
    assert any("hg38" in g.evidence or "scratch" in g.evidence
               for g in storage_gaps)

def test_broken_undeclared_output_fires():
    wf = parser.parse_file(FIXTURES / "broken.nf")
    report = engine.run(wf)
    assert "IO-001" in gap_ids(report)

def test_broken_call_variants_missing_output():
    wf = parser.parse_file(FIXTURES / "broken.nf")
    report = engine.run(wf)
    cv_gaps = gaps_for_process(report, "CALL_VARIANTS")
    assert any(g.gap_id == "IO-001" for g in cv_gaps)

def test_broken_score_is_penalised():
    wf = parser.parse_file(FIXTURES / "broken.nf")
    report = engine.run(wf)
    assert report.summary.cloud_readiness_score < 0.5

def test_broken_summary_counts_are_correct():
    wf = parser.parse_file(FIXTURES / "broken.nf")
    report = engine.run(wf)
    assert report.summary.critical >= 2   # both processes missing container
    assert report.summary.total_gaps == (
        report.summary.critical
        + report.summary.major
        + report.summary.minor
        + report.summary.info
    )


# ── Partial workflow — mixed results ─────────────────────────────────────────

def test_partial_latest_tag_fires_on_trim():
    wf = parser.parse_file(FIXTURES / "partial.nf")
    report = engine.run(wf)
    trim_gaps = gaps_for_process(report, "TRIM")
    assert any(g.gap_id == "CONTAINER-002" for g in trim_gaps)

def test_partial_container_missing_fires_on_fastqc():
    wf = parser.parse_file(FIXTURES / "partial.nf")
    report = engine.run(wf)
    fastqc_gaps = gaps_for_process(report, "FASTQC")
    assert any(g.gap_id == "CONTAINER-001" for g in fastqc_gaps)

def test_partial_latest_tag_does_not_fire_on_fastqc():
    # FASTQC has no container at all — CONTAINER-001 should fire, not 002
    wf = parser.parse_file(FIXTURES / "partial.nf")
    report = engine.run(wf)
    fastqc_gaps = gaps_for_process(report, "FASTQC")
    assert not any(g.gap_id == "CONTAINER-002" for g in fastqc_gaps)

def test_partial_score_is_between_zero_and_one():
    wf = parser.parse_file(FIXTURES / "partial.nf")
    report = engine.run(wf)
    assert 0.0 < report.summary.cloud_readiness_score < 1.0


# ── GapReport structure ───────────────────────────────────────────────────────

def test_report_has_generated_at():
    wf = parser.parse_file(FIXTURES / "broken.nf")
    report = engine.run(wf)
    assert report.generated_at is not None

def test_report_workflow_path_is_set():
    wf = parser.parse_file(FIXTURES / "broken.nf")
    report = engine.run(wf)
    assert "broken.nf" in report.workflow_path

def test_gap_location_has_valid_lines():
    wf = parser.parse_file(FIXTURES / "broken.nf")
    report = engine.run(wf)
    for gap in report.gaps:
        assert gap.location.line_start > 0
        assert gap.location.line_end >= gap.location.line_start