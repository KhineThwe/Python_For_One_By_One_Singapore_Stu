with open('data.txt','r') as file:
    if file:
        print("The file Pointer at byte",file.tell())
        contents = file.read()
        print("The file pointer at byte",file.tell())
    else:
        print("something wrong")

#r ---> 0
#w ----> 0
#a ---> last
