<!-- WORKFLOW CLINIC ISSUE DRAFT -->
<!-- Title: [Workflow Clinic] 9 cloud-readiness gaps across 2 processes (score: 8%) -->

## 🏥 Workflow Clinic — Automated Cloud-Readiness Report

> **This issue was drafted automatically by [Workflow Clinic](https://github.com/electricdystopia/workflow-clinic), a GA4GH Cloud Work Stream tool for detecting and fixing cloud-readiness gaps in bioinformatics workflows.**
>
> Workflow: `tests/fixtures/nextflow/broken.nf`  
> Generated: 2026-03-27 15:25 UTC  
> Schema: `0.1.0`

### 🔴 Cloud Readiness Score: **0.08 / 1.00**

### Summary

| Severity | Count | Description |
|---|---|---|
| 🔴 **Critical** | 2 | Portability blockers — workflow cannot run on cloud WES |
| 🟠 **Major** | 3 | Significant gaps affecting reproducibility or correctness |
| 🟡 **Minor** | 4 | Resource hints missing — affects cost and scheduling efficiency |
| **Total** | **9** | |
| Auto-fixable | 2 | Can be fixed automatically with `workflow-clinic doctor` |

> 💡 **2 gap(s) can be fixed automatically.** Run `workflow-clinic doctor <path> --gap CONTAINER-001` to generate a patch and open a PR.

### Gaps

| # | Gap ID | Severity | Process | Category | Lines | Auto-fix |
|---|---|---|---|---|---|---|
| 1 | `CONTAINER-001` | 🔴 CRITICAL | `ALIGN` | containerization | L1–11 | ✅ |
| 2 | `STORAGE-001` | 🟠 MAJOR | `ALIGN` | storage | L1–11 | — |
| 3 | `IO-001` | 🟠 MAJOR | `ALIGN` | io_declaration | L1–11 | — |
| 4 | `RESOURCE-001` | 🟡 MINOR | `ALIGN` | resource_hints | L1–11 | — |
| 5 | `RESOURCE-002` | 🟡 MINOR | `ALIGN` | resource_hints | L1–11 | — |
| 6 | `CONTAINER-001` | 🔴 CRITICAL | `CALL_VARIANTS` | containerization | L13–23 | ✅ |
| 7 | `IO-001` | 🟠 MAJOR | `CALL_VARIANTS` | io_declaration | L13–23 | — |
| 8 | `RESOURCE-001` | 🟡 MINOR | `CALL_VARIANTS` | resource_hints | L13–23 | — |
| 9 | `RESOURCE-002` | 🟡 MINOR | `CALL_VARIANTS` | resource_hints | L13–23 | — |

### Detail

<details><summary>🔴 <strong>1. CONTAINER-001 — ALIGN</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `tests/fixtures/nextflow/broken.nf` L1–11  
**Auto-fixable:** Yes

**Description:**  
Process 'ALIGN' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'
```

</details>

<details><summary>🟠 <strong>2. STORAGE-001 — ALIGN</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `tests/fixtures/nextflow/broken.nf` L1–11  
**Auto-fixable:** No

**Description:**  
Process 'ALIGN' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
/data/ref/hg38.fa, /scratch/aligned.bam
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟠 <strong>3. IO-001 — ALIGN</strong> (MAJOR)</summary>

**Category:** `io_declaration`  
**Location:** `tests/fixtures/nextflow/broken.nf` L1–11  
**Auto-fixable:** No

**Description:**  
Process 'ALIGN' has no output declaration. Workflow engines cannot chain this process to downstream steps or track its results without explicit outputs.

**Recommendation:**
```
Add an output: block declaring all files this process produces, e.g.:
    output:
        path "*.bam"
```

</details>

<details><summary>🟡 <strong>4. RESOURCE-001 — ALIGN</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `tests/fixtures/nextflow/broken.nf` L1–11  
**Auto-fixable:** No

**Description:**  
Process 'ALIGN' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>5. RESOURCE-002 — ALIGN</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `tests/fixtures/nextflow/broken.nf` L1–11  
**Auto-fixable:** No

**Description:**  
Process 'ALIGN' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>6. CONTAINER-001 — CALL_VARIANTS</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `tests/fixtures/nextflow/broken.nf` L13–23  
**Auto-fixable:** Yes

**Description:**  
Process 'CALL_VARIANTS' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'
```

</details>

<details><summary>🟠 <strong>7. IO-001 — CALL_VARIANTS</strong> (MAJOR)</summary>

**Category:** `io_declaration`  
**Location:** `tests/fixtures/nextflow/broken.nf` L13–23  
**Auto-fixable:** No

**Description:**  
Process 'CALL_VARIANTS' has no output declaration. Workflow engines cannot chain this process to downstream steps or track its results without explicit outputs.

**Recommendation:**
```
Add an output: block declaring all files this process produces, e.g.:
    output:
        path "*.bam"
```

</details>

<details><summary>🟡 <strong>8. RESOURCE-001 — CALL_VARIANTS</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `tests/fixtures/nextflow/broken.nf` L13–23  
**Auto-fixable:** No

**Description:**  
Process 'CALL_VARIANTS' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>9. RESOURCE-002 — CALL_VARIANTS</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `tests/fixtures/nextflow/broken.nf` L13–23  
**Auto-fixable:** No

**Description:**  
Process 'CALL_VARIANTS' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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