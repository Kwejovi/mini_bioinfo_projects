from Bio import SeqIO
import sys

def fasta_quality_report(fasta_file):
    print("ID\tLength\tGC(%)\tN_count")
    for record in SeqIO.parse(fasta_file, "fasta"):
        seq = record.seq.upper()
        gc = (seq.count("G") + seq.count("C")) / len(seq) * 100
        n_count = seq.count("N")
        print(f"{record.id}\t{len(seq)}\t{gc:.2f}\t{n_count}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python fasta_quality.py <fasta_file>")
        sys.exit(1)
    fasta_quality_report(sys.argv[1])
