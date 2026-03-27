"""
Tests for the resource_hints rules (RESOURCE-001, RESOURCE-002)
and the --create-issue / --issue-output CLI flags introduced on Day 7.

Coverage targets
────────────────
resource_hints.py — 100%
  ✓ CpusMissingRule fires on broken.nf (no cpus anywhere)
  ✓ CpusMissingRule is silent on clean.nf
  ✓ CpusMissingRule is silent on partial.nf FASTQC (has cpus 1)
  ✓ MemoryMissingRule fires on broken.nf
  ✓ MemoryMissingRule fires on partial.nf TRIM (cpus present, memory absent)
  ✓ MemoryMissingRule is silent on clean.nf
  ✓ MemoryMissingRule is silent on partial.nf FASTQC (has memory '2 GB')
  ✓ Both rules produce MINOR severity
  ✓ Both rules set category = RESOURCE_HINTS
  ✓ auto_fixable is False for both (no fixer yet)

engine integration
  ✓ clean.nf: no new gaps (both directives present in both processes)
  ✓ broken.nf: 4 new MINOR gaps (2 processes × 2 missing directives)
  ✓ partial.nf TRIM: only RESOURCE-002 (has cpus, missing memory)
  ✓ partial.nf FASTQC: no resource gaps (both present)

CLI --create-issue
  ✓ flag accepted with exit 0
  ✓ output contains suggested title
  ✓ output contains gap_id strings (proves gaps are threaded through)
  ✓ output contains severity labels
  ✓ --issue-output saves to file
  ✓ clean workflow draft says no gaps found
"""

from __future__ import annotations

import json
from pathlib import Path
from typer.testing import CliRunner

import pytest

from workflow_clinic.critic.engine import CriticEngine
from workflow_clinic.critic.rules.resource_hints import CpusMissingRule, MemoryMissingRule
from workflow_clinic.parsers.nextflow import NextflowParser
from workflow_clinic.schema.gap_report import GapCategory, Severity
from workflow_clinic.cli import app

FIXTURES = Path(__file__).parent / "fixtures" / "nextflow"
parser  = NextflowParser()
engine  = CriticEngine()
runner  = CliRunner()


# ─────────────────────────────────────────────────────────────────────────────
# Helper
# ─────────────────────────────────────────────────────────────────────────────

def _gaps_for(fixture: str, rule_cls: type) -> list:
    rule = rule_cls()
    wf   = parser.parse_file(FIXTURES / fixture)
    return [g for proc in wf.processes for g in [rule.check(proc, fixture)] if g]


# ─────────────────────────────────────────────────────────────────────────────
# CpusMissingRule (RESOURCE-001)
# ─────────────────────────────────────────────────────────────────────────────

class TestCpusMissingRule:

    def test_fires_on_broken(self):
        """broken.nf processes have no cpus → rule fires for each."""
        gaps = _gaps_for("broken.nf", CpusMissingRule)
        assert len(gaps) == 2  # ALIGN and CALL_VARIANTS both missing cpus

    def test_gap_id_is_resource_001(self):
        gaps = _gaps_for("broken.nf", CpusMissingRule)
        assert all(g.gap_id == "RESOURCE-001" for g in gaps)

    def test_severity_is_minor(self):
        gaps = _gaps_for("broken.nf", CpusMissingRule)
        assert all(g.severity == Severity.MINOR for g in gaps)

    def test_category_is_resource_hints(self):
        gaps = _gaps_for("broken.nf", CpusMissingRule)
        assert all(g.category == GapCategory.RESOURCE_HINTS for g in gaps)

    def test_not_auto_fixable(self):
        gaps = _gaps_for("broken.nf", CpusMissingRule)
        assert all(not g.auto_fixable for g in gaps)

    def test_silent_on_clean(self):
        """clean.nf has cpus on both processes → rule should be silent."""
        gaps = _gaps_for("clean.nf", CpusMissingRule)
        assert gaps == []

    def test_silent_on_fastqc_in_partial(self):
        """FASTQC in partial.nf has cpus 1 → no gap."""
        rule = CpusMissingRule()
        wf   = parser.parse_file(FIXTURES / "partial.nf")
        fastqc = next(p for p in wf.processes if p.name == "FASTQC")
        assert rule.check(fastqc, "partial.nf") is None

    def test_fires_on_trim_in_partial(self):
        """TRIM in partial.nf has cpus 2 → should NOT fire."""
        rule = CpusMissingRule()
        wf   = parser.parse_file(FIXTURES / "partial.nf")
        trim = next(p for p in wf.processes if p.name == "TRIM")
        assert rule.check(trim, "partial.nf") is None  # TRIM has cpus 2

    def test_recommendation_mentions_task_cpus(self):
        """Recommendation must mention ${task.cpus} so devs know how to wire it up."""
        gaps = _gaps_for("broken.nf", CpusMissingRule)
        assert any("task.cpus" in g.recommendation for g in gaps)


