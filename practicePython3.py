# This program will ask the user for a number, and then will print out a new
# list containing any number in the original list that is less than the user's number

# Declaring a list to start with, and a new list that will contain numbers lower than the user's
list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
newList = []

# Grab the user's number and store it in a variable
number = input("Type a number: ")

# A loop that goes through every list element
for x in list:
    # If the list element is less than the user's number. . .
    if x < int(number):
        # Append that list item to the new list
        newList.append(x)

# Print the new list
print(newList)
