#!/usr/bin/env python3
"""
Author : qianwenluo
Date   : 2019-02-15
Purpose: Rock the Casbah
"""

import os
import sys
import re

# --------------------------------------------------
def main():
    args = sys.argv[1:]

    if len(args) != 1:
        print('Usage: {} STATE'.format(os.path.basename(sys.argv[0])))
        sys.exit(1)

    state = args[0]
    if not re.search('^[.XO]{9}$',state):
        print('State "{}" must be 9 characters of only ., X, O'.format(state))
        sys.exit(1)
    
   # for i, c in enumerate(state):
   
    #        print(state) 
    win_combination = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)] 
    for a, b, c in win_combination:
        if state[a] == state[b] == state[c] in 'XO':
            print('{} has won'.format(state[a]))
            return True
    else:print('No winner')   
# --------------------------------------------------
main()
