# This program is a guessing game that you can exit at anytime, and it will
# keep track of the amount of tries it takes for the user to guess the number

# Import the random module
import random

# Define the function that returns a random number
def random_num():
    return random.randint(1, 10)

# Self explanatory
print("-----The Random Number Game!-----")
print("\nType 'exit' at any time to quit.")

# Set the random number
number = random_num()

# Prepare the userGuess and tries variables
userGuess = 0
tries = 0

# A loop that runs while the user's guess isn't the number AND their answer isn't exit
while userGuess != number and userGuess != "exit":
    # Get the user's guess
    userGuess = input("Guess my number between 1 and 9. . . :")

    # If the user types exit end the loop
    if userGuess.lower() == "exit":
        break

    # If the guess is too high. . .
    if int(userGuess) > number:
        print("Try a little lower")
        # Add a try
        tries += 1

    # If the guess is too low. . .
    elif int(userGuess) < number:
        print("It's higher than that")
        # Add a try
        tries += 1

    # If the guess is correct. . .
    elif int(userGuess) == number:
        # Tell the user it is correct and show them how many tries it took
        print("That's right! It took you", tries,"tries!\n\n")
        # Reset the random number
        number = random_num()
        # Reset the user's tries
        tries = 0
