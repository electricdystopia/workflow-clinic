<!-- WORKFLOW CLINIC ISSUE DRAFT -->
<!-- Title: [Workflow Clinic] 20 cloud-readiness gaps across 5 processes (score: 0%) -->

## 🏥 Workflow Clinic — Automated Cloud-Readiness Report

> **This issue was drafted automatically by [Workflow Clinic](https://github.com/electricdystopia/workflow-clinic), a GA4GH Cloud Work Stream tool for detecting and fixing cloud-readiness gaps in bioinformatics workflows.**
>
> Workflow: `main.nf`  
> Generated: 2026-03-31 19:23 UTC  
> Schema: `0.1.0`

### 🔴 Cloud Readiness Score: **0.00 / 1.00**

### Summary

| Severity | Count | Description |
|---|---|---|
| 🔴 **Critical** | 5 | Portability blockers — workflow cannot run on cloud WES |
| 🟠 **Major** | 5 | Significant gaps affecting reproducibility or correctness |
| 🟡 **Minor** | 10 | Resource hints missing — affects cost and scheduling efficiency |
| **Total** | **20** | |
| Auto-fixable | 5 | Can be fixed automatically with `workflow-clinic doctor` |

> 💡 **5 gap(s) can be fixed automatically.** Run `workflow-clinic doctor <path> --gap CONTAINER-001` to generate a patch and open a PR.

### Gaps

| # | Gap ID | Severity | Process | Category | Lines | Auto-fix |
|---|---|---|---|---|---|---|
| 1 | `CONTAINER-001` | 🔴 CRITICAL | `CELLPROFILER_ANALYSIS` | containerization | L119–192 | ✅ |
| 2 | `STORAGE-001` | 🟠 MAJOR | `CELLPROFILER_ANALYSIS` | storage | L119–192 | — |
| 3 | `RESOURCE-001` | 🟡 MINOR | `CELLPROFILER_ANALYSIS` | resource_hints | L119–192 | — |
| 4 | `RESOURCE-002` | 🟡 MINOR | `CELLPROFILER_ANALYSIS` | resource_hints | L119–192 | — |
| 5 | `CONTAINER-001` | 🔴 CRITICAL | `CELLPROFILER_ASSAYDEVELOPMENT` | containerization | L196–252 | ✅ |
| 6 | `STORAGE-001` | 🟠 MAJOR | `CELLPROFILER_ASSAYDEVELOPMENT` | storage | L196–252 | — |
| 7 | `RESOURCE-001` | 🟡 MINOR | `CELLPROFILER_ASSAYDEVELOPMENT` | resource_hints | L196–252 | — |
| 8 | `RESOURCE-002` | 🟡 MINOR | `CELLPROFILER_ASSAYDEVELOPMENT` | resource_hints | L196–252 | — |
| 9 | `CONTAINER-001` | 🔴 CRITICAL | `CELLPROFILER_ILLUMINATIONCORRECTION` | containerization | L256–311 | ✅ |
| 10 | `STORAGE-001` | 🟠 MAJOR | `CELLPROFILER_ILLUMINATIONCORRECTION` | storage | L256–311 | — |
| 11 | `RESOURCE-001` | 🟡 MINOR | `CELLPROFILER_ILLUMINATIONCORRECTION` | resource_hints | L256–311 | — |
| 12 | `RESOURCE-002` | 🟡 MINOR | `CELLPROFILER_ILLUMINATIONCORRECTION` | resource_hints | L256–311 | — |
| 13 | `CONTAINER-001` | 🔴 CRITICAL | `CYTOTABLE` | containerization | L315–354 | ✅ |
| 14 | `STORAGE-001` | 🟠 MAJOR | `CYTOTABLE` | storage | L315–354 | — |
| 15 | `RESOURCE-001` | 🟡 MINOR | `CYTOTABLE` | resource_hints | L315–354 | — |
| 16 | `RESOURCE-002` | 🟡 MINOR | `CYTOTABLE` | resource_hints | L315–354 | — |
| 17 | `CONTAINER-001` | 🔴 CRITICAL | `MULTIQC` | containerization | L358–420 | ✅ |
| 18 | `STORAGE-001` | 🟠 MAJOR | `MULTIQC` | storage | L358–420 | — |
| 19 | `RESOURCE-001` | 🟡 MINOR | `MULTIQC` | resource_hints | L358–420 | — |
| 20 | `RESOURCE-002` | 🟡 MINOR | `MULTIQC` | resource_hints | L358–420 | — |

### Detail

<details><summary>🔴 <strong>1. CONTAINER-001 — CELLPROFILER_ANALYSIS</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L119–192  
**Auto-fixable:** Yes

**Description:**  
Process 'CELLPROFILER_ANALYSIS' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟠 <strong>2. STORAGE-001 — CELLPROFILER_ANALYSIS</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L119–192  
**Auto-fixable:** No

**Description:**  
Process 'CELLPROFILER_ANALYSIS' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
//, //, // ... (7 more)
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>3. RESOURCE-001 — CELLPROFILER_ANALYSIS</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L119–192  
**Auto-fixable:** No

**Description:**  
Process 'CELLPROFILER_ANALYSIS' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>4. RESOURCE-002 — CELLPROFILER_ANALYSIS</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L119–192  
**Auto-fixable:** No

**Description:**  
Process 'CELLPROFILER_ANALYSIS' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>5. CONTAINER-001 — CELLPROFILER_ASSAYDEVELOPMENT</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L196–252  
**Auto-fixable:** Yes

**Description:**  
Process 'CELLPROFILER_ASSAYDEVELOPMENT' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟠 <strong>6. STORAGE-001 — CELLPROFILER_ASSAYDEVELOPMENT</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L196–252  
**Auto-fixable:** No

**Description:**  
Process 'CELLPROFILER_ASSAYDEVELOPMENT' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
/mock_segmentedimage.png, /mock_Image.csv
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>7. RESOURCE-001 — CELLPROFILER_ASSAYDEVELOPMENT</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L196–252  
**Auto-fixable:** No

**Description:**  
Process 'CELLPROFILER_ASSAYDEVELOPMENT' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>8. RESOURCE-002 — CELLPROFILER_ASSAYDEVELOPMENT</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L196–252  
**Auto-fixable:** No

**Description:**  
Process 'CELLPROFILER_ASSAYDEVELOPMENT' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>9. CONTAINER-001 — CELLPROFILER_ILLUMINATIONCORRECTION</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L256–311  
**Auto-fixable:** Yes

**Description:**  
Process 'CELLPROFILER_ILLUMINATIONCORRECTION' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟠 <strong>10. STORAGE-001 — CELLPROFILER_ILLUMINATIONCORRECTION</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L256–311  
**Auto-fixable:** No

**Description:**  
Process 'CELLPROFILER_ILLUMINATIONCORRECTION' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
/g, /images/
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>11. RESOURCE-001 — CELLPROFILER_ILLUMINATIONCORRECTION</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L256–311  
**Auto-fixable:** No

**Description:**  
Process 'CELLPROFILER_ILLUMINATIONCORRECTION' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>12. RESOURCE-002 — CELLPROFILER_ILLUMINATIONCORRECTION</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L256–311  
**Auto-fixable:** No

**Description:**  
Process 'CELLPROFILER_ILLUMINATIONCORRECTION' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>13. CONTAINER-001 — CYTOTABLE</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L315–354  
**Auto-fixable:** Yes

**Description:**  
Process 'CYTOTABLE' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟠 <strong>14. STORAGE-001 — CYTOTABLE</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L315–354  
**Auto-fixable:** No

**Description:**  
Process 'CYTOTABLE' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
/usr/bin/env
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>15. RESOURCE-001 — CYTOTABLE</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L315–354  
**Auto-fixable:** No

**Description:**  
Process 'CYTOTABLE' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>16. RESOURCE-002 — CYTOTABLE</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L315–354  
**Auto-fixable:** No

**Description:**  
Process 'CYTOTABLE' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>17. CONTAINER-001 — MULTIQC</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L358–420  
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

<details><summary>🟠 <strong>18. STORAGE-001 — MULTIQC</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L358–420  
**Auto-fixable:** No

**Description:**  
Process 'MULTIQC' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
/multiqc, //g
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>19. RESOURCE-001 — MULTIQC</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L358–420  
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

<details><summary>🟡 <strong>20. RESOURCE-002 — MULTIQC</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L358–420  
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

---

_Generated by [Workflow Clinic](https://github.com/electricdystopia/workflow-clinic) · schema `0.1.0` · [Report a false positive](https://github.com/electricdystopia/workflow-clinic/issues)_