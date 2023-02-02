# *) Write a Python program to find the first repeated character in a given string. 

def first_repeated_char(string):
    temp = {}
    for char in string:
        if char in temp:
            return char
        else:
            temp[char] = 0
    return 'None'

string=input("Enter any string : ")
print(first_repeated_char(string))