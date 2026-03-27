"""
Tests for the Snakemake parser.
Structure mirrors test_nextflow_parser.py — one section per fixture,
asserting exact field values rather than just presence.
"""

from pathlib import Path
import pytest

from workflow_clinic.parsers.snakemake import SnakemakeParser
from workflow_clinic.parsers.registry import ParserRegistry
from workflow_clinic.parsers.nextflow import NextflowParser

FIXTURES = Path(__file__).parent / "fixtures" / "snakemake"
parser   = SnakemakeParser()


# ── Clean workflow ────────────────────────────────────────────────────────────

def test_clean_process_count():
    wf = parser.parse_file(FIXTURES / "clean.smk")
    assert len(wf.processes) == 2

def test_clean_process_names():
    wf    = parser.parse_file(FIXTURES / "clean.smk")
    names = [p.name for p in wf.processes]
    assert "ALIGN"   in names
    assert "SORT_BAM" in names

def test_clean_singularity_captured_as_container():
    wf    = parser.parse_file(FIXTURES / "clean.smk")
    align = next(p for p in wf.processes if p.name == "ALIGN")
    assert align.container == "docker://quay.io/biocontainers/bwa:0.7.17--h5bf99c6_8"

def test_clean_threads_captured_as_cpus():
    wf    = parser.parse_file(FIXTURES / "clean.smk")
    align = next(p for p in wf.processes if p.name == "ALIGN")
    assert align.cpus == "4"

def test_clean_mem_mb_captured_as_memory():
    wf    = parser.parse_file(FIXTURES / "clean.smk")
    align = next(p for p in wf.processes if p.name == "ALIGN")
    assert align.memory is not None
    assert "8000" in align.memory

def test_clean_input_captured():
    wf    = parser.parse_file(FIXTURES / "clean.smk")
    align = next(p for p in wf.processes if p.name == "ALIGN")
    assert align.input.raw != ""

def test_clean_output_captured():
    wf    = parser.parse_file(FIXTURES / "clean.smk")
    align = next(p for p in wf.processes if p.name == "ALIGN")
    assert align.output.raw != ""

def test_clean_shell_captured_as_script():
    wf    = parser.parse_file(FIXTURES / "clean.smk")
    align = next(p for p in wf.processes if p.name == "ALIGN")
    assert align.script.raw != ""
    assert "bwa" in align.script.raw

def test_clean_no_conda_on_singularity_rules():
    wf = parser.parse_file(FIXTURES / "clean.smk")
    for proc in wf.processes:
        assert proc.conda is None

def test_clean_all_expected_directives_present():
    wf = parser.parse_file(FIXTURES / "clean.smk")
    for proc in wf.processes:
        found = set(proc.directives_found())
        assert {"container", "cpus", "memory", "input", "output", "script"} \
               <= found


# ── Broken workflow ───────────────────────────────────────────────────────────

def test_broken_process_count():
    wf = parser.parse_file(FIXTURES / "broken.smk")
    assert len(wf.processes) == 2

def test_broken_no_container():
    wf = parser.parse_file(FIXTURES / "broken.smk")
    for proc in wf.processes:
        assert proc.container is None

def test_broken_no_conda():
    wf = parser.parse_file(FIXTURES / "broken.smk")
    for proc in wf.processes:
        assert proc.conda is None

def test_broken_no_cpus():
    wf = parser.parse_file(FIXTURES / "broken.smk")
    for proc in wf.processes:
        assert proc.cpus is None

def test_broken_no_memory():
    wf = parser.parse_file(FIXTURES / "broken.smk")
    for proc in wf.processes:
        assert proc.memory is None

def test_broken_align_script_has_hardcoded_path():
    wf    = parser.parse_file(FIXTURES / "broken.smk")
    align = next(p for p in wf.processes if p.name == "ALIGN")
    assert "/data/ref/hg38.fa" in align.script.raw or "hg38" in align.script.raw