# ─────────────────────────────────────────────────────────────────────────────
# MemoryMissingRule (RESOURCE-002)
# ─────────────────────────────────────────────────────────────────────────────

class TestMemoryMissingRule:

    def test_fires_on_broken(self):
        """broken.nf processes have no memory → rule fires for each."""
        gaps = _gaps_for("broken.nf", MemoryMissingRule)
        assert len(gaps) == 2

    def test_gap_id_is_resource_002(self):
        gaps = _gaps_for("broken.nf", MemoryMissingRule)
        assert all(g.gap_id == "RESOURCE-002" for g in gaps)

    def test_severity_is_minor(self):
        gaps = _gaps_for("broken.nf", MemoryMissingRule)
        assert all(g.severity == Severity.MINOR for g in gaps)

    def test_category_is_resource_hints(self):
        gaps = _gaps_for("broken.nf", MemoryMissingRule)
        assert all(g.category == GapCategory.RESOURCE_HINTS for g in gaps)

    def test_not_auto_fixable(self):
        gaps = _gaps_for("broken.nf", MemoryMissingRule)
        assert all(not g.auto_fixable for g in gaps)

    def test_silent_on_clean(self):
        gaps = _gaps_for("clean.nf", MemoryMissingRule)
        assert gaps == []

    def test_fires_on_trim_in_partial(self):
        """TRIM has cpus 2 but no memory → RESOURCE-002 must fire."""
        rule = MemoryMissingRule()
        wf   = parser.parse_file(FIXTURES / "partial.nf")
        trim = next(p for p in wf.processes if p.name == "TRIM")
        gap  = rule.check(trim, "partial.nf")
        assert gap is not None
        assert gap.gap_id == "RESOURCE-002"

    def test_silent_on_fastqc_in_partial(self):
        """FASTQC has memory '2 GB' → rule should be silent."""
        rule   = MemoryMissingRule()
        wf     = parser.parse_file(FIXTURES / "partial.nf")
        fastqc = next(p for p in wf.processes if p.name == "FASTQC")
        assert rule.check(fastqc, "partial.nf") is None

    def test_recommendation_mentions_retry(self):
        """Recommendation should mention retry strategy — the cloud best practice."""
        gaps = _gaps_for("broken.nf", MemoryMissingRule)
        assert any("retry" in g.recommendation.lower() for g in gaps)


# ─────────────────────────────────────────────────────────────────────────────
# Engine integration — rules registered and producing expected counts
# ─────────────────────────────────────────────────────────────────────────────

class TestResourceRulesInEngine:

    def test_clean_still_has_no_gaps(self):
        """Adding resource rules must not break the clean.nf golden test."""
        wf     = parser.parse_file(FIXTURES / "clean.nf")
        report = engine.run(wf)
        assert report.summary.total_gaps == 0

    def test_clean_score_still_perfect(self):
        wf     = parser.parse_file(FIXTURES / "clean.nf")
        report = engine.run(wf)
        assert report.summary.cloud_readiness_score == 1.0

    def test_broken_has_resource_001_gaps(self):
        wf     = parser.parse_file(FIXTURES / "broken.nf")
        report = engine.run(wf)
        resource_001 = [g for g in report.gaps if g.gap_id == "RESOURCE-001"]
        assert len(resource_001) == 2  # one per process

    def test_broken_has_resource_002_gaps(self):
        wf     = parser.parse_file(FIXTURES / "broken.nf")
        report = engine.run(wf)
        resource_002 = [g for g in report.gaps if g.gap_id == "RESOURCE-002"]
        assert len(resource_002) == 2

    def test_broken_minor_count_increased(self):
        """Both resource rules are MINOR — broken.nf should now have minor gaps."""
        wf     = parser.parse_file(FIXTURES / "broken.nf")
        report = engine.run(wf)
        assert report.summary.minor >= 4  # 2 × RESOURCE-001 + 2 × RESOURCE-002

    def test_broken_total_count_includes_resource_gaps(self):
        """Arithmetic: total must equal sum of all severity buckets."""
        wf     = parser.parse_file(FIXTURES / "broken.nf")
        report = engine.run(wf)
        s = report.summary
        assert s.total_gaps == s.critical + s.major + s.minor + s.info

    def test_partial_trim_has_resource_002_not_001(self):
        """TRIM has cpus but not memory: only RESOURCE-002 should fire."""
        wf     = parser.parse_file(FIXTURES / "partial.nf")
        report = engine.run(wf)
        trim_gaps = [g for g in report.gaps if g.process_name == "TRIM"]
        gap_ids   = [g.gap_id for g in trim_gaps]
        assert "RESOURCE-002" in gap_ids
        assert "RESOURCE-001" not in gap_ids

    def test_partial_fastqc_has_no_resource_gaps(self):
        """FASTQC in partial.nf has both cpus and memory."""
        wf     = parser.parse_file(FIXTURES / "partial.nf")
        report = engine.run(wf)
        fastqc_resource = [
            g for g in report.gaps
            if g.process_name == "FASTQC"
            and g.gap_id.startswith("RESOURCE")
        ]
        assert fastqc_resource == []

    def test_partial_score_still_between_zero_and_one(self):
        wf     = parser.parse_file(FIXTURES / "partial.nf")
        report = engine.run(wf)
        assert 0.0 < report.summary.cloud_readiness_score < 1.0


