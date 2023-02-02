# 28.	Write a Python program to check whether a string starts with specified characters. 

def string_check(string):
    specified_char="!#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
    
    if string[0] in specified_char:
        print("\n True. String Starts with specified character")
    else:
        print("\n False. String not Starting with specified character")

string=input("\nEnter the String : ")
string_check(string)
            