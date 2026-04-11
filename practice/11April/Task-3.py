""" Question-3: write a pyhton program that takes str as input
and returns dict containing frequency of each character in the string.
eg input: 'python'
output: {'p': 1, 'y': 1, 't': 1, 'h': 1, 'o': 1, 'n': 1}"""

def char_frequency():
    str=input("Enter the string:")
    dict={}
    for n in str:
        keys=dict.keys()
        if n in keys:
            dict[n]=dict[n]+1
        else:
            dict[n]=1
    return dict
print(char_frequency())