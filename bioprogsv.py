
from addscript.sv_rdrt_functions import (transcribe,
                                         reverse,
                                         complement,
                                         reverse_complement,
                                         is_none)
from addscript.qc_tool.fastq_qc_function import fast_qc
from addscript.qc_tool.fastq_read_write_file import read_fastq, write_fastq
import argparse
import logging

def run_dna_rna_tools(*args):

    """
    Parameters:
    *args (list): list of seqs(list) and action(str)

    Returns:
    result (list or str): A list of DNA/RNA
        sequences or single DNA/RNA sequence

    Module:
    is_none - checking is value None or not
    """
    results = []
    *seqs, action = args
    for seq in seqs:
        if action == "transcribe":
            val = transcribe(seq)
            is_none(val, results)
        elif action == "reverse":
            val = reverse(seq)
            is_none(val, results)
        elif action == "complement":
            val = complement(seq)
            is_none(val, results)
        elif action == "reverse_complement":
            val = reverse_complement(seq)
            is_none(val, results)
    if len(results) == 1:
        return results[0]
    else:
        return results


def filter_fastq(
    input_fastq: str, 
    output_fastq: str, 
    gc_bounds: tuple[int, int] | int = (0, 100), 
    length_bounds: tuple[int, int] | int = (0, 2**32), 
    quality_threshold: float = 0.0
) -> str:
    """
    Filters FASTQ sequences based on GC content, length, and quality thresholds.

    Parameters:
    - input_fastq (str): Path to the input FASTQ file.
    - output_fastq (str): Path to the filtered FASTQ file.
    - gc_bounds (tuple[int, int] | int): Bounds for GC content filtering.
      If an integer is provided, it is treated as the upper bound.
    - length_bounds (tuple[int, int] | int): Bounds for sequence length filtering.
      If an integer is provided, it is treated as the upper bound.
    - quality_threshold (float): Minimum average quality score required.

    Returns:
    - str: Path to the generated FASTQ file containing the filtered sequences.
    """

    gc_bounds = (0, gc_bounds) if isinstance(gc_bounds, int) else gc_bounds
    length_bounds = (0, length_bounds) if isinstance(length_bounds, int) else length_bounds
    input_fastq_data, _ = read_fastq(input_fastq)
    qc_results = fast_qc(input_fastq_data)
    filtered_data = {
        seq_name: seq_data
        for seq_name, seq_data in input_fastq_data.items()
        if (
            gc_bounds[0] <= qc_results[seq_name][0] <= gc_bounds[1] and
            length_bounds[0] <= qc_results[seq_name][1] <= length_bounds[1] and
            qc_results[seq_name][2] >= quality_threshold
        )
    }

    write_fastq(filtered_data, output_fastq)
    return output_fastq


# Настройка парсера аргументов
def parse_args():
    parser = argparse.ArgumentParser(description="DNA/RNA tools and FASTQ filtering.")
    subparsers = parser.add_subparsers(dest="command")

    # Парсер для DNA/RNA инструментов
    dna_rna_parser = subparsers.add_parser("dna_rna_tools", help="Perform DNA/RNA transformations.")
    dna_rna_parser.add_argument("--seqs", nargs="+", required=True, help="List of DNA/RNA sequences.")
    dna_rna_parser.add_argument("--action", choices=["transcribe", "reverse", "complement", "reverse_complement"],
                                required=True, help="Action to perform.")

    # Парсер для фильтрации FASTQ
    fastq_parser = subparsers.add_parser("filter_fastq", help="Filter FASTQ sequences.")
    fastq_parser.add_argument("input_fastq", help="Path to the input FASTQ file.")
    fastq_parser.add_argument("output_fastq", help="Path to the filtered FASTQ file.")
    fastq_parser.add_argument("--gc_bounds", nargs=2, type=int, default=(0, 100),
                              help="GC content bounds (min max).")
    fastq_parser.add_argument("--length_bounds", nargs=2, type=int, default=(0, 2**32),
                              help="Sequence length bounds (min max).")
    fastq_parser.add_argument("--quality_threshold", type=float, default=0.0,
                              help="Minimum average quality score.")

    return parser.parse_args()

# Настройка логгирования
def setup_logger(log_file):
    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )
    return logging.getLogger(__name__)

# Основная программа
def main():
    args = parse_args()
    logger = setup_logger("tool.log")

    try:
        if args.command == "dna_rna_tools":
            logger.info("Running DNA/RNA tools...")
            result = run_dna_rna_tools(args.seqs, args.action)
            print(result)
        
        elif args.command == "filter_fastq":
            logger.info("Filtering FASTQ file...")
            output_path = filter_fastq(
                args.input_fastq,
                args.output_fastq,
                gc_bounds=args.gc_bounds,
                length_bounds=args.length_bounds,
                quality_threshold=args.quality_threshold
            )
            logger.info(f"Filtered FASTQ saved to {output_path}")
        
        else:
            logger.error("Unknown command.")
            raise ValueError("Unknown command.")
    
    except Exception as e:
        logger.error(f"An error occurred: {e}")
        raise

if __name__ == "__main__":
    main()
