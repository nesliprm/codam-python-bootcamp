#!/usr/bin/env python3

import sys

def upcase_it():
    if len(sys.argv)!=2:
        print("none")
    else:
        print(sys.argv[1].upper())

upcase_it()

    

