# 37.	Write a Python program to print the following integers with zeros to the left of the specified width 

def add_zero(no_of_0,number):
    add="0" * no_of_0
    print(add + str(number))

number=int(input("\nEnter the number : "))
no_of_0=int(input("\nEnter how many zeros you want to add : "))
add_zero(no_of_0,number)