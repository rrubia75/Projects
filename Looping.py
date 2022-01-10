from time import sleep
names=["Ryan", "Melissa","Aubrey","Madison","Karlee","Dennis"]
alpha=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O""P","Q","R","S","T","U","V","W","X","Y","Z"]
for x in names:
    if x.startswith("M"):
        print(x + "'s name starts with M!")
    else:
        print(x + "'s name doesn't start with M.")
sleep(1)
print("That is the end of the names.")