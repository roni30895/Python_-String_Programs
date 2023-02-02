# *) Write a Python program to lowercase the first n characters in a string. 

def lowercase(string,n):
    print(string[:n+1].lower() + string[n+1:])

string=input("\n Enter the string : ")
n=int(input("\n Enter the index upto which you want make string lowercase : "))
lowercase(string,n)
