import os

def read_fastq(input_fastq):
    base_directory = os.path.dirname(input_fastq)
    filtered_directory = os.path.join(base_directory, 'filtered')
    os.makedirs(filtered_directory, exist_ok=True)
    
    input_fastq_data = {}
    with open(input_fastq) as file:
        while True:
            header = file.readline().strip()
            if not header:
                break
            sequence = file.readline().strip()
            _ = file.readline().strip()  # Пропускаем строку '+'
            quality = file.readline().strip()
            input_fastq_data[header] = (sequence, quality)
    
    return input_fastq_data, filtered_directory


def write_fastq(output_fastq_data, output_fastq):
    with open(output_fastq, 'w') as file:
        for sequence_id, (sequence, quality) in output_fastq_data.items():
            file.write(f"{sequence_id}\n")
            file.write(f"{sequence}\n")
            file.write(f"+{sequence_id[1:]}\n")
            file.write(f"{quality}\n")