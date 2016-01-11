import random

rand = random.randint(1,100)

def user(guess):
    if guess > rand:
        print "Lower"
    elif guess < rand:
        print "Higher"
    else:
        print "You got it"

user_guess = int(raw_input("What is your guess?"))
user(user_guess)

while user_guess != rand:
    another = int(raw_input("Not it, another guess"))
    user(another)

