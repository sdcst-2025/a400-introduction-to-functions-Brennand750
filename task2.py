"""
Create a program to play a number guessing game
There should be a function:
title()
displays instructions and how to play

game()
plays the game

This will be silimar to something you have already done, but in this task you 
are breaking the code up into different sections to make each a function.
"""
import random
def title():
    print("the main goal of the game is to guess a random number that generated from 1 to 100 in the least amount of guesses. / Also the game will tell you if your guess is too high or too low.")

def game():
    rnum = random.randint(1,100)
    attempts = 0
    print("Please guess a random number")
    while True:
        guess = input("Please guess a random number from 1 to 100")
        guess = int(guess)
        attempts += 1
        if guess > rnum:
            print("Your guess is too high")
        elif guess < rnum:
            print("Your guess is too low")
        else:
            print("You are correct")
            print("it took you this many trys", attempts)
            break

if __name__ == "__main__":
    title()
    game()
        

