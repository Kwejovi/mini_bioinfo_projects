from Bio import SeqIO
import matplotlib.pyplot as plt
import sys

def gc_skew(sequence, window=50):
    sequence = sequence.upper()
    skew_values = []
    positions = []
    for i in range(0, len(sequence) - window + 1):
        win_seq = sequence[i:i+window]
        g = win_seq.count("G")
        c = win_seq.count("C")
        skew = (g - c) / (g + c) if (g + c) != 0 else 0
        skew_values.append(skew)
        positions.append(i + window//2)
    return positions, skew_values

def main():
    if len(sys.argv) < 2:
        print("Usage: python gc_skew_plotter.py <fasta_file> [window_size]")
        sys.exit(1)
    fasta_file = sys.argv[1]
    window = int(sys.argv[2]) if len(sys.argv) > 2 else 50

    for record in SeqIO.parse(fasta_file, "fasta"):
        pos, skew = gc_skew(str(record.seq), window)
        plt.plot(pos, skew, label=record.id)

    plt.xlabel("Position")
    plt.ylabel("GC Skew")
    plt.title(f"GC Skew Plot (window={window})")
    plt.legend()
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
