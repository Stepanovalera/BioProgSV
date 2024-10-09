
def read_fastq(input_fastq):
    with open(input_fastq) as file:
        keys = []
        values = []
        for line in file.readlines():
            line_new = line.strip()
            if line_new.startswith('@SRX'):
                keys.append(line_new)
            elif not line_new.startswith('+SRX'):
                values.append(line_new)
        input_fastq_data = {keys[i]: (values[2 * i], values[2 * i + 1]) for i in range(len(keys))}      
    return input_fastq_data


def write_fastq(output_fastq_data, output_fastq):
    with open(output_fastq, 'w') as file:
        for sequence_id, (sequence_fastq, quality_fastq) in output_fastq_data.items():
                    file.write(sequence_id + '\n')
                    file.write(output_fastq.items(sequence_fastq + '\n'))
                    file.write(output_fastq.items('+' + sequence_id[1:] + '\n'))
                    file.write(output_fastq.items(quality_fastq + '\n'))