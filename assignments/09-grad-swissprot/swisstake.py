#!/usr/bin/env python3
"""
Author : qianwenluo
Date   : 2019-03-12
Purpose: Rock the Casbah
"""

import argparse
import sys
import os
from Bio import SeqIO
from Bio import SwissProt



# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Filter Swissprot file for keywords, taxa',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'FILE', metavar='FILE', help='Uniprot file')

    parser.add_argument(
        '-s',
        '--skip',
        help='Skip taxa',
        metavar='STR',
        type=str,
        default='',
        nargs='+')

    parser.add_argument(
        '-k',
        '--keyword',
        help='Take on keyword',
        metavar='STR',
        type=str,
        default='',
        required=True)

    parser.add_argument(
        '-o',
        '--output',
        help='Output filename',
        metavar='FILE',
        type=str,
        default='out.fa')

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


# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()
    skip = args.skip
    keyword = args.keyword.capitalize()
    output = args.output
    input = args.FILE

    skip_upper = [ i.capitalize() for i in skip]

    if not os.path.isfile(input):
        die('"{}" is not a file'.format(input))


    match = 0
    accession = []
    with open(input) as handle:
        records = SwissProt.parse(handle)
        for i, record in enumerate(records, start=1):
            keyword_set = set(record.keywords)
            taxa_set = set(record.organism_classification)

            if keyword_set.intersection(set([keyword])) and not taxa_set.intersection(set(skip_upper)):
                match += 1
                accession.append(record.accessions[0])

    fh = open(output, 'wt')
    for seq in SeqIO.parse(input, 'swiss'):
        if seq.id in accession:
            SeqIO.write(seq, fh, 'fasta')

    print('Processing "{}"'.format(input))
    print('Done, skipped {} and took {}. See output in "{}".'.format(i-match, match, output))

# --------------------------------------------------
if __name__ == '__main__':
    main()
