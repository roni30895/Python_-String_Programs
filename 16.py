# 16.	Write a Python program to count the occurrences of each word in a given sentence.
def word_occurance(string):
    l=string.split()
    occurance={}
    for i in l:
        if i in occurance:
            occurance[i]+=1
        else:
            occurance[i]=1
    print(occurance)

string=input("Enter the sring : ")
word_occurance(string)