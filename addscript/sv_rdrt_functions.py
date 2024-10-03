

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