# Write a Python program to find the first repeated character in a given string where the index of the first occurrence is smallest. 

def first_repeated_char_smallest_index(string):
  temp = {}
  for char in string:
    if char in temp:
      return char, string.index(char);
    else:
      temp[char] = 0
  return 'None'

string=input("\n Enter the string : ")
print(first_repeated_char_smallest_index(string))

