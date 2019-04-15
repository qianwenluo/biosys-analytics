#!/usr/bin/env python3
"""
Author : qianwenluo
Date   : 2019-04-14
Purpose: Rock the Casbah
"""

import argparse
import sys
import os
import logging


# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Hamming distance',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'positional', metavar='FILE', help='file inputs',nargs=2)

    parser.add_argument(
        '-d',
        '--debug',
        help='Debug',
        action='store_true',
        default=False)

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

def dist(s1,s2):
    hamm = 0
    for i in range(0, min(len(s1), len(s2))):
        if s1[i] != s2[i]:
            hamm += 1
    return hamm + max(len(s1),len(s2)) - min(len(s1), len(s2))


# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()
    input = args.positional
    debug = args.debug

    if not os.path.isfile(input[0]):
        die('"{}" is not a file'.format(input[0]))
    if not os.path.isfile(input[1]):
        die('"{}" is not a file'.format(input[1]))

    logging.basicConfig(
        filename='.log',
        filemode='w',
        level=logging.DEBUG if debug else logging.CRITICAL
    )


    file1 = open(input[0],'r')
    file2 = open(input[1],'r')
    logging.debug('file1 = {}, file2 = {}'.format(input[0],input[1]))

    content1 = []
    content2 = []
    for row1 in file1:
        for words1 in row1.split():
            content1.append(words1)
    for row2 in file2:
        for words2 in row2.split():
            content2.append(words2)

    distance = 0
    for a, b in zip(content1, content2):
        hamm_d = dist(a,b)
        distance += hamm_d
        logging.debug('s1 = {}, s2 = {}, d = {}'.format(a,b,hamm_d))
    print(distance)



# --------------------------------------------------
if __name__ == '__main__':
    main()
