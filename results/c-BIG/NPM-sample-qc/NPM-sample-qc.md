<!-- WORKFLOW CLINIC ISSUE DRAFT -->
<!-- Title: [Workflow Clinic] 36 cloud-readiness gaps across 11 processes (score: 0%) -->

## 🏥 Workflow Clinic — Automated Cloud-Readiness Report

> **This issue was drafted automatically by [Workflow Clinic](https://github.com/electricdystopia/workflow-clinic), a GA4GH Cloud Work Stream tool for detecting and fixing cloud-readiness gaps in bioinformatics workflows.**
>
> Workflow: `main.nf`  
> Generated: 2026-03-31 19:35 UTC  
> Schema: `0.1.0`

### 🔴 Cloud Readiness Score: **0.00 / 1.00**

### Summary

| Severity | Count | Description |
|---|---|---|
| 🔴 **Critical** | 11 | Portability blockers — workflow cannot run on cloud WES |
| 🟠 **Major** | 3 | Significant gaps affecting reproducibility or correctness |
| 🟡 **Minor** | 22 | Resource hints missing — affects cost and scheduling efficiency |
| **Total** | **36** | |
| Auto-fixable | 11 | Can be fixed automatically with `workflow-clinic doctor` |

> 💡 **11 gap(s) can be fixed automatically.** Run `workflow-clinic doctor <path> --gap CONTAINER-001` to generate a patch and open a PR.

### Gaps

| # | Gap ID | Severity | Process | Category | Lines | Auto-fix |
|---|---|---|---|---|---|---|
| 1 | `CONTAINER-001` | 🔴 CRITICAL | `picard_collect_multiple_metrics` | containerization | L313–347 | ✅ |
| 2 | `STORAGE-001` | 🟠 MAJOR | `picard_collect_multiple_metrics` | storage | L313–347 | — |
| 3 | `RESOURCE-001` | 🟡 MINOR | `picard_collect_multiple_metrics` | resource_hints | L313–347 | — |
| 4 | `RESOURCE-002` | 🟡 MINOR | `picard_collect_multiple_metrics` | resource_hints | L313–347 | — |
| 5 | `CONTAINER-001` | 🔴 CRITICAL | `picard_collect_variant_calling_metrics_vcf` | containerization | L351–369 | ✅ |
| 6 | `RESOURCE-001` | 🟡 MINOR | `picard_collect_variant_calling_metrics_vcf` | resource_hints | L351–369 | — |
| 7 | `RESOURCE-002` | 🟡 MINOR | `picard_collect_variant_calling_metrics_vcf` | resource_hints | L351–369 | — |
| 8 | `CONTAINER-001` | 🔴 CRITICAL | `picard_collect_wgs_metrics` | containerization | L372–408 | ✅ |
| 9 | `RESOURCE-001` | 🟡 MINOR | `picard_collect_wgs_metrics` | resource_hints | L372–408 | — |
| 10 | `RESOURCE-002` | 🟡 MINOR | `picard_collect_wgs_metrics` | resource_hints | L372–408 | — |
| 11 | `CONTAINER-001` | 🔴 CRITICAL | `bcftools_stats` | containerization | L412–428 | ✅ |
| 12 | `RESOURCE-001` | 🟡 MINOR | `bcftools_stats` | resource_hints | L412–428 | — |
| 13 | `RESOURCE-002` | 🟡 MINOR | `bcftools_stats` | resource_hints | L412–428 | — |
| 14 | `CONTAINER-001` | 🔴 CRITICAL | `compile_aln_vcf` | containerization | L431–452 | ✅ |
| 15 | `RESOURCE-001` | 🟡 MINOR | `compile_aln_vcf` | resource_hints | L431–452 | — |
| 16 | `RESOURCE-002` | 🟡 MINOR | `compile_aln_vcf` | resource_hints | L431–452 | — |
| 17 | `CONTAINER-001` | 🔴 CRITICAL | `count_aln` | containerization | L456–475 | ✅ |
| 18 | `RESOURCE-001` | 🟡 MINOR | `count_aln` | resource_hints | L456–475 | — |
| 19 | `RESOURCE-002` | 🟡 MINOR | `count_aln` | resource_hints | L456–475 | — |
| 20 | `CONTAINER-001` | 🔴 CRITICAL | `count_variants` | containerization | L479–500 | ✅ |
| 21 | `RESOURCE-001` | 🟡 MINOR | `count_variants` | resource_hints | L479–500 | — |
| 22 | `RESOURCE-002` | 🟡 MINOR | `count_variants` | resource_hints | L479–500 | — |
| 23 | `CONTAINER-001` | 🔴 CRITICAL | `metric_aln` | containerization | L504–517 | ✅ |
| 24 | `RESOURCE-001` | 🟡 MINOR | `metric_aln` | resource_hints | L504–517 | — |
| 25 | `RESOURCE-002` | 🟡 MINOR | `metric_aln` | resource_hints | L504–517 | — |
| 26 | `CONTAINER-001` | 🔴 CRITICAL | `metric_variants` | containerization | L521–534 | ✅ |
| 27 | `RESOURCE-001` | 🟡 MINOR | `metric_variants` | resource_hints | L521–534 | — |
| 28 | `RESOURCE-002` | 🟡 MINOR | `metric_variants` | resource_hints | L521–534 | — |
| 29 | `CONTAINER-001` | 🔴 CRITICAL | `samtools_stats` | containerization | L538–578 | ✅ |
| 30 | `STORAGE-001` | 🟠 MAJOR | `samtools_stats` | storage | L538–578 | — |
| 31 | `RESOURCE-001` | 🟡 MINOR | `samtools_stats` | resource_hints | L538–578 | — |
| 32 | `RESOURCE-002` | 🟡 MINOR | `samtools_stats` | resource_hints | L538–578 | — |
| 33 | `CONTAINER-001` | 🔴 CRITICAL | `verifybamid2` | containerization | L582–611 | ✅ |
| 34 | `STORAGE-001` | 🟠 MAJOR | `verifybamid2` | storage | L582–611 | — |
| 35 | `RESOURCE-001` | 🟡 MINOR | `verifybamid2` | resource_hints | L582–611 | — |
| 36 | `RESOURCE-002` | 🟡 MINOR | `verifybamid2` | resource_hints | L582–611 | — |

### Detail

<details><summary>🔴 <strong>1. CONTAINER-001 — picard_collect_multiple_metrics</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L313–347  
**Auto-fixable:** Yes

**Description:**  
Process 'picard_collect_multiple_metrics' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟠 <strong>2. STORAGE-001 — picard_collect_multiple_metrics</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L313–347  
**Auto-fixable:** No

**Description:**  
Process 'picard_collect_multiple_metrics' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
/R
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>3. RESOURCE-001 — picard_collect_multiple_metrics</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L313–347  
**Auto-fixable:** No

**Description:**  
Process 'picard_collect_multiple_metrics' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>4. RESOURCE-002 — picard_collect_multiple_metrics</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L313–347  
**Auto-fixable:** No

**Description:**  
Process 'picard_collect_multiple_metrics' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>5. CONTAINER-001 — picard_collect_variant_calling_metrics_vcf</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L351–369  
**Auto-fixable:** Yes

**Description:**  
Process 'picard_collect_variant_calling_metrics_vcf' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟡 <strong>6. RESOURCE-001 — picard_collect_variant_calling_metrics_vcf</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L351–369  
**Auto-fixable:** No

**Description:**  
Process 'picard_collect_variant_calling_metrics_vcf' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>7. RESOURCE-002 — picard_collect_variant_calling_metrics_vcf</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L351–369  
**Auto-fixable:** No

**Description:**  
Process 'picard_collect_variant_calling_metrics_vcf' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>8. CONTAINER-001 — picard_collect_wgs_metrics</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L372–408  
**Auto-fixable:** Yes

**Description:**  
Process 'picard_collect_wgs_metrics' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟡 <strong>9. RESOURCE-001 — picard_collect_wgs_metrics</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L372–408  
**Auto-fixable:** No

**Description:**  
Process 'picard_collect_wgs_metrics' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>10. RESOURCE-002 — picard_collect_wgs_metrics</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L372–408  
**Auto-fixable:** No

**Description:**  
Process 'picard_collect_wgs_metrics' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>11. CONTAINER-001 — bcftools_stats</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L412–428  
**Auto-fixable:** Yes

**Description:**  
Process 'bcftools_stats' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟡 <strong>12. RESOURCE-001 — bcftools_stats</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L412–428  
**Auto-fixable:** No

**Description:**  
Process 'bcftools_stats' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>13. RESOURCE-002 — bcftools_stats</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L412–428  
**Auto-fixable:** No

**Description:**  
Process 'bcftools_stats' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>14. CONTAINER-001 — compile_aln_vcf</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L431–452  
**Auto-fixable:** Yes

**Description:**  
Process 'compile_aln_vcf' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟡 <strong>15. RESOURCE-001 — compile_aln_vcf</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L431–452  
**Auto-fixable:** No

**Description:**  
Process 'compile_aln_vcf' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>16. RESOURCE-002 — compile_aln_vcf</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L431–452  
**Auto-fixable:** No

**Description:**  
Process 'compile_aln_vcf' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>17. CONTAINER-001 — count_aln</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L456–475  
**Auto-fixable:** Yes

**Description:**  
Process 'count_aln' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟡 <strong>18. RESOURCE-001 — count_aln</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L456–475  
**Auto-fixable:** No

**Description:**  
Process 'count_aln' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>19. RESOURCE-002 — count_aln</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L456–475  
**Auto-fixable:** No

**Description:**  
Process 'count_aln' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>20. CONTAINER-001 — count_variants</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L479–500  
**Auto-fixable:** Yes

**Description:**  
Process 'count_variants' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟡 <strong>21. RESOURCE-001 — count_variants</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L479–500  
**Auto-fixable:** No

**Description:**  
Process 'count_variants' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>22. RESOURCE-002 — count_variants</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L479–500  
**Auto-fixable:** No

**Description:**  
Process 'count_variants' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>23. CONTAINER-001 — metric_aln</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L504–517  
**Auto-fixable:** Yes

**Description:**  
Process 'metric_aln' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟡 <strong>24. RESOURCE-001 — metric_aln</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L504–517  
**Auto-fixable:** No

**Description:**  
Process 'metric_aln' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>25. RESOURCE-002 — metric_aln</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L504–517  
**Auto-fixable:** No

**Description:**  
Process 'metric_aln' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>26. CONTAINER-001 — metric_variants</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L521–534  
**Auto-fixable:** Yes

**Description:**  
Process 'metric_variants' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟡 <strong>27. RESOURCE-001 — metric_variants</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L521–534  
**Auto-fixable:** No

**Description:**  
Process 'metric_variants' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>28. RESOURCE-002 — metric_variants</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L521–534  
**Auto-fixable:** No

**Description:**  
Process 'metric_variants' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>29. CONTAINER-001 — samtools_stats</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L538–578  
**Auto-fixable:** Yes

**Description:**  
Process 'samtools_stats' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟠 <strong>30. STORAGE-001 — samtools_stats</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L538–578  
**Auto-fixable:** No

**Description:**  
Process 'samtools_stats' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
/--reference
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>31. RESOURCE-001 — samtools_stats</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L538–578  
**Auto-fixable:** No

**Description:**  
Process 'samtools_stats' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>32. RESOURCE-002 — samtools_stats</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L538–578  
**Auto-fixable:** No

**Description:**  
Process 'samtools_stats' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>33. CONTAINER-001 — verifybamid2</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L582–611  
**Auto-fixable:** Yes

**Description:**  
Process 'verifybamid2' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟠 <strong>34. STORAGE-001 — verifybamid2</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L582–611  
**Auto-fixable:** No

**Description:**  
Process 'verifybamid2' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
/--Reference
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>35. RESOURCE-001 — verifybamid2</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L582–611  
**Auto-fixable:** No

**Description:**  
Process 'verifybamid2' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>36. RESOURCE-002 — verifybamid2</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L582–611  
**Auto-fixable:** No

**Description:**  
Process 'verifybamid2' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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