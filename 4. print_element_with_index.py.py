# # Write a Python program to print the index of a character in a string. 
# Sample string: w3resource
# Expected output:
# Current character w position at 0
# Current character 3 position at 1
# Current character r position at 2
# - - - - - - - - - - - - - - - - - - - - - - - - -
# Current character c position at 8
# Current character e position at 9

def print_index(string):
    for i in string:
        print("\n Current character", i,"position at ", string.index(i))
string= input("\n Enter the string : ")
print_index(string)
