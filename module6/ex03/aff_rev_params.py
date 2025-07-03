#!/usr/bin/env python3

import sys

if len(sys.argv)<3:
    print('none')
else:
    list=sys.argv[1:] #list of args minus the script name
    list.reverse() #apply reverse in separate line
    for i in list:
        print(i)
    

