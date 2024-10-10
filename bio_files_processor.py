import os

def convert_multiline_fasta_to_oneline(input_fasta, output_fasta):
    base_directory = os.path.dirname(input_fasta)
    output_fasta = base_directory + '/' + output_fasta
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

def parse_blast_output(input_blast, output_blast):
    base_directory = os.path.dirname(input_blast)
    output_blast = base_directory + '/' + output_blast
    with open(output_blast, 'w') as out_file:
        with open(input_blast) as in_file:
            recording = False
            for line in in_file:
                line = line.strip()
                if line.startswith('Description'):
                    recording = True
                    continue
                if recording and line == "":
                    break
                if recording:
                    changed_line = line.split('...')
                    out_file.write(changed_line[0] + '...\n')
    return output_blast

def select_genes_from_gbk_to_fasta(input_gbk, genes, output_fasta, n_before=1, n_after=1):
    base_directory = os.path.dirname(input_gbk)
    output_fasta = base_directory + '/' + output_fasta


#file = convert_multiline_fasta_to_oneline('/Users/lerastepanova/Downloads/example_multiline_fasta.fasta','1.fasta')
#parse_blast_output('/Users/lerastepanova/Downloads/example_blast_results.txt', 'int.txt')