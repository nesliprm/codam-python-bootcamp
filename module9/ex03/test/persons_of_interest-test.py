#!/usr/bin/env python3

def famous_births(people_dict):

    def birthyears(data):
        return list(data[1].values())[1]
    
    sorted_dict=sorted(people_dict.items(), key=birthyears)
    for name, info in sorted_dict:
        name=list((info).values())[0]
        birthyear=list(info.values())[1]
        
        print(f"{name} is a great scientist born in {birthyear}.")

    
women_scientists = {
    "ada": { "name": "Ada Lovelace", "date_of_birth": "1815" },
    "cecilia": { "name": "Cecila Payne", "date_of_birth": "1900" },
    "lise": { "name": "Lise Meitner", "date_of_birth": "1878" },
    "grace": { "name": "Grace Hopper", "date_of_birth": "1906" }
}

famous_births(women_scientists)
