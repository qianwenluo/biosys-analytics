#!/usr/bin/env python3
"""
Author : qianwenluo
Date   : 2019-02-01
Purpose: homework
"""

import os
import sys


# --------------------------------------------------
def main():
    args = sys.argv[1:]

    if len(args) != 1:
        print('Usage: {} STRING'.format(os.path.basename(sys.argv[0])))
        sys.exit(1)
    
    string = args[0]
    count=0
    for i in string:
        if i == "a" or i =="e" or i == "i" or i == "o" or i == "u" or i == "A" or i == "E" or i == "I" or i == "O" or i == "U":
           count += 1
    if count == 1:    
        print('There is {} vowel in "{}."'.format(count,string))
    else:
        print('There are {} vowels in "{}."'.format(count,string))


# --------------------------------------------------
main()
