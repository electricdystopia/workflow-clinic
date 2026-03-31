<!-- WORKFLOW CLINIC ISSUE DRAFT -->
<!-- Title: [Workflow Clinic] 481 cloud-readiness gaps across 123 processes (score: 0%) -->

## 🏥 Workflow Clinic — Automated Cloud-Readiness Report

> **This issue was drafted automatically by [Workflow Clinic](https://github.com/electricdystopia/workflow-clinic), a GA4GH Cloud Work Stream tool for detecting and fixing cloud-readiness gaps in bioinformatics workflows.**
>
> Workflow: `main.nf`  
> Generated: 2026-03-31 19:49 UTC  
> Schema: `0.1.0`

### 🔴 Cloud Readiness Score: **0.00 / 1.00**

### Summary

| Severity | Count | Description |
|---|---|---|
| 🔴 **Critical** | 120 | Portability blockers — workflow cannot run on cloud WES |
| 🟠 **Major** | 117 | Significant gaps affecting reproducibility or correctness |
| 🟡 **Minor** | 244 | Resource hints missing — affects cost and scheduling efficiency |
| **Total** | **481** | |
| Auto-fixable | 120 | Can be fixed automatically with `workflow-clinic doctor` |

> 💡 **120 gap(s) can be fixed automatically.** Run `workflow-clinic doctor <path> --gap CONTAINER-001` to generate a patch and open a PR.

### Gaps

| # | Gap ID | Severity | Process | Category | Lines | Auto-fix |
|---|---|---|---|---|---|---|
| 1 | `CONTAINER-001` | 🔴 CRITICAL | `ADD_INFO_TO_VCF` | containerization | L417–457 | ✅ |
| 2 | `STORAGE-001` | 🟠 MAJOR | `ADD_INFO_TO_VCF` | storage | L417–457 | — |
| 3 | `RESOURCE-001` | 🟡 MINOR | `ADD_INFO_TO_VCF` | resource_hints | L417–457 | — |
| 4 | `RESOURCE-002` | 🟡 MINOR | `ADD_INFO_TO_VCF` | resource_hints | L417–457 | — |
| 5 | `CONTAINER-001` | 🔴 CRITICAL | `CONSENSUS_FROM_SITES` | containerization | L464–521 | ✅ |
| 6 | `STORAGE-001` | 🟠 MAJOR | `CONSENSUS_FROM_SITES` | storage | L464–521 | — |
| 7 | `RESOURCE-001` | 🟡 MINOR | `CONSENSUS_FROM_SITES` | resource_hints | L464–521 | — |
| 8 | `RESOURCE-002` | 🟡 MINOR | `CONSENSUS_FROM_SITES` | resource_hints | L464–521 | — |
| 9 | `CONTAINER-001` | 🔴 CRITICAL | `CREATE_INTERVALS_BED` | containerization | L525–612 | ✅ |
| 10 | `STORAGE-001` | 🟠 MAJOR | `CREATE_INTERVALS_BED` | storage | L525–612 | — |
| 11 | `RESOURCE-001` | 🟡 MINOR | `CREATE_INTERVALS_BED` | resource_hints | L525–612 | — |
| 12 | `RESOURCE-002` | 🟡 MINOR | `CREATE_INTERVALS_BED` | resource_hints | L525–612 | — |
| 13 | `CONTAINER-001` | 🔴 CRITICAL | `SAMTOOLS_REINDEX_BAM` | containerization | L620–672 | ✅ |
| 14 | `STORAGE-001` | 🟠 MAJOR | `SAMTOOLS_REINDEX_BAM` | storage | L620–672 | — |
| 15 | `RESOURCE-001` | 🟡 MINOR | `SAMTOOLS_REINDEX_BAM` | resource_hints | L620–672 | — |
| 16 | `RESOURCE-002` | 🟡 MINOR | `SAMTOOLS_REINDEX_BAM` | resource_hints | L620–672 | — |
| 17 | `CONTAINER-001` | 🔴 CRITICAL | `ASCAT` | containerization | L676–932 | ✅ |
| 18 | `STORAGE-001` | 🟠 MAJOR | `ASCAT` | storage | L676–932 | — |
| 19 | `RESOURCE-001` | 🟡 MINOR | `ASCAT` | resource_hints | L676–932 | — |
| 20 | `RESOURCE-002` | 🟡 MINOR | `ASCAT` | resource_hints | L676–932 | — |
| 21 | `CONTAINER-001` | 🔴 CRITICAL | `BBMAP_BBSPLIT` | containerization | L936–1065 | ✅ |
| 22 | `STORAGE-001` | 🟠 MAJOR | `BBMAP_BBSPLIT` | storage | L936–1065 | — |
| 23 | `RESOURCE-001` | 🟡 MINOR | `BBMAP_BBSPLIT` | resource_hints | L936–1065 | — |
| 24 | `RESOURCE-002` | 🟡 MINOR | `BBMAP_BBSPLIT` | resource_hints | L936–1065 | — |
| 25 | `CONTAINER-001` | 🔴 CRITICAL | `BCFTOOLS_ANNOTATE` | containerization | L1069–1155 | ✅ |
| 26 | `STORAGE-001` | 🟠 MAJOR | `BCFTOOLS_ANNOTATE` | storage | L1069–1155 | — |
| 27 | `RESOURCE-001` | 🟡 MINOR | `BCFTOOLS_ANNOTATE` | resource_hints | L1069–1155 | — |
| 28 | `RESOURCE-002` | 🟡 MINOR | `BCFTOOLS_ANNOTATE` | resource_hints | L1069–1155 | — |
| 29 | `CONTAINER-001` | 🔴 CRITICAL | `BCFTOOLS_CONCAT` | containerization | L1159–1230 | ✅ |
| 30 | `STORAGE-001` | 🟠 MAJOR | `BCFTOOLS_CONCAT` | storage | L1159–1230 | — |
| 31 | `RESOURCE-001` | 🟡 MINOR | `BCFTOOLS_CONCAT` | resource_hints | L1159–1230 | — |
| 32 | `RESOURCE-002` | 🟡 MINOR | `BCFTOOLS_CONCAT` | resource_hints | L1159–1230 | — |
| 33 | `CONTAINER-001` | 🔴 CRITICAL | `BCFTOOLS_ISEC` | containerization | L1234–1284 | ✅ |
| 34 | `STORAGE-001` | 🟠 MAJOR | `BCFTOOLS_ISEC` | storage | L1234–1284 | — |
| 35 | `RESOURCE-001` | 🟡 MINOR | `BCFTOOLS_ISEC` | resource_hints | L1234–1284 | — |
| 36 | `RESOURCE-002` | 🟡 MINOR | `BCFTOOLS_ISEC` | resource_hints | L1234–1284 | — |
| 37 | `CONTAINER-001` | 🔴 CRITICAL | `BCFTOOLS_MERGE` | containerization | L1288–1361 | ✅ |
| 38 | `STORAGE-001` | 🟠 MAJOR | `BCFTOOLS_MERGE` | storage | L1288–1361 | — |
| 39 | `RESOURCE-001` | 🟡 MINOR | `BCFTOOLS_MERGE` | resource_hints | L1288–1361 | — |
| 40 | `RESOURCE-002` | 🟡 MINOR | `BCFTOOLS_MERGE` | resource_hints | L1288–1361 | — |
| 41 | `CONTAINER-001` | 🔴 CRITICAL | `BCFTOOLS_MPILEUP` | containerization | L1365–1436 | ✅ |
| 42 | `STORAGE-001` | 🟠 MAJOR | `BCFTOOLS_MPILEUP` | storage | L1365–1436 | — |
| 43 | `RESOURCE-001` | 🟡 MINOR | `BCFTOOLS_MPILEUP` | resource_hints | L1365–1436 | — |
| 44 | `RESOURCE-002` | 🟡 MINOR | `BCFTOOLS_MPILEUP` | resource_hints | L1365–1436 | — |
| 45 | `CONTAINER-001` | 🔴 CRITICAL | `BCFTOOLS_NORM` | containerization | L1440–1513 | ✅ |
| 46 | `STORAGE-001` | 🟠 MAJOR | `BCFTOOLS_NORM` | storage | L1440–1513 | — |
| 47 | `RESOURCE-001` | 🟡 MINOR | `BCFTOOLS_NORM` | resource_hints | L1440–1513 | — |
| 48 | `RESOURCE-002` | 🟡 MINOR | `BCFTOOLS_NORM` | resource_hints | L1440–1513 | — |
| 49 | `CONTAINER-001` | 🔴 CRITICAL | `BCFTOOLS_SORT` | containerization | L1517–1586 | ✅ |
| 50 | `STORAGE-001` | 🟠 MAJOR | `BCFTOOLS_SORT` | storage | L1517–1586 | — |
| 51 | `RESOURCE-001` | 🟡 MINOR | `BCFTOOLS_SORT` | resource_hints | L1517–1586 | — |
| 52 | `RESOURCE-002` | 🟡 MINOR | `BCFTOOLS_SORT` | resource_hints | L1517–1586 | — |
| 53 | `CONTAINER-001` | 🔴 CRITICAL | `BCFTOOLS_STATS` | containerization | L1590–1649 | ✅ |
| 54 | `STORAGE-001` | 🟠 MAJOR | `BCFTOOLS_STATS` | storage | L1590–1649 | — |
| 55 | `RESOURCE-001` | 🟡 MINOR | `BCFTOOLS_STATS` | resource_hints | L1590–1649 | — |
| 56 | `RESOURCE-002` | 🟡 MINOR | `BCFTOOLS_STATS` | resource_hints | L1590–1649 | — |
| 57 | `CONTAINER-001` | 🔴 CRITICAL | `BCFTOOLS_VIEW` | containerization | L1653–1727 | ✅ |
| 58 | `STORAGE-001` | 🟠 MAJOR | `BCFTOOLS_VIEW` | storage | L1653–1727 | — |
| 59 | `RESOURCE-001` | 🟡 MINOR | `BCFTOOLS_VIEW` | resource_hints | L1653–1727 | — |
| 60 | `RESOURCE-002` | 🟡 MINOR | `BCFTOOLS_VIEW` | resource_hints | L1653–1727 | — |
| 61 | `CONTAINER-001` | 🔴 CRITICAL | `BWA_INDEX` | containerization | L1731–1785 | ✅ |
| 62 | `STORAGE-001` | 🟠 MAJOR | `BWA_INDEX` | storage | L1731–1785 | — |
| 63 | `RESOURCE-001` | 🟡 MINOR | `BWA_INDEX` | resource_hints | L1731–1785 | — |
| 64 | `CONTAINER-001` | 🔴 CRITICAL | `BWA_MEM` | containerization | L1789–1862 | ✅ |
| 65 | `STORAGE-001` | 🟠 MAJOR | `BWA_MEM` | storage | L1789–1862 | — |
| 66 | `RESOURCE-001` | 🟡 MINOR | `BWA_MEM` | resource_hints | L1789–1862 | — |
| 67 | `RESOURCE-002` | 🟡 MINOR | `BWA_MEM` | resource_hints | L1789–1862 | — |
| 68 | `CONTAINER-001` | 🔴 CRITICAL | `BWAMEM2_INDEX` | containerization | L1866–1920 | ✅ |
| 69 | `STORAGE-001` | 🟠 MAJOR | `BWAMEM2_INDEX` | storage | L1866–1920 | — |
| 70 | `RESOURCE-001` | 🟡 MINOR | `BWAMEM2_INDEX` | resource_hints | L1866–1920 | — |
| 71 | `CONTAINER-001` | 🔴 CRITICAL | `BWAMEM2_MEM` | containerization | L1924–2006 | ✅ |
| 72 | `STORAGE-001` | 🟠 MAJOR | `BWAMEM2_MEM` | storage | L1924–2006 | — |
| 73 | `RESOURCE-001` | 🟡 MINOR | `BWAMEM2_MEM` | resource_hints | L1924–2006 | — |
| 74 | `RESOURCE-002` | 🟡 MINOR | `BWAMEM2_MEM` | resource_hints | L1924–2006 | — |
| 75 | `CONTAINER-001` | 🔴 CRITICAL | `CAT_CAT` | containerization | L2010–2081 | ✅ |
| 76 | `STORAGE-001` | 🟠 MAJOR | `CAT_CAT` | storage | L2010–2081 | — |
| 77 | `RESOURCE-001` | 🟡 MINOR | `CAT_CAT` | resource_hints | L2010–2081 | — |
| 78 | `RESOURCE-002` | 🟡 MINOR | `CAT_CAT` | resource_hints | L2010–2081 | — |
| 79 | `CONTAINER-001` | 🔴 CRITICAL | `CAT_FASTQ` | containerization | L2091–2178 | ✅ |
| 80 | `STORAGE-001` | 🟠 MAJOR | `CAT_FASTQ` | storage | L2091–2178 | — |
| 81 | `RESOURCE-001` | 🟡 MINOR | `CAT_FASTQ` | resource_hints | L2091–2178 | — |
| 82 | `RESOURCE-002` | 🟡 MINOR | `CAT_FASTQ` | resource_hints | L2091–2178 | — |
| 83 | `CONTAINER-001` | 🔴 CRITICAL | `CNVKIT_ANTITARGET` | containerization | L2182–2217 | ✅ |
| 84 | `STORAGE-001` | 🟠 MAJOR | `CNVKIT_ANTITARGET` | storage | L2182–2217 | — |
| 85 | `RESOURCE-001` | 🟡 MINOR | `CNVKIT_ANTITARGET` | resource_hints | L2182–2217 | — |
| 86 | `RESOURCE-002` | 🟡 MINOR | `CNVKIT_ANTITARGET` | resource_hints | L2182–2217 | — |
| 87 | `CONTAINER-001` | 🔴 CRITICAL | `CNVKIT_BATCH` | containerization | L2221–2330 | ✅ |
| 88 | `STORAGE-001` | 🟠 MAJOR | `CNVKIT_BATCH` | storage | L2221–2330 | — |
| 89 | `RESOURCE-001` | 🟡 MINOR | `CNVKIT_BATCH` | resource_hints | L2221–2330 | — |
| 90 | `RESOURCE-002` | 🟡 MINOR | `CNVKIT_BATCH` | resource_hints | L2221–2330 | — |
| 91 | `CONTAINER-001` | 🔴 CRITICAL | `CNVKIT_CALL` | containerization | L2334–2380 | ✅ |
| 92 | `STORAGE-001` | 🟠 MAJOR | `CNVKIT_CALL` | storage | L2334–2380 | — |
| 93 | `RESOURCE-001` | 🟡 MINOR | `CNVKIT_CALL` | resource_hints | L2334–2380 | — |
| 94 | `RESOURCE-002` | 🟡 MINOR | `CNVKIT_CALL` | resource_hints | L2334–2380 | — |
| 95 | `CONTAINER-001` | 🔴 CRITICAL | `CNVKIT_EXPORT` | containerization | L2384–2430 | ✅ |
| 96 | `STORAGE-001` | 🟠 MAJOR | `CNVKIT_EXPORT` | storage | L2384–2430 | — |
| 97 | `RESOURCE-001` | 🟡 MINOR | `CNVKIT_EXPORT` | resource_hints | L2384–2430 | — |
| 98 | `RESOURCE-002` | 🟡 MINOR | `CNVKIT_EXPORT` | resource_hints | L2384–2430 | — |
| 99 | `CONTAINER-001` | 🔴 CRITICAL | `CNVKIT_GENEMETRICS` | containerization | L2434–2472 | ✅ |
| 100 | `STORAGE-001` | 🟠 MAJOR | `CNVKIT_GENEMETRICS` | storage | L2434–2472 | — |
| 101 | `RESOURCE-001` | 🟡 MINOR | `CNVKIT_GENEMETRICS` | resource_hints | L2434–2472 | — |
| 102 | `RESOURCE-002` | 🟡 MINOR | `CNVKIT_GENEMETRICS` | resource_hints | L2434–2472 | — |
| 103 | `CONTAINER-001` | 🔴 CRITICAL | `CNVKIT_REFERENCE` | containerization | L2476–2515 | ✅ |
| 104 | `STORAGE-001` | 🟠 MAJOR | `CNVKIT_REFERENCE` | storage | L2476–2515 | — |
| 105 | `RESOURCE-001` | 🟡 MINOR | `CNVKIT_REFERENCE` | resource_hints | L2476–2515 | — |
| 106 | `RESOURCE-002` | 🟡 MINOR | `CNVKIT_REFERENCE` | resource_hints | L2476–2515 | — |
| 107 | `CONTAINER-001` | 🔴 CRITICAL | `CONTROLFREEC_ASSESSSIGNIFICANCE` | containerization | L2519–2565 | ✅ |
| 108 | `STORAGE-001` | 🟠 MAJOR | `CONTROLFREEC_ASSESSSIGNIFICANCE` | storage | L2519–2565 | — |
| 109 | `RESOURCE-001` | 🟡 MINOR | `CONTROLFREEC_ASSESSSIGNIFICANCE` | resource_hints | L2519–2565 | — |
| 110 | `RESOURCE-002` | 🟡 MINOR | `CONTROLFREEC_ASSESSSIGNIFICANCE` | resource_hints | L2519–2565 | — |
| 111 | `CONTAINER-001` | 🔴 CRITICAL | `CONTROLFREEC_FREEC` | containerization | L2569–2749 | ✅ |
| 112 | `STORAGE-001` | 🟠 MAJOR | `CONTROLFREEC_FREEC` | storage | L2569–2749 | — |
| 113 | `RESOURCE-001` | 🟡 MINOR | `CONTROLFREEC_FREEC` | resource_hints | L2569–2749 | — |
| 114 | `RESOURCE-002` | 🟡 MINOR | `CONTROLFREEC_FREEC` | resource_hints | L2569–2749 | — |
| 115 | `CONTAINER-001` | 🔴 CRITICAL | `CONTROLFREEC_FREEC2BED` | containerization | L2753–2798 | ✅ |
| 116 | `STORAGE-001` | 🟠 MAJOR | `CONTROLFREEC_FREEC2BED` | storage | L2753–2798 | — |
| 117 | `RESOURCE-001` | 🟡 MINOR | `CONTROLFREEC_FREEC2BED` | resource_hints | L2753–2798 | — |
| 118 | `RESOURCE-002` | 🟡 MINOR | `CONTROLFREEC_FREEC2BED` | resource_hints | L2753–2798 | — |
| 119 | `CONTAINER-001` | 🔴 CRITICAL | `CONTROLFREEC_FREEC2CIRCOS` | containerization | L2802–2847 | ✅ |
| 120 | `STORAGE-001` | 🟠 MAJOR | `CONTROLFREEC_FREEC2CIRCOS` | storage | L2802–2847 | — |
| 121 | `RESOURCE-001` | 🟡 MINOR | `CONTROLFREEC_FREEC2CIRCOS` | resource_hints | L2802–2847 | — |
| 122 | `RESOURCE-002` | 🟡 MINOR | `CONTROLFREEC_FREEC2CIRCOS` | resource_hints | L2802–2847 | — |
| 123 | `CONTAINER-001` | 🔴 CRITICAL | `CONTROLFREEC_MAKEGRAPH2` | containerization | L2851–2906 | ✅ |
| 124 | `STORAGE-001` | 🟠 MAJOR | `CONTROLFREEC_MAKEGRAPH2` | storage | L2851–2906 | — |
| 125 | `RESOURCE-001` | 🟡 MINOR | `CONTROLFREEC_MAKEGRAPH2` | resource_hints | L2851–2906 | — |
| 126 | `RESOURCE-002` | 🟡 MINOR | `CONTROLFREEC_MAKEGRAPH2` | resource_hints | L2851–2906 | — |
| 127 | `STORAGE-001` | 🟠 MAJOR | `DEEPVARIANT_RUNDEEPVARIANT` | storage | L2910–2982 | — |
| 128 | `RESOURCE-001` | 🟡 MINOR | `DEEPVARIANT_RUNDEEPVARIANT` | resource_hints | L2910–2982 | — |
| 129 | `RESOURCE-002` | 🟡 MINOR | `DEEPVARIANT_RUNDEEPVARIANT` | resource_hints | L2910–2982 | — |
| 130 | `CONTAINER-001` | 🔴 CRITICAL | `DRAGMAP_ALIGN` | containerization | L2986–3075 | ✅ |
| 131 | `STORAGE-001` | 🟠 MAJOR | `DRAGMAP_ALIGN` | storage | L2986–3075 | — |
| 132 | `RESOURCE-001` | 🟡 MINOR | `DRAGMAP_ALIGN` | resource_hints | L2986–3075 | — |
| 133 | `RESOURCE-002` | 🟡 MINOR | `DRAGMAP_ALIGN` | resource_hints | L2986–3075 | — |
| 134 | `CONTAINER-001` | 🔴 CRITICAL | `DRAGMAP_HASHTABLE` | containerization | L3079–3125 | ✅ |
| 135 | `RESOURCE-001` | 🟡 MINOR | `DRAGMAP_HASHTABLE` | resource_hints | L3079–3125 | — |
| 136 | `RESOURCE-002` | 🟡 MINOR | `DRAGMAP_HASHTABLE` | resource_hints | L3079–3125 | — |
| 137 | `CONTAINER-001` | 🔴 CRITICAL | `ENSEMBLVEP_DOWNLOAD` | containerization | L3129–3166 | ✅ |
| 138 | `RESOURCE-001` | 🟡 MINOR | `ENSEMBLVEP_DOWNLOAD` | resource_hints | L3129–3166 | — |
| 139 | `RESOURCE-002` | 🟡 MINOR | `ENSEMBLVEP_DOWNLOAD` | resource_hints | L3129–3166 | — |
| 140 | `CONTAINER-001` | 🔴 CRITICAL | `ENSEMBLVEP_VEP` | containerization | L3170–3236 | ✅ |
| 141 | `STORAGE-001` | 🟠 MAJOR | `ENSEMBLVEP_VEP` | storage | L3170–3236 | — |
| 142 | `RESOURCE-001` | 🟡 MINOR | `ENSEMBLVEP_VEP` | resource_hints | L3170–3236 | — |
| 143 | `RESOURCE-002` | 🟡 MINOR | `ENSEMBLVEP_VEP` | resource_hints | L3170–3236 | — |
| 144 | `CONTAINER-001` | 🔴 CRITICAL | `FASTP` | containerization | L3240–3364 | ✅ |
| 145 | `STORAGE-001` | 🟠 MAJOR | `FASTP` | storage | L3240–3364 | — |
| 146 | `RESOURCE-001` | 🟡 MINOR | `FASTP` | resource_hints | L3240–3364 | — |
| 147 | `RESOURCE-002` | 🟡 MINOR | `FASTP` | resource_hints | L3240–3364 | — |
| 148 | `CONTAINER-001` | 🔴 CRITICAL | `FASTQC` | containerization | L3368–3431 | ✅ |
| 149 | `STORAGE-001` | 🟠 MAJOR | `FASTQC` | storage | L3368–3431 | — |
| 150 | `RESOURCE-001` | 🟡 MINOR | `FASTQC` | resource_hints | L3368–3431 | — |
| 151 | `RESOURCE-002` | 🟡 MINOR | `FASTQC` | resource_hints | L3368–3431 | — |
| 152 | `CONTAINER-001` | 🔴 CRITICAL | `FGBIO_CALLMOLECULARCONSENSUSREADS` | containerization | L3435–3498 | ✅ |
| 153 | `STORAGE-001` | 🟠 MAJOR | `FGBIO_CALLMOLECULARCONSENSUSREADS` | storage | L3435–3498 | — |
| 154 | `RESOURCE-001` | 🟡 MINOR | `FGBIO_CALLMOLECULARCONSENSUSREADS` | resource_hints | L3435–3498 | — |
| 155 | `RESOURCE-002` | 🟡 MINOR | `FGBIO_CALLMOLECULARCONSENSUSREADS` | resource_hints | L3435–3498 | — |
| 156 | `CONTAINER-001` | 🔴 CRITICAL | `FGBIO_COPYUMIFROMREADNAME` | containerization | L3502–3565 | ✅ |
| 157 | `STORAGE-001` | 🟠 MAJOR | `FGBIO_COPYUMIFROMREADNAME` | storage | L3502–3565 | — |
| 158 | `RESOURCE-001` | 🟡 MINOR | `FGBIO_COPYUMIFROMREADNAME` | resource_hints | L3502–3565 | — |
| 159 | `RESOURCE-002` | 🟡 MINOR | `FGBIO_COPYUMIFROMREADNAME` | resource_hints | L3502–3565 | — |
| 160 | `CONTAINER-001` | 🔴 CRITICAL | `FGBIO_FASTQTOBAM` | containerization | L3569–3638 | ✅ |
| 161 | `STORAGE-001` | 🟠 MAJOR | `FGBIO_FASTQTOBAM` | storage | L3569–3638 | — |
| 162 | `RESOURCE-001` | 🟡 MINOR | `FGBIO_FASTQTOBAM` | resource_hints | L3569–3638 | — |
| 163 | `RESOURCE-002` | 🟡 MINOR | `FGBIO_FASTQTOBAM` | resource_hints | L3569–3638 | — |
| 164 | `CONTAINER-001` | 🔴 CRITICAL | `FGBIO_GROUPREADSBYUMI` | containerization | L3642–3708 | ✅ |
| 165 | `STORAGE-001` | 🟠 MAJOR | `FGBIO_GROUPREADSBYUMI` | storage | L3642–3708 | — |
| 166 | `RESOURCE-001` | 🟡 MINOR | `FGBIO_GROUPREADSBYUMI` | resource_hints | L3642–3708 | — |
| 167 | `RESOURCE-002` | 🟡 MINOR | `FGBIO_GROUPREADSBYUMI` | resource_hints | L3642–3708 | — |
| 168 | `CONTAINER-001` | 🔴 CRITICAL | `FREEBAYES` | containerization | L3712–3772 | ✅ |
| 169 | `STORAGE-001` | 🟠 MAJOR | `FREEBAYES` | storage | L3712–3772 | — |
| 170 | `RESOURCE-001` | 🟡 MINOR | `FREEBAYES` | resource_hints | L3712–3772 | — |
| 171 | `RESOURCE-002` | 🟡 MINOR | `FREEBAYES` | resource_hints | L3712–3772 | — |
| 172 | `CONTAINER-001` | 🔴 CRITICAL | `GATK4_APPLYBQSR` | containerization | L3776–3847 | ✅ |
| 173 | `STORAGE-001` | 🟠 MAJOR | `GATK4_APPLYBQSR` | storage | L3776–3847 | — |
| 174 | `RESOURCE-001` | 🟡 MINOR | `GATK4_APPLYBQSR` | resource_hints | L3776–3847 | — |
| 175 | `RESOURCE-002` | 🟡 MINOR | `GATK4_APPLYBQSR` | resource_hints | L3776–3847 | — |
| 176 | `CONTAINER-001` | 🔴 CRITICAL | `GATK4_APPLYVQSR` | containerization | L3851–3913 | ✅ |
| 177 | `STORAGE-001` | 🟠 MAJOR | `GATK4_APPLYVQSR` | storage | L3851–3913 | — |
| 178 | `RESOURCE-001` | 🟡 MINOR | `GATK4_APPLYVQSR` | resource_hints | L3851–3913 | — |
| 179 | `RESOURCE-002` | 🟡 MINOR | `GATK4_APPLYVQSR` | resource_hints | L3851–3913 | — |
| 180 | `CONTAINER-001` | 🔴 CRITICAL | `GATK4_BASERECALIBRATOR` | containerization | L3917–3979 | ✅ |
| 181 | `STORAGE-001` | 🟠 MAJOR | `GATK4_BASERECALIBRATOR` | storage | L3917–3979 | — |
| 182 | `RESOURCE-001` | 🟡 MINOR | `GATK4_BASERECALIBRATOR` | resource_hints | L3917–3979 | — |
| 183 | `RESOURCE-002` | 🟡 MINOR | `GATK4_BASERECALIBRATOR` | resource_hints | L3917–3979 | — |
| 184 | `CONTAINER-001` | 🔴 CRITICAL | `GATK4_CALCULATECONTAMINATION` | containerization | L3983–4040 | ✅ |
| 185 | `STORAGE-001` | 🟠 MAJOR | `GATK4_CALCULATECONTAMINATION` | storage | L3983–4040 | — |
| 186 | `RESOURCE-001` | 🟡 MINOR | `GATK4_CALCULATECONTAMINATION` | resource_hints | L3983–4040 | — |
| 187 | `RESOURCE-002` | 🟡 MINOR | `GATK4_CALCULATECONTAMINATION` | resource_hints | L3983–4040 | — |
| 188 | `STORAGE-001` | 🟠 MAJOR | `GATK4_CNNSCOREVARIANTS` | storage | L4044–4118 | — |
| 189 | `RESOURCE-001` | 🟡 MINOR | `GATK4_CNNSCOREVARIANTS` | resource_hints | L4044–4118 | — |
| 190 | `RESOURCE-002` | 🟡 MINOR | `GATK4_CNNSCOREVARIANTS` | resource_hints | L4044–4118 | — |
| 191 | `CONTAINER-001` | 🔴 CRITICAL | `GATK4_CREATESEQUENCEDICTIONARY` | containerization | L4122–4174 | ✅ |
| 192 | `STORAGE-001` | 🟠 MAJOR | `GATK4_CREATESEQUENCEDICTIONARY` | storage | L4122–4174 | — |
| 193 | `RESOURCE-001` | 🟡 MINOR | `GATK4_CREATESEQUENCEDICTIONARY` | resource_hints | L4122–4174 | — |
| 194 | `RESOURCE-002` | 🟡 MINOR | `GATK4_CREATESEQUENCEDICTIONARY` | resource_hints | L4122–4174 | — |
| 195 | `CONTAINER-001` | 🔴 CRITICAL | `GATK4_ESTIMATELIBRARYCOMPLEXITY` | containerization | L4178–4238 | ✅ |
| 196 | `STORAGE-001` | 🟠 MAJOR | `GATK4_ESTIMATELIBRARYCOMPLEXITY` | storage | L4178–4238 | — |
| 197 | `RESOURCE-001` | 🟡 MINOR | `GATK4_ESTIMATELIBRARYCOMPLEXITY` | resource_hints | L4178–4238 | — |
| 198 | `RESOURCE-002` | 🟡 MINOR | `GATK4_ESTIMATELIBRARYCOMPLEXITY` | resource_hints | L4178–4238 | — |
| 199 | `CONTAINER-001` | 🔴 CRITICAL | `GATK4_FILTERMUTECTCALLS` | containerization | L4242–4312 | ✅ |
| 200 | `STORAGE-001` | 🟠 MAJOR | `GATK4_FILTERMUTECTCALLS` | storage | L4242–4312 | — |
| 201 | `RESOURCE-001` | 🟡 MINOR | `GATK4_FILTERMUTECTCALLS` | resource_hints | L4242–4312 | — |
| 202 | `RESOURCE-002` | 🟡 MINOR | `GATK4_FILTERMUTECTCALLS` | resource_hints | L4242–4312 | — |
| 203 | `CONTAINER-001` | 🔴 CRITICAL | `GATK4_FILTERVARIANTTRANCHES` | containerization | L4316–4380 | ✅ |
| 204 | `STORAGE-001` | 🟠 MAJOR | `GATK4_FILTERVARIANTTRANCHES` | storage | L4316–4380 | — |
| 205 | `RESOURCE-001` | 🟡 MINOR | `GATK4_FILTERVARIANTTRANCHES` | resource_hints | L4316–4380 | — |
| 206 | `RESOURCE-002` | 🟡 MINOR | `GATK4_FILTERVARIANTTRANCHES` | resource_hints | L4316–4380 | — |
| 207 | `CONTAINER-001` | 🔴 CRITICAL | `GATK4_GATHERBQSRREPORTS` | containerization | L4384–4427 | ✅ |
| 208 | `STORAGE-001` | 🟠 MAJOR | `GATK4_GATHERBQSRREPORTS` | storage | L4384–4427 | — |
| 209 | `RESOURCE-001` | 🟡 MINOR | `GATK4_GATHERBQSRREPORTS` | resource_hints | L4384–4427 | — |
| 210 | `RESOURCE-002` | 🟡 MINOR | `GATK4_GATHERBQSRREPORTS` | resource_hints | L4384–4427 | — |
| 211 | `CONTAINER-001` | 🔴 CRITICAL | `GATK4_GATHERPILEUPSUMMARIES` | containerization | L4431–4488 | ✅ |
| 212 | `STORAGE-001` | 🟠 MAJOR | `GATK4_GATHERPILEUPSUMMARIES` | storage | L4431–4488 | — |
| 213 | `RESOURCE-001` | 🟡 MINOR | `GATK4_GATHERPILEUPSUMMARIES` | resource_hints | L4431–4488 | — |
| 214 | `RESOURCE-002` | 🟡 MINOR | `GATK4_GATHERPILEUPSUMMARIES` | resource_hints | L4431–4488 | — |
| 215 | `CONTAINER-001` | 🔴 CRITICAL | `GATK4_GENOMICSDBIMPORT` | containerization | L4492–4595 | ✅ |
| 216 | `STORAGE-001` | 🟠 MAJOR | `GATK4_GENOMICSDBIMPORT` | storage | L4492–4595 | — |
| 217 | `RESOURCE-001` | 🟡 MINOR | `GATK4_GENOMICSDBIMPORT` | resource_hints | L4492–4595 | — |
| 218 | `RESOURCE-002` | 🟡 MINOR | `GATK4_GENOMICSDBIMPORT` | resource_hints | L4492–4595 | — |
| 219 | `CONTAINER-001` | 🔴 CRITICAL | `GATK4_GENOTYPEGVCFS` | containerization | L4599–4666 | ✅ |
| 220 | `STORAGE-001` | 🟠 MAJOR | `GATK4_GENOTYPEGVCFS` | storage | L4599–4666 | — |
| 221 | `RESOURCE-001` | 🟡 MINOR | `GATK4_GENOTYPEGVCFS` | resource_hints | L4599–4666 | — |
| 222 | `RESOURCE-002` | 🟡 MINOR | `GATK4_GENOTYPEGVCFS` | resource_hints | L4599–4666 | — |
| 223 | `CONTAINER-001` | 🔴 CRITICAL | `GATK4_GETPILEUPSUMMARIES` | containerization | L4670–4733 | ✅ |
| 224 | `STORAGE-001` | 🟠 MAJOR | `GATK4_GETPILEUPSUMMARIES` | storage | L4670–4733 | — |
| 225 | `RESOURCE-001` | 🟡 MINOR | `GATK4_GETPILEUPSUMMARIES` | resource_hints | L4670–4733 | — |
| 226 | `RESOURCE-002` | 🟡 MINOR | `GATK4_GETPILEUPSUMMARIES` | resource_hints | L4670–4733 | — |
| 227 | `CONTAINER-001` | 🔴 CRITICAL | `GATK4_HAPLOTYPECALLER` | containerization | L4737–4813 | ✅ |
| 228 | `STORAGE-001` | 🟠 MAJOR | `GATK4_HAPLOTYPECALLER` | storage | L4737–4813 | — |
| 229 | `RESOURCE-001` | 🟡 MINOR | `GATK4_HAPLOTYPECALLER` | resource_hints | L4737–4813 | — |
| 230 | `RESOURCE-002` | 🟡 MINOR | `GATK4_HAPLOTYPECALLER` | resource_hints | L4737–4813 | — |
| 231 | `CONTAINER-001` | 🔴 CRITICAL | `GATK4_INTERVALLISTTOBED` | containerization | L4817–4872 | ✅ |
| 232 | `STORAGE-001` | 🟠 MAJOR | `GATK4_INTERVALLISTTOBED` | storage | L4817–4872 | — |
| 233 | `RESOURCE-001` | 🟡 MINOR | `GATK4_INTERVALLISTTOBED` | resource_hints | L4817–4872 | — |
| 234 | `RESOURCE-002` | 🟡 MINOR | `GATK4_INTERVALLISTTOBED` | resource_hints | L4817–4872 | — |
| 235 | `CONTAINER-001` | 🔴 CRITICAL | `GATK4_LEARNREADORIENTATIONMODEL` | containerization | L4876–4919 | ✅ |
| 236 | `STORAGE-001` | 🟠 MAJOR | `GATK4_LEARNREADORIENTATIONMODEL` | storage | L4876–4919 | — |
| 237 | `RESOURCE-001` | 🟡 MINOR | `GATK4_LEARNREADORIENTATIONMODEL` | resource_hints | L4876–4919 | — |
| 238 | `RESOURCE-002` | 🟡 MINOR | `GATK4_LEARNREADORIENTATIONMODEL` | resource_hints | L4876–4919 | — |
| 239 | `CONTAINER-001` | 🔴 CRITICAL | `GATK4_MARKDUPLICATES` | containerization | L4923–5008 | ✅ |
| 240 | `STORAGE-001` | 🟠 MAJOR | `GATK4_MARKDUPLICATES` | storage | L4923–5008 | — |
| 241 | `RESOURCE-001` | 🟡 MINOR | `GATK4_MARKDUPLICATES` | resource_hints | L4923–5008 | — |
| 242 | `RESOURCE-002` | 🟡 MINOR | `GATK4_MARKDUPLICATES` | resource_hints | L4923–5008 | — |
| 243 | `CONTAINER-001` | 🔴 CRITICAL | `GATK4_MERGEMUTECTSTATS` | containerization | L5012–5066 | ✅ |
| 244 | `STORAGE-001` | 🟠 MAJOR | `GATK4_MERGEMUTECTSTATS` | storage | L5012–5066 | — |
| 245 | `RESOURCE-001` | 🟡 MINOR | `GATK4_MERGEMUTECTSTATS` | resource_hints | L5012–5066 | — |
| 246 | `RESOURCE-002` | 🟡 MINOR | `GATK4_MERGEMUTECTSTATS` | resource_hints | L5012–5066 | — |
| 247 | `CONTAINER-001` | 🔴 CRITICAL | `GATK4_MERGEVCFS` | containerization | L5070–5129 | ✅ |
| 248 | `STORAGE-001` | 🟠 MAJOR | `GATK4_MERGEVCFS` | storage | L5070–5129 | — |
| 249 | `RESOURCE-001` | 🟡 MINOR | `GATK4_MERGEVCFS` | resource_hints | L5070–5129 | — |
| 250 | `RESOURCE-002` | 🟡 MINOR | `GATK4_MERGEVCFS` | resource_hints | L5070–5129 | — |
| 251 | `CONTAINER-001` | 🔴 CRITICAL | `GATK4_MUTECT2` | containerization | L5133–5207 | ✅ |
| 252 | `STORAGE-001` | 🟠 MAJOR | `GATK4_MUTECT2` | storage | L5133–5207 | — |
| 253 | `RESOURCE-001` | 🟡 MINOR | `GATK4_MUTECT2` | resource_hints | L5133–5207 | — |
| 254 | `RESOURCE-002` | 🟡 MINOR | `GATK4_MUTECT2` | resource_hints | L5133–5207 | — |
| 255 | `CONTAINER-001` | 🔴 CRITICAL | `GATK4_VARIANTRECALIBRATOR` | containerization | L5211–5281 | ✅ |
| 256 | `STORAGE-001` | 🟠 MAJOR | `GATK4_VARIANTRECALIBRATOR` | storage | L5211–5281 | — |
| 257 | `RESOURCE-001` | 🟡 MINOR | `GATK4_VARIANTRECALIBRATOR` | resource_hints | L5211–5281 | — |
| 258 | `RESOURCE-002` | 🟡 MINOR | `GATK4_VARIANTRECALIBRATOR` | resource_hints | L5211–5281 | — |
| 259 | `CONTAINER-001` | 🔴 CRITICAL | `GATK4SPARK_APPLYBQSR` | containerization | L5285–5355 | ✅ |
| 260 | `STORAGE-001` | 🟠 MAJOR | `GATK4SPARK_APPLYBQSR` | storage | L5285–5355 | — |
| 261 | `RESOURCE-001` | 🟡 MINOR | `GATK4SPARK_APPLYBQSR` | resource_hints | L5285–5355 | — |
| 262 | `RESOURCE-002` | 🟡 MINOR | `GATK4SPARK_APPLYBQSR` | resource_hints | L5285–5355 | — |
| 263 | `CONTAINER-001` | 🔴 CRITICAL | `GATK4SPARK_BASERECALIBRATOR` | containerization | L5359–5425 | ✅ |
| 264 | `STORAGE-001` | 🟠 MAJOR | `GATK4SPARK_BASERECALIBRATOR` | storage | L5359–5425 | — |
| 265 | `RESOURCE-001` | 🟡 MINOR | `GATK4SPARK_BASERECALIBRATOR` | resource_hints | L5359–5425 | — |
| 266 | `RESOURCE-002` | 🟡 MINOR | `GATK4SPARK_BASERECALIBRATOR` | resource_hints | L5359–5425 | — |
| 267 | `CONTAINER-001` | 🔴 CRITICAL | `GATK4SPARK_MARKDUPLICATES` | containerization | L5429–5493 | ✅ |
| 268 | `STORAGE-001` | 🟠 MAJOR | `GATK4SPARK_MARKDUPLICATES` | storage | L5429–5493 | — |
| 269 | `RESOURCE-001` | 🟡 MINOR | `GATK4SPARK_MARKDUPLICATES` | resource_hints | L5429–5493 | — |
| 270 | `RESOURCE-002` | 🟡 MINOR | `GATK4SPARK_MARKDUPLICATES` | resource_hints | L5429–5493 | — |
| 271 | `CONTAINER-001` | 🔴 CRITICAL | `GAWK` | containerization | L5497–5566 | ✅ |
| 272 | `STORAGE-001` | 🟠 MAJOR | `GAWK` | storage | L5497–5566 | — |
| 273 | `RESOURCE-001` | 🟡 MINOR | `GAWK` | resource_hints | L5497–5566 | — |
| 274 | `RESOURCE-002` | 🟡 MINOR | `GAWK` | resource_hints | L5497–5566 | — |
| 275 | `CONTAINER-001` | 🔴 CRITICAL | `GOLEFT_INDEXCOV` | containerization | L5570–5634 | ✅ |
| 276 | `STORAGE-001` | 🟠 MAJOR | `GOLEFT_INDEXCOV` | storage | L5570–5634 | — |
| 277 | `RESOURCE-001` | 🟡 MINOR | `GOLEFT_INDEXCOV` | resource_hints | L5570–5634 | — |
| 278 | `RESOURCE-002` | 🟡 MINOR | `GOLEFT_INDEXCOV` | resource_hints | L5570–5634 | — |
| 279 | `CONTAINER-001` | 🔴 CRITICAL | `GUNZIP` | containerization | L5638–5692 | ✅ |
| 280 | `STORAGE-001` | 🟠 MAJOR | `GUNZIP` | storage | L5638–5692 | — |
| 281 | `RESOURCE-001` | 🟡 MINOR | `GUNZIP` | resource_hints | L5638–5692 | — |
| 282 | `RESOURCE-002` | 🟡 MINOR | `GUNZIP` | resource_hints | L5638–5692 | — |
| 283 | `CONTAINER-001` | 🔴 CRITICAL | `LOFREQ_CALLPARALLEL` | containerization | L5696–5765 | ✅ |
| 284 | `STORAGE-001` | 🟠 MAJOR | `LOFREQ_CALLPARALLEL` | storage | L5696–5765 | — |
| 285 | `RESOURCE-001` | 🟡 MINOR | `LOFREQ_CALLPARALLEL` | resource_hints | L5696–5765 | — |
| 286 | `RESOURCE-002` | 🟡 MINOR | `LOFREQ_CALLPARALLEL` | resource_hints | L5696–5765 | — |
| 287 | `CONTAINER-001` | 🔴 CRITICAL | `MANTA_GERMLINE` | containerization | L5769–5849 | ✅ |
| 288 | `STORAGE-001` | 🟠 MAJOR | `MANTA_GERMLINE` | storage | L5769–5849 | — |
| 289 | `RESOURCE-001` | 🟡 MINOR | `MANTA_GERMLINE` | resource_hints | L5769–5849 | — |
| 290 | `RESOURCE-002` | 🟡 MINOR | `MANTA_GERMLINE` | resource_hints | L5769–5849 | — |
| 291 | `CONTAINER-001` | 🔴 CRITICAL | `MANTA_SOMATIC` | containerization | L5853–5940 | ✅ |
| 292 | `STORAGE-001` | 🟠 MAJOR | `MANTA_SOMATIC` | storage | L5853–5940 | — |
| 293 | `RESOURCE-001` | 🟡 MINOR | `MANTA_SOMATIC` | resource_hints | L5853–5940 | — |
| 294 | `RESOURCE-002` | 🟡 MINOR | `MANTA_SOMATIC` | resource_hints | L5853–5940 | — |
| 295 | `CONTAINER-001` | 🔴 CRITICAL | `MANTA_TUMORONLY` | containerization | L5944–6022 | ✅ |
| 296 | `STORAGE-001` | 🟠 MAJOR | `MANTA_TUMORONLY` | storage | L5944–6022 | — |
| 297 | `RESOURCE-001` | 🟡 MINOR | `MANTA_TUMORONLY` | resource_hints | L5944–6022 | — |
| 298 | `RESOURCE-002` | 🟡 MINOR | `MANTA_TUMORONLY` | resource_hints | L5944–6022 | — |
| 299 | `CONTAINER-001` | 🔴 CRITICAL | `MOSDEPTH` | containerization | L6026–6105 | ✅ |
| 300 | `STORAGE-001` | 🟠 MAJOR | `MOSDEPTH` | storage | L6026–6105 | — |
| 301 | `RESOURCE-001` | 🟡 MINOR | `MOSDEPTH` | resource_hints | L6026–6105 | — |
| 302 | `RESOURCE-002` | 🟡 MINOR | `MOSDEPTH` | resource_hints | L6026–6105 | — |
| 303 | `CONTAINER-001` | 🔴 CRITICAL | `MSISENSOR2_MSI` | containerization | L6109–6160 | ✅ |
| 304 | `STORAGE-001` | 🟠 MAJOR | `MSISENSOR2_MSI` | storage | L6109–6160 | — |
| 305 | `RESOURCE-001` | 🟡 MINOR | `MSISENSOR2_MSI` | resource_hints | L6109–6160 | — |
| 306 | `RESOURCE-002` | 🟡 MINOR | `MSISENSOR2_MSI` | resource_hints | L6109–6160 | — |
| 307 | `CONTAINER-001` | 🔴 CRITICAL | `MSISENSORPRO_MSISOMATIC` | containerization | L6163–6225 | ✅ |
| 308 | `STORAGE-001` | 🟠 MAJOR | `MSISENSORPRO_MSISOMATIC` | storage | L6163–6225 | — |
| 309 | `RESOURCE-001` | 🟡 MINOR | `MSISENSORPRO_MSISOMATIC` | resource_hints | L6163–6225 | — |
| 310 | `RESOURCE-002` | 🟡 MINOR | `MSISENSORPRO_MSISOMATIC` | resource_hints | L6163–6225 | — |
| 311 | `CONTAINER-001` | 🔴 CRITICAL | `MSISENSORPRO_SCAN` | containerization | L6229–6274 | ✅ |
| 312 | `STORAGE-001` | 🟠 MAJOR | `MSISENSORPRO_SCAN` | storage | L6229–6274 | — |
| 313 | `RESOURCE-001` | 🟡 MINOR | `MSISENSORPRO_SCAN` | resource_hints | L6229–6274 | — |
| 314 | `RESOURCE-002` | 🟡 MINOR | `MSISENSORPRO_SCAN` | resource_hints | L6229–6274 | — |
| 315 | `CONTAINER-001` | 🔴 CRITICAL | `MULTIQC` | containerization | L6278–6332 | ✅ |
| 316 | `RESOURCE-001` | 🟡 MINOR | `MULTIQC` | resource_hints | L6278–6332 | — |
| 317 | `RESOURCE-002` | 🟡 MINOR | `MULTIQC` | resource_hints | L6278–6332 | — |
| 318 | `CONTAINER-001` | 🔴 CRITICAL | `MUSE_CALL` | containerization | L6336–6385 | ✅ |
| 319 | `STORAGE-001` | 🟠 MAJOR | `MUSE_CALL` | storage | L6336–6385 | — |
| 320 | `RESOURCE-001` | 🟡 MINOR | `MUSE_CALL` | resource_hints | L6336–6385 | — |
| 321 | `RESOURCE-002` | 🟡 MINOR | `MUSE_CALL` | resource_hints | L6336–6385 | — |
| 322 | `CONTAINER-001` | 🔴 CRITICAL | `MUSE_SUMP` | containerization | L6389–6447 | ✅ |
| 323 | `STORAGE-001` | 🟠 MAJOR | `MUSE_SUMP` | storage | L6389–6447 | — |
| 324 | `RESOURCE-001` | 🟡 MINOR | `MUSE_SUMP` | resource_hints | L6389–6447 | — |
| 325 | `RESOURCE-002` | 🟡 MINOR | `MUSE_SUMP` | resource_hints | L6389–6447 | — |
| 326 | `CONTAINER-001` | 🔴 CRITICAL | `NGSCHECKMATE_NCM` | containerization | L6451–6515 | ✅ |
| 327 | `STORAGE-001` | 🟠 MAJOR | `NGSCHECKMATE_NCM` | storage | L6451–6515 | — |
| 328 | `RESOURCE-001` | 🟡 MINOR | `NGSCHECKMATE_NCM` | resource_hints | L6451–6515 | — |
| 329 | `RESOURCE-002` | 🟡 MINOR | `NGSCHECKMATE_NCM` | resource_hints | L6451–6515 | — |
| 330 | `STORAGE-001` | 🟠 MAJOR | `PARABRICKS_FQ2BAM` | storage | L6519–6635 | — |
| 331 | `RESOURCE-001` | 🟡 MINOR | `PARABRICKS_FQ2BAM` | resource_hints | L6519–6635 | — |
| 332 | `RESOURCE-002` | 🟡 MINOR | `PARABRICKS_FQ2BAM` | resource_hints | L6519–6635 | — |
| 333 | `CONTAINER-001` | 🔴 CRITICAL | `RBT_VCFSPLIT` | containerization | L6639–6686 | ✅ |
| 334 | `RESOURCE-001` | 🟡 MINOR | `RBT_VCFSPLIT` | resource_hints | L6639–6686 | — |
| 335 | `RESOURCE-002` | 🟡 MINOR | `RBT_VCFSPLIT` | resource_hints | L6639–6686 | — |
| 336 | `CONTAINER-001` | 🔴 CRITICAL | `SAMTOOLS_BAM2FQ` | containerization | L6690–6745 | ✅ |
| 337 | `STORAGE-001` | 🟠 MAJOR | `SAMTOOLS_BAM2FQ` | storage | L6690–6745 | — |
| 338 | `RESOURCE-001` | 🟡 MINOR | `SAMTOOLS_BAM2FQ` | resource_hints | L6690–6745 | — |
| 339 | `RESOURCE-002` | 🟡 MINOR | `SAMTOOLS_BAM2FQ` | resource_hints | L6690–6745 | — |
| 340 | `CONTAINER-001` | 🔴 CRITICAL | `SAMTOOLS_COLLATEFASTQ` | containerization | L6749–6824 | ✅ |
| 341 | `STORAGE-001` | 🟠 MAJOR | `SAMTOOLS_COLLATEFASTQ` | storage | L6749–6824 | — |
| 342 | `RESOURCE-001` | 🟡 MINOR | `SAMTOOLS_COLLATEFASTQ` | resource_hints | L6749–6824 | — |
| 343 | `RESOURCE-002` | 🟡 MINOR | `SAMTOOLS_COLLATEFASTQ` | resource_hints | L6749–6824 | — |
| 344 | `CONTAINER-001` | 🔴 CRITICAL | `SAMTOOLS_CONVERT` | containerization | L6828–6887 | ✅ |
| 345 | `STORAGE-001` | 🟠 MAJOR | `SAMTOOLS_CONVERT` | storage | L6828–6887 | — |
| 346 | `RESOURCE-001` | 🟡 MINOR | `SAMTOOLS_CONVERT` | resource_hints | L6828–6887 | — |
| 347 | `RESOURCE-002` | 🟡 MINOR | `SAMTOOLS_CONVERT` | resource_hints | L6828–6887 | — |
| 348 | `CONTAINER-001` | 🔴 CRITICAL | `SAMTOOLS_FAIDX` | containerization | L6891–6951 | ✅ |
| 349 | `STORAGE-001` | 🟠 MAJOR | `SAMTOOLS_FAIDX` | storage | L6891–6951 | — |
| 350 | `RESOURCE-001` | 🟡 MINOR | `SAMTOOLS_FAIDX` | resource_hints | L6891–6951 | — |
| 351 | `RESOURCE-002` | 🟡 MINOR | `SAMTOOLS_FAIDX` | resource_hints | L6891–6951 | — |
| 352 | `CONTAINER-001` | 🔴 CRITICAL | `SAMTOOLS_INDEX` | containerization | L6955–7003 | ✅ |
| 353 | `STORAGE-001` | 🟠 MAJOR | `SAMTOOLS_INDEX` | storage | L6955–7003 | — |
| 354 | `RESOURCE-001` | 🟡 MINOR | `SAMTOOLS_INDEX` | resource_hints | L6955–7003 | — |
| 355 | `RESOURCE-002` | 🟡 MINOR | `SAMTOOLS_INDEX` | resource_hints | L6955–7003 | — |
| 356 | `CONTAINER-001` | 🔴 CRITICAL | `SAMTOOLS_MERGE` | containerization | L7007–7067 | ✅ |
| 357 | `STORAGE-001` | 🟠 MAJOR | `SAMTOOLS_MERGE` | storage | L7007–7067 | — |
| 358 | `RESOURCE-001` | 🟡 MINOR | `SAMTOOLS_MERGE` | resource_hints | L7007–7067 | — |
| 359 | `RESOURCE-002` | 🟡 MINOR | `SAMTOOLS_MERGE` | resource_hints | L7007–7067 | — |
| 360 | `CONTAINER-001` | 🔴 CRITICAL | `SAMTOOLS_MPILEUP` | containerization | L7071–7121 | ✅ |
| 361 | `STORAGE-001` | 🟠 MAJOR | `SAMTOOLS_MPILEUP` | storage | L7071–7121 | — |
| 362 | `RESOURCE-001` | 🟡 MINOR | `SAMTOOLS_MPILEUP` | resource_hints | L7071–7121 | — |
| 363 | `RESOURCE-002` | 🟡 MINOR | `SAMTOOLS_MPILEUP` | resource_hints | L7071–7121 | — |
| 364 | `CONTAINER-001` | 🔴 CRITICAL | `SAMTOOLS_STATS` | containerization | L7125–7172 | ✅ |
| 365 | `STORAGE-001` | 🟠 MAJOR | `SAMTOOLS_STATS` | storage | L7125–7172 | — |
| 366 | `RESOURCE-001` | 🟡 MINOR | `SAMTOOLS_STATS` | resource_hints | L7125–7172 | — |
| 367 | `RESOURCE-002` | 🟡 MINOR | `SAMTOOLS_STATS` | resource_hints | L7125–7172 | — |
| 368 | `CONTAINER-001` | 🔴 CRITICAL | `SAMTOOLS_VIEW` | containerization | L7176–7278 | ✅ |
| 369 | `STORAGE-001` | 🟠 MAJOR | `SAMTOOLS_VIEW` | storage | L7176–7278 | — |
| 370 | `RESOURCE-001` | 🟡 MINOR | `SAMTOOLS_VIEW` | resource_hints | L7176–7278 | — |
| 371 | `RESOURCE-002` | 🟡 MINOR | `SAMTOOLS_VIEW` | resource_hints | L7176–7278 | — |
| 372 | `CONTAINER-001` | 🔴 CRITICAL | `SENTIEON_APPLYVARCAL` | containerization | L7282–7343 | ✅ |
| 373 | `STORAGE-001` | 🟠 MAJOR | `SENTIEON_APPLYVARCAL` | storage | L7282–7343 | — |
| 374 | `RESOURCE-001` | 🟡 MINOR | `SENTIEON_APPLYVARCAL` | resource_hints | L7282–7343 | — |
| 375 | `RESOURCE-002` | 🟡 MINOR | `SENTIEON_APPLYVARCAL` | resource_hints | L7282–7343 | — |
| 376 | `CONTAINER-001` | 🔴 CRITICAL | `SENTIEON_BWAMEM` | containerization | L7347–7416 | ✅ |
| 377 | `STORAGE-001` | 🟠 MAJOR | `SENTIEON_BWAMEM` | storage | L7347–7416 | — |
| 378 | `RESOURCE-001` | 🟡 MINOR | `SENTIEON_BWAMEM` | resource_hints | L7347–7416 | — |
| 379 | `RESOURCE-002` | 🟡 MINOR | `SENTIEON_BWAMEM` | resource_hints | L7347–7416 | — |
| 380 | `CONTAINER-001` | 🔴 CRITICAL | `SENTIEON_DEDUP` | containerization | L7420–7494 | ✅ |
| 381 | `STORAGE-001` | 🟠 MAJOR | `SENTIEON_DEDUP` | storage | L7420–7494 | — |
| 382 | `RESOURCE-001` | 🟡 MINOR | `SENTIEON_DEDUP` | resource_hints | L7420–7494 | — |
| 383 | `RESOURCE-002` | 🟡 MINOR | `SENTIEON_DEDUP` | resource_hints | L7420–7494 | — |
| 384 | `CONTAINER-001` | 🔴 CRITICAL | `SENTIEON_DNAMODELAPPLY` | containerization | L7498–7557 | ✅ |
| 385 | `STORAGE-001` | 🟠 MAJOR | `SENTIEON_DNAMODELAPPLY` | storage | L7498–7557 | — |
| 386 | `RESOURCE-001` | 🟡 MINOR | `SENTIEON_DNAMODELAPPLY` | resource_hints | L7498–7557 | — |
| 387 | `RESOURCE-002` | 🟡 MINOR | `SENTIEON_DNAMODELAPPLY` | resource_hints | L7498–7557 | — |
| 388 | `CONTAINER-001` | 🔴 CRITICAL | `SENTIEON_DNASCOPE` | containerization | L7561–7648 | ✅ |
| 389 | `STORAGE-001` | 🟠 MAJOR | `SENTIEON_DNASCOPE` | storage | L7561–7648 | — |
| 390 | `RESOURCE-001` | 🟡 MINOR | `SENTIEON_DNASCOPE` | resource_hints | L7561–7648 | — |
| 391 | `RESOURCE-002` | 🟡 MINOR | `SENTIEON_DNASCOPE` | resource_hints | L7561–7648 | — |
| 392 | `CONTAINER-001` | 🔴 CRITICAL | `SENTIEON_GVCFTYPER` | containerization | L7652–7706 | ✅ |
| 393 | `STORAGE-001` | 🟠 MAJOR | `SENTIEON_GVCFTYPER` | storage | L7652–7706 | — |
| 394 | `RESOURCE-001` | 🟡 MINOR | `SENTIEON_GVCFTYPER` | resource_hints | L7652–7706 | — |
| 395 | `RESOURCE-002` | 🟡 MINOR | `SENTIEON_GVCFTYPER` | resource_hints | L7652–7706 | — |
| 396 | `CONTAINER-001` | 🔴 CRITICAL | `SENTIEON_HAPLOTYPER` | containerization | L7710–7802 | ✅ |
| 397 | `STORAGE-001` | 🟠 MAJOR | `SENTIEON_HAPLOTYPER` | storage | L7710–7802 | — |
| 398 | `RESOURCE-001` | 🟡 MINOR | `SENTIEON_HAPLOTYPER` | resource_hints | L7710–7802 | — |
| 399 | `RESOURCE-002` | 🟡 MINOR | `SENTIEON_HAPLOTYPER` | resource_hints | L7710–7802 | — |
| 400 | `CONTAINER-001` | 🔴 CRITICAL | `SENTIEON_TNSCOPE` | containerization | L7806–7881 | ✅ |
| 401 | `STORAGE-001` | 🟠 MAJOR | `SENTIEON_TNSCOPE` | storage | L7806–7881 | — |
| 402 | `RESOURCE-001` | 🟡 MINOR | `SENTIEON_TNSCOPE` | resource_hints | L7806–7881 | — |
| 403 | `RESOURCE-002` | 🟡 MINOR | `SENTIEON_TNSCOPE` | resource_hints | L7806–7881 | — |
| 404 | `CONTAINER-001` | 🔴 CRITICAL | `SENTIEON_VARCAL` | containerization | L7885–7982 | ✅ |
| 405 | `STORAGE-001` | 🟠 MAJOR | `SENTIEON_VARCAL` | storage | L7885–7982 | — |
| 406 | `RESOURCE-001` | 🟡 MINOR | `SENTIEON_VARCAL` | resource_hints | L7885–7982 | — |
| 407 | `RESOURCE-002` | 🟡 MINOR | `SENTIEON_VARCAL` | resource_hints | L7885–7982 | — |
| 408 | `CONTAINER-001` | 🔴 CRITICAL | `SNPEFF_DOWNLOAD` | containerization | L7986–8040 | ✅ |
| 409 | `STORAGE-001` | 🟠 MAJOR | `SNPEFF_DOWNLOAD` | storage | L7986–8040 | — |
| 410 | `RESOURCE-001` | 🟡 MINOR | `SNPEFF_DOWNLOAD` | resource_hints | L7986–8040 | — |
| 411 | `RESOURCE-002` | 🟡 MINOR | `SNPEFF_DOWNLOAD` | resource_hints | L7986–8040 | — |
| 412 | `CONTAINER-001` | 🔴 CRITICAL | `SNPEFF_SNPEFF` | containerization | L8044–8108 | ✅ |
| 413 | `RESOURCE-001` | 🟡 MINOR | `SNPEFF_SNPEFF` | resource_hints | L8044–8108 | — |
| 414 | `RESOURCE-002` | 🟡 MINOR | `SNPEFF_SNPEFF` | resource_hints | L8044–8108 | — |
| 415 | `CONTAINER-001` | 🔴 CRITICAL | `SNPSIFT_ANNMEM` | containerization | L8112–8166 | ✅ |
| 416 | `STORAGE-001` | 🟠 MAJOR | `SNPSIFT_ANNMEM` | storage | L8112–8166 | — |
| 417 | `RESOURCE-001` | 🟡 MINOR | `SNPSIFT_ANNMEM` | resource_hints | L8112–8166 | — |
| 418 | `RESOURCE-002` | 🟡 MINOR | `SNPSIFT_ANNMEM` | resource_hints | L8112–8166 | — |
| 419 | `CONTAINER-001` | 🔴 CRITICAL | `SNPSIFT_ANNMEMCREATE` | containerization | L8170–8207 | ✅ |
| 420 | `RESOURCE-001` | 🟡 MINOR | `SNPSIFT_ANNMEMCREATE` | resource_hints | L8170–8207 | — |
| 421 | `RESOURCE-002` | 🟡 MINOR | `SNPSIFT_ANNMEMCREATE` | resource_hints | L8170–8207 | — |
| 422 | `CONTAINER-001` | 🔴 CRITICAL | `SPRING_DECOMPRESS` | containerization | L8211–8264 | ✅ |
| 423 | `STORAGE-001` | 🟠 MAJOR | `SPRING_DECOMPRESS` | storage | L8211–8264 | — |
| 424 | `RESOURCE-001` | 🟡 MINOR | `SPRING_DECOMPRESS` | resource_hints | L8211–8264 | — |
| 425 | `RESOURCE-002` | 🟡 MINOR | `SPRING_DECOMPRESS` | resource_hints | L8211–8264 | — |
| 426 | `CONTAINER-001` | 🔴 CRITICAL | `STRELKA_GERMLINE` | containerization | L8268–8332 | ✅ |
| 427 | `STORAGE-001` | 🟠 MAJOR | `STRELKA_GERMLINE` | storage | L8268–8332 | — |
| 428 | `RESOURCE-001` | 🟡 MINOR | `STRELKA_GERMLINE` | resource_hints | L8268–8332 | — |
| 429 | `RESOURCE-002` | 🟡 MINOR | `STRELKA_GERMLINE` | resource_hints | L8268–8332 | — |
| 430 | `CONTAINER-001` | 🔴 CRITICAL | `STRELKA_SOMATIC` | containerization | L8336–8403 | ✅ |
| 431 | `STORAGE-001` | 🟠 MAJOR | `STRELKA_SOMATIC` | storage | L8336–8403 | — |
| 432 | `RESOURCE-001` | 🟡 MINOR | `STRELKA_SOMATIC` | resource_hints | L8336–8403 | — |
| 433 | `RESOURCE-002` | 🟡 MINOR | `STRELKA_SOMATIC` | resource_hints | L8336–8403 | — |
| 434 | `CONTAINER-001` | 🔴 CRITICAL | `SVDB_MERGE` | containerization | L8407–8511 | ✅ |
| 435 | `STORAGE-001` | 🟠 MAJOR | `SVDB_MERGE` | storage | L8407–8511 | — |
| 436 | `RESOURCE-001` | 🟡 MINOR | `SVDB_MERGE` | resource_hints | L8407–8511 | — |
| 437 | `RESOURCE-002` | 🟡 MINOR | `SVDB_MERGE` | resource_hints | L8407–8511 | — |
| 438 | `CONTAINER-001` | 🔴 CRITICAL | `TABIX_BGZIPTABIX` | containerization | L8515–8562 | ✅ |
| 439 | `STORAGE-001` | 🟠 MAJOR | `TABIX_BGZIPTABIX` | storage | L8515–8562 | — |
| 440 | `RESOURCE-001` | 🟡 MINOR | `TABIX_BGZIPTABIX` | resource_hints | L8515–8562 | — |
| 441 | `RESOURCE-002` | 🟡 MINOR | `TABIX_BGZIPTABIX` | resource_hints | L8515–8562 | — |
| 442 | `CONTAINER-001` | 🔴 CRITICAL | `TABIX_TABIX` | containerization | L8566–8610 | ✅ |
| 443 | `STORAGE-001` | 🟠 MAJOR | `TABIX_TABIX` | storage | L8566–8610 | — |
| 444 | `RESOURCE-001` | 🟡 MINOR | `TABIX_TABIX` | resource_hints | L8566–8610 | — |
| 445 | `RESOURCE-002` | 🟡 MINOR | `TABIX_TABIX` | resource_hints | L8566–8610 | — |
| 446 | `CONTAINER-001` | 🔴 CRITICAL | `TIDDIT_SV` | containerization | L8614–8669 | ✅ |
| 447 | `STORAGE-001` | 🟠 MAJOR | `TIDDIT_SV` | storage | L8614–8669 | — |
| 448 | `RESOURCE-001` | 🟡 MINOR | `TIDDIT_SV` | resource_hints | L8614–8669 | — |
| 449 | `RESOURCE-002` | 🟡 MINOR | `TIDDIT_SV` | resource_hints | L8614–8669 | — |
| 450 | `CONTAINER-001` | 🔴 CRITICAL | `UNTAR` | containerization | L8673–8756 | ✅ |
| 451 | `STORAGE-001` | 🟠 MAJOR | `UNTAR` | storage | L8673–8756 | — |
| 452 | `RESOURCE-001` | 🟡 MINOR | `UNTAR` | resource_hints | L8673–8756 | — |
| 453 | `RESOURCE-002` | 🟡 MINOR | `UNTAR` | resource_hints | L8673–8756 | — |
| 454 | `CONTAINER-001` | 🔴 CRITICAL | `UNZIP` | containerization | L8760–8808 | ✅ |
| 455 | `STORAGE-001` | 🟠 MAJOR | `UNZIP` | storage | L8760–8808 | — |
| 456 | `RESOURCE-001` | 🟡 MINOR | `UNZIP` | resource_hints | L8760–8808 | — |
| 457 | `RESOURCE-002` | 🟡 MINOR | `UNZIP` | resource_hints | L8760–8808 | — |
| 458 | `CONTAINER-001` | 🔴 CRITICAL | `VARLOCIRAPTOR_CALLVARIANTS` | containerization | L8812–8862 | ✅ |
| 459 | `STORAGE-001` | 🟠 MAJOR | `VARLOCIRAPTOR_CALLVARIANTS` | storage | L8812–8862 | — |
| 460 | `RESOURCE-001` | 🟡 MINOR | `VARLOCIRAPTOR_CALLVARIANTS` | resource_hints | L8812–8862 | — |
| 461 | `RESOURCE-002` | 🟡 MINOR | `VARLOCIRAPTOR_CALLVARIANTS` | resource_hints | L8812–8862 | — |
| 462 | `CONTAINER-001` | 🔴 CRITICAL | `VARLOCIRAPTOR_ESTIMATEALIGNMENTPROPERTIES` | containerization | L8866–8913 | ✅ |
| 463 | `STORAGE-001` | 🟠 MAJOR | `VARLOCIRAPTOR_ESTIMATEALIGNMENTPROPERTIES` | storage | L8866–8913 | — |
| 464 | `RESOURCE-001` | 🟡 MINOR | `VARLOCIRAPTOR_ESTIMATEALIGNMENTPROPERTIES` | resource_hints | L8866–8913 | — |
| 465 | `RESOURCE-002` | 🟡 MINOR | `VARLOCIRAPTOR_ESTIMATEALIGNMENTPROPERTIES` | resource_hints | L8866–8913 | — |
| 466 | `CONTAINER-001` | 🔴 CRITICAL | `VARLOCIRAPTOR_PREPROCESS` | containerization | L8917–8967 | ✅ |
| 467 | `STORAGE-001` | 🟠 MAJOR | `VARLOCIRAPTOR_PREPROCESS` | storage | L8917–8967 | — |
| 468 | `RESOURCE-001` | 🟡 MINOR | `VARLOCIRAPTOR_PREPROCESS` | resource_hints | L8917–8967 | — |
| 469 | `RESOURCE-002` | 🟡 MINOR | `VARLOCIRAPTOR_PREPROCESS` | resource_hints | L8917–8967 | — |
| 470 | `CONTAINER-001` | 🔴 CRITICAL | `VCFLIB_VCFFILTER` | containerization | L8971–9029 | ✅ |
| 471 | `STORAGE-001` | 🟠 MAJOR | `VCFLIB_VCFFILTER` | storage | L8971–9029 | — |
| 472 | `RESOURCE-001` | 🟡 MINOR | `VCFLIB_VCFFILTER` | resource_hints | L8971–9029 | — |
| 473 | `RESOURCE-002` | 🟡 MINOR | `VCFLIB_VCFFILTER` | resource_hints | L8971–9029 | — |
| 474 | `CONTAINER-001` | 🔴 CRITICAL | `VCFTOOLS` | containerization | L9033–9231 | ✅ |
| 475 | `STORAGE-001` | 🟠 MAJOR | `VCFTOOLS` | storage | L9033–9231 | — |
| 476 | `RESOURCE-001` | 🟡 MINOR | `VCFTOOLS` | resource_hints | L9033–9231 | — |
| 477 | `RESOURCE-002` | 🟡 MINOR | `VCFTOOLS` | resource_hints | L9033–9231 | — |
| 478 | `CONTAINER-001` | 🔴 CRITICAL | `YTE` | containerization | L9235–9284 | ✅ |
| 479 | `STORAGE-001` | 🟠 MAJOR | `YTE` | storage | L9235–9284 | — |
| 480 | `RESOURCE-001` | 🟡 MINOR | `YTE` | resource_hints | L9235–9284 | — |
| 481 | `RESOURCE-002` | 🟡 MINOR | `YTE` | resource_hints | L9235–9284 | — |

### Detail

<details><summary>🔴 <strong>1. CONTAINER-001 — ADD_INFO_TO_VCF</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L417–457  
**Auto-fixable:** Yes

**Description:**  
Process 'ADD_INFO_TO_VCF' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟠 <strong>2. STORAGE-001 — ADD_INFO_TO_VCF</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L417–457  
**Auto-fixable:** No

**Description:**  
Process 'ADD_INFO_TO_VCF' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
/., //, //
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>3. RESOURCE-001 — ADD_INFO_TO_VCF</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L417–457  
**Auto-fixable:** No

**Description:**  
Process 'ADD_INFO_TO_VCF' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>4. RESOURCE-002 — ADD_INFO_TO_VCF</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L417–457  
**Auto-fixable:** No

**Description:**  
Process 'ADD_INFO_TO_VCF' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>5. CONTAINER-001 — CONSENSUS_FROM_SITES</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L464–521  
**Auto-fixable:** Yes

**Description:**  
Process 'CONSENSUS_FROM_SITES' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟠 <strong>6. STORAGE-001 — CONSENSUS_FROM_SITES</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L464–521  
**Auto-fixable:** No

**Description:**  
Process 'CONSENSUS_FROM_SITES' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
/sites.txt
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>7. RESOURCE-001 — CONSENSUS_FROM_SITES</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L464–521  
**Auto-fixable:** No

**Description:**  
Process 'CONSENSUS_FROM_SITES' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>8. RESOURCE-002 — CONSENSUS_FROM_SITES</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L464–521  
**Auto-fixable:** No

**Description:**  
Process 'CONSENSUS_FROM_SITES' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>9. CONTAINER-001 — CREATE_INTERVALS_BED</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L525–612  
**Auto-fixable:** Yes

**Description:**  
Process 'CREATE_INTERVALS_BED' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟠 <strong>10. STORAGE-001 — CREATE_INTERVALS_BED</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L525–612  
**Auto-fixable:** No

**Description:**  
Process 'CREATE_INTERVALS_BED' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
//, //, // ... (9 more)
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>11. RESOURCE-001 — CREATE_INTERVALS_BED</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L525–612  
**Auto-fixable:** No

**Description:**  
Process 'CREATE_INTERVALS_BED' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>12. RESOURCE-002 — CREATE_INTERVALS_BED</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L525–612  
**Auto-fixable:** No

**Description:**  
Process 'CREATE_INTERVALS_BED' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>13. CONTAINER-001 — SAMTOOLS_REINDEX_BAM</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L620–672  
**Auto-fixable:** Yes

**Description:**  
Process 'SAMTOOLS_REINDEX_BAM' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟠 <strong>14. STORAGE-001 — SAMTOOLS_REINDEX_BAM</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L620–672  
**Auto-fixable:** No

**Description:**  
Process 'SAMTOOLS_REINDEX_BAM' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
/dev/null, //, /Using. ... (1 more)
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>15. RESOURCE-001 — SAMTOOLS_REINDEX_BAM</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L620–672  
**Auto-fixable:** No

**Description:**  
Process 'SAMTOOLS_REINDEX_BAM' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>16. RESOURCE-002 — SAMTOOLS_REINDEX_BAM</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L620–672  
**Auto-fixable:** No

**Description:**  
Process 'SAMTOOLS_REINDEX_BAM' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>17. CONTAINER-001 — ASCAT</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L676–932  
**Auto-fixable:** Yes

**Description:**  
Process 'ASCAT' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟠 <strong>18. STORAGE-001 — ASCAT</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L676–932  
**Auto-fixable:** No

**Description:**  
Process 'ASCAT' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
/usr/bin/env
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>19. RESOURCE-001 — ASCAT</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L676–932  
**Auto-fixable:** No

**Description:**  
Process 'ASCAT' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>20. RESOURCE-002 — ASCAT</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L676–932  
**Auto-fixable:** No

**Description:**  
Process 'ASCAT' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>21. CONTAINER-001 — BBMAP_BBSPLIT</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L936–1065  
**Auto-fixable:** Yes

**Description:**  
Process 'BBMAP_BBSPLIT' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟠 <strong>22. STORAGE-001 — BBMAP_BBSPLIT</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L936–1065  
**Auto-fixable:** No

**Description:**  
Process 'BBMAP_BBSPLIT' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
/ref, /ref/genome, /ref/ ... (7 more)
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>23. RESOURCE-001 — BBMAP_BBSPLIT</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L936–1065  
**Auto-fixable:** No

**Description:**  
Process 'BBMAP_BBSPLIT' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>24. RESOURCE-002 — BBMAP_BBSPLIT</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L936–1065  
**Auto-fixable:** No

**Description:**  
Process 'BBMAP_BBSPLIT' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>25. CONTAINER-001 — BCFTOOLS_ANNOTATE</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L1069–1155  
**Auto-fixable:** Yes

**Description:**  
Process 'BCFTOOLS_ANNOTATE' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟠 <strong>26. STORAGE-001 — BCFTOOLS_ANNOTATE</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L1069–1155  
**Auto-fixable:** No

**Description:**  
Process 'BCFTOOLS_ANNOTATE' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
//
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>27. RESOURCE-001 — BCFTOOLS_ANNOTATE</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L1069–1155  
**Auto-fixable:** No

**Description:**  
Process 'BCFTOOLS_ANNOTATE' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>28. RESOURCE-002 — BCFTOOLS_ANNOTATE</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L1069–1155  
**Auto-fixable:** No

**Description:**  
Process 'BCFTOOLS_ANNOTATE' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>29. CONTAINER-001 — BCFTOOLS_CONCAT</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L1159–1230  
**Auto-fixable:** Yes

**Description:**  
Process 'BCFTOOLS_CONCAT' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟠 <strong>30. STORAGE-001 — BCFTOOLS_CONCAT</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L1159–1230  
**Auto-fixable:** No

**Description:**  
Process 'BCFTOOLS_CONCAT' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
//, //
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>31. RESOURCE-001 — BCFTOOLS_CONCAT</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L1159–1230  
**Auto-fixable:** No

**Description:**  
Process 'BCFTOOLS_CONCAT' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>32. RESOURCE-002 — BCFTOOLS_CONCAT</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L1159–1230  
**Auto-fixable:** No

**Description:**  
Process 'BCFTOOLS_CONCAT' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>33. CONTAINER-001 — BCFTOOLS_ISEC</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L1234–1284  
**Auto-fixable:** Yes

**Description:**  
Process 'BCFTOOLS_ISEC' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟠 <strong>34. STORAGE-001 — BCFTOOLS_ISEC</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L1234–1284  
**Auto-fixable:** No

**Description:**  
Process 'BCFTOOLS_ISEC' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
//, //
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>35. RESOURCE-001 — BCFTOOLS_ISEC</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L1234–1284  
**Auto-fixable:** No

**Description:**  
Process 'BCFTOOLS_ISEC' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>36. RESOURCE-002 — BCFTOOLS_ISEC</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L1234–1284  
**Auto-fixable:** No

**Description:**  
Process 'BCFTOOLS_ISEC' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>37. CONTAINER-001 — BCFTOOLS_MERGE</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L1288–1361  
**Auto-fixable:** Yes

**Description:**  
Process 'BCFTOOLS_MERGE' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟠 <strong>38. STORAGE-001 — BCFTOOLS_MERGE</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L1288–1361  
**Auto-fixable:** No

**Description:**  
Process 'BCFTOOLS_MERGE' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
//, //
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>39. RESOURCE-001 — BCFTOOLS_MERGE</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L1288–1361  
**Auto-fixable:** No

**Description:**  
Process 'BCFTOOLS_MERGE' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>40. RESOURCE-002 — BCFTOOLS_MERGE</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L1288–1361  
**Auto-fixable:** No

**Description:**  
Process 'BCFTOOLS_MERGE' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>41. CONTAINER-001 — BCFTOOLS_MPILEUP</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L1365–1436  
**Auto-fixable:** Yes

**Description:**  
Process 'BCFTOOLS_MPILEUP' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟠 <strong>42. STORAGE-001 — BCFTOOLS_MPILEUP</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L1365–1436  
**Auto-fixable:** No

**Description:**  
Process 'BCFTOOLS_MPILEUP' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
//, //
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>43. RESOURCE-001 — BCFTOOLS_MPILEUP</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L1365–1436  
**Auto-fixable:** No

**Description:**  
Process 'BCFTOOLS_MPILEUP' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>44. RESOURCE-002 — BCFTOOLS_MPILEUP</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L1365–1436  
**Auto-fixable:** No

**Description:**  
Process 'BCFTOOLS_MPILEUP' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>45. CONTAINER-001 — BCFTOOLS_NORM</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L1440–1513  
**Auto-fixable:** Yes

**Description:**  
Process 'BCFTOOLS_NORM' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟠 <strong>46. STORAGE-001 — BCFTOOLS_NORM</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L1440–1513  
**Auto-fixable:** No

**Description:**  
Process 'BCFTOOLS_NORM' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
//, //
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>47. RESOURCE-001 — BCFTOOLS_NORM</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L1440–1513  
**Auto-fixable:** No

**Description:**  
Process 'BCFTOOLS_NORM' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>48. RESOURCE-002 — BCFTOOLS_NORM</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L1440–1513  
**Auto-fixable:** No

**Description:**  
Process 'BCFTOOLS_NORM' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>49. CONTAINER-001 — BCFTOOLS_SORT</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L1517–1586  
**Auto-fixable:** Yes

**Description:**  
Process 'BCFTOOLS_SORT' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟠 <strong>50. STORAGE-001 — BCFTOOLS_SORT</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L1517–1586  
**Auto-fixable:** No

**Description:**  
Process 'BCFTOOLS_SORT' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
//, //
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>51. RESOURCE-001 — BCFTOOLS_SORT</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L1517–1586  
**Auto-fixable:** No

**Description:**  
Process 'BCFTOOLS_SORT' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>52. RESOURCE-002 — BCFTOOLS_SORT</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L1517–1586  
**Auto-fixable:** No

**Description:**  
Process 'BCFTOOLS_SORT' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>53. CONTAINER-001 — BCFTOOLS_STATS</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L1590–1649  
**Auto-fixable:** Yes

**Description:**  
Process 'BCFTOOLS_STATS' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟠 <strong>54. STORAGE-001 — BCFTOOLS_STATS</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L1590–1649  
**Auto-fixable:** No

**Description:**  
Process 'BCFTOOLS_STATS' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
//, //
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>55. RESOURCE-001 — BCFTOOLS_STATS</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L1590–1649  
**Auto-fixable:** No

**Description:**  
Process 'BCFTOOLS_STATS' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>56. RESOURCE-002 — BCFTOOLS_STATS</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L1590–1649  
**Auto-fixable:** No

**Description:**  
Process 'BCFTOOLS_STATS' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>57. CONTAINER-001 — BCFTOOLS_VIEW</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L1653–1727  
**Auto-fixable:** Yes

**Description:**  
Process 'BCFTOOLS_VIEW' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟠 <strong>58. STORAGE-001 — BCFTOOLS_VIEW</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L1653–1727  
**Auto-fixable:** No

**Description:**  
Process 'BCFTOOLS_VIEW' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
//, //
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>59. RESOURCE-001 — BCFTOOLS_VIEW</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L1653–1727  
**Auto-fixable:** No

**Description:**  
Process 'BCFTOOLS_VIEW' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>60. RESOURCE-002 — BCFTOOLS_VIEW</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L1653–1727  
**Auto-fixable:** No

**Description:**  
Process 'BCFTOOLS_VIEW' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>61. CONTAINER-001 — BWA_INDEX</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L1731–1785  
**Auto-fixable:** Yes

**Description:**  
Process 'BWA_INDEX' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟠 <strong>62. STORAGE-001 — BWA_INDEX</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L1731–1785  
**Auto-fixable:** No

**Description:**  
Process 'BWA_INDEX' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
//, /Contact, //
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>63. RESOURCE-001 — BWA_INDEX</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L1731–1785  
**Auto-fixable:** No

**Description:**  
Process 'BWA_INDEX' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🔴 <strong>64. CONTAINER-001 — BWA_MEM</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L1789–1862  
**Auto-fixable:** Yes

**Description:**  
Process 'BWA_MEM' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟠 <strong>65. STORAGE-001 — BWA_MEM</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L1789–1862  
**Auto-fixable:** No

**Description:**  
Process 'BWA_MEM' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
//, //, /Contact ... (4 more)
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>66. RESOURCE-001 — BWA_MEM</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L1789–1862  
**Auto-fixable:** No

**Description:**  
Process 'BWA_MEM' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>67. RESOURCE-002 — BWA_MEM</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L1789–1862  
**Auto-fixable:** No

**Description:**  
Process 'BWA_MEM' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>68. CONTAINER-001 — BWAMEM2_INDEX</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L1866–1920  
**Auto-fixable:** Yes

**Description:**  
Process 'BWAMEM2_INDEX' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟠 <strong>69. STORAGE-001 — BWAMEM2_INDEX</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L1866–1920  
**Auto-fixable:** No

**Description:**  
Process 'BWAMEM2_INDEX' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
/., //
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>70. RESOURCE-001 — BWAMEM2_INDEX</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L1866–1920  
**Auto-fixable:** No

**Description:**  
Process 'BWAMEM2_INDEX' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🔴 <strong>71. CONTAINER-001 — BWAMEM2_MEM</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L1924–2006  
**Auto-fixable:** Yes

**Description:**  
Process 'BWAMEM2_MEM' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟠 <strong>72. STORAGE-001 — BWAMEM2_MEM</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L1924–2006  
**Auto-fixable:** No

**Description:**  
Process 'BWAMEM2_MEM' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
//, /., // ... (3 more)
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>73. RESOURCE-001 — BWAMEM2_MEM</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L1924–2006  
**Auto-fixable:** No

**Description:**  
Process 'BWAMEM2_MEM' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>74. RESOURCE-002 — BWAMEM2_MEM</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L1924–2006  
**Auto-fixable:** No

**Description:**  
Process 'BWAMEM2_MEM' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>75. CONTAINER-001 — CAT_CAT</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L2010–2081  
**Auto-fixable:** Yes

**Description:**  
Process 'CAT_CAT' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟠 <strong>76. STORAGE-001 — CAT_CAT</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L2010–2081  
**Auto-fixable:** No

**Description:**  
Process 'CAT_CAT' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
//, //, // ... (7 more)
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>77. RESOURCE-001 — CAT_CAT</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L2010–2081  
**Auto-fixable:** No

**Description:**  
Process 'CAT_CAT' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>78. RESOURCE-002 — CAT_CAT</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L2010–2081  
**Auto-fixable:** No

**Description:**  
Process 'CAT_CAT' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>79. CONTAINER-001 — CAT_FASTQ</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L2091–2178  
**Auto-fixable:** Yes

**Description:**  
Process 'CAT_FASTQ' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟠 <strong>80. STORAGE-001 — CAT_FASTQ</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L2091–2178  
**Auto-fixable:** No

**Description:**  
Process 'CAT_FASTQ' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
//, //, // ... (1 more)
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>81. RESOURCE-001 — CAT_FASTQ</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L2091–2178  
**Auto-fixable:** No

**Description:**  
Process 'CAT_FASTQ' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>82. RESOURCE-002 — CAT_FASTQ</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L2091–2178  
**Auto-fixable:** No

**Description:**  
Process 'CAT_FASTQ' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>83. CONTAINER-001 — CNVKIT_ANTITARGET</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L2182–2217  
**Auto-fixable:** Yes

**Description:**  
Process 'CNVKIT_ANTITARGET' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟠 <strong>84. STORAGE-001 — CNVKIT_ANTITARGET</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L2182–2217  
**Auto-fixable:** No

**Description:**  
Process 'CNVKIT_ANTITARGET' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
/cnvkit, //g
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>85. RESOURCE-001 — CNVKIT_ANTITARGET</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L2182–2217  
**Auto-fixable:** No

**Description:**  
Process 'CNVKIT_ANTITARGET' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>86. RESOURCE-002 — CNVKIT_ANTITARGET</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L2182–2217  
**Auto-fixable:** No

**Description:**  
Process 'CNVKIT_ANTITARGET' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>87. CONTAINER-001 — CNVKIT_BATCH</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L2221–2330  
**Auto-fixable:** Yes

**Description:**  
Process 'CNVKIT_BATCH' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟠 <strong>88. STORAGE-001 — CNVKIT_BATCH</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L2221–2330  
**Auto-fixable:** No

**Description:**  
Process 'CNVKIT_BATCH' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
//, //, // ... (12 more)
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>89. RESOURCE-001 — CNVKIT_BATCH</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L2221–2330  
**Auto-fixable:** No

**Description:**  
Process 'CNVKIT_BATCH' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>90. RESOURCE-002 — CNVKIT_BATCH</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L2221–2330  
**Auto-fixable:** No

**Description:**  
Process 'CNVKIT_BATCH' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>91. CONTAINER-001 — CNVKIT_CALL</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L2334–2380  
**Auto-fixable:** Yes

**Description:**  
Process 'CNVKIT_CALL' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟠 <strong>92. STORAGE-001 — CNVKIT_CALL</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L2334–2380  
**Auto-fixable:** No

**Description:**  
Process 'CNVKIT_CALL' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
/cnvkit, //g
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>93. RESOURCE-001 — CNVKIT_CALL</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L2334–2380  
**Auto-fixable:** No

**Description:**  
Process 'CNVKIT_CALL' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>94. RESOURCE-002 — CNVKIT_CALL</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L2334–2380  
**Auto-fixable:** No

**Description:**  
Process 'CNVKIT_CALL' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>95. CONTAINER-001 — CNVKIT_EXPORT</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L2384–2430  
**Auto-fixable:** Yes

**Description:**  
Process 'CNVKIT_EXPORT' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟠 <strong>96. STORAGE-001 — CNVKIT_EXPORT</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L2384–2430  
**Auto-fixable:** No

**Description:**  
Process 'CNVKIT_EXPORT' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
/cnvkit, //g
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>97. RESOURCE-001 — CNVKIT_EXPORT</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L2384–2430  
**Auto-fixable:** No

**Description:**  
Process 'CNVKIT_EXPORT' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>98. RESOURCE-002 — CNVKIT_EXPORT</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L2384–2430  
**Auto-fixable:** No

**Description:**  
Process 'CNVKIT_EXPORT' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>99. CONTAINER-001 — CNVKIT_GENEMETRICS</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L2434–2472  
**Auto-fixable:** Yes

**Description:**  
Process 'CNVKIT_GENEMETRICS' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟠 <strong>100. STORAGE-001 — CNVKIT_GENEMETRICS</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L2434–2472  
**Auto-fixable:** No

**Description:**  
Process 'CNVKIT_GENEMETRICS' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
/cnvkit, //g
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>101. RESOURCE-001 — CNVKIT_GENEMETRICS</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L2434–2472  
**Auto-fixable:** No

**Description:**  
Process 'CNVKIT_GENEMETRICS' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>102. RESOURCE-002 — CNVKIT_GENEMETRICS</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L2434–2472  
**Auto-fixable:** No

**Description:**  
Process 'CNVKIT_GENEMETRICS' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>103. CONTAINER-001 — CNVKIT_REFERENCE</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L2476–2515  
**Auto-fixable:** Yes

**Description:**  
Process 'CNVKIT_REFERENCE' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟠 <strong>104. STORAGE-001 — CNVKIT_REFERENCE</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L2476–2515  
**Auto-fixable:** No

**Description:**  
Process 'CNVKIT_REFERENCE' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
/cnvkit, //g
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>105. RESOURCE-001 — CNVKIT_REFERENCE</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L2476–2515  
**Auto-fixable:** No

**Description:**  
Process 'CNVKIT_REFERENCE' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>106. RESOURCE-002 — CNVKIT_REFERENCE</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L2476–2515  
**Auto-fixable:** No

**Description:**  
Process 'CNVKIT_REFERENCE' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>107. CONTAINER-001 — CONTROLFREEC_ASSESSSIGNIFICANCE</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L2519–2565  
**Auto-fixable:** Yes

**Description:**  
Process 'CONTROLFREEC_ASSESSSIGNIFICANCE' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟠 <strong>108. STORAGE-001 — CONTROLFREEC_ASSESSSIGNIFICANCE</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L2519–2565  
**Auto-fixable:** No

**Description:**  
Process 'CONTROLFREEC_ASSESSSIGNIFICANCE' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
//
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>109. RESOURCE-001 — CONTROLFREEC_ASSESSSIGNIFICANCE</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L2519–2565  
**Auto-fixable:** No

**Description:**  
Process 'CONTROLFREEC_ASSESSSIGNIFICANCE' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>110. RESOURCE-002 — CONTROLFREEC_ASSESSSIGNIFICANCE</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L2519–2565  
**Auto-fixable:** No

**Description:**  
Process 'CONTROLFREEC_ASSESSSIGNIFICANCE' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>111. CONTAINER-001 — CONTROLFREEC_FREEC</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L2569–2749  
**Auto-fixable:** Yes

**Description:**  
Process 'CONTROLFREEC_FREEC' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟠 <strong>112. STORAGE-001 — CONTROLFREEC_FREEC</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L2569–2749  
**Auto-fixable:** No

**Description:**  
Process 'CONTROLFREEC_FREEC' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
//, //, // ... (3 more)
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>113. RESOURCE-001 — CONTROLFREEC_FREEC</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L2569–2749  
**Auto-fixable:** No

**Description:**  
Process 'CONTROLFREEC_FREEC' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>114. RESOURCE-002 — CONTROLFREEC_FREEC</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L2569–2749  
**Auto-fixable:** No

**Description:**  
Process 'CONTROLFREEC_FREEC' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>115. CONTAINER-001 — CONTROLFREEC_FREEC2BED</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L2753–2798  
**Auto-fixable:** Yes

**Description:**  
Process 'CONTROLFREEC_FREEC2BED' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟠 <strong>116. STORAGE-001 — CONTROLFREEC_FREEC2BED</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L2753–2798  
**Auto-fixable:** No

**Description:**  
Process 'CONTROLFREEC_FREEC2BED' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
//
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>117. RESOURCE-001 — CONTROLFREEC_FREEC2BED</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L2753–2798  
**Auto-fixable:** No

**Description:**  
Process 'CONTROLFREEC_FREEC2BED' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>118. RESOURCE-002 — CONTROLFREEC_FREEC2BED</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L2753–2798  
**Auto-fixable:** No

**Description:**  
Process 'CONTROLFREEC_FREEC2BED' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>119. CONTAINER-001 — CONTROLFREEC_FREEC2CIRCOS</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L2802–2847  
**Auto-fixable:** Yes

**Description:**  
Process 'CONTROLFREEC_FREEC2CIRCOS' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟠 <strong>120. STORAGE-001 — CONTROLFREEC_FREEC2CIRCOS</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L2802–2847  
**Auto-fixable:** No

**Description:**  
Process 'CONTROLFREEC_FREEC2CIRCOS' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
//
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>121. RESOURCE-001 — CONTROLFREEC_FREEC2CIRCOS</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L2802–2847  
**Auto-fixable:** No

**Description:**  
Process 'CONTROLFREEC_FREEC2CIRCOS' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>122. RESOURCE-002 — CONTROLFREEC_FREEC2CIRCOS</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L2802–2847  
**Auto-fixable:** No

**Description:**  
Process 'CONTROLFREEC_FREEC2CIRCOS' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>123. CONTAINER-001 — CONTROLFREEC_MAKEGRAPH2</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L2851–2906  
**Auto-fixable:** Yes

**Description:**  
Process 'CONTROLFREEC_MAKEGRAPH2' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟠 <strong>124. STORAGE-001 — CONTROLFREEC_MAKEGRAPH2</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L2851–2906  
**Auto-fixable:** No

**Description:**  
Process 'CONTROLFREEC_MAKEGRAPH2' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
//
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>125. RESOURCE-001 — CONTROLFREEC_MAKEGRAPH2</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L2851–2906  
**Auto-fixable:** No

**Description:**  
Process 'CONTROLFREEC_MAKEGRAPH2' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>126. RESOURCE-002 — CONTROLFREEC_MAKEGRAPH2</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L2851–2906  
**Auto-fixable:** No

**Description:**  
Process 'CONTROLFREEC_MAKEGRAPH2' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🟠 <strong>127. STORAGE-001 — DEEPVARIANT_RUNDEEPVARIANT</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L2910–2982  
**Auto-fixable:** No

**Description:**  
Process 'DEEPVARIANT_RUNDEEPVARIANT' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
//, /opt/deepvariant/bin/run_deepvariant, /opt/deepvariant/bin/run_deepvariant ... (2 more)
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>128. RESOURCE-001 — DEEPVARIANT_RUNDEEPVARIANT</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L2910–2982  
**Auto-fixable:** No

**Description:**  
Process 'DEEPVARIANT_RUNDEEPVARIANT' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>129. RESOURCE-002 — DEEPVARIANT_RUNDEEPVARIANT</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L2910–2982  
**Auto-fixable:** No

**Description:**  
Process 'DEEPVARIANT_RUNDEEPVARIANT' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>130. CONTAINER-001 — DRAGMAP_ALIGN</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L2986–3075  
**Auto-fixable:** Yes

**Description:**  
Process 'DRAGMAP_ALIGN' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟠 <strong>131. STORAGE-001 — DRAGMAP_ALIGN</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L2986–3075  
**Auto-fixable:** No

**Description:**  
Process 'DRAGMAP_ALIGN' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
//, /Using., // ... (2 more)
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>132. RESOURCE-001 — DRAGMAP_ALIGN</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L2986–3075  
**Auto-fixable:** No

**Description:**  
Process 'DRAGMAP_ALIGN' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>133. RESOURCE-002 — DRAGMAP_ALIGN</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L2986–3075  
**Auto-fixable:** No

**Description:**  
Process 'DRAGMAP_ALIGN' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>134. CONTAINER-001 — DRAGMAP_HASHTABLE</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L3079–3125  
**Auto-fixable:** Yes

**Description:**  
Process 'DRAGMAP_HASHTABLE' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟡 <strong>135. RESOURCE-001 — DRAGMAP_HASHTABLE</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L3079–3125  
**Auto-fixable:** No

**Description:**  
Process 'DRAGMAP_HASHTABLE' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>136. RESOURCE-002 — DRAGMAP_HASHTABLE</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L3079–3125  
**Auto-fixable:** No

**Description:**  
Process 'DRAGMAP_HASHTABLE' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>137. CONTAINER-001 — ENSEMBLVEP_DOWNLOAD</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L3129–3166  
**Auto-fixable:** Yes

**Description:**  
Process 'ENSEMBLVEP_DOWNLOAD' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟡 <strong>138. RESOURCE-001 — ENSEMBLVEP_DOWNLOAD</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L3129–3166  
**Auto-fixable:** No

**Description:**  
Process 'ENSEMBLVEP_DOWNLOAD' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>139. RESOURCE-002 — ENSEMBLVEP_DOWNLOAD</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L3129–3166  
**Auto-fixable:** No

**Description:**  
Process 'ENSEMBLVEP_DOWNLOAD' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>140. CONTAINER-001 — ENSEMBLVEP_VEP</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L3170–3236  
**Auto-fixable:** Yes

**Description:**  
Process 'ENSEMBLVEP_VEP' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟠 <strong>141. STORAGE-001 — ENSEMBLVEP_VEP</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L3170–3236  
**Auto-fixable:** No

**Description:**  
Process 'ENSEMBLVEP_VEP' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
/.vep
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>142. RESOURCE-001 — ENSEMBLVEP_VEP</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L3170–3236  
**Auto-fixable:** No

**Description:**  
Process 'ENSEMBLVEP_VEP' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>143. RESOURCE-002 — ENSEMBLVEP_VEP</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L3170–3236  
**Auto-fixable:** No

**Description:**  
Process 'ENSEMBLVEP_VEP' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>144. CONTAINER-001 — FASTP</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L3240–3364  
**Auto-fixable:** Yes

**Description:**  
Process 'FASTP' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟠 <strong>145. STORAGE-001 — FASTP</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L3240–3364  
**Auto-fixable:** No

**Description:**  
Process 'FASTP' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
//, //, /fastp ... (5 more)
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>146. RESOURCE-001 — FASTP</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L3240–3364  
**Auto-fixable:** No

**Description:**  
Process 'FASTP' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>147. RESOURCE-002 — FASTP</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L3240–3364  
**Auto-fixable:** No

**Description:**  
Process 'FASTP' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>148. CONTAINER-001 — FASTQC</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L3368–3431  
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

<details><summary>🟠 <strong>149. STORAGE-001 — FASTQC</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L3368–3431  
**Auto-fixable:** No

**Description:**  
Process 'FASTQC' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
//, //, // ... (6 more)
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>150. RESOURCE-001 — FASTQC</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L3368–3431  
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

<details><summary>🟡 <strong>151. RESOURCE-002 — FASTQC</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L3368–3431  
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

<details><summary>🔴 <strong>152. CONTAINER-001 — FGBIO_CALLMOLECULARCONSENSUSREADS</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L3435–3498  
**Auto-fixable:** Yes

**Description:**  
Process 'FGBIO_CALLMOLECULARCONSENSUSREADS' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟠 <strong>153. STORAGE-001 — FGBIO_CALLMOLECULARCONSENSUSREADS</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L3435–3498  
**Auto-fixable:** No

**Description:**  
Process 'FGBIO_CALLMOLECULARCONSENSUSREADS' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
//, //
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>154. RESOURCE-001 — FGBIO_CALLMOLECULARCONSENSUSREADS</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L3435–3498  
**Auto-fixable:** No

**Description:**  
Process 'FGBIO_CALLMOLECULARCONSENSUSREADS' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>155. RESOURCE-002 — FGBIO_CALLMOLECULARCONSENSUSREADS</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L3435–3498  
**Auto-fixable:** No

**Description:**  
Process 'FGBIO_CALLMOLECULARCONSENSUSREADS' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>156. CONTAINER-001 — FGBIO_COPYUMIFROMREADNAME</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L3502–3565  
**Auto-fixable:** Yes

**Description:**  
Process 'FGBIO_COPYUMIFROMREADNAME' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟠 <strong>157. STORAGE-001 — FGBIO_COPYUMIFROMREADNAME</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L3502–3565  
**Auto-fixable:** No

**Description:**  
Process 'FGBIO_COPYUMIFROMREADNAME' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
//, //
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>158. RESOURCE-001 — FGBIO_COPYUMIFROMREADNAME</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L3502–3565  
**Auto-fixable:** No

**Description:**  
Process 'FGBIO_COPYUMIFROMREADNAME' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>159. RESOURCE-002 — FGBIO_COPYUMIFROMREADNAME</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L3502–3565  
**Auto-fixable:** No

**Description:**  
Process 'FGBIO_COPYUMIFROMREADNAME' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>160. CONTAINER-001 — FGBIO_FASTQTOBAM</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L3569–3638  
**Auto-fixable:** Yes

**Description:**  
Process 'FGBIO_FASTQTOBAM' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟠 <strong>161. STORAGE-001 — FGBIO_FASTQTOBAM</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L3569–3638  
**Auto-fixable:** No

**Description:**  
Process 'FGBIO_FASTQTOBAM' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
//, //
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>162. RESOURCE-001 — FGBIO_FASTQTOBAM</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L3569–3638  
**Auto-fixable:** No

**Description:**  
Process 'FGBIO_FASTQTOBAM' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>163. RESOURCE-002 — FGBIO_FASTQTOBAM</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L3569–3638  
**Auto-fixable:** No

**Description:**  
Process 'FGBIO_FASTQTOBAM' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>164. CONTAINER-001 — FGBIO_GROUPREADSBYUMI</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L3642–3708  
**Auto-fixable:** Yes

**Description:**  
Process 'FGBIO_GROUPREADSBYUMI' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟠 <strong>165. STORAGE-001 — FGBIO_GROUPREADSBYUMI</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L3642–3708  
**Auto-fixable:** No

**Description:**  
Process 'FGBIO_GROUPREADSBYUMI' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
//, //
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>166. RESOURCE-001 — FGBIO_GROUPREADSBYUMI</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L3642–3708  
**Auto-fixable:** No

**Description:**  
Process 'FGBIO_GROUPREADSBYUMI' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>167. RESOURCE-002 — FGBIO_GROUPREADSBYUMI</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L3642–3708  
**Auto-fixable:** No

**Description:**  
Process 'FGBIO_GROUPREADSBYUMI' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>168. CONTAINER-001 — FREEBAYES</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L3712–3772  
**Auto-fixable:** Yes

**Description:**  
Process 'FREEBAYES' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟠 <strong>169. STORAGE-001 — FREEBAYES</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L3712–3772  
**Auto-fixable:** No

**Description:**  
Process 'FREEBAYES' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
/version, //g
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>170. RESOURCE-001 — FREEBAYES</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L3712–3772  
**Auto-fixable:** No

**Description:**  
Process 'FREEBAYES' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>171. RESOURCE-002 — FREEBAYES</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L3712–3772  
**Auto-fixable:** No

**Description:**  
Process 'FREEBAYES' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>172. CONTAINER-001 — GATK4_APPLYBQSR</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L3776–3847  
**Auto-fixable:** Yes

**Description:**  
Process 'GATK4_APPLYBQSR' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟠 <strong>173. STORAGE-001 — GATK4_APPLYBQSR</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L3776–3847  
**Auto-fixable:** No

**Description:**  
Process 'GATK4_APPLYBQSR' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
//, //, //
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>174. RESOURCE-001 — GATK4_APPLYBQSR</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L3776–3847  
**Auto-fixable:** No

**Description:**  
Process 'GATK4_APPLYBQSR' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>175. RESOURCE-002 — GATK4_APPLYBQSR</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L3776–3847  
**Auto-fixable:** No

**Description:**  
Process 'GATK4_APPLYBQSR' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>176. CONTAINER-001 — GATK4_APPLYVQSR</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L3851–3913  
**Auto-fixable:** Yes

**Description:**  
Process 'GATK4_APPLYVQSR' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟠 <strong>177. STORAGE-001 — GATK4_APPLYVQSR</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L3851–3913  
**Auto-fixable:** No

**Description:**  
Process 'GATK4_APPLYVQSR' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
//, //
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>178. RESOURCE-001 — GATK4_APPLYVQSR</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L3851–3913  
**Auto-fixable:** No

**Description:**  
Process 'GATK4_APPLYVQSR' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>179. RESOURCE-002 — GATK4_APPLYVQSR</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L3851–3913  
**Auto-fixable:** No

**Description:**  
Process 'GATK4_APPLYVQSR' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>180. CONTAINER-001 — GATK4_BASERECALIBRATOR</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L3917–3979  
**Auto-fixable:** Yes

**Description:**  
Process 'GATK4_BASERECALIBRATOR' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟠 <strong>181. STORAGE-001 — GATK4_BASERECALIBRATOR</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L3917–3979  
**Auto-fixable:** No

**Description:**  
Process 'GATK4_BASERECALIBRATOR' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
//, //
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>182. RESOURCE-001 — GATK4_BASERECALIBRATOR</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L3917–3979  
**Auto-fixable:** No

**Description:**  
Process 'GATK4_BASERECALIBRATOR' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>183. RESOURCE-002 — GATK4_BASERECALIBRATOR</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L3917–3979  
**Auto-fixable:** No

**Description:**  
Process 'GATK4_BASERECALIBRATOR' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>184. CONTAINER-001 — GATK4_CALCULATECONTAMINATION</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L3983–4040  
**Auto-fixable:** Yes

**Description:**  
Process 'GATK4_CALCULATECONTAMINATION' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟠 <strong>185. STORAGE-001 — GATK4_CALCULATECONTAMINATION</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L3983–4040  
**Auto-fixable:** No

**Description:**  
Process 'GATK4_CALCULATECONTAMINATION' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
//, //
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>186. RESOURCE-001 — GATK4_CALCULATECONTAMINATION</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L3983–4040  
**Auto-fixable:** No

**Description:**  
Process 'GATK4_CALCULATECONTAMINATION' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>187. RESOURCE-002 — GATK4_CALCULATECONTAMINATION</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L3983–4040  
**Auto-fixable:** No

**Description:**  
Process 'GATK4_CALCULATECONTAMINATION' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🟠 <strong>188. STORAGE-001 — GATK4_CNNSCOREVARIANTS</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L4044–4118  
**Auto-fixable:** No

**Description:**  
Process 'GATK4_CNNSCOREVARIANTS' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
//, //, //
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>189. RESOURCE-001 — GATK4_CNNSCOREVARIANTS</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L4044–4118  
**Auto-fixable:** No

**Description:**  
Process 'GATK4_CNNSCOREVARIANTS' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>190. RESOURCE-002 — GATK4_CNNSCOREVARIANTS</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L4044–4118  
**Auto-fixable:** No

**Description:**  
Process 'GATK4_CNNSCOREVARIANTS' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>191. CONTAINER-001 — GATK4_CREATESEQUENCEDICTIONARY</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L4122–4174  
**Auto-fixable:** Yes

**Description:**  
Process 'GATK4_CREATESEQUENCEDICTIONARY' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟠 <strong>192. STORAGE-001 — GATK4_CREATESEQUENCEDICTIONARY</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L4122–4174  
**Auto-fixable:** No

**Description:**  
Process 'GATK4_CREATESEQUENCEDICTIONARY' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
//, //
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>193. RESOURCE-001 — GATK4_CREATESEQUENCEDICTIONARY</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L4122–4174  
**Auto-fixable:** No

**Description:**  
Process 'GATK4_CREATESEQUENCEDICTIONARY' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>194. RESOURCE-002 — GATK4_CREATESEQUENCEDICTIONARY</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L4122–4174  
**Auto-fixable:** No

**Description:**  
Process 'GATK4_CREATESEQUENCEDICTIONARY' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>195. CONTAINER-001 — GATK4_ESTIMATELIBRARYCOMPLEXITY</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L4178–4238  
**Auto-fixable:** Yes

**Description:**  
Process 'GATK4_ESTIMATELIBRARYCOMPLEXITY' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟠 <strong>196. STORAGE-001 — GATK4_ESTIMATELIBRARYCOMPLEXITY</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L4178–4238  
**Auto-fixable:** No

**Description:**  
Process 'GATK4_ESTIMATELIBRARYCOMPLEXITY' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
//, //
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>197. RESOURCE-001 — GATK4_ESTIMATELIBRARYCOMPLEXITY</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L4178–4238  
**Auto-fixable:** No

**Description:**  
Process 'GATK4_ESTIMATELIBRARYCOMPLEXITY' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>198. RESOURCE-002 — GATK4_ESTIMATELIBRARYCOMPLEXITY</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L4178–4238  
**Auto-fixable:** No

**Description:**  
Process 'GATK4_ESTIMATELIBRARYCOMPLEXITY' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>199. CONTAINER-001 — GATK4_FILTERMUTECTCALLS</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L4242–4312  
**Auto-fixable:** Yes

**Description:**  
Process 'GATK4_FILTERMUTECTCALLS' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟠 <strong>200. STORAGE-001 — GATK4_FILTERMUTECTCALLS</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L4242–4312  
**Auto-fixable:** No

**Description:**  
Process 'GATK4_FILTERMUTECTCALLS' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
//, //
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>201. RESOURCE-001 — GATK4_FILTERMUTECTCALLS</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L4242–4312  
**Auto-fixable:** No

**Description:**  
Process 'GATK4_FILTERMUTECTCALLS' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>202. RESOURCE-002 — GATK4_FILTERMUTECTCALLS</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L4242–4312  
**Auto-fixable:** No

**Description:**  
Process 'GATK4_FILTERMUTECTCALLS' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>203. CONTAINER-001 — GATK4_FILTERVARIANTTRANCHES</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L4316–4380  
**Auto-fixable:** Yes

**Description:**  
Process 'GATK4_FILTERVARIANTTRANCHES' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟠 <strong>204. STORAGE-001 — GATK4_FILTERVARIANTTRANCHES</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L4316–4380  
**Auto-fixable:** No

**Description:**  
Process 'GATK4_FILTERVARIANTTRANCHES' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
//, //
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>205. RESOURCE-001 — GATK4_FILTERVARIANTTRANCHES</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L4316–4380  
**Auto-fixable:** No

**Description:**  
Process 'GATK4_FILTERVARIANTTRANCHES' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>206. RESOURCE-002 — GATK4_FILTERVARIANTTRANCHES</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L4316–4380  
**Auto-fixable:** No

**Description:**  
Process 'GATK4_FILTERVARIANTTRANCHES' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>207. CONTAINER-001 — GATK4_GATHERBQSRREPORTS</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L4384–4427  
**Auto-fixable:** Yes

**Description:**  
Process 'GATK4_GATHERBQSRREPORTS' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟠 <strong>208. STORAGE-001 — GATK4_GATHERBQSRREPORTS</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L4384–4427  
**Auto-fixable:** No

**Description:**  
Process 'GATK4_GATHERBQSRREPORTS' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
//, //
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>209. RESOURCE-001 — GATK4_GATHERBQSRREPORTS</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L4384–4427  
**Auto-fixable:** No

**Description:**  
Process 'GATK4_GATHERBQSRREPORTS' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>210. RESOURCE-002 — GATK4_GATHERBQSRREPORTS</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L4384–4427  
**Auto-fixable:** No

**Description:**  
Process 'GATK4_GATHERBQSRREPORTS' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>211. CONTAINER-001 — GATK4_GATHERPILEUPSUMMARIES</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L4431–4488  
**Auto-fixable:** Yes

**Description:**  
Process 'GATK4_GATHERPILEUPSUMMARIES' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟠 <strong>212. STORAGE-001 — GATK4_GATHERPILEUPSUMMARIES</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L4431–4488  
**Auto-fixable:** No

**Description:**  
Process 'GATK4_GATHERPILEUPSUMMARIES' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
//, //
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>213. RESOURCE-001 — GATK4_GATHERPILEUPSUMMARIES</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L4431–4488  
**Auto-fixable:** No

**Description:**  
Process 'GATK4_GATHERPILEUPSUMMARIES' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>214. RESOURCE-002 — GATK4_GATHERPILEUPSUMMARIES</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L4431–4488  
**Auto-fixable:** No

**Description:**  
Process 'GATK4_GATHERPILEUPSUMMARIES' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>215. CONTAINER-001 — GATK4_GENOMICSDBIMPORT</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L4492–4595  
**Auto-fixable:** Yes

**Description:**  
Process 'GATK4_GENOMICSDBIMPORT' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟠 <strong>216. STORAGE-001 — GATK4_GENOMICSDBIMPORT</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L4492–4595  
**Auto-fixable:** No

**Description:**  
Process 'GATK4_GENOMICSDBIMPORT' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
//, //, // ... (2 more)
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>217. RESOURCE-001 — GATK4_GENOMICSDBIMPORT</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L4492–4595  
**Auto-fixable:** No

**Description:**  
Process 'GATK4_GENOMICSDBIMPORT' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>218. RESOURCE-002 — GATK4_GENOMICSDBIMPORT</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L4492–4595  
**Auto-fixable:** No

**Description:**  
Process 'GATK4_GENOMICSDBIMPORT' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>219. CONTAINER-001 — GATK4_GENOTYPEGVCFS</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L4599–4666  
**Auto-fixable:** Yes

**Description:**  
Process 'GATK4_GENOTYPEGVCFS' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟠 <strong>220. STORAGE-001 — GATK4_GENOTYPEGVCFS</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L4599–4666  
**Auto-fixable:** No

**Description:**  
Process 'GATK4_GENOTYPEGVCFS' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
//, //, //
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>221. RESOURCE-001 — GATK4_GENOTYPEGVCFS</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L4599–4666  
**Auto-fixable:** No

**Description:**  
Process 'GATK4_GENOTYPEGVCFS' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>222. RESOURCE-002 — GATK4_GENOTYPEGVCFS</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L4599–4666  
**Auto-fixable:** No

**Description:**  
Process 'GATK4_GENOTYPEGVCFS' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>223. CONTAINER-001 — GATK4_GETPILEUPSUMMARIES</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L4670–4733  
**Auto-fixable:** Yes

**Description:**  
Process 'GATK4_GETPILEUPSUMMARIES' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟠 <strong>224. STORAGE-001 — GATK4_GETPILEUPSUMMARIES</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L4670–4733  
**Auto-fixable:** No

**Description:**  
Process 'GATK4_GETPILEUPSUMMARIES' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
//, //
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>225. RESOURCE-001 — GATK4_GETPILEUPSUMMARIES</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L4670–4733  
**Auto-fixable:** No

**Description:**  
Process 'GATK4_GETPILEUPSUMMARIES' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>226. RESOURCE-002 — GATK4_GETPILEUPSUMMARIES</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L4670–4733  
**Auto-fixable:** No

**Description:**  
Process 'GATK4_GETPILEUPSUMMARIES' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>227. CONTAINER-001 — GATK4_HAPLOTYPECALLER</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L4737–4813  
**Auto-fixable:** Yes

**Description:**  
Process 'GATK4_HAPLOTYPECALLER' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟠 <strong>228. STORAGE-001 — GATK4_HAPLOTYPECALLER</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L4737–4813  
**Auto-fixable:** No

**Description:**  
Process 'GATK4_HAPLOTYPECALLER' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
//, //
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>229. RESOURCE-001 — GATK4_HAPLOTYPECALLER</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L4737–4813  
**Auto-fixable:** No

**Description:**  
Process 'GATK4_HAPLOTYPECALLER' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>230. RESOURCE-002 — GATK4_HAPLOTYPECALLER</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L4737–4813  
**Auto-fixable:** No

**Description:**  
Process 'GATK4_HAPLOTYPECALLER' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>231. CONTAINER-001 — GATK4_INTERVALLISTTOBED</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L4817–4872  
**Auto-fixable:** Yes

**Description:**  
Process 'GATK4_INTERVALLISTTOBED' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟠 <strong>232. STORAGE-001 — GATK4_INTERVALLISTTOBED</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L4817–4872  
**Auto-fixable:** No

**Description:**  
Process 'GATK4_INTERVALLISTTOBED' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
//, //
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>233. RESOURCE-001 — GATK4_INTERVALLISTTOBED</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L4817–4872  
**Auto-fixable:** No

**Description:**  
Process 'GATK4_INTERVALLISTTOBED' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>234. RESOURCE-002 — GATK4_INTERVALLISTTOBED</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L4817–4872  
**Auto-fixable:** No

**Description:**  
Process 'GATK4_INTERVALLISTTOBED' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>235. CONTAINER-001 — GATK4_LEARNREADORIENTATIONMODEL</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L4876–4919  
**Auto-fixable:** Yes

**Description:**  
Process 'GATK4_LEARNREADORIENTATIONMODEL' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟠 <strong>236. STORAGE-001 — GATK4_LEARNREADORIENTATIONMODEL</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L4876–4919  
**Auto-fixable:** No

**Description:**  
Process 'GATK4_LEARNREADORIENTATIONMODEL' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
//, //
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>237. RESOURCE-001 — GATK4_LEARNREADORIENTATIONMODEL</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L4876–4919  
**Auto-fixable:** No

**Description:**  
Process 'GATK4_LEARNREADORIENTATIONMODEL' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>238. RESOURCE-002 — GATK4_LEARNREADORIENTATIONMODEL</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L4876–4919  
**Auto-fixable:** No

**Description:**  
Process 'GATK4_LEARNREADORIENTATIONMODEL' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>239. CONTAINER-001 — GATK4_MARKDUPLICATES</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L4923–5008  
**Auto-fixable:** Yes

**Description:**  
Process 'GATK4_MARKDUPLICATES' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟠 <strong>240. STORAGE-001 — GATK4_MARKDUPLICATES</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L4923–5008  
**Auto-fixable:** No

**Description:**  
Process 'GATK4_MARKDUPLICATES' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
//, //, // ... (7 more)
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>241. RESOURCE-001 — GATK4_MARKDUPLICATES</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L4923–5008  
**Auto-fixable:** No

**Description:**  
Process 'GATK4_MARKDUPLICATES' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>242. RESOURCE-002 — GATK4_MARKDUPLICATES</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L4923–5008  
**Auto-fixable:** No

**Description:**  
Process 'GATK4_MARKDUPLICATES' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>243. CONTAINER-001 — GATK4_MERGEMUTECTSTATS</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L5012–5066  
**Auto-fixable:** Yes

**Description:**  
Process 'GATK4_MERGEMUTECTSTATS' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟠 <strong>244. STORAGE-001 — GATK4_MERGEMUTECTSTATS</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L5012–5066  
**Auto-fixable:** No

**Description:**  
Process 'GATK4_MERGEMUTECTSTATS' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
//, //
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>245. RESOURCE-001 — GATK4_MERGEMUTECTSTATS</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L5012–5066  
**Auto-fixable:** No

**Description:**  
Process 'GATK4_MERGEMUTECTSTATS' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>246. RESOURCE-002 — GATK4_MERGEMUTECTSTATS</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L5012–5066  
**Auto-fixable:** No

**Description:**  
Process 'GATK4_MERGEMUTECTSTATS' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>247. CONTAINER-001 — GATK4_MERGEVCFS</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L5070–5129  
**Auto-fixable:** Yes

**Description:**  
Process 'GATK4_MERGEVCFS' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟠 <strong>248. STORAGE-001 — GATK4_MERGEVCFS</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L5070–5129  
**Auto-fixable:** No

**Description:**  
Process 'GATK4_MERGEVCFS' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
//, //
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>249. RESOURCE-001 — GATK4_MERGEVCFS</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L5070–5129  
**Auto-fixable:** No

**Description:**  
Process 'GATK4_MERGEVCFS' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>250. RESOURCE-002 — GATK4_MERGEVCFS</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L5070–5129  
**Auto-fixable:** No

**Description:**  
Process 'GATK4_MERGEVCFS' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>251. CONTAINER-001 — GATK4_MUTECT2</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L5133–5207  
**Auto-fixable:** Yes

**Description:**  
Process 'GATK4_MUTECT2' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟠 <strong>252. STORAGE-001 — GATK4_MUTECT2</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L5133–5207  
**Auto-fixable:** No

**Description:**  
Process 'GATK4_MUTECT2' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
//, //
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>253. RESOURCE-001 — GATK4_MUTECT2</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L5133–5207  
**Auto-fixable:** No

**Description:**  
Process 'GATK4_MUTECT2' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>254. RESOURCE-002 — GATK4_MUTECT2</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L5133–5207  
**Auto-fixable:** No

**Description:**  
Process 'GATK4_MUTECT2' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>255. CONTAINER-001 — GATK4_VARIANTRECALIBRATOR</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L5211–5281  
**Auto-fixable:** Yes

**Description:**  
Process 'GATK4_VARIANTRECALIBRATOR' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟠 <strong>256. STORAGE-001 — GATK4_VARIANTRECALIBRATOR</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L5211–5281  
**Auto-fixable:** No

**Description:**  
Process 'GATK4_VARIANTRECALIBRATOR' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
//, //
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>257. RESOURCE-001 — GATK4_VARIANTRECALIBRATOR</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L5211–5281  
**Auto-fixable:** No

**Description:**  
Process 'GATK4_VARIANTRECALIBRATOR' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>258. RESOURCE-002 — GATK4_VARIANTRECALIBRATOR</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L5211–5281  
**Auto-fixable:** No

**Description:**  
Process 'GATK4_VARIANTRECALIBRATOR' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>259. CONTAINER-001 — GATK4SPARK_APPLYBQSR</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L5285–5355  
**Auto-fixable:** Yes

**Description:**  
Process 'GATK4SPARK_APPLYBQSR' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟠 <strong>260. STORAGE-001 — GATK4SPARK_APPLYBQSR</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L5285–5355  
**Auto-fixable:** No

**Description:**  
Process 'GATK4SPARK_APPLYBQSR' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
//, //, //
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>261. RESOURCE-001 — GATK4SPARK_APPLYBQSR</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L5285–5355  
**Auto-fixable:** No

**Description:**  
Process 'GATK4SPARK_APPLYBQSR' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>262. RESOURCE-002 — GATK4SPARK_APPLYBQSR</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L5285–5355  
**Auto-fixable:** No

**Description:**  
Process 'GATK4SPARK_APPLYBQSR' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>263. CONTAINER-001 — GATK4SPARK_BASERECALIBRATOR</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L5359–5425  
**Auto-fixable:** Yes

**Description:**  
Process 'GATK4SPARK_BASERECALIBRATOR' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟠 <strong>264. STORAGE-001 — GATK4SPARK_BASERECALIBRATOR</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L5359–5425  
**Auto-fixable:** No

**Description:**  
Process 'GATK4SPARK_BASERECALIBRATOR' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
//, //
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>265. RESOURCE-001 — GATK4SPARK_BASERECALIBRATOR</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L5359–5425  
**Auto-fixable:** No

**Description:**  
Process 'GATK4SPARK_BASERECALIBRATOR' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>266. RESOURCE-002 — GATK4SPARK_BASERECALIBRATOR</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L5359–5425  
**Auto-fixable:** No

**Description:**  
Process 'GATK4SPARK_BASERECALIBRATOR' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>267. CONTAINER-001 — GATK4SPARK_MARKDUPLICATES</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L5429–5493  
**Auto-fixable:** Yes

**Description:**  
Process 'GATK4SPARK_MARKDUPLICATES' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟠 <strong>268. STORAGE-001 — GATK4SPARK_MARKDUPLICATES</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L5429–5493  
**Auto-fixable:** No

**Description:**  
Process 'GATK4SPARK_MARKDUPLICATES' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
//, //
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>269. RESOURCE-001 — GATK4SPARK_MARKDUPLICATES</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L5429–5493  
**Auto-fixable:** No

**Description:**  
Process 'GATK4SPARK_MARKDUPLICATES' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>270. RESOURCE-002 — GATK4SPARK_MARKDUPLICATES</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L5429–5493  
**Auto-fixable:** No

**Description:**  
Process 'GATK4SPARK_MARKDUPLICATES' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>271. CONTAINER-001 — GAWK</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L5497–5566  
**Auto-fixable:** Yes

**Description:**  
Process 'GAWK' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟠 <strong>272. STORAGE-001 — GAWK</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L5497–5566  
**Auto-fixable:** No

**Description:**  
Process 'GAWK' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
//, //, // ... (3 more)
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>273. RESOURCE-001 — GAWK</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L5497–5566  
**Auto-fixable:** No

**Description:**  
Process 'GAWK' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>274. RESOURCE-002 — GAWK</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L5497–5566  
**Auto-fixable:** No

**Description:**  
Process 'GAWK' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>275. CONTAINER-001 — GOLEFT_INDEXCOV</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L5570–5634  
**Auto-fixable:** Yes

**Description:**  
Process 'GOLEFT_INDEXCOV' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟠 <strong>276. STORAGE-001 — GOLEFT_INDEXCOV</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L5570–5634  
**Auto-fixable:** No

**Description:**  
Process 'GOLEFT_INDEXCOV' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
//, //, // ... (1 more)
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>277. RESOURCE-001 — GOLEFT_INDEXCOV</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L5570–5634  
**Auto-fixable:** No

**Description:**  
Process 'GOLEFT_INDEXCOV' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>278. RESOURCE-002 — GOLEFT_INDEXCOV</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L5570–5634  
**Auto-fixable:** No

**Description:**  
Process 'GOLEFT_INDEXCOV' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>279. CONTAINER-001 — GUNZIP</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L5638–5692  
**Auto-fixable:** Yes

**Description:**  
Process 'GUNZIP' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟠 <strong>280. STORAGE-001 — GUNZIP</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L5638–5692  
**Auto-fixable:** No

**Description:**  
Process 'GUNZIP' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
//, //
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>281. RESOURCE-001 — GUNZIP</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L5638–5692  
**Auto-fixable:** No

**Description:**  
Process 'GUNZIP' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>282. RESOURCE-002 — GUNZIP</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L5638–5692  
**Auto-fixable:** No

**Description:**  
Process 'GUNZIP' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>283. CONTAINER-001 — LOFREQ_CALLPARALLEL</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L5696–5765  
**Auto-fixable:** Yes

**Description:**  
Process 'LOFREQ_CALLPARALLEL' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟠 <strong>284. STORAGE-001 — LOFREQ_CALLPARALLEL</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L5696–5765  
**Auto-fixable:** No

**Description:**  
Process 'LOFREQ_CALLPARALLEL' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
//, //
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>285. RESOURCE-001 — LOFREQ_CALLPARALLEL</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L5696–5765  
**Auto-fixable:** No

**Description:**  
Process 'LOFREQ_CALLPARALLEL' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>286. RESOURCE-002 — LOFREQ_CALLPARALLEL</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L5696–5765  
**Auto-fixable:** No

**Description:**  
Process 'LOFREQ_CALLPARALLEL' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>287. CONTAINER-001 — MANTA_GERMLINE</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L5769–5849  
**Auto-fixable:** Yes

**Description:**  
Process 'MANTA_GERMLINE' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟠 <strong>288. STORAGE-001 — MANTA_GERMLINE</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L5769–5849  
**Auto-fixable:** No

**Description:**  
Process 'MANTA_GERMLINE' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
/runWorkflow.py, /results/variants/candidateSmallIndels.vcf.gz, /results/variants/candidateSmallIndels.vcf.gz.tbi ... (4 more)
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>289. RESOURCE-001 — MANTA_GERMLINE</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L5769–5849  
**Auto-fixable:** No

**Description:**  
Process 'MANTA_GERMLINE' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>290. RESOURCE-002 — MANTA_GERMLINE</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L5769–5849  
**Auto-fixable:** No

**Description:**  
Process 'MANTA_GERMLINE' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>291. CONTAINER-001 — MANTA_SOMATIC</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L5853–5940  
**Auto-fixable:** Yes

**Description:**  
Process 'MANTA_SOMATIC' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟠 <strong>292. STORAGE-001 — MANTA_SOMATIC</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L5853–5940  
**Auto-fixable:** No

**Description:**  
Process 'MANTA_SOMATIC' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
/runWorkflow.py, /results/variants/candidateSmallIndels.vcf.gz, /results/variants/candidateSmallIndels.vcf.gz.tbi ... (6 more)
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>293. RESOURCE-001 — MANTA_SOMATIC</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L5853–5940  
**Auto-fixable:** No

**Description:**  
Process 'MANTA_SOMATIC' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>294. RESOURCE-002 — MANTA_SOMATIC</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L5853–5940  
**Auto-fixable:** No

**Description:**  
Process 'MANTA_SOMATIC' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>295. CONTAINER-001 — MANTA_TUMORONLY</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L5944–6022  
**Auto-fixable:** Yes

**Description:**  
Process 'MANTA_TUMORONLY' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟠 <strong>296. STORAGE-001 — MANTA_TUMORONLY</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L5944–6022  
**Auto-fixable:** No

**Description:**  
Process 'MANTA_TUMORONLY' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
/runWorkflow.py, /results/variants/candidateSmallIndels.vcf.gz, /results/variants/candidateSmallIndels.vcf.gz.tbi ... (4 more)
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>297. RESOURCE-001 — MANTA_TUMORONLY</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L5944–6022  
**Auto-fixable:** No

**Description:**  
Process 'MANTA_TUMORONLY' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>298. RESOURCE-002 — MANTA_TUMORONLY</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L5944–6022  
**Auto-fixable:** No

**Description:**  
Process 'MANTA_TUMORONLY' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>299. CONTAINER-001 — MOSDEPTH</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L6026–6105  
**Auto-fixable:** Yes

**Description:**  
Process 'MOSDEPTH' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟠 <strong>300. STORAGE-001 — MOSDEPTH</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L6026–6105  
**Auto-fixable:** No

**Description:**  
Process 'MOSDEPTH' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
//, //
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>301. RESOURCE-001 — MOSDEPTH</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L6026–6105  
**Auto-fixable:** No

**Description:**  
Process 'MOSDEPTH' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>302. RESOURCE-002 — MOSDEPTH</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L6026–6105  
**Auto-fixable:** No

**Description:**  
Process 'MOSDEPTH' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>303. CONTAINER-001 — MSISENSOR2_MSI</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L6109–6160  
**Auto-fixable:** Yes

**Description:**  
Process 'MSISENSOR2_MSI' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟠 <strong>304. STORAGE-001 — MSISENSOR2_MSI</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L6109–6160  
**Auto-fixable:** No

**Description:**  
Process 'MSISENSOR2_MSI' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
/Version, //g
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>305. RESOURCE-001 — MSISENSOR2_MSI</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L6109–6160  
**Auto-fixable:** No

**Description:**  
Process 'MSISENSOR2_MSI' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>306. RESOURCE-002 — MSISENSOR2_MSI</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L6109–6160  
**Auto-fixable:** No

**Description:**  
Process 'MSISENSOR2_MSI' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>307. CONTAINER-001 — MSISENSORPRO_MSISOMATIC</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L6163–6225  
**Auto-fixable:** Yes

**Description:**  
Process 'MSISENSORPRO_MSISOMATIC' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟠 <strong>308. STORAGE-001 — MSISENSORPRO_MSISOMATIC</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L6163–6225  
**Auto-fixable:** No

**Description:**  
Process 'MSISENSORPRO_MSISOMATIC' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
/Version
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>309. RESOURCE-001 — MSISENSORPRO_MSISOMATIC</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L6163–6225  
**Auto-fixable:** No

**Description:**  
Process 'MSISENSORPRO_MSISOMATIC' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>310. RESOURCE-002 — MSISENSORPRO_MSISOMATIC</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L6163–6225  
**Auto-fixable:** No

**Description:**  
Process 'MSISENSORPRO_MSISOMATIC' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>311. CONTAINER-001 — MSISENSORPRO_SCAN</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L6229–6274  
**Auto-fixable:** Yes

**Description:**  
Process 'MSISENSORPRO_SCAN' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟠 <strong>312. STORAGE-001 — MSISENSORPRO_SCAN</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L6229–6274  
**Auto-fixable:** No

**Description:**  
Process 'MSISENSORPRO_SCAN' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
/Version
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>313. RESOURCE-001 — MSISENSORPRO_SCAN</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L6229–6274  
**Auto-fixable:** No

**Description:**  
Process 'MSISENSORPRO_SCAN' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>314. RESOURCE-002 — MSISENSORPRO_SCAN</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L6229–6274  
**Auto-fixable:** No

**Description:**  
Process 'MSISENSORPRO_SCAN' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>315. CONTAINER-001 — MULTIQC</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L6278–6332  
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

<details><summary>🟡 <strong>316. RESOURCE-001 — MULTIQC</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L6278–6332  
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

<details><summary>🟡 <strong>317. RESOURCE-002 — MULTIQC</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L6278–6332  
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

<details><summary>🔴 <strong>318. CONTAINER-001 — MUSE_CALL</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L6336–6385  
**Auto-fixable:** Yes

**Description:**  
Process 'MUSE_CALL' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟠 <strong>319. STORAGE-001 — MUSE_CALL</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L6336–6385  
**Auto-fixable:** No

**Description:**  
Process 'MUSE_CALL' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
/MuSE, //g, /MuSE ... (1 more)
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>320. RESOURCE-001 — MUSE_CALL</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L6336–6385  
**Auto-fixable:** No

**Description:**  
Process 'MUSE_CALL' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>321. RESOURCE-002 — MUSE_CALL</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L6336–6385  
**Auto-fixable:** No

**Description:**  
Process 'MUSE_CALL' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>322. CONTAINER-001 — MUSE_SUMP</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L6389–6447  
**Auto-fixable:** Yes

**Description:**  
Process 'MUSE_SUMP' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟠 <strong>323. STORAGE-001 — MUSE_SUMP</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L6389–6447  
**Auto-fixable:** No

**Description:**  
Process 'MUSE_SUMP' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
//, //, /MuSE ... (5 more)
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>324. RESOURCE-001 — MUSE_SUMP</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L6389–6447  
**Auto-fixable:** No

**Description:**  
Process 'MUSE_SUMP' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>325. RESOURCE-002 — MUSE_SUMP</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L6389–6447  
**Auto-fixable:** No

**Description:**  
Process 'MUSE_SUMP' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>326. CONTAINER-001 — NGSCHECKMATE_NCM</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L6451–6515  
**Auto-fixable:** Yes

**Description:**  
Process 'NGSCHECKMATE_NCM' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟠 <strong>327. STORAGE-001 — NGSCHECKMATE_NCM</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L6451–6515  
**Auto-fixable:** No

**Description:**  
Process 'NGSCHECKMATE_NCM' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
//g
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>328. RESOURCE-001 — NGSCHECKMATE_NCM</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L6451–6515  
**Auto-fixable:** No

**Description:**  
Process 'NGSCHECKMATE_NCM' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>329. RESOURCE-002 — NGSCHECKMATE_NCM</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L6451–6515  
**Auto-fixable:** No

**Description:**  
Process 'NGSCHECKMATE_NCM' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🟠 <strong>330. STORAGE-001 — PARABRICKS_FQ2BAM</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L6519–6635  
**Auto-fixable:** No

**Description:**  
Process 'PARABRICKS_FQ2BAM' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
//, //, //
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>331. RESOURCE-001 — PARABRICKS_FQ2BAM</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L6519–6635  
**Auto-fixable:** No

**Description:**  
Process 'PARABRICKS_FQ2BAM' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>332. RESOURCE-002 — PARABRICKS_FQ2BAM</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L6519–6635  
**Auto-fixable:** No

**Description:**  
Process 'PARABRICKS_FQ2BAM' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>333. CONTAINER-001 — RBT_VCFSPLIT</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L6639–6686  
**Auto-fixable:** Yes

**Description:**  
Process 'RBT_VCFSPLIT' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟡 <strong>334. RESOURCE-001 — RBT_VCFSPLIT</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L6639–6686  
**Auto-fixable:** No

**Description:**  
Process 'RBT_VCFSPLIT' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>335. RESOURCE-002 — RBT_VCFSPLIT</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L6639–6686  
**Auto-fixable:** No

**Description:**  
Process 'RBT_VCFSPLIT' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>336. CONTAINER-001 — SAMTOOLS_BAM2FQ</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L6690–6745  
**Auto-fixable:** Yes

**Description:**  
Process 'SAMTOOLS_BAM2FQ' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟠 <strong>337. STORAGE-001 — SAMTOOLS_BAM2FQ</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L6690–6745  
**Auto-fixable:** No

**Description:**  
Process 'SAMTOOLS_BAM2FQ' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
//, /Using., // ... (3 more)
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>338. RESOURCE-001 — SAMTOOLS_BAM2FQ</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L6690–6745  
**Auto-fixable:** No

**Description:**  
Process 'SAMTOOLS_BAM2FQ' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>339. RESOURCE-002 — SAMTOOLS_BAM2FQ</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L6690–6745  
**Auto-fixable:** No

**Description:**  
Process 'SAMTOOLS_BAM2FQ' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>340. CONTAINER-001 — SAMTOOLS_COLLATEFASTQ</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L6749–6824  
**Auto-fixable:** Yes

**Description:**  
Process 'SAMTOOLS_COLLATEFASTQ' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟠 <strong>341. STORAGE-001 — SAMTOOLS_COLLATEFASTQ</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L6749–6824  
**Auto-fixable:** No

**Description:**  
Process 'SAMTOOLS_COLLATEFASTQ' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
//, /Using., //
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>342. RESOURCE-001 — SAMTOOLS_COLLATEFASTQ</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L6749–6824  
**Auto-fixable:** No

**Description:**  
Process 'SAMTOOLS_COLLATEFASTQ' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>343. RESOURCE-002 — SAMTOOLS_COLLATEFASTQ</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L6749–6824  
**Auto-fixable:** No

**Description:**  
Process 'SAMTOOLS_COLLATEFASTQ' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>344. CONTAINER-001 — SAMTOOLS_CONVERT</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L6828–6887  
**Auto-fixable:** Yes

**Description:**  
Process 'SAMTOOLS_CONVERT' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟠 <strong>345. STORAGE-001 — SAMTOOLS_CONVERT</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L6828–6887  
**Auto-fixable:** No

**Description:**  
Process 'SAMTOOLS_CONVERT' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
//, /Using., //
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>346. RESOURCE-001 — SAMTOOLS_CONVERT</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L6828–6887  
**Auto-fixable:** No

**Description:**  
Process 'SAMTOOLS_CONVERT' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>347. RESOURCE-002 — SAMTOOLS_CONVERT</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L6828–6887  
**Auto-fixable:** No

**Description:**  
Process 'SAMTOOLS_CONVERT' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>348. CONTAINER-001 — SAMTOOLS_FAIDX</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L6891–6951  
**Auto-fixable:** Yes

**Description:**  
Process 'SAMTOOLS_FAIDX' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟠 <strong>349. STORAGE-001 — SAMTOOLS_FAIDX</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L6891–6951  
**Auto-fixable:** No

**Description:**  
Process 'SAMTOOLS_FAIDX' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
//, /Using., //
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>350. RESOURCE-001 — SAMTOOLS_FAIDX</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L6891–6951  
**Auto-fixable:** No

**Description:**  
Process 'SAMTOOLS_FAIDX' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>351. RESOURCE-002 — SAMTOOLS_FAIDX</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L6891–6951  
**Auto-fixable:** No

**Description:**  
Process 'SAMTOOLS_FAIDX' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>352. CONTAINER-001 — SAMTOOLS_INDEX</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L6955–7003  
**Auto-fixable:** Yes

**Description:**  
Process 'SAMTOOLS_INDEX' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟠 <strong>353. STORAGE-001 — SAMTOOLS_INDEX</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L6955–7003  
**Auto-fixable:** No

**Description:**  
Process 'SAMTOOLS_INDEX' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
//, /Using., //
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>354. RESOURCE-001 — SAMTOOLS_INDEX</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L6955–7003  
**Auto-fixable:** No

**Description:**  
Process 'SAMTOOLS_INDEX' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>355. RESOURCE-002 — SAMTOOLS_INDEX</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L6955–7003  
**Auto-fixable:** No

**Description:**  
Process 'SAMTOOLS_INDEX' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>356. CONTAINER-001 — SAMTOOLS_MERGE</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L7007–7067  
**Auto-fixable:** Yes

**Description:**  
Process 'SAMTOOLS_MERGE' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟠 <strong>357. STORAGE-001 — SAMTOOLS_MERGE</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L7007–7067  
**Auto-fixable:** No

**Description:**  
Process 'SAMTOOLS_MERGE' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
//, /Using., //
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>358. RESOURCE-001 — SAMTOOLS_MERGE</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L7007–7067  
**Auto-fixable:** No

**Description:**  
Process 'SAMTOOLS_MERGE' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>359. RESOURCE-002 — SAMTOOLS_MERGE</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L7007–7067  
**Auto-fixable:** No

**Description:**  
Process 'SAMTOOLS_MERGE' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>360. CONTAINER-001 — SAMTOOLS_MPILEUP</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L7071–7121  
**Auto-fixable:** Yes

**Description:**  
Process 'SAMTOOLS_MPILEUP' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟠 <strong>361. STORAGE-001 — SAMTOOLS_MPILEUP</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L7071–7121  
**Auto-fixable:** No

**Description:**  
Process 'SAMTOOLS_MPILEUP' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
//, /Using., //
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>362. RESOURCE-001 — SAMTOOLS_MPILEUP</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L7071–7121  
**Auto-fixable:** No

**Description:**  
Process 'SAMTOOLS_MPILEUP' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>363. RESOURCE-002 — SAMTOOLS_MPILEUP</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L7071–7121  
**Auto-fixable:** No

**Description:**  
Process 'SAMTOOLS_MPILEUP' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>364. CONTAINER-001 — SAMTOOLS_STATS</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L7125–7172  
**Auto-fixable:** Yes

**Description:**  
Process 'SAMTOOLS_STATS' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟠 <strong>365. STORAGE-001 — SAMTOOLS_STATS</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L7125–7172  
**Auto-fixable:** No

**Description:**  
Process 'SAMTOOLS_STATS' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
//, /Using., //
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>366. RESOURCE-001 — SAMTOOLS_STATS</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L7125–7172  
**Auto-fixable:** No

**Description:**  
Process 'SAMTOOLS_STATS' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>367. RESOURCE-002 — SAMTOOLS_STATS</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L7125–7172  
**Auto-fixable:** No

**Description:**  
Process 'SAMTOOLS_STATS' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>368. CONTAINER-001 — SAMTOOLS_VIEW</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L7176–7278  
**Auto-fixable:** Yes

**Description:**  
Process 'SAMTOOLS_VIEW' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟠 <strong>369. STORAGE-001 — SAMTOOLS_VIEW</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L7176–7278  
**Auto-fixable:** No

**Description:**  
Process 'SAMTOOLS_VIEW' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
//, //, /Using. ... (1 more)
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>370. RESOURCE-001 — SAMTOOLS_VIEW</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L7176–7278  
**Auto-fixable:** No

**Description:**  
Process 'SAMTOOLS_VIEW' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>371. RESOURCE-002 — SAMTOOLS_VIEW</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L7176–7278  
**Auto-fixable:** No

**Description:**  
Process 'SAMTOOLS_VIEW' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>372. CONTAINER-001 — SENTIEON_APPLYVARCAL</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L7282–7343  
**Auto-fixable:** Yes

**Description:**  
Process 'SENTIEON_APPLYVARCAL' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟠 <strong>373. STORAGE-001 — SENTIEON_APPLYVARCAL</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L7282–7343  
**Auto-fixable:** No

**Description:**  
Process 'SENTIEON_APPLYVARCAL' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
/sentieon-genomics-//g
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>374. RESOURCE-001 — SENTIEON_APPLYVARCAL</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L7282–7343  
**Auto-fixable:** No

**Description:**  
Process 'SENTIEON_APPLYVARCAL' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>375. RESOURCE-002 — SENTIEON_APPLYVARCAL</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L7282–7343  
**Auto-fixable:** No

**Description:**  
Process 'SENTIEON_APPLYVARCAL' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>376. CONTAINER-001 — SENTIEON_BWAMEM</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L7347–7416  
**Auto-fixable:** Yes

**Description:**  
Process 'SENTIEON_BWAMEM' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟠 <strong>377. STORAGE-001 — SENTIEON_BWAMEM</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L7347–7416  
**Auto-fixable:** No

**Description:**  
Process 'SENTIEON_BWAMEM' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
/.amb//, //, /Contact ... (2 more)
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>378. RESOURCE-001 — SENTIEON_BWAMEM</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L7347–7416  
**Auto-fixable:** No

**Description:**  
Process 'SENTIEON_BWAMEM' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>379. RESOURCE-002 — SENTIEON_BWAMEM</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L7347–7416  
**Auto-fixable:** No

**Description:**  
Process 'SENTIEON_BWAMEM' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>380. CONTAINER-001 — SENTIEON_DEDUP</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L7420–7494  
**Auto-fixable:** Yes

**Description:**  
Process 'SENTIEON_DEDUP' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟠 <strong>381. STORAGE-001 — SENTIEON_DEDUP</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L7420–7494  
**Auto-fixable:** No

**Description:**  
Process 'SENTIEON_DEDUP' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
/sentieon-genomics-//g
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>382. RESOURCE-001 — SENTIEON_DEDUP</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L7420–7494  
**Auto-fixable:** No

**Description:**  
Process 'SENTIEON_DEDUP' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>383. RESOURCE-002 — SENTIEON_DEDUP</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L7420–7494  
**Auto-fixable:** No

**Description:**  
Process 'SENTIEON_DEDUP' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>384. CONTAINER-001 — SENTIEON_DNAMODELAPPLY</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L7498–7557  
**Auto-fixable:** Yes

**Description:**  
Process 'SENTIEON_DNAMODELAPPLY' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟠 <strong>385. STORAGE-001 — SENTIEON_DNAMODELAPPLY</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L7498–7557  
**Auto-fixable:** No

**Description:**  
Process 'SENTIEON_DNAMODELAPPLY' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
/sentieon-genomics-//g
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>386. RESOURCE-001 — SENTIEON_DNAMODELAPPLY</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L7498–7557  
**Auto-fixable:** No

**Description:**  
Process 'SENTIEON_DNAMODELAPPLY' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>387. RESOURCE-002 — SENTIEON_DNAMODELAPPLY</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L7498–7557  
**Auto-fixable:** No

**Description:**  
Process 'SENTIEON_DNAMODELAPPLY' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>388. CONTAINER-001 — SENTIEON_DNASCOPE</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L7561–7648  
**Auto-fixable:** Yes

**Description:**  
Process 'SENTIEON_DNASCOPE' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟠 <strong>389. STORAGE-001 — SENTIEON_DNASCOPE</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L7561–7648  
**Auto-fixable:** No

**Description:**  
Process 'SENTIEON_DNASCOPE' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
//, //, // ... (3 more)
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>390. RESOURCE-001 — SENTIEON_DNASCOPE</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L7561–7648  
**Auto-fixable:** No

**Description:**  
Process 'SENTIEON_DNASCOPE' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>391. RESOURCE-002 — SENTIEON_DNASCOPE</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L7561–7648  
**Auto-fixable:** No

**Description:**  
Process 'SENTIEON_DNASCOPE' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>392. CONTAINER-001 — SENTIEON_GVCFTYPER</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L7652–7706  
**Auto-fixable:** Yes

**Description:**  
Process 'SENTIEON_GVCFTYPER' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟠 <strong>393. STORAGE-001 — SENTIEON_GVCFTYPER</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L7652–7706  
**Auto-fixable:** No

**Description:**  
Process 'SENTIEON_GVCFTYPER' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
/sentieon-genomics-//g
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>394. RESOURCE-001 — SENTIEON_GVCFTYPER</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L7652–7706  
**Auto-fixable:** No

**Description:**  
Process 'SENTIEON_GVCFTYPER' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>395. RESOURCE-002 — SENTIEON_GVCFTYPER</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L7652–7706  
**Auto-fixable:** No

**Description:**  
Process 'SENTIEON_GVCFTYPER' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>396. CONTAINER-001 — SENTIEON_HAPLOTYPER</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L7710–7802  
**Auto-fixable:** Yes

**Description:**  
Process 'SENTIEON_HAPLOTYPER' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟠 <strong>397. STORAGE-001 — SENTIEON_HAPLOTYPER</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L7710–7802  
**Auto-fixable:** No

**Description:**  
Process 'SENTIEON_HAPLOTYPER' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
//, //, // ... (7 more)
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>398. RESOURCE-001 — SENTIEON_HAPLOTYPER</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L7710–7802  
**Auto-fixable:** No

**Description:**  
Process 'SENTIEON_HAPLOTYPER' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>399. RESOURCE-002 — SENTIEON_HAPLOTYPER</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L7710–7802  
**Auto-fixable:** No

**Description:**  
Process 'SENTIEON_HAPLOTYPER' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>400. CONTAINER-001 — SENTIEON_TNSCOPE</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L7806–7881  
**Auto-fixable:** Yes

**Description:**  
Process 'SENTIEON_TNSCOPE' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟠 <strong>401. STORAGE-001 — SENTIEON_TNSCOPE</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L7806–7881  
**Auto-fixable:** No

**Description:**  
Process 'SENTIEON_TNSCOPE' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
/sentieon-genomics-//g
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>402. RESOURCE-001 — SENTIEON_TNSCOPE</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L7806–7881  
**Auto-fixable:** No

**Description:**  
Process 'SENTIEON_TNSCOPE' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>403. RESOURCE-002 — SENTIEON_TNSCOPE</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L7806–7881  
**Auto-fixable:** No

**Description:**  
Process 'SENTIEON_TNSCOPE' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>404. CONTAINER-001 — SENTIEON_VARCAL</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L7885–7982  
**Auto-fixable:** Yes

**Description:**  
Process 'SENTIEON_VARCAL' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟠 <strong>405. STORAGE-001 — SENTIEON_VARCAL</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L7885–7982  
**Auto-fixable:** No

**Description:**  
Process 'SENTIEON_VARCAL' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
//, //, // ... (3 more)
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>406. RESOURCE-001 — SENTIEON_VARCAL</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L7885–7982  
**Auto-fixable:** No

**Description:**  
Process 'SENTIEON_VARCAL' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>407. RESOURCE-002 — SENTIEON_VARCAL</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L7885–7982  
**Auto-fixable:** No

**Description:**  
Process 'SENTIEON_VARCAL' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>408. CONTAINER-001 — SNPEFF_DOWNLOAD</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L7986–8040  
**Auto-fixable:** Yes

**Description:**  
Process 'SNPEFF_DOWNLOAD' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟠 <strong>409. STORAGE-001 — SNPEFF_DOWNLOAD</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L7986–8040  
**Auto-fixable:** No

**Description:**  
Process 'SNPEFF_DOWNLOAD' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
/snpeff_cache
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>410. RESOURCE-001 — SNPEFF_DOWNLOAD</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L7986–8040  
**Auto-fixable:** No

**Description:**  
Process 'SNPEFF_DOWNLOAD' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>411. RESOURCE-002 — SNPEFF_DOWNLOAD</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L7986–8040  
**Auto-fixable:** No

**Description:**  
Process 'SNPEFF_DOWNLOAD' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>412. CONTAINER-001 — SNPEFF_SNPEFF</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L8044–8108  
**Auto-fixable:** Yes

**Description:**  
Process 'SNPEFF_SNPEFF' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟡 <strong>413. RESOURCE-001 — SNPEFF_SNPEFF</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L8044–8108  
**Auto-fixable:** No

**Description:**  
Process 'SNPEFF_SNPEFF' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>414. RESOURCE-002 — SNPEFF_SNPEFF</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L8044–8108  
**Auto-fixable:** No

**Description:**  
Process 'SNPEFF_SNPEFF' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>415. CONTAINER-001 — SNPSIFT_ANNMEM</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L8112–8166  
**Auto-fixable:** Yes

**Description:**  
Process 'SNPSIFT_ANNMEM' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟠 <strong>416. STORAGE-001 — SNPSIFT_ANNMEM</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L8112–8166  
**Auto-fixable:** No

**Description:**  
Process 'SNPSIFT_ANNMEM' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
//, //
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>417. RESOURCE-001 — SNPSIFT_ANNMEM</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L8112–8166  
**Auto-fixable:** No

**Description:**  
Process 'SNPSIFT_ANNMEM' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>418. RESOURCE-002 — SNPSIFT_ANNMEM</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L8112–8166  
**Auto-fixable:** No

**Description:**  
Process 'SNPSIFT_ANNMEM' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>419. CONTAINER-001 — SNPSIFT_ANNMEMCREATE</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L8170–8207  
**Auto-fixable:** Yes

**Description:**  
Process 'SNPSIFT_ANNMEMCREATE' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟡 <strong>420. RESOURCE-001 — SNPSIFT_ANNMEMCREATE</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L8170–8207  
**Auto-fixable:** No

**Description:**  
Process 'SNPSIFT_ANNMEMCREATE' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>421. RESOURCE-002 — SNPSIFT_ANNMEMCREATE</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L8170–8207  
**Auto-fixable:** No

**Description:**  
Process 'SNPSIFT_ANNMEMCREATE' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>422. CONTAINER-001 — SPRING_DECOMPRESS</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L8211–8264  
**Auto-fixable:** Yes

**Description:**  
Process 'SPRING_DECOMPRESS' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟠 <strong>423. STORAGE-001 — SPRING_DECOMPRESS</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L8211–8264  
**Auto-fixable:** No

**Description:**  
Process 'SPRING_DECOMPRESS' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
//
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>424. RESOURCE-001 — SPRING_DECOMPRESS</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L8211–8264  
**Auto-fixable:** No

**Description:**  
Process 'SPRING_DECOMPRESS' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>425. RESOURCE-002 — SPRING_DECOMPRESS</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L8211–8264  
**Auto-fixable:** No

**Description:**  
Process 'SPRING_DECOMPRESS' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>426. CONTAINER-001 — STRELKA_GERMLINE</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L8268–8332  
**Auto-fixable:** Yes

**Description:**  
Process 'STRELKA_GERMLINE' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟠 <strong>427. STORAGE-001 — STRELKA_GERMLINE</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L8268–8332  
**Auto-fixable:** No

**Description:**  
Process 'STRELKA_GERMLINE' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
/g, /runWorkflow.py, /runWorkflow.py ... (4 more)
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>428. RESOURCE-001 — STRELKA_GERMLINE</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L8268–8332  
**Auto-fixable:** No

**Description:**  
Process 'STRELKA_GERMLINE' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>429. RESOURCE-002 — STRELKA_GERMLINE</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L8268–8332  
**Auto-fixable:** No

**Description:**  
Process 'STRELKA_GERMLINE' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>430. CONTAINER-001 — STRELKA_SOMATIC</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L8336–8403  
**Auto-fixable:** Yes

**Description:**  
Process 'STRELKA_SOMATIC' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟠 <strong>431. STORAGE-001 — STRELKA_SOMATIC</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L8336–8403  
**Auto-fixable:** No

**Description:**  
Process 'STRELKA_SOMATIC' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
/g, /runWorkflow.py, /runWorkflow.py ... (4 more)
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>432. RESOURCE-001 — STRELKA_SOMATIC</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L8336–8403  
**Auto-fixable:** No

**Description:**  
Process 'STRELKA_SOMATIC' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>433. RESOURCE-002 — STRELKA_SOMATIC</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L8336–8403  
**Auto-fixable:** No

**Description:**  
Process 'STRELKA_SOMATIC' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>434. CONTAINER-001 — SVDB_MERGE</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L8407–8511  
**Auto-fixable:** Yes

**Description:**  
Process 'SVDB_MERGE' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟠 <strong>435. STORAGE-001 — SVDB_MERGE</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L8407–8511  
**Auto-fixable:** No

**Description:**  
Process 'SVDB_MERGE' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
//, //, // ... (4 more)
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>436. RESOURCE-001 — SVDB_MERGE</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L8407–8511  
**Auto-fixable:** No

**Description:**  
Process 'SVDB_MERGE' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>437. RESOURCE-002 — SVDB_MERGE</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L8407–8511  
**Auto-fixable:** No

**Description:**  
Process 'SVDB_MERGE' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>438. CONTAINER-001 — TABIX_BGZIPTABIX</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L8515–8562  
**Auto-fixable:** Yes

**Description:**  
Process 'TABIX_BGZIPTABIX' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟠 <strong>439. STORAGE-001 — TABIX_BGZIPTABIX</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L8515–8562  
**Auto-fixable:** No

**Description:**  
Process 'TABIX_BGZIPTABIX' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
//, //
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>440. RESOURCE-001 — TABIX_BGZIPTABIX</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L8515–8562  
**Auto-fixable:** No

**Description:**  
Process 'TABIX_BGZIPTABIX' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>441. RESOURCE-002 — TABIX_BGZIPTABIX</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L8515–8562  
**Auto-fixable:** No

**Description:**  
Process 'TABIX_BGZIPTABIX' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>442. CONTAINER-001 — TABIX_TABIX</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L8566–8610  
**Auto-fixable:** Yes

**Description:**  
Process 'TABIX_TABIX' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟠 <strong>443. STORAGE-001 — TABIX_TABIX</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L8566–8610  
**Auto-fixable:** No

**Description:**  
Process 'TABIX_TABIX' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
//, //
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>444. RESOURCE-001 — TABIX_TABIX</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L8566–8610  
**Auto-fixable:** No

**Description:**  
Process 'TABIX_TABIX' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>445. RESOURCE-002 — TABIX_TABIX</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L8566–8610  
**Auto-fixable:** No

**Description:**  
Process 'TABIX_TABIX' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>446. CONTAINER-001 — TIDDIT_SV</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L8614–8669  
**Auto-fixable:** Yes

**Description:**  
Process 'TIDDIT_SV' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟠 <strong>447. STORAGE-001 — TIDDIT_SV</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L8614–8669  
**Auto-fixable:** No

**Description:**  
Process 'TIDDIT_SV' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
//, //
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>448. RESOURCE-001 — TIDDIT_SV</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L8614–8669  
**Auto-fixable:** No

**Description:**  
Process 'TIDDIT_SV' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>449. RESOURCE-002 — TIDDIT_SV</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L8614–8669  
**Auto-fixable:** No

**Description:**  
Process 'TIDDIT_SV' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>450. CONTAINER-001 — UNTAR</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L8673–8756  
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

<details><summary>🟠 <strong>451. STORAGE-001 — UNTAR</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L8673–8756  
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

<details><summary>🟡 <strong>452. RESOURCE-001 — UNTAR</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L8673–8756  
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

<details><summary>🟡 <strong>453. RESOURCE-002 — UNTAR</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L8673–8756  
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

<details><summary>🔴 <strong>454. CONTAINER-001 — UNZIP</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L8760–8808  
**Auto-fixable:** Yes

**Description:**  
Process 'UNZIP' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟠 <strong>455. STORAGE-001 — UNZIP</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L8760–8808  
**Auto-fixable:** No

**Description:**  
Process 'UNZIP' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
/., //, //
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>456. RESOURCE-001 — UNZIP</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L8760–8808  
**Auto-fixable:** No

**Description:**  
Process 'UNZIP' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>457. RESOURCE-002 — UNZIP</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L8760–8808  
**Auto-fixable:** No

**Description:**  
Process 'UNZIP' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>458. CONTAINER-001 — VARLOCIRAPTOR_CALLVARIANTS</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L8812–8862  
**Auto-fixable:** Yes

**Description:**  
Process 'VARLOCIRAPTOR_CALLVARIANTS' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟠 <strong>459. STORAGE-001 — VARLOCIRAPTOR_CALLVARIANTS</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L8812–8862  
**Auto-fixable:** No

**Description:**  
Process 'VARLOCIRAPTOR_CALLVARIANTS' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
//If, //If, // ... (1 more)
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>460. RESOURCE-001 — VARLOCIRAPTOR_CALLVARIANTS</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L8812–8862  
**Auto-fixable:** No

**Description:**  
Process 'VARLOCIRAPTOR_CALLVARIANTS' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>461. RESOURCE-002 — VARLOCIRAPTOR_CALLVARIANTS</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L8812–8862  
**Auto-fixable:** No

**Description:**  
Process 'VARLOCIRAPTOR_CALLVARIANTS' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>462. CONTAINER-001 — VARLOCIRAPTOR_ESTIMATEALIGNMENTPROPERTIES</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L8866–8913  
**Auto-fixable:** Yes

**Description:**  
Process 'VARLOCIRAPTOR_ESTIMATEALIGNMENTPROPERTIES' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟠 <strong>463. STORAGE-001 — VARLOCIRAPTOR_ESTIMATEALIGNMENTPROPERTIES</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L8866–8913  
**Auto-fixable:** No

**Description:**  
Process 'VARLOCIRAPTOR_ESTIMATEALIGNMENTPROPERTIES' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
//, //
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>464. RESOURCE-001 — VARLOCIRAPTOR_ESTIMATEALIGNMENTPROPERTIES</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L8866–8913  
**Auto-fixable:** No

**Description:**  
Process 'VARLOCIRAPTOR_ESTIMATEALIGNMENTPROPERTIES' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>465. RESOURCE-002 — VARLOCIRAPTOR_ESTIMATEALIGNMENTPROPERTIES</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L8866–8913  
**Auto-fixable:** No

**Description:**  
Process 'VARLOCIRAPTOR_ESTIMATEALIGNMENTPROPERTIES' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>466. CONTAINER-001 — VARLOCIRAPTOR_PREPROCESS</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L8917–8967  
**Auto-fixable:** Yes

**Description:**  
Process 'VARLOCIRAPTOR_PREPROCESS' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟠 <strong>467. STORAGE-001 — VARLOCIRAPTOR_PREPROCESS</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L8917–8967  
**Auto-fixable:** No

**Description:**  
Process 'VARLOCIRAPTOR_PREPROCESS' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
//, //
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>468. RESOURCE-001 — VARLOCIRAPTOR_PREPROCESS</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L8917–8967  
**Auto-fixable:** No

**Description:**  
Process 'VARLOCIRAPTOR_PREPROCESS' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>469. RESOURCE-002 — VARLOCIRAPTOR_PREPROCESS</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L8917–8967  
**Auto-fixable:** No

**Description:**  
Process 'VARLOCIRAPTOR_PREPROCESS' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>470. CONTAINER-001 — VCFLIB_VCFFILTER</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L8971–9029  
**Auto-fixable:** Yes

**Description:**  
Process 'VCFLIB_VCFFILTER' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟠 <strong>471. STORAGE-001 — VCFLIB_VCFFILTER</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L8971–9029  
**Auto-fixable:** No

**Description:**  
Process 'VCFLIB_VCFFILTER' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
//, /--info-filter, /--genotype-filter
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>472. RESOURCE-001 — VCFLIB_VCFFILTER</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L8971–9029  
**Auto-fixable:** No

**Description:**  
Process 'VCFLIB_VCFFILTER' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>473. RESOURCE-002 — VCFLIB_VCFFILTER</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L8971–9029  
**Auto-fixable:** No

**Description:**  
Process 'VCFLIB_VCFFILTER' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>474. CONTAINER-001 — VCFTOOLS</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L9033–9231  
**Auto-fixable:** Yes

**Description:**  
Process 'VCFTOOLS' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟠 <strong>475. STORAGE-001 — VCFTOOLS</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L9033–9231  
**Auto-fixable:** No

**Description:**  
Process 'VCFTOOLS' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
//, //
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>476. RESOURCE-001 — VCFTOOLS</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L9033–9231  
**Auto-fixable:** No

**Description:**  
Process 'VCFTOOLS' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>477. RESOURCE-002 — VCFTOOLS</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L9033–9231  
**Auto-fixable:** No

**Description:**  
Process 'VCFTOOLS' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>478. CONTAINER-001 — YTE</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L9235–9284  
**Auto-fixable:** Yes

**Description:**  
Process 'YTE' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟠 <strong>479. STORAGE-001 — YTE</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L9235–9284  
**Auto-fixable:** No

**Description:**  
Process 'YTE' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
//, //
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>480. RESOURCE-001 — YTE</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L9235–9284  
**Auto-fixable:** No

**Description:**  
Process 'YTE' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>481. RESOURCE-002 — YTE</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L9235–9284  
**Auto-fixable:** No

**Description:**  
Process 'YTE' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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