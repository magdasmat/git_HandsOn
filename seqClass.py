#!/usr/bin/env python

import sys, re
from argparse import ArgumentParser

def calculate_nucleotide_percentage(sequence):
    sequence = sequence.upper()
    total_length = len(sequence)

    # Count occurrences of each nucleotide
    count_a = sequence.count('A')
    count_c = sequence.count('C')
    count_g = sequence.count('G')
    count_t = sequence.count('T')
    count_u = sequence.count('U')  # For RNA

    # Calculate percentages
    percentage_a = (count_a / total_length) * 100
    percentage_c = (count_c / total_length) * 100
    percentage_g = (count_g / total_length) * 100
    percentage_t = (count_t / total_length) * 100
    percentage_u = (count_u / total_length) * 100

    return {
        'A': percentage_a,
        'C': percentage_c,
        'G': percentage_g,
        'T': percentage_t,
        'U': percentage_u
    }

# Create an ArgumentParser object to handle command line arguments
parser = ArgumentParser(description='Classify a sequence as DNA or RNA and calculate nucleotide percentages')
# Define command line arguments
parser.add_argument("-s", "--seq", type=str, required=True, help="Input sequence")
parser.add_argument("-m", "--motif", type=str, required=False, help="Motif")

# Check if no command line arguments are provided, print help and exit if true
if len(sys.argv) == 1:
    parser.print_help()
    sys.exit(1)

# Parse command line arguments
args = parser.parse_args()

# Convert the input sequence to uppercase
args.seq = args.seq.upper()

# Check if the sequence contains only valid characters (ACGTU)
if re.search('^[ACGTU]+$', args.seq):
    # Check if 'T' is present in the sequence, indicating DNA
    if 'T' in args.seq:
        print('The sequence is DNA')
    # Check if 'U' is present in the sequence, indicating RNA
    elif 'U' in args.seq:
        print('The sequence is RNA')
    # If neither 'T' nor 'U' is present, it can be DNA or RNA
    else:
        print('The sequence can be DNA or RNA')

    # Calculate and print nucleotide percentages
    result = calculate_nucleotide_percentage(args.seq)
    print("\nNucleotide percentages:")
    for nucleotide, percentage in result.items():
        print(f"{nucleotide}: {percentage:.2f}%")
# If the sequence contains characters other than A, C, G, T, or U, it is neither DNA nor RNA
else:
    print("The sequence is not DNA nor RNA")

# Check if a motif is provided as a command line argument
if args.motif:
    # Convert the motif to uppercase
    args.motif = args.motif.upper()
    # Print a message indicating motif search is enabled
    print(f'Motif search enabled: looking for motif "{args.motif}" in sequence "{args.seq}"... ', end='')
    # Check if the motif is found in the sequence
    if re.search(args.motif, args.seq):
        print("FOUND")
    else:
        print("NOT FOUND")
