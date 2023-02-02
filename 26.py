# 26.	Write a Python program to sort a string lexicographically.

def sort(string):
    l=[]
    for i in string:
        l.append(i)
    print(sorted(l))

string=input("\nEnter the string : ")
sort(string)