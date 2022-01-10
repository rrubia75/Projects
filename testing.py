#!/usr/bin/python3
"""Author: Ryan Rubia :: Purpose: RPG game project"""

from PIL import Image, ImageFont, ImageDraw
import sys, os
from time import sleep
from RPG_project.text import IntroText
ShowText = 'PYTHON RPG'
def MainMenuImage():
    ShowText= 'PYTHON RPG'
font = ImageFont.truetype('arialbd.ttf', 9)  # load the font
size = font.getsize(ShowText)  # calc the size of text in pixels
image = Image.new('1', size, 1)  # create a b/w image
draw = ImageDraw.Draw(image)
draw.text((0, 0), ShowText, font=font)  # render the text to the bitmap


def mapBitToChar(im, col, row):
    if im.getpixel((col, row)):
        return ' '
    else:
        return '#'

for r in range(size[1]):
    print(''.join([mapBitToChar(image, c, r) for c in range(size[0])]))
input("Press Enter to continue!")


def showInstructions():
    # print a main menu and the commands
    clearScreen()
    print('''
Commands:
  go [direction]
  get [item]
----------------------------------
Goal: Escape the house. Good luck!
''')
    input("Press Enter to continue!")
    clearScreen()

def showStatus():
    # print the player's current status
    print('You are in the ' + currentRoom)
    # print the current inventory
    print('Inventory : ' + str(inventory))
    # print an item if there is one
    if "item" in rooms[currentRoom]:
        print('You see a ' + rooms[currentRoom]['item'])
    #print("---------------------------")
    print('"""""""""""""""""""""""""""""')

# Shows next possible move options
def nextMove():
    print("OPTIONS: ")
    print("You can go: ")
    if currentRoom == "Hall":
        print("North to the Attic, \n"
              "East to the Dining Room, \n"
              "South to the Kitchen, \n"
              "West to the Living Room \n")
    elif currentRoom == "Kitchen":
        print("North to the Hall or "
              "Downstairs to the Basement")
    elif currentRoom == "Basement":
        print("Upstairs to the Kitchen")
    elif currentRoom == "Living Room":
        print("East to the Hall")
    elif currentRoom == "Attic":
        print("Downstairs to the hall ")
    elif currentRoom == "Dining Room":
        print("West to the Hall or "
              "South to the Garden")
    else:
        print("North to the Dining Room")

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

# an inventory, which is initially empty
inventory = []

# a dictionary linking a room to other rooms
## A dictionary linking a room to other rooms
rooms = {

    'Hall': {
        'south': 'Kitchen',
        'east': 'Dining Room',
        'west': 'Living Room',
        'north': 'Attic'
    },

    'Kitchen': {
        'north': 'Hall',
        'downstairs': 'Basement',
        'item': 'cauldron'
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

# start the player in the Basement
currentRoom = 'Basement'
MainMenuImage()
clearScreen()
IntroText()
input("press enter to continue")
clearScreen()
showInstructions()
while True:
    showStatus()
    nextMove()

# loop until player has bat, poison ivy, and silver coin. Then enters kitchen to perform spell.
while True:

    # get the player's next 'move'
    # .split() breaks it up into a list array
    # eg typing 'go east' would give the list:
    # ['go','east']
    move = ''
    while move == '':
        move = input('>')

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
        # there is no door (link) to the new room
        else:
            print('You can\'t go that way!')

    # if they type 'get' first
    if move[0] == 'get':
        # if the room contains an item, and the item is the one they want to get
        if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
            # add the item to their inventory
            inventory += [move[1]]
            # display a helpful message
            print(move[1] + ' got!')
            # delete the item from the room
            del rooms[currentRoom]['item']
            clearScreen()
        # otherwise, if the item isn't there to get
        else:
            # tell them they can't get it
            print('Can\'t get ' + move[1] + '!')
