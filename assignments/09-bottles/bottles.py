#!/usr/bin/env python3
"""
Author : qianwenluo
Date   : 2019-03-12
Purpose: Rock the Casbah
"""

import argparse
import sys


# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Bottles of beer song',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)


    parser.add_argument(
        '-n',
        '--num_bottles',
        help='How many bottles',
        metavar='INT',
        type=int,
        default=10)

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
    num_bottles = args.num_bottles

    for i in range(num_bottles, 0, -1):
        if i == 1:
            print('1 bottle of beer on the wall,\n'
                '1 bottle of beer,\n'
                'Take one down, pass it around,\n'
                '0 bottles of beer on the wall!')
        elif i == 2:
            print('2 bottles of beer on the wall,\n'
                '2 bottles of beer,\n'
                'Take one down, pass it around,\n'
                '1 bottle of beer on the wall!\n')
        else:
            print('{} bottles of beer on the wall,\n'
                '{} bottles of beer,\n'
                'Take one down, pass it around,\n'
                '{} bottles of beer on the wall!\n'.format(i,i,i-1))

    #print('int_arg = "{}"'.format(num_bottles))

# --------------------------------------------------
if __name__ == '__main__':
    main()
