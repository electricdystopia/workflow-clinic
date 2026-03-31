<!-- WORKFLOW CLINIC ISSUE DRAFT -->
<!-- Title: [Workflow Clinic] 208 cloud-readiness gaps across 55 processes (score: 0%) -->

## 🏥 Workflow Clinic — Automated Cloud-Readiness Report

> **This issue was drafted automatically by [Workflow Clinic](https://github.com/electricdystopia/workflow-clinic), a GA4GH Cloud Work Stream tool for detecting and fixing cloud-readiness gaps in bioinformatics workflows.**
>
> Workflow: `main.nf`  
> Generated: 2026-03-31 19:27 UTC  
> Schema: `0.1.0`

### 🔴 Cloud Readiness Score: **0.00 / 1.00**

### Summary

| Severity | Count | Description |
|---|---|---|
| 🔴 **Critical** | 55 | Portability blockers — workflow cannot run on cloud WES |
| 🟠 **Major** | 43 | Significant gaps affecting reproducibility or correctness |
| 🟡 **Minor** | 110 | Resource hints missing — affects cost and scheduling efficiency |
| **Total** | **208** | |
| Auto-fixable | 55 | Can be fixed automatically with `workflow-clinic doctor` |

> 💡 **55 gap(s) can be fixed automatically.** Run `workflow-clinic doctor <path> --gap CONTAINER-001` to generate a patch and open a PR.

### Gaps

| # | Gap ID | Severity | Process | Category | Lines | Auto-fix |
|---|---|---|---|---|---|---|
| 1 | `CONTAINER-001` | 🔴 CRITICAL | `KRAKEN2_STANDARD_REPORT` | containerization | L97–127 | ✅ |
| 2 | `STORAGE-001` | 🟠 MAJOR | `KRAKEN2_STANDARD_REPORT` | storage | L97–127 | — |
| 3 | `RESOURCE-001` | 🟡 MINOR | `KRAKEN2_STANDARD_REPORT` | resource_hints | L97–127 | — |
| 4 | `RESOURCE-002` | 🟡 MINOR | `KRAKEN2_STANDARD_REPORT` | resource_hints | L97–127 | — |
| 5 | `CONTAINER-001` | 🔴 CRITICAL | `KRONA_CLEANUP` | containerization | L131–170 | ✅ |
| 6 | `STORAGE-001` | 🟠 MAJOR | `KRONA_CLEANUP` | storage | L131–170 | — |
| 7 | `RESOURCE-001` | 🟡 MINOR | `KRONA_CLEANUP` | resource_hints | L131–170 | — |
| 8 | `RESOURCE-002` | 🟡 MINOR | `KRONA_CLEANUP` | resource_hints | L131–170 | — |
| 9 | `CONTAINER-001` | 🔴 CRITICAL | `ADAPTERREMOVAL` | containerization | L174–292 | ✅ |
| 10 | `STORAGE-001` | 🟠 MAJOR | `ADAPTERREMOVAL` | storage | L174–292 | — |
| 11 | `RESOURCE-001` | 🟡 MINOR | `ADAPTERREMOVAL` | resource_hints | L174–292 | — |
| 12 | `RESOURCE-002` | 🟡 MINOR | `ADAPTERREMOVAL` | resource_hints | L174–292 | — |
| 13 | `CONTAINER-001` | 🔴 CRITICAL | `BBMAP_BBDUK` | containerization | L296–352 | ✅ |
| 14 | `RESOURCE-001` | 🟡 MINOR | `BBMAP_BBDUK` | resource_hints | L296–352 | — |
| 15 | `RESOURCE-002` | 🟡 MINOR | `BBMAP_BBDUK` | resource_hints | L296–352 | — |
| 16 | `CONTAINER-001` | 🔴 CRITICAL | `BOWTIE2_ALIGN` | containerization | L356–471 | ✅ |
| 17 | `STORAGE-001` | 🟠 MAJOR | `BOWTIE2_ALIGN` | storage | L356–471 | — |
| 18 | `RESOURCE-001` | 🟡 MINOR | `BOWTIE2_ALIGN` | resource_hints | L356–471 | — |
| 19 | `RESOURCE-002` | 🟡 MINOR | `BOWTIE2_ALIGN` | resource_hints | L356–471 | — |
| 20 | `CONTAINER-001` | 🔴 CRITICAL | `BOWTIE2_BUILD` | containerization | L475–516 | ✅ |
| 21 | `STORAGE-001` | 🟠 MAJOR | `BOWTIE2_BUILD` | storage | L475–516 | — |
| 22 | `RESOURCE-001` | 🟡 MINOR | `BOWTIE2_BUILD` | resource_hints | L475–516 | — |
| 23 | `RESOURCE-002` | 🟡 MINOR | `BOWTIE2_BUILD` | resource_hints | L475–516 | — |
| 24 | `CONTAINER-001` | 🔴 CRITICAL | `BRACKEN_BRACKEN` | containerization | L520–574 | ✅ |
| 25 | `RESOURCE-001` | 🟡 MINOR | `BRACKEN_BRACKEN` | resource_hints | L520–574 | — |
| 26 | `RESOURCE-002` | 🟡 MINOR | `BRACKEN_BRACKEN` | resource_hints | L520–574 | — |
| 27 | `CONTAINER-001` | 🔴 CRITICAL | `BRACKEN_COMBINEBRACKENOUTPUTS` | containerization | L578–629 | ✅ |
| 28 | `STORAGE-001` | 🟠 MAJOR | `BRACKEN_COMBINEBRACKENOUTPUTS` | storage | L578–629 | — |
| 29 | `RESOURCE-001` | 🟡 MINOR | `BRACKEN_COMBINEBRACKENOUTPUTS` | resource_hints | L578–629 | — |
| 30 | `RESOURCE-002` | 🟡 MINOR | `BRACKEN_COMBINEBRACKENOUTPUTS` | resource_hints | L578–629 | — |
| 31 | `CONTAINER-001` | 🔴 CRITICAL | `CAT_FASTQ` | containerization | L633–720 | ✅ |
| 32 | `STORAGE-001` | 🟠 MAJOR | `CAT_FASTQ` | storage | L633–720 | — |
| 33 | `RESOURCE-001` | 🟡 MINOR | `CAT_FASTQ` | resource_hints | L633–720 | — |
| 34 | `RESOURCE-002` | 🟡 MINOR | `CAT_FASTQ` | resource_hints | L633–720 | — |
| 35 | `CONTAINER-001` | 🔴 CRITICAL | `CENTRIFUGE_CENTRIFUGE` | containerization | L724–816 | ✅ |
| 36 | `STORAGE-001` | 🟠 MAJOR | `CENTRIFUGE_CENTRIFUGE` | storage | L724–816 | — |
| 37 | `RESOURCE-001` | 🟡 MINOR | `CENTRIFUGE_CENTRIFUGE` | resource_hints | L724–816 | — |
| 38 | `RESOURCE-002` | 🟡 MINOR | `CENTRIFUGE_CENTRIFUGE` | resource_hints | L724–816 | — |
| 39 | `CONTAINER-001` | 🔴 CRITICAL | `CENTRIFUGE_KREPORT` | containerization | L820–867 | ✅ |
| 40 | `STORAGE-001` | 🟠 MAJOR | `CENTRIFUGE_KREPORT` | storage | L820–867 | — |
| 41 | `RESOURCE-001` | 🟡 MINOR | `CENTRIFUGE_KREPORT` | resource_hints | L820–867 | — |
| 42 | `RESOURCE-002` | 🟡 MINOR | `CENTRIFUGE_KREPORT` | resource_hints | L820–867 | — |
| 43 | `CONTAINER-001` | 🔴 CRITICAL | `DIAMOND_BLASTX` | containerization | L871–983 | ✅ |
| 44 | `STORAGE-001` | 🟠 MAJOR | `DIAMOND_BLASTX` | storage | L871–983 | — |
| 45 | `RESOURCE-001` | 🟡 MINOR | `DIAMOND_BLASTX` | resource_hints | L871–983 | — |
| 46 | `RESOURCE-002` | 🟡 MINOR | `DIAMOND_BLASTX` | resource_hints | L871–983 | — |
| 47 | `CONTAINER-001` | 🔴 CRITICAL | `FALCO` | containerization | L987–1043 | ✅ |
| 48 | `STORAGE-001` | 🟠 MAJOR | `FALCO` | storage | L987–1043 | — |
| 49 | `RESOURCE-001` | 🟡 MINOR | `FALCO` | resource_hints | L987–1043 | — |
| 50 | `RESOURCE-002` | 🟡 MINOR | `FALCO` | resource_hints | L987–1043 | — |
| 51 | `CONTAINER-001` | 🔴 CRITICAL | `FASTP` | containerization | L1047–1171 | ✅ |
| 52 | `STORAGE-001` | 🟠 MAJOR | `FASTP` | storage | L1047–1171 | — |
| 53 | `RESOURCE-001` | 🟡 MINOR | `FASTP` | resource_hints | L1047–1171 | — |
| 54 | `RESOURCE-002` | 🟡 MINOR | `FASTP` | resource_hints | L1047–1171 | — |
| 55 | `CONTAINER-001` | 🔴 CRITICAL | `FASTQC` | containerization | L1175–1238 | ✅ |
| 56 | `STORAGE-001` | 🟠 MAJOR | `FASTQC` | storage | L1175–1238 | — |
| 57 | `RESOURCE-001` | 🟡 MINOR | `FASTQC` | resource_hints | L1175–1238 | — |
| 58 | `RESOURCE-002` | 🟡 MINOR | `FASTQC` | resource_hints | L1175–1238 | — |
| 59 | `CONTAINER-001` | 🔴 CRITICAL | `FILTLONG` | containerization | L1242–1280 | ✅ |
| 60 | `STORAGE-001` | 🟠 MAJOR | `FILTLONG` | storage | L1242–1280 | — |
| 61 | `RESOURCE-001` | 🟡 MINOR | `FILTLONG` | resource_hints | L1242–1280 | — |
| 62 | `RESOURCE-002` | 🟡 MINOR | `FILTLONG` | resource_hints | L1242–1280 | — |
| 63 | `CONTAINER-001` | 🔴 CRITICAL | `GANON_CLASSIFY` | containerization | L1284–1347 | ✅ |
| 64 | `STORAGE-001` | 🟠 MAJOR | `GANON_CLASSIFY` | storage | L1284–1347 | — |
| 65 | `RESOURCE-001` | 🟡 MINOR | `GANON_CLASSIFY` | resource_hints | L1284–1347 | — |
| 66 | `RESOURCE-002` | 🟡 MINOR | `GANON_CLASSIFY` | resource_hints | L1284–1347 | — |
| 67 | `CONTAINER-001` | 🔴 CRITICAL | `GANON_REPORT` | containerization | L1351–1402 | ✅ |
| 68 | `STORAGE-001` | 🟠 MAJOR | `GANON_REPORT` | storage | L1351–1402 | — |
| 69 | `RESOURCE-001` | 🟡 MINOR | `GANON_REPORT` | resource_hints | L1351–1402 | — |
| 70 | `RESOURCE-002` | 🟡 MINOR | `GANON_REPORT` | resource_hints | L1351–1402 | — |
| 71 | `CONTAINER-001` | 🔴 CRITICAL | `GANON_TABLE` | containerization | L1406–1452 | ✅ |
| 72 | `STORAGE-001` | 🟠 MAJOR | `GANON_TABLE` | storage | L1406–1452 | — |
| 73 | `RESOURCE-001` | 🟡 MINOR | `GANON_TABLE` | resource_hints | L1406–1452 | — |
| 74 | `RESOURCE-002` | 🟡 MINOR | `GANON_TABLE` | resource_hints | L1406–1452 | — |
| 75 | `CONTAINER-001` | 🔴 CRITICAL | `GUNZIP` | containerization | L1456–1510 | ✅ |
| 76 | `STORAGE-001` | 🟠 MAJOR | `GUNZIP` | storage | L1456–1510 | — |
| 77 | `RESOURCE-001` | 🟡 MINOR | `GUNZIP` | resource_hints | L1456–1510 | — |
| 78 | `RESOURCE-002` | 🟡 MINOR | `GUNZIP` | resource_hints | L1456–1510 | — |
| 79 | `CONTAINER-001` | 🔴 CRITICAL | `KAIJU_KAIJU` | containerization | L1514–1568 | ✅ |
| 80 | `STORAGE-001` | 🟠 MAJOR | `KAIJU_KAIJU` | storage | L1514–1568 | — |
| 81 | `RESOURCE-001` | 🟡 MINOR | `KAIJU_KAIJU` | resource_hints | L1514–1568 | — |
| 82 | `RESOURCE-002` | 🟡 MINOR | `KAIJU_KAIJU` | resource_hints | L1514–1568 | — |
| 83 | `CONTAINER-001` | 🔴 CRITICAL | `KAIJU_KAIJU2KRONA` | containerization | L1572–1622 | ✅ |
| 84 | `STORAGE-001` | 🟠 MAJOR | `KAIJU_KAIJU2KRONA` | storage | L1572–1622 | — |
| 85 | `RESOURCE-001` | 🟡 MINOR | `KAIJU_KAIJU2KRONA` | resource_hints | L1572–1622 | — |
| 86 | `RESOURCE-002` | 🟡 MINOR | `KAIJU_KAIJU2KRONA` | resource_hints | L1572–1622 | — |
| 87 | `CONTAINER-001` | 🔴 CRITICAL | `KAIJU_KAIJU2TABLE` | containerization | L1626–1677 | ✅ |
| 88 | `STORAGE-001` | 🟠 MAJOR | `KAIJU_KAIJU2TABLE` | storage | L1626–1677 | — |
| 89 | `RESOURCE-001` | 🟡 MINOR | `KAIJU_KAIJU2TABLE` | resource_hints | L1626–1677 | — |
| 90 | `RESOURCE-002` | 🟡 MINOR | `KAIJU_KAIJU2TABLE` | resource_hints | L1626–1677 | — |
| 91 | `CONTAINER-001` | 🔴 CRITICAL | `KMCP_PROFILE` | containerization | L1681–1732 | ✅ |
| 92 | `STORAGE-001` | 🟠 MAJOR | `KMCP_PROFILE` | storage | L1681–1732 | — |
| 93 | `RESOURCE-001` | 🟡 MINOR | `KMCP_PROFILE` | resource_hints | L1681–1732 | — |
| 94 | `RESOURCE-002` | 🟡 MINOR | `KMCP_PROFILE` | resource_hints | L1681–1732 | — |
| 95 | `CONTAINER-001` | 🔴 CRITICAL | `KMCP_SEARCH` | containerization | L1736–1786 | ✅ |
| 96 | `STORAGE-001` | 🟠 MAJOR | `KMCP_SEARCH` | storage | L1736–1786 | — |
| 97 | `RESOURCE-001` | 🟡 MINOR | `KMCP_SEARCH` | resource_hints | L1736–1786 | — |
| 98 | `RESOURCE-002` | 🟡 MINOR | `KMCP_SEARCH` | resource_hints | L1736–1786 | — |
| 99 | `CONTAINER-001` | 🔴 CRITICAL | `KRAKEN2_KRAKEN2` | containerization | L1790–1874 | ✅ |
| 100 | `STORAGE-001` | 🟠 MAJOR | `KRAKEN2_KRAKEN2` | storage | L1790–1874 | — |
| 101 | `RESOURCE-001` | 🟡 MINOR | `KRAKEN2_KRAKEN2` | resource_hints | L1790–1874 | — |
| 102 | `RESOURCE-002` | 🟡 MINOR | `KRAKEN2_KRAKEN2` | resource_hints | L1790–1874 | — |
| 103 | `CONTAINER-001` | 🔴 CRITICAL | `KRAKENTOOLS_COMBINEKREPORTS` | containerization | L1878–1924 | ✅ |
| 104 | `STORAGE-001` | 🟠 MAJOR | `KRAKENTOOLS_COMBINEKREPORTS` | storage | L1878–1924 | — |
| 105 | `RESOURCE-001` | 🟡 MINOR | `KRAKENTOOLS_COMBINEKREPORTS` | resource_hints | L1878–1924 | — |
| 106 | `RESOURCE-002` | 🟡 MINOR | `KRAKENTOOLS_COMBINEKREPORTS` | resource_hints | L1878–1924 | — |
| 107 | `CONTAINER-001` | 🔴 CRITICAL | `KRAKENTOOLS_KREPORT2KRONA` | containerization | L1928–1976 | ✅ |
| 108 | `STORAGE-001` | 🟠 MAJOR | `KRAKENTOOLS_KREPORT2KRONA` | storage | L1928–1976 | — |
| 109 | `RESOURCE-001` | 🟡 MINOR | `KRAKENTOOLS_KREPORT2KRONA` | resource_hints | L1928–1976 | — |
| 110 | `RESOURCE-002` | 🟡 MINOR | `KRAKENTOOLS_KREPORT2KRONA` | resource_hints | L1928–1976 | — |
| 111 | `CONTAINER-001` | 🔴 CRITICAL | `KRAKENUNIQ_PRELOADEDKRAKENUNIQ` | containerization | L1980–2206 | ✅ |
| 112 | `STORAGE-001` | 🟠 MAJOR | `KRAKENUNIQ_PRELOADEDKRAKENUNIQ` | storage | L1980–2206 | — |
| 113 | `RESOURCE-001` | 🟡 MINOR | `KRAKENUNIQ_PRELOADEDKRAKENUNIQ` | resource_hints | L1980–2206 | — |
| 114 | `RESOURCE-002` | 🟡 MINOR | `KRAKENUNIQ_PRELOADEDKRAKENUNIQ` | resource_hints | L1980–2206 | — |
| 115 | `CONTAINER-001` | 🔴 CRITICAL | `KRONA_KTIMPORTTAXONOMY` | containerization | L2210–2260 | ✅ |
| 116 | `RESOURCE-001` | 🟡 MINOR | `KRONA_KTIMPORTTAXONOMY` | resource_hints | L2210–2260 | — |
| 117 | `RESOURCE-002` | 🟡 MINOR | `KRONA_KTIMPORTTAXONOMY` | resource_hints | L2210–2260 | — |
| 118 | `CONTAINER-001` | 🔴 CRITICAL | `KRONA_KTIMPORTTEXT` | containerization | L2264–2308 | ✅ |
| 119 | `STORAGE-001` | 🟠 MAJOR | `KRONA_KTIMPORTTEXT` | storage | L2264–2308 | — |
| 120 | `RESOURCE-001` | 🟡 MINOR | `KRONA_KTIMPORTTEXT` | resource_hints | L2264–2308 | — |
| 121 | `RESOURCE-002` | 🟡 MINOR | `KRONA_KTIMPORTTEXT` | resource_hints | L2264–2308 | — |
| 122 | `CONTAINER-001` | 🔴 CRITICAL | `MALT_RUN` | containerization | L2312–2365 | ✅ |
| 123 | `RESOURCE-001` | 🟡 MINOR | `MALT_RUN` | resource_hints | L2312–2365 | — |
| 124 | `RESOURCE-002` | 🟡 MINOR | `MALT_RUN` | resource_hints | L2312–2365 | — |
| 125 | `CONTAINER-001` | 🔴 CRITICAL | `MEGAN_RMA2INFO` | containerization | L2369–2419 | ✅ |
| 126 | `STORAGE-001` | 🟠 MAJOR | `MEGAN_RMA2INFO` | storage | L2369–2419 | — |
| 127 | `RESOURCE-001` | 🟡 MINOR | `MEGAN_RMA2INFO` | resource_hints | L2369–2419 | — |
| 128 | `RESOURCE-002` | 🟡 MINOR | `MEGAN_RMA2INFO` | resource_hints | L2369–2419 | — |
| 129 | `CONTAINER-001` | 🔴 CRITICAL | `METAPHLAN_MERGEMETAPHLANTABLES` | containerization | L2423–2467 | ✅ |
| 130 | `RESOURCE-001` | 🟡 MINOR | `METAPHLAN_MERGEMETAPHLANTABLES` | resource_hints | L2423–2467 | — |
| 131 | `RESOURCE-002` | 🟡 MINOR | `METAPHLAN_MERGEMETAPHLANTABLES` | resource_hints | L2423–2467 | — |
| 132 | `CONTAINER-001` | 🔴 CRITICAL | `METAPHLAN_METAPHLAN` | containerization | L2471–2541 | ✅ |
| 133 | `STORAGE-001` | 🟠 MAJOR | `METAPHLAN_METAPHLAN` | storage | L2471–2541 | — |
| 134 | `RESOURCE-001` | 🟡 MINOR | `METAPHLAN_METAPHLAN` | resource_hints | L2471–2541 | — |
| 135 | `RESOURCE-002` | 🟡 MINOR | `METAPHLAN_METAPHLAN` | resource_hints | L2471–2541 | — |
| 136 | `CONTAINER-001` | 🔴 CRITICAL | `MINIMAP2_ALIGN` | containerization | L2545–2622 | ✅ |
| 137 | `STORAGE-001` | 🟠 MAJOR | `MINIMAP2_ALIGN` | storage | L2545–2622 | — |
| 138 | `RESOURCE-001` | 🟡 MINOR | `MINIMAP2_ALIGN` | resource_hints | L2545–2622 | — |
| 139 | `RESOURCE-002` | 🟡 MINOR | `MINIMAP2_ALIGN` | resource_hints | L2545–2622 | — |
| 140 | `CONTAINER-001` | 🔴 CRITICAL | `MINIMAP2_INDEX` | containerization | L2626–2669 | ✅ |
| 141 | `RESOURCE-001` | 🟡 MINOR | `MINIMAP2_INDEX` | resource_hints | L2626–2669 | — |
| 142 | `RESOURCE-002` | 🟡 MINOR | `MINIMAP2_INDEX` | resource_hints | L2626–2669 | — |
| 143 | `CONTAINER-001` | 🔴 CRITICAL | `MOTUS_MERGE` | containerization | L2673–2735 | ✅ |
| 144 | `STORAGE-001` | 🟠 MAJOR | `MOTUS_MERGE` | storage | L2673–2735 | — |
| 145 | `RESOURCE-001` | 🟡 MINOR | `MOTUS_MERGE` | resource_hints | L2673–2735 | — |
| 146 | `RESOURCE-002` | 🟡 MINOR | `MOTUS_MERGE` | resource_hints | L2673–2735 | — |
| 147 | `CONTAINER-001` | 🔴 CRITICAL | `MOTUS_PROFILE` | containerization | L2739–2818 | ✅ |
| 148 | `STORAGE-001` | 🟠 MAJOR | `MOTUS_PROFILE` | storage | L2739–2818 | — |
| 149 | `RESOURCE-001` | 🟡 MINOR | `MOTUS_PROFILE` | resource_hints | L2739–2818 | — |
| 150 | `RESOURCE-002` | 🟡 MINOR | `MOTUS_PROFILE` | resource_hints | L2739–2818 | — |
| 151 | `CONTAINER-001` | 🔴 CRITICAL | `MULTIQC` | containerization | L2822–2884 | ✅ |
| 152 | `STORAGE-001` | 🟠 MAJOR | `MULTIQC` | storage | L2822–2884 | — |
| 153 | `RESOURCE-001` | 🟡 MINOR | `MULTIQC` | resource_hints | L2822–2884 | — |
| 154 | `RESOURCE-002` | 🟡 MINOR | `MULTIQC` | resource_hints | L2822–2884 | — |
| 155 | `CONTAINER-001` | 🔴 CRITICAL | `NANOQ` | containerization | L2888–2936 | ✅ |
| 156 | `STORAGE-001` | 🟠 MAJOR | `NANOQ` | storage | L2888–2936 | — |
| 157 | `RESOURCE-001` | 🟡 MINOR | `NANOQ` | resource_hints | L2888–2936 | — |
| 158 | `RESOURCE-002` | 🟡 MINOR | `NANOQ` | resource_hints | L2888–2936 | — |
| 159 | `CONTAINER-001` | 🔴 CRITICAL | `NONPAREIL_CURVE` | containerization | L2940–2990 | ✅ |
| 160 | `STORAGE-001` | 🟠 MAJOR | `NONPAREIL_CURVE` | storage | L2940–2990 | — |
| 161 | `RESOURCE-001` | 🟡 MINOR | `NONPAREIL_CURVE` | resource_hints | L2940–2990 | — |
| 162 | `RESOURCE-002` | 🟡 MINOR | `NONPAREIL_CURVE` | resource_hints | L2940–2990 | — |
| 163 | `CONTAINER-001` | 🔴 CRITICAL | `NONPAREIL_NONPAREIL` | containerization | L2994–3052 | ✅ |
| 164 | `STORAGE-001` | 🟠 MAJOR | `NONPAREIL_NONPAREIL` | storage | L2994–3052 | — |
| 165 | `RESOURCE-001` | 🟡 MINOR | `NONPAREIL_NONPAREIL` | resource_hints | L2994–3052 | — |
| 166 | `RESOURCE-002` | 🟡 MINOR | `NONPAREIL_NONPAREIL` | resource_hints | L2994–3052 | — |
| 167 | `CONTAINER-001` | 🔴 CRITICAL | `NONPAREIL_NONPAREILCURVESR` | containerization | L3056–3112 | ✅ |
| 168 | `STORAGE-001` | 🟠 MAJOR | `NONPAREIL_NONPAREILCURVESR` | storage | L3056–3112 | — |
| 169 | `RESOURCE-001` | 🟡 MINOR | `NONPAREIL_NONPAREILCURVESR` | resource_hints | L3056–3112 | — |
| 170 | `RESOURCE-002` | 🟡 MINOR | `NONPAREIL_NONPAREILCURVESR` | resource_hints | L3056–3112 | — |
| 171 | `CONTAINER-001` | 🔴 CRITICAL | `NONPAREIL_SET` | containerization | L3116–3166 | ✅ |
| 172 | `STORAGE-001` | 🟠 MAJOR | `NONPAREIL_SET` | storage | L3116–3166 | — |
| 173 | `RESOURCE-001` | 🟡 MINOR | `NONPAREIL_SET` | resource_hints | L3116–3166 | — |
| 174 | `RESOURCE-002` | 🟡 MINOR | `NONPAREIL_SET` | resource_hints | L3116–3166 | — |
| 175 | `CONTAINER-001` | 🔴 CRITICAL | `PORECHOP_ABI` | containerization | L3170–3219 | ✅ |
| 176 | `RESOURCE-001` | 🟡 MINOR | `PORECHOP_ABI` | resource_hints | L3170–3219 | — |
| 177 | `RESOURCE-002` | 🟡 MINOR | `PORECHOP_ABI` | resource_hints | L3170–3219 | — |
| 178 | `CONTAINER-001` | 🔴 CRITICAL | `PORECHOP_PORECHOP` | containerization | L3223–3273 | ✅ |
| 179 | `RESOURCE-001` | 🟡 MINOR | `PORECHOP_PORECHOP` | resource_hints | L3223–3273 | — |
| 180 | `RESOURCE-002` | 🟡 MINOR | `PORECHOP_PORECHOP` | resource_hints | L3223–3273 | — |
| 181 | `CONTAINER-001` | 🔴 CRITICAL | `PRINSEQPLUSPLUS` | containerization | L3277–3337 | ✅ |
| 182 | `RESOURCE-001` | 🟡 MINOR | `PRINSEQPLUSPLUS` | resource_hints | L3277–3337 | — |
| 183 | `RESOURCE-002` | 🟡 MINOR | `PRINSEQPLUSPLUS` | resource_hints | L3277–3337 | — |
| 184 | `CONTAINER-001` | 🔴 CRITICAL | `SAMTOOLS_FASTQ` | containerization | L3341–3400 | ✅ |
| 185 | `STORAGE-001` | 🟠 MAJOR | `SAMTOOLS_FASTQ` | storage | L3341–3400 | — |
| 186 | `RESOURCE-001` | 🟡 MINOR | `SAMTOOLS_FASTQ` | resource_hints | L3341–3400 | — |
| 187 | `RESOURCE-002` | 🟡 MINOR | `SAMTOOLS_FASTQ` | resource_hints | L3341–3400 | — |
| 188 | `CONTAINER-001` | 🔴 CRITICAL | `SAMTOOLS_INDEX` | containerization | L3404–3452 | ✅ |
| 189 | `STORAGE-001` | 🟠 MAJOR | `SAMTOOLS_INDEX` | storage | L3404–3452 | — |
| 190 | `RESOURCE-001` | 🟡 MINOR | `SAMTOOLS_INDEX` | resource_hints | L3404–3452 | — |
| 191 | `RESOURCE-002` | 🟡 MINOR | `SAMTOOLS_INDEX` | resource_hints | L3404–3452 | — |
| 192 | `CONTAINER-001` | 🔴 CRITICAL | `SAMTOOLS_STATS` | containerization | L3456–3493 | ✅ |
| 193 | `RESOURCE-001` | 🟡 MINOR | `SAMTOOLS_STATS` | resource_hints | L3456–3493 | — |
| 194 | `RESOURCE-002` | 🟡 MINOR | `SAMTOOLS_STATS` | resource_hints | L3456–3493 | — |
| 195 | `CONTAINER-001` | 🔴 CRITICAL | `SAMTOOLS_VIEW` | containerization | L3497–3590 | ✅ |
| 196 | `STORAGE-001` | 🟠 MAJOR | `SAMTOOLS_VIEW` | storage | L3497–3590 | — |
| 197 | `RESOURCE-001` | 🟡 MINOR | `SAMTOOLS_VIEW` | resource_hints | L3497–3590 | — |
| 198 | `RESOURCE-002` | 🟡 MINOR | `SAMTOOLS_VIEW` | resource_hints | L3497–3590 | — |
| 199 | `CONTAINER-001` | 🔴 CRITICAL | `TAXPASTA_MERGE` | containerization | L3594–3651 | ✅ |
| 200 | `RESOURCE-001` | 🟡 MINOR | `TAXPASTA_MERGE` | resource_hints | L3594–3651 | — |
| 201 | `RESOURCE-002` | 🟡 MINOR | `TAXPASTA_MERGE` | resource_hints | L3594–3651 | — |
| 202 | `CONTAINER-001` | 🔴 CRITICAL | `TAXPASTA_STANDARDISE` | containerization | L3655–3707 | ✅ |
| 203 | `RESOURCE-001` | 🟡 MINOR | `TAXPASTA_STANDARDISE` | resource_hints | L3655–3707 | — |
| 204 | `RESOURCE-002` | 🟡 MINOR | `TAXPASTA_STANDARDISE` | resource_hints | L3655–3707 | — |
| 205 | `CONTAINER-001` | 🔴 CRITICAL | `UNTAR` | containerization | L3711–3794 | ✅ |
| 206 | `STORAGE-001` | 🟠 MAJOR | `UNTAR` | storage | L3711–3794 | — |
| 207 | `RESOURCE-001` | 🟡 MINOR | `UNTAR` | resource_hints | L3711–3794 | — |
| 208 | `RESOURCE-002` | 🟡 MINOR | `UNTAR` | resource_hints | L3711–3794 | — |

### Detail

<details><summary>🔴 <strong>1. CONTAINER-001 — KRAKEN2_STANDARD_REPORT</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L97–127  
**Auto-fixable:** Yes

**Description:**  
Process 'KRAKEN2_STANDARD_REPORT' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟠 <strong>2. STORAGE-001 — KRAKEN2_STANDARD_REPORT</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L97–127  
**Auto-fixable:** No

**Description:**  
Process 'KRAKEN2_STANDARD_REPORT' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
//, //
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>3. RESOURCE-001 — KRAKEN2_STANDARD_REPORT</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L97–127  
**Auto-fixable:** No

**Description:**  
Process 'KRAKEN2_STANDARD_REPORT' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

**Recommendation:**
```
Add a cpus directive appropriate for the tool's parallelism:
    cpus 4

Reference the allocation in the script block so the tool actually uses the provisioned cores:
    bwa mem -t ${task.cpus} ...

For workflows that need to scale, consider a dynamic expression:
    cpus { reads.size() > 5.GB ? 8 : 4 }
```

</details>

<details><summary>🟡 <strong>4. RESOURCE-002 — KRAKEN2_STANDARD_REPORT</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L97–127  
**Auto-fixable:** No

**Description:**  
Process 'KRAKEN2_STANDARD_REPORT' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

**Recommendation:**
```
Add a memory directive sized for the tool's peak usage:
    memory '8 GB'

For resilient pipelines, combine with an error strategy that increases memory on retry:
    errorStrategy 'retry'
    maxRetries 2
    memory { (8.GB * task.attempt).clamp(null, 32.GB) }
```

</details>

<details><summary>🔴 <strong>5. CONTAINER-001 — KRONA_CLEANUP</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L131–170  
**Auto-fixable:** Yes

**Description:**  
Process 'KRONA_CLEANUP' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟠 <strong>6. STORAGE-001 — KRONA_CLEANUP</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L131–170  
**Auto-fixable:** No

**Description:**  
Process 'KRONA_CLEANUP' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
//g, /_/, /g ... (2 more)
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>7. RESOURCE-001 — KRONA_CLEANUP</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L131–170  
**Auto-fixable:** No

**Description:**  
Process 'KRONA_CLEANUP' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

**Recommendation:**
```
Add a cpus directive appropriate for the tool's parallelism:
    cpus 4

Reference the allocation in the script block so the tool actually uses the provisioned cores:
    bwa mem -t ${task.cpus} ...

For workflows that need to scale, consider a dynamic expression:
    cpus { reads.size() > 5.GB ? 8 : 4 }
```

</details>

<details><summary>🟡 <strong>8. RESOURCE-002 — KRONA_CLEANUP</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L131–170  
**Auto-fixable:** No

**Description:**  
Process 'KRONA_CLEANUP' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

**Recommendation:**
```
Add a memory directive sized for the tool's peak usage:
    memory '8 GB'

For resilient pipelines, combine with an error strategy that increases memory on retry:
    errorStrategy 'retry'
    maxRetries 2
    memory { (8.GB * task.attempt).clamp(null, 32.GB) }
```

</details>

<details><summary>🔴 <strong>9. CONTAINER-001 — ADAPTERREMOVAL</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L174–292  
**Auto-fixable:** Yes

**Description:**  
Process 'ADAPTERREMOVAL' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟠 <strong>10. STORAGE-001 — ADAPTERREMOVAL</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L174–292  
**Auto-fixable:** No

**Description:**  
Process 'ADAPTERREMOVAL' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
/AdapterRemoval, //g, /AdapterRemoval ... (1 more)
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>11. RESOURCE-001 — ADAPTERREMOVAL</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L174–292  
**Auto-fixable:** No

**Description:**  
Process 'ADAPTERREMOVAL' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

**Recommendation:**
```
Add a cpus directive appropriate for the tool's parallelism:
    cpus 4

Reference the allocation in the script block so the tool actually uses the provisioned cores:
    bwa mem -t ${task.cpus} ...

For workflows that need to scale, consider a dynamic expression:
    cpus { reads.size() > 5.GB ? 8 : 4 }
```

</details>

<details><summary>🟡 <strong>12. RESOURCE-002 — ADAPTERREMOVAL</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L174–292  
**Auto-fixable:** No

**Description:**  
Process 'ADAPTERREMOVAL' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

**Recommendation:**
```
Add a memory directive sized for the tool's peak usage:
    memory '8 GB'

For resilient pipelines, combine with an error strategy that increases memory on retry:
    errorStrategy 'retry'
    maxRetries 2
    memory { (8.GB * task.attempt).clamp(null, 32.GB) }
```

</details>

<details><summary>🔴 <strong>13. CONTAINER-001 — BBMAP_BBDUK</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L296–352  
**Auto-fixable:** Yes

**Description:**  
Process 'BBMAP_BBDUK' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟡 <strong>14. RESOURCE-001 — BBMAP_BBDUK</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L296–352  
**Auto-fixable:** No

**Description:**  
Process 'BBMAP_BBDUK' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

**Recommendation:**
```
Add a cpus directive appropriate for the tool's parallelism:
    cpus 4

Reference the allocation in the script block so the tool actually uses the provisioned cores:
    bwa mem -t ${task.cpus} ...

For workflows that need to scale, consider a dynamic expression:
    cpus { reads.size() > 5.GB ? 8 : 4 }
```

</details>

<details><summary>🟡 <strong>15. RESOURCE-002 — BBMAP_BBDUK</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L296–352  
**Auto-fixable:** No

**Description:**  
Process 'BBMAP_BBDUK' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

**Recommendation:**
```
Add a memory directive sized for the tool's peak usage:
    memory '8 GB'

For resilient pipelines, combine with an error strategy that increases memory on retry:
    errorStrategy 'retry'
    maxRetries 2
    memory { (8.GB * task.attempt).clamp(null, 32.GB) }
```

</details>

<details><summary>🔴 <strong>16. CONTAINER-001 — BOWTIE2_ALIGN</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L356–471  
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

<details><summary>🟠 <strong>17. STORAGE-001 — BOWTIE2_ALIGN</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L356–471  
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

<details><summary>🟡 <strong>18. RESOURCE-001 — BOWTIE2_ALIGN</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L356–471  
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

<details><summary>🟡 <strong>19. RESOURCE-002 — BOWTIE2_ALIGN</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L356–471  
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

<details><summary>🔴 <strong>20. CONTAINER-001 — BOWTIE2_BUILD</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L475–516  
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

<details><summary>🟠 <strong>21. STORAGE-001 — BOWTIE2_BUILD</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L475–516  
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

<details><summary>🟡 <strong>22. RESOURCE-001 — BOWTIE2_BUILD</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L475–516  
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

<details><summary>🟡 <strong>23. RESOURCE-002 — BOWTIE2_BUILD</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L475–516  
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

<details><summary>🔴 <strong>24. CONTAINER-001 — BRACKEN_BRACKEN</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L520–574  
**Auto-fixable:** Yes

**Description:**  
Process 'BRACKEN_BRACKEN' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟡 <strong>25. RESOURCE-001 — BRACKEN_BRACKEN</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L520–574  
**Auto-fixable:** No

**Description:**  
Process 'BRACKEN_BRACKEN' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

**Recommendation:**
```
Add a cpus directive appropriate for the tool's parallelism:
    cpus 4

Reference the allocation in the script block so the tool actually uses the provisioned cores:
    bwa mem -t ${task.cpus} ...

For workflows that need to scale, consider a dynamic expression:
    cpus { reads.size() > 5.GB ? 8 : 4 }
```

</details>

<details><summary>🟡 <strong>26. RESOURCE-002 — BRACKEN_BRACKEN</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L520–574  
**Auto-fixable:** No

**Description:**  
Process 'BRACKEN_BRACKEN' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

**Recommendation:**
```
Add a memory directive sized for the tool's peak usage:
    memory '8 GB'

For resilient pipelines, combine with an error strategy that increases memory on retry:
    errorStrategy 'retry'
    maxRetries 2
    memory { (8.GB * task.attempt).clamp(null, 32.GB) }
```

</details>

<details><summary>🔴 <strong>27. CONTAINER-001 — BRACKEN_COMBINEBRACKENOUTPUTS</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L578–629  
**Auto-fixable:** Yes

**Description:**  
Process 'BRACKEN_COMBINEBRACKENOUTPUTS' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟠 <strong>28. STORAGE-001 — BRACKEN_COMBINEBRACKENOUTPUTS</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L578–629  
**Auto-fixable:** No

**Description:**  
Process 'BRACKEN_COMBINEBRACKENOUTPUTS' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
//, //
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>29. RESOURCE-001 — BRACKEN_COMBINEBRACKENOUTPUTS</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L578–629  
**Auto-fixable:** No

**Description:**  
Process 'BRACKEN_COMBINEBRACKENOUTPUTS' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

**Recommendation:**
```
Add a cpus directive appropriate for the tool's parallelism:
    cpus 4

Reference the allocation in the script block so the tool actually uses the provisioned cores:
    bwa mem -t ${task.cpus} ...

For workflows that need to scale, consider a dynamic expression:
    cpus { reads.size() > 5.GB ? 8 : 4 }
```

</details>

<details><summary>🟡 <strong>30. RESOURCE-002 — BRACKEN_COMBINEBRACKENOUTPUTS</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L578–629  
**Auto-fixable:** No

**Description:**  
Process 'BRACKEN_COMBINEBRACKENOUTPUTS' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

**Recommendation:**
```
Add a memory directive sized for the tool's peak usage:
    memory '8 GB'

For resilient pipelines, combine with an error strategy that increases memory on retry:
    errorStrategy 'retry'
    maxRetries 2
    memory { (8.GB * task.attempt).clamp(null, 32.GB) }
```

</details>

<details><summary>🔴 <strong>31. CONTAINER-001 — CAT_FASTQ</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L633–720  
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

<details><summary>🟠 <strong>32. STORAGE-001 — CAT_FASTQ</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L633–720  
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

<details><summary>🟡 <strong>33. RESOURCE-001 — CAT_FASTQ</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L633–720  
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

<details><summary>🟡 <strong>34. RESOURCE-002 — CAT_FASTQ</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L633–720  
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

<details><summary>🔴 <strong>35. CONTAINER-001 — CENTRIFUGE_CENTRIFUGE</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L724–816  
**Auto-fixable:** Yes

**Description:**  
Process 'CENTRIFUGE_CENTRIFUGE' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟠 <strong>36. STORAGE-001 — CENTRIFUGE_CENTRIFUGE</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L724–816  
**Auto-fixable:** No

**Description:**  
Process 'CENTRIFUGE_CENTRIFUGE' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
//, /tmp, /tmp ... (3 more)
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>37. RESOURCE-001 — CENTRIFUGE_CENTRIFUGE</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L724–816  
**Auto-fixable:** No

**Description:**  
Process 'CENTRIFUGE_CENTRIFUGE' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

**Recommendation:**
```
Add a cpus directive appropriate for the tool's parallelism:
    cpus 4

Reference the allocation in the script block so the tool actually uses the provisioned cores:
    bwa mem -t ${task.cpus} ...

For workflows that need to scale, consider a dynamic expression:
    cpus { reads.size() > 5.GB ? 8 : 4 }
```

</details>

<details><summary>🟡 <strong>38. RESOURCE-002 — CENTRIFUGE_CENTRIFUGE</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L724–816  
**Auto-fixable:** No

**Description:**  
Process 'CENTRIFUGE_CENTRIFUGE' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

**Recommendation:**
```
Add a memory directive sized for the tool's peak usage:
    memory '8 GB'

For resilient pipelines, combine with an error strategy that increases memory on retry:
    errorStrategy 'retry'
    maxRetries 2
    memory { (8.GB * task.attempt).clamp(null, 32.GB) }
```

</details>

<details><summary>🔴 <strong>39. CONTAINER-001 — CENTRIFUGE_KREPORT</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L820–867  
**Auto-fixable:** Yes

**Description:**  
Process 'CENTRIFUGE_KREPORT' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟠 <strong>40. STORAGE-001 — CENTRIFUGE_KREPORT</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L820–867  
**Auto-fixable:** No

**Description:**  
Process 'CENTRIFUGE_KREPORT' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
//, //
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>41. RESOURCE-001 — CENTRIFUGE_KREPORT</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L820–867  
**Auto-fixable:** No

**Description:**  
Process 'CENTRIFUGE_KREPORT' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

**Recommendation:**
```
Add a cpus directive appropriate for the tool's parallelism:
    cpus 4

Reference the allocation in the script block so the tool actually uses the provisioned cores:
    bwa mem -t ${task.cpus} ...

For workflows that need to scale, consider a dynamic expression:
    cpus { reads.size() > 5.GB ? 8 : 4 }
```

</details>

<details><summary>🟡 <strong>42. RESOURCE-002 — CENTRIFUGE_KREPORT</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L820–867  
**Auto-fixable:** No

**Description:**  
Process 'CENTRIFUGE_KREPORT' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

**Recommendation:**
```
Add a memory directive sized for the tool's peak usage:
    memory '8 GB'

For resilient pipelines, combine with an error strategy that increases memory on retry:
    errorStrategy 'retry'
    maxRetries 2
    memory { (8.GB * task.attempt).clamp(null, 32.GB) }
```

</details>

<details><summary>🔴 <strong>43. CONTAINER-001 — DIAMOND_BLASTX</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L871–983  
**Auto-fixable:** Yes

**Description:**  
Process 'DIAMOND_BLASTX' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟠 <strong>44. STORAGE-001 — DIAMOND_BLASTX</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L871–983  
**Auto-fixable:** No

**Description:**  
Process 'DIAMOND_BLASTX' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
//, //
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>45. RESOURCE-001 — DIAMOND_BLASTX</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L871–983  
**Auto-fixable:** No

**Description:**  
Process 'DIAMOND_BLASTX' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

**Recommendation:**
```
Add a cpus directive appropriate for the tool's parallelism:
    cpus 4

Reference the allocation in the script block so the tool actually uses the provisioned cores:
    bwa mem -t ${task.cpus} ...

For workflows that need to scale, consider a dynamic expression:
    cpus { reads.size() > 5.GB ? 8 : 4 }
```

</details>

<details><summary>🟡 <strong>46. RESOURCE-002 — DIAMOND_BLASTX</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L871–983  
**Auto-fixable:** No

**Description:**  
Process 'DIAMOND_BLASTX' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

**Recommendation:**
```
Add a memory directive sized for the tool's peak usage:
    memory '8 GB'

For resilient pipelines, combine with an error strategy that increases memory on retry:
    errorStrategy 'retry'
    maxRetries 2
    memory { (8.GB * task.attempt).clamp(null, 32.GB) }
```

</details>

<details><summary>🔴 <strong>47. CONTAINER-001 — FALCO</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L987–1043  
**Auto-fixable:** Yes

**Description:**  
Process 'FALCO' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟠 <strong>48. STORAGE-001 — FALCO</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L987–1043  
**Auto-fixable:** No

**Description:**  
Process 'FALCO' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
/falco//g, /falco//g
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>49. RESOURCE-001 — FALCO</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L987–1043  
**Auto-fixable:** No

**Description:**  
Process 'FALCO' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

**Recommendation:**
```
Add a cpus directive appropriate for the tool's parallelism:
    cpus 4

Reference the allocation in the script block so the tool actually uses the provisioned cores:
    bwa mem -t ${task.cpus} ...

For workflows that need to scale, consider a dynamic expression:
    cpus { reads.size() > 5.GB ? 8 : 4 }
```

</details>

<details><summary>🟡 <strong>50. RESOURCE-002 — FALCO</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L987–1043  
**Auto-fixable:** No

**Description:**  
Process 'FALCO' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

**Recommendation:**
```
Add a memory directive sized for the tool's peak usage:
    memory '8 GB'

For resilient pipelines, combine with an error strategy that increases memory on retry:
    errorStrategy 'retry'
    maxRetries 2
    memory { (8.GB * task.attempt).clamp(null, 32.GB) }
```

</details>

<details><summary>🔴 <strong>51. CONTAINER-001 — FASTP</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L1047–1171  
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

<details><summary>🟠 <strong>52. STORAGE-001 — FASTP</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L1047–1171  
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

<details><summary>🟡 <strong>53. RESOURCE-001 — FASTP</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L1047–1171  
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

<details><summary>🟡 <strong>54. RESOURCE-002 — FASTP</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L1047–1171  
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

<details><summary>🔴 <strong>55. CONTAINER-001 — FASTQC</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L1175–1238  
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

<details><summary>🟠 <strong>56. STORAGE-001 — FASTQC</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L1175–1238  
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

<details><summary>🟡 <strong>57. RESOURCE-001 — FASTQC</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L1175–1238  
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

<details><summary>🟡 <strong>58. RESOURCE-002 — FASTQC</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L1175–1238  
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

<details><summary>🔴 <strong>59. CONTAINER-001 — FILTLONG</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L1242–1280  
**Auto-fixable:** Yes

**Description:**  
Process 'FILTLONG' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟠 <strong>60. STORAGE-001 — FILTLONG</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L1242–1280  
**Auto-fixable:** No

**Description:**  
Process 'FILTLONG' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
/Filtlong, //g
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>61. RESOURCE-001 — FILTLONG</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L1242–1280  
**Auto-fixable:** No

**Description:**  
Process 'FILTLONG' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

**Recommendation:**
```
Add a cpus directive appropriate for the tool's parallelism:
    cpus 4

Reference the allocation in the script block so the tool actually uses the provisioned cores:
    bwa mem -t ${task.cpus} ...

For workflows that need to scale, consider a dynamic expression:
    cpus { reads.size() > 5.GB ? 8 : 4 }
```

</details>

<details><summary>🟡 <strong>62. RESOURCE-002 — FILTLONG</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L1242–1280  
**Auto-fixable:** No

**Description:**  
Process 'FILTLONG' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

**Recommendation:**
```
Add a memory directive sized for the tool's peak usage:
    memory '8 GB'

For resilient pipelines, combine with an error strategy that increases memory on retry:
    errorStrategy 'retry'
    maxRetries 2
    memory { (8.GB * task.attempt).clamp(null, 32.GB) }
```

</details>

<details><summary>🔴 <strong>63. CONTAINER-001 — GANON_CLASSIFY</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L1284–1347  
**Auto-fixable:** Yes

**Description:**  
Process 'GANON_CLASSIFY' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟠 <strong>64. STORAGE-001 — GANON_CLASSIFY</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L1284–1347  
**Auto-fixable:** No

**Description:**  
Process 'GANON_CLASSIFY' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
//, /., //g
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>65. RESOURCE-001 — GANON_CLASSIFY</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L1284–1347  
**Auto-fixable:** No

**Description:**  
Process 'GANON_CLASSIFY' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

**Recommendation:**
```
Add a cpus directive appropriate for the tool's parallelism:
    cpus 4

Reference the allocation in the script block so the tool actually uses the provisioned cores:
    bwa mem -t ${task.cpus} ...

For workflows that need to scale, consider a dynamic expression:
    cpus { reads.size() > 5.GB ? 8 : 4 }
```

</details>

<details><summary>🟡 <strong>66. RESOURCE-002 — GANON_CLASSIFY</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L1284–1347  
**Auto-fixable:** No

**Description:**  
Process 'GANON_CLASSIFY' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

**Recommendation:**
```
Add a memory directive sized for the tool's peak usage:
    memory '8 GB'

For resilient pipelines, combine with an error strategy that increases memory on retry:
    errorStrategy 'retry'
    maxRetries 2
    memory { (8.GB * task.attempt).clamp(null, 32.GB) }
```

</details>

<details><summary>🔴 <strong>67. CONTAINER-001 — GANON_REPORT</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L1351–1402  
**Auto-fixable:** Yes

**Description:**  
Process 'GANON_REPORT' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟠 <strong>68. STORAGE-001 — GANON_REPORT</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L1351–1402  
**Auto-fixable:** No

**Description:**  
Process 'GANON_REPORT' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
//, /., //g
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>69. RESOURCE-001 — GANON_REPORT</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L1351–1402  
**Auto-fixable:** No

**Description:**  
Process 'GANON_REPORT' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

**Recommendation:**
```
Add a cpus directive appropriate for the tool's parallelism:
    cpus 4

Reference the allocation in the script block so the tool actually uses the provisioned cores:
    bwa mem -t ${task.cpus} ...

For workflows that need to scale, consider a dynamic expression:
    cpus { reads.size() > 5.GB ? 8 : 4 }
```

</details>

<details><summary>🟡 <strong>70. RESOURCE-002 — GANON_REPORT</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L1351–1402  
**Auto-fixable:** No

**Description:**  
Process 'GANON_REPORT' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

**Recommendation:**
```
Add a memory directive sized for the tool's peak usage:
    memory '8 GB'

For resilient pipelines, combine with an error strategy that increases memory on retry:
    errorStrategy 'retry'
    maxRetries 2
    memory { (8.GB * task.attempt).clamp(null, 32.GB) }
```

</details>

<details><summary>🔴 <strong>71. CONTAINER-001 — GANON_TABLE</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L1406–1452  
**Auto-fixable:** Yes

**Description:**  
Process 'GANON_TABLE' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟠 <strong>72. STORAGE-001 — GANON_TABLE</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L1406–1452  
**Auto-fixable:** No

**Description:**  
Process 'GANON_TABLE' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
/., //g
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>73. RESOURCE-001 — GANON_TABLE</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L1406–1452  
**Auto-fixable:** No

**Description:**  
Process 'GANON_TABLE' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

**Recommendation:**
```
Add a cpus directive appropriate for the tool's parallelism:
    cpus 4

Reference the allocation in the script block so the tool actually uses the provisioned cores:
    bwa mem -t ${task.cpus} ...

For workflows that need to scale, consider a dynamic expression:
    cpus { reads.size() > 5.GB ? 8 : 4 }
```

</details>

<details><summary>🟡 <strong>74. RESOURCE-002 — GANON_TABLE</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L1406–1452  
**Auto-fixable:** No

**Description:**  
Process 'GANON_TABLE' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

**Recommendation:**
```
Add a memory directive sized for the tool's peak usage:
    memory '8 GB'

For resilient pipelines, combine with an error strategy that increases memory on retry:
    errorStrategy 'retry'
    maxRetries 2
    memory { (8.GB * task.attempt).clamp(null, 32.GB) }
```

</details>

<details><summary>🔴 <strong>75. CONTAINER-001 — GUNZIP</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L1456–1510  
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

<details><summary>🟠 <strong>76. STORAGE-001 — GUNZIP</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L1456–1510  
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

<details><summary>🟡 <strong>77. RESOURCE-001 — GUNZIP</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L1456–1510  
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

<details><summary>🟡 <strong>78. RESOURCE-002 — GUNZIP</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L1456–1510  
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

<details><summary>🔴 <strong>79. CONTAINER-001 — KAIJU_KAIJU</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L1514–1568  
**Auto-fixable:** Yes

**Description:**  
Process 'KAIJU_KAIJU' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟠 <strong>80. STORAGE-001 — KAIJU_KAIJU</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L1514–1568  
**Auto-fixable:** No

**Description:**  
Process 'KAIJU_KAIJU' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
//
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>81. RESOURCE-001 — KAIJU_KAIJU</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L1514–1568  
**Auto-fixable:** No

**Description:**  
Process 'KAIJU_KAIJU' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

**Recommendation:**
```
Add a cpus directive appropriate for the tool's parallelism:
    cpus 4

Reference the allocation in the script block so the tool actually uses the provisioned cores:
    bwa mem -t ${task.cpus} ...

For workflows that need to scale, consider a dynamic expression:
    cpus { reads.size() > 5.GB ? 8 : 4 }
```

</details>

<details><summary>🟡 <strong>82. RESOURCE-002 — KAIJU_KAIJU</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L1514–1568  
**Auto-fixable:** No

**Description:**  
Process 'KAIJU_KAIJU' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

**Recommendation:**
```
Add a memory directive sized for the tool's peak usage:
    memory '8 GB'

For resilient pipelines, combine with an error strategy that increases memory on retry:
    errorStrategy 'retry'
    maxRetries 2
    memory { (8.GB * task.attempt).clamp(null, 32.GB) }
```

</details>

<details><summary>🔴 <strong>83. CONTAINER-001 — KAIJU_KAIJU2KRONA</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L1572–1622  
**Auto-fixable:** Yes

**Description:**  
Process 'KAIJU_KAIJU2KRONA' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟠 <strong>84. STORAGE-001 — KAIJU_KAIJU2KRONA</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L1572–1622  
**Auto-fixable:** No

**Description:**  
Process 'KAIJU_KAIJU2KRONA' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
//
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>85. RESOURCE-001 — KAIJU_KAIJU2KRONA</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L1572–1622  
**Auto-fixable:** No

**Description:**  
Process 'KAIJU_KAIJU2KRONA' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

**Recommendation:**
```
Add a cpus directive appropriate for the tool's parallelism:
    cpus 4

Reference the allocation in the script block so the tool actually uses the provisioned cores:
    bwa mem -t ${task.cpus} ...

For workflows that need to scale, consider a dynamic expression:
    cpus { reads.size() > 5.GB ? 8 : 4 }
```

</details>

<details><summary>🟡 <strong>86. RESOURCE-002 — KAIJU_KAIJU2KRONA</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L1572–1622  
**Auto-fixable:** No

**Description:**  
Process 'KAIJU_KAIJU2KRONA' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

**Recommendation:**
```
Add a memory directive sized for the tool's peak usage:
    memory '8 GB'

For resilient pipelines, combine with an error strategy that increases memory on retry:
    errorStrategy 'retry'
    maxRetries 2
    memory { (8.GB * task.attempt).clamp(null, 32.GB) }
```

</details>

<details><summary>🔴 <strong>87. CONTAINER-001 — KAIJU_KAIJU2TABLE</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L1626–1677  
**Auto-fixable:** Yes

**Description:**  
Process 'KAIJU_KAIJU2TABLE' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟠 <strong>88. STORAGE-001 — KAIJU_KAIJU2TABLE</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L1626–1677  
**Auto-fixable:** No

**Description:**  
Process 'KAIJU_KAIJU2TABLE' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
//
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>89. RESOURCE-001 — KAIJU_KAIJU2TABLE</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L1626–1677  
**Auto-fixable:** No

**Description:**  
Process 'KAIJU_KAIJU2TABLE' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

**Recommendation:**
```
Add a cpus directive appropriate for the tool's parallelism:
    cpus 4

Reference the allocation in the script block so the tool actually uses the provisioned cores:
    bwa mem -t ${task.cpus} ...

For workflows that need to scale, consider a dynamic expression:
    cpus { reads.size() > 5.GB ? 8 : 4 }
```

</details>

<details><summary>🟡 <strong>90. RESOURCE-002 — KAIJU_KAIJU2TABLE</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L1626–1677  
**Auto-fixable:** No

**Description:**  
Process 'KAIJU_KAIJU2TABLE' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

**Recommendation:**
```
Add a memory directive sized for the tool's peak usage:
    memory '8 GB'

For resilient pipelines, combine with an error strategy that increases memory on retry:
    errorStrategy 'retry'
    maxRetries 2
    memory { (8.GB * task.attempt).clamp(null, 32.GB) }
```

</details>

<details><summary>🔴 <strong>91. CONTAINER-001 — KMCP_PROFILE</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L1681–1732  
**Auto-fixable:** Yes

**Description:**  
Process 'KMCP_PROFILE' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟠 <strong>92. STORAGE-001 — KMCP_PROFILE</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L1681–1732  
**Auto-fixable:** No

**Description:**  
Process 'KMCP_PROFILE' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
//
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>93. RESOURCE-001 — KMCP_PROFILE</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L1681–1732  
**Auto-fixable:** No

**Description:**  
Process 'KMCP_PROFILE' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

**Recommendation:**
```
Add a cpus directive appropriate for the tool's parallelism:
    cpus 4

Reference the allocation in the script block so the tool actually uses the provisioned cores:
    bwa mem -t ${task.cpus} ...

For workflows that need to scale, consider a dynamic expression:
    cpus { reads.size() > 5.GB ? 8 : 4 }
```

</details>

<details><summary>🟡 <strong>94. RESOURCE-002 — KMCP_PROFILE</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L1681–1732  
**Auto-fixable:** No

**Description:**  
Process 'KMCP_PROFILE' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

**Recommendation:**
```
Add a memory directive sized for the tool's peak usage:
    memory '8 GB'

For resilient pipelines, combine with an error strategy that increases memory on retry:
    errorStrategy 'retry'
    maxRetries 2
    memory { (8.GB * task.attempt).clamp(null, 32.GB) }
```

</details>

<details><summary>🔴 <strong>95. CONTAINER-001 — KMCP_SEARCH</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L1736–1786  
**Auto-fixable:** Yes

**Description:**  
Process 'KMCP_SEARCH' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟠 <strong>96. STORAGE-001 — KMCP_SEARCH</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L1736–1786  
**Auto-fixable:** No

**Description:**  
Process 'KMCP_SEARCH' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
//
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>97. RESOURCE-001 — KMCP_SEARCH</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L1736–1786  
**Auto-fixable:** No

**Description:**  
Process 'KMCP_SEARCH' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

**Recommendation:**
```
Add a cpus directive appropriate for the tool's parallelism:
    cpus 4

Reference the allocation in the script block so the tool actually uses the provisioned cores:
    bwa mem -t ${task.cpus} ...

For workflows that need to scale, consider a dynamic expression:
    cpus { reads.size() > 5.GB ? 8 : 4 }
```

</details>

<details><summary>🟡 <strong>98. RESOURCE-002 — KMCP_SEARCH</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L1736–1786  
**Auto-fixable:** No

**Description:**  
Process 'KMCP_SEARCH' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

**Recommendation:**
```
Add a memory directive sized for the tool's peak usage:
    memory '8 GB'

For resilient pipelines, combine with an error strategy that increases memory on retry:
    errorStrategy 'retry'
    maxRetries 2
    memory { (8.GB * task.attempt).clamp(null, 32.GB) }
```

</details>

<details><summary>🔴 <strong>99. CONTAINER-001 — KRAKEN2_KRAKEN2</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L1790–1874  
**Auto-fixable:** Yes

**Description:**  
Process 'KRAKEN2_KRAKEN2' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟠 <strong>100. STORAGE-001 — KRAKEN2_KRAKEN2</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L1790–1874  
**Auto-fixable:** No

**Description:**  
Process 'KRAKEN2_KRAKEN2' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
/dev/null, //, // ... (2 more)
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>101. RESOURCE-001 — KRAKEN2_KRAKEN2</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L1790–1874  
**Auto-fixable:** No

**Description:**  
Process 'KRAKEN2_KRAKEN2' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

**Recommendation:**
```
Add a cpus directive appropriate for the tool's parallelism:
    cpus 4

Reference the allocation in the script block so the tool actually uses the provisioned cores:
    bwa mem -t ${task.cpus} ...

For workflows that need to scale, consider a dynamic expression:
    cpus { reads.size() > 5.GB ? 8 : 4 }
```

</details>

<details><summary>🟡 <strong>102. RESOURCE-002 — KRAKEN2_KRAKEN2</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L1790–1874  
**Auto-fixable:** No

**Description:**  
Process 'KRAKEN2_KRAKEN2' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

**Recommendation:**
```
Add a memory directive sized for the tool's peak usage:
    memory '8 GB'

For resilient pipelines, combine with an error strategy that increases memory on retry:
    errorStrategy 'retry'
    maxRetries 2
    memory { (8.GB * task.attempt).clamp(null, 32.GB) }
```

</details>

<details><summary>🔴 <strong>103. CONTAINER-001 — KRAKENTOOLS_COMBINEKREPORTS</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L1878–1924  
**Auto-fixable:** Yes

**Description:**  
Process 'KRAKENTOOLS_COMBINEKREPORTS' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟠 <strong>104. STORAGE-001 — KRAKENTOOLS_COMBINEKREPORTS</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L1878–1924  
**Auto-fixable:** No

**Description:**  
Process 'KRAKENTOOLS_COMBINEKREPORTS' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
//
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>105. RESOURCE-001 — KRAKENTOOLS_COMBINEKREPORTS</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L1878–1924  
**Auto-fixable:** No

**Description:**  
Process 'KRAKENTOOLS_COMBINEKREPORTS' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

**Recommendation:**
```
Add a cpus directive appropriate for the tool's parallelism:
    cpus 4

Reference the allocation in the script block so the tool actually uses the provisioned cores:
    bwa mem -t ${task.cpus} ...

For workflows that need to scale, consider a dynamic expression:
    cpus { reads.size() > 5.GB ? 8 : 4 }
```

</details>

<details><summary>🟡 <strong>106. RESOURCE-002 — KRAKENTOOLS_COMBINEKREPORTS</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L1878–1924  
**Auto-fixable:** No

**Description:**  
Process 'KRAKENTOOLS_COMBINEKREPORTS' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

**Recommendation:**
```
Add a memory directive sized for the tool's peak usage:
    memory '8 GB'

For resilient pipelines, combine with an error strategy that increases memory on retry:
    errorStrategy 'retry'
    maxRetries 2
    memory { (8.GB * task.attempt).clamp(null, 32.GB) }
```

</details>

<details><summary>🔴 <strong>107. CONTAINER-001 — KRAKENTOOLS_KREPORT2KRONA</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L1928–1976  
**Auto-fixable:** Yes

**Description:**  
Process 'KRAKENTOOLS_KREPORT2KRONA' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟠 <strong>108. STORAGE-001 — KRAKENTOOLS_KREPORT2KRONA</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L1928–1976  
**Auto-fixable:** No

**Description:**  
Process 'KRAKENTOOLS_KREPORT2KRONA' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
//
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>109. RESOURCE-001 — KRAKENTOOLS_KREPORT2KRONA</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L1928–1976  
**Auto-fixable:** No

**Description:**  
Process 'KRAKENTOOLS_KREPORT2KRONA' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

**Recommendation:**
```
Add a cpus directive appropriate for the tool's parallelism:
    cpus 4

Reference the allocation in the script block so the tool actually uses the provisioned cores:
    bwa mem -t ${task.cpus} ...

For workflows that need to scale, consider a dynamic expression:
    cpus { reads.size() > 5.GB ? 8 : 4 }
```

</details>

<details><summary>🟡 <strong>110. RESOURCE-002 — KRAKENTOOLS_KREPORT2KRONA</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L1928–1976  
**Auto-fixable:** No

**Description:**  
Process 'KRAKENTOOLS_KREPORT2KRONA' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

**Recommendation:**
```
Add a memory directive sized for the tool's peak usage:
    memory '8 GB'

For resilient pipelines, combine with an error strategy that increases memory on retry:
    errorStrategy 'retry'
    maxRetries 2
    memory { (8.GB * task.attempt).clamp(null, 32.GB) }
```

</details>

<details><summary>🔴 <strong>111. CONTAINER-001 — KRAKENUNIQ_PRELOADEDKRAKENUNIQ</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L1980–2206  
**Auto-fixable:** Yes

**Description:**  
Process 'KRAKENUNIQ_PRELOADEDKRAKENUNIQ' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟠 <strong>112. STORAGE-001 — KRAKENUNIQ_PRELOADEDKRAKENUNIQ</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L1980–2206  
**Auto-fixable:** No

**Description:**  
Process 'KRAKENUNIQ_PRELOADEDKRAKENUNIQ' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
//, //, // ... (1 more)
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>113. RESOURCE-001 — KRAKENUNIQ_PRELOADEDKRAKENUNIQ</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L1980–2206  
**Auto-fixable:** No

**Description:**  
Process 'KRAKENUNIQ_PRELOADEDKRAKENUNIQ' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

**Recommendation:**
```
Add a cpus directive appropriate for the tool's parallelism:
    cpus 4

Reference the allocation in the script block so the tool actually uses the provisioned cores:
    bwa mem -t ${task.cpus} ...

For workflows that need to scale, consider a dynamic expression:
    cpus { reads.size() > 5.GB ? 8 : 4 }
```

</details>

<details><summary>🟡 <strong>114. RESOURCE-002 — KRAKENUNIQ_PRELOADEDKRAKENUNIQ</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L1980–2206  
**Auto-fixable:** No

**Description:**  
Process 'KRAKENUNIQ_PRELOADEDKRAKENUNIQ' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

**Recommendation:**
```
Add a memory directive sized for the tool's peak usage:
    memory '8 GB'

For resilient pipelines, combine with an error strategy that increases memory on retry:
    errorStrategy 'retry'
    maxRetries 2
    memory { (8.GB * task.attempt).clamp(null, 32.GB) }
```

</details>

<details><summary>🔴 <strong>115. CONTAINER-001 — KRONA_KTIMPORTTAXONOMY</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L2210–2260  
**Auto-fixable:** Yes

**Description:**  
Process 'KRONA_KTIMPORTTAXONOMY' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟡 <strong>116. RESOURCE-001 — KRONA_KTIMPORTTAXONOMY</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L2210–2260  
**Auto-fixable:** No

**Description:**  
Process 'KRONA_KTIMPORTTAXONOMY' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

**Recommendation:**
```
Add a cpus directive appropriate for the tool's parallelism:
    cpus 4

Reference the allocation in the script block so the tool actually uses the provisioned cores:
    bwa mem -t ${task.cpus} ...

For workflows that need to scale, consider a dynamic expression:
    cpus { reads.size() > 5.GB ? 8 : 4 }
```

</details>

<details><summary>🟡 <strong>117. RESOURCE-002 — KRONA_KTIMPORTTAXONOMY</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L2210–2260  
**Auto-fixable:** No

**Description:**  
Process 'KRONA_KTIMPORTTAXONOMY' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

**Recommendation:**
```
Add a memory directive sized for the tool's peak usage:
    memory '8 GB'

For resilient pipelines, combine with an error strategy that increases memory on retry:
    errorStrategy 'retry'
    maxRetries 2
    memory { (8.GB * task.attempt).clamp(null, 32.GB) }
```

</details>

<details><summary>🔴 <strong>118. CONTAINER-001 — KRONA_KTIMPORTTEXT</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L2264–2308  
**Auto-fixable:** Yes

**Description:**  
Process 'KRONA_KTIMPORTTEXT' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟠 <strong>119. STORAGE-001 — KRONA_KTIMPORTTEXT</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L2264–2308  
**Auto-fixable:** No

**Description:**  
Process 'KRONA_KTIMPORTTEXT' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
//g, /-, //g
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>120. RESOURCE-001 — KRONA_KTIMPORTTEXT</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L2264–2308  
**Auto-fixable:** No

**Description:**  
Process 'KRONA_KTIMPORTTEXT' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

**Recommendation:**
```
Add a cpus directive appropriate for the tool's parallelism:
    cpus 4

Reference the allocation in the script block so the tool actually uses the provisioned cores:
    bwa mem -t ${task.cpus} ...

For workflows that need to scale, consider a dynamic expression:
    cpus { reads.size() > 5.GB ? 8 : 4 }
```

</details>

<details><summary>🟡 <strong>121. RESOURCE-002 — KRONA_KTIMPORTTEXT</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L2264–2308  
**Auto-fixable:** No

**Description:**  
Process 'KRONA_KTIMPORTTEXT' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

**Recommendation:**
```
Add a memory directive sized for the tool's peak usage:
    memory '8 GB'

For resilient pipelines, combine with an error strategy that increases memory on retry:
    errorStrategy 'retry'
    maxRetries 2
    memory { (8.GB * task.attempt).clamp(null, 32.GB) }
```

</details>

<details><summary>🔴 <strong>122. CONTAINER-001 — MALT_RUN</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L2312–2365  
**Auto-fixable:** Yes

**Description:**  
Process 'MALT_RUN' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟡 <strong>123. RESOURCE-001 — MALT_RUN</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L2312–2365  
**Auto-fixable:** No

**Description:**  
Process 'MALT_RUN' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

**Recommendation:**
```
Add a cpus directive appropriate for the tool's parallelism:
    cpus 4

Reference the allocation in the script block so the tool actually uses the provisioned cores:
    bwa mem -t ${task.cpus} ...

For workflows that need to scale, consider a dynamic expression:
    cpus { reads.size() > 5.GB ? 8 : 4 }
```

</details>

<details><summary>🟡 <strong>124. RESOURCE-002 — MALT_RUN</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L2312–2365  
**Auto-fixable:** No

**Description:**  
Process 'MALT_RUN' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

**Recommendation:**
```
Add a memory directive sized for the tool's peak usage:
    memory '8 GB'

For resilient pipelines, combine with an error strategy that increases memory on retry:
    errorStrategy 'retry'
    maxRetries 2
    memory { (8.GB * task.attempt).clamp(null, 32.GB) }
```

</details>

<details><summary>🔴 <strong>125. CONTAINER-001 — MEGAN_RMA2INFO</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L2369–2419  
**Auto-fixable:** Yes

**Description:**  
Process 'MEGAN_RMA2INFO' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟠 <strong>126. STORAGE-001 — MEGAN_RMA2INFO</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L2369–2419  
**Auto-fixable:** No

**Description:**  
Process 'MEGAN_RMA2INFO' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
/., //g, //g
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>127. RESOURCE-001 — MEGAN_RMA2INFO</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L2369–2419  
**Auto-fixable:** No

**Description:**  
Process 'MEGAN_RMA2INFO' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

**Recommendation:**
```
Add a cpus directive appropriate for the tool's parallelism:
    cpus 4

Reference the allocation in the script block so the tool actually uses the provisioned cores:
    bwa mem -t ${task.cpus} ...

For workflows that need to scale, consider a dynamic expression:
    cpus { reads.size() > 5.GB ? 8 : 4 }
```

</details>

<details><summary>🟡 <strong>128. RESOURCE-002 — MEGAN_RMA2INFO</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L2369–2419  
**Auto-fixable:** No

**Description:**  
Process 'MEGAN_RMA2INFO' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

**Recommendation:**
```
Add a memory directive sized for the tool's peak usage:
    memory '8 GB'

For resilient pipelines, combine with an error strategy that increases memory on retry:
    errorStrategy 'retry'
    maxRetries 2
    memory { (8.GB * task.attempt).clamp(null, 32.GB) }
```

</details>

<details><summary>🔴 <strong>129. CONTAINER-001 — METAPHLAN_MERGEMETAPHLANTABLES</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L2423–2467  
**Auto-fixable:** Yes

**Description:**  
Process 'METAPHLAN_MERGEMETAPHLANTABLES' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟡 <strong>130. RESOURCE-001 — METAPHLAN_MERGEMETAPHLANTABLES</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L2423–2467  
**Auto-fixable:** No

**Description:**  
Process 'METAPHLAN_MERGEMETAPHLANTABLES' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

**Recommendation:**
```
Add a cpus directive appropriate for the tool's parallelism:
    cpus 4

Reference the allocation in the script block so the tool actually uses the provisioned cores:
    bwa mem -t ${task.cpus} ...

For workflows that need to scale, consider a dynamic expression:
    cpus { reads.size() > 5.GB ? 8 : 4 }
```

</details>

<details><summary>🟡 <strong>131. RESOURCE-002 — METAPHLAN_MERGEMETAPHLANTABLES</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L2423–2467  
**Auto-fixable:** No

**Description:**  
Process 'METAPHLAN_MERGEMETAPHLANTABLES' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

**Recommendation:**
```
Add a memory directive sized for the tool's peak usage:
    memory '8 GB'

For resilient pipelines, combine with an error strategy that increases memory on retry:
    errorStrategy 'retry'
    maxRetries 2
    memory { (8.GB * task.attempt).clamp(null, 32.GB) }
```

</details>

<details><summary>🔴 <strong>132. CONTAINER-001 — METAPHLAN_METAPHLAN</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L2471–2541  
**Auto-fixable:** Yes

**Description:**  
Process 'METAPHLAN_METAPHLAN' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟠 <strong>133. STORAGE-001 — METAPHLAN_METAPHLAN</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L2471–2541  
**Auto-fixable:** No

**Description:**  
Process 'METAPHLAN_METAPHLAN' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
/., /., // ... (2 more)
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>134. RESOURCE-001 — METAPHLAN_METAPHLAN</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L2471–2541  
**Auto-fixable:** No

**Description:**  
Process 'METAPHLAN_METAPHLAN' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

**Recommendation:**
```
Add a cpus directive appropriate for the tool's parallelism:
    cpus 4

Reference the allocation in the script block so the tool actually uses the provisioned cores:
    bwa mem -t ${task.cpus} ...

For workflows that need to scale, consider a dynamic expression:
    cpus { reads.size() > 5.GB ? 8 : 4 }
```

</details>

<details><summary>🟡 <strong>135. RESOURCE-002 — METAPHLAN_METAPHLAN</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L2471–2541  
**Auto-fixable:** No

**Description:**  
Process 'METAPHLAN_METAPHLAN' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

**Recommendation:**
```
Add a memory directive sized for the tool's peak usage:
    memory '8 GB'

For resilient pipelines, combine with an error strategy that increases memory on retry:
    errorStrategy 'retry'
    maxRetries 2
    memory { (8.GB * task.attempt).clamp(null, 32.GB) }
```

</details>

<details><summary>🔴 <strong>136. CONTAINER-001 — MINIMAP2_ALIGN</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L2545–2622  
**Auto-fixable:** Yes

**Description:**  
Process 'MINIMAP2_ALIGN' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟠 <strong>137. STORAGE-001 — MINIMAP2_ALIGN</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L2545–2622  
**Auto-fixable:** No

**Description:**  
Process 'MINIMAP2_ALIGN' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
//, /Using., //
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>138. RESOURCE-001 — MINIMAP2_ALIGN</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L2545–2622  
**Auto-fixable:** No

**Description:**  
Process 'MINIMAP2_ALIGN' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

**Recommendation:**
```
Add a cpus directive appropriate for the tool's parallelism:
    cpus 4

Reference the allocation in the script block so the tool actually uses the provisioned cores:
    bwa mem -t ${task.cpus} ...

For workflows that need to scale, consider a dynamic expression:
    cpus { reads.size() > 5.GB ? 8 : 4 }
```

</details>

<details><summary>🟡 <strong>139. RESOURCE-002 — MINIMAP2_ALIGN</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L2545–2622  
**Auto-fixable:** No

**Description:**  
Process 'MINIMAP2_ALIGN' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

**Recommendation:**
```
Add a memory directive sized for the tool's peak usage:
    memory '8 GB'

For resilient pipelines, combine with an error strategy that increases memory on retry:
    errorStrategy 'retry'
    maxRetries 2
    memory { (8.GB * task.attempt).clamp(null, 32.GB) }
```

</details>

<details><summary>🔴 <strong>140. CONTAINER-001 — MINIMAP2_INDEX</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L2626–2669  
**Auto-fixable:** Yes

**Description:**  
Process 'MINIMAP2_INDEX' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟡 <strong>141. RESOURCE-001 — MINIMAP2_INDEX</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L2626–2669  
**Auto-fixable:** No

**Description:**  
Process 'MINIMAP2_INDEX' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

**Recommendation:**
```
Add a cpus directive appropriate for the tool's parallelism:
    cpus 4

Reference the allocation in the script block so the tool actually uses the provisioned cores:
    bwa mem -t ${task.cpus} ...

For workflows that need to scale, consider a dynamic expression:
    cpus { reads.size() > 5.GB ? 8 : 4 }
```

</details>

<details><summary>🟡 <strong>142. RESOURCE-002 — MINIMAP2_INDEX</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L2626–2669  
**Auto-fixable:** No

**Description:**  
Process 'MINIMAP2_INDEX' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

**Recommendation:**
```
Add a memory directive sized for the tool's peak usage:
    memory '8 GB'

For resilient pipelines, combine with an error strategy that increases memory on retry:
    errorStrategy 'retry'
    maxRetries 2
    memory { (8.GB * task.attempt).clamp(null, 32.GB) }
```

</details>

<details><summary>🔴 <strong>143. CONTAINER-001 — MOTUS_MERGE</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L2673–2735  
**Auto-fixable:** Yes

**Description:**  
Process 'MOTUS_MERGE' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟠 <strong>144. STORAGE-001 — MOTUS_MERGE</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L2673–2735  
**Auto-fixable:** No

**Description:**  
Process 'MOTUS_MERGE' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
/profile, /., //g
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>145. RESOURCE-001 — MOTUS_MERGE</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L2673–2735  
**Auto-fixable:** No

**Description:**  
Process 'MOTUS_MERGE' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

**Recommendation:**
```
Add a cpus directive appropriate for the tool's parallelism:
    cpus 4

Reference the allocation in the script block so the tool actually uses the provisioned cores:
    bwa mem -t ${task.cpus} ...

For workflows that need to scale, consider a dynamic expression:
    cpus { reads.size() > 5.GB ? 8 : 4 }
```

</details>

<details><summary>🟡 <strong>146. RESOURCE-002 — MOTUS_MERGE</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L2673–2735  
**Auto-fixable:** No

**Description:**  
Process 'MOTUS_MERGE' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

**Recommendation:**
```
Add a memory directive sized for the tool's peak usage:
    memory '8 GB'

For resilient pipelines, combine with an error strategy that increases memory on retry:
    errorStrategy 'retry'
    maxRetries 2
    memory { (8.GB * task.attempt).clamp(null, 32.GB) }
```

</details>

<details><summary>🔴 <strong>147. CONTAINER-001 — MOTUS_PROFILE</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L2739–2818  
**Auto-fixable:** Yes

**Description:**  
Process 'MOTUS_PROFILE' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟠 <strong>148. STORAGE-001 — MOTUS_PROFILE</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L2739–2818  
**Auto-fixable:** No

**Description:**  
Process 'MOTUS_PROFILE' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
//, /References., // ... (3 more)
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>149. RESOURCE-001 — MOTUS_PROFILE</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L2739–2818  
**Auto-fixable:** No

**Description:**  
Process 'MOTUS_PROFILE' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

**Recommendation:**
```
Add a cpus directive appropriate for the tool's parallelism:
    cpus 4

Reference the allocation in the script block so the tool actually uses the provisioned cores:
    bwa mem -t ${task.cpus} ...

For workflows that need to scale, consider a dynamic expression:
    cpus { reads.size() > 5.GB ? 8 : 4 }
```

</details>

<details><summary>🟡 <strong>150. RESOURCE-002 — MOTUS_PROFILE</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L2739–2818  
**Auto-fixable:** No

**Description:**  
Process 'MOTUS_PROFILE' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

**Recommendation:**
```
Add a memory directive sized for the tool's peak usage:
    memory '8 GB'

For resilient pipelines, combine with an error strategy that increases memory on retry:
    errorStrategy 'retry'
    maxRetries 2
    memory { (8.GB * task.attempt).clamp(null, 32.GB) }
```

</details>

<details><summary>🔴 <strong>151. CONTAINER-001 — MULTIQC</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L2822–2884  
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

<details><summary>🟠 <strong>152. STORAGE-001 — MULTIQC</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L2822–2884  
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

<details><summary>🟡 <strong>153. RESOURCE-001 — MULTIQC</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L2822–2884  
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

<details><summary>🟡 <strong>154. RESOURCE-002 — MULTIQC</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L2822–2884  
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

<details><summary>🔴 <strong>155. CONTAINER-001 — NANOQ</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L2888–2936  
**Auto-fixable:** Yes

**Description:**  
Process 'NANOQ' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟠 <strong>156. STORAGE-001 — NANOQ</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L2888–2936  
**Auto-fixable:** No

**Description:**  
Process 'NANOQ' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
/nanoq, //g
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>157. RESOURCE-001 — NANOQ</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L2888–2936  
**Auto-fixable:** No

**Description:**  
Process 'NANOQ' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

**Recommendation:**
```
Add a cpus directive appropriate for the tool's parallelism:
    cpus 4

Reference the allocation in the script block so the tool actually uses the provisioned cores:
    bwa mem -t ${task.cpus} ...

For workflows that need to scale, consider a dynamic expression:
    cpus { reads.size() > 5.GB ? 8 : 4 }
```

</details>

<details><summary>🟡 <strong>158. RESOURCE-002 — NANOQ</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L2888–2936  
**Auto-fixable:** No

**Description:**  
Process 'NANOQ' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

**Recommendation:**
```
Add a memory directive sized for the tool's peak usage:
    memory '8 GB'

For resilient pipelines, combine with an error strategy that increases memory on retry:
    errorStrategy 'retry'
    maxRetries 2
    memory { (8.GB * task.attempt).clamp(null, 32.GB) }
```

</details>

<details><summary>🔴 <strong>159. CONTAINER-001 — NONPAREIL_CURVE</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L2940–2990  
**Auto-fixable:** Yes

**Description:**  
Process 'NONPAREIL_CURVE' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟠 <strong>160. STORAGE-001 — NONPAREIL_CURVE</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L2940–2990  
**Auto-fixable:** No

**Description:**  
Process 'NONPAREIL_CURVE' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
/usr/bin/env
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>161. RESOURCE-001 — NONPAREIL_CURVE</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L2940–2990  
**Auto-fixable:** No

**Description:**  
Process 'NONPAREIL_CURVE' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

**Recommendation:**
```
Add a cpus directive appropriate for the tool's parallelism:
    cpus 4

Reference the allocation in the script block so the tool actually uses the provisioned cores:
    bwa mem -t ${task.cpus} ...

For workflows that need to scale, consider a dynamic expression:
    cpus { reads.size() > 5.GB ? 8 : 4 }
```

</details>

<details><summary>🟡 <strong>162. RESOURCE-002 — NONPAREIL_CURVE</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L2940–2990  
**Auto-fixable:** No

**Description:**  
Process 'NONPAREIL_CURVE' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

**Recommendation:**
```
Add a memory directive sized for the tool's peak usage:
    memory '8 GB'

For resilient pipelines, combine with an error strategy that increases memory on retry:
    errorStrategy 'retry'
    maxRetries 2
    memory { (8.GB * task.attempt).clamp(null, 32.GB) }
```

</details>

<details><summary>🔴 <strong>163. CONTAINER-001 — NONPAREIL_NONPAREIL</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L2994–3052  
**Auto-fixable:** Yes

**Description:**  
Process 'NONPAREIL_NONPAREIL' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟠 <strong>164. STORAGE-001 — NONPAREIL_NONPAREIL</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L2994–3052  
**Auto-fixable:** No

**Description:**  
Process 'NONPAREIL_NONPAREIL' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
/Nonpareil, //
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>165. RESOURCE-001 — NONPAREIL_NONPAREIL</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L2994–3052  
**Auto-fixable:** No

**Description:**  
Process 'NONPAREIL_NONPAREIL' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

**Recommendation:**
```
Add a cpus directive appropriate for the tool's parallelism:
    cpus 4

Reference the allocation in the script block so the tool actually uses the provisioned cores:
    bwa mem -t ${task.cpus} ...

For workflows that need to scale, consider a dynamic expression:
    cpus { reads.size() > 5.GB ? 8 : 4 }
```

</details>

<details><summary>🟡 <strong>166. RESOURCE-002 — NONPAREIL_NONPAREIL</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L2994–3052  
**Auto-fixable:** No

**Description:**  
Process 'NONPAREIL_NONPAREIL' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

**Recommendation:**
```
Add a memory directive sized for the tool's peak usage:
    memory '8 GB'

For resilient pipelines, combine with an error strategy that increases memory on retry:
    errorStrategy 'retry'
    maxRetries 2
    memory { (8.GB * task.attempt).clamp(null, 32.GB) }
```

</details>

<details><summary>🔴 <strong>167. CONTAINER-001 — NONPAREIL_NONPAREILCURVESR</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L3056–3112  
**Auto-fixable:** Yes

**Description:**  
Process 'NONPAREIL_NONPAREILCURVESR' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟠 <strong>168. STORAGE-001 — NONPAREIL_NONPAREILCURVESR</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L3056–3112  
**Auto-fixable:** No

**Description:**  
Process 'NONPAREIL_NONPAREILCURVESR' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
/Nonpareil, //
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>169. RESOURCE-001 — NONPAREIL_NONPAREILCURVESR</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L3056–3112  
**Auto-fixable:** No

**Description:**  
Process 'NONPAREIL_NONPAREILCURVESR' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

**Recommendation:**
```
Add a cpus directive appropriate for the tool's parallelism:
    cpus 4

Reference the allocation in the script block so the tool actually uses the provisioned cores:
    bwa mem -t ${task.cpus} ...

For workflows that need to scale, consider a dynamic expression:
    cpus { reads.size() > 5.GB ? 8 : 4 }
```

</details>

<details><summary>🟡 <strong>170. RESOURCE-002 — NONPAREIL_NONPAREILCURVESR</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L3056–3112  
**Auto-fixable:** No

**Description:**  
Process 'NONPAREIL_NONPAREILCURVESR' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

**Recommendation:**
```
Add a memory directive sized for the tool's peak usage:
    memory '8 GB'

For resilient pipelines, combine with an error strategy that increases memory on retry:
    errorStrategy 'retry'
    maxRetries 2
    memory { (8.GB * task.attempt).clamp(null, 32.GB) }
```

</details>

<details><summary>🔴 <strong>171. CONTAINER-001 — NONPAREIL_SET</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L3116–3166  
**Auto-fixable:** Yes

**Description:**  
Process 'NONPAREIL_SET' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟠 <strong>172. STORAGE-001 — NONPAREIL_SET</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L3116–3166  
**Auto-fixable:** No

**Description:**  
Process 'NONPAREIL_SET' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
/usr/bin/env
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>173. RESOURCE-001 — NONPAREIL_SET</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L3116–3166  
**Auto-fixable:** No

**Description:**  
Process 'NONPAREIL_SET' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

**Recommendation:**
```
Add a cpus directive appropriate for the tool's parallelism:
    cpus 4

Reference the allocation in the script block so the tool actually uses the provisioned cores:
    bwa mem -t ${task.cpus} ...

For workflows that need to scale, consider a dynamic expression:
    cpus { reads.size() > 5.GB ? 8 : 4 }
```

</details>

<details><summary>🟡 <strong>174. RESOURCE-002 — NONPAREIL_SET</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L3116–3166  
**Auto-fixable:** No

**Description:**  
Process 'NONPAREIL_SET' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

**Recommendation:**
```
Add a memory directive sized for the tool's peak usage:
    memory '8 GB'

For resilient pipelines, combine with an error strategy that increases memory on retry:
    errorStrategy 'retry'
    maxRetries 2
    memory { (8.GB * task.attempt).clamp(null, 32.GB) }
```

</details>

<details><summary>🔴 <strong>175. CONTAINER-001 — PORECHOP_ABI</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L3170–3219  
**Auto-fixable:** Yes

**Description:**  
Process 'PORECHOP_ABI' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟡 <strong>176. RESOURCE-001 — PORECHOP_ABI</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L3170–3219  
**Auto-fixable:** No

**Description:**  
Process 'PORECHOP_ABI' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

**Recommendation:**
```
Add a cpus directive appropriate for the tool's parallelism:
    cpus 4

Reference the allocation in the script block so the tool actually uses the provisioned cores:
    bwa mem -t ${task.cpus} ...

For workflows that need to scale, consider a dynamic expression:
    cpus { reads.size() > 5.GB ? 8 : 4 }
```

</details>

<details><summary>🟡 <strong>177. RESOURCE-002 — PORECHOP_ABI</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L3170–3219  
**Auto-fixable:** No

**Description:**  
Process 'PORECHOP_ABI' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

**Recommendation:**
```
Add a memory directive sized for the tool's peak usage:
    memory '8 GB'

For resilient pipelines, combine with an error strategy that increases memory on retry:
    errorStrategy 'retry'
    maxRetries 2
    memory { (8.GB * task.attempt).clamp(null, 32.GB) }
```

</details>

<details><summary>🔴 <strong>178. CONTAINER-001 — PORECHOP_PORECHOP</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L3223–3273  
**Auto-fixable:** Yes

**Description:**  
Process 'PORECHOP_PORECHOP' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟡 <strong>179. RESOURCE-001 — PORECHOP_PORECHOP</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L3223–3273  
**Auto-fixable:** No

**Description:**  
Process 'PORECHOP_PORECHOP' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

**Recommendation:**
```
Add a cpus directive appropriate for the tool's parallelism:
    cpus 4

Reference the allocation in the script block so the tool actually uses the provisioned cores:
    bwa mem -t ${task.cpus} ...

For workflows that need to scale, consider a dynamic expression:
    cpus { reads.size() > 5.GB ? 8 : 4 }
```

</details>

<details><summary>🟡 <strong>180. RESOURCE-002 — PORECHOP_PORECHOP</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L3223–3273  
**Auto-fixable:** No

**Description:**  
Process 'PORECHOP_PORECHOP' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

**Recommendation:**
```
Add a memory directive sized for the tool's peak usage:
    memory '8 GB'

For resilient pipelines, combine with an error strategy that increases memory on retry:
    errorStrategy 'retry'
    maxRetries 2
    memory { (8.GB * task.attempt).clamp(null, 32.GB) }
```

</details>

<details><summary>🔴 <strong>181. CONTAINER-001 — PRINSEQPLUSPLUS</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L3277–3337  
**Auto-fixable:** Yes

**Description:**  
Process 'PRINSEQPLUSPLUS' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟡 <strong>182. RESOURCE-001 — PRINSEQPLUSPLUS</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L3277–3337  
**Auto-fixable:** No

**Description:**  
Process 'PRINSEQPLUSPLUS' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

**Recommendation:**
```
Add a cpus directive appropriate for the tool's parallelism:
    cpus 4

Reference the allocation in the script block so the tool actually uses the provisioned cores:
    bwa mem -t ${task.cpus} ...

For workflows that need to scale, consider a dynamic expression:
    cpus { reads.size() > 5.GB ? 8 : 4 }
```

</details>

<details><summary>🟡 <strong>183. RESOURCE-002 — PRINSEQPLUSPLUS</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L3277–3337  
**Auto-fixable:** No

**Description:**  
Process 'PRINSEQPLUSPLUS' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

**Recommendation:**
```
Add a memory directive sized for the tool's peak usage:
    memory '8 GB'

For resilient pipelines, combine with an error strategy that increases memory on retry:
    errorStrategy 'retry'
    maxRetries 2
    memory { (8.GB * task.attempt).clamp(null, 32.GB) }
```

</details>

<details><summary>🔴 <strong>184. CONTAINER-001 — SAMTOOLS_FASTQ</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L3341–3400  
**Auto-fixable:** Yes

**Description:**  
Process 'SAMTOOLS_FASTQ' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟠 <strong>185. STORAGE-001 — SAMTOOLS_FASTQ</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L3341–3400  
**Auto-fixable:** No

**Description:**  
Process 'SAMTOOLS_FASTQ' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
//, /Using., //
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>186. RESOURCE-001 — SAMTOOLS_FASTQ</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L3341–3400  
**Auto-fixable:** No

**Description:**  
Process 'SAMTOOLS_FASTQ' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

**Recommendation:**
```
Add a cpus directive appropriate for the tool's parallelism:
    cpus 4

Reference the allocation in the script block so the tool actually uses the provisioned cores:
    bwa mem -t ${task.cpus} ...

For workflows that need to scale, consider a dynamic expression:
    cpus { reads.size() > 5.GB ? 8 : 4 }
```

</details>

<details><summary>🟡 <strong>187. RESOURCE-002 — SAMTOOLS_FASTQ</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L3341–3400  
**Auto-fixable:** No

**Description:**  
Process 'SAMTOOLS_FASTQ' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

**Recommendation:**
```
Add a memory directive sized for the tool's peak usage:
    memory '8 GB'

For resilient pipelines, combine with an error strategy that increases memory on retry:
    errorStrategy 'retry'
    maxRetries 2
    memory { (8.GB * task.attempt).clamp(null, 32.GB) }
```

</details>

<details><summary>🔴 <strong>188. CONTAINER-001 — SAMTOOLS_INDEX</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L3404–3452  
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

<details><summary>🟠 <strong>189. STORAGE-001 — SAMTOOLS_INDEX</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L3404–3452  
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

<details><summary>🟡 <strong>190. RESOURCE-001 — SAMTOOLS_INDEX</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L3404–3452  
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

<details><summary>🟡 <strong>191. RESOURCE-002 — SAMTOOLS_INDEX</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L3404–3452  
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

<details><summary>🔴 <strong>192. CONTAINER-001 — SAMTOOLS_STATS</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L3456–3493  
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

<details><summary>🟡 <strong>193. RESOURCE-001 — SAMTOOLS_STATS</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L3456–3493  
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

<details><summary>🟡 <strong>194. RESOURCE-002 — SAMTOOLS_STATS</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L3456–3493  
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

<details><summary>🔴 <strong>195. CONTAINER-001 — SAMTOOLS_VIEW</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L3497–3590  
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

<details><summary>🟠 <strong>196. STORAGE-001 — SAMTOOLS_VIEW</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L3497–3590  
**Auto-fixable:** No

**Description:**  
Process 'SAMTOOLS_VIEW' contains hardcoded absolute paths in its script block. These paths will not exist on cloud execution environments.

**Evidence:**
```
//
```

**Recommendation:**
```
Replace hardcoded paths with Nextflow input parameters. Reference files should be declared in the input: block and passed in via a params file or the workflow's input channel.
```

</details>

<details><summary>🟡 <strong>197. RESOURCE-001 — SAMTOOLS_VIEW</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L3497–3590  
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

<details><summary>🟡 <strong>198. RESOURCE-002 — SAMTOOLS_VIEW</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L3497–3590  
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

<details><summary>🔴 <strong>199. CONTAINER-001 — TAXPASTA_MERGE</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L3594–3651  
**Auto-fixable:** Yes

**Description:**  
Process 'TAXPASTA_MERGE' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟡 <strong>200. RESOURCE-001 — TAXPASTA_MERGE</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L3594–3651  
**Auto-fixable:** No

**Description:**  
Process 'TAXPASTA_MERGE' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

**Recommendation:**
```
Add a cpus directive appropriate for the tool's parallelism:
    cpus 4

Reference the allocation in the script block so the tool actually uses the provisioned cores:
    bwa mem -t ${task.cpus} ...

For workflows that need to scale, consider a dynamic expression:
    cpus { reads.size() > 5.GB ? 8 : 4 }
```

</details>

<details><summary>🟡 <strong>201. RESOURCE-002 — TAXPASTA_MERGE</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L3594–3651  
**Auto-fixable:** No

**Description:**  
Process 'TAXPASTA_MERGE' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

**Recommendation:**
```
Add a memory directive sized for the tool's peak usage:
    memory '8 GB'

For resilient pipelines, combine with an error strategy that increases memory on retry:
    errorStrategy 'retry'
    maxRetries 2
    memory { (8.GB * task.attempt).clamp(null, 32.GB) }
```

</details>

<details><summary>🔴 <strong>202. CONTAINER-001 — TAXPASTA_STANDARDISE</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L3655–3707  
**Auto-fixable:** Yes

**Description:**  
Process 'TAXPASTA_STANDARDISE' has no container directive. It cannot run portably on any WES-compliant cloud platform.

**Recommendation:**
```
Add a container directive with a pinned image, e.g.:
    container 'quay.io/biocontainers/tool:1.0.0'

For Snakemake, use a singularity directive:
    singularity: "docker://quay.io/biocontainers/tool:1.0.0"
```

</details>

<details><summary>🟡 <strong>203. RESOURCE-001 — TAXPASTA_STANDARDISE</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L3655–3707  
**Auto-fixable:** No

**Description:**  
Process 'TAXPASTA_STANDARDISE' has no cpus directive. Cloud schedulers cannot allocate the correct number of CPU cores without an explicit declaration, leading to either over-provisioning (wasted cost) or under-provisioning (slow or failed runs). The tool cannot parallelise itself via ${task.cpus} without this value.

**Recommendation:**
```
Add a cpus directive appropriate for the tool's parallelism:
    cpus 4

Reference the allocation in the script block so the tool actually uses the provisioned cores:
    bwa mem -t ${task.cpus} ...

For workflows that need to scale, consider a dynamic expression:
    cpus { reads.size() > 5.GB ? 8 : 4 }
```

</details>

<details><summary>🟡 <strong>204. RESOURCE-002 — TAXPASTA_STANDARDISE</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L3655–3707  
**Auto-fixable:** No

**Description:**  
Process 'TAXPASTA_STANDARDISE' has no memory directive. Cloud schedulers cannot reserve sufficient RAM without an explicit declaration. Memory-hungry bioinformatics tools (aligners, variant callers) will be killed by OOM errors on instances with inadequate RAM, with no meaningful error message.

**Recommendation:**
```
Add a memory directive sized for the tool's peak usage:
    memory '8 GB'

For resilient pipelines, combine with an error strategy that increases memory on retry:
    errorStrategy 'retry'
    maxRetries 2
    memory { (8.GB * task.attempt).clamp(null, 32.GB) }
```

</details>

<details><summary>🔴 <strong>205. CONTAINER-001 — UNTAR</strong> (CRITICAL)</summary>

**Category:** `containerization`  
**Location:** `main.nf` L3711–3794  
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

<details><summary>🟠 <strong>206. STORAGE-001 — UNTAR</strong> (MAJOR)</summary>

**Category:** `storage`  
**Location:** `main.nf` L3711–3794  
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

<details><summary>🟡 <strong>207. RESOURCE-001 — UNTAR</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L3711–3794  
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

<details><summary>🟡 <strong>208. RESOURCE-002 — UNTAR</strong> (MINOR)</summary>

**Category:** `resource_hints`  
**Location:** `main.nf` L3711–3794  
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