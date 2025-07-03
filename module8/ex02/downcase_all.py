#!/usr/bin/env python3

import sys

def downcase_it():
    params=sys.argv
    if len(params)!=3:
        print("none")
    else:
        for p in params:
            print(p.lower())

downcase_it()


    

