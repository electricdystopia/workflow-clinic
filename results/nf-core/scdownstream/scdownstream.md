<!-- WORKFLOW CLINIC ISSUE DRAFT -->
<!-- Title: [Workflow Clinic] 168 cloud-readiness gaps across 56 processes (score: 0%) -->

## 🏥 Workflow Clinic — Automated Cloud-Readiness Report

> **This issue was drafted automatically by [Workflow Clinic](https://github.com/electricdystopia/workflow-clinic), a GA4GH Cloud Work Stream tool for detecting and fixing cloud-readiness gaps in bioinformatics workflows.**
>
> Workflow: `main.nf`  
> Generated: 2026-03-31 19:31 UTC  
> Schema: `0.1.0`

### 🔴 Cloud Readiness Score: **0.00 / 1.00**

### Summary

| Severity | Count | Description |
|---|---|---|
| 🔴 **Critical** | 55 | Portability blockers — workflow cannot run on cloud WES |
| 🟠 **Major** | 1 | Significant gaps affecting reproducibility or correctness |
| 🟡 **Minor** | 112 | Resource hints missing — affects cost and scheduling efficiency |
| **Total** | **168** | |
| Auto-fixable | 55 | Can be fixed automatically with `workflow-clinic doctor` |

> 💡 **55 gap(s) can be fixed automatically.** Run `workflow-clinic doctor <path> --gap CONTAINER-001` to generate a patch and open a PR.

### Gaps

| # | Gap ID | Severity | Process | Category | Lines | Auto-fix |
|---|---|---|---|---|---|---|
| 1 | `CONTAINER-001` | 🔴 CRITICAL | `ADATA_ENTROPY` | containerization | L239–281 | ✅ |
| 2 | `RESOURCE-001` | 🟡 MINOR | `ADATA_ENTROPY` | resource_hints | L239–281 | — |
| 3 | `RESOURCE-002` | 🟡 MINOR | `ADATA_ENTROPY` | resource_hints | L239–281 | — |
| 4 | `CONTAINER-001` | 🔴 CRITICAL | `ADATA_EXTEND` | containerization | L285–325 | ✅ |
| 5 | `RESOURCE-001` | 🟡 MINOR | `ADATA_EXTEND` | resource_hints | L285–325 | — |
| 6 | `RESOURCE-002` | 🟡 MINOR | `ADATA_EXTEND` | resource_hints | L285–325 | — |
| 7 | `CONTAINER-001` | 🔴 CRITICAL | `ADATA_MERGE` | containerization | L329–367 | ✅ |
| 8 | `RESOURCE-001` | 🟡 MINOR | `ADATA_MERGE` | resource_hints | L329–367 | — |
| 9 | `RESOURCE-002` | 🟡 MINOR | `ADATA_MERGE` | resource_hints | L329–367 | — |
| 10 | `CONTAINER-001` | 🔴 CRITICAL | `ADATA_MERGEEMBEDDINGS` | containerization | L371–404 | ✅ |
| 11 | `RESOURCE-001` | 🟡 MINOR | `ADATA_MERGEEMBEDDINGS` | resource_hints | L371–404 | — |
| 12 | `RESOURCE-002` | 🟡 MINOR | `ADATA_MERGEEMBEDDINGS` | resource_hints | L371–404 | — |
| 13 | `CONTAINER-001` | 🔴 CRITICAL | `ADATA_MYGENE` | containerization | L408–442 | ✅ |
| 14 | `RESOURCE-001` | 🟡 MINOR | `ADATA_MYGENE` | resource_hints | L408–442 | — |
| 15 | `RESOURCE-002` | 🟡 MINOR | `ADATA_MYGENE` | resource_hints | L408–442 | — |
| 16 | `CONTAINER-001` | 🔴 CRITICAL | `ADATA_PREPCELLXGENE` | containerization | L446–481 | ✅ |
| 17 | `RESOURCE-001` | 🟡 MINOR | `ADATA_PREPCELLXGENE` | resource_hints | L446–481 | — |
| 18 | `RESOURCE-002` | 🟡 MINOR | `ADATA_PREPCELLXGENE` | resource_hints | L446–481 | — |
| 19 | `CONTAINER-001` | 🔴 CRITICAL | `ADATA_READCSV` | containerization | L485–514 | ✅ |
| 20 | `RESOURCE-001` | 🟡 MINOR | `ADATA_READCSV` | resource_hints | L485–514 | — |
| 21 | `RESOURCE-002` | 🟡 MINOR | `ADATA_READCSV` | resource_hints | L485–514 | — |
| 22 | `CONTAINER-001` | 🔴 CRITICAL | `ADATA_READRDS` | containerization | L518–544 | ✅ |
| 23 | `RESOURCE-001` | 🟡 MINOR | `ADATA_READRDS` | resource_hints | L518–544 | — |
| 24 | `RESOURCE-002` | 🟡 MINOR | `ADATA_READRDS` | resource_hints | L518–544 | — |
| 25 | `CONTAINER-001` | 🔴 CRITICAL | `ADATA_SETINDEX` | containerization | L548–586 | ✅ |
| 26 | `RESOURCE-001` | 🟡 MINOR | `ADATA_SETINDEX` | resource_hints | L548–586 | — |
| 27 | `RESOURCE-002` | 🟡 MINOR | `ADATA_SETINDEX` | resource_hints | L548–586 | — |
| 28 | `CONTAINER-001` | 🔴 CRITICAL | `ADATA_SPLITCOL` | containerization | L590–621 | ✅ |
| 29 | `RESOURCE-001` | 🟡 MINOR | `ADATA_SPLITCOL` | resource_hints | L590–621 | — |
| 30 | `RESOURCE-002` | 🟡 MINOR | `ADATA_SPLITCOL` | resource_hints | L590–621 | — |
| 31 | `CONTAINER-001` | 🔴 CRITICAL | `ADATA_SPLITEMBEDDINGS` | containerization | L625–655 | ✅ |
| 32 | `RESOURCE-001` | 🟡 MINOR | `ADATA_SPLITEMBEDDINGS` | resource_hints | L625–655 | — |
| 33 | `RESOURCE-002` | 🟡 MINOR | `ADATA_SPLITEMBEDDINGS` | resource_hints | L625–655 | — |
| 34 | `CONTAINER-001` | 🔴 CRITICAL | `ADATA_TORDS` | containerization | L659–690 | ✅ |
| 35 | `RESOURCE-001` | 🟡 MINOR | `ADATA_TORDS` | resource_hints | L659–690 | — |
| 36 | `RESOURCE-002` | 🟡 MINOR | `ADATA_TORDS` | resource_hints | L659–690 | — |
| 37 | `CONTAINER-001` | 🔴 CRITICAL | `ADATA_UNIFY` | containerization | L694–731 | ✅ |
| 38 | `RESOURCE-001` | 🟡 MINOR | `ADATA_UNIFY` | resource_hints | L694–731 | — |
| 39 | `RESOURCE-002` | 🟡 MINOR | `ADATA_UNIFY` | resource_hints | L694–731 | — |
| 40 | `CONTAINER-001` | 🔴 CRITICAL | `ADATA_UPSETGENES` | containerization | L735–766 | ✅ |
| 41 | `RESOURCE-001` | 🟡 MINOR | `ADATA_UPSETGENES` | resource_hints | L735–766 | — |
| 42 | `RESOURCE-002` | 🟡 MINOR | `ADATA_UPSETGENES` | resource_hints | L735–766 | — |
| 43 | `CONTAINER-001` | 🔴 CRITICAL | `CELDA_DECONTX` | containerization | L770–802 | ✅ |
| 44 | `RESOURCE-001` | 🟡 MINOR | `CELDA_DECONTX` | resource_hints | L770–802 | — |
| 45 | `RESOURCE-002` | 🟡 MINOR | `CELDA_DECONTX` | resource_hints | L770–802 | — |
| 46 | `CONTAINER-001` | 🔴 CRITICAL | `CELLDEX_FETCHREFERENCE` | containerization | L806–836 | ✅ |
| 47 | `RESOURCE-001` | 🟡 MINOR | `CELLDEX_FETCHREFERENCE` | resource_hints | L806–836 | — |
| 48 | `RESOURCE-002` | 🟡 MINOR | `CELLDEX_FETCHREFERENCE` | resource_hints | L806–836 | — |
| 49 | `CONTAINER-001` | 🔴 CRITICAL | `CELLTYPES_CELLTYPIST` | containerization | L840–872 | ✅ |
| 50 | `RESOURCE-001` | 🟡 MINOR | `CELLTYPES_CELLTYPIST` | resource_hints | L840–872 | — |
| 51 | `RESOURCE-002` | 🟡 MINOR | `CELLTYPES_CELLTYPIST` | resource_hints | L840–872 | — |
| 52 | `CONTAINER-001` | 🔴 CRITICAL | `CELLTYPES_SINGLER` | containerization | L876–911 | ✅ |
| 53 | `RESOURCE-001` | 🟡 MINOR | `CELLTYPES_SINGLER` | resource_hints | L876–911 | — |
| 54 | `RESOURCE-002` | 🟡 MINOR | `CELLTYPES_SINGLER` | resource_hints | L876–911 | — |
| 55 | `CONTAINER-001` | 🔴 CRITICAL | `CUSTOM_COLLECTSIZES` | containerization | L915–943 | ✅ |
| 56 | `RESOURCE-001` | 🟡 MINOR | `CUSTOM_COLLECTSIZES` | resource_hints | L915–943 | — |
| 57 | `RESOURCE-002` | 🟡 MINOR | `CUSTOM_COLLECTSIZES` | resource_hints | L915–943 | — |
| 58 | `CONTAINER-001` | 🔴 CRITICAL | `DOUBLET_REMOVAL` | containerization | L947–979 | ✅ |
| 59 | `RESOURCE-001` | 🟡 MINOR | `DOUBLET_REMOVAL` | resource_hints | L947–979 | — |
| 60 | `RESOURCE-002` | 🟡 MINOR | `DOUBLET_REMOVAL` | resource_hints | L947–979 | — |
| 61 | `RESOURCE-001` | 🟡 MINOR | `SCDS` | resource_hints | L983–1011 | — |
| 62 | `RESOURCE-002` | 🟡 MINOR | `SCDS` | resource_hints | L983–1011 | — |
| 63 | `CONTAINER-001` | 🔴 CRITICAL | `HUGOUNIFIER_APPLY` | containerization | L1015–1048 | ✅ |
| 64 | `RESOURCE-001` | 🟡 MINOR | `HUGOUNIFIER_APPLY` | resource_hints | L1015–1048 | — |
| 65 | `RESOURCE-002` | 🟡 MINOR | `HUGOUNIFIER_APPLY` | resource_hints | L1015–1048 | — |
| 66 | `CONTAINER-001` | 🔴 CRITICAL | `HUGOUNIFIER_GET` | containerization | L1052–1090 | ✅ |
| 67 | `RESOURCE-001` | 🟡 MINOR | `HUGOUNIFIER_GET` | resource_hints | L1052–1090 | — |
| 68 | `RESOURCE-002` | 🟡 MINOR | `HUGOUNIFIER_GET` | resource_hints | L1052–1090 | — |
| 69 | `CONTAINER-001` | 🔴 CRITICAL | `LIANA_RANKAGGREGATE` | containerization | L1094–1127 | ✅ |
| 70 | `RESOURCE-001` | 🟡 MINOR | `LIANA_RANKAGGREGATE` | resource_hints | L1094–1127 | — |
| 71 | `RESOURCE-002` | 🟡 MINOR | `LIANA_RANKAGGREGATE` | resource_hints | L1094–1127 | — |
| 72 | `CONTAINER-001` | 🔴 CRITICAL | `SCANPY_BBKNN` | containerization | L1131–1162 | ✅ |
| 73 | `RESOURCE-001` | 🟡 MINOR | `SCANPY_BBKNN` | resource_hints | L1131–1162 | — |
| 74 | `RESOURCE-002` | 🟡 MINOR | `SCANPY_BBKNN` | resource_hints | L1131–1162 | — |
| 75 | `CONTAINER-001` | 🔴 CRITICAL | `SCANPY_CELLCYCLE` | containerization | L1166–1203 | ✅ |
| 76 | `RESOURCE-001` | 🟡 MINOR | `SCANPY_CELLCYCLE` | resource_hints | L1166–1203 | — |
| 77 | `RESOURCE-002` | 🟡 MINOR | `SCANPY_CELLCYCLE` | resource_hints | L1166–1203 | — |
| 78 | `CONTAINER-001` | 🔴 CRITICAL | `SCANPY_COMBAT` | containerization | L1207–1242 | ✅ |
| 79 | `RESOURCE-001` | 🟡 MINOR | `SCANPY_COMBAT` | resource_hints | L1207–1242 | — |
| 80 | `RESOURCE-002` | 🟡 MINOR | `SCANPY_COMBAT` | resource_hints | L1207–1242 | — |
| 81 | `CONTAINER-001` | 🔴 CRITICAL | `SCANPY_FILTER` | containerization | L1246–1285 | ✅ |
| 82 | `RESOURCE-001` | 🟡 MINOR | `SCANPY_FILTER` | resource_hints | L1246–1285 | — |
| 83 | `RESOURCE-002` | 🟡 MINOR | `SCANPY_FILTER` | resource_hints | L1246–1285 | — |
| 84 | `CONTAINER-001` | 🔴 CRITICAL | `SCANPY_HARMONY` | containerization | L1289–1325 | ✅ |
| 85 | `RESOURCE-001` | 🟡 MINOR | `SCANPY_HARMONY` | resource_hints | L1289–1325 | — |
| 86 | `RESOURCE-002` | 🟡 MINOR | `SCANPY_HARMONY` | resource_hints | L1289–1325 | — |
| 87 | `CONTAINER-001` | 🔴 CRITICAL | `SCANPY_HVGS` | containerization | L1329–1363 | ✅ |
| 88 | `RESOURCE-001` | 🟡 MINOR | `SCANPY_HVGS` | resource_hints | L1329–1363 | — |
| 89 | `RESOURCE-002` | 🟡 MINOR | `SCANPY_HVGS` | resource_hints | L1329–1363 | — |
| 90 | `CONTAINER-001` | 🔴 CRITICAL | `SCANPY_LEIDEN` | containerization | L1367–1408 | ✅ |
| 91 | `RESOURCE-001` | 🟡 MINOR | `SCANPY_LEIDEN` | resource_hints | L1367–1408 | — |
| 92 | `RESOURCE-002` | 🟡 MINOR | `SCANPY_LEIDEN` | resource_hints | L1367–1408 | — |
| 93 | `CONTAINER-001` | 🔴 CRITICAL | `SCANPY_NEIGHBORS` | containerization | L1412–1443 | ✅ |
| 94 | `RESOURCE-001` | 🟡 MINOR | `SCANPY_NEIGHBORS` | resource_hints | L1412–1443 | — |
| 95 | `RESOURCE-002` | 🟡 MINOR | `SCANPY_NEIGHBORS` | resource_hints | L1412–1443 | — |
| 96 | `CONTAINER-001` | 🔴 CRITICAL | `SCANPY_PAGA` | containerization | L1447–1485 | ✅ |
| 97 | `RESOURCE-001` | 🟡 MINOR | `SCANPY_PAGA` | resource_hints | L1447–1485 | — |
| 98 | `RESOURCE-002` | 🟡 MINOR | `SCANPY_PAGA` | resource_hints | L1447–1485 | — |
| 99 | `CONTAINER-001` | 🔴 CRITICAL | `SCANPY_PCA` | containerization | L1489–1535 | ✅ |
| 100 | `RESOURCE-001` | 🟡 MINOR | `SCANPY_PCA` | resource_hints | L1489–1535 | — |
| 101 | `RESOURCE-002` | 🟡 MINOR | `SCANPY_PCA` | resource_hints | L1489–1535 | — |
| 102 | `CONTAINER-001` | 🔴 CRITICAL | `SCANPY_PLOTQC` | containerization | L1539–1574 | ✅ |
| 103 | `RESOURCE-001` | 🟡 MINOR | `SCANPY_PLOTQC` | resource_hints | L1539–1574 | — |
| 104 | `RESOURCE-002` | 🟡 MINOR | `SCANPY_PLOTQC` | resource_hints | L1539–1574 | — |
| 105 | `CONTAINER-001` | 🔴 CRITICAL | `SCANPY_RANKGENESGROUPS` | containerization | L1578–1617 | ✅ |
| 106 | `RESOURCE-001` | 🟡 MINOR | `SCANPY_RANKGENESGROUPS` | resource_hints | L1578–1617 | — |
| 107 | `RESOURCE-002` | 🟡 MINOR | `SCANPY_RANKGENESGROUPS` | resource_hints | L1578–1617 | — |
| 108 | `CONTAINER-001` | 🔴 CRITICAL | `SCANPY_READH5` | containerization | L1621–1650 | ✅ |
| 109 | `RESOURCE-001` | 🟡 MINOR | `SCANPY_READH5` | resource_hints | L1621–1650 | — |
| 110 | `RESOURCE-002` | 🟡 MINOR | `SCANPY_READH5` | resource_hints | L1621–1650 | — |
| 111 | `CONTAINER-001` | 🔴 CRITICAL | `SCANPY_SAMPLE` | containerization | L1654–1688 | ✅ |
| 112 | `RESOURCE-001` | 🟡 MINOR | `SCANPY_SAMPLE` | resource_hints | L1654–1688 | — |
| 113 | `RESOURCE-002` | 🟡 MINOR | `SCANPY_SAMPLE` | resource_hints | L1654–1688 | — |
| 114 | `CONTAINER-001` | 🔴 CRITICAL | `SCANPY_UMAP` | containerization | L1692–1726 | ✅ |
| 115 | `RESOURCE-001` | 🟡 MINOR | `SCANPY_UMAP` | resource_hints | L1692–1726 | — |
| 116 | `RESOURCE-002` | 🟡 MINOR | `SCANPY_UMAP` | resource_hints | L1692–1726 | — |
| 117 | `CONTAINER-001` | 🔴 CRITICAL | `SCIMILARITY_ANNOTATE` | containerization | L1730–1767 | ✅ |
| 118 | `RESOURCE-001` | 🟡 MINOR | `SCIMILARITY_ANNOTATE` | resource_hints | L1730–1767 | — |
| 119 | `RESOURCE-002` | 🟡 MINOR | `SCIMILARITY_ANNOTATE` | resource_hints | L1730–1767 | — |
| 120 | `CONTAINER-001` | 🔴 CRITICAL | `SCIMILARITY_EMBED` | containerization | L1771–1804 | ✅ |
| 121 | `RESOURCE-001` | 🟡 MINOR | `SCIMILARITY_EMBED` | resource_hints | L1771–1804 | — |
| 122 | `RESOURCE-002` | 🟡 MINOR | `SCIMILARITY_EMBED` | resource_hints | L1771–1804 | — |
| 123 | `CONTAINER-001` | 🔴 CRITICAL | `SCIMILARITY_PSEUDOBULK` | containerization | L1808–1845 | ✅ |
| 124 | `RESOURCE-001` | 🟡 MINOR | `SCIMILARITY_PSEUDOBULK` | resource_hints | L1808–1845 | — |
| 125 | `RESOURCE-002` | 🟡 MINOR | `SCIMILARITY_PSEUDOBULK` | resource_hints | L1808–1845 | — |
| 126 | `CONTAINER-001` | 🔴 CRITICAL | `SCVITOOLS_SCANVI` | containerization | L1849–1903 | ✅ |
| 127 | `RESOURCE-001` | 🟡 MINOR | `SCVITOOLS_SCANVI` | resource_hints | L1849–1903 | — |
| 128 | `RESOURCE-002` | 🟡 MINOR | `SCVITOOLS_SCANVI` | resource_hints | L1849–1903 | — |
| 129 | `CONTAINER-001` | 🔴 CRITICAL | `SCVITOOLS_SCVI` | containerization | L1907–1958 | ✅ |
| 130 | `RESOURCE-001` | 🟡 MINOR | `SCVITOOLS_SCVI` | resource_hints | L1907–1958 | — |
| 131 | `RESOURCE-002` | 🟡 MINOR | `SCVITOOLS_SCVI` | resource_hints | L1907–1958 | — |
| 132 | `CONTAINER-001` | 🔴 CRITICAL | `SEURAT_INTEGRATION` | containerization | L1962–1989 | ✅ |
| 133 | `RESOURCE-001` | 🟡 MINOR | `SEURAT_INTEGRATION` | resource_hints | L1962–1989 | — |
| 134 | `RESOURCE-002` | 🟡 MINOR | `SEURAT_INTEGRATION` | resource_hints | L1962–1989 | — |
| 135 | `CONTAINER-001` | 🔴 CRITICAL | `SOUPX` | containerization | L1993–2025 | ✅ |
| 136 | `RESOURCE-001` | 🟡 MINOR | `SOUPX` | resource_hints | L1993–2025 | — |
| 137 | `RESOURCE-002` | 🟡 MINOR | `SOUPX` | resource_hints | L1993–2025 | — |
| 138 | `CONTAINER-001` | 🔴 CRITICAL | `ANNDATA_BARCODES` | containerization | L2029–2064 | ✅ |
| 139 | `RESOURCE-001` | 🟡 MINOR | `ANNDATA_BARCODES` | resource_hints | L2029–2064 | — |
| 140 | `RESOURCE-002` | 🟡 MINOR | `ANNDATA_BARCODES` | resource_hints | L2029–2064 | — |
| 141 | `CONTAINER-001` | 🔴 CRITICAL | `ANNDATA_GETSIZE` | containerization | L2068–2103 | ✅ |
| 142 | `RESOURCE-001` | 🟡 MINOR | `ANNDATA_GETSIZE` | resource_hints | L2068–2103 | — |
| 143 | `RESOURCE-002` | 🟡 MINOR | `ANNDATA_GETSIZE` | resource_hints | L2068–2103 | — |
| 144 | `CONTAINER-001` | 🔴 CRITICAL | `CELLBENDER_MERGE` | containerization | L2107–2142 | ✅ |
| 145 | `RESOURCE-001` | 🟡 MINOR | `CELLBENDER_MERGE` | resource_hints | L2107–2142 | — |
| 146 | `RESOURCE-002` | 🟡 MINOR | `CELLBENDER_MERGE` | resource_hints | L2107–2142 | — |
| 147 | `CONTAINER-001` | 🔴 CRITICAL | `CELLBENDER_REMOVEBACKGROUND` | containerization | L2146–2212 | ✅ |
| 148 | `RESOURCE-001` | 🟡 MINOR | `CELLBENDER_REMOVEBACKGROUND` | resource_hints | L2146–2212 | — |
| 149 | `RESOURCE-002` | 🟡 MINOR | `CELLBENDER_REMOVEBACKGROUND` | resource_hints | L2146–2212 | — |
| 150 | `CONTAINER-001` | 🔴 CRITICAL | `DOUBLETDETECTION` | containerization | L2216–2253 | ✅ |
| 151 | `RESOURCE-001` | 🟡 MINOR | `DOUBLETDETECTION` | resource_hints | L2216–2253 | — |
| 152 | `RESOURCE-002` | 🟡 MINOR | `DOUBLETDETECTION` | resource_hints | L2216–2253 | — |
| 153 | `CONTAINER-001` | 🔴 CRITICAL | `MULTIQC` | containerization | L2257–2311 | ✅ |
| 154 | `RESOURCE-001` | 🟡 MINOR | `MULTIQC` | resource_hints | L2257–2311 | — |
| 155 | `RESOURCE-002` | 🟡 MINOR | `MULTIQC` | resource_hints | L2257–2311 | — |
| 156 | `CONTAINER-001` | 🔴 CRITICAL | `SCANPY_SCRUBLET` | containerization | L2315–2363 | ✅ |
| 157 | `RESOURCE-001` | 🟡 MINOR | `SCANPY_SCRUBLET` | resource_hints | L2315–2363 | — |
| 158 | `RESOURCE-002` | 🟡 MINOR | `SCANPY_SCRUBLET` | resource_hints | L2315–2363 | — |
| 159 | `CONTAINER-001` | 🔴 CRITICAL | `SCVITOOLS_SCAR` | containerization | L2367–2405 | ✅ |
| 160 | `RESOURCE-001` | 🟡 MINOR | `SCVITOOLS_SCAR` | resource_hints | L2367–2405 | — |
| 161 | `RESOURCE-002` | 🟡 MINOR | `SCVITOOLS_SCAR` | resource_hints | L2367–2405 | — |
| 162 | `CONTAINER-001` | 🔴 CRITICAL | `SCVITOOLS_SOLO` | containerization | L2409–2450 | ✅ |
| 163 | `RESOURCE-001` | 🟡 MINOR | `SCVITOOLS_SOLO` | resource_hints | L2409–2450 | — |
| 164 | `RESOURCE-002` | 🟡 MINOR | `SCVITOOLS_SOLO` | resource_hints | L2409–2450 | — |
| 165 | `CONTAINER-001` | 🔴 CRITICAL | `UNTAR` | containerization | L2454–2537 | ✅ |
| 166 | `STORAGE-001` | 🟠 MAJOR | `UNTAR` | storage | L2454–2537 | — |
| 167 | `RESOURCE-001` | 🟡 MINOR | `UNTAR` | resource_hints | L2454–2537 | — |
| 168 | `RESOURCE-002` | 🟡 MINOR | `UNTAR` | resource_hints | L2454–2537 | — |

### Detail

<details><summary>🔴 <strong>1. CONTAINER-001 — ADATA_ENTROPY</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L239–281  
**Auto-fixable:** Yes

**Description:**  
Process 'ADATA_ENTROPY' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟡 <strong>2. RESOURCE-001 — ADATA_ENTROPY</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L239–281  
**Auto-fixable:** No

**Description:**  
Process 'ADATA_ENTROPY' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>3. RESOURCE-002 — ADATA_ENTROPY</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L239–281  
**Auto-fixable:** No

**Description:**  
Process 'ADATA_ENTROPY' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>4. CONTAINER-001 — ADATA_EXTEND</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L285–325  
**Auto-fixable:** Yes

**Description:**  
Process 'ADATA_EXTEND' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟡 <strong>5. RESOURCE-001 — ADATA_EXTEND</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L285–325  
**Auto-fixable:** No

**Description:**  
Process 'ADATA_EXTEND' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>6. RESOURCE-002 — ADATA_EXTEND</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L285–325  
**Auto-fixable:** No

**Description:**  
Process 'ADATA_EXTEND' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>7. CONTAINER-001 — ADATA_MERGE</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L329–367  
**Auto-fixable:** Yes

**Description:**  
Process 'ADATA_MERGE' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟡 <strong>8. RESOURCE-001 — ADATA_MERGE</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L329–367  
**Auto-fixable:** No

**Description:**  
Process 'ADATA_MERGE' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>9. RESOURCE-002 — ADATA_MERGE</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L329–367  
**Auto-fixable:** No

**Description:**  
Process 'ADATA_MERGE' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>10. CONTAINER-001 — ADATA_MERGEEMBEDDINGS</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L371–404  
**Auto-fixable:** Yes

**Description:**  
Process 'ADATA_MERGEEMBEDDINGS' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟡 <strong>11. RESOURCE-001 — ADATA_MERGEEMBEDDINGS</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L371–404  
**Auto-fixable:** No

**Description:**  
Process 'ADATA_MERGEEMBEDDINGS' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>12. RESOURCE-002 — ADATA_MERGEEMBEDDINGS</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L371–404  
**Auto-fixable:** No

**Description:**  
Process 'ADATA_MERGEEMBEDDINGS' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>13. CONTAINER-001 — ADATA_MYGENE</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L408–442  
**Auto-fixable:** Yes

**Description:**  
Process 'ADATA_MYGENE' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟡 <strong>14. RESOURCE-001 — ADATA_MYGENE</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L408–442  
**Auto-fixable:** No

**Description:**  
Process 'ADATA_MYGENE' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>15. RESOURCE-002 — ADATA_MYGENE</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L408–442  
**Auto-fixable:** No

**Description:**  
Process 'ADATA_MYGENE' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>16. CONTAINER-001 — ADATA_PREPCELLXGENE</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L446–481  
**Auto-fixable:** Yes

**Description:**  
Process 'ADATA_PREPCELLXGENE' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟡 <strong>17. RESOURCE-001 — ADATA_PREPCELLXGENE</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L446–481  
**Auto-fixable:** No

**Description:**  
Process 'ADATA_PREPCELLXGENE' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>18. RESOURCE-002 — ADATA_PREPCELLXGENE</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L446–481  
**Auto-fixable:** No

**Description:**  
Process 'ADATA_PREPCELLXGENE' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>19. CONTAINER-001 — ADATA_READCSV</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L485–514  
**Auto-fixable:** Yes

**Description:**  
Process 'ADATA_READCSV' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟡 <strong>20. RESOURCE-001 — ADATA_READCSV</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L485–514  
**Auto-fixable:** No

**Description:**  
Process 'ADATA_READCSV' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>21. RESOURCE-002 — ADATA_READCSV</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L485–514  
**Auto-fixable:** No

**Description:**  
Process 'ADATA_READCSV' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>22. CONTAINER-001 — ADATA_READRDS</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L518–544  
**Auto-fixable:** Yes

**Description:**  
Process 'ADATA_READRDS' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟡 <strong>23. RESOURCE-001 — ADATA_READRDS</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L518–544  
**Auto-fixable:** No

**Description:**  
Process 'ADATA_READRDS' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>24. RESOURCE-002 — ADATA_READRDS</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L518–544  
**Auto-fixable:** No

**Description:**  
Process 'ADATA_READRDS' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>25. CONTAINER-001 — ADATA_SETINDEX</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L548–586  
**Auto-fixable:** Yes

**Description:**  
Process 'ADATA_SETINDEX' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟡 <strong>26. RESOURCE-001 — ADATA_SETINDEX</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L548–586  
**Auto-fixable:** No

**Description:**  
Process 'ADATA_SETINDEX' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>27. RESOURCE-002 — ADATA_SETINDEX</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L548–586  
**Auto-fixable:** No

**Description:**  
Process 'ADATA_SETINDEX' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>28. CONTAINER-001 — ADATA_SPLITCOL</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L590–621  
**Auto-fixable:** Yes

**Description:**  
Process 'ADATA_SPLITCOL' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟡 <strong>29. RESOURCE-001 — ADATA_SPLITCOL</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L590–621  
**Auto-fixable:** No

**Description:**  
Process 'ADATA_SPLITCOL' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>30. RESOURCE-002 — ADATA_SPLITCOL</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L590–621  
**Auto-fixable:** No

**Description:**  
Process 'ADATA_SPLITCOL' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>31. CONTAINER-001 — ADATA_SPLITEMBEDDINGS</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L625–655  
**Auto-fixable:** Yes

**Description:**  
Process 'ADATA_SPLITEMBEDDINGS' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟡 <strong>32. RESOURCE-001 — ADATA_SPLITEMBEDDINGS</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L625–655  
**Auto-fixable:** No

**Description:**  
Process 'ADATA_SPLITEMBEDDINGS' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>33. RESOURCE-002 — ADATA_SPLITEMBEDDINGS</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L625–655  
**Auto-fixable:** No

**Description:**  
Process 'ADATA_SPLITEMBEDDINGS' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>34. CONTAINER-001 — ADATA_TORDS</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L659–690  
**Auto-fixable:** Yes

**Description:**  
Process 'ADATA_TORDS' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟡 <strong>35. RESOURCE-001 — ADATA_TORDS</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L659–690  
**Auto-fixable:** No

**Description:**  
Process 'ADATA_TORDS' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>36. RESOURCE-002 — ADATA_TORDS</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L659–690  
**Auto-fixable:** No

**Description:**  
Process 'ADATA_TORDS' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>37. CONTAINER-001 — ADATA_UNIFY</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L694–731  
**Auto-fixable:** Yes

**Description:**  
Process 'ADATA_UNIFY' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟡 <strong>38. RESOURCE-001 — ADATA_UNIFY</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L694–731  
**Auto-fixable:** No

**Description:**  
Process 'ADATA_UNIFY' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>39. RESOURCE-002 — ADATA_UNIFY</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L694–731  
**Auto-fixable:** No

**Description:**  
Process 'ADATA_UNIFY' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>40. CONTAINER-001 — ADATA_UPSETGENES</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L735–766  
**Auto-fixable:** Yes

**Description:**  
Process 'ADATA_UPSETGENES' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟡 <strong>41. RESOURCE-001 — ADATA_UPSETGENES</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L735–766  
**Auto-fixable:** No

**Description:**  
Process 'ADATA_UPSETGENES' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>42. RESOURCE-002 — ADATA_UPSETGENES</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L735–766  
**Auto-fixable:** No

**Description:**  
Process 'ADATA_UPSETGENES' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>43. CONTAINER-001 — CELDA_DECONTX</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L770–802  
**Auto-fixable:** Yes

**Description:**  
Process 'CELDA_DECONTX' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟡 <strong>44. RESOURCE-001 — CELDA_DECONTX</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L770–802  
**Auto-fixable:** No

**Description:**  
Process 'CELDA_DECONTX' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>45. RESOURCE-002 — CELDA_DECONTX</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L770–802  
**Auto-fixable:** No

**Description:**  
Process 'CELDA_DECONTX' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>46. CONTAINER-001 — CELLDEX_FETCHREFERENCE</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L806–836  
**Auto-fixable:** Yes

**Description:**  
Process 'CELLDEX_FETCHREFERENCE' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟡 <strong>47. RESOURCE-001 — CELLDEX_FETCHREFERENCE</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L806–836  
**Auto-fixable:** No

**Description:**  
Process 'CELLDEX_FETCHREFERENCE' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>48. RESOURCE-002 — CELLDEX_FETCHREFERENCE</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L806–836  
**Auto-fixable:** No

**Description:**  
Process 'CELLDEX_FETCHREFERENCE' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>49. CONTAINER-001 — CELLTYPES_CELLTYPIST</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L840–872  
**Auto-fixable:** Yes

**Description:**  
Process 'CELLTYPES_CELLTYPIST' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟡 <strong>50. RESOURCE-001 — CELLTYPES_CELLTYPIST</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L840–872  
**Auto-fixable:** No

**Description:**  
Process 'CELLTYPES_CELLTYPIST' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>51. RESOURCE-002 — CELLTYPES_CELLTYPIST</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L840–872  
**Auto-fixable:** No

**Description:**  
Process 'CELLTYPES_CELLTYPIST' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>52. CONTAINER-001 — CELLTYPES_SINGLER</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L876–911  
**Auto-fixable:** Yes

**Description:**  
Process 'CELLTYPES_SINGLER' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟡 <strong>53. RESOURCE-001 — CELLTYPES_SINGLER</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L876–911  
**Auto-fixable:** No

**Description:**  
Process 'CELLTYPES_SINGLER' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>54. RESOURCE-002 — CELLTYPES_SINGLER</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L876–911  
**Auto-fixable:** No

**Description:**  
Process 'CELLTYPES_SINGLER' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>55. CONTAINER-001 — CUSTOM_COLLECTSIZES</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L915–943  
**Auto-fixable:** Yes

**Description:**  
Process 'CUSTOM_COLLECTSIZES' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟡 <strong>56. RESOURCE-001 — CUSTOM_COLLECTSIZES</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L915–943  
**Auto-fixable:** No

**Description:**  
Process 'CUSTOM_COLLECTSIZES' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>57. RESOURCE-002 — CUSTOM_COLLECTSIZES</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L915–943  
**Auto-fixable:** No

**Description:**  
Process 'CUSTOM_COLLECTSIZES' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>58. CONTAINER-001 — DOUBLET_REMOVAL</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L947–979  
**Auto-fixable:** Yes

**Description:**  
Process 'DOUBLET_REMOVAL' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟡 <strong>59. RESOURCE-001 — DOUBLET_REMOVAL</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L947–979  
**Auto-fixable:** No

**Description:**  
Process 'DOUBLET_REMOVAL' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>60. RESOURCE-002 — DOUBLET_REMOVAL</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L947–979  
**Auto-fixable:** No

**Description:**  
Process 'DOUBLET_REMOVAL' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🟡 <strong>61. RESOURCE-001 — SCDS</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L983–1011  
**Auto-fixable:** No

**Description:**  
Process 'SCDS' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>62. RESOURCE-002 — SCDS</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L983–1011  
**Auto-fixable:** No

**Description:**  
Process 'SCDS' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>63. CONTAINER-001 — HUGOUNIFIER_APPLY</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L1015–1048  
**Auto-fixable:** Yes

**Description:**  
Process 'HUGOUNIFIER_APPLY' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟡 <strong>64. RESOURCE-001 — HUGOUNIFIER_APPLY</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L1015–1048  
**Auto-fixable:** No

**Description:**  
Process 'HUGOUNIFIER_APPLY' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>65. RESOURCE-002 — HUGOUNIFIER_APPLY</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L1015–1048  
**Auto-fixable:** No

**Description:**  
Process 'HUGOUNIFIER_APPLY' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>66. CONTAINER-001 — HUGOUNIFIER_GET</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L1052–1090  
**Auto-fixable:** Yes

**Description:**  
Process 'HUGOUNIFIER_GET' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟡 <strong>67. RESOURCE-001 — HUGOUNIFIER_GET</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L1052–1090  
**Auto-fixable:** No

**Description:**  
Process 'HUGOUNIFIER_GET' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>68. RESOURCE-002 — HUGOUNIFIER_GET</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L1052–1090  
**Auto-fixable:** No

**Description:**  
Process 'HUGOUNIFIER_GET' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>69. CONTAINER-001 — LIANA_RANKAGGREGATE</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L1094–1127  
**Auto-fixable:** Yes

**Description:**  
Process 'LIANA_RANKAGGREGATE' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟡 <strong>70. RESOURCE-001 — LIANA_RANKAGGREGATE</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L1094–1127  
**Auto-fixable:** No

**Description:**  
Process 'LIANA_RANKAGGREGATE' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>71. RESOURCE-002 — LIANA_RANKAGGREGATE</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L1094–1127  
**Auto-fixable:** No

**Description:**  
Process 'LIANA_RANKAGGREGATE' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>72. CONTAINER-001 — SCANPY_BBKNN</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L1131–1162  
**Auto-fixable:** Yes

**Description:**  
Process 'SCANPY_BBKNN' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟡 <strong>73. RESOURCE-001 — SCANPY_BBKNN</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L1131–1162  
**Auto-fixable:** No

**Description:**  
Process 'SCANPY_BBKNN' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>74. RESOURCE-002 — SCANPY_BBKNN</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L1131–1162  
**Auto-fixable:** No

**Description:**  
Process 'SCANPY_BBKNN' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>75. CONTAINER-001 — SCANPY_CELLCYCLE</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L1166–1203  
**Auto-fixable:** Yes

**Description:**  
Process 'SCANPY_CELLCYCLE' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟡 <strong>76. RESOURCE-001 — SCANPY_CELLCYCLE</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L1166–1203  
**Auto-fixable:** No

**Description:**  
Process 'SCANPY_CELLCYCLE' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>77. RESOURCE-002 — SCANPY_CELLCYCLE</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L1166–1203  
**Auto-fixable:** No

**Description:**  
Process 'SCANPY_CELLCYCLE' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>78. CONTAINER-001 — SCANPY_COMBAT</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L1207–1242  
**Auto-fixable:** Yes

**Description:**  
Process 'SCANPY_COMBAT' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟡 <strong>79. RESOURCE-001 — SCANPY_COMBAT</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L1207–1242  
**Auto-fixable:** No

**Description:**  
Process 'SCANPY_COMBAT' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>80. RESOURCE-002 — SCANPY_COMBAT</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L1207–1242  
**Auto-fixable:** No

**Description:**  
Process 'SCANPY_COMBAT' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>81. CONTAINER-001 — SCANPY_FILTER</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L1246–1285  
**Auto-fixable:** Yes

**Description:**  
Process 'SCANPY_FILTER' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟡 <strong>82. RESOURCE-001 — SCANPY_FILTER</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L1246–1285  
**Auto-fixable:** No

**Description:**  
Process 'SCANPY_FILTER' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>83. RESOURCE-002 — SCANPY_FILTER</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L1246–1285  
**Auto-fixable:** No

**Description:**  
Process 'SCANPY_FILTER' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>84. CONTAINER-001 — SCANPY_HARMONY</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L1289–1325  
**Auto-fixable:** Yes

**Description:**  
Process 'SCANPY_HARMONY' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟡 <strong>85. RESOURCE-001 — SCANPY_HARMONY</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L1289–1325  
**Auto-fixable:** No

**Description:**  
Process 'SCANPY_HARMONY' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>86. RESOURCE-002 — SCANPY_HARMONY</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L1289–1325  
**Auto-fixable:** No

**Description:**  
Process 'SCANPY_HARMONY' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>87. CONTAINER-001 — SCANPY_HVGS</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L1329–1363  
**Auto-fixable:** Yes

**Description:**  
Process 'SCANPY_HVGS' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟡 <strong>88. RESOURCE-001 — SCANPY_HVGS</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L1329–1363  
**Auto-fixable:** No

**Description:**  
Process 'SCANPY_HVGS' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>89. RESOURCE-002 — SCANPY_HVGS</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L1329–1363  
**Auto-fixable:** No

**Description:**  
Process 'SCANPY_HVGS' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>90. CONTAINER-001 — SCANPY_LEIDEN</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L1367–1408  
**Auto-fixable:** Yes

**Description:**  
Process 'SCANPY_LEIDEN' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟡 <strong>91. RESOURCE-001 — SCANPY_LEIDEN</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L1367–1408  
**Auto-fixable:** No

**Description:**  
Process 'SCANPY_LEIDEN' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>92. RESOURCE-002 — SCANPY_LEIDEN</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L1367–1408  
**Auto-fixable:** No

**Description:**  
Process 'SCANPY_LEIDEN' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>93. CONTAINER-001 — SCANPY_NEIGHBORS</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L1412–1443  
**Auto-fixable:** Yes

**Description:**  
Process 'SCANPY_NEIGHBORS' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟡 <strong>94. RESOURCE-001 — SCANPY_NEIGHBORS</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L1412–1443  
**Auto-fixable:** No

**Description:**  
Process 'SCANPY_NEIGHBORS' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>95. RESOURCE-002 — SCANPY_NEIGHBORS</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L1412–1443  
**Auto-fixable:** No

**Description:**  
Process 'SCANPY_NEIGHBORS' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>96. CONTAINER-001 — SCANPY_PAGA</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L1447–1485  
**Auto-fixable:** Yes

**Description:**  
Process 'SCANPY_PAGA' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟡 <strong>97. RESOURCE-001 — SCANPY_PAGA</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L1447–1485  
**Auto-fixable:** No

**Description:**  
Process 'SCANPY_PAGA' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>98. RESOURCE-002 — SCANPY_PAGA</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L1447–1485  
**Auto-fixable:** No

**Description:**  
Process 'SCANPY_PAGA' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>99. CONTAINER-001 — SCANPY_PCA</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L1489–1535  
**Auto-fixable:** Yes

**Description:**  
Process 'SCANPY_PCA' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟡 <strong>100. RESOURCE-001 — SCANPY_PCA</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L1489–1535  
**Auto-fixable:** No

**Description:**  
Process 'SCANPY_PCA' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>101. RESOURCE-002 — SCANPY_PCA</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L1489–1535  
**Auto-fixable:** No

**Description:**  
Process 'SCANPY_PCA' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>102. CONTAINER-001 — SCANPY_PLOTQC</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L1539–1574  
**Auto-fixable:** Yes

**Description:**  
Process 'SCANPY_PLOTQC' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟡 <strong>103. RESOURCE-001 — SCANPY_PLOTQC</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L1539–1574  
**Auto-fixable:** No

**Description:**  
Process 'SCANPY_PLOTQC' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>104. RESOURCE-002 — SCANPY_PLOTQC</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L1539–1574  
**Auto-fixable:** No

**Description:**  
Process 'SCANPY_PLOTQC' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>105. CONTAINER-001 — SCANPY_RANKGENESGROUPS</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L1578–1617  
**Auto-fixable:** Yes

**Description:**  
Process 'SCANPY_RANKGENESGROUPS' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟡 <strong>106. RESOURCE-001 — SCANPY_RANKGENESGROUPS</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L1578–1617  
**Auto-fixable:** No

**Description:**  
Process 'SCANPY_RANKGENESGROUPS' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>107. RESOURCE-002 — SCANPY_RANKGENESGROUPS</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L1578–1617  
**Auto-fixable:** No

**Description:**  
Process 'SCANPY_RANKGENESGROUPS' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>108. CONTAINER-001 — SCANPY_READH5</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L1621–1650  
**Auto-fixable:** Yes

**Description:**  
Process 'SCANPY_READH5' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟡 <strong>109. RESOURCE-001 — SCANPY_READH5</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L1621–1650  
**Auto-fixable:** No

**Description:**  
Process 'SCANPY_READH5' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>110. RESOURCE-002 — SCANPY_READH5</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L1621–1650  
**Auto-fixable:** No

**Description:**  
Process 'SCANPY_READH5' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>111. CONTAINER-001 — SCANPY_SAMPLE</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L1654–1688  
**Auto-fixable:** Yes

**Description:**  
Process 'SCANPY_SAMPLE' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟡 <strong>112. RESOURCE-001 — SCANPY_SAMPLE</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L1654–1688  
**Auto-fixable:** No

**Description:**  
Process 'SCANPY_SAMPLE' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>113. RESOURCE-002 — SCANPY_SAMPLE</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L1654–1688  
**Auto-fixable:** No

**Description:**  
Process 'SCANPY_SAMPLE' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>114. CONTAINER-001 — SCANPY_UMAP</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L1692–1726  
**Auto-fixable:** Yes

**Description:**  
Process 'SCANPY_UMAP' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟡 <strong>115. RESOURCE-001 — SCANPY_UMAP</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L1692–1726  
**Auto-fixable:** No

**Description:**  
Process 'SCANPY_UMAP' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>116. RESOURCE-002 — SCANPY_UMAP</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L1692–1726  
**Auto-fixable:** No

**Description:**  
Process 'SCANPY_UMAP' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>117. CONTAINER-001 — SCIMILARITY_ANNOTATE</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L1730–1767  
**Auto-fixable:** Yes

**Description:**  
Process 'SCIMILARITY_ANNOTATE' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟡 <strong>118. RESOURCE-001 — SCIMILARITY_ANNOTATE</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L1730–1767  
**Auto-fixable:** No

**Description:**  
Process 'SCIMILARITY_ANNOTATE' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>119. RESOURCE-002 — SCIMILARITY_ANNOTATE</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L1730–1767  
**Auto-fixable:** No

**Description:**  
Process 'SCIMILARITY_ANNOTATE' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>120. CONTAINER-001 — SCIMILARITY_EMBED</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L1771–1804  
**Auto-fixable:** Yes

**Description:**  
Process 'SCIMILARITY_EMBED' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟡 <strong>121. RESOURCE-001 — SCIMILARITY_EMBED</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L1771–1804  
**Auto-fixable:** No

**Description:**  
Process 'SCIMILARITY_EMBED' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>122. RESOURCE-002 — SCIMILARITY_EMBED</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L1771–1804  
**Auto-fixable:** No

**Description:**  
Process 'SCIMILARITY_EMBED' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>123. CONTAINER-001 — SCIMILARITY_PSEUDOBULK</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L1808–1845  
**Auto-fixable:** Yes

**Description:**  
Process 'SCIMILARITY_PSEUDOBULK' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟡 <strong>124. RESOURCE-001 — SCIMILARITY_PSEUDOBULK</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L1808–1845  
**Auto-fixable:** No

**Description:**  
Process 'SCIMILARITY_PSEUDOBULK' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>125. RESOURCE-002 — SCIMILARITY_PSEUDOBULK</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L1808–1845  
**Auto-fixable:** No

**Description:**  
Process 'SCIMILARITY_PSEUDOBULK' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>126. CONTAINER-001 — SCVITOOLS_SCANVI</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L1849–1903  
**Auto-fixable:** Yes

**Description:**  
Process 'SCVITOOLS_SCANVI' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟡 <strong>127. RESOURCE-001 — SCVITOOLS_SCANVI</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L1849–1903  
**Auto-fixable:** No

**Description:**  
Process 'SCVITOOLS_SCANVI' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>128. RESOURCE-002 — SCVITOOLS_SCANVI</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L1849–1903  
**Auto-fixable:** No

**Description:**  
Process 'SCVITOOLS_SCANVI' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>129. CONTAINER-001 — SCVITOOLS_SCVI</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L1907–1958  
**Auto-fixable:** Yes

**Description:**  
Process 'SCVITOOLS_SCVI' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟡 <strong>130. RESOURCE-001 — SCVITOOLS_SCVI</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L1907–1958  
**Auto-fixable:** No

**Description:**  
Process 'SCVITOOLS_SCVI' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>131. RESOURCE-002 — SCVITOOLS_SCVI</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L1907–1958  
**Auto-fixable:** No

**Description:**  
Process 'SCVITOOLS_SCVI' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>132. CONTAINER-001 — SEURAT_INTEGRATION</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L1962–1989  
**Auto-fixable:** Yes

**Description:**  
Process 'SEURAT_INTEGRATION' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟡 <strong>133. RESOURCE-001 — SEURAT_INTEGRATION</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L1962–1989  
**Auto-fixable:** No

**Description:**  
Process 'SEURAT_INTEGRATION' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>134. RESOURCE-002 — SEURAT_INTEGRATION</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L1962–1989  
**Auto-fixable:** No

**Description:**  
Process 'SEURAT_INTEGRATION' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>135. CONTAINER-001 — SOUPX</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L1993–2025  
**Auto-fixable:** Yes

**Description:**  
Process 'SOUPX' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟡 <strong>136. RESOURCE-001 — SOUPX</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L1993–2025  
**Auto-fixable:** No

**Description:**  
Process 'SOUPX' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>137. RESOURCE-002 — SOUPX</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L1993–2025  
**Auto-fixable:** No

**Description:**  
Process 'SOUPX' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>138. CONTAINER-001 — ANNDATA_BARCODES</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L2029–2064  
**Auto-fixable:** Yes

**Description:**  
Process 'ANNDATA_BARCODES' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟡 <strong>139. RESOURCE-001 — ANNDATA_BARCODES</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L2029–2064  
**Auto-fixable:** No

**Description:**  
Process 'ANNDATA_BARCODES' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>140. RESOURCE-002 — ANNDATA_BARCODES</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L2029–2064  
**Auto-fixable:** No

**Description:**  
Process 'ANNDATA_BARCODES' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>141. CONTAINER-001 — ANNDATA_GETSIZE</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L2068–2103  
**Auto-fixable:** Yes

**Description:**  
Process 'ANNDATA_GETSIZE' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟡 <strong>142. RESOURCE-001 — ANNDATA_GETSIZE</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L2068–2103  
**Auto-fixable:** No

**Description:**  
Process 'ANNDATA_GETSIZE' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>143. RESOURCE-002 — ANNDATA_GETSIZE</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L2068–2103  
**Auto-fixable:** No

**Description:**  
Process 'ANNDATA_GETSIZE' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>144. CONTAINER-001 — CELLBENDER_MERGE</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L2107–2142  
**Auto-fixable:** Yes

**Description:**  
Process 'CELLBENDER_MERGE' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟡 <strong>145. RESOURCE-001 — CELLBENDER_MERGE</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L2107–2142  
**Auto-fixable:** No

**Description:**  
Process 'CELLBENDER_MERGE' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>146. RESOURCE-002 — CELLBENDER_MERGE</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L2107–2142  
**Auto-fixable:** No

**Description:**  
Process 'CELLBENDER_MERGE' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>147. CONTAINER-001 — CELLBENDER_REMOVEBACKGROUND</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L2146–2212  
**Auto-fixable:** Yes

**Description:**  
Process 'CELLBENDER_REMOVEBACKGROUND' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟡 <strong>148. RESOURCE-001 — CELLBENDER_REMOVEBACKGROUND</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L2146–2212  
**Auto-fixable:** No

**Description:**  
Process 'CELLBENDER_REMOVEBACKGROUND' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>149. RESOURCE-002 — CELLBENDER_REMOVEBACKGROUND</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L2146–2212  
**Auto-fixable:** No

**Description:**  
Process 'CELLBENDER_REMOVEBACKGROUND' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>150. CONTAINER-001 — DOUBLETDETECTION</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L2216–2253  
**Auto-fixable:** Yes

**Description:**  
Process 'DOUBLETDETECTION' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟡 <strong>151. RESOURCE-001 — DOUBLETDETECTION</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L2216–2253  
**Auto-fixable:** No

**Description:**  
Process 'DOUBLETDETECTION' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>152. RESOURCE-002 — DOUBLETDETECTION</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L2216–2253  
**Auto-fixable:** No

**Description:**  
Process 'DOUBLETDETECTION' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>153. CONTAINER-001 — MULTIQC</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L2257–2311  
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

<details><summary>🟡 <strong>154. RESOURCE-001 — MULTIQC</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L2257–2311  
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

<details><summary>🟡 <strong>155. RESOURCE-002 — MULTIQC</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L2257–2311  
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

<details><summary>🔴 <strong>156. CONTAINER-001 — SCANPY_SCRUBLET</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L2315–2363  
**Auto-fixable:** Yes

**Description:**  
Process 'SCANPY_SCRUBLET' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟡 <strong>157. RESOURCE-001 — SCANPY_SCRUBLET</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L2315–2363  
**Auto-fixable:** No

**Description:**  
Process 'SCANPY_SCRUBLET' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>158. RESOURCE-002 — SCANPY_SCRUBLET</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L2315–2363  
**Auto-fixable:** No

**Description:**  
Process 'SCANPY_SCRUBLET' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>159. CONTAINER-001 — SCVITOOLS_SCAR</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L2367–2405  
**Auto-fixable:** Yes

**Description:**  
Process 'SCVITOOLS_SCAR' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟡 <strong>160. RESOURCE-001 — SCVITOOLS_SCAR</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L2367–2405  
**Auto-fixable:** No

**Description:**  
Process 'SCVITOOLS_SCAR' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>161. RESOURCE-002 — SCVITOOLS_SCAR</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L2367–2405  
**Auto-fixable:** No

**Description:**  
Process 'SCVITOOLS_SCAR' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>162. CONTAINER-001 — SCVITOOLS_SOLO</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L2409–2450  
**Auto-fixable:** Yes

**Description:**  
Process 'SCVITOOLS_SOLO' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟡 <strong>163. RESOURCE-001 — SCVITOOLS_SOLO</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L2409–2450  
**Auto-fixable:** No

**Description:**  
Process 'SCVITOOLS_SOLO' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>164. RESOURCE-002 — SCVITOOLS_SOLO</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L2409–2450  
**Auto-fixable:** No

**Description:**  
Process 'SCVITOOLS_SOLO' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>165. CONTAINER-001 — UNTAR</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L2454–2537  
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

<details><summary>🟠 <strong>166. STORAGE-001 — UNTAR</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L2454–2537  
**Auto-fixable:** No

**Description:**  
Process 'UNTAR' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
//, //
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>167. RESOURCE-001 — UNTAR</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L2454–2537  
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

<details><summary>🟡 <strong>168. RESOURCE-002 — UNTAR</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L2454–2537  
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