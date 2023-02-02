# 14.	Write a Python program to change a given string to a newly string where the first and last chars have been exchanged.

def new_string(string):
    print(string[-1]+string[1:-1]+string[0])

string=input("Enter the sring : ")
new_string(string)