#8.	Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.
def replace(string):
    str=string[1:].replace('r','$')
    print(string[0] + str)

string="restart"
replace(string)