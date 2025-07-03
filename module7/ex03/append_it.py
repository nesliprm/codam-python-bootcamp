#!/usr/bin/env python3

import sys

params=sys.argv[1:]
for p in params:
    if p.find('ism') != len(p)-3:
        newp=p+'ism'
        print(newp)
    
    
