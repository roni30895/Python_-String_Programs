# 20.	Write a Python function to insert a string in the middle of a string.  
def insert_middle(symbol,string):
    print(symbol[:2]+string+symbol[2:])

insert_middle('[[]]','python')