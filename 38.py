# 38.	Write a Python program to print the following integers with '*' to the right of the specified width 

def add_star(no_of_star,number):
    add="*" * no_of_star
    print(str(number) + add)

number=int(input("\nEnter the number : "))
no_of_star=int(input("\nEnter how many star you want to add : "))
add_star(no_of_star,number)