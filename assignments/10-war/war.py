#!/usr/bin/env python3
"""
Author : qianwenluo
Date   : 2019-03-19
Purpose: Rock the Casbah
"""

import argparse
import sys
from itertools import product
import random




# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='"War" cardgame',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)


    parser.add_argument(
        '-s',
        '--seed',
        help='Random seed',
        metavar='int',
        type=int,
        default=None)


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
    seed = args.seed

    if seed is not None:
        random.seed(seed)

    suites = ['♥','♠','♣','♦']
    ranks = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    cards=list(product(suites,ranks))
    cards.sort()
    random.shuffle(cards)

    values = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'J':11, 'Q':12, 'K':13, 'A':14}
    p1_count = 0
    p2_count = 0
    war_count = 0

    cards.reverse()
    for i in range(0, 26):
        p1=cards.pop(0)
        p2=cards.pop(0)

        if values[p2[1]] > values[p1[1]]:
            p2_count += 1
            print('{:>3} {:>3} P2'.format(''.join(p1), ''.join(p2)))
        elif values[p2[1]] < values[p1[1]]:
            p1_count += 1
            print('{:>3} {:>3} P1'.format(''.join(p1), ''.join(p2)))
        else:
            war_count += 1
            print('{:>3} {:>3} WAR!'.format(''.join(p1), ''.join(p2)))

    if p1_count > p2_count:
        print('P1 {} P2 {}: Player 1 wins'.format(p1_count,p2_count))
    elif p1_count < p2_count:
        print('P1 {} P2 {}: Player 2 wins'.format(p1_count,p2_count))
    else:
        print('P1 {} P2 {}: DRAW'.format(p1_count,p2_count))

# --------------------------------------------------
if __name__ == '__main__':
    main()
