#!/usr/bin/env python3
"""
Author : qianwenluo
Date   : 2019-04-04
Purpose: Rock the Casbah
"""

import argparse
import sys
import os
import re
from Bio import SeqIO

# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Find unclustered proteins',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        '-c',
        '--cdhit',
        help='Output file from CD-HIT (clustered proteins)',
        metavar='str',
        type=str,
        default=None,
        required=True)

    parser.add_argument(
        '-p',
        '--proteins',
        help='Proteins FASTA',
        metavar='str',
        type=str,
        default=None,
        required=True)

    parser.add_argument(
        '-o',
        '--outfile',
        help='Output file',
        metavar='str',
        type=str,
        default='unclustered.fa')

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
    hit = args.cdhit
    protein = args.proteins
    output = args.outfile


    if not os.path.isfile(protein):
        die('--proteins "{}" is not a file'.format(protein))

    if not os.path.isfile(hit):
        die('--cdhit "{}" is not a file'.format(hit))

    id = []
    with open(hit, 'r') as txt:
        for row in txt:
            match1 = re.search('>gi\|(\d+)',row)
            if match1:
                cd_id = match1.group(1)
                id.append(cd_id)

    fh = open(output,'wt')

    count = 0
    unclustered = 0

    for record in SeqIO.parse(protein, 'fasta'):
        count += 1
        match2 = re.search('(\d+)',record.id)
        if match2:
            p_id = match2.group(1)
            if p_id not in id:
                unclustered +=1
                SeqIO.write(record, fh, "fasta")

    print('Wrote {:,} of {:,} unclustered proteins to "{}"'.format(unclustered, count, output))



# --------------------------------------------------
if __name__ == '__main__':
    main()
