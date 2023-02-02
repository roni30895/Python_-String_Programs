# 11.	Write a Python program to find the first appearance of the substrings 'not' and 'poor' in a given string. If 'not' follows 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string

def remove_not_poor(string):
    not_index=string.rfind("not")
    # print(not_index)
    
    poor_index=string.rfind("poor")
    # print(poor_index)
    
    remove_string=string[not_index:poor_index+4]
    # print(remove_string)
    
    replace_string=string.replace(remove_string,"good")
    print(replace_string)
    
string="Rahul is not a poor person!"
remove_not_poor(string)