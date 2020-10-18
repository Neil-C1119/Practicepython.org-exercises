# I'm going to make this more complicated than the exercise calls for

# Import the random module
import random

# Create two empty lists to compare
list1 = []
list2 = []

# Create an empty list to push any similar numbers into
listSame = []

# For loops to fill the two lists with random numbers to compare
for x in range(1, 9):
    list1.append(random.randrange(100))
for x in range(1, 13):
    list2.append(random.randrange(100))

# For loop to check through every number in list1
for x in list1:
    # If the number in list1 is also in list2
    if x in list2:
        # Push that number into the list that holds similar numbers
        listSame.append(x)

# If the same number list has at least one element
if len(listSame) > 0:
    # Print the list
    print(listSame)
# If the list doesn't have at least one element
else:
    # Print this message
    print("There are no similar numbers in either of the lists.")
