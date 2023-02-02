# Write a Python program to split a string on the last occurrence of the delimiter. 

def split_string(string,delimiter):
    print(string.rsplit(delimiter,1))

string=input("\n Enter the String : ")
print("Before Splitting:",string)
delimiter=input("\n Enter the delimiter : ")
split_string(string,delimiter)
 