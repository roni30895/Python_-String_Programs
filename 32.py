# 32.	Write a Python program to add prefix text to all of the lines in a string.  
from textwrap import *
def add_prefix(string):
    start=0
    end=50
    for i in range(len(string)//50):
        line=string[start:end]
        prefix=indent(line,'> ')
        print("\n",prefix)
        start=end
        end=end+50

# string=input("\n Enter the String : ")
string='''Python is a widely used high-level, general-purpose, interpreted,dynamic programming language. Its design philosophy emphasizes code readability, and its syntax allows programmers to express concepts in fewer lines of code than possible in languages such as C++ or Java.'''
add_prefix(string)