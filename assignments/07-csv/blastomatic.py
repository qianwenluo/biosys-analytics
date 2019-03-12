#!/usr/bin/env python3
"""
Author : qianwenluo
Date   : 2019-02-27
Purpose: Rock the Casbah
"""

import argparse
import sys
import os
import csv

# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Annotate BLAST output',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'csv', metavar='FILE', help='BLAST output (-outfmt 6)')

    parser.add_argument(
        '-a',
        '--annotations',
        help='Annotation file',
        metavar='FILE',
        type=str,
        default='')

    parser.add_argument(
        '-o',
        '--outfile',
        help='Output file',
        metavar='FILE',
        type=str,
        default='')


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
    annotations = args.annotations
    outfile = args.outfile
    input = args.csv

    if not os.path.isfile(input):
        die('"{}" is not a file'.format(input))

    if not os.path.isfile(annotations):
        die('"{}" is not a file'.format(annotations))

    with open(input) as txt:
        rows = ( line.split('\t') for line in txt )
        hits = {row[1]:row[2] for row in rows}

    tree = {}
    with open(annotations) as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        for rows in reader:
            if rows['species'] == '':
                rows['species'] = 'NA'
            if rows['genus'] == '':
                rows['genus'] = 'NA'
            tree[rows['centroid']] = rows['genus'], rows['species']

    # match two dictionary
    out_fh = open(outfile, 'wt') if outfile else sys.stdout
    name = ("seq_id", "pident", "genus", "species")
    out_fh.write('\t'.join(name) + '\n')

    for key in hits.keys():
        if key in tree.keys():
            out_fh.write(key + '\t' + hits[key] + '\t' + '\t'.join(tree[key]) + '\n')

        else:
            sys.stderr.write('Cannot find seq "{}" in lookup\n'.format(key))



# --------------------------------------------------
if __name__ == '__main__':
    main()
