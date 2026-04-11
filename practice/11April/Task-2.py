""" Question-2- write python program that takes sentence as input
and return dictionary where each word is mapped to a numeric value
based on specific condition applied to the word.
eg input: 'python is a programming language'
output: {'python': 6, 'is': 2, 'a': 0, 'programming': 10, 'language': 6}"""

def word_frequency():
    sentence = input("Enter a sentence: ")
    words = sentence.split()
    frequency = {}
    for word in words:
        n=word.count('a')
        frequency[word] = len(word) - n
    # subtract the frequency of 'a' from the frequency of each word
    return frequency
result = word_frequency()
print(result) 