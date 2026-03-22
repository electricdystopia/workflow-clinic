process ALIGN {
    container 'quay.io/biocontainers/bwa:0.7.17'
    cpus 4
    memory '8 GB'

    input:
        path reads
        path reference

    output:
        path "*.bam"

    script:
        """
        bwa mem -t ${task.cpus} ${reference} ${reads} > aligned.bam
        """
}

process SORT_BAM {
    container 'quay.io/biocontainers/samtools:1.18'
    cpus 2
    memory '4 GB'

    input:
        path bam

    output:
        path "*.sorted.bam"

    script:
        """
        samtools sort -@ ${task.cpus} ${bam} -o sorted.bam
        """
}