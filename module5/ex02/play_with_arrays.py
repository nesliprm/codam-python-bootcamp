#!/usr/bin/env python3

numbers=[1,3,5,7,9,11,13]
newnumbers=[]

for n in numbers:
    if n>5:
        newnumbers.append(n+2)

print(f"Original array: {numbers}")
print(f"Modified array: {newnumbers}")