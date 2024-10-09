import os

def convert_multiline_fasta_to_oneline(input_fasta, output_fasta):
    base_directory = os.path.dirname(input_fasta)
    output_fasta = base_directory + '/' + output_fasta
    print(output_fasta)
    with open(output_fasta, 'w') as out_file:
        with open(input_fasta, 'r') as in_file:
            sequence = ""
            for line in in_file:
                line = line.strip()
                if line.startswith('>'):
                    if sequence:
                        out_file.write(sequence + '\n')
                        sequence = ""
                    out_file.write(line + '\n')
                else:
                    sequence += line
            if sequence:
                out_file.write(sequence + '\n')
    return output_fasta

def parse_blast_output(input_file, output_file):
    pass

def select_genes_from_gbk_to_fasta(input_gbk, genes, n_before, n_after, output_fasta):
    pass


#file = convert_multiline_fasta_to_oneline('/Users/lerastepanova/Downloads/example_multiline_fasta.fasta','1.fasta')
