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
        print('Usage: {} NUM'.format(os.path.basename(sys.argv[0])))
        sys.exit(1)

    grid_size = int(args[0])
    if not 2 <= grid_size <=9:
        print ('NUM ({}) must be between 1 and 9'.format(grid_size))
        sys.exit(1)
            
    grids = [[i for i in range(j,j+grid_size)] for j in range(1,grid_size ** 2 +1,grid_size)]
    #print (grids)
    for row in grids:
        for item in row:
            print('{:3}'.format(item),end='')
        print()    

   
# --------------------------------------------------
main()
