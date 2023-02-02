# 21.	Write a Python function to get a string made of 4 copies of the last two characters of a specified string (length must be at least 2)

def copies(string):
    if len(string)>=2:
        print(4*string[-2:])
    else:
        print("\nInvalid input: Enter the string of more than 2 character ")

string=input("\nEnter the string of more than 2 character ")
copies(string)