"""
Run the Critic against real public Nextflow workflows from Dockstore
and save the gap reports to results/.

Run with:
    python scripts/collect_real_results.py
"""

from __future__ import annotations

import json
from pathlib import Path

from workflow_clinic.core.fetcher import fetch
from workflow_clinic.critic.engine import CriticEngine
from workflow_clinic.parsers.nextflow import NextflowParser

WORKFLOWS = [
    "dockstore:github.com/nf-core/rnaseq",
    "dockstore:github.com/nf-core/sarek",
    "dockstore:github.com/nf-core/methylseq",
    "dockstore:github.com/nf-core/atacseq",
    "dockstore:github.com/nf-core/chipseq",
    "dockstore:github.com/AAFC-Bioinfo-AAC/metagenomics-nf",
    "dockstore:github.com/bethsheets/workflows-demo",
    "dockstore:github.com/erinyoung/roundabout"
]

results_dir = Path("results")
results_dir.mkdir(exist_ok=True)

parser = NextflowParser()
engine = CriticEngine()

for source in WORKFLOWS:
    print(f"Fetching {source} ...", end=" ", flush=True)
    try:
        fetched  = fetch(source, full_repo=True)
        workflow = parser.parse(fetched.content, Path(fetched.filename))
        report   = engine.run(workflow)

        slug     = source.replace("dockstore:github.com/", "").replace("/", "_")
        out_path = results_dir / f"{slug}.json"
        out_path.write_text(
            json.dumps(report.model_dump(mode="json"), indent=2),
            encoding="utf-8",
        )
        score = report.summary.cloud_readiness_score
        gaps  = report.summary.total_gaps
        print(f"score={score:.2f}  gaps={gaps}  → {out_path}")

    except Exception as exc:
        print(f"FAILED — {exc}")