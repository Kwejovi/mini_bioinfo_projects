import sys

def read_fasta(path):
    sequence = []
    with open(path, 'r') as f:
        for line in f:
            line = line.strip()
            if not line.startswith(">"):
                sequence.append(line)
    return "".join(sequence)

def calculate_gc(sequence):
    if len(sequence) == 0:
        return 0
    g = sequence.count("G")
    c = sequence.count("C")
    gc_percent = ((g + c) / len(sequence)) * 100
    return gc_percent

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python gc_content.py <input.fasta> <output.txt>")
        sys.exit(1)

    fasta_file = sys.argv[1]
    output_file = sys.argv[2]

    seq = read_fasta(fasta_file)
    gc = calculate_gc(seq)

    with open(output_file, 'w') as out:
        out.write(f"Sequence length: {len(seq)}\n")
        out.write(f"GC content: {gc:.2f}%\n")

    print(f"GC content calculated. Output saved to {output_file}")
