#!/usr/bin/env python3
"""
Author : qianwenluo
Date   : 2019-03-24
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
        description='Blackjack Game',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        '-s',
        '--seed',
        help='Random seed',
        metavar='int',
        type=int,
        default=None)

    parser.add_argument(
        '-p', '--player_hits', help='A boolean flag', action='store_true')

    parser.add_argument(
        '-d', '--dealer_hits', help='A boolean flag', action='store_true')

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
    player = args.player_hits
    dealer = args.dealer_hits

    if seed is not None:
        random.seed(seed)

    suites = ['♥','♠','♣','♦']
    ranks = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    cards=list(product(suites,ranks))
    cards.sort()
    random.shuffle(cards)
    #print(cards)

    values = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'J':10, 'Q':10, 'K':10, 'A':1}
    cards.reverse()

    p1=cards.pop(0)
    d1=cards.pop(0)
    p2=cards.pop(0)
    d2=cards.pop(0)

    if player:
        p3=cards.pop(0)
        p_hits = values[p1[1]] + values[p2[1]] +values[p3[1]]
        p_cards = ''.join(p1) + ' ' + ''.join(p2) + ' ' + ''.join(p3)
    else:
        p_hits = values[p1[1]] + values[p2[1]]
        p_cards = ''.join(p1) + ' ' + ''.join(p2)

    if dealer:
        d3=cards.pop(0)
        d_hits = values[d1[1]] + values[d2[1]] +values[d3[1]]
        d_cards = ''.join(d1) + ' ' + ''.join(d2) + ' ' + ''.join(d3)
    else:
        d_hits = values[d1[1]] + values[d2[1]]
        d_cards = ''.join(d1) + ' ' + ''.join(d2)

    print('D [{:2}]: {}'.format(d_hits, d_cards))
    print('P [{:2}]: {}'.format(p_hits, p_cards))

    if p_hits >21:
        print('Player busts! You lose, loser!')
        exit(0)
    if d_hits >21:
        print('Dealer busts.')
        exit(0)
    if p_hits ==21:
        print('Player wins. You probably cheated.')
        exit(0)
    if d_hits ==21:
        print('Dealer wins!')
        exit(0)
    if d_hits < 18:
        print('Dealer should hit.')
    if p_hits < 18:
        print('Player should hit.')



# --------------------------------------------------
if __name__ == '__main__':
    main()
