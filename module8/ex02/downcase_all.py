#!/usr/bin/env python3

import sys


params=sys.argv[1:]
def downcase_it(params):
    
    if len(params)<1:
        print("none")
    else:
        for p in params:
            print(p.lower())

downcase_it(params)


    

