# This program will ask the user for a word and check if it is a palindrome

# Take the user's word
palindromeTest = input("Type in a word that you would like to check: ")

# If the word the user gives is the same backwards as it is forwards
if palindromeTest[::-1] == palindromeTest:
    print("This word is a palindrome")
