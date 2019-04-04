#!/usr/bin/env python3
"""
Author : qianwenluo
Date   : 2019-04-04
Purpose: Rock the Casbah
"""

import os
import sys
import re


# --------------------------------------------------
def main():
    args = sys.argv[1:]

    if len(args) != 2:
        print('Usage: {} PASSWORD ALT'.format(os.path.basename(sys.argv[0])))
        sys.exit(1)

    input1 = args[0]
    input2 = args[1]


    pass_re = re.compile('.?'+ input1+'.?',re.IGNORECASE)

    match = pass_re.match(input2)

    if match:
        print('ok')
    else:
        print('nah')

# --------------------------------------------------
main()
