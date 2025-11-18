from Bio import SeqIO
import sys

START_CODON = "ATG"
STOP_CODONS = ["TAA", "TAG", "TGA"]

def find_orfs(seq, min_len=30):
    seq = seq.upper()
    orfs = []
    for frame in range(3):
        i = frame
        while i < len(seq) - 2:
            codon = seq[i:i+3]
            if codon == START_CODON:
                for j in range(i+3, len(seq)-2, 3):
                    codon2 = seq[j:j+3]
                    if codon2 in STOP_CODONS:
                        orf_seq = seq[i:j+3]
                        if len(orf_seq) >= min_len:
                            orfs.append((i+1, j+3, orf_seq))  # +1 for 1-based indexing
                        i = j + 3
                        break
                else:
                    i += 3
            else:
                i += 3
    return orfs

def main():
    if len(sys.argv) < 2:
        print("Usage: python orf_finder.py <fasta_file>")
        sys.exit(1)

    fasta_file = sys.argv[1]
    for record in SeqIO.parse(fasta_file, "fasta"):
        print(f"Sequence: {record.id}")
        orfs = find_orfs(str(record.seq))
        if not orfs:
            print("  No ORFs found")
        else:
            for start, end, orf_seq in orfs:
                print(f"  ORF: {start}-{end}, Length: {len(orf_seq)}")
                print(f"    {orf_seq}")

if __name__ == "__main__":
    main()
