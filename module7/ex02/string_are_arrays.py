#!/usr/bin/env python3

import sys
import re

params=sys.argv[1:]

if len(params) == 0:
    print('No parameters provided.')
else:
    if len(re.findall('z', sys.argv[1]))==0:
        print('none')
    else:
        zcount=len(re.findall('z', sys.argv[1]))
        zlist= 'z' * zcount
        print(zlist)