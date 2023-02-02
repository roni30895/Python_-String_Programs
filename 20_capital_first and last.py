# Write a Python program to capitalize the first and last letters of each word in a given string.

def capital_first_and_last_word(string):
    for word in string:
        print(word[0].upper() + word[1:-1] + word[-1].upper(), end=" ")
    

string=input("\n Enter the string : ").split()

capital_first_and_last_word(string)