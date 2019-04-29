#!/usr/bin/env python3
"""
Author : qianwenluo
Date   : 2019-04-25
Purpose: Rock the Casbah
"""

import argparse
import sys
import os
import logging
import re
from tabulate import tabulate
import pandas as pd


# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Find common words',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'positional', metavar='FILE', help='Input files', nargs=2)

    parser.add_argument(
        '-m',
        '--min_len',
        help='Minimum length of words',
        metavar='int',
        type=int,
        default=0)

    parser.add_argument(
        '-n',
        '--hamming_distance',
        help='Allowed Hamming distance',
        metavar='int',
        type=int,
        default=0)

    parser.add_argument(
        '-l',
        '--logfile',
        help='Logfile name',
        metavar='str',
        type=str,
        default='.log')

    parser.add_argument(
        '-d', '--debug', help='Debug', action='store_true',default=False)

    parser.add_argument(
        '-t', '--table', help='Table output', action='store_true',default=False)

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
def dist(s1, s2):
    d = abs(len(s1) - len(s2)) + sum(
        map(lambda p: 0 if p[0] == p[1] else 1, zip(s1, s2)))
    logging.debug('s1 = {}, s2 = {}, d = {}'.format(s1, s2, d))

    return d
# --------------------------------------------------

def main():
    """Make a jazz noise here"""
    args = get_args()
    files = args.positional
    min_len = args.min_len
    h_dist = args.hamming_distance
    logfile = args.logfile
    debug = args.debug
    table = args.table


    logging.basicConfig(
        filename=logfile,
        filemode='w',
        level=logging.DEBUG if debug else logging.CRITICAL
    )

    for file in files:
        if not os.path.isfile(file):
            die('"{}" is not a file'.format(file))

    if h_dist < 0:
        die('--distance "{}" must be > 0'.format(h_dist))

    fh1 = open(files[0],'r')
    fh2 = open(files[1],'r')
    logging.debug('file1 = {}, file2 = {}'.format(files[0],files[1]))

    content1 = []
    content2 = []
    for row1 in fh1:
        for words1 in row1.split():
            words1 = re.sub('[^a-zA-Z0-9]', '', words1).lower()
            if len(words1) >= min_len:
                content1.append(words1)

    for row2 in fh2:
        for words2 in row2.split():
            words2 = re.sub('[^a-zA-Z0-9]', '', words2).lower()
            if len(words2) >= min_len:
                content2.append(words2)

    count = 0
    output = {}
    output['word1'] = []
    output['word2'] = []
    output['distance'] = []
    for i in content1:
        for j in content2:
            distance = dist(i,j)
            if distance <= h_dist:
                count += 1
                output['word1'].append(i)
                output['word2'].append(j)
                output['distance'].append(distance)
    if count == 0:
        print('No words in common.')
    else:
        headers = ['word1','word2','distance']
        df = pd.DataFrame(output)
        df = df.sort_values(by=['word1','word2'])
        df = df.drop_duplicates()
        df = df.set_index('word1')
        if table:
            print(tabulate(df, headers, tablefmt='psql'))
        else:
            output2 = df.to_csv(sep='\t', mode='a',line_terminator='\n')
            print(output2,end='')

# --------------------------------------------------
if __name__ == '__main__':
    main()
