import random
n = random.randint(1,20)
n_guess = 0
guess = ''
while guess != n:
    print("Guess the number. It's between 1 and 20.")
    guess = int(input())
    if guess < n:
        print('Too low.')
        n_guess += 1
    elif guess > n:
        print('Too high.')
        n_guess += 1
print('Correct. You guessed it in ' + str(n_guess) + ' attempts.')
            
