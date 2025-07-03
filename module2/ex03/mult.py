#!/usr/bin/env python3

print("Enter a number")
num1=int(input())
print("Enter another number")
num2=int(input())
result= num1 * num2
print(f"{num1} x {num2} = {result}")
if result > 0:
	print("Result is positive")
elif result<0:
	print("Result is negative")
else:
	print("Result is zero")

