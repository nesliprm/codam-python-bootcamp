#!/usr/bin/env python3

import sys

if len(sys.argv) != 3:
    print('Please enter exactly two numbers as parameters.')
else:
    param1=int(sys.argv[1])
    param2=int(sys.argv[2])
    if param1<param2:
        numrange=range(param1, param2+1)
        numarray=[]
        for n in numrange:
            numarray.append(n)
        print(numarray)
    else:
        print('First number must be smaller than the second.')
            



