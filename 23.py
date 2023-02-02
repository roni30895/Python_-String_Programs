# 23.	Write a Python program to get the last part of a string before a specified character 
def last_part(string):
    specified_char="!#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
    l=[]
    for i in specified_char:
        for j in string:
            if i==j:
                l.append(i)
    print(l)
    index=string.rfind(l[-1])
    print(string[index+1:])

string="Whe!language, #we $use ma^ny &kinds o&f se'n$ten+ces, t-o e:xpress ourse;lve<s =>we?ll i_n e[ve]ry}day"
last_part(string)