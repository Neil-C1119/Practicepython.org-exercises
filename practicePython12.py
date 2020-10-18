# This program takes an original list and adds the first and last object into
# a new list using a regular function and list comprehension

# Declaring variables
starterList = [5, 10, 15, 20, 25]
newList = []

# Defining a function that will take in two lists and add the first and last object of the original list into a new one
def get_numbers(original, new):
    new.append(original[0])
    new.append(original[len(original) - 1])

# Call the function
get_numbers(starterList, newList)

# A function that uses list comprehension to return a list with the first and last object of the list it is called on
def list_comprehension(original):
    return [original[0], original[len(original) - 1]]

# Print out the returned value of the list_comprehension function using the starter list
print(list_comprehension(starterList))
