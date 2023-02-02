# 24.	Write a Python function to reverse a string if its length is a multiple of 4.  

def reverse(string):
    if len(string)%4==0:
        print(string[::-1])
    else:
        print("\n SORRY! Invalid input : Lenth of string is not multiple of 4")
string=input("\nEnter the string : ")
reverse(string)