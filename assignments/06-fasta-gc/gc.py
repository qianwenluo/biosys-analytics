#!/usr/bin/env python3
"""
Author : qianwenluo
Date   : 2019-02-24
Purpose: Rock the Casbah
"""

import argparse
import sys
import os
from collections import Counter
from Bio import SeqIO

# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Segregate FASTA sequences by GC content',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'fasta', metavar='FILE', help='Input FASTA file(s)', nargs='+')

    parser.add_argument(
        '-o',
        '--outdir',
        help='Output directory',
        metavar='DIR',
        type=str,
        default='out')

    parser.add_argument(
        '-p',
        '--pct_gc',
        help='Dividing line for percent GC',
        metavar='int',
        type=int,
        default=50)

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
    out_dir = args.outdir
    pct = args.pct_gc
    fasta = args.fasta

    if pct is not None and not 1 <= pct <= 100:
        die('--pct_gc "{}" must be between 0 and 100'.format(pct))

    if not os.path.isdir(out_dir):
        os.mkdir(out_dir)

    num_written = 0
    for i ,file in enumerate(fasta, start = 1):
        if not os.path.isfile(file):
            warn('"{}" is not a file'.format(os.path.basename(file)))
        else:
            print('{:3d}: {}'.format(i, os.path.basename(file)))

            base, ext = os.path.splitext(os.path.basename(file))
            low = os.path.join(out_dir, base + '_low' + ext)
            high = os.path.join(out_dir, base + '_high' + ext)
            high_seq = []
            low_seq = []


            for record in SeqIO.parse(file, 'fasta'):
                num_written += 1
                seq_len = len(record.seq)
                nucs = Counter(record.seq)
                gc_num = nucs.get('G', 0) + nucs.get('C', 0)
                gc = int(gc_num / seq_len * 100)

                if gc >= pct:
                    high_seq.append(record)
                    SeqIO.write(high_seq, high, "fasta")
                else:
                    low_seq.append(record)
                    SeqIO.write(low_seq, low, "fasta")


    print('Done, wrote {} sequence{} to out dir "{}"'.format(
        num_written, '' if num_written == 1 else 's', out_dir))
# --------------------------------------------------
if __name__ == '__main__':
    main()
