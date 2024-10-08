with open('/Users/lerastepanova/Documents/bioinf/Python/example_fastq.fastq') as file: # контекстный менеджер
        keys = []
        values = []
        for line in file.readlines():
            line_new = line.strip()
            if line_new.startswith('@SRX'):
                keys.append(line_new)
            elif not line_new.startswith('+SRX'):
                values.append(line_new)
resulting_dict = {keys[i]: (values[2 * i], values[2 * i + 1]) for i in range(len(keys))}      

with open('filtered.fastq', 'w') as file:
    file.write('Это первая строка.\n')
    file.write('Это вторая строка.\n')

