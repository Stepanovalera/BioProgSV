

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

def is_none(val, results): # is None
    if val is not None:
        results.append(val)


