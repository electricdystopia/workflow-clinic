# Workflow Clinic

Workflow Clinic is a command-line tool that audits Nextflow workflows for
cloud-readiness gaps and proposes code-level fixes. It is built as a proof of
concept for the GA4GH Cloud Work Stream's GSoC 2026 Workflow Clinic project.

---

## Install
```bash
git clone https://github.com/electricdystopia/workflow-clinic
cd workflow-clinic
python -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"
```

---

## Quick start

**Analyse a local workflow:**
```bash
workflow-clinic critic tests/fixtures/nextflow/broken.nf
```
```
───────────────── Workflow Clinic — Gap Report ─────────────────
Workflow:  tests/fixtures/nextflow/broken.nf
Processes: 2

Cloud Readiness Score: 0.20 / 1.00

 Total gaps    5
 Critical      2
 Major         3
 Auto-fixable  2
```

**Analyse a real workflow from GitHub:**
```bash
workflow-clinic critic https://github.com/nf-core/atacseq
```

**Get a machine-readable JSON report:**
```bash
workflow-clinic critic tests/fixtures/nextflow/broken.nf --format json
```

**Generate a fix for missing container directives:**
```bash
export GEMINI_API_KEY=your_key   # or OLLAMA_MODEL=llama3.2 for fully local
workflow-clinic doctor tests/fixtures/nextflow/broken.nf --gap CONTAINER-001
```
```
──────────────── CONTAINER-001 — ALIGN ─────────────────
Fix:        Add container directive: 'quay.io/biocontainers/bwa:0.7.17'
Confidence: 85%
Validated:  ✓ Parser confirmed container directive is present.

@@ -1,4 +1,5 @@
 process ALIGN {
+    container 'quay.io/biocontainers/bwa:0.7.17'
     input:
```

---

## Architecture
```
CLI (workflow_clinic/cli.py)
 ├── parse     → NextflowParser → ParsedWorkflow
 ├── critic    → CriticEngine   → GapReport (JSON / Markdown / terminal)
 └── doctor    → DoctorEngine   → FixProposal (unified diff)

Core services (workflow_clinic/core/)
 ├── fetcher.py      — Dockstore TRS API + GitHub Tree API
 └── llm_client.py   — model-agnostic wrapper (Gemini / Ollama / OpenAI)

Parser (workflow_clinic/parsers/nextflow.py)
 └── line-by-line state machine, extracts process blocks + directives

Rule engine (workflow_clinic/critic/rules/)
 ├── CONTAINER-001   missing container directive         CRITICAL
 ├── CONTAINER-002   :latest or untagged image           MAJOR
 ├── STORAGE-001     hardcoded absolute paths            MAJOR
 └── IO-001          missing output declaration          MAJOR

Fix generators (workflow_clinic/doctor/fix_generators/)
 ├── ContainerMissingFixer    — LLM suggests pinned image, inserts directive
 └── ContainerLatestTagFixer  — LLM suggests pinned replacement for :latest
```

---

## LLM setup (for `doctor` command)

The `doctor` command requires one of:

| Provider | Setup | Cost |
|---|---|---|
| **Ollama** (recommended for local dev) | `ollama pull llama3.2` then `export OLLAMA_MODEL=llama3.2` | Free, fully local |
| **Gemini** | Get key at [aistudio.google.com](https://aistudio.google.com) then `export GEMINI_API_KEY=...` | Free tier, 1500 req/day |
| **Groq** | Sign up at [console.groq.com](https://console.groq.com) then `export GROQ_API_KEY=...` | Free tier |

The `parse` and `critic` commands work with no API key at all.

---

## Real-world results

Gap reports from real Dockstore workflows are in [`results/`](results/). Summary:

| Workflow | Score | Critical | Major |
|---|---|---|---|
| nf-core/rnaseq | 1.00 | 0 | 0 |
| nf-core/atacseq | 0.00 | 51 | 37 |
| nf-core/methylseq | 0.00 | 6 | 5 |
| nf-core/chipseq | 0.30 | 2 | 2 |
| erinyoung/roundabout | 0.00 | 1 | 10 |

---

## Gap report schema

The full schema is defined in
[`workflow_clinic/schema/gap_report.py`](workflow_clinic/schema/gap_report.py).
Every gap report is a versioned JSON document:
```json
{
  "schema_version": "0.1.0",
  "generated_at": "2026-03-24T13:48:49Z",
  "workflow_path": "main.nf",
  "gaps": [...],
  "summary": {
    "total_gaps": 5,
    "critical": 2,
    "cloud_readiness_score": 0.20
  }
}
```

---

## Running tests
```bash
pytest tests/ -v --cov=workflow_clinic
```

---

## Project context

This tool is a proof of concept for the
[GA4GH Cloud Work Stream GSoC 2026 Workflow Clinic project](https://ga4gh.github.io/).
The full project will extend coverage to Snakemake, CWL, and WDL, add GitHub
issue and PR creation, and integrate a full agentic pipeline using LangGraph and
CrewAI. See [`docs/`](docs/) for detailed design decisions for each day of
development.