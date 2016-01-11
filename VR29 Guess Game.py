# Guess the number game.
# By VR29
import random

min = 1
max = 100
tries = 5

number = random.randint(min,max)
guesses_taken = 0

try:
    input_number = int(input("Guess a number between %s and %s: " % (min,max)))
    guesses_taken += 1
    while guesses_taken != tries:
        if input_number == number:
            print("You guessed the right number in %s guesses!" % (guesses_taken))
            break
        elif input_number < number:
            input_number = int(input("The number you guessed is too low. Guess again: "))
            guesses_taken += 1
        elif input_number > number:
            input_number = int(input("The number you guessed is too high. Guess again: "))
            guesses_taken += 1
    else:
        print("You did not guess the number. The correct number was %s." % (number))

except ValueError:
    print("Input is not a number.")