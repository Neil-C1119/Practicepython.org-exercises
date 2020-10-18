# This program will ask the user for a number and will print out the divisors
# 2 - 12 that divide evenly

# Declare the divisors to be used
divisors = range(2, 13)

# Get the user's number and store it in a variable
userNumber = input("Pick a number: ")

# A loop that goes through each number in the divisors list
for x in divisors:
    # If the user's number divided by the divisor returns no remainder
    if int(userNumber) % x == 0:
        # Print the divisor
        print(x)
