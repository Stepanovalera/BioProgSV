#  DNA
DNA = {'a': 't', 'A': 'T',
       'g': 'c', 'G': 'C',
       'c': 'g', 'C': 'G',
       't': 'a', 'T': 'A'
       }
#  RNA
RNA = {'a': 'u', 'A': 'U',
       'g': 'c', 'G': 'C',
       'c': 'g', 'C': 'G',
       'u': 'a', 'U': 'A'
       }


def is_dna(seq):    # is DNA 
    return set(seq).issubset(DNA.keys())


def is_rna(seq):    # is RNA 
    return set(seq).issubset(RNA.keys())


def run_dna_rna_tools(*args):   #  main
    results = []
    *seqs, action = args
    for seq in seqs:
        if action == "transcribe":
            val = transcribe(seq)
            if val is not None:
                results.append(val)
        elif action == "reverse":
            val = reverse(seq)
            if val is not None:
                results.append(val)
        elif action == "complement":
            val = complement(seq)
            if val is not None:
                results.append(val)
        elif action == "reverse_complement":
            val = reverse_complement(seq)
            if val is not None:
                results.append(val)
    if len(results) == 1:
        return results[0]
    else:
        return results


def reverse(seq):
    if is_dna(seq) or is_rna(seq):
        result = seq[::-1]
        return result


def complement(seq):
    result = ''
    if is_rna(seq):
        for n in seq:
            result += RNA[n]
        return result
    elif is_dna(seq):
        for n in seq:
            result += DNA[n]
        return result


def reverse_complement(seq):
    return reverse(complement(seq))


def transcribe(seq):
    if is_dna(seq):
        result = seq.replace('T', 'U').replace('t', 'u')
        return result
