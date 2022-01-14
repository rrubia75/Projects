#!/usr/bin/python3
"""Author: Ryan Rubia :: Purpose: RPG game project"""

# from PIL import Image, ImageFont, ImageDraw
import sys
import os
from time import sleep
from text import IntroText, EndingText
import random
import shutil
from ConsoleColor import Color
import ConsoleColor

def DisplayGameLogo():
    with open("StartMenuImage2.txt") as file:
        data= file.read().splitlines()
        borderWidth= len(data[1]) + 5

        print(ConsoleColor.text(("*" * borderWidth).center(CONSOLE_WIDTH), Color.RED))

        for line in data:
            print(ConsoleColor.text(line.center(CONSOLE_WIDTH), Color.RED))

        print(ConsoleColor.text(("*" * borderWidth).center(CONSOLE_WIDTH), Color.RED))

def EndingImage():
    with open("EndingImage.txt") as file:
        data= file.read().splitlines()
        for line in data:
            print(ConsoleColor.text((line.center(CONSOLE_WIDTH)), Color.RED))


def showInstructions():
    # print a main menu and the commands
    clearScreen()
    print()
    print()
    print("\n+--------------------------------------+")
    typingPrint(' To Win: Escape the house. Good luck!  \n')
    typingPrint(ConsoleColor.text(('       BEWARE OF THE WITCH!'), Color.RED))
    sleep(0.5)
    print("\n+--------------------------------------+")
    input("Press Enter to continue!")
    clearScreen()

def showStatus():
    # print the player's current status
    print(ConsoleColor.text(("+--------------------------------+"), Color.RED))
    print(ConsoleColor.text(('You are in the ' + currentRoom), Color.BOLD))
    # print the current inventory
    print(ConsoleColor.text(('Pockets : ' + str(inventory)), Color.RED))
    # print an item if there is one
    if "item" in rooms[currentRoom]:
        print(ConsoleColor.text(('You see a ' + rooms[currentRoom]['item']), Color.BOLD))
    print(ConsoleColor.text(("+--------------------------------+"), Color.RED))

# Shows next possible move options
def nextMove():
    print(ConsoleColor.text(("You can go: "), Color.BOLD))
    if currentRoom == "Hall":
        print(ConsoleColor.text(("Upstairs to the Attic, \n"
              "East to the Dining Room, \n"
              "South to the Kitchen, \n"
              "West to the Living Room \n"), Color.RED))
    elif currentRoom == "Kitchen":
        print(ConsoleColor.text(("North to the Hall \n"
              "Downstairs to the Basement"), Color.RED))
    elif currentRoom == "Basement":
        print(ConsoleColor.text(("Upstairs to the Kitchen"), Color.RED))
    elif currentRoom == "Living Room":
        print(ConsoleColor.text(("East to the Hall"), Color.RED))
    elif currentRoom == "Attic":
        print(ConsoleColor.text(("Downstairs to the hall "), Color.RED))
    elif currentRoom == "Dining Room":
        print(ConsoleColor.text(("West to the Hall or "
              "South to the Garden"), Color.RED))
    else:
        print(ConsoleColor.text(("North to the Dining Room"), Color.RED))
    print(ConsoleColor.text(("+--------------------------------+"), Color.RED))


