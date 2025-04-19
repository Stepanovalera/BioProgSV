# BioProg_SV

**BioProg_SV** (Biological Program by Stepnova Valeriya) is a toolkit designed for performing basic DNA/RNA sequence analysis and filtering FASTQ data based on quality metrics. The toolset includes functions for sequence transformation, filtering, and analysis.

---

## Authors

- **Stepanova Valeriya**  
  Bioinformatics Institute, 2024–2025

Documentation is available in the GitHub repository: [Repository Link](https://github.com/your-repo-link).

---

## Table of Contents

1. [Instructions](#instructions)
2. [Function Descriptions](#function-descriptions)
3. [Usage Examples](#usage-examples)
4. [Contact](#contact)

---

## Instructions

### Installing Dependencies

If the project uses third-party libraries, install them using the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

If the file is empty, it means the project only uses Python's standard libraries.

### Running the Program

The program supports two main modes of operation:

1. **DNA/RNA Sequence Analysis**:
   ```bash
   python main.py dna_rna_tools --seqs "ATG" --action transcribe
   ```

2. **FASTQ File Filtering**:
   ```bash
   python main.py filter_fastq input.fastq output.fastq --gc_bounds 50 60 --length_bounds 50 100 --quality_threshold 30
   ```

---

## Function Descriptions

### 1. `filter_fastq`

This function filters sequences from a FASTQ file based on specified quality criteria.

#### Parameters:
- `input_fastq` (str): Path to the input FASTQ file.
- `output_fastq` (str): Path to the output FASTQ file.
- `gc_bounds` (tuple or int): GC content bounds (default: `(0, 100)`). If a single number is provided, it is treated as the upper bound.
- `length_bounds` (tuple or int): Sequence length bounds (default: `(0, 2**32)`). If a single number is provided, it is treated as the upper bound.
- `quality_threshold` (float): Minimum average quality score required for sequences to be included (default: `0.0`).

#### Returns:
- A filtered FASTQ file containing sequences that meet the specified criteria.

---

### 2. `fast_qc`

This function calculates quality metrics for DNA/RNA sequences.

#### Metrics Calculated:
- **GC Content**: Percentage of guanine (G) and cytosine (C) in the sequence.
- **Sequence Length**: Number of bases in the sequence.
- **Average Quality Score**: Mean quality score derived from Phred quality scores.

#### Parameters:
- `seqs` (dict): A dictionary where keys are sequence names, and values are tuples containing the sequence (str) and its quality string (str).

#### Returns:
- A dictionary with sequence names as keys and tuples as values. Each tuple contains:
  - GC content (float)
  - Sequence length (int)
  - Average quality score (float)

---

### 3. `convert_multiline_fasta_to_oneline`

Converts a multi-line FASTA file into a single-line format.

#### Parameters:
- `input_fasta` (str): Path to the input FASTA file.
- `output_fasta` (str): Path to the output FASTA file.

#### Returns:
- A FASTA file where each sequence is represented as a single line.

---

### 4. `parse_blast_output`

Parses BLAST output files to extract relevant sequence descriptions.

#### Parameters:
- `input_blast` (str): Path to the input BLAST output file.
- `output_blast` (str): Path to the output file for parsed results.

#### Returns:
- A file containing truncated descriptions of sequences.

---

### 5. `select_genes_from_gbk_to_fasta`

Extracts neighboring gene sequences from a GenBank (GBK) file.

#### Parameters:
- `input_gbk` (str): Path to the input GenBank file.
- `output_fasta` (str): Path to the output FASTA file.
- `genes` (list): List of target gene names.
- `n_before` (int, optional): Number of genes before the target gene to include (default: `1`).
- `n_after` (int, optional): Number of genes after the target gene to include (default: `1`).

#### Returns:
- A FASTA file containing sequences of neighboring genes.

---

### 6. `run_dna_rna_tools`

Performs various DNA/RNA operations, including transcription, reverse complementation, and more.

#### Supported Actions:
- `transcribe`: Converts DNA to RNA.
- `reverse`: Reverses a sequence.
- `complement`: Generates the complement of a DNA sequence.
- `reverse_complement`: Generates the reverse complement of a DNA sequence.

#### Parameters:
- `seqs` (list): List of DNA/RNA sequences.
- `action` (str): Action to perform (e.g., `"transcribe"`, `"reverse"`).

#### Returns:
- A single sequence (if one input) or a list of processed sequences.

---

## Usage Examples

### Example 1: DNA/RNA Tools

```python
# Transcribe DNA to RNA
run_dna_rna_tools(["ATG"], "transcribe")  # Output: ["AUG"]

# Reverse a sequence
run_dna_rna_tools(["AGT"], "reverse")  # Output: ["TGA"]

# Generate reverse complement
run_dna_rna_tools(["GTGT"], "reverse_complement")  # Output: ["ACAC"]
```

### Example 2: FASTQ Filtering

```python
# Filter sequences based on length
filter_fastq("input.fastq", "output.fastq", length_bounds=(50, 100))

# Filter sequences based on GC content and quality
filter_fastq("input.fastq", "output.fastq", gc_bounds=(50, 60), quality_threshold=30)
```

---

## Contact

For questions, feedback, or suggestions, please contact:

- Email: ukrainskaya49@gmail.com

---

