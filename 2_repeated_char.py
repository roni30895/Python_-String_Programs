# # Write a Python program to count repeated characters in a string. 
# Sample string: 'thequickbrownfoxjumpsoverthelazydog'
# Expected output :
# o 4
# e 3
# u 2
# h 2
# r 2
# t 2

def repeated_char(string):
    # counting the occurance of characters
    occurance={}
    for i in string:
        if i in occurance:
            occurance[i]+=1
        else:
            occurance[i]=1
    
    # sorting the dictonary elements 
    dict_values= sorted(occurance.items(),key = lambda x:x[1],reverse = True )

    # printing the repeated characters
    for i in dict_values:
        if i[1]>1:
            print(i[0]," ",i[1])

string=input("Enter any string : ")
repeated_char(string)
 
