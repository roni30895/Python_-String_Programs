

def maximum_character(string):
    # counting the occurance of characters
    occurance={}
    for i in string:
        if i in occurance:
            occurance[i]+=1
        else:
            occurance[i]=1
    max_char=max(occurance, key=occurance.get)
    return max_char

string= input("\n Enter the String : ")
print(maximum_character(string))
