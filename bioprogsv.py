
from addscript.sv_rdrt_functions import (transcribe,
                                         reverse,
                                         complement,
                                         reverse_complement,
                                         is_none)
from addscript.fastq_qc_function import fast_qc
from addscript.fastq_read_write_file import read_fastq, write_fastq


def run_dna_rna_tools(*args):

    """
    Parameters:
    *args (list): list of seqs(list) and action(str)

    Returns:
    result (list or str): A list of DNA/RNA
        sequences or single DNA/RNA sequence

    Module:
    is_none - checking is value None or not
    """
    results = []
    *seqs, action = args
    for seq in seqs:
        if action == "transcribe":
            val = transcribe(seq)
            is_none(val, results)
        elif action == "reverse":
            val = reverse(seq)
            is_none(val, results)
        elif action == "complement":
            val = complement(seq)
            is_none(val, results)
        elif action == "reverse_complement":
            val = reverse_complement(seq)
            is_none(val, results)
    if len(results) == 1:
        return results[0]
    else:
        return results


def filter_fastq(
    input_fastq: str, 
    output_fastq: str, 
    gc_bounds: tuple[int, int] = (0, 100), 
    length_bounds: tuple[int, int] = (0, 2**32), 
    quality_threshold: float = 0.0
) -> str:
    """
    Parameters:
    input_fastq (str): Path to the input FASTQ file.
    output_fastq (str): filtered FASTQ file name.
    gc_bounds (tuple of int or int): Bounds for GC content filtering; 
    if an int, used as an upper bound.
    length_bounds (tuple of int or int): Bounds for sequence length filtering; 
    if an int, used as an upper bound.
    quality_threshold (float): Minimum quality score required for sequences to be included.

    Returns:
    str: Path to the generated FASTQ file containing the filtered sequences.
    """
    if isinstance(gc_bounds, (int)):
        gc_bounds = (0, gc_bounds)
    if isinstance(length_bounds, (int)):
        length_bounds = (0, length_bounds)
    input_fastq_data, filtered_directory = read_fastq(input_fastq)
    output_fastq = filtered_directory + '/' + output_fastq
    data_param = fast_qc(input_fastq_data)
    output_fastq_data = {}
    for sequence_name, (gc, length, quality) in data_param.items():
        if (gc_bounds[0] <= gc <= gc_bounds[1]) and \
           (length_bounds[0] <= length <= length_bounds[1]) and \
           (quality >= float(quality_threshold)):
            output_fastq_data[sequence_name] = input_fastq_data[sequence_name]
    return write_fastq(output_fastq_data, output_fastq)
