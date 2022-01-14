#!/usr/bin/env python3
"""Author: Ryan Rubia :: Purpose: provide text for RPG game"""
import sys
from time import sleep
import random
def typingPrint(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        sleep(0.04)

def IntroText():
    typingPrint("""
Your eyes open.
As your vision begins to focus, you are laying in a dark, musky room.
You sit up and realize you are in what appears to be a basement.
The only light in the room is the moonlight peering through a tiny window with metal bars.
You see a body lying on the floor across from you.
Suddenly, you hear the body let out a low, raspy moan.
You get up, shake out the feeling of fatigue, and begin to look around.
To your left, you see a set of stairs leading up to a door.
You make your way slowly up the stairs and try the doorknob.
<The door is locked>
You start to turn around to head back down the stairs.
Suddenly, you hear an extremely loud, very high pitch shriek “Hahehehehe”.
You sprint down the stairs.
You notice that the body that was lying on the floor is now sitting up.
It is an old, skinny man with grey, shaggy hair that is sitting with his knees to his chest.
The old man is slowly rocking back and forth, staring blankly ahead.
He slowly mumbles; “That’s the Witch. I’ve been here for weeks. She’ll never let us go.
You begin to frantically search the room. You don’t find anything.
You notice the old man slowly raise his hand and point to the corner of the room.
There sits a small table with a very old book and a key sitting in front of it.
You walk to the book and try to read, but notice the language is one that you do not recognize.
However, you notice there are notes scribbled to the side in English:
To banish a Witch, you need the following ingredients;
1.) Fur of a bat 2.) Something made of silver 3.) Leaf of a poison ivy plant
Combine these ingredients into a bowl and set it on fire, and the Witch shall be banished.
As you finish reading these words, you hear the old man say;
"If you pick up that key, you’ll be able to unlock the door."
The man continues;"Just beware of the Witch. If she finds you, she’ll drag you straight back to the basement."
With these words in mind, your journey begins.""")

def EndingText():
    typingPrint('''
As you enter the kitchen with all of the items needed for the spell, you see a black, old cauldron.
You rush over to the cauldron, add the bat fur, poison ivy leaf, and silver coin to the cauldron.
You take out the matches and set the items on fire.
Somewhere in the far side of the house, you hear a deafening, high pitched scream.
In the living room, you hear a loud *CLICK*.
You run to the living room and notice a door that wasn't there before and it is slightly ajar.
You swing the door open and sprint out of the house. You are free.
YOU WIN!!!''')



def Witch():
    if RandomRoom == currentRoom:
        # print ("The witch is in "+ RandomRoom)
        print("You hear a high pitched crackle as the Witch drags you back to the basement!")
        currentRoom= 'basement'
        input("<Press Enter to continue>")
        clearScreen()
    else:
        print("The witch is in " + RandomRoom)


mylist=['kitchen', 'living room', 'dining room' , 'garden' , 'attic']
RandomRoom= random.choice(mylist)