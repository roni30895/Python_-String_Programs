# 22.	Write a Python function to get a string made of the first three characters of a specified string. If the length of the string is less than 3, return the original string.  
def first_three(string):
    if len(string)<=3:
        print(string)
    else:
        print(string[:3])
string=input("\nEnter the string : ")
first_three(string)