#!/usr/bin/env python3
"""
Author : qianwenluo
Date   : 2019-02-14
Purpose: Rock the Casbah
"""

import argparse
import sys
import os
import re

# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Translate DNA/RNA to proteins',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'positional', metavar='STR', help='DNA/RNA sequence')

    parser.add_argument(
        '-c',
        '--codons',
        help='A file with codon translations',
        metavar='FILE',
        type=str,
        default=None,
        required=True)

    parser.add_argument(
        '-o',
        '--outfile',
        help='Output filename',
        metavar='FILE',
        type=str,
        default='out.txt')

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
    codons = args.codons
    outfile = args.outfile
    pos_arg = args.positional.upper()

    if codons and not os.path.isfile(codons):
        die('--codons "{}" is not a file'.format(codons))     
    
    codon2aa = {}
    with open(codons) as txt:
        for row in txt:
            codon,aa = row.split()
            codon2aa[codon] = aa 
    
    out_fh = open(outfile, 'wt')
    k =3 
    n = len(pos_arg) - k +1
    protein =''
    for i in range(0, n, k):
        if pos_arg[i:i+k] in codon2aa:
            input_codon = pos_arg[i:i+k]
            protein = codon2aa[input_codon]
        else:
            protein = '-'
        out_fh.write(protein)        
    out_fh.close()
    print('Output written to "{}"'.format(outfile))
# --------------------------------------------------
if __name__ == '__main__':
    main()
