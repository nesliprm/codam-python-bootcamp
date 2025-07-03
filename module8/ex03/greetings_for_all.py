#!/usr/bin/env python3

def greetings(name="noble stranger"):
    if not isinstance(name, str):
        print("ERROR: Please enter a valid name!")
    else:
        print(f"Hello, {name}!")

greetings('Alexandra')
greetings('Wil')
greetings()
greetings(42)
   