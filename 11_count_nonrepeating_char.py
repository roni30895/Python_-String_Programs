# *) Write a Python program to find the first non-repeating character in a given string

def non_repeated_char(string):
    # counting the occurance of characters
    occurance={}
    for i in string:
        if i in occurance:
            occurance[i]+=1
        else:
            occurance[i]=1
    
    # sorting the dictonary elements 
    dict_values= sorted(occurance.items(),key = lambda x:x[1])

    # printing the repeated characters
    for i in dict_values:
        if i[1] <= 1:
            print(i[0]," ",i[1])

string=input("Enter any string : ")
non_repeated_char(string)
 
