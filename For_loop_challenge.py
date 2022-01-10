farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]
NE_animals=farms[0]["agriculture"]
W_animals=farms[1]["agriculture"]
SE_animals=farms[2]["agriculture"]
#for x in NE_animals:
    #print(x)
x=input("Choose a farm from the list: NE/W/SE: ")
if x == "NE".lower():
    print(NE_animals)
elif x == "W".lower():
    print(W_animals)
elif x == "SE".lower():
    print(SE_animals)
else:
    print("You didn't answer correctly, dummy! Run this script again")
