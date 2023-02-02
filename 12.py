#12.	Write a Python function that takes a list of words and return the longest word and the length of the longest one.

def longest(lst):
    long=lst[0]
    for i in lst:
        if len(long)<len(i):
            long=i
    print("\nLongest World :",long)
    print("\nLength of longest world :",len(long))

lst=input("Enter the space separated string : ").split()
longest(lst)


    
