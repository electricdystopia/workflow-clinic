<!-- WORKFLOW CLINIC ISSUE DRAFT -->
<!-- Title: [Workflow Clinic] 10 cloud-readiness gaps across 3 processes (score: 0%) -->

## 🏥 Workflow Clinic — Automated Cloud-Readiness Report

> **This issue was drafted automatically by [Workflow Clinic](https://github.com/electricdystopia/workflow-clinic), a GA4GH Cloud Work Stream tool for detecting and fixing cloud-readiness gaps in bioinformatics workflows.**
>
> Workflow: `main.nf`  
> Generated: 2026-03-31 19:53 UTC  
> Schema: `0.1.0`

### 🔴 Cloud Readiness Score: **0.00 / 1.00**

### Summary

| Severity | Count | Description |
|---|---|---|
| 🔴 **Critical** | 3 | Portability blockers — workflow cannot run on cloud WES |
| 🟠 **Major** | 1 | Significant gaps affecting reproducibility or correctness |
| 🟡 **Minor** | 6 | Resource hints missing — affects cost and scheduling efficiency |
| **Total** | **10** | |
| Auto-fixable | 3 | Can be fixed automatically with `workflow-clinic doctor` |

> 💡 **3 gap(s) can be fixed automatically.** Run `workflow-clinic doctor <path> --gap CONTAINER-001` to generate a patch and open a PR.

### Gaps

| # | Gap ID | Severity | Process | Category | Lines | Auto-fix |
|---|---|---|---|---|---|---|
| 1 | `CONTAINER-001` | 🔴 CRITICAL | `FASTQC` | containerization | L107–160 | ✅ |
| 2 | `STORAGE-001` | 🟠 MAJOR | `FASTQC` | storage | L107–160 | — |
| 3 | `RESOURCE-001` | 🟡 MINOR | `FASTQC` | resource_hints | L107–160 | — |
| 4 | `RESOURCE-002` | 🟡 MINOR | `FASTQC` | resource_hints | L107–160 | — |
| 5 | `CONTAINER-001` | 🔴 CRITICAL | `MULTIQC` | containerization | L164–218 | ✅ |
| 6 | `RESOURCE-001` | 🟡 MINOR | `MULTIQC` | resource_hints | L164–218 | — |
| 7 | `RESOURCE-002` | 🟡 MINOR | `MULTIQC` | resource_hints | L164–218 | — |
| 8 | `CONTAINER-001` | 🔴 CRITICAL | `SEQTK_TRIM` | containerization | L222–254 | ✅ |
| 9 | `RESOURCE-001` | 🟡 MINOR | `SEQTK_TRIM` | resource_hints | L222–254 | — |
| 10 | `RESOURCE-002` | 🟡 MINOR | `SEQTK_TRIM` | resource_hints | L222–254 | — |

### Detail

<details><summary>🔴 <strong>1. CONTAINER-001 — FASTQC</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L107–160  
**Auto-fixable:** Yes

**Description:**  
Process 'FASTQC' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟠 <strong>2. STORAGE-001 — FASTQC</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L107–160  
**Auto-fixable:** No

**Description:**  
Process 'FASTQC' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
//, //, // ... (3 more)
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>3. RESOURCE-001 — FASTQC</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L107–160  
**Auto-fixable:** No

**Description:**  
Process 'FASTQC' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>4. RESOURCE-002 — FASTQC</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L107–160  
**Auto-fixable:** No

**Description:**  
Process 'FASTQC' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>5. CONTAINER-001 — MULTIQC</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L164–218  
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

<details><summary>🟡 <strong>6. RESOURCE-001 — MULTIQC</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L164–218  
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

<details><summary>🟡 <strong>7. RESOURCE-002 — MULTIQC</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L164–218  
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

<details><summary>🔴 <strong>8. CONTAINER-001 — SEQTK_TRIM</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L222–254  
**Auto-fixable:** Yes

**Description:**  
Process 'SEQTK_TRIM' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟡 <strong>9. RESOURCE-001 — SEQTK_TRIM</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L222–254  
**Auto-fixable:** No

**Description:**  
Process 'SEQTK_TRIM' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>10. RESOURCE-002 — SEQTK_TRIM</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L222–254  
**Auto-fixable:** No

**Description:**  
Process 'SEQTK_TRIM' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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