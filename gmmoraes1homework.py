import random
randomNumber = random.randrange(1, 100, 1)




correct = False
while not correct:  #while the input is not the same as the random number
    inputNumber = int(input("Enter a number lower than 100: "))
    while inputNumber > 100:
        inputNumber = int(input("Enter a number lower than 100: "))
    #avoids number higher than 100
    if randomNumber > inputNumber and randomNumber - inputNumber < 11: 
        print ("Your number was smaller than the random, but dont give up you are close to the answer" + "\n" + "your number was " + str(inputNumber))
    elif randomNumber < inputNumber and inputNumber - randomNumber > 10:
        print ("Your number was bigger than the random," + "\n" + "your number is far from the correct number" + "\n" + "your number was " + str(inputNumber))
    elif randomNumber < inputNumber and inputNumber - randomNumber < 11:
        print ("Your number was bigger than the random, but dont give up you are close to the answer" + "\n" + "your number was " + str(inputNumber))
    elif randomNumber == inputNumber:
        correct = True
        print("Congratulations you have guessed the correct number!" + "\n" +  "your number was" + " " + str(inputNumber) + " the answer was" + " " + str(randomNumber))
    else:
        print ("Your number was smaller than the random," + "\n" + "your number is far from the correct number" + "\n" + "your number was " + str(inputNumber))
         


