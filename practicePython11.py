# This program will ask the user for a number and determine whether the number
# is prime or not

# Declare the divisors to be used
divisors = [2, 3, 5, 7, 9, 11]

# Get the user's number and store it in a variable
userNumber = int(input("Pick a number to test: "))

# If the user's number is more than 0
if userNumber > 0:

    # For each number in the range 2 through (the user number - 1)
    for x in range(2, userNumber - 1):

        # If the user's number divides with anything and returns no remainder
        if userNumber % x == 0:

            # Let them know and break the loop
            print("This number isn't prime.")
            break
            
        # If the user's number returns a remainder every time it is prime
        else:
            print("This number is prime.")
            break

# If the user's number is 0 it isn't prime
elif userNumber == 0:
    print("This number isn't prime.")

# If the user's number is negative it isn't prime
else:
    print("This number isn't prime.")
