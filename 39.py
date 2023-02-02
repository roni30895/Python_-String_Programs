# 39.	Write a Python program to display a number with a comma separator 

def comma_separator(number):
    for i in number:
        print(i,end=",")

number=input("\nEnter the number : ")
comma_separator(number)