# ─────────────────────────────────────────────────────────────────────────────
# CLI — --create-issue flag
# ─────────────────────────────────────────────────────────────────────────────

class TestCreateIssueFlag:

    def test_create_issue_exits_zero(self):
        result = runner.invoke(
            app, ["critic", str(FIXTURES / "broken.nf"), "--create-issue"]
        )
        assert result.exit_code == 0

    def test_create_issue_output_contains_title(self):
        result = runner.invoke(
            app, ["critic", str(FIXTURES / "broken.nf"), "--create-issue"]
        )
        assert "Suggested title" in result.output

    def test_create_issue_output_contains_gap_ids(self):
        result = runner.invoke(
            app, ["critic", str(FIXTURES / "broken.nf"), "--create-issue"]
        )
        assert "CONTAINER-001" in result.output

    def test_create_issue_output_contains_severity_label(self):
        result = runner.invoke(
            app, ["critic", str(FIXTURES / "broken.nf"), "--create-issue"]
        )
        assert "CRITICAL" in result.output

    def test_create_issue_output_contains_process_name(self):
        result = runner.invoke(
            app, ["critic", str(FIXTURES / "broken.nf"), "--create-issue"]
        )
        assert "ALIGN" in result.output

    def test_create_issue_notes_it_is_not_submitted(self):
        """Draft must clearly tell the user nothing was POSTed to GitHub."""
        result = runner.invoke(
            app, ["critic", str(FIXTURES / "broken.nf"), "--create-issue"]
        )
        assert "NOT been submitted" in result.output or "not submit" in result.output.lower()

    def test_create_issue_output_flag_writes_file(self, tmp_path):
        out = tmp_path / "issue.md"
        result = runner.invoke(
            app, [
                "critic", str(FIXTURES / "broken.nf"),
                "--issue-output", str(out),
            ]
        )
        assert result.exit_code == 0
        assert out.exists()
        content = out.read_text()
        assert "WORKFLOW CLINIC ISSUE DRAFT" in content
        assert "CONTAINER-001" in content

    def test_create_issue_output_flag_implies_create_issue(self, tmp_path):
        """--issue-output alone (no --create-issue) should still write the file."""
        out = tmp_path / "issue.md"
        result = runner.invoke(
            app, [
                "critic", str(FIXTURES / "broken.nf"),
                "--issue-output", str(out),
            ]
        )
        assert out.exists()
        assert result.exit_code == 0

    def test_create_issue_clean_workflow_says_no_gaps(self):
        result = runner.invoke(
            app, ["critic", str(FIXTURES / "clean.nf"), "--create-issue"]
        )
        assert result.exit_code == 0
        # clean workflow → issue draft should reflect clean state
        assert "No gaps found" in result.output or "no gaps" in result.output.lower()

    def test_create_issue_includes_resource_001_gaps(self):
        """RESOURCE-001 gaps from broken.nf must appear in the issue draft."""
        result = runner.invoke(
            app, ["critic", str(FIXTURES / "broken.nf"), "--create-issue"]
        )
        assert "RESOURCE-001" in result.output

    def test_create_issue_includes_resource_002_gaps(self):
        result = runner.invoke(
            app, ["critic", str(FIXTURES / "broken.nf"), "--create-issue"]
        )
        assert "RESOURCE-002" in result.output

    def test_create_issue_compatible_with_json_format(self):
        """--create-issue should work alongside --format json.

        The output is mixed: the JSON report comes first (via typer.echo),
        then the rich-rendered issue draft follows.  We extract the JSON by
        using JSONDecoder.raw_decode(), which stops at the exact character
        where the first complete JSON object ends — unaffected by any `}`
        characters that appear later in the markdown body.
        """
        result = runner.invoke(
            app, [
                "critic", str(FIXTURES / "broken.nf"),
                "--format", "json",
                "--create-issue",
            ]
        )
        assert result.exit_code == 0

        json_start = result.output.find("{")
        assert json_start >= 0, "No JSON object found in output"

        data, _ = json.JSONDecoder().raw_decode(result.output, json_start)
        assert "gaps" in data
        assert "summary" in data

    def test_issue_output_file_contains_title_comment(self, tmp_path):
        out = tmp_path / "issue.md"
        runner.invoke(
            app, [
                "critic", str(FIXTURES / "broken.nf"),
                "--issue-output", str(out),
            ]
        )
        content = out.read_text()
        # The HTML comment with the title should be the very first line
        assert content.startswith("<!-- WORKFLOW CLINIC ISSUE DRAFT -->")