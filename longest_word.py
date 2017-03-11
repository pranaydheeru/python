def longest_word():
    new_list2 = []
    myfile = open("text.txt","r")
    new_list = [line.split(' ') for line in myfile.readlines()]
    for new_list1 in new_list:
        for val in new_list1:
            new_list2.append(val)
    #print max(new_list2, key=len)
    maxlength = max(len(s) for s in new_list2)
    for k in new_list2:
        if(len(k)==maxlength):
            print(k)

longest_word()
  
  
  
