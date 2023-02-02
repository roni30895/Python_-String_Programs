from itertools import product

def string_permutation(string,elements_in_grp):
    letters = list(string)
    results = []
    for char in product(letters, repeat =elements_in_grp):
        results.append(char)
    print(results)
string=input("\n Enter the String : ")
elements_in_grp=int(input("\n Enter how namy elements you want in a group : "))
string_permutation(string,elements_in_grp)
