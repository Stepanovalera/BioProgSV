
from addscript.sv_rdrt_functions import transcribe, reverse, complement, reverse_complement, is_none
from addscript.fastq_qc_function import fast_qc

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


def filter_fastq(seqs, gc_bounds = (0, 100),
                 length_bounds = (0, 2**32),
                 quality_threshold = 0):
    """
    Parameters:
    - seqs dict[str, tuple[str, str]: A
        dictionary where each key is a sequence name and each value
      is a tuple containing the DNA sequence (str)
        and its quality string (str).
    - gc_bounds(tuple):
    - length_bounds(tuple):
    - quality_threshold(float):

    Returns:
    - filtered_fastq(dict[str: tuple(str, str)]):
        A dictionary of filtered sequences in the format:
      {sequence_name: (sequence, quality_string)}.
    """
    if isinstance(gc_bounds, (int)):
        gc_bounds = (0, gc_bounds)
    if isinstance(length_bounds, (int)):
        length_bounds = (0, length_bounds)
    filtered_fastq = {}
    filtered_data = fast_qc(seqs)
    for sequence_name, (gc, length, quality) in filtered_data.items():
        if (gc_bounds[0] <= gc <= gc_bounds[1]) and \
           (length_bounds[0] <= length <= length_bounds[1]) and \
           (quality >= float(quality_threshold)):
            filtered_fastq[sequence_name] = seqs[sequence_name]
    return filtered_fastq
