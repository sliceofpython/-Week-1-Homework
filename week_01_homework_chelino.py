#This is Chelino's heavily commented [Week 1] homework project
#It assigns a random value to an variable and asks the user to keep guessing until correct
#note: built for Python 3

#import the random module to be able to use the randint function
import random

#this gets a random value using the randint function from the random module
theNumber = random.randint(1, 100)

#welcome and instructions here
print("Welcome friend, let's play a game.")
print("I'm thinking of a number between 1 and 100, guess what it is.")

#this while loop keeps running until the correct answer is guessed
while True:
    #this gets the user's guess
    guess = input()
    #converts the user's guess into an int variable
    guess = int(guess)
    #if, elif, else evaluates the guess and theNumber
    if guess == theNumber:
        print("You got it!")
        #break ends the while loop (and the program since there are no more commands after this)
        break
    elif guess > theNumber:
        print("Sorry, that's too high. Try again.")
    else:
        print("Sorry, that's too low.  Try again.")
