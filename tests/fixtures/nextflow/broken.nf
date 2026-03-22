process ALIGN {
    // no container, no cpus, no memory

    input:
        path reads

    script:
        """
        bwa mem /data/ref/hg38.fa ${reads} > /scratch/aligned.bam
        """
}

process CALL_VARIANTS {
    input:
        path bam

    // no output declared at all

    script:
        """
        gatk HaplotypeCaller -I ${bam} -O variants.vcf
        """
}