import random

# This is a very simple concept, this simple concept code are help you to understand random module of python.
coinFlip = random.randint(1,2)
# Take a user input for guess the coin match.
userGuess = str(input("Please choose Lion or Tiger:  "))
if userGuess == "Tiger":
    guess = 1
elif userGuess == "Lion":
    guess = 2
else:
    guess = 0

if coinFlip == guess:
    print("Congratulation! You won the coin flip.")
else:
    print("Don't worry, play again try again.")