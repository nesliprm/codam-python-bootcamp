#!/usr/bin/env python3

print("Enter a number less than 25")
number=int(input())
if number > 25:
    print('Error')
else:
    i=number
    while i<=25:
        print(i)
        i+=1