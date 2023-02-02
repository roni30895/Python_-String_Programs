# # Write a Python program to swap commas and dots in a string. 
# Sample string: "*)*),*)
# Expected Output: "*)*).*)

string=input("\n Enter the String : ")


list_string = list(string)
for i in range(len(list_string)):
    if list_string[i] == ",":
        list_string[i] = "."
    elif list_string[i] ==".":
        list_string[i] = ","
print ("".join(list_string))




