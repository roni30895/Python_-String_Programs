# Move spaces to front

def move_spaces_to_front(string):
    list=[]
    for char in string:
        if char!=" ":
            list.append(char)
    # print(list)
    space_length=(len(string) - len (list) )
    # print(space_length)
    spaces_in_front=" " * space_length

    return (spaces_in_front + "".join(list))

string= input("\n Enter the string : ")
print(move_spaces_to_front(string))


