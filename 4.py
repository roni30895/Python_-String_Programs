#4.	Write a program to accept 10 different strings and convert it into tuple and print it.
def dictionary(n):
    
    lst=input("\nEnter the space separated string : ").split()[:n]
    t=tuple(lst)
    print("\n",t)

n=int(input("\nEnter the number how many elements you want to add :"))
dictionary(n)