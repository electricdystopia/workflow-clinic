"""
CLI integration tests — run the critic command and check exit codes,
output content, and file writing without depending on terminal rendering.
"""

from pathlib import Path
from typer.testing import CliRunner
from workflow_clinic.cli import app
import json

FIXTURES = Path(__file__).parent / "fixtures" / "nextflow"
runner = CliRunner()


# ── critic — terminal (default) ───────────────────────────────────────────────

def test_critic_terminal_exits_zero_on_clean():
    result = runner.invoke(app, ["critic", str(FIXTURES / "clean.nf")])
    assert result.exit_code == 0

def test_critic_terminal_exits_zero_on_broken():
    # non-zero gaps should still exit 0 — gaps are not a CLI error
    result = runner.invoke(app, ["critic", str(FIXTURES / "broken.nf")])
    assert result.exit_code == 0

def test_critic_terminal_shows_gap_id():
    result = runner.invoke(app, ["critic", str(FIXTURES / "broken.nf")])
    assert "CONTAINER-001" in result.output

def test_critic_terminal_shows_process_name():
    result = runner.invoke(app, ["critic", str(FIXTURES / "broken.nf")])
    assert "ALIGN" in result.output

def test_critic_clean_shows_no_gaps_message():
    result = runner.invoke(app, ["critic", str(FIXTURES / "clean.nf")])
    assert "No gaps found" in result.output


# ── critic — json format ──────────────────────────────────────────────────────

def test_critic_json_is_valid_json():
    result = runner.invoke(app, ["critic", str(FIXTURES / "broken.nf"), "--format", "json"])
    assert result.exit_code == 0
    data = json.loads(result.output)
    assert "gaps" in data
    assert "summary" in data

def test_critic_json_contains_expected_gap():
    result = runner.invoke(app, ["critic", str(FIXTURES / "broken.nf"), "--format", "json"])
    data = json.loads(result.output)
    gap_ids = [g["gap_id"] for g in data["gaps"]]
    assert "CONTAINER-001" in gap_ids

def test_critic_json_score_is_float():
    result = runner.invoke(app, ["critic", str(FIXTURES / "broken.nf"), "--format", "json"])
    data = json.loads(result.output)
    assert isinstance(data["summary"]["cloud_readiness_score"], float)


# ── critic — markdown format ──────────────────────────────────────────────────

def test_critic_markdown_contains_header():
    result = runner.invoke(app, ["critic", str(FIXTURES / "broken.nf"), "--format", "markdown"])
    assert result.exit_code == 0
    assert "Workflow Clinic" in result.output

def test_critic_markdown_contains_gap_table():
    result = runner.invoke(app, ["critic", str(FIXTURES / "broken.nf"), "--format", "markdown"])
    assert "CONTAINER-001" in result.output
    assert "CRITICAL" in result.output


# ── critic — --score flag ─────────────────────────────────────────────────────

def test_critic_score_flag_returns_float():
    result = runner.invoke(app, ["critic", str(FIXTURES / "broken.nf"), "--score"])
    assert result.exit_code == 0
    score = float(result.output.strip())
    assert 0.0 <= score <= 1.0

def test_critic_score_clean_is_perfect():
    result = runner.invoke(app, ["critic", str(FIXTURES / "clean.nf"), "--score"])
    assert float(result.output.strip()) == 1.0

def test_critic_score_broken_is_low():
    result = runner.invoke(app, ["critic", str(FIXTURES / "broken.nf"), "--score"])
    assert float(result.output.strip()) < 0.5


# ── critic — --output flag ────────────────────────────────────────────────────

def test_critic_output_writes_json_file(tmp_path):
    out = tmp_path / "report.json"
    result = runner.invoke(app, [
        "critic", str(FIXTURES / "broken.nf"),
        "--format", "json",
        "--output", str(out),
    ])
    assert result.exit_code == 0
    assert out.exists()
    data = json.loads(out.read_text())
    assert "gaps" in data

def test_critic_output_writes_markdown_file(tmp_path):
    out = tmp_path / "report.md"
    result = runner.invoke(app, [
        "critic", str(FIXTURES / "broken.nf"),
        "--format", "markdown",
        "--output", str(out),
    ])
    assert result.exit_code == 0
    assert out.exists()
    assert "Workflow Clinic" in out.read_text()


# ── error handling ────────────────────────────────────────────────────────────

def test_critic_missing_file_exits_nonzero():
    result = runner.invoke(app, ["critic", "does_not_exist.nf"])
    assert result.exit_code == 1


# ── parse command still works ─────────────────────────────────────────────────

def test_parse_still_works():
    result = runner.invoke(app, ["parse", str(FIXTURES / "clean.nf")])
    assert result.exit_code == 0
    assert "ALIGN" in result.output