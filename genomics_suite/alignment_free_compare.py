from Bio import SeqIO
import sys

def kmer_set(seq, k):
    seq = seq.upper()
    kmers = set()
    for i in range(len(seq) - k + 1):
        kmer = seq[i:i+k]
        if "N" not in kmer:
            kmers.add(kmer)
    return kmers

def jaccard_similarity(set1, set2):
    intersection = len(set1 & set2)
    union = len(set1 | set2)
    return intersection / union if union != 0 else 0

def main():
    if len(sys.argv) < 4:
        print("Usage: python alignment_free_compare.py <fasta_file1> <fasta_file2> <k>")
        sys.exit(1)
    
    fasta1 = sys.argv[1]
    fasta2 = sys.argv[2]
    k = int(sys.argv[3])
    
    seq1 = next(SeqIO.parse(fasta1, "fasta")).seq
    seq2 = next(SeqIO.parse(fasta2, "fasta")).seq
    
    kmers1 = kmer_set(seq1, k)
    kmers2 = kmer_set(seq2, k)
    
    sim = jaccard_similarity(kmers1, kmers2)
    print(f"Jaccard similarity ({k}-mers) = {sim:.4f}")

if __name__ == "__main__":
    main()
