#*) Write a Python program to count and display vowels in text. 

def count_vowels(string):
    string=string.casefold() # The term "casefold" has been used to refer to a method of ignoring cases.
    vowels='aeiou'

    vowels_count={}.fromkeys(vowels,0)
    
    for i in string:
        if i in vowels_count:
            vowels_count[i] +=1
    print("\n The number of vowles in the string are : ",vowels_count)

string=input("\n Enter the string : ")
count_vowels(string)

