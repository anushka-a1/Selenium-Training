""" Question-1 - write a python code, check anagram of two strings 
write a python function that takes two strings as input and checks if they are anagrams of each other.
return true if the strings are anagrams, false otherwise."""

def is_anagram():
    # taking the two strings as input
    str1 = input("Enter the first string: ")
    str2 = input("Enter the second string: ")

    # checking if the strings are anagrams of each other
    if sorted(str1) == sorted(str2):
        return True
    else:
        return False
# calling the function
print(is_anagram())
    