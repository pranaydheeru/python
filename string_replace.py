def string_replace():
    k=0
    new_string = ""
    old_string = input("Enter the string to be modified: ")
    p = old_string[0]
    for i in old_string:
        k += 1
        if(k>1):
            if(i==p):
                new_string += "$"
            else:
                new_string += i
        else:
           new_string += i 
    print("Modified string: " + new_string)


string_replace()
