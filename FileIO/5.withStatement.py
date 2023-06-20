#with statement ---> exception ----> file auto off

with open('data4.txt','r') as file:
    if file:
        contents = file.read()
        print(contents)
    else:
        print("Something wrong")
