import random
comp_number = random.randint(1,100)
guess = -1

while(guess != comp_number):
    try:
        guess = int(input("Guess a number between 1 and 100: "))
        if(guess == comp_number):
            print("Nice guess.")
        elif(guess > comp_number):
            print("Try a lower number.")
        else:
            print("Try a higher number.")    
    except ValueError:
        print("Next time use an actual number.")