#!/usr/bin/env python3
"""
Author : qianwenluo
Date   : 2019-02-05
Purpose: Rock the Casbah
"""

import os
import sys


# --------------------------------------------------
def main():
    args = sys.argv[1:]

    if len(args) != 1:
        print('Usage: {} FILE'.format(os.path.basename(sys.argv[0])))
        sys.exit(1)

    file = args[0]
    if not os.path.isfile(file):
        print('{} is not a file'.format(file))
        sys.exit(1)

    with open(file) as txt:
        line = txt.readline()
        count = 1
        while line:
            print('{:3}: {}'.format(count,line.strip()))
            line = txt.readline()
            count +=1

# --------------------------------------------------
main()
