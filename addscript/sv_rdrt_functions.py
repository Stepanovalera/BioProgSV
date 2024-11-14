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


def is_none(val, results):   # is None
    if val is not None:
        results.append(val)


def reverse(seq):
    if is_dna(seq) or is_rna(seq):
        return seq[::-1]


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
