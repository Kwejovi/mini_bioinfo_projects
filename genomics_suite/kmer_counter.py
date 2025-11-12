from Bio import SeqIO
from collections import Counter
import sys

def count_kmers(fasta_file, k):
    kmers = Counter()
    for record in SeqIO.parse(fasta_file, "fasta"):
        seq = str(record.seq).upper()
        for i in range(len(seq) - k + 1):
            kmer = seq[i:i+k]
            if "N" not in kmer:  # skip ambiguous bases
                kmers[kmer] += 1
    return kmers

def main():
    if len(sys.argv) < 3:
        print("Usage: python kmer_counter.py <fasta_file> <k>")
        sys.exit(1)
    fasta_file = sys.argv[1]
    k = int(sys.argv[2])
    kmers = count_kmers(fasta_file, k)
    print(f"Top 10 {k}-mers:")
    for kmer, count in kmers.most_common(10):
        print(f"{kmer}\t{count}")

if __name__ == "__main__":
    main()