def test_broken_call_variants_missing_output():
    wf = parser.parse_file(FIXTURES / "broken.smk")
    cv = next(p for p in wf.processes if p.name == "CALL_VARIANTS")
    assert cv.output.raw == ""


# ── Partial workflow ──────────────────────────────────────────────────────────

def test_partial_conda_captured_on_trim():
    wf   = parser.parse_file(FIXTURES / "partial.smk")
    trim = next(p for p in wf.processes if p.name == "TRIM")
    assert trim.conda is not None
    assert "trimmomatic" in trim.conda

def test_partial_trim_no_singularity():
    wf   = parser.parse_file(FIXTURES / "partial.smk")
    trim = next(p for p in wf.processes if p.name == "TRIM")
    assert trim.container is None

def test_partial_trim_has_cpus_no_memory():
    wf   = parser.parse_file(FIXTURES / "partial.smk")
    trim = next(p for p in wf.processes if p.name == "TRIM")
    assert trim.cpus    is not None
    assert trim.memory  is None

def test_partial_trim_has_output():
    wf   = parser.parse_file(FIXTURES / "partial.smk")
    trim = next(p for p in wf.processes if p.name == "TRIM")
    assert trim.output.raw != ""

def test_partial_fastqc_no_container_no_conda():
    wf     = parser.parse_file(FIXTURES / "partial.smk")
    fastqc = next(p for p in wf.processes if p.name == "FASTQC")
    assert fastqc.container is None
    assert fastqc.conda     is None

def test_partial_fastqc_has_cpus_and_memory():
    wf     = parser.parse_file(FIXTURES / "partial.smk")
    fastqc = next(p for p in wf.processes if p.name == "FASTQC")
    assert fastqc.cpus   is not None
    assert fastqc.memory is not None

def test_partial_process_count():
    wf = parser.parse_file(FIXTURES / "partial.smk")
    assert len(wf.processes) == 2


# ── Line ranges ───────────────────────────────────────────────────────────────

def test_line_range_is_set():
    wf = parser.parse_file(FIXTURES / "clean.smk")
    for proc in wf.processes:
        assert proc.line_start > 0
        assert proc.line_end   > proc.line_start

def test_second_rule_starts_after_first_ends():
    wf    = parser.parse_file(FIXTURES / "clean.smk")
    align = next(p for p in wf.processes if p.name == "ALIGN")
    sort  = next(p for p in wf.processes if p.name == "SORT_BAM")
    assert sort.line_start > align.line_end


# ── ParserRegistry ────────────────────────────────────────────────────────────

def test_registry_returns_snakemake_parser_for_smk():
    p = ParserRegistry().get_parser(Path("workflow.smk"))
    assert isinstance(p, SnakemakeParser)

def test_registry_returns_snakemake_parser_for_snakefile():
    p = ParserRegistry().get_parser(Path("Snakefile"))
    assert isinstance(p, SnakemakeParser)

def test_registry_returns_snakemake_parser_for_snakefile_case_insensitive():
    p = ParserRegistry().get_parser(Path("SNAKEFILE"))
    assert isinstance(p, SnakemakeParser)

def test_registry_returns_nextflow_parser_for_nf():
    p = ParserRegistry().get_parser(Path("workflow.nf"))
    assert isinstance(p, NextflowParser)

def test_registry_defaults_to_nextflow_for_unknown_extension():
    p = ParserRegistry().get_parser(Path("workflow.cwl"))
    assert isinstance(p, NextflowParser)

def test_registry_parse_file_roundtrip():
    """Registry-resolved parser produces the same result as direct instantiation."""
    direct   = SnakemakeParser().parse_file(FIXTURES / "clean.smk")
    via_reg  = ParserRegistry().get_parser(FIXTURES / "clean.smk").parse_file(
        FIXTURES / "clean.smk"
    )
    assert [p.name for p in direct.processes] == \
           [p.name for p in via_reg.processes]