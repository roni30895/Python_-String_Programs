#3.	Write a program to accept 10 different strings and convert it into dictionary and print it.
def dictionary(n):
    lst1=list(range(1,n+1))
    lst2=input("\nEnter the space separated string : ").split()[:n]
    d=zip(lst1,lst2)
    lst_to_dict=dict(d)
    print("\n",lst_to_dict)

n=int(input("\nEnter the number how many elements you want to add :"))
dictionary(n)