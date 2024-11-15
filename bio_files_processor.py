import os


def convert_multiline_fasta_to_oneline(input_fasta: str, output_fasta: str) -> str:
    '''
    Parameters:
    input_fasta (str): Path to the input FASTA file.
    output_fasta (str): output FASTA file name

    Returns:
    str: Path to the generated output FASTA file.
    '''
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


def parse_blast_output(input_blast: str, output_blast: str) -> str:
    '''
    Parameters:
    input_blast (str): Path to the input BLAST output file.
    output_blast (str): file name

    Returns:
    str: Path to the generated output file containing parsed descriptions.
    '''
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


def select_genes_from_gbk_to_fasta(
    input_gbk: str, 
    output_fasta: str, 
    genes: list[str], 
    n_before: int = 1, 
    n_after: int = 1
) -> str:
    '''
    Parameters:
    input_gbk (str): Path to the input GenBank file.
    output_fasta (str): output FASTA file name.
    genes (list of str): Names of the target genes for which 
    adjacent sequences are extracted.
    n_before (int, optional): Number of genes to include 
    before each target gene. Defaults to 1.
    n_after (int, optional): Number of genes to include 
    after each target gene. Defaults to 1.

    Returns:
    str: Path to the generated FASTA file containing 
    neighboring gene sequences.
    '''
    base_directory = os.path.dirname(input_gbk)
    output_fasta = os.path.join(base_directory, output_fasta)
    gene_to_translation = {}
    with open(input_gbk) as gbk_file:
        recording = False
        current_gene = None
        translation_lines = []
        for line in gbk_file:
            if line.startswith('                     /gene='):
                current_gene = line.split('"')[1]
                gene_to_translation[current_gene] = ''
                recording = True
            if recording:
                if line.startswith('                     /translation='):
                    line_translation = line.strip().split('"')[1]
                    translation_lines.append(line_translation)
                elif line.startswith('                     ') and not line.startswith('                     /'):
                    line_translation = line.strip().strip('"')
                    if line_translation:
                        translation_lines.append(line_translation)
            if line.startswith('     CDS') and current_gene is not None:
                if translation_lines:
                    gene_to_translation[current_gene] = ''.join(translation_lines)
                current_gene = None
                translation_lines = []
                recording = False
    with open(output_fasta, 'w') as fasta_file:
        genes_found = list(gene_to_translation.keys())
        for index, gene_name in enumerate(genes_found):
            if any(gene_name == s for s in genes):
                start_index = max(0, index - n_before)
                end_index = min(len(genes_found), index + n_after + 1)
                for i in range(start_index, end_index):
                    if i == index:
                        continue
                    gene = genes_found[i]
                    sequence = gene_to_translation[gene]
                    fasta_file.write(f'>{gene}\n')
                    fasta_file.write(sequence + '\n')
    return output_fasta
