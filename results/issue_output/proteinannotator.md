<!-- WORKFLOW CLINIC ISSUE DRAFT -->
<!-- Title: [Workflow Clinic] 39 cloud-readiness gaps across 11 processes (score: 0%) -->

## 🏥 Workflow Clinic — Automated Cloud-Readiness Report

> **This issue was drafted automatically by [Workflow Clinic](https://github.com/electricdystopia/workflow-clinic), a GA4GH Cloud Work Stream tool for detecting and fixing cloud-readiness gaps in bioinformatics workflows.**
>
> Workflow: `main.nf`  
> Generated: 2026-03-28 18:43 UTC  
> Schema: `0.1.0`

### 🔴 Cloud Readiness Score: **0.00 / 1.00**

### Summary

| Severity | Count | Description |
|---|---|---|
| 🔴 **Critical** | 11 | Portability blockers — workflow cannot run on cloud WES |
| 🟠 **Major** | 6 | Significant gaps affecting reproducibility or correctness |
| 🟡 **Minor** | 22 | Resource hints missing — affects cost and scheduling efficiency |
| **Total** | **39** | |
| Auto-fixable | 11 | Can be fixed automatically with `workflow-clinic doctor` |

> 💡 **11 gap(s) can be fixed automatically.** Run `workflow-clinic doctor <path> --gap CONTAINER-001` to generate a patch and open a PR.

### Gaps

| # | Gap ID | Severity | Process | Category | Lines | Auto-fix |
|---|---|---|---|---|---|---|
| 1 | `CONTAINER-001` | 🔴 CRITICAL | `ARIA2` | containerization | L110–156 | ✅ |
| 2 | `RESOURCE-001` | 🟡 MINOR | `ARIA2` | resource_hints | L110–156 | — |
| 3 | `RESOURCE-002` | 🟡 MINOR | `ARIA2` | resource_hints | L110–156 | — |
| 4 | `CONTAINER-001` | 🔴 CRITICAL | `HMMER_HMMSEARCH` | containerization | L160–229 | ✅ |
| 5 | `STORAGE-001` | 🟠 MAJOR | `HMMER_HMMSEARCH` | storage | L160–229 | — |
| 6 | `RESOURCE-001` | 🟡 MINOR | `HMMER_HMMSEARCH` | resource_hints | L160–229 | — |
| 7 | `RESOURCE-002` | 🟡 MINOR | `HMMER_HMMSEARCH` | resource_hints | L160–229 | — |
| 8 | `CONTAINER-001` | 🔴 CRITICAL | `INTERPROSCAN` | containerization | L233–291 | ✅ |
| 9 | `STORAGE-001` | 🟠 MAJOR | `INTERPROSCAN` | storage | L233–291 | — |
| 10 | `RESOURCE-001` | 🟡 MINOR | `INTERPROSCAN` | resource_hints | L233–291 | — |
| 11 | `RESOURCE-002` | 🟡 MINOR | `INTERPROSCAN` | resource_hints | L233–291 | — |
| 12 | `CONTAINER-001` | 🔴 CRITICAL | `MULTIQC` | containerization | L295–349 | ✅ |
| 13 | `RESOURCE-001` | 🟡 MINOR | `MULTIQC` | resource_hints | L295–349 | — |
| 14 | `RESOURCE-002` | 🟡 MINOR | `MULTIQC` | resource_hints | L295–349 | — |
| 15 | `CONTAINER-001` | 🔴 CRITICAL | `S4PRED_RUNMODEL` | containerization | L353–404 | ✅ |
| 16 | `STORAGE-001` | 🟠 MAJOR | `S4PRED_RUNMODEL` | storage | L353–404 | — |
| 17 | `RESOURCE-001` | 🟡 MINOR | `S4PRED_RUNMODEL` | resource_hints | L353–404 | — |
| 18 | `RESOURCE-002` | 🟡 MINOR | `S4PRED_RUNMODEL` | resource_hints | L353–404 | — |
| 19 | `CONTAINER-001` | 🔴 CRITICAL | `SEQFU_STATS` | containerization | L408–459 | ✅ |
| 20 | `RESOURCE-001` | 🟡 MINOR | `SEQFU_STATS` | resource_hints | L408–459 | — |
| 21 | `RESOURCE-002` | 🟡 MINOR | `SEQFU_STATS` | resource_hints | L408–459 | — |
| 22 | `CONTAINER-001` | 🔴 CRITICAL | `SEQKIT_REPLACE` | containerization | L463–514 | ✅ |
| 23 | `STORAGE-001` | 🟠 MAJOR | `SEQKIT_REPLACE` | storage | L463–514 | — |
| 24 | `RESOURCE-001` | 🟡 MINOR | `SEQKIT_REPLACE` | resource_hints | L463–514 | — |
| 25 | `RESOURCE-002` | 🟡 MINOR | `SEQKIT_REPLACE` | resource_hints | L463–514 | — |
| 26 | `CONTAINER-001` | 🔴 CRITICAL | `SEQKIT_RMDUP` | containerization | L518–583 | ✅ |
| 27 | `STORAGE-001` | 🟠 MAJOR | `SEQKIT_RMDUP` | storage | L518–583 | — |
| 28 | `RESOURCE-001` | 🟡 MINOR | `SEQKIT_RMDUP` | resource_hints | L518–583 | — |
| 29 | `RESOURCE-002` | 🟡 MINOR | `SEQKIT_RMDUP` | resource_hints | L518–583 | — |
| 30 | `CONTAINER-001` | 🔴 CRITICAL | `SEQKIT_SEQ` | containerization | L587–653 | ✅ |
| 31 | `STORAGE-001` | 🟠 MAJOR | `SEQKIT_SEQ` | storage | L587–653 | — |
| 32 | `RESOURCE-001` | 🟡 MINOR | `SEQKIT_SEQ` | resource_hints | L587–653 | — |
| 33 | `RESOURCE-002` | 🟡 MINOR | `SEQKIT_SEQ` | resource_hints | L587–653 | — |
| 34 | `CONTAINER-001` | 🔴 CRITICAL | `SEQKIT_STATS` | containerization | L657–692 | ✅ |
| 35 | `RESOURCE-001` | 🟡 MINOR | `SEQKIT_STATS` | resource_hints | L657–692 | — |
| 36 | `RESOURCE-002` | 🟡 MINOR | `SEQKIT_STATS` | resource_hints | L657–692 | — |
| 37 | `CONTAINER-001` | 🔴 CRITICAL | `UNTAR` | containerization | L696–770 | ✅ |
| 38 | `RESOURCE-001` | 🟡 MINOR | `UNTAR` | resource_hints | L696–770 | — |
| 39 | `RESOURCE-002` | 🟡 MINOR | `UNTAR` | resource_hints | L696–770 | — |

### Detail

<details><summary>🔴 <strong>1. CONTAINER-001 — ARIA2</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L110–156  
**Auto-fixable:** Yes

**Description:**  
Process 'ARIA2' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟡 <strong>2. RESOURCE-001 — ARIA2</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L110–156  
**Auto-fixable:** No

**Description:**  
Process 'ARIA2' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

**Recommendation:**
```
Add a cpus directive appropriate for the tool's parallelism:
    cpus 4

Reference the allocation in the script block so the tool actually uses the provisioned cores:
    bwa mem -t ${task.cpus} ...

For workflows that need to scale, consider a dynamic expression:
    cpus { reads.size() > 5.GB ? 8 : 4 }
```

</details>

<details><summary>🟡 <strong>3. RESOURCE-002 — ARIA2</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L110–156  
**Auto-fixable:** No

**Description:**  
Process 'ARIA2' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

**Recommendation:**
```
Add a memory directive sized for the tool's peak usage:
    memory '8 GB'

For resilient pipelines, combine with an error strategy that increases memory on retry:
    errorStrategy 'retry'
    maxRetries 2
    memory { (8.GB * task.attempt).clamp(null, 32.GB) }
```

</details>

<details><summary>🔴 <strong>4. CONTAINER-001 — HMMER_HMMSEARCH</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L160–229  
**Auto-fixable:** Yes

**Description:**  
Process 'HMMER_HMMSEARCH' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟠 <strong>5. STORAGE-001 — HMMER_HMMSEARCH</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L160–229  
**Auto-fixable:** No

**Description:**  
Process 'HMMER_HMMSEARCH' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
//
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>6. RESOURCE-001 — HMMER_HMMSEARCH</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L160–229  
**Auto-fixable:** No

**Description:**  
Process 'HMMER_HMMSEARCH' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

**Recommendation:**
```
Add a cpus directive appropriate for the tool's parallelism:
    cpus 4

Reference the allocation in the script block so the tool actually uses the provisioned cores:
    bwa mem -t ${task.cpus} ...

For workflows that need to scale, consider a dynamic expression:
    cpus { reads.size() > 5.GB ? 8 : 4 }
```

</details>

<details><summary>🟡 <strong>7. RESOURCE-002 — HMMER_HMMSEARCH</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L160–229  
**Auto-fixable:** No

**Description:**  
Process 'HMMER_HMMSEARCH' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

**Recommendation:**
```
Add a memory directive sized for the tool's peak usage:
    memory '8 GB'

For resilient pipelines, combine with an error strategy that increases memory on retry:
    errorStrategy 'retry'
    maxRetries 2
    memory { (8.GB * task.attempt).clamp(null, 32.GB) }
```

</details>

<details><summary>🔴 <strong>8. CONTAINER-001 — INTERPROSCAN</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L233–291  
**Auto-fixable:** Yes

**Description:**  
Process 'INTERPROSCAN' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟠 <strong>9. STORAGE-001 — INTERPROSCAN</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L233–291  
**Auto-fixable:** No

**Description:**  
Process 'INTERPROSCAN' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
/share, /bin
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>10. RESOURCE-001 — INTERPROSCAN</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L233–291  
**Auto-fixable:** No

**Description:**  
Process 'INTERPROSCAN' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

**Recommendation:**
```
Add a cpus directive appropriate for the tool's parallelism:
    cpus 4

Reference the allocation in the script block so the tool actually uses the provisioned cores:
    bwa mem -t ${task.cpus} ...

For workflows that need to scale, consider a dynamic expression:
    cpus { reads.size() > 5.GB ? 8 : 4 }
```

</details>

<details><summary>🟡 <strong>11. RESOURCE-002 — INTERPROSCAN</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L233–291  
**Auto-fixable:** No

**Description:**  
Process 'INTERPROSCAN' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

**Recommendation:**
```
Add a memory directive sized for the tool's peak usage:
    memory '8 GB'

For resilient pipelines, combine with an error strategy that increases memory on retry:
    errorStrategy 'retry'
    maxRetries 2
    memory { (8.GB * task.attempt).clamp(null, 32.GB) }
```

</details>

<details><summary>🔴 <strong>12. CONTAINER-001 — MULTIQC</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L295–349  
**Auto-fixable:** Yes

**Description:**  
Process 'MULTIQC' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟡 <strong>13. RESOURCE-001 — MULTIQC</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L295–349  
**Auto-fixable:** No

**Description:**  
Process 'MULTIQC' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

**Recommendation:**
```
Add a cpus directive appropriate for the tool's parallelism:
    cpus 4

Reference the allocation in the script block so the tool actually uses the provisioned cores:
    bwa mem -t ${task.cpus} ...

For workflows that need to scale, consider a dynamic expression:
    cpus { reads.size() > 5.GB ? 8 : 4 }
```

</details>

<details><summary>🟡 <strong>14. RESOURCE-002 — MULTIQC</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L295–349  
**Auto-fixable:** No

**Description:**  
Process 'MULTIQC' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

**Recommendation:**
```
Add a memory directive sized for the tool's peak usage:
    memory '8 GB'

For resilient pipelines, combine with an error strategy that increases memory on retry:
    errorStrategy 'retry'
    maxRetries 2
    memory { (8.GB * task.attempt).clamp(null, 32.GB) }
```

</details>

<details><summary>🔴 <strong>15. CONTAINER-001 — S4PRED_RUNMODEL</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L353–404  
**Auto-fixable:** Yes

**Description:**  
Process 'S4PRED_RUNMODEL' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟠 <strong>16. STORAGE-001 — S4PRED_RUNMODEL</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L353–404  
**Auto-fixable:** No

**Description:**  
Process 'S4PRED_RUNMODEL' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
//
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>17. RESOURCE-001 — S4PRED_RUNMODEL</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L353–404  
**Auto-fixable:** No

**Description:**  
Process 'S4PRED_RUNMODEL' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

**Recommendation:**
```
Add a cpus directive appropriate for the tool's parallelism:
    cpus 4

Reference the allocation in the script block so the tool actually uses the provisioned cores:
    bwa mem -t ${task.cpus} ...

For workflows that need to scale, consider a dynamic expression:
    cpus { reads.size() > 5.GB ? 8 : 4 }
```

</details>

<details><summary>🟡 <strong>18. RESOURCE-002 — S4PRED_RUNMODEL</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L353–404  
**Auto-fixable:** No

**Description:**  
Process 'S4PRED_RUNMODEL' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

**Recommendation:**
```
Add a memory directive sized for the tool's peak usage:
    memory '8 GB'

For resilient pipelines, combine with an error strategy that increases memory on retry:
    errorStrategy 'retry'
    maxRetries 2
    memory { (8.GB * task.attempt).clamp(null, 32.GB) }
```

</details>

<details><summary>🔴 <strong>19. CONTAINER-001 — SEQFU_STATS</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L408–459  
**Auto-fixable:** Yes

**Description:**  
Process 'SEQFU_STATS' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟡 <strong>20. RESOURCE-001 — SEQFU_STATS</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L408–459  
**Auto-fixable:** No

**Description:**  
Process 'SEQFU_STATS' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

**Recommendation:**
```
Add a cpus directive appropriate for the tool's parallelism:
    cpus 4

Reference the allocation in the script block so the tool actually uses the provisioned cores:
    bwa mem -t ${task.cpus} ...

For workflows that need to scale, consider a dynamic expression:
    cpus { reads.size() > 5.GB ? 8 : 4 }
```

</details>

<details><summary>🟡 <strong>21. RESOURCE-002 — SEQFU_STATS</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L408–459  
**Auto-fixable:** No

**Description:**  
Process 'SEQFU_STATS' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

**Recommendation:**
```
Add a memory directive sized for the tool's peak usage:
    memory '8 GB'

For resilient pipelines, combine with an error strategy that increases memory on retry:
    errorStrategy 'retry'
    maxRetries 2
    memory { (8.GB * task.attempt).clamp(null, 32.GB) }
```

</details>

<details><summary>🔴 <strong>22. CONTAINER-001 — SEQKIT_REPLACE</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L463–514  
**Auto-fixable:** Yes

**Description:**  
Process 'SEQKIT_REPLACE' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟠 <strong>23. STORAGE-001 — SEQKIT_REPLACE</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L463–514  
**Auto-fixable:** No

**Description:**  
Process 'SEQKIT_REPLACE' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
/., /.
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>24. RESOURCE-001 — SEQKIT_REPLACE</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L463–514  
**Auto-fixable:** No

**Description:**  
Process 'SEQKIT_REPLACE' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

**Recommendation:**
```
Add a cpus directive appropriate for the tool's parallelism:
    cpus 4

Reference the allocation in the script block so the tool actually uses the provisioned cores:
    bwa mem -t ${task.cpus} ...

For workflows that need to scale, consider a dynamic expression:
    cpus { reads.size() > 5.GB ? 8 : 4 }
```

</details>

<details><summary>🟡 <strong>25. RESOURCE-002 — SEQKIT_REPLACE</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L463–514  
**Auto-fixable:** No

**Description:**  
Process 'SEQKIT_REPLACE' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

**Recommendation:**
```
Add a memory directive sized for the tool's peak usage:
    memory '8 GB'

For resilient pipelines, combine with an error strategy that increases memory on retry:
    errorStrategy 'retry'
    maxRetries 2
    memory { (8.GB * task.attempt).clamp(null, 32.GB) }
```

</details>

<details><summary>🔴 <strong>26. CONTAINER-001 — SEQKIT_RMDUP</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L518–583  
**Auto-fixable:** Yes

**Description:**  
Process 'SEQKIT_RMDUP' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟠 <strong>27. STORAGE-001 — SEQKIT_RMDUP</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L518–583  
**Auto-fixable:** No

**Description:**  
Process 'SEQKIT_RMDUP' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
/., //, /rmdup ... (1 more)
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>28. RESOURCE-001 — SEQKIT_RMDUP</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L518–583  
**Auto-fixable:** No

**Description:**  
Process 'SEQKIT_RMDUP' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

**Recommendation:**
```
Add a cpus directive appropriate for the tool's parallelism:
    cpus 4

Reference the allocation in the script block so the tool actually uses the provisioned cores:
    bwa mem -t ${task.cpus} ...

For workflows that need to scale, consider a dynamic expression:
    cpus { reads.size() > 5.GB ? 8 : 4 }
```

</details>

<details><summary>🟡 <strong>29. RESOURCE-002 — SEQKIT_RMDUP</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L518–583  
**Auto-fixable:** No

**Description:**  
Process 'SEQKIT_RMDUP' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

**Recommendation:**
```
Add a memory directive sized for the tool's peak usage:
    memory '8 GB'

For resilient pipelines, combine with an error strategy that increases memory on retry:
    errorStrategy 'retry'
    maxRetries 2
    memory { (8.GB * task.attempt).clamp(null, 32.GB) }
```

</details>

<details><summary>🔴 <strong>30. CONTAINER-001 — SEQKIT_SEQ</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L587–653  
**Auto-fixable:** Yes

**Description:**  
Process 'SEQKIT_SEQ' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟠 <strong>31. STORAGE-001 — SEQKIT_SEQ</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L587–653  
**Auto-fixable:** No

**Description:**  
Process 'SEQKIT_SEQ' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
/.
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>32. RESOURCE-001 — SEQKIT_SEQ</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L587–653  
**Auto-fixable:** No

**Description:**  
Process 'SEQKIT_SEQ' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

**Recommendation:**
```
Add a cpus directive appropriate for the tool's parallelism:
    cpus 4

Reference the allocation in the script block so the tool actually uses the provisioned cores:
    bwa mem -t ${task.cpus} ...

For workflows that need to scale, consider a dynamic expression:
    cpus { reads.size() > 5.GB ? 8 : 4 }
```

</details>

<details><summary>🟡 <strong>33. RESOURCE-002 — SEQKIT_SEQ</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L587–653  
**Auto-fixable:** No

**Description:**  
Process 'SEQKIT_SEQ' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

**Recommendation:**
```
Add a memory directive sized for the tool's peak usage:
    memory '8 GB'

For resilient pipelines, combine with an error strategy that increases memory on retry:
    errorStrategy 'retry'
    maxRetries 2
    memory { (8.GB * task.attempt).clamp(null, 32.GB) }
```

</details>

<details><summary>🔴 <strong>34. CONTAINER-001 — SEQKIT_STATS</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L657–692  
**Auto-fixable:** Yes

**Description:**  
Process 'SEQKIT_STATS' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟡 <strong>35. RESOURCE-001 — SEQKIT_STATS</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L657–692  
**Auto-fixable:** No

**Description:**  
Process 'SEQKIT_STATS' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

**Recommendation:**
```
Add a cpus directive appropriate for the tool's parallelism:
    cpus 4

Reference the allocation in the script block so the tool actually uses the provisioned cores:
    bwa mem -t ${task.cpus} ...

For workflows that need to scale, consider a dynamic expression:
    cpus { reads.size() > 5.GB ? 8 : 4 }
```

</details>

<details><summary>🟡 <strong>36. RESOURCE-002 — SEQKIT_STATS</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L657–692  
**Auto-fixable:** No

**Description:**  
Process 'SEQKIT_STATS' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

**Recommendation:**
```
Add a memory directive sized for the tool's peak usage:
    memory '8 GB'

For resilient pipelines, combine with an error strategy that increases memory on retry:
    errorStrategy 'retry'
    maxRetries 2
    memory { (8.GB * task.attempt).clamp(null, 32.GB) }
```

</details>

<details><summary>🔴 <strong>37. CONTAINER-001 — UNTAR</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L696–770  
**Auto-fixable:** Yes

**Description:**  
Process 'UNTAR' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟡 <strong>38. RESOURCE-001 — UNTAR</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L696–770  
**Auto-fixable:** No

**Description:**  
Process 'UNTAR' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

**Recommendation:**
```
Add a cpus directive appropriate for the tool's parallelism:
    cpus 4

Reference the allocation in the script block so the tool actually uses the provisioned cores:
    bwa mem -t ${task.cpus} ...

For workflows that need to scale, consider a dynamic expression:
    cpus { reads.size() > 5.GB ? 8 : 4 }
```

</details>

<details><summary>🟡 <strong>39. RESOURCE-002 — UNTAR</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L696–770  
**Auto-fixable:** No

**Description:**  
Process 'UNTAR' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

**Recommendation:**
```
Add a memory directive sized for the tool's peak usage:
    memory '8 GB'

For resilient pipelines, combine with an error strategy that increases memory on retry:
    errorStrategy 'retry'
    maxRetries 2
    memory { (8.GB * task.attempt).clamp(null, 32.GB) }
```

</details>

---

_Generated by [Workflow Clinic](https://github.com/electricdystopia/workflow-clinic) · schema `0.1.0` · [Report a false positive](https://github.com/electricdystopia/workflow-clinic/issues)_