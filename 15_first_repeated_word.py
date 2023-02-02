# Write a Python program to find the first repeated word in a given string.

def first_repeated_word(string):
    temp = {}
    for word in string:
        if word in temp:
            return word
        else:
            temp[word] = 0
    return 'None'

string=input("\n Enter the string : ").split()
print(first_repeated_word(string))



#Tree data structure (Hindi) is used to represent hierarchical data such as organization hierachy, product categories, geographic locations etc. In this video, we will go over general tree data structure. We will cover binary trees in another tutorial. We will implement tree in python and build a tree of electronic item categories.