# Write a Python program to check whether a string contains all letters of the alphabet. 
def alpha_check(string):
    alphabets="abcdefghijklmnopqrstuvwxyz"
    string=string.lower()
    return all(char in string for char in alphabets)
    

string=input("\n Entet the string : ")
alpha_check(string)

if alpha_check(string):
    print("The string contains all aplhabets")
else:
    print("The strign not contains all alphabets.")
