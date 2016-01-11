import random

def checkAnswer(guess):                                     # Function to check the user's answer
	if guess == n: 
		return False
	elif guess > n:
		print("Too High")
	else:
		print("Too Low")
		
print("Hello, try to guess the number!")                    # Welcomes the player.

n = random.randint(1,100)                                   # Creates random Number
stateofGame = True
while stateofGame != False :                                # Crap loop
	userGuess = int(input('Choose a number between 1-100\n')) # Prompt for user answer
	stateofGame = checkAnswer(userGuess)                      # Executes the checkAnswer Functon
print("Congratulations you won!")                           # Congralutatory message upon victory.
