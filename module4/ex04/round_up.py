#!/usr/bin/env python3

import math 

num=float(input('Give me a number: '))
#roundupnum=round(num)
roundupnum = math.ceil(num)
print(f'{num} rounds up to {roundupnum}.')
