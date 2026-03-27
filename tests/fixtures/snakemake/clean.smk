rule ALIGN:
    singularity:
        "docker://quay.io/biocontainers/bwa:0.7.17--h5bf99c6_8"
    threads: 4
    resources:
        mem_mb = 8000
    input:
        reads = "data/{sample}.fastq.gz",
        ref   = "data/ref.fa"
    output:
        bam = "results/{sample}.bam"
    shell:
        """
        bwa mem -t {threads} {input.ref} {input.reads} > {output.bam}
        """


rule SORT_BAM:
    singularity:
        "docker://quay.io/biocontainers/samtools:1.18--h50ea8bc_1"
    threads: 2
    resources:
        mem_mb = 4000
    input:
        bam = "results/{sample}.bam"
    output:
        sorted_bam = "results/{sample}.sorted.bam"
    shell:
        """
        samtools sort -@ {threads} {input.bam} -o {output.sorted_bam}
        """