
# BIOPROG_SV

<img align="right" src="logo.jpg" alt="MetaFast" width="400"> #Добавить свою картинку

**BioProg_SV** (Biological Programm by Stepnova Valeriya) is a versatile toolkit designed to calculate basic DNA/RNA parameters and validate DNA quality from FastQC data.

Authors:
**Stepanova Valeria** Bioinformatics institute 2024/2025


**BioProg_SV** documentation is available on the GitHub [repo](https://github.com/Stepanovalera/BioProgSV).<br/>


## Content

* [Installation](#installation)
* [Instructions](#instructions)
* [Examples](#examples)
* [Contact](#contact)




## Installation


## Instructions

This program contains main functions:

**filter_fastqc()** - This function processes FastQC output data to filter and validate DNA sequences based on quality metrics. It applies multiple quality criteria to determine which sequences from a given dictionary (seqs) pass the filtering steps. The filtering criteria include:

  *GC Content Bounds*: Only sequences within the specified percentage range are retained. The GC content influences sequence stability and should fall within acceptable bounds for specific analyses. Default paramenter: `gc_bounds = (0, 100)`

  *Length Bounds*: The function checks if sequence lengths are within the specified minimum and maximum values, ensuring that only sequences of appropriate length are included. Default paramenter: `length_bounds = (0, 2**32)`

  *Quality Threshold*: Sequences must exceed a minimum quality score, ensuring that only high-quality data are used for downstream analyses. Default paramenter: `quality_threshold = 0`


  `fast_qc` - The function calculates:
    - GC Content: Percentage of guanine (G) and cytosine (C) in the DNA sequence.
    - Sequence Length: The number of bases in the DNA sequence.
    - Average Quality Score: An average derived from Phred quality scores
      indicating the reliability of the sequence data.


**run_dna_rna_tools()** -This overarching function orchestrates multiple DNA/RNA operations, providing a streamlined interface to process sequences efficiently.

  `reverse()` - Reverses a given nucleotide sequence.
  
  
  `reverse_complement()` - Generates the reverse complement of a DNA sequence.
  
  
  `transcribe()` - Converts a DNA sequence into an RNA sequence by replacing thymine with uracil.
  
  
  `complement()` - Produces the complement of a DNA strand by replacing each nucleotide with its complementary base.
  
  
  `is_none()` -Checks if the given sequence is empty or None. This utility function ensures that subsequent operations are performed only on valid sequences, preventing errors in data processing.
  
  
  `is_DNA()` - Validates whether the provided sequence is a DNA sequence, checking for the presence of valid DNA nucleotides (A, T, C, G).
  
  
  `is_RNA()` - Determines if the sequence is an RNA sequence by verifying the presence of valid RNA nucleotides (A, U, C, G). 
  
Each sequence is processed, and results are collected into a list. If there is only one sequence to process, the function directly returns the single result; otherwise, it returns a `list()`. This design allows the function to handle both individual sequences and batches efficiently, making it suitable for batch processing tasks or single-sequence manipulation.

## Examples

For `run_dna_rna_tools()`:


~~~
    run_dna_rna_tools("ATG", "transcribe") == "AUG"
    run_dna_rna_tools("AGt", "transcribe") == "AGu"
~~~

For `bioprogsv()`:


~~~
EXAMPLE_FASTQ = {
    # 'name' : ('sequence', 'quality')
    '@SRX079801': ('ACAGCAACATAAACATGATGGGATGGCGTAAGCCCCCGAGATATCAGTTTACCCAGGATAAGAGATTAAATTATGAGCAACATTATTAA', 'FGGGFGGGFGGGFGDFGCEBB@CCDFDDFFFFBFFGFGEFDFFFF;D@DD>C@DDGGGDFGDGG?GFGFEGFGGEF@FDGGGFGFBGGD'),
    '@SRX079802': ('ATTAGCGAGGAGGAGTGCTGAGAAGATGTCGCCTACGCCGTTGAAATTCCCTTCAATCAGGGGGTACTGGAGGATACGAGTTTGTGTG', 'BFFFFFFFB@B@A<@D>BDDACDDDEBEDEFFFBFFFEFFDFFF=CC@DDFD8FFFFFFF8/+.2,@7<<:?B/:<><-><@.A*C>D'),
    '@SRX079803': ('GAACGACAGCAGCTCCTGCATAACCGCGTCCTTCTTCTTTAGCGTTGTGCAAAGCATGTTTTGTATTACGGGCATCTCGAGCGAATC', 'DFFFEGDGGGGFGGEDCCDCEFFFFCCCCCB>CEBFGFBGGG?DE=:6@=>A<A>D?D8DCEE:>EEABE5D@5:DDCA;EEE-DCD')}
~~~
## Contact

Also, you can send your feedback to [ukrainskaya49@gmail.com](mailto:ukrainskaya49@gmail.com).







