# This program will ask the user for a number and test whether it is even
# or odd, and if it is divisible by 4 it will print a different message than
# if it was just even

# Get the user's number
userNumber = input("Give me a number: ")

# Defining a function to test the user's number
def numberTest(number):
    # If the number is divisible by 4
    if number % 4 == 0:
        print("This number is divisible by 4")
    # If the number is divisble by 2, but not 4
    elif number % 2 == 0:
        print("This number is even")
    # If the number is not divisible by 2 or 4, then it's odd
    else:
        print("This number is odd")

# Call the function I defined with the user's number as the argument converted into an integer
numberTest(int(userNumber))
