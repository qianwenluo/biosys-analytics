#!/usr/bin/env python3
"""
Author : qianwenluo
Date   : 2019-02-19
Purpose: Rock the Casbah
"""

import argparse
import os
import sys


# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Argparse Python script',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'positional', metavar='DIR', help='[DIR ...]', nargs='+')

    parser.add_argument(
        '-w',
        '--width',
        help='A named string argument',
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
    width = args.width
    pos_arg = args.positional

    for i in pos_arg:
        if not os.path.isdir(i):
            print('"{}" is not a directory'.format(i), file = sys.stderr)
        else:
            print(i)
            out = {}
            for file in os.listdir(i):
                with open(os.path.join(i, file)) as txt:
                    lines = txt.readlines()[0].rstrip()
                    ellipses = '.' * (width - len(lines) - len(file))
                    out[file] = lines + ' ' + ellipses + ' ' + file
            pairs = sorted([(x[1], x[0]) for x in out.items()])
            for content, name in pairs:
                print('{}'.format(content))


# --------------------------------------------------
if __name__ == '__main__':
    main()
