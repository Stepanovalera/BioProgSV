
import os
def read_fastq(input_fastq):
    base_directory = os.path.dirname(input_fastq)
    if not os.path.exists(base_directory):
        filtered_directory = os.path.join(base_directory, 'filtered')
        if not os.path.exists(filtered_directory):
            os.makedirs(filtered_directory)
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
    return input_fastq_data, filtered_directory


def write_fastq(output_fastq_data, output_fastq):
    with open(output_fastq, 'w') as file:
        for sequence_id, (sequence_fastq, quality_fastq) in output_fastq_data.items():
                    file.write(sequence_id + '\n')
                    file.write(output_fastq.items(sequence_fastq + '\n'))
                    file.write(output_fastq.items('+' + sequence_id[1:] + '\n'))
                    file.write(output_fastq.items(quality_fastq + '\n'))
    return output_fastq