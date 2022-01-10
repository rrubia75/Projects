"""Author: Ryan Rubia : Purpose: Maze Game for practice and fun"""
from time import sleep
def decision():
    if choice == "left":
        print("Left it is!")
    elif choice == "right":
        print("To the right we go!")
    else:
        print("You have to choose left or right")




print("You are hiking through the forest. You smell the fresh air blowing through the evergreen trees and can feel the sunlight occasionally hitting your face through the trees.")
sleep(5)
print("You come to a fork in the trail. To the left, there is a sign that reads: 'Climb the mountain.' To the right, there is a sign that reads: 'Descend into the valley.' ")
input()
input("Which direction do you choose?: ".lower())
choice= decision()

