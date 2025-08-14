# fasta2psiblast

## Description

Convert fasta MSA to format suitable for PSIBLAST (see below).

## Usage

    $ ./fasta2psiblast.py <input_file>

## Options

Positional arguments:

    input_file   Input file with multiple sequence alignment in FASTA format.

Options:

    -b BLOCK_SIZE, --block-size BLOCK_SIZE
                   Block size for the output alignment. (default: 60)
    -h, --help     Show help message and exit
    -v, --version  Show program's version number and exit.

## Multiple sequence alignment format for PSIBLAST

See example file [out.msa](out.msa).

From <https://www.ncbi.nlm.nih.gov/books/NBK569842>:

>The `-in_msa` psiblast option provides a way to jump start psiblast from a
>master-slave multiple sequence alignment computed outside psiblast. The
>multiple sequence alignment must contain the query sequence as one of its
>sequences, but it need not be the first sequence. The multiple sequence
>alignment must be specified in a format that is derived from Clustal, but
>without some headers and trailers (see example below).
>
>The rules are also described by the following words. Suppose the multiple
>sequence alignment has N sequences. It may be presented in one or more blocks,
>where each block presents a range of columns from the multiple sequence
>alignment. E.g., the first block might have columns 1-60, the second block
>might have columns 61-95, the third block might have columns 96-128. Each block
>should have N rows, one row per sequence. The sequences should be in the same
>order in every block. Blocks are separated by one or more black lines. Within a
>block there are no blank lines, and each line consists of one sequence
>identifier followed by some whitespace followed by characters (and gaps) for
>that sequence in the multiple sequence alignment. In each column, all letters
>must be in upper case, or all letters must be in lower case.

## License and Copyright

Copyright (C) 2025 Johan Nylander johan.nylander@nrm.se.
Distributed under terms of the MIT license.
