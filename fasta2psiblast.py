#! /usr/bin/env python3
# vim:fenc=utf-8
#
# Copyright © 2025 nylander <johan.nylander@nrm.se>
#
# Distributed under terms of the MIT license.

"""

Read a fasta formatted file and write a multiple sequence file according to the
specifications in the PSIBLAST manual
(https://www.ncbi.nlm.nih.gov/books/NBK569842/).

"""

import sys
import argparse

VERSION = "0.1.0"

def read_fasta(file):
    """Read a FASTA file and return a list of sequences as tuples (header, sequence)."""
    sequences = []
    header = None
    sequence = []

    for line in file:
        line = line.strip()
        if not line:
            continue  # Skip empty lines
        if line.startswith('>'):
            if header is not None:
                sequences.append((header, ''.join(sequence)))
            header = line[1:]  # Remove '>'
            sequence = []
        else:
            sequence.append(line)

    if header is not None:
        sequences.append((header, ''.join(sequence)))

    return sequences

def write_msa(sequences, block_size=60):
    """
    Write the sequences in a multiple sequence alignment format suitable for PSIBLAST.
    """
    if not sequences:
        print("No sequences found.")
        return

    max_length = max(len(seq) for _, seq in sequences)

    blocks = []

    for start in range(0, max_length, block_size):
        end = min(start + block_size, max_length)
        block = []
        for header, seq in sequences:
            # Pad the sequence with white space if it's shorter than the current block size
            padded_seq = seq[start:end].ljust(block_size, ' ')
            block.append(f"{header}\t{padded_seq}")
        blocks.append(block)

    for i, block in enumerate(blocks):
        if i > 0:
            print()
        for line in block:
            print(line)

def main():
    """
    Main function to parse arguments and execute the conversion.
    """
    parser = argparse.ArgumentParser(
        description="Convert a FASTA file to a multiple sequence alignment format suitable for PSIBLAST.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument(
        "input_file",
        type=argparse.FileType('r'),
        help="Input FASTA file."
    )
    parser.add_argument(
        "-b", "--block-size",
        type=int,
        default=60,
        help="Block size for the output alignment."
    )
    parser.add_argument(
        "-v", "--version",
        action="version",
        version=f"%(prog)s {VERSION}",
        help="Show program's version number and exit."
    )
    args = parser.parse_args()
    input_file = args.input_file
    block_size = args.block_size
    sequences = read_fasta(input_file)
    write_msa(sequences, block_size)

if __name__ == "__main__":
    main()
