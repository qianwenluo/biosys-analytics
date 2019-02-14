#!/usr/bin/env python3
"""
Author : qianwenluo
Date   : 2019-02-07
Purpose: Rock the Casbah
"""

import argparse
import sys


# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Tic-Tac-Toe board',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        '-s',
        '--state',
        help='Board state',
        metavar='str',
        type=str,
        default=".........")

    parser.add_argument(
        '-p',
        '--player',
        help='Player',
        metavar='str',
        type=str,
        default = '')

    parser.add_argument(
        '-c', 
        '--cell', 
        help='Cell to apply -p',
        metavar='int',
        type=int)


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
    state_arg = args.state
    player_arg = args.player
    cell_arg = args.cell
    
    arg = sys.argv[1:]
    if len(arg) == 0:
        board = [1,2,3,4,5,6,7,8,9]
        print('-------------')
        print('|',board[0],'|',board[1],'|',board[2],'|')
        print('-------------')
        print('|',board[3],'|',board[4],'|',board[5],'|')
        print('-------------')
        print('|',board[6],'|',board[7],'|',board[8],'|')
        print('-------------')
        sys.exit(1)        
    
    if state_arg and not len(state_arg) == 9:
        print('Invalid state "{}", must be 9 characters of only -, X, O'.format(state_arg)) 
        sys.exit(1)   

    if player_arg is not None and not player_arg in 'XO':
        die('Invalid player "{}", must be X or O'.format(player_arg))    
    
    if cell_arg is not None and not 1 <= cell_arg <= 9:
        die('Invalid cell "{}", must be 1-9'.format(cell_arg)) 
     
    if any([player_arg, cell_arg]) and not all ([player_arg, cell_arg]):
        die('Must provide both --player and --cell')
    
    # print a valid state
    state = list(state_arg)
    for i, c in enumerate(state):
        if c == '.':
            state[i] = str(i+1)
        if cell_arg is not None and player_arg in 'XO':
            if state_arg[cell_arg-1] in 'XO':
                die('Cell {} already taken'.format(cell_arg))
            else:
                state[cell_arg-1] = player_arg 
    print('-------------')
    print('|',state[0],'|',state[1],'|',state[2],'|')
    print('-------------')
    print('|',state[3],'|',state[4],'|',state[5],'|')
    print('-------------')
    print('|',state[6],'|',state[7],'|',state[8],'|')
    print('-------------')        
# move 
    
    #if board[cell_arg] == '':
    #    board[cell_arg] = 
    #else:
    #    print('Cell {} already taken'.format(cell_arg))


# --------------------------------------------------
if __name__ == '__main__':
    main()
