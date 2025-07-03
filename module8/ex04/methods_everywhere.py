#!/usr/bin/env python3

import sys

def shrink(word):
    x=slice(8)
    print(word[x])

def enlarge(word):
    newword=word
    while len(newword) < 8:
        newword += 'Z'
    print(newword)

params=sys.argv[1:]

for p in params:
    if len(p) > 8:
        shrink(p)
    elif len(p) < 8:
        enlarge(p)
    else:
        print(p)

