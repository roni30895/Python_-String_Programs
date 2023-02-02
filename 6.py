#6.	Write a Python program to count the number of characters (character frequency) in a string
def count_characters(string):
    char_count = {}
    for char in string:
        char_count[char] = char_count.get(char, 0) + 1
    return char_count

print(count_characters("hello"))


