#7.	Write a Python program to get a string made of the first 2 and last 2 characters of a given string. If the string length is less than 2, return the empty string instead.

def first_last(string):
    if len(string)==1:
        print("\nEmpty String")
    elif len(string)==2:
        print(string * 2)
    else:
        print(string[0:2] + string[-2:])

string=input("Enter any string : ")
first_last(string)