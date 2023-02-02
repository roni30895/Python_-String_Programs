# 35. Write a Python program to print the following numbers up to 2 decimal places with a sign 
def dec_with_sign(num):
    print("{:+.2f}".format(num))
num=float(input("\n Enter the number with decimal point : "))
dec_with_sign(num)