#!/usr/bin/env python3

import sys

if len(sys.argv)==1:
    print("none")
else:
    first_param = sys.argv[1]
    print(f"First parameter is '{first_param}'")