#This is for adding "Typing effect on text"
def typingPrint(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        sleep(0.05)
#This is for clearing the screen after input
def clearScreen():
    if sys.platform == "win32":
        os.system('cls')
    else:
        os.system('clear')

mylist=['Living Room', 'Dining Room' , 'Garden' , 'Attic']
ingredients=['Fur of a Bat','Something Silver','Leaf of Poison Ivy Plant']
# RandomRoom= random.choice(mylist)
def Witch():
    global currentRoom
    global RandomRoom
    while True:
        if RandomRoom == currentRoom:
            # print ("The witch is in "+ RandomRoom)
            typingPrint(ConsoleColor.text(("""
You hear a high pitched voice whisper in your ear,
"You're mine forever, my sweetie."
You feel a cold hand grasp the back of your neck and
the Witch drags you away!\n"""), Color.BRIGHT_RED))
            currentRoom= 'Basement'
            input("<Press enter to continue>")
            clearScreen()
            RandomRoom = random.choice(mylist)
            print("\n")
            input("\n<You open your eyes and see the basement>")
            clearScreen()
            # continue


        else:
            break


def displaymainmenu():
    DisplayGameLogo()
    print("\n")
    print_center("MAIN MENU\n")
    for option in main_menu_options:
        print_center("<"+option+">")

def print_center(s):
    print(s.center(shutil.get_terminal_size().columns))


def getinput():
    playerinput = input("> ").upper()
    return playerinput

# if __name__ == "__main--":
CONSOLE_WIDTH= os.get_terminal_size().columns
GAME_OVER = False
main_menu_options = ["PLAY", "QUIT"]
RandomRoom = random.choice(mylist)

while GAME_OVER == False:
    displaymainmenu()
    mainmenuoptionselected = getinput()

    if mainmenuoptionselected == 'PLAY':
        rooms = {

            'Hall': {
                'south': 'Kitchen',
                'east': 'Dining Room',
                'west': 'Living Room',
                'upstairs': 'Attic'
            },

            'Kitchen': {
                'north': 'Hall',
                'downstairs': 'Basement'
            },
            'Dining Room': {
                'west': 'Hall',
                'south': 'Garden',
                'item': 'matches'
            },
            'Garden': {
                'north': 'Dining Room',
                'item': 'poison ivy leaf'
            },
            'Basement': {
                'upstairs': 'Kitchen',
                'item': 'key',
            },
            'Attic': {
                'downstairs': 'Hall',
                'item': 'dead bat'
            },
            'Living Room': {
                'east': 'Hall',
                'item': 'silver coin'
            },
        }


        currentRoom = 'Basement'
        inventory= []
        # MainMenuImage()
        clearScreen()
        IntroText()
        input("\n<Press enter to continue>")
        clearScreen()
        showInstructions()
        while True:
            showStatus()
            nextMove()
            # get the player's next 'move'
            # .split() breaks it up into a list array
            # eg typing 'go east' would give the list:
            # ['go','east']
            move = ''
            while move == '':
                move = input(ConsoleColor.text(('>'), Color.BOLD))

            # split allows an items to have a space on them
            # get golden key is returned ["get", "golden key"]
            move = move.lower().split(" ", 1)

            if move[0] == 'get':
                # if the room contains an item, and the item is the one they want to get
                if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
                    # add the item to their inventory
                    inventory += [move[1]]
                    clearScreen()
                    # display a helpful message
                    print("Picked up the "+move[1]+"!" )
                    # delete the item from the room
                    del rooms[currentRoom]['item']
                    input("<Press enter to continue>")
                    clearScreen()
                    break
                # otherwise, if the item isn't there to get
                else:
                    # tell them they can't get it
                    print('Can\'t get ' + move[1] + '!')
            else:
                print("<ERROR> You need to get the key!")
                print("Try typing:\ngo [direction] \nget [item]")
                input("<Press enter to continue>")
                clearScreen()
                continue

            # if they type 'go' first
            if move[0] == 'go' and 'key' in inventory:
                # check that they are allowed wherever they want to go
                if move[1] in rooms[currentRoom]:
                    clearScreen()
                    currentRoom = rooms[currentRoom][move[1]]
                    print("You are now in the "+currentRoom+"!")
                    input("<Press enter to continue>")
                    clearScreen()
                    break
                else:
                    print("That's not a valid option")

            # loop until player has bat, poison ivy, silver coin and matches. Then enters kitchen to perform spell.
        while True:
            Witch()
            clearScreen()
            showStatus()
            nextMove()
            # get the player's next 'move'
            # .split() breaks it up into a list array
            # eg typing 'go east' would give the list:
            # ['go','east']
            move = ''
            while move == '':
                move = input(ConsoleColor.text(('>'), Color.BOLD))

            # split allows an items to have a space on them
            # get golden key is returned ["get", "golden key"]
            move = move.lower().split(" ", 1)

            # if they type 'go' first
            if move[0] == 'go':
                # check that they are allowed wherever they want to go
                if move[1] in rooms[currentRoom]:
                    # set the current room to the new room
                    currentRoom = rooms[currentRoom][move[1]]
                    clearScreen()
                    print("You are now in the "+currentRoom+"!")
                    input("<Press enter to continue>")
                    clearScreen()
                # there is no door (link) to the new room
                else:
                    print("YOU CAN'T GO THAT WAY!")
                    input("<Press enter to try again>")
                    clearScreen()
            # else:
            #     input("<ERROR> Press enter to try again!")
            #     continue


            # if they type 'get' first
            if move[0] == 'get':
                # if the room contains an item, and the item is the one they want to get
                if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
                    # add the item to their inventory
                    inventory += [move[1]]
                    clearScreen()
                    # display a helpful message
                    print("Picked up the "+move[1]+"!" )
                    # delete the item from the room
                    del rooms[currentRoom]['item']
                    input("<Press enter to continue>")
                    clearScreen()
                # otherwise, if the item isn't there to get
                else:
                    # tell them they can't get it
                    print('Can\'t get ' + move[1] + '!')

            ## Define how a player can win
            if currentRoom == 'Kitchen' and 'poison ivy leaf' in inventory and 'dead bat' in inventory and 'silver coin' in inventory and 'matches' in inventory:
                EndingText()
                input("<Press enter to Exit>")
                clearScreen()
                EndingImage()
                input("<Press enter to continue>")
                clearScreen()
                break
    elif mainmenuoptionselected == 'QUIT':
        print("THANKS FOR PLAYING!")
        input()
        break

    else:
        print("That's an invalid response!")
        input("<press enter to try again>")
        clearScreen()
