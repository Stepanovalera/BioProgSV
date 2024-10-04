def fast_qc(seqs):
    """
    Parameters:
    - seqs (dict): A dictionary where each key
      is a sequence name and each value
      is a tuple containing the DNA
      sequence (str) and its quality string (str).

    Returns:
    - dict[str, tuple[float, int, float]: A dictionary
    with sequence names as keys and a tuple as values.
    Each tuple contains:
      * GC content (tuple): The percentage of 'G'
        and 'C' bases in the sequence.
      * Length (tuple): The length of the DNA sequence.
      * Average quality score (float):
        The mean quality score derived from the
          quality string.

    The function calculates:
    - GC Content: Percentage of guanine (G)
        and cytosine (C) in the DNA sequence.
    - Sequence Length: The number of bases in the DNA sequence.
    - Average Quality Score: An average derived from Phred quality scores
      indicating the reliability of the sequence data.
    """
    gc_len_q = {}
    quality_scores = []
    for sequence_name, (sequence, quality) in seqs.items():
        gc_count = (sequence.count('G') + sequence.count('C'))/len(sequence) * 100
        quality_scores = [ord(char) - 33 for char in quality]
        average_quality = sum(quality_scores) / len(quality_scores) if quality_scores else 0
        length = float(len(sequence))
        gc_len_q[sequence_name] = (gc_count, length, average_quality)
    return gc_len_q
