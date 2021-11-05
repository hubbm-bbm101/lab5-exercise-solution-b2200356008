import random

randomNum = random.randint(1,10)
guess = None

def getGuess():
    global guess
    guess = int(input("Guess the number in range (1, 10): "))

getGuess()

while randomNum != guess:
    if guess < randomNum:
        print("Increase your number.")
        getGuess()
    else:
        print("Decrease your number.")
        getGuess()

print("Your guess is correct!")