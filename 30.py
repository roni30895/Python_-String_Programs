# 30.	Write a Python program to display formatted text (width=50) as output 

def text_wrap(string):
    start=0
    end=50
    for i in range(len(string)//50):
        print(string[start:end])
        print("")
        start=end
        end=end+50

# string=input("\n Enter the String : ")
string='''Python is a widely used high-level, general-purpose, interpreted,dynamic programming language. Its design philosophy emphasizes code readability, and its syntax allows programmers to express concepts in fewer lines of code than possible in languages such as C++ or Java.'''
text_wrap(string)
