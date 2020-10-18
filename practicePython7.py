# This program will take a list and add only the even numbers to a new list, then
# print it in one line
# It is also disgusting looking

# Starting list
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# This function looks through each element of the starting list, a, and if the element
# returns no remainder after dividing by 2 it will be added to the even list
even = [x for x in a if x % 2 == 0]

print(even)
