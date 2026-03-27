rule ALIGN:
    # no singularity, no resources, no threads
    input:
        reads = "data/{sample}.fastq.gz"
    shell:
        """
        bwa mem /data/ref/hg38.fa {input.reads} > /scratch/aligned.bam
        """


rule CALL_VARIANTS:
    input:
        bam = "results/{sample}.bam"

    # no output declared at all

    shell:
        """
        gatk HaplotypeCaller -I {input.bam} -O variants.vcf
        """