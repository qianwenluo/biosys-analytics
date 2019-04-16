#!/usr/bin/env python3
"""
Author : qianwenluo
Date   : 2019-04-15
Purpose: Rock the Casbah
"""

import argparse
import sys
import os
from Bio import SeqIO

# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='De Bruijn Graphs in Python',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'positional', metavar='FILE', help='Input FASTA format file')

    parser.add_argument(
        '-k',
        '--overlap',
        help='k overlap',
        metavar='int',
        type=int,
        default=3)



    return parser.parse_args()


# --------------------------------------------------
def warn(msg):
    """Print a message to STDERR"""
    print(msg, file=sys.stderr)


# --------------------------------------------------
def die(msg='Something bad happened'):
    """warn() and exit with error"""
    warn(msg)
    sys.exit(1)

def find_kmers(seq, k):
    kmer_list = []
    for i in range(0, len(seq) - k + 1):
        kmer = seq[i:i + k]
        if kmer not in kmer_list:
            kmer_list.append(kmer)
    return kmer_list

# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()
    kmer = args.overlap
    file = args.positional

    if not os.path.isfile(file):
        die('"{}" is not a file'.format(file))

    if kmer in [0, -1]:
        die('-k "{}" must be a positive integer'.format(kmer))

    start= {}
    end = {}
    for record in SeqIO.parse(file, 'fasta'):
        start[record.id]=str(record.seq[0:kmer])
        end[record.id]=str(record.seq[-kmer:])

    for i in start.keys():
        for j in end.keys():
            if i != j and start[i] == end[j]:
                print(j, i)
        





# --------------------------------------------------
if __name__ == '__main__':
    main()
