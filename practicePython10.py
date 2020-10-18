# This program takes two lists of random numbers and will add any of the numbers
# that appear in both into a new list using list comprehension with no duplicates
# ex.
# list = [x for x in otherList if x % 2 == 0]

# Import the random module
import random

# Create two empty lists to compare
list1 = []
list2 = []

# For loops to fill the two lists with random numbers to compare
for x in range(1, 9):
    list1.append(random.randrange(100))
for x in range(1, 13):
    list2.append(random.randrange(100))

# Create an empty list to push any similar numbers into
listSame = [set(x for x in list1 if x in list1 and x in list2)]

print(list1)
print(list2)
print(listSame)
