<!-- WORKFLOW CLINIC ISSUE DRAFT -->
<!-- Title: [Workflow Clinic] 197 cloud-readiness gaps across 51 processes (score: 0%) -->

## 🏥 Workflow Clinic — Automated Cloud-Readiness Report

> **This issue was drafted automatically by [Workflow Clinic](https://github.com/electricdystopia/workflow-clinic), a GA4GH Cloud Work Stream tool for detecting and fixing cloud-readiness gaps in bioinformatics workflows.**
>
> Workflow: `main.nf`  
> Generated: 2026-03-31 19:43 UTC  
> Schema: `0.1.0`

### 🔴 Cloud Readiness Score: **0.00 / 1.00**

### Summary

| Severity | Count | Description |
|---|---|---|
| 🔴 **Critical** | 52 | Portability blockers — workflow cannot run on cloud WES |
| 🟠 **Major** | 41 | Significant gaps affecting reproducibility or correctness |
| 🟡 **Minor** | 104 | Resource hints missing — affects cost and scheduling efficiency |
| **Total** | **197** | |
| Auto-fixable | 52 | Can be fixed automatically with `workflow-clinic doctor` |

> 💡 **52 gap(s) can be fixed automatically.** Run `workflow-clinic doctor <path> --gap CONTAINER-001` to generate a patch and open a PR.

### Gaps

| # | Gap ID | Severity | Process | Category | Lines | Auto-fix |
|---|---|---|---|---|---|---|
| 1 | `CONTAINER-001` | 🔴 CRITICAL | `ANNOTATE_BOOLEAN_PEAKS` | containerization | L182–209 | ✅ |
| 2 | `STORAGE-001` | 🟠 MAJOR | `ANNOTATE_BOOLEAN_PEAKS` | storage | L182–209 | — |
| 3 | `RESOURCE-001` | 🟡 MINOR | `ANNOTATE_BOOLEAN_PEAKS` | resource_hints | L182–209 | — |
| 4 | `RESOURCE-002` | 🟡 MINOR | `ANNOTATE_BOOLEAN_PEAKS` | resource_hints | L182–209 | — |
| 5 | `CONTAINER-001` | 🔴 CRITICAL | `BAM_REMOVE_ORPHANS` | containerization | L216–258 | ✅ |
| 6 | `RESOURCE-001` | 🟡 MINOR | `BAM_REMOVE_ORPHANS` | resource_hints | L216–258 | — |
| 7 | `RESOURCE-002` | 🟡 MINOR | `BAM_REMOVE_ORPHANS` | resource_hints | L216–258 | — |
| 8 | `CONTAINER-001` | 🔴 CRITICAL | `BAMTOOLS_FILTER` | containerization | L262–304 | ✅ |
| 9 | `STORAGE-001` | 🟠 MAJOR | `BAMTOOLS_FILTER` | storage | L262–304 | — |
| 10 | `RESOURCE-001` | 🟡 MINOR | `BAMTOOLS_FILTER` | resource_hints | L262–304 | — |
| 11 | `RESOURCE-002` | 🟡 MINOR | `BAMTOOLS_FILTER` | resource_hints | L262–304 | — |
| 12 | `CONTAINER-001` | 🔴 CRITICAL | `BEDTOOLS_GENOMECOV` | containerization | L308–350 | ✅ |
| 13 | `STORAGE-001` | 🟠 MAJOR | `BEDTOOLS_GENOMECOV` | storage | L308–350 | — |
| 14 | `RESOURCE-001` | 🟡 MINOR | `BEDTOOLS_GENOMECOV` | resource_hints | L308–350 | — |
| 15 | `RESOURCE-002` | 🟡 MINOR | `BEDTOOLS_GENOMECOV` | resource_hints | L308–350 | — |
| 16 | `CONTAINER-001` | 🔴 CRITICAL | `DESEQ2_QC` | containerization | L354–410 | ✅ |
| 17 | `STORAGE-001` | 🟠 MAJOR | `DESEQ2_QC` | storage | L354–410 | — |
| 18 | `RESOURCE-001` | 🟡 MINOR | `DESEQ2_QC` | resource_hints | L354–410 | — |
| 19 | `RESOURCE-002` | 🟡 MINOR | `DESEQ2_QC` | resource_hints | L354–410 | — |
| 20 | `CONTAINER-001` | 🔴 CRITICAL | `FRIP_SCORE` | containerization | L414–447 | ✅ |
| 21 | `STORAGE-001` | 🟠 MAJOR | `FRIP_SCORE` | storage | L414–447 | — |
| 22 | `RESOURCE-001` | 🟡 MINOR | `FRIP_SCORE` | resource_hints | L414–447 | — |
| 23 | `RESOURCE-002` | 🟡 MINOR | `FRIP_SCORE` | resource_hints | L414–447 | — |
| 24 | `CONTAINER-001` | 🔴 CRITICAL | `GENOME_BLACKLIST_REGIONS` | containerization | L454–494 | ✅ |
| 25 | `STORAGE-001` | 🟠 MAJOR | `GENOME_BLACKLIST_REGIONS` | storage | L454–494 | — |
| 26 | `RESOURCE-001` | 🟡 MINOR | `GENOME_BLACKLIST_REGIONS` | resource_hints | L454–494 | — |
| 27 | `RESOURCE-002` | 🟡 MINOR | `GENOME_BLACKLIST_REGIONS` | resource_hints | L454–494 | — |
| 28 | `CONTAINER-001` | 🔴 CRITICAL | `GTF2BED` | containerization | L498–528 | ✅ |
| 29 | `RESOURCE-001` | 🟡 MINOR | `GTF2BED` | resource_hints | L498–528 | — |
| 30 | `RESOURCE-002` | 🟡 MINOR | `GTF2BED` | resource_hints | L498–528 | — |
| 31 | `CONTAINER-001` | 🔴 CRITICAL | `IGV` | containerization | L535–581 | ✅ |
| 32 | `RESOURCE-001` | 🟡 MINOR | `IGV` | resource_hints | L535–581 | — |
| 33 | `RESOURCE-002` | 🟡 MINOR | `IGV` | resource_hints | L535–581 | — |
| 34 | `CONTAINER-001` | 🔴 CRITICAL | `MACS3_CONSENSUS` | containerization | L588–648 | ✅ |
| 35 | `RESOURCE-001` | 🟡 MINOR | `MACS3_CONSENSUS` | resource_hints | L588–648 | — |
| 36 | `RESOURCE-002` | 🟡 MINOR | `MACS3_CONSENSUS` | resource_hints | L588–648 | — |
| 37 | `CONTAINER-001` | 🔴 CRITICAL | `MULTIQC` | containerization | L652–726 | ✅ |
| 38 | `STORAGE-001` | 🟠 MAJOR | `MULTIQC` | storage | L652–726 | — |
| 39 | `RESOURCE-001` | 🟡 MINOR | `MULTIQC` | resource_hints | L652–726 | — |
| 40 | `RESOURCE-002` | 🟡 MINOR | `MULTIQC` | resource_hints | L652–726 | — |
| 41 | `CONTAINER-001` | 🔴 CRITICAL | `MULTIQC_CUSTOM_PEAKS` | containerization | L730–762 | ✅ |
| 42 | `STORAGE-001` | 🟠 MAJOR | `MULTIQC_CUSTOM_PEAKS` | storage | L730–762 | — |
| 43 | `RESOURCE-001` | 🟡 MINOR | `MULTIQC_CUSTOM_PEAKS` | resource_hints | L730–762 | — |
| 44 | `RESOURCE-002` | 🟡 MINOR | `MULTIQC_CUSTOM_PEAKS` | resource_hints | L730–762 | — |
| 45 | `CONTAINER-001` | 🔴 CRITICAL | `MULTIQC_CUSTOM_PHANTOMPEAKQUALTOOLS` | containerization | L766–801 | ✅ |
| 46 | `STORAGE-001` | 🟠 MAJOR | `MULTIQC_CUSTOM_PHANTOMPEAKQUALTOOLS` | storage | L766–801 | — |
| 47 | `RESOURCE-001` | 🟡 MINOR | `MULTIQC_CUSTOM_PHANTOMPEAKQUALTOOLS` | resource_hints | L766–801 | — |
| 48 | `RESOURCE-002` | 🟡 MINOR | `MULTIQC_CUSTOM_PHANTOMPEAKQUALTOOLS` | resource_hints | L766–801 | — |
| 49 | `CONTAINER-001` | 🔴 CRITICAL | `PLOT_HOMER_ANNOTATEPEAKS` | containerization | L805–844 | ✅ |
| 50 | `RESOURCE-001` | 🟡 MINOR | `PLOT_HOMER_ANNOTATEPEAKS` | resource_hints | L805–844 | — |
| 51 | `RESOURCE-002` | 🟡 MINOR | `PLOT_HOMER_ANNOTATEPEAKS` | resource_hints | L805–844 | — |
| 52 | `CONTAINER-001` | 🔴 CRITICAL | `PLOT_MACS3_QC` | containerization | L848–882 | ✅ |
| 53 | `RESOURCE-001` | 🟡 MINOR | `PLOT_MACS3_QC` | resource_hints | L848–882 | — |
| 54 | `RESOURCE-002` | 🟡 MINOR | `PLOT_MACS3_QC` | resource_hints | L848–882 | — |
| 55 | `CONTAINER-001` | 🔴 CRITICAL | `SAMPLESHEET_CHECK` | containerization | L886–917 | ✅ |
| 56 | `RESOURCE-001` | 🟡 MINOR | `SAMPLESHEET_CHECK` | resource_hints | L886–917 | — |
| 57 | `RESOURCE-002` | 🟡 MINOR | `SAMPLESHEET_CHECK` | resource_hints | L886–917 | — |
| 58 | `CONTAINER-001` | 🔴 CRITICAL | `STAR_ALIGN` | containerization | L921–981 | ✅ |
| 59 | `STORAGE-001` | 🟠 MAJOR | `STAR_ALIGN` | storage | L921–981 | — |
| 60 | `RESOURCE-001` | 🟡 MINOR | `STAR_ALIGN` | resource_hints | L921–981 | — |
| 61 | `RESOURCE-002` | 🟡 MINOR | `STAR_ALIGN` | resource_hints | L921–981 | — |
| 62 | `CONTAINER-001` | 🔴 CRITICAL | `STAR_GENOMEGENERATE` | containerization | L985–1045 | ✅ |
| 63 | `STORAGE-001` | 🟠 MAJOR | `STAR_GENOMEGENERATE` | storage | L985–1045 | — |
| 64 | `RESOURCE-001` | 🟡 MINOR | `STAR_GENOMEGENERATE` | resource_hints | L985–1045 | — |
| 65 | `RESOURCE-002` | 🟡 MINOR | `STAR_GENOMEGENERATE` | resource_hints | L985–1045 | — |
| 66 | `CONTAINER-001` | 🔴 CRITICAL | `BOWTIE2_ALIGN` | containerization | L1049–1165 | ✅ |
| 67 | `STORAGE-001` | 🟠 MAJOR | `BOWTIE2_ALIGN` | storage | L1049–1165 | — |
| 68 | `RESOURCE-001` | 🟡 MINOR | `BOWTIE2_ALIGN` | resource_hints | L1049–1165 | — |
| 69 | `RESOURCE-002` | 🟡 MINOR | `BOWTIE2_ALIGN` | resource_hints | L1049–1165 | — |
| 70 | `CONTAINER-001` | 🔴 CRITICAL | `BOWTIE2_BUILD` | containerization | L1169–1210 | ✅ |
| 71 | `STORAGE-001` | 🟠 MAJOR | `BOWTIE2_BUILD` | storage | L1169–1210 | — |
| 72 | `RESOURCE-001` | 🟡 MINOR | `BOWTIE2_BUILD` | resource_hints | L1169–1210 | — |
| 73 | `RESOURCE-002` | 🟡 MINOR | `BOWTIE2_BUILD` | resource_hints | L1169–1210 | — |
| 74 | `CONTAINER-001` | 🔴 CRITICAL | `BWA_INDEX` | containerization | L1214–1266 | ✅ |
| 75 | `STORAGE-001` | 🟠 MAJOR | `BWA_INDEX` | storage | L1214–1266 | — |
| 76 | `RESOURCE-001` | 🟡 MINOR | `BWA_INDEX` | resource_hints | L1214–1266 | — |
| 77 | `RESOURCE-002` | 🟡 MINOR | `BWA_INDEX` | resource_hints | L1214–1266 | — |
| 78 | `CONTAINER-001` | 🔴 CRITICAL | `BWA_MEM` | containerization | L1270–1345 | ✅ |
| 79 | `STORAGE-001` | 🟠 MAJOR | `BWA_MEM` | storage | L1270–1345 | — |
| 80 | `RESOURCE-001` | 🟡 MINOR | `BWA_MEM` | resource_hints | L1270–1345 | — |
| 81 | `RESOURCE-002` | 🟡 MINOR | `BWA_MEM` | resource_hints | L1270–1345 | — |
| 82 | `CONTAINER-001` | 🔴 CRITICAL | `CHROMAP_CHROMAP` | containerization | L1349–1461 | ✅ |
| 83 | `STORAGE-001` | 🟠 MAJOR | `CHROMAP_CHROMAP` | storage | L1349–1461 | — |
| 84 | `RESOURCE-001` | 🟡 MINOR | `CHROMAP_CHROMAP` | resource_hints | L1349–1461 | — |
| 85 | `RESOURCE-002` | 🟡 MINOR | `CHROMAP_CHROMAP` | resource_hints | L1349–1461 | — |
| 86 | `CONTAINER-001` | 🔴 CRITICAL | `CHROMAP_INDEX` | containerization | L1465–1511 | ✅ |
| 87 | `RESOURCE-001` | 🟡 MINOR | `CHROMAP_INDEX` | resource_hints | L1465–1511 | — |
| 88 | `RESOURCE-002` | 🟡 MINOR | `CHROMAP_INDEX` | resource_hints | L1465–1511 | — |
| 89 | `CONTAINER-001` | 🔴 CRITICAL | `CUSTOM_GETCHROMSIZES` | containerization | L1515–1561 | ✅ |
| 90 | `STORAGE-001` | 🟠 MAJOR | `CUSTOM_GETCHROMSIZES` | storage | L1515–1561 | — |
| 91 | `RESOURCE-001` | 🟡 MINOR | `CUSTOM_GETCHROMSIZES` | resource_hints | L1515–1561 | — |
| 92 | `RESOURCE-002` | 🟡 MINOR | `CUSTOM_GETCHROMSIZES` | resource_hints | L1515–1561 | — |
| 93 | `CONTAINER-001` | 🔴 CRITICAL | `DEEPTOOLS_COMPUTEMATRIX` | containerization | L1565–1615 | ✅ |
| 94 | `STORAGE-001` | 🟠 MAJOR | `DEEPTOOLS_COMPUTEMATRIX` | storage | L1565–1615 | — |
| 95 | `RESOURCE-001` | 🟡 MINOR | `DEEPTOOLS_COMPUTEMATRIX` | resource_hints | L1565–1615 | — |
| 96 | `RESOURCE-002` | 🟡 MINOR | `DEEPTOOLS_COMPUTEMATRIX` | resource_hints | L1565–1615 | — |
| 97 | `CONTAINER-001` | 🔴 CRITICAL | `DEEPTOOLS_PLOTFINGERPRINT` | containerization | L1619–1672 | ✅ |
| 98 | `STORAGE-001` | 🟠 MAJOR | `DEEPTOOLS_PLOTFINGERPRINT` | storage | L1619–1672 | — |
| 99 | `RESOURCE-001` | 🟡 MINOR | `DEEPTOOLS_PLOTFINGERPRINT` | resource_hints | L1619–1672 | — |
| 100 | `RESOURCE-002` | 🟡 MINOR | `DEEPTOOLS_PLOTFINGERPRINT` | resource_hints | L1619–1672 | — |
| 101 | `CONTAINER-001` | 🔴 CRITICAL | `DEEPTOOLS_PLOTHEATMAP` | containerization | L1676–1723 | ✅ |
| 102 | `STORAGE-001` | 🟠 MAJOR | `DEEPTOOLS_PLOTHEATMAP` | storage | L1676–1723 | — |
| 103 | `RESOURCE-001` | 🟡 MINOR | `DEEPTOOLS_PLOTHEATMAP` | resource_hints | L1676–1723 | — |
| 104 | `RESOURCE-002` | 🟡 MINOR | `DEEPTOOLS_PLOTHEATMAP` | resource_hints | L1676–1723 | — |
| 105 | `CONTAINER-001` | 🔴 CRITICAL | `DEEPTOOLS_PLOTPROFILE` | containerization | L1727–1774 | ✅ |
| 106 | `STORAGE-001` | 🟠 MAJOR | `DEEPTOOLS_PLOTPROFILE` | storage | L1727–1774 | — |
| 107 | `RESOURCE-001` | 🟡 MINOR | `DEEPTOOLS_PLOTPROFILE` | resource_hints | L1727–1774 | — |
| 108 | `RESOURCE-002` | 🟡 MINOR | `DEEPTOOLS_PLOTPROFILE` | resource_hints | L1727–1774 | — |
| 109 | `CONTAINER-001` | 🔴 CRITICAL | `FASTQC` | containerization | L1778–1838 | ✅ |
| 110 | `STORAGE-001` | 🟠 MAJOR | `FASTQC` | storage | L1778–1838 | — |
| 111 | `RESOURCE-001` | 🟡 MINOR | `FASTQC` | resource_hints | L1778–1838 | — |
| 112 | `RESOURCE-002` | 🟡 MINOR | `FASTQC` | resource_hints | L1778–1838 | — |
| 113 | `CONTAINER-001` | 🔴 CRITICAL | `GFFREAD` | containerization | L1842–1901 | ✅ |
| 114 | `STORAGE-001` | 🟠 MAJOR | `GFFREAD` | storage | L1842–1901 | — |
| 115 | `RESOURCE-001` | 🟡 MINOR | `GFFREAD` | resource_hints | L1842–1901 | — |
| 116 | `RESOURCE-002` | 🟡 MINOR | `GFFREAD` | resource_hints | L1842–1901 | — |
| 117 | `CONTAINER-001` | 🔴 CRITICAL | `GUNZIP` | containerization | L1905–1959 | ✅ |
| 118 | `STORAGE-001` | 🟠 MAJOR | `GUNZIP` | storage | L1905–1959 | — |
| 119 | `RESOURCE-001` | 🟡 MINOR | `GUNZIP` | resource_hints | L1905–1959 | — |
| 120 | `RESOURCE-002` | 🟡 MINOR | `GUNZIP` | resource_hints | L1905–1959 | — |
| 121 | `CONTAINER-001` | 🔴 CRITICAL | `HOMER_ANNOTATEPEAKS` | containerization | L1963–2004 | ✅ |
| 122 | `STORAGE-001` | 🟠 MAJOR | `HOMER_ANNOTATEPEAKS` | storage | L1963–2004 | — |
| 123 | `RESOURCE-001` | 🟡 MINOR | `HOMER_ANNOTATEPEAKS` | resource_hints | L1963–2004 | — |
| 124 | `RESOURCE-002` | 🟡 MINOR | `HOMER_ANNOTATEPEAKS` | resource_hints | L1963–2004 | — |
| 125 | `CONTAINER-001` | 🔴 CRITICAL | `KHMER_UNIQUEKMERS` | containerization | L2008–2045 | ✅ |
| 126 | `STORAGE-001` | 🟠 MAJOR | `KHMER_UNIQUEKMERS` | storage | L2008–2045 | — |
| 127 | `RESOURCE-001` | 🟡 MINOR | `KHMER_UNIQUEKMERS` | resource_hints | L2008–2045 | — |
| 128 | `RESOURCE-002` | 🟡 MINOR | `KHMER_UNIQUEKMERS` | resource_hints | L2008–2045 | — |
| 129 | `CONTAINER-001` | 🔴 CRITICAL | `MACS3_CALLPEAK` | containerization | L2050–2118 | ✅ |
| 130 | `STORAGE-001` | 🟠 MAJOR | `MACS3_CALLPEAK` | storage | L2050–2118 | — |
| 131 | `RESOURCE-001` | 🟡 MINOR | `MACS3_CALLPEAK` | resource_hints | L2050–2118 | — |
| 132 | `RESOURCE-002` | 🟡 MINOR | `MACS3_CALLPEAK` | resource_hints | L2050–2118 | — |
| 133 | `CONTAINER-001` | 🔴 CRITICAL | `MULTIQC` | containerization | L2122–2182 | ✅ |
| 134 | `STORAGE-001` | 🟠 MAJOR | `MULTIQC` | storage | L2122–2182 | — |
| 135 | `RESOURCE-001` | 🟡 MINOR | `MULTIQC` | resource_hints | L2122–2182 | — |
| 136 | `RESOURCE-002` | 🟡 MINOR | `MULTIQC` | resource_hints | L2122–2182 | — |
| 137 | `CONTAINER-001` | 🔴 CRITICAL | `PHANTOMPEAKQUALTOOLS` | containerization | L2186–2236 | ✅ |
| 138 | `STORAGE-001` | 🟠 MAJOR | `PHANTOMPEAKQUALTOOLS` | storage | L2186–2236 | — |
| 139 | `RESOURCE-001` | 🟡 MINOR | `PHANTOMPEAKQUALTOOLS` | resource_hints | L2186–2236 | — |
| 140 | `RESOURCE-002` | 🟡 MINOR | `PHANTOMPEAKQUALTOOLS` | resource_hints | L2186–2236 | — |
| 141 | `CONTAINER-001` | 🔴 CRITICAL | `PICARD_COLLECTMULTIPLEMETRICS` | containerization | L2240–2306 | ✅ |
| 142 | `RESOURCE-001` | 🟡 MINOR | `PICARD_COLLECTMULTIPLEMETRICS` | resource_hints | L2240–2306 | — |
| 143 | `RESOURCE-002` | 🟡 MINOR | `PICARD_COLLECTMULTIPLEMETRICS` | resource_hints | L2240–2306 | — |
| 144 | `CONTAINER-001` | 🔴 CRITICAL | `PICARD_MARKDUPLICATES` | containerization | L2310–2377 | ✅ |
| 145 | `RESOURCE-001` | 🟡 MINOR | `PICARD_MARKDUPLICATES` | resource_hints | L2310–2377 | — |
| 146 | `RESOURCE-002` | 🟡 MINOR | `PICARD_MARKDUPLICATES` | resource_hints | L2310–2377 | — |
| 147 | `CONTAINER-001` | 🔴 CRITICAL | `PICARD_MERGESAMFILES` | containerization | L2381–2432 | ✅ |
| 148 | `RESOURCE-001` | 🟡 MINOR | `PICARD_MERGESAMFILES` | resource_hints | L2381–2432 | — |
| 149 | `RESOURCE-002` | 🟡 MINOR | `PICARD_MERGESAMFILES` | resource_hints | L2381–2432 | — |
| 150 | `CONTAINER-001` | 🔴 CRITICAL | `PRESEQ_LCEXTRAP` | containerization | L2436–2488 | ✅ |
| 151 | `STORAGE-001` | 🟠 MAJOR | `PRESEQ_LCEXTRAP` | storage | L2436–2488 | — |
| 152 | `RESOURCE-001` | 🟡 MINOR | `PRESEQ_LCEXTRAP` | resource_hints | L2436–2488 | — |
| 153 | `RESOURCE-002` | 🟡 MINOR | `PRESEQ_LCEXTRAP` | resource_hints | L2436–2488 | — |
| 154 | `CONTAINER-001` | 🔴 CRITICAL | `SAMTOOLS_FLAGSTAT` | containerization | L2492–2537 | ✅ |
| 155 | `STORAGE-001` | 🟠 MAJOR | `SAMTOOLS_FLAGSTAT` | storage | L2492–2537 | — |
| 156 | `RESOURCE-001` | 🟡 MINOR | `SAMTOOLS_FLAGSTAT` | resource_hints | L2492–2537 | — |
| 157 | `RESOURCE-002` | 🟡 MINOR | `SAMTOOLS_FLAGSTAT` | resource_hints | L2492–2537 | — |
| 158 | `CONTAINER-001` | 🔴 CRITICAL | `SAMTOOLS_IDXSTATS` | containerization | L2541–2588 | ✅ |
| 159 | `STORAGE-001` | 🟠 MAJOR | `SAMTOOLS_IDXSTATS` | storage | L2541–2588 | — |
| 160 | `RESOURCE-001` | 🟡 MINOR | `SAMTOOLS_IDXSTATS` | resource_hints | L2541–2588 | — |
| 161 | `RESOURCE-002` | 🟡 MINOR | `SAMTOOLS_IDXSTATS` | resource_hints | L2541–2588 | — |
| 162 | `CONTAINER-001` | 🔴 CRITICAL | `SAMTOOLS_INDEX` | containerization | L2592–2640 | ✅ |
| 163 | `STORAGE-001` | 🟠 MAJOR | `SAMTOOLS_INDEX` | storage | L2592–2640 | — |
| 164 | `RESOURCE-001` | 🟡 MINOR | `SAMTOOLS_INDEX` | resource_hints | L2592–2640 | — |
| 165 | `RESOURCE-002` | 🟡 MINOR | `SAMTOOLS_INDEX` | resource_hints | L2592–2640 | — |
| 166 | `CONTAINER-001` | 🔴 CRITICAL | `SAMTOOLS_SORT` | containerization | L2644–2716 | ✅ |
| 167 | `STORAGE-001` | 🟠 MAJOR | `SAMTOOLS_SORT` | storage | L2644–2716 | — |
| 168 | `RESOURCE-001` | 🟡 MINOR | `SAMTOOLS_SORT` | resource_hints | L2644–2716 | — |
| 169 | `RESOURCE-002` | 🟡 MINOR | `SAMTOOLS_SORT` | resource_hints | L2644–2716 | — |
| 170 | `CONTAINER-001` | 🔴 CRITICAL | `SAMTOOLS_STATS` | containerization | L2720–2768 | ✅ |
| 171 | `STORAGE-001` | 🟠 MAJOR | `SAMTOOLS_STATS` | storage | L2720–2768 | — |
| 172 | `RESOURCE-001` | 🟡 MINOR | `SAMTOOLS_STATS` | resource_hints | L2720–2768 | — |
| 173 | `RESOURCE-002` | 🟡 MINOR | `SAMTOOLS_STATS` | resource_hints | L2720–2768 | — |
| 174 | `CONTAINER-001` | 🔴 CRITICAL | `SUBREAD_FEATURECOUNTS` | containerization | L2772–2830 | ✅ |
| 175 | `STORAGE-001` | 🟠 MAJOR | `SUBREAD_FEATURECOUNTS` | storage | L2772–2830 | — |
| 176 | `RESOURCE-001` | 🟡 MINOR | `SUBREAD_FEATURECOUNTS` | resource_hints | L2772–2830 | — |
| 177 | `RESOURCE-002` | 🟡 MINOR | `SUBREAD_FEATURECOUNTS` | resource_hints | L2772–2830 | — |
| 178 | `CONTAINER-001` | 🔴 CRITICAL | `TRIMGALORE` | containerization | L2834–2929 | ✅ |
| 179 | `STORAGE-001` | 🟠 MAJOR | `TRIMGALORE` | storage | L2834–2929 | — |
| 180 | `RESOURCE-001` | 🟡 MINOR | `TRIMGALORE` | resource_hints | L2834–2929 | — |
| 181 | `RESOURCE-002` | 🟡 MINOR | `TRIMGALORE` | resource_hints | L2834–2929 | — |
| 182 | `CONTAINER-001` | 🔴 CRITICAL | `UCSC_BEDGRAPHTOBIGWIG` | containerization | L2933–2981 | ✅ |
| 183 | `STORAGE-001` | 🟠 MAJOR | `UCSC_BEDGRAPHTOBIGWIG` | storage | L2933–2981 | — |
| 184 | `RESOURCE-001` | 🟡 MINOR | `UCSC_BEDGRAPHTOBIGWIG` | resource_hints | L2933–2981 | — |
| 185 | `RESOURCE-002` | 🟡 MINOR | `UCSC_BEDGRAPHTOBIGWIG` | resource_hints | L2933–2981 | — |
| 186 | `CONTAINER-001` | 🔴 CRITICAL | `UMITOOLS_EXTRACT` | containerization | L2985–3058 | ✅ |
| 187 | `STORAGE-001` | 🟠 MAJOR | `UMITOOLS_EXTRACT` | storage | L2985–3058 | — |
| 188 | `RESOURCE-001` | 🟡 MINOR | `UMITOOLS_EXTRACT` | resource_hints | L2985–3058 | — |
| 189 | `RESOURCE-002` | 🟡 MINOR | `UMITOOLS_EXTRACT` | resource_hints | L2985–3058 | — |
| 190 | `CONTAINER-001` | 🔴 CRITICAL | `UNTAR` | containerization | L3062–3145 | ✅ |
| 191 | `STORAGE-001` | 🟠 MAJOR | `UNTAR` | storage | L3062–3145 | — |
| 192 | `RESOURCE-001` | 🟡 MINOR | `UNTAR` | resource_hints | L3062–3145 | — |
| 193 | `RESOURCE-002` | 🟡 MINOR | `UNTAR` | resource_hints | L3062–3145 | — |
| 194 | `CONTAINER-001` | 🔴 CRITICAL | `UNTARFILES` | containerization | L3149–3200 | ✅ |
| 195 | `STORAGE-001` | 🟠 MAJOR | `UNTARFILES` | storage | L3149–3200 | — |
| 196 | `RESOURCE-001` | 🟡 MINOR | `UNTARFILES` | resource_hints | L3149–3200 | — |
| 197 | `RESOURCE-002` | 🟡 MINOR | `UNTARFILES` | resource_hints | L3149–3200 | — |

### Detail

<details><summary>🔴 <strong>1. CONTAINER-001 — ANNOTATE_BOOLEAN_PEAKS</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L182–209  
**Auto-fixable:** Yes

**Description:**  
Process 'ANNOTATE_BOOLEAN_PEAKS' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟠 <strong>2. STORAGE-001 — ANNOTATE_BOOLEAN_PEAKS</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L182–209  
**Auto-fixable:** No

**Description:**  
Process 'ANNOTATE_BOOLEAN_PEAKS' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
//, //
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>3. RESOURCE-001 — ANNOTATE_BOOLEAN_PEAKS</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L182–209  
**Auto-fixable:** No

**Description:**  
Process 'ANNOTATE_BOOLEAN_PEAKS' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>4. RESOURCE-002 — ANNOTATE_BOOLEAN_PEAKS</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L182–209  
**Auto-fixable:** No

**Description:**  
Process 'ANNOTATE_BOOLEAN_PEAKS' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>5. CONTAINER-001 — BAM_REMOVE_ORPHANS</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L216–258  
**Auto-fixable:** Yes

**Description:**  
Process 'BAM_REMOVE_ORPHANS' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟡 <strong>6. RESOURCE-001 — BAM_REMOVE_ORPHANS</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L216–258  
**Auto-fixable:** No

**Description:**  
Process 'BAM_REMOVE_ORPHANS' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>7. RESOURCE-002 — BAM_REMOVE_ORPHANS</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L216–258  
**Auto-fixable:** No

**Description:**  
Process 'BAM_REMOVE_ORPHANS' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>8. CONTAINER-001 — BAMTOOLS_FILTER</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L262–304  
**Auto-fixable:** Yes

**Description:**  
Process 'BAMTOOLS_FILTER' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟠 <strong>9. STORAGE-001 — BAMTOOLS_FILTER</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L262–304  
**Auto-fixable:** No

**Description:**  
Process 'BAMTOOLS_FILTER' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
//, /Using., // ... (3 more)
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>10. RESOURCE-001 — BAMTOOLS_FILTER</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L262–304  
**Auto-fixable:** No

**Description:**  
Process 'BAMTOOLS_FILTER' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>11. RESOURCE-002 — BAMTOOLS_FILTER</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L262–304  
**Auto-fixable:** No

**Description:**  
Process 'BAMTOOLS_FILTER' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>12. CONTAINER-001 — BEDTOOLS_GENOMECOV</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L308–350  
**Auto-fixable:** Yes

**Description:**  
Process 'BEDTOOLS_GENOMECOV' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟠 <strong>13. STORAGE-001 — BEDTOOLS_GENOMECOV</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L308–350  
**Auto-fixable:** No

**Description:**  
Process 'BEDTOOLS_GENOMECOV' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
/bedtools, //g
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>14. RESOURCE-001 — BEDTOOLS_GENOMECOV</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L308–350  
**Auto-fixable:** No

**Description:**  
Process 'BEDTOOLS_GENOMECOV' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>15. RESOURCE-002 — BEDTOOLS_GENOMECOV</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L308–350  
**Auto-fixable:** No

**Description:**  
Process 'BEDTOOLS_GENOMECOV' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>16. CONTAINER-001 — DESEQ2_QC</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L354–410  
**Auto-fixable:** Yes

**Description:**  
Process 'DESEQ2_QC' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟠 <strong>17. STORAGE-001 — DESEQ2_QC</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L354–410  
**Auto-fixable:** No

**Description:**  
Process 'DESEQ2_QC' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
/deseq2_pca/deseq2_pca_, /g, /DESeq2 ... (7 more)
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>18. RESOURCE-001 — DESEQ2_QC</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L354–410  
**Auto-fixable:** No

**Description:**  
Process 'DESEQ2_QC' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>19. RESOURCE-002 — DESEQ2_QC</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L354–410  
**Auto-fixable:** No

**Description:**  
Process 'DESEQ2_QC' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>20. CONTAINER-001 — FRIP_SCORE</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L414–447  
**Auto-fixable:** Yes

**Description:**  
Process 'FRIP_SCORE' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟠 <strong>21. STORAGE-001 — FRIP_SCORE</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L414–447  
**Auto-fixable:** No

**Description:**  
Process 'FRIP_SCORE' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
/bedtools, //g, // ... (2 more)
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>22. RESOURCE-001 — FRIP_SCORE</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L414–447  
**Auto-fixable:** No

**Description:**  
Process 'FRIP_SCORE' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>23. RESOURCE-002 — FRIP_SCORE</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L414–447  
**Auto-fixable:** No

**Description:**  
Process 'FRIP_SCORE' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>24. CONTAINER-001 — GENOME_BLACKLIST_REGIONS</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L454–494  
**Auto-fixable:** Yes

**Description:**  
Process 'GENOME_BLACKLIST_REGIONS' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟠 <strong>25. STORAGE-001 — GENOME_BLACKLIST_REGIONS</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L454–494  
**Auto-fixable:** No

**Description:**  
Process 'GENOME_BLACKLIST_REGIONS' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
/bedtools, //g, /bedtools ... (1 more)
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>26. RESOURCE-001 — GENOME_BLACKLIST_REGIONS</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L454–494  
**Auto-fixable:** No

**Description:**  
Process 'GENOME_BLACKLIST_REGIONS' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>27. RESOURCE-002 — GENOME_BLACKLIST_REGIONS</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L454–494  
**Auto-fixable:** No

**Description:**  
Process 'GENOME_BLACKLIST_REGIONS' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>28. CONTAINER-001 — GTF2BED</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L498–528  
**Auto-fixable:** Yes

**Description:**  
Process 'GTF2BED' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟡 <strong>29. RESOURCE-001 — GTF2BED</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L498–528  
**Auto-fixable:** No

**Description:**  
Process 'GTF2BED' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>30. RESOURCE-002 — GTF2BED</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L498–528  
**Auto-fixable:** No

**Description:**  
Process 'GTF2BED' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>31. CONTAINER-001 — IGV</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L535–581  
**Auto-fixable:** Yes

**Description:**  
Process 'IGV' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟡 <strong>32. RESOURCE-001 — IGV</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L535–581  
**Auto-fixable:** No

**Description:**  
Process 'IGV' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>33. RESOURCE-002 — IGV</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L535–581  
**Auto-fixable:** No

**Description:**  
Process 'IGV' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>34. CONTAINER-001 — MACS3_CONSENSUS</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L588–648  
**Auto-fixable:** Yes

**Description:**  
Process 'MACS3_CONSENSUS' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟡 <strong>35. RESOURCE-001 — MACS3_CONSENSUS</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L588–648  
**Auto-fixable:** No

**Description:**  
Process 'MACS3_CONSENSUS' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>36. RESOURCE-002 — MACS3_CONSENSUS</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L588–648  
**Auto-fixable:** No

**Description:**  
Process 'MACS3_CONSENSUS' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>37. CONTAINER-001 — MULTIQC</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L652–726  
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

<details><summary>🟠 <strong>38. STORAGE-001 — MULTIQC</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L652–726  
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

<details><summary>🟡 <strong>39. RESOURCE-001 — MULTIQC</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L652–726  
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

<details><summary>🟡 <strong>40. RESOURCE-002 — MULTIQC</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L652–726  
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

<details><summary>🔴 <strong>41. CONTAINER-001 — MULTIQC_CUSTOM_PEAKS</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L730–762  
**Auto-fixable:** Yes

**Description:**  
Process 'MULTIQC_CUSTOM_PEAKS' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟠 <strong>42. STORAGE-001 — MULTIQC_CUSTOM_PEAKS</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L730–762  
**Auto-fixable:** No

**Description:**  
Process 'MULTIQC_CUSTOM_PEAKS' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
//, //
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>43. RESOURCE-001 — MULTIQC_CUSTOM_PEAKS</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L730–762  
**Auto-fixable:** No

**Description:**  
Process 'MULTIQC_CUSTOM_PEAKS' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>44. RESOURCE-002 — MULTIQC_CUSTOM_PEAKS</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L730–762  
**Auto-fixable:** No

**Description:**  
Process 'MULTIQC_CUSTOM_PEAKS' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>45. CONTAINER-001 — MULTIQC_CUSTOM_PHANTOMPEAKQUALTOOLS</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L766–801  
**Auto-fixable:** Yes

**Description:**  
Process 'MULTIQC_CUSTOM_PHANTOMPEAKQUALTOOLS' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟠 <strong>46. STORAGE-001 — MULTIQC_CUSTOM_PHANTOMPEAKQUALTOOLS</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L766–801  
**Auto-fixable:** No

**Description:**  
Process 'MULTIQC_CUSTOM_PHANTOMPEAKQUALTOOLS' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
//, //
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>47. RESOURCE-001 — MULTIQC_CUSTOM_PHANTOMPEAKQUALTOOLS</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L766–801  
**Auto-fixable:** No

**Description:**  
Process 'MULTIQC_CUSTOM_PHANTOMPEAKQUALTOOLS' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>48. RESOURCE-002 — MULTIQC_CUSTOM_PHANTOMPEAKQUALTOOLS</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L766–801  
**Auto-fixable:** No

**Description:**  
Process 'MULTIQC_CUSTOM_PHANTOMPEAKQUALTOOLS' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>49. CONTAINER-001 — PLOT_HOMER_ANNOTATEPEAKS</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L805–844  
**Auto-fixable:** Yes

**Description:**  
Process 'PLOT_HOMER_ANNOTATEPEAKS' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟡 <strong>50. RESOURCE-001 — PLOT_HOMER_ANNOTATEPEAKS</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L805–844  
**Auto-fixable:** No

**Description:**  
Process 'PLOT_HOMER_ANNOTATEPEAKS' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>51. RESOURCE-002 — PLOT_HOMER_ANNOTATEPEAKS</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L805–844  
**Auto-fixable:** No

**Description:**  
Process 'PLOT_HOMER_ANNOTATEPEAKS' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>52. CONTAINER-001 — PLOT_MACS3_QC</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L848–882  
**Auto-fixable:** Yes

**Description:**  
Process 'PLOT_MACS3_QC' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟡 <strong>53. RESOURCE-001 — PLOT_MACS3_QC</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L848–882  
**Auto-fixable:** No

**Description:**  
Process 'PLOT_MACS3_QC' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>54. RESOURCE-002 — PLOT_MACS3_QC</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L848–882  
**Auto-fixable:** No

**Description:**  
Process 'PLOT_MACS3_QC' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>55. CONTAINER-001 — SAMPLESHEET_CHECK</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L886–917  
**Auto-fixable:** Yes

**Description:**  
Process 'SAMPLESHEET_CHECK' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟡 <strong>56. RESOURCE-001 — SAMPLESHEET_CHECK</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L886–917  
**Auto-fixable:** No

**Description:**  
Process 'SAMPLESHEET_CHECK' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>57. RESOURCE-002 — SAMPLESHEET_CHECK</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L886–917  
**Auto-fixable:** No

**Description:**  
Process 'SAMPLESHEET_CHECK' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>58. CONTAINER-001 — STAR_ALIGN</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L921–981  
**Auto-fixable:** Yes

**Description:**  
Process 'STAR_ALIGN' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟠 <strong>59. STORAGE-001 — STAR_ALIGN</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L921–981  
**Auto-fixable:** No

**Description:**  
Process 'STAR_ALIGN' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
/STAR_//g
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>60. RESOURCE-001 — STAR_ALIGN</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L921–981  
**Auto-fixable:** No

**Description:**  
Process 'STAR_ALIGN' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>61. RESOURCE-002 — STAR_ALIGN</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L921–981  
**Auto-fixable:** No

**Description:**  
Process 'STAR_ALIGN' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>62. CONTAINER-001 — STAR_GENOMEGENERATE</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L985–1045  
**Auto-fixable:** Yes

**Description:**  
Process 'STAR_GENOMEGENERATE' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟠 <strong>63. STORAGE-001 — STAR_GENOMEGENERATE</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L985–1045  
**Auto-fixable:** No

**Description:**  
Process 'STAR_GENOMEGENERATE' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
/STAR_//g, /log, /2 ... (3 more)
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>64. RESOURCE-001 — STAR_GENOMEGENERATE</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L985–1045  
**Auto-fixable:** No

**Description:**  
Process 'STAR_GENOMEGENERATE' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>65. RESOURCE-002 — STAR_GENOMEGENERATE</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L985–1045  
**Auto-fixable:** No

**Description:**  
Process 'STAR_GENOMEGENERATE' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>66. CONTAINER-001 — BOWTIE2_ALIGN</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L1049–1165  
**Auto-fixable:** Yes

**Description:**  
Process 'BOWTIE2_ALIGN' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟠 <strong>67. STORAGE-001 — BOWTIE2_ALIGN</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L1049–1165  
**Auto-fixable:** No

**Description:**  
Process 'BOWTIE2_ALIGN' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
//, //, // ... (6 more)
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>68. RESOURCE-001 — BOWTIE2_ALIGN</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L1049–1165  
**Auto-fixable:** No

**Description:**  
Process 'BOWTIE2_ALIGN' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>69. RESOURCE-002 — BOWTIE2_ALIGN</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L1049–1165  
**Auto-fixable:** No

**Description:**  
Process 'BOWTIE2_ALIGN' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>70. CONTAINER-001 — BOWTIE2_BUILD</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L1169–1210  
**Auto-fixable:** Yes

**Description:**  
Process 'BOWTIE2_BUILD' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟠 <strong>71. STORAGE-001 — BOWTIE2_BUILD</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L1169–1210  
**Auto-fixable:** No

**Description:**  
Process 'BOWTIE2_BUILD' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
//, //
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>72. RESOURCE-001 — BOWTIE2_BUILD</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L1169–1210  
**Auto-fixable:** No

**Description:**  
Process 'BOWTIE2_BUILD' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>73. RESOURCE-002 — BOWTIE2_BUILD</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L1169–1210  
**Auto-fixable:** No

**Description:**  
Process 'BOWTIE2_BUILD' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>74. CONTAINER-001 — BWA_INDEX</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L1214–1266  
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

<details><summary>🟠 <strong>75. STORAGE-001 — BWA_INDEX</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L1214–1266  
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

<details><summary>🟡 <strong>76. RESOURCE-001 — BWA_INDEX</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L1214–1266  
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

<details><summary>🟡 <strong>77. RESOURCE-002 — BWA_INDEX</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L1214–1266  
**Auto-fixable:** No

**Description:**  
Process 'BWA_INDEX' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>78. CONTAINER-001 — BWA_MEM</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L1270–1345  
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

<details><summary>🟠 <strong>79. STORAGE-001 — BWA_MEM</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L1270–1345  
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

<details><summary>🟡 <strong>80. RESOURCE-001 — BWA_MEM</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L1270–1345  
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

<details><summary>🟡 <strong>81. RESOURCE-002 — BWA_MEM</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L1270–1345  
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

<details><summary>🔴 <strong>82. CONTAINER-001 — CHROMAP_CHROMAP</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L1349–1461  
**Auto-fixable:** Yes

**Description:**  
Process 'CHROMAP_CHROMAP' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟠 <strong>83. STORAGE-001 — CHROMAP_CHROMAP</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L1349–1461  
**Auto-fixable:** No

**Description:**  
Process 'CHROMAP_CHROMAP' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
//, /Using., // ... (3 more)
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>84. RESOURCE-001 — CHROMAP_CHROMAP</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L1349–1461  
**Auto-fixable:** No

**Description:**  
Process 'CHROMAP_CHROMAP' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>85. RESOURCE-002 — CHROMAP_CHROMAP</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L1349–1461  
**Auto-fixable:** No

**Description:**  
Process 'CHROMAP_CHROMAP' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>86. CONTAINER-001 — CHROMAP_INDEX</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L1465–1511  
**Auto-fixable:** Yes

**Description:**  
Process 'CHROMAP_INDEX' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟡 <strong>87. RESOURCE-001 — CHROMAP_INDEX</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L1465–1511  
**Auto-fixable:** No

**Description:**  
Process 'CHROMAP_INDEX' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>88. RESOURCE-002 — CHROMAP_INDEX</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L1465–1511  
**Auto-fixable:** No

**Description:**  
Process 'CHROMAP_INDEX' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>89. CONTAINER-001 — CUSTOM_GETCHROMSIZES</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L1515–1561  
**Auto-fixable:** Yes

**Description:**  
Process 'CUSTOM_GETCHROMSIZES' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟠 <strong>90. STORAGE-001 — CUSTOM_GETCHROMSIZES</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L1515–1561  
**Auto-fixable:** No

**Description:**  
Process 'CUSTOM_GETCHROMSIZES' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
//, /Using., //
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>91. RESOURCE-001 — CUSTOM_GETCHROMSIZES</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L1515–1561  
**Auto-fixable:** No

**Description:**  
Process 'CUSTOM_GETCHROMSIZES' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>92. RESOURCE-002 — CUSTOM_GETCHROMSIZES</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L1515–1561  
**Auto-fixable:** No

**Description:**  
Process 'CUSTOM_GETCHROMSIZES' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>93. CONTAINER-001 — DEEPTOOLS_COMPUTEMATRIX</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L1565–1615  
**Auto-fixable:** Yes

**Description:**  
Process 'DEEPTOOLS_COMPUTEMATRIX' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟠 <strong>94. STORAGE-001 — DEEPTOOLS_COMPUTEMATRIX</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L1565–1615  
**Auto-fixable:** No

**Description:**  
Process 'DEEPTOOLS_COMPUTEMATRIX' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
/computeMatrix, //g
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>95. RESOURCE-001 — DEEPTOOLS_COMPUTEMATRIX</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L1565–1615  
**Auto-fixable:** No

**Description:**  
Process 'DEEPTOOLS_COMPUTEMATRIX' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>96. RESOURCE-002 — DEEPTOOLS_COMPUTEMATRIX</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L1565–1615  
**Auto-fixable:** No

**Description:**  
Process 'DEEPTOOLS_COMPUTEMATRIX' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>97. CONTAINER-001 — DEEPTOOLS_PLOTFINGERPRINT</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L1619–1672  
**Auto-fixable:** Yes

**Description:**  
Process 'DEEPTOOLS_PLOTFINGERPRINT' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟠 <strong>98. STORAGE-001 — DEEPTOOLS_PLOTFINGERPRINT</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L1619–1672  
**Auto-fixable:** No

**Description:**  
Process 'DEEPTOOLS_PLOTFINGERPRINT' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
/plotFingerprint, //g
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>99. RESOURCE-001 — DEEPTOOLS_PLOTFINGERPRINT</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L1619–1672  
**Auto-fixable:** No

**Description:**  
Process 'DEEPTOOLS_PLOTFINGERPRINT' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>100. RESOURCE-002 — DEEPTOOLS_PLOTFINGERPRINT</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L1619–1672  
**Auto-fixable:** No

**Description:**  
Process 'DEEPTOOLS_PLOTFINGERPRINT' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>101. CONTAINER-001 — DEEPTOOLS_PLOTHEATMAP</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L1676–1723  
**Auto-fixable:** Yes

**Description:**  
Process 'DEEPTOOLS_PLOTHEATMAP' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟠 <strong>102. STORAGE-001 — DEEPTOOLS_PLOTHEATMAP</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L1676–1723  
**Auto-fixable:** No

**Description:**  
Process 'DEEPTOOLS_PLOTHEATMAP' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
/plotHeatmap, //g
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>103. RESOURCE-001 — DEEPTOOLS_PLOTHEATMAP</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L1676–1723  
**Auto-fixable:** No

**Description:**  
Process 'DEEPTOOLS_PLOTHEATMAP' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>104. RESOURCE-002 — DEEPTOOLS_PLOTHEATMAP</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L1676–1723  
**Auto-fixable:** No

**Description:**  
Process 'DEEPTOOLS_PLOTHEATMAP' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>105. CONTAINER-001 — DEEPTOOLS_PLOTPROFILE</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L1727–1774  
**Auto-fixable:** Yes

**Description:**  
Process 'DEEPTOOLS_PLOTPROFILE' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟠 <strong>106. STORAGE-001 — DEEPTOOLS_PLOTPROFILE</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L1727–1774  
**Auto-fixable:** No

**Description:**  
Process 'DEEPTOOLS_PLOTPROFILE' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
/plotProfile, //g
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>107. RESOURCE-001 — DEEPTOOLS_PLOTPROFILE</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L1727–1774  
**Auto-fixable:** No

**Description:**  
Process 'DEEPTOOLS_PLOTPROFILE' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>108. RESOURCE-002 — DEEPTOOLS_PLOTPROFILE</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L1727–1774  
**Auto-fixable:** No

**Description:**  
Process 'DEEPTOOLS_PLOTPROFILE' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>109. CONTAINER-001 — FASTQC</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L1778–1838  
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

<details><summary>🟠 <strong>110. STORAGE-001 — FASTQC</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L1778–1838  
**Auto-fixable:** No

**Description:**  
Process 'FASTQC' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
//, //, /FastQC ... (2 more)
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>111. RESOURCE-001 — FASTQC</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L1778–1838  
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

<details><summary>🟡 <strong>112. RESOURCE-002 — FASTQC</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L1778–1838  
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

<details><summary>🔴 <strong>113. CONTAINER-001 — GFFREAD</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L1842–1901  
**Auto-fixable:** Yes

**Description:**  
Process 'GFFREAD' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟠 <strong>114. STORAGE-001 — GFFREAD</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L1842–1901  
**Auto-fixable:** No

**Description:**  
Process 'GFFREAD' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
//
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>115. RESOURCE-001 — GFFREAD</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L1842–1901  
**Auto-fixable:** No

**Description:**  
Process 'GFFREAD' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>116. RESOURCE-002 — GFFREAD</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L1842–1901  
**Auto-fixable:** No

**Description:**  
Process 'GFFREAD' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>117. CONTAINER-001 — GUNZIP</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L1905–1959  
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

<details><summary>🟠 <strong>118. STORAGE-001 — GUNZIP</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L1905–1959  
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

<details><summary>🟡 <strong>119. RESOURCE-001 — GUNZIP</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L1905–1959  
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

<details><summary>🟡 <strong>120. RESOURCE-002 — GUNZIP</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L1905–1959  
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

<details><summary>🔴 <strong>121. CONTAINER-001 — HOMER_ANNOTATEPEAKS</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L1963–2004  
**Auto-fixable:** Yes

**Description:**  
Process 'HOMER_ANNOTATEPEAKS' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟠 <strong>122. STORAGE-001 — HOMER_ANNOTATEPEAKS</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L1963–2004  
**Auto-fixable:** No

**Description:**  
Process 'HOMER_ANNOTATEPEAKS' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
//
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>123. RESOURCE-001 — HOMER_ANNOTATEPEAKS</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L1963–2004  
**Auto-fixable:** No

**Description:**  
Process 'HOMER_ANNOTATEPEAKS' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>124. RESOURCE-002 — HOMER_ANNOTATEPEAKS</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L1963–2004  
**Auto-fixable:** No

**Description:**  
Process 'HOMER_ANNOTATEPEAKS' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>125. CONTAINER-001 — KHMER_UNIQUEKMERS</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L2008–2045  
**Auto-fixable:** Yes

**Description:**  
Process 'KHMER_UNIQUEKMERS' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟠 <strong>126. STORAGE-001 — KHMER_UNIQUEKMERS</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L2008–2045  
**Auto-fixable:** No

**Description:**  
Process 'KHMER_UNIQUEKMERS' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
//g, //, //
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>127. RESOURCE-001 — KHMER_UNIQUEKMERS</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L2008–2045  
**Auto-fixable:** No

**Description:**  
Process 'KHMER_UNIQUEKMERS' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>128. RESOURCE-002 — KHMER_UNIQUEKMERS</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L2008–2045  
**Auto-fixable:** No

**Description:**  
Process 'KHMER_UNIQUEKMERS' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>129. CONTAINER-001 — MACS3_CALLPEAK</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L2050–2118  
**Auto-fixable:** Yes

**Description:**  
Process 'MACS3_CALLPEAK' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟠 <strong>130. STORAGE-001 — MACS3_CALLPEAK</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L2050–2118  
**Auto-fixable:** No

**Description:**  
Process 'MACS3_CALLPEAK' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
/macs3, //g
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>131. RESOURCE-001 — MACS3_CALLPEAK</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L2050–2118  
**Auto-fixable:** No

**Description:**  
Process 'MACS3_CALLPEAK' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>132. RESOURCE-002 — MACS3_CALLPEAK</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L2050–2118  
**Auto-fixable:** No

**Description:**  
Process 'MACS3_CALLPEAK' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>133. CONTAINER-001 — MULTIQC</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L2122–2182  
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

<details><summary>🟠 <strong>134. STORAGE-001 — MULTIQC</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L2122–2182  
**Auto-fixable:** No

**Description:**  
Process 'MULTIQC' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
/--cl-config, /multiqc, //g
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>135. RESOURCE-001 — MULTIQC</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L2122–2182  
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

<details><summary>🟡 <strong>136. RESOURCE-002 — MULTIQC</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L2122–2182  
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

<details><summary>🔴 <strong>137. CONTAINER-001 — PHANTOMPEAKQUALTOOLS</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L2186–2236  
**Auto-fixable:** Yes

**Description:**  
Process 'PHANTOMPEAKQUALTOOLS' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟠 <strong>138. STORAGE-001 — PHANTOMPEAKQUALTOOLS</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L2186–2236  
**Auto-fixable:** No

**Description:**  
Process 'PHANTOMPEAKQUALTOOLS' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
//
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>139. RESOURCE-001 — PHANTOMPEAKQUALTOOLS</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L2186–2236  
**Auto-fixable:** No

**Description:**  
Process 'PHANTOMPEAKQUALTOOLS' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>140. RESOURCE-002 — PHANTOMPEAKQUALTOOLS</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L2186–2236  
**Auto-fixable:** No

**Description:**  
Process 'PHANTOMPEAKQUALTOOLS' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>141. CONTAINER-001 — PICARD_COLLECTMULTIPLEMETRICS</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L2240–2306  
**Auto-fixable:** Yes

**Description:**  
Process 'PICARD_COLLECTMULTIPLEMETRICS' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟡 <strong>142. RESOURCE-001 — PICARD_COLLECTMULTIPLEMETRICS</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L2240–2306  
**Auto-fixable:** No

**Description:**  
Process 'PICARD_COLLECTMULTIPLEMETRICS' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>143. RESOURCE-002 — PICARD_COLLECTMULTIPLEMETRICS</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L2240–2306  
**Auto-fixable:** No

**Description:**  
Process 'PICARD_COLLECTMULTIPLEMETRICS' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>144. CONTAINER-001 — PICARD_MARKDUPLICATES</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L2310–2377  
**Auto-fixable:** Yes

**Description:**  
Process 'PICARD_MARKDUPLICATES' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟡 <strong>145. RESOURCE-001 — PICARD_MARKDUPLICATES</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L2310–2377  
**Auto-fixable:** No

**Description:**  
Process 'PICARD_MARKDUPLICATES' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>146. RESOURCE-002 — PICARD_MARKDUPLICATES</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L2310–2377  
**Auto-fixable:** No

**Description:**  
Process 'PICARD_MARKDUPLICATES' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>147. CONTAINER-001 — PICARD_MERGESAMFILES</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L2381–2432  
**Auto-fixable:** Yes

**Description:**  
Process 'PICARD_MERGESAMFILES' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟡 <strong>148. RESOURCE-001 — PICARD_MERGESAMFILES</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L2381–2432  
**Auto-fixable:** No

**Description:**  
Process 'PICARD_MERGESAMFILES' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>149. RESOURCE-002 — PICARD_MERGESAMFILES</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L2381–2432  
**Auto-fixable:** No

**Description:**  
Process 'PICARD_MERGESAMFILES' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>150. CONTAINER-001 — PRESEQ_LCEXTRAP</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L2436–2488  
**Auto-fixable:** Yes

**Description:**  
Process 'PRESEQ_LCEXTRAP' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟠 <strong>151. STORAGE-001 — PRESEQ_LCEXTRAP</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L2436–2488  
**Auto-fixable:** No

**Description:**  
Process 'PRESEQ_LCEXTRAP' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
//, //, /Usage ... (1 more)
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>152. RESOURCE-001 — PRESEQ_LCEXTRAP</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L2436–2488  
**Auto-fixable:** No

**Description:**  
Process 'PRESEQ_LCEXTRAP' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>153. RESOURCE-002 — PRESEQ_LCEXTRAP</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L2436–2488  
**Auto-fixable:** No

**Description:**  
Process 'PRESEQ_LCEXTRAP' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>154. CONTAINER-001 — SAMTOOLS_FLAGSTAT</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L2492–2537  
**Auto-fixable:** Yes

**Description:**  
Process 'SAMTOOLS_FLAGSTAT' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟠 <strong>155. STORAGE-001 — SAMTOOLS_FLAGSTAT</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L2492–2537  
**Auto-fixable:** No

**Description:**  
Process 'SAMTOOLS_FLAGSTAT' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
//, /Using., //
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>156. RESOURCE-001 — SAMTOOLS_FLAGSTAT</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L2492–2537  
**Auto-fixable:** No

**Description:**  
Process 'SAMTOOLS_FLAGSTAT' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>157. RESOURCE-002 — SAMTOOLS_FLAGSTAT</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L2492–2537  
**Auto-fixable:** No

**Description:**  
Process 'SAMTOOLS_FLAGSTAT' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>158. CONTAINER-001 — SAMTOOLS_IDXSTATS</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L2541–2588  
**Auto-fixable:** Yes

**Description:**  
Process 'SAMTOOLS_IDXSTATS' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟠 <strong>159. STORAGE-001 — SAMTOOLS_IDXSTATS</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L2541–2588  
**Auto-fixable:** No

**Description:**  
Process 'SAMTOOLS_IDXSTATS' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
//, /Using., //
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>160. RESOURCE-001 — SAMTOOLS_IDXSTATS</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L2541–2588  
**Auto-fixable:** No

**Description:**  
Process 'SAMTOOLS_IDXSTATS' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>161. RESOURCE-002 — SAMTOOLS_IDXSTATS</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L2541–2588  
**Auto-fixable:** No

**Description:**  
Process 'SAMTOOLS_IDXSTATS' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>162. CONTAINER-001 — SAMTOOLS_INDEX</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L2592–2640  
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

<details><summary>🟠 <strong>163. STORAGE-001 — SAMTOOLS_INDEX</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L2592–2640  
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

<details><summary>🟡 <strong>164. RESOURCE-001 — SAMTOOLS_INDEX</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L2592–2640  
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

<details><summary>🟡 <strong>165. RESOURCE-002 — SAMTOOLS_INDEX</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L2592–2640  
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

<details><summary>🔴 <strong>166. CONTAINER-001 — SAMTOOLS_SORT</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L2644–2716  
**Auto-fixable:** Yes

**Description:**  
Process 'SAMTOOLS_SORT' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟠 <strong>167. STORAGE-001 — SAMTOOLS_SORT</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L2644–2716  
**Auto-fixable:** No

**Description:**  
Process 'SAMTOOLS_SORT' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
//, /Using., //
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>168. RESOURCE-001 — SAMTOOLS_SORT</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L2644–2716  
**Auto-fixable:** No

**Description:**  
Process 'SAMTOOLS_SORT' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>169. RESOURCE-002 — SAMTOOLS_SORT</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L2644–2716  
**Auto-fixable:** No

**Description:**  
Process 'SAMTOOLS_SORT' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>170. CONTAINER-001 — SAMTOOLS_STATS</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L2720–2768  
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

<details><summary>🟠 <strong>171. STORAGE-001 — SAMTOOLS_STATS</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L2720–2768  
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

<details><summary>🟡 <strong>172. RESOURCE-001 — SAMTOOLS_STATS</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L2720–2768  
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

<details><summary>🟡 <strong>173. RESOURCE-002 — SAMTOOLS_STATS</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L2720–2768  
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

<details><summary>🔴 <strong>174. CONTAINER-001 — SUBREAD_FEATURECOUNTS</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L2772–2830  
**Auto-fixable:** Yes

**Description:**  
Process 'SUBREAD_FEATURECOUNTS' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟠 <strong>175. STORAGE-001 — SUBREAD_FEATURECOUNTS</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L2772–2830  
**Auto-fixable:** No

**Description:**  
Process 'SUBREAD_FEATURECOUNTS' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
/featureCounts, //g
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>176. RESOURCE-001 — SUBREAD_FEATURECOUNTS</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L2772–2830  
**Auto-fixable:** No

**Description:**  
Process 'SUBREAD_FEATURECOUNTS' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>177. RESOURCE-002 — SUBREAD_FEATURECOUNTS</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L2772–2830  
**Auto-fixable:** No

**Description:**  
Process 'SUBREAD_FEATURECOUNTS' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>178. CONTAINER-001 — TRIMGALORE</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L2834–2929  
**Auto-fixable:** Yes

**Description:**  
Process 'TRIMGALORE' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟠 <strong>179. STORAGE-001 — TRIMGALORE</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L2834–2929  
**Auto-fixable:** No

**Description:**  
Process 'TRIMGALORE' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
//, //, //github.com/FelixKrueger/TrimGalore/blob/master/Changelog.md ... (9 more)
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>180. RESOURCE-001 — TRIMGALORE</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L2834–2929  
**Auto-fixable:** No

**Description:**  
Process 'TRIMGALORE' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>181. RESOURCE-002 — TRIMGALORE</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L2834–2929  
**Auto-fixable:** No

**Description:**  
Process 'TRIMGALORE' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>182. CONTAINER-001 — UCSC_BEDGRAPHTOBIGWIG</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L2933–2981  
**Auto-fixable:** Yes

**Description:**  
Process 'UCSC_BEDGRAPHTOBIGWIG' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟠 <strong>183. STORAGE-001 — UCSC_BEDGRAPHTOBIGWIG</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L2933–2981  
**Auto-fixable:** No

**Description:**  
Process 'UCSC_BEDGRAPHTOBIGWIG' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
//
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>184. RESOURCE-001 — UCSC_BEDGRAPHTOBIGWIG</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L2933–2981  
**Auto-fixable:** No

**Description:**  
Process 'UCSC_BEDGRAPHTOBIGWIG' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>185. RESOURCE-002 — UCSC_BEDGRAPHTOBIGWIG</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L2933–2981  
**Auto-fixable:** No

**Description:**  
Process 'UCSC_BEDGRAPHTOBIGWIG' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>186. CONTAINER-001 — UMITOOLS_EXTRACT</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L2985–3058  
**Auto-fixable:** Yes

**Description:**  
Process 'UMITOOLS_EXTRACT' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟠 <strong>187. STORAGE-001 — UMITOOLS_EXTRACT</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L2985–3058  
**Auto-fixable:** No

**Description:**  
Process 'UMITOOLS_EXTRACT' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
/version, /., // ... (3 more)
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>188. RESOURCE-001 — UMITOOLS_EXTRACT</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L2985–3058  
**Auto-fixable:** No

**Description:**  
Process 'UMITOOLS_EXTRACT' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>189. RESOURCE-002 — UMITOOLS_EXTRACT</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L2985–3058  
**Auto-fixable:** No

**Description:**  
Process 'UMITOOLS_EXTRACT' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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

<details><summary>🔴 <strong>190. CONTAINER-001 — UNTAR</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L3062–3145  
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

<details><summary>🟠 <strong>191. STORAGE-001 — UNTAR</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L3062–3145  
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

<details><summary>🟡 <strong>192. RESOURCE-001 — UNTAR</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L3062–3145  
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

<details><summary>🟡 <strong>193. RESOURCE-002 — UNTAR</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L3062–3145  
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

<details><summary>🔴 <strong>194. CONTAINER-001 — UNTARFILES</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L3149–3200  
**Auto-fixable:** Yes

**Description:**  
Process 'UNTARFILES' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟠 <strong>195. STORAGE-001 — UNTARFILES</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L3149–3200  
**Auto-fixable:** No

**Description:**  
Process 'UNTARFILES' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
//, //
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>196. RESOURCE-001 — UNTARFILES</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L3149–3200  
**Auto-fixable:** No

**Description:**  
Process 'UNTARFILES' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

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

<details><summary>🟡 <strong>197. RESOURCE-002 — UNTARFILES</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L3149–3200  
**Auto-fixable:** No

**Description:**  
Process 'UNTARFILES' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

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