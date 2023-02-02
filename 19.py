# 19.	Write a Python function to create an HTML string with tags around the word(s).  
def html_tag(tag,string):
    print('<'+tag+'>'+string+'</'+tag+'>')

tag=input("\nEnter the HTML tag : ")
string=input("\nEnter the string : ")
html_tag(tag,string)
