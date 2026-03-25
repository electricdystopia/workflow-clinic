"""
Run the Doctor against real public Nextflow workflows and save fix proposals
to results/doctor_*.json.

Only runs against workflows that already have a critic results file with at
least one auto-fixable gap — avoids spending LLM calls on clean workflows.

Run with:
    python scripts/collect_doctor_results.py

Requires an LLM key:
    export OLLAMA_MODEL=phi3:latest        # local, recommended
    export ANTHROPIC_API_KEY=...
    export GEMINI_API_KEY=...
"""

from __future__ import annotations

import dataclasses
import json
from datetime import datetime, timezone
from pathlib import Path

from workflow_clinic.core.fetcher import fetch
from workflow_clinic.critic.engine import CriticEngine
from workflow_clinic.doctor.engine import DoctorEngine
from workflow_clinic.parsers.nextflow import NextflowParser

# ── Workflows to process ──────────────────────────────────────────────────────
# These are the same sources used in collect_real_results.py.
# The script skips any that have no auto-fixable gaps.

WORKFLOWS = [
    "dockstore:github.com/nf-core/rnaseq",
    "dockstore:github.com/nf-core/sarek",
    "dockstore:github.com/nf-core/methylseq",
    "dockstore:github.com/nf-core/atacseq",
    "dockstore:github.com/nf-core/chipseq",
    "dockstore:github.com/AAFC-Bioinfo-AAC/metagenomics-nf",
    "dockstore:github.com/bethsheets/workflows-demo",
    "dockstore:github.com/erinyoung/roundabout",
]

# Only attempt fixes for this gap type — the only auto-fixable one so far.
GAP_FILTER = "CONTAINER-001"

results_dir = Path("results")
results_dir.mkdir(exist_ok=True)

parser = NextflowParser()
critic = CriticEngine()
doctor = DoctorEngine()


def _render_json(proposals, workflow_path: str, source: str) -> str:
    doc = {
        "schema_version": "0.1.0",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "workflow_path": workflow_path,
        "source": source,
        "proposals": [dataclasses.asdict(p) for p in proposals],
        "summary": {
            "total_proposals": len(proposals),
            "validated": sum(1 for p in proposals if p.validation_passed),
            "human_review_required": sum(
                1 for p in proposals if p.human_review_required
            ),
            "avg_confidence": round(
                sum(p.confidence for p in proposals) / len(proposals), 2
            ) if proposals else 0.0,
        },
    }
    return json.dumps(doc, indent=2)


for source in WORKFLOWS:
    slug = source.replace("dockstore:github.com/", "").replace("/", "_")
    print(f"Processing {slug} ...", end=" ", flush=True)

    try:
        fetched  = fetch(source, full_repo=True)
        workflow = parser.parse(fetched.content, Path(fetched.filename))
        report   = critic.run(workflow)

        # Skip workflows with no auto-fixable CONTAINER-001 gaps
        fixable = [g for g in report.gaps
                   if g.auto_fixable and g.gap_id == GAP_FILTER]
        if not fixable:
            print(f"skipped (no {GAP_FILTER} gaps)")
            continue

        print(f"{len(fixable)} fixable gaps → running Doctor ...", end=" ", flush=True)

        # Filter report to only the fixable gaps before passing to Doctor
        filtered_report = report.model_copy(update={"gaps": fixable})
        source_lines    = fetched.content.splitlines(keepends=True)
        proposals       = doctor.run(filtered_report, source_lines)

        validated = sum(1 for p in proposals if p.validation_passed)
        print(f"{len(proposals)} proposals ({validated} validated)")

        out_path = results_dir / f"doctor_{slug}.json"
        out_path.write_text(
            _render_json(proposals, fetched.filename, source),
            encoding="utf-8",
        )
        print(f"  → {out_path}")

    except Exception as exc:
        print(f"FAILED — {exc}")