# 9.	Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.
# Sample String : 'abc', 'xyz'
# Expected Result : 'xyc abz'

def replace(str1,str2):
    print(str1.replace(str1[:2],str2[:2]), str2.replace(str2[:2],str1[:2]))
str1='abc'
str2='xyz'
replace(str1,str2)