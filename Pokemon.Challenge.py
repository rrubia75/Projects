#!/usr/bin/env python3
import csv
from time import sleep
print("What pokemon would you like to learn about?" )
pokename= input().capitalize()
with open("pokedex.txt","r") as pokedata:
    for x in csv.DictReader(pokedata):
        pokedict = dict(x)
        if pokedict["Name"] == pokename:
            print(f"{pokedict['Name']} is of the {pokedict['Type 1']} and {pokedict['Type 2']} types!")
            sleep(1)
            print("Which stat would you like to know? (HP,Attack,Defense,Sp. Atk,Sp. Def or Speed)" )
            x= input().lower()
            if x == "hp":
                print(f"{pokedict['Name']} has an HP stat of {pokedict['HP']}")
            elif x == "attack":
                print(f"{pokedict['Name']} has an Attack stat of {pokedict['Attack']}")
            elif x == "defense":
                print(f"{pokedict['Name']} has a Defense stat of {pokedict['Defense']}")
            elif x == "sp. atk":
                print(f"{pokedict['Name']} has a Sp.Atk stat of {pokedict['Sp. Atk']}")
            elif x == "sp. def":
                print(f"{pokedict['Name']} has a Sp. Def stat of {pokedict['Sp. Def']}")
            elif x == "speed":
                print(f"{pokedict['Name']} has a Speed stat of {pokedict['Speed']}")
            else:
                print("You were supposed to choose a stat to view. Now you need to start over")
                break

