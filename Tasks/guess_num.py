import random
mumber = random.randint(1, 25)

guess= int(input("Guess a number between 1 and 25: "))
while guess != mumber:
    if guess < mumber:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")
    guess = int(input("Guess a number between 1 and 25: "))