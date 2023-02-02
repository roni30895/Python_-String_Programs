# Write a Python program to create a Caesar encryption 
 
def caesar_encryption(increment,string):
    cipher=''

    for i in range(len(string)):
        a=string[i]
        
        if (a.islower()):
            number=((ord(a))+(increment)-97)
            character=(number % 26) + 97
            cipher=cipher+chr(character)
        else:
            number=((ord(a)) + increment - 65)
            character=(number % 26) + 65
            cipher=cipher+chr(character)
    return cipher

string=input("\n Enter the String : ")
increment=int(input("\n Enter the incrementing number : "))
print("\n Original String : ", string)
print("\n Cipher String : ",caesar_encryption(increment,string))



