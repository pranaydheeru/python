def duplicate_word():
    new_list2 = []
    new_list3 = []
    myfile = open("text.txt","r")
    new_list = [line.split(' ') for line in myfile.readlines()]
    for new_list1 in new_list:
        for val in new_list1:
            new_list2.append(val)
    for item in new_list2:
        if item not in new_list3:
            new_list3.append(item)
    print (new_list3)

duplicate_word()
