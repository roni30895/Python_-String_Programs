# 25.	Write a Python function to convert a given string to all uppercase if it contains at least 2 uppercase characters in the first 4 characters 

def upper(string):
    sub=string[:4]
    l=[]
    for i in sub:
        txt=i
        x=txt.isupper()
        if x==True:
            l.append(i)
    if len(l)>=2:
        print(string.upper())
    
string=input("\nElement the String : ")
upper(string)