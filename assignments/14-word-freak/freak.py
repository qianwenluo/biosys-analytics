#!/usr/bin/env python3
"""
Author : qianwenluo
Date   : 2019-04-18
Purpose: Rock the Casbah
"""

import argparse
import sys
import re
import collections

# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Print word frequencies',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'positional', metavar='FILE', help='File input(s)', nargs='+',
        type=argparse.FileType('r', encoding='UTF-8'))

    parser.add_argument(
        '-s',
        '--sort',
        help='Sort by word or frequency',
        metavar='str',
        type=str,
        default='word')

    parser.add_argument(
        '-m',
        '--min',
        help='Minimum count',
        metavar='int',
        type=int,
        default=0)


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
    files = args.positional
    sort = args.sort
    m = args.min


    txt1 = []
    txt2 = []
    words = []
    for file in files:
        for text in file.read().split():
            words.append(text)
    for word in words:
        word = word.lower()
        txt1.append(re.sub('[^a-zA-Z0-9]', '', word))
    for i in txt1:
        if i != '':
            txt2.append(i)
    cnt=collections.Counter(txt2)
    if sort == 'word':
        for w, c in sorted(cnt.items()):
            if c >= m:
                print('{:20} {}'.format(w, c))
    else:
        pairs = sorted([(x[1], x[0]) for x in cnt.items()])
        for c, w in pairs:
            if c >= m:
                print('{:20} {}'.format(w, c))






# --------------------------------------------------
if __name__ == '__main__':
    main()
