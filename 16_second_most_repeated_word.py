#  Write a Python program to find the second most repeated word in a given string. 

def second_most_repeated_word(string):
    if len(string) > 1:
        count_word = dict()
    
        for word in string:
            if word in count_word:
                count_word[word] += 1
            else:
                count_word[word] = 1
    
        list_values=[]

        for i in count_word:
            list_values.append(count_word.get(i))

        print(list_values)

        soretd_list=sorted(set(list_values),reverse=True)
        print(soretd_list)

        second_most_repeated=soretd_list[1]
        
        for i in count_word:
            if second_most_repeated == count_word.get(i):
                print(i,"---->",second_most_repeated)
    else:
        print("\n Invalid Input... Please inert correct input")
    


string=input("\n Enter the string : ").split()
print(second_most_repeated_word(string))
 
