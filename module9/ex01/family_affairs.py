#!/usr/bin/env python3

def find_the_redheads(fam_members):
    
    filtered=filter(lambda name:fam_members[name] == 'red', fam_members.keys())
    return list(filtered)



dupont_family = {
"florian": "red",
"marie": "blond",
"virginie": "brunette",
"david": "red",
"franck": "red"
}

print(find_the_redheads(dupont_family))


        