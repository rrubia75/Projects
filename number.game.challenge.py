#!/usr/bin/env python3
"""Number guessing game!"""

import random

def main():
    num= random.randint(1,100)
    while True:
        print("Guess a number between 1 and 100:")
        guess= input()
        try:

            if guess > num:
                print("Too high!")

            elif guess < num:
                print("Too low!")

            elif guess == num:
                print("Correct!")
                break
            elif guess == 'Q' or 'q':
                print("Quitting!")
                break
            else:
                print("Try again!")
        except:
            print("Nice Try!")
main()