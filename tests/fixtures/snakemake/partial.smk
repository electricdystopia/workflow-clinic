rule TRIM:
    conda: "envs/trimmomatic.yaml"  # unpinned conda env — no singularity
    threads: 2
    # mem_mb missing
    input:
        reads = "data/{sample}.fastq.gz"
    output:
        trimmed = "results/{sample}.trimmed.fastq.gz"
    shell:
        """
        trimmomatic SE {input.reads} {output.trimmed}
        """


rule FASTQC:
    # no singularity, no conda at all
    threads: 1
    resources:
        mem_mb = 2000
    input:
        reads = "data/{sample}.fastq.gz"
    output:
        html = "results/{sample}_fastqc.html"
    shell:
        """
        fastqc {input.reads} -o results/
        """