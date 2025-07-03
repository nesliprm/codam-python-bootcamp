#!/usr/bin/env python3

import sys

params=sys.argv[1:]
for p in params:
    if p.find('ism') == -1:
        newp=p+'ism'
        print(newp)
    
    
