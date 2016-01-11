import random
number = random.randint(1,100)
print("Guess a number between 1 and 100")
found = False
while not found:
    userguess = input("What is your guess? ")
    if userguess.isalpha(): #if the users input is a strirng it asks to write a number
        print("Please enter a number!")
    elif userguess.isdigit(): #if the users input is an int then it continues with the if statements
        if number == int(userguess):
            found = True
            print("Good Job!")
        elif int(userguess) > number:
            print("Guess lower!")
        else:
            print("Guess higher!")
            
  # Note: if it is a float or a combination of string and int it just repeats the question.
