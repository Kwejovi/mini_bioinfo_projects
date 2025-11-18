 Mini Bioinformatics Projects

A practical collection of bioinformatics tools for learning, analysis, and visualization of DNA sequences.  
Each module is self-contained, reproducible, and written in Python using Biopython (and Matplotlib for plots).

 📁 Repository Structure

mini_bioinfo_projects/
│
├── genomics_suite/
│ ├── fasta_quality.py  Module 1: FASTA Quality Report
│ ├── kmer_counter.py Module 2: K-mer Frequency Counter
│ ├── orf_finder.py  Module 3: ORF Finder
│ ├── gc_skew_plotter.py Module 4: GC Skew Plotter
│ ├── alignment_free_compare.py  Module 5: Alignment-Free Genome Comparison
│ └── test_data/
│ ├── sample1.fasta
│ └── sample2.fasta
│
├── environment.yml
├── .gitignore
└── README.md

 Modules Overview

Module 1: FASTA Quality Report
•	Description: Evaluate sequence quality metrics including length, GC content, and ambiguous bases (N).  
•	Usage:
python genomics_suite/fasta_quality.py genomics_suite/test_data/sample1.fasta
Module 2: K-mer Frequency Counter
•	Description: Count all k-length subsequences (k-mers) and report the most frequent ones.
•	Usage:
python genomics_suite/kmer_counter.py genomics_suite/test_data/sample1.fasta 3

Module 3: ORF Finder
•	Description: Detect open reading frames (ORFs) in DNA sequences, outputting start/end positions and sequences.
•	Usage:
python genomics_suite/orf_finder.py genomics_suite/test_data/sample1.fasta

Module 4: GC Skew Plotter
•	Description: Calculate GC skew along a sequence and plot it for visualization.
•	Usage:
python genomics_suite/gc_skew_plotter.py genomics_suite/test_data/sample1.fasta 50

Module 5: Alignment-Free Genome Comparison
•	Description: Compare two sequences using k-mer composition and Jaccard similarity.
•	Usage:
python genomics_suite/alignment_free_compare.py genomics_suite/test_data/sample1.fasta genomics_suite/test_data/sample2.fasta 4

Requirements
•	Python 3.x
•	Biopython: pip install biopython
•	Matplotlib (for Module 4): pip install matplotlib
Or use the Conda environment:
conda env create -f environment.yml
conda activate mini_bioinfo


