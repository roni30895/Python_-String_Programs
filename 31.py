import re

def remove_indentation(string):
    
    pattern = re.compile(r'^[ \t]+', re.MULTILINE) # re.MULTILINE ^ matches beginning of the string and each line
    
    return pattern.sub('', string)

string = "    This is an indented text.\n        It has multiple lines."
print(remove_indentation(string))
