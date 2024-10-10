import os
import re

def convert_multiline_fasta_to_oneline(input_fasta, output_fasta):
    base_directory = os.path.dirname(input_fasta)
    output_fasta = base_directory + '/' + output_fasta
    with open(output_fasta, 'w') as out_file:
        with open(input_fasta) as in_file:
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


def select_genes_from_gbk_to_fasta(input_gbk, output_fasta, genes, n_before=1, n_after=1):
    base_directory = os.path.dirname(input_gbk)
    output_fasta = base_directory + '/' + output_fasta
    with open(output_fasta, 'w') as fasta_file:
        with open(input_gbk) as gbk_file:
            recording = False
            translation_lines = []
            for line in gbk_file:
                if line.startswith('                     /gene='):
                    gene_name = line.split('"')[1]
                    if any(gene_name in s for s in genes):
                        recording = True
                        translation_lines = []
                        fasta_file.write('>' + gene_name + '\n')
                    else:
                        recording = False
                if recording:
                    if line.startswith('                     /translation='):
                        line_translation = line.strip().split('"')[1]
                        translation_lines.append(line_translation)
                    elif line.startswith('                     ') and not line.startswith('                     /'):
                        line_translation = line.strip().strip('"')
                        if line_translation:
                            translation_lines.append(line_translation)
                if line.startswith('     CDS') and translation_lines:
                    fasta_file.write(''.join(translation_lines) + '\n')
                    translation_lines = []
                    recording = False
    return output_fasta
