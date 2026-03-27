from pathlib import Path
from workflow_clinic.parsers.nextflow import NextflowParser


FIXTURES = Path(__file__).parent / "fixtures" / "nextflow"
parser = NextflowParser()


# ── Clean workflow ────────────────────────────────────────────────────────────

def test_clean_process_count():
    wf = parser.parse_file(FIXTURES / "clean.nf")
    assert len(wf.processes) == 2

def test_clean_process_names():
    wf = parser.parse_file(FIXTURES / "clean.nf")
    names = [p.name for p in wf.processes]
    assert "ALIGN" in names
    assert "SORT_BAM" in names

def test_clean_container_detected():
    wf = parser.parse_file(FIXTURES / "clean.nf")
    align = next(p for p in wf.processes if p.name == "ALIGN")
    assert align.container == "quay.io/biocontainers/bwa:0.7.17"

def test_clean_cpus_memory_detected():
    wf = parser.parse_file(FIXTURES / "clean.nf")
    align = next(p for p in wf.processes if p.name == "ALIGN")
    assert align.cpus == "4"
    assert align.memory == "'8 GB'"

def test_clean_all_directives_present():
    wf = parser.parse_file(FIXTURES / "clean.nf")
    for proc in wf.processes:
        assert set(["container", "cpus", "memory", "input", "output", "script"]) \
               == set(proc.directives_found())


# ── Broken workflow ───────────────────────────────────────────────────────────

def test_broken_process_count():
    wf = parser.parse_file(FIXTURES / "broken.nf")
    assert len(wf.processes) == 2

def test_broken_no_container():
    wf = parser.parse_file(FIXTURES / "broken.nf")
    for proc in wf.processes:
        assert proc.container is None

def test_broken_no_cpus_memory():
    wf = parser.parse_file(FIXTURES / "broken.nf")
    align = next(p for p in wf.processes if p.name == "ALIGN")
    assert align.cpus is None
    assert align.memory is None

def test_broken_script_captured():
    wf = parser.parse_file(FIXTURES / "broken.nf")
    align = next(p for p in wf.processes if p.name == "ALIGN")
    assert "hg38.fa" in align.script.raw   # hardcoded path evidence present

def test_broken_missing_output():
    wf = parser.parse_file(FIXTURES / "broken.nf")
    call = next(p for p in wf.processes if p.name == "CALL_VARIANTS")
    assert call.output.raw == ""


# ── Partial workflow ──────────────────────────────────────────────────────────

def test_partial_latest_tag_captured():
    wf = parser.parse_file(FIXTURES / "partial.nf")
    trim = next(p for p in wf.processes if p.name == "TRIM")
    assert trim.container is not None
    assert "latest" in trim.container

def test_partial_missing_container_on_fastqc():
    wf = parser.parse_file(FIXTURES / "partial.nf")
    fastqc = next(p for p in wf.processes if p.name == "FASTQC")
    assert fastqc.container is None

def test_partial_missing_memory_on_trim():
    wf = parser.parse_file(FIXTURES / "partial.nf")
    trim = next(p for p in wf.processes if p.name == "TRIM")
    assert trim.memory is None


# ── Line ranges ───────────────────────────────────────────────────────────────

def test_line_range_is_set():
    wf = parser.parse_file(FIXTURES / "clean.nf")
    for proc in wf.processes:
        assert proc.line_start > 0
        assert proc.line_end > proc.line_start