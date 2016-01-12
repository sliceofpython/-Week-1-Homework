import random

# define function 'Ask', that we will ask after session of guessing
def ask():
    a = input ('''Type 'go' or 'yes' to continue\n''')
    if (a == 'go' or a == 'yes'):
        guessnumber() # we will define it later
    else:
        print('Bye-bye!')

def guessnumber(): # probably redundant function... ))
    x = int(input('Guessing number from 1 to .. what exactly? Type the max number\n'))
    print('Time to guess! The number is from 1 to ' + str(x) +', 7 attempts allowed.')
    guessesTaken = 0
    number = random.randint(1, x)

    while guessesTaken < 7: # 7 attempts to guess the number
        print('Guess!')
        guess = input() # getting user's number
        guess = int(guess) # making sure it's integer type
        guessesTaken = guessesTaken + 1 # counting guesses
        if guess + 12 < number:
            print('Very cold')
        elif guess - 12 > number:
            print('Very cold')
        elif guess + 8 < number:
            print('Cold')
        elif guess - 8 > number:
            print('Cold')
        elif guess + 4 < number:
            print('Warm')
        elif guess - 4 > number:
            print('Warm')
        elif guess + 1 < number:
            print('Kind of hot')
        elif guess - 1 > number:
            print('Kind of hot')
        elif guess < number:
            print('Volcano heat!')
        elif guess > number:
            print('Volcano heat!')
        elif guess == number:
            break
        
    if guess == number:
        guessesTaken = str(guessesTaken)
        print('You\'ve guessed the number from ' + guessesTaken + ' attempt')
        ask()
    if guess != number:
        number = str(number)
        print('Nope, the number was: ' + number)
        
ask() # starts the function that we've defined at the very beginning
