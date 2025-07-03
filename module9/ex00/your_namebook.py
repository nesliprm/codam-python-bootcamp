#!/usr/bin/env python3

def array_of_names(people):
    fullnames=[]
    for first, last in people.items():
        fullname = first.capitalize() + " " + last.capitalize()
        fullnames.append(fullname)
    return fullnames 
    

people = {
"jean": "valjean",
"grace": "hopper",
"xavier": "niel",
"fifi": "brindacier"
}

print(array_of_names(people))

        