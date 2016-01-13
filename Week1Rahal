import random
def guess_game():
    print("Welcome, try to guess my 1 to 100 number!")
    n = 0 #number of guesses
    condition = True #condition, to avoid using break
    my_number = random.randint(1,100) #random number
    while condition: #the game won't stop until the user guess it correctly
        guess = input('Take a guess: ')
        try:
            int(guess)
        except ValueError: #checks if the input is an integer
            print ('Not a valid guess')
            n += 1 #adds 1 to the number of guesses you made
            continue
        guess = int(guess) # str to int, i know the input is correct
        if guess > my_number:
            print ('Your guess was too high')
            n += 1
            continue
        if guess < my_number:
            print ('Your guess was to low')
            n += 1
            continue
        else:
            print('Your got it! %d was my number and you took %d guesses' %(my_number,n) )
            condition = False
    print ('Thank you for playing.')
guess_game()
