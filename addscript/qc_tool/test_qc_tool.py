import unittest
import os
from qc_tool.fastq_read_write_file  import  read_fastq, write_fastq
from qc_tool.fastq_qc_function  import  fast_qc

class TestFastQC(unittest.TestCase):
    def test_gc_content(self):
        seqs = {"seq1": ("AGCTGCTA", "IIIIIIII")}
        result = fast_qc(seqs)
        self.assertAlmostEqual(result["seq1"][0], 50.0)  # GC content is 50%

    def test_sequence_length(self):
        seqs = {"seq1": ("AGCTGCTA", "IIIIIIII")}
        result = fast_qc(seqs)
        self.assertEqual(result["seq1"][1], 8)  # Length is 8

    def test_average_quality(self):
        seqs = {"seq1": ("AGCTGCTA", "IIIIIIII")}
        result = fast_qc(seqs)
        self.assertAlmostEqual(result["seq1"][2], 40.0)  # Average quality is 40

    def test_empty_sequence(self):
        seqs = {"seq1": ("", "")}
        result = fast_qc(seqs)
        self.assertEqual(result["seq1"], (0.0, 0, 0.0))  # Empty sequence

    def test_read_fastq(self):
        with open("test.fastq", "w") as f:
            f.write("@seq1\nAGCTGCTA\n+\nIIIIIIII\n")
        seqs, _ = read_fastq("test.fastq")
        self.assertEqual(seqs, {"@seq1": ("AGCTGCTA", "IIIIIIII")})
        os.remove("test.fastq")

    def test_write_fastq(self):
        data = {"@seq1": ("AGCTGCTA", "IIIIIIII")}
        write_fastq(data, "output.fastq")
        with open("output.fastq") as f:
            content = f.read()
        expected = "@seq1\nAGCTGCTA\n+seq1\nIIIIIIII\n"
        self.assertEqual(content, expected)
        os.remove("output.fastq")

    def test_invalid_file(self):
        with self.assertRaises(FileNotFoundError):
            read_fastq("nonexistent.fastq")

    def test_logging(self):
        import logging
        logger = logging.getLogger(__name__)
        with self.assertLogs(logger, level='INFO') as log:
            logger.info("Test log message")
            self.assertIn("INFO:Test log message", log.output[0])

if __name__ == "__main__":
    unittest.main()