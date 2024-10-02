# Создадим словарь DNA
DNA = {'a': 't', 'A': 'T',
       'g': 'c', 'G': 'C',
       'c': 'g', 'C': 'G',
       't': 'a', 'T': 'A'
       }
# Создадим словарь RNA
RNA = {'a': 'u', 'A': 'U',
       'g': 'c', 'G': 'C',
       'c': 'g', 'C': 'G',
       'u': 'a', 'U': 'A'
       }


def is_dna(seq):    # проверка DNA это или нет
    return set(seq).issubset(DNA.keys())


def is_rna(seq):    # проверка RNA это или нет
    return set(seq).issubset(RNA.keys())


def run_dna_rna_tools(*seqs):   # функция main
    results = []
    action = seqs[-1]
    seqs = seqs[0:-1]
    for seq in seqs:
        if action == "transcribe":
            val = test_transcribe(seq)
            if val is not None:
                results.append(val)
        elif action == "reverse":
            val = test_reverse(seq)
            if val is not None:
                results.append(val)
        elif action == "complement":
            val = test_complement(seq)
            if val is not None:
                results.append(val)
        elif action == "reverse_complement":
            val = test_reverse_complement(seq)
            if val is not None:
                results.append(val)
    if len(results) == 1:
        return results[0]
    else:
        return results


def test_reverse(seq):
    if is_dna(seq) or is_rna(seq):
        result = seq[::-1]
        return result


def test_complement(seq):
    result = ' '
    if is_rna(seq):
        for n in seq:
            result += RNA[n]
        return result
    elif is_dna(seq):
        for n in seq:
            result += DNA[n]
        return result


def test_reverse_complement(seq):
    result = test_complement(seq)
    result = test_reverse(result)
    return result


def test_transcribe(seq):
    if is_dna(seq):
        result = seq.replace('T', 'U').replace('t', 'u')
        return result
