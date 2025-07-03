#!/usr/bin/env python3

import sys

word=input('What was the parameter?\n')

if len(sys.argv) < 2:
    print('none')
else:
    if word == sys.argv[1]:
        print('Good job!')
    else:
        print('Nope, sorry...')

