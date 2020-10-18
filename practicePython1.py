# This program will ask a user for their name, age, and the amount of times
# they want to see the personalized message, and will print their personalized
# message the specified amount of times

# Get the user's name, age, and amount of messages
userName = input("What is your name? : ")
userAge = input("How old are you? : ")
messageAmount = input("How many times would you like the message to appear? : ")

# Establish this current year, didn't want to use extra modules
thisYear = 2020

# Calculate the year the user will turn 100 based on their age and this current year
oneHundred = thisYear + (100 - int(userAge))

# A loop to print this personalized message their specified amount of times
for x in range(int(messageAmount)):
    # The %s is used to format and insert the variables inside of this tuple vvvvv
    print("\n%s, you will be 100 years old in the year %s" % (userName, oneHundred))
