# The original base code is from http://inventwithpython.com/guess.py
# I will be using Python 3 coding in this game.
# In the beginning book the author states. Programmers spend   50% of the day of the time looking up
# information on Google.
#
# So when I started this I did not know how to go about it.
# I can read the code and understand it but actually making my own was beyond be, I could not see the whole picture. 
# So I copied public code and made it my own.
# About 90% of the way through I realized I was not editing code I was adding my own stuff.
# By doing it, Something just clicked.
#
# I did add a lot of stuff to the base code. like the countdown on the guesses.



print ('This is Python_Johns Homework for sliceofpython reddit group')
print (' Its [Week 1] Section 1, 2, 3 from Automate the Boring Stuff with Python.')
print ('WEEKLY PROJECT: GUESS THE NUMBER GAME')
print()
print()
print ('The computer will pick a random number between 1 and 100. The player tries to guess the number. The computer will tell the player if the guess is too high, too low or exactly right.')
print()
import random  # This imports the random module

print ('Please enter your name.')
YourName = input()  #ask for input on the YourName string

print ( YourName+ ' Please pick a number between 1 and 100.')
print (' ok ' +YourName+' You have 10 tries')
number = random.randint ( 1,100) # this lets the script know the number range 
guesses =0

print(10 - guesses, "Trys left")
while guesses < 10: # this limuts game to 10 trys
    print('Take a guess.')
    
    guess = input()
    guess = int(guess)
    guesses = guesses + 1
    
    if guess < number: # if number is less than the random numebr 
        print('That guess was to low, Please try again.')
        print(10 - guesses, "Trys left") # The code I used to count the Guesses down from 10
        
    if guess > number: # if number is higher than the random numebr 
        print('That guess was to high, Please try again.')
        print(10 - guesses, "Trys left")

    if guess == number: # Guess is euqal to the number game stops
        print (YourName+ 'That guess was to just right.')
        break
    
if guess == number: # this is the print out if the correct number is entered
        guesses = str(guesses)
        print(YourName + '! You guessed my number in ' + guesses + ' guesses!')
      

if guess != number: # to many trys 10 in this case
    number = str(number)
    print('Sorry, '+YourName+ ' The number I was thinking of was ' + number)

