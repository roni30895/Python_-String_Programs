# 15.	Write a Python program to remove characters that have odd index values in a given string.
def odd_index(string):
    l=[]
    for i in string:
        evenindex=string.index(i)
        if evenindex % 2==0:
            l.append(i)
    print("".join(l))
    #OR
    print(string[::2])

string=input("Enter the sring : ")
odd_index(string)

