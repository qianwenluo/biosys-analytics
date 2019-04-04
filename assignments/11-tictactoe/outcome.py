#!/usr/bin/env python3
"""
Author : qianwenluo
Date   : 2019-04-03
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

    x_win1 = re.compile('X{3}[.XO]{3}[.XO]{3}')
    x_win2 = re.compile('[.XO]{3}X{3}[.XO]{3}')
    x_win3 = re.compile('[.XO]{3}[.XO]{3}X{3}')
    x_win4 = re.compile('X[.XO]{2}X[.XO]{2}X[.XO]{2}')
    x_win5 = re.compile('[.XO]{1}X[.XO]{2}X[.XO]{2}X[.XO]{1}')
    x_win6 = re.compile('[.XO]{2}X[.XO]{2}X[.XO]{2}X')
    x_win7 = re.compile('X[.XO]{3}X[.XO]{3}X')
    x_win8 = re.compile('[.XO]{2}X[.XO]{1}X[.XO]{1}X[.XO]{2}')

    o_win1 = re.compile('O{3}[.XO]{3}[.XO]{3}')
    o_win2 = re.compile('[.XO]{3}O{3}[.XO]{3}')
    o_win3 = re.compile('[.XO]{3}[.XO]{3}O{3}')
    o_win4 = re.compile('O[.XO]{2}O[.XO]{2}O[.XO]{2}')
    o_win5 = re.compile('[.XO]{1}O[.XO]{2}O[.XO]{2}O[.XO]{1}')
    o_win6 = re.compile('[.XO]{2}O[.XO]{2}O[.XO]{2}O')
    o_win7 = re.compile('O[.XO]{3}O[.XO]{3}O')
    o_win8 = re.compile('[.XO]{2}O[.XO]{1}O[.XO]{1}O[.XO]{2}')

    match1 = x_win1.match(state) or x_win2.match(state) or x_win3.match(state) or x_win4.match(state) or x_win5.match(state) \
    or x_win6.match(state) or x_win7.match(state) or x_win8.match(state)

    match2 = o_win1.match(state) or o_win2.match(state) or o_win3.match(state) or o_win4.match(state) or o_win5.match(state) \
    or o_win6.match(state) or o_win7.match(state) or o_win8.match(state)

    if match1:
        print('X has won')
    elif match2:
        print('O has won')
    else:
        print('No winner')


# --------------------------------------------------
main()
