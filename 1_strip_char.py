# Write a Python program to strip a set of characters from a string. 

def Strip_char(string,char):
    char_list=[]
    for item in char:
        char_list.append(item)
   
    for i in char_list:
        print(i)
        str=string.replace(i,'')
    print("\n Stripped String is : ",str)

if __name__=="__main__":
    string=input("\n Enter the String : ")
    char=input("\n Enter the set of char which you want to strip :  ")
    Strip_char(string,char)
