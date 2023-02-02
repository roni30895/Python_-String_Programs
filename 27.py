# 27.	Write a Python program to remove a newline in Python

def remove_newline(string):
    re=string.splitlines()
    print("\nBefore : ",string)
    print("\nAfter : ","".join(re))

string = "\n Roahn  \n Nanabhau \n Pawar \n"
remove_newline(string)