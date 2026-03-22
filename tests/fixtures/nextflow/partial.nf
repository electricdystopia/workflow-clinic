process TRIM {
    container 'quay.io/biocontainers/trimmomatic:latest'  // latest tag — bad
    cpus 2
    // memory missing

    input:
        path reads

    output:
        path "*.trimmed.fastq"

    script:
        """
        trimmomatic SE ${reads} output.trimmed.fastq
        """
}

process FASTQC {
    // no container
    cpus 1
    memory '2 GB'

    input:
        path reads

    output:
        path "*.html"

    script:
        """
        fastqc ${reads}
        """
}