colors = ["Red","Green","Yellow","Blue"]
print(''.join(colors))

#List comprehension
mystr = "Hello"
# myList = []
# for c in mystr:
#     myList.append(c)
# print(myList)
myList = [c.upper() for c in mystr]
print(myList)

numbers = [1,2,3,4,5]
myList1 = [num*2 for num in numbers]
print(myList1)

