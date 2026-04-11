""" Question-4: write a python program that takes list of string
represent filenames or domain name split each them into its name and 
extension and group based on their extension using a dict. the extension should be the
key and the list of names should be the value. print the result in dictionary
input: ['a.py', 'b.py', 'c.java', 'd.py', 'e.py', 'f.java']
output: {'py': ['a.py', 'b.py', 'd.py', 'e.py'], 'java': ['c.java', 'f.java']}
"""

def group_by_extension():
    # takes input - list of strings
    data=list(input("Enter the list of strings: ").split(","))
    # creating a dictionary to store the result
    result = {}
    # iterating over the list of strings
    for i in data:
        # splitting the string into its name and extension
        name, extension = i.split(".")
        # adding the extension as a key and the name as a value to the dictionary
        result.setdefault(extension, []).append(name)
    return result
print(group_by_extension())