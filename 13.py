# 13.	Write a Python program to remove the nth index character from a nonempty string.
def remove(string, n):
    print(string[:n]+string[n+1:])

string=input("Enter the sring : ")
n=int(input("Enter the index of the character to remove:"))
remove(string,n)
