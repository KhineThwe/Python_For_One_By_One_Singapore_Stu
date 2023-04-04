#List comprehension
myList = ['phone','laptop','tablet']
newList = []
# for x in myList:
#     if 'phone' in myList:
#         newList.append(x)
# print(newList)
# newList = [x for x in myList if 'phone' in myList]
# print(newList)

#Syntax
# newList = [expression for item in iterable if condition==True]

#other eg
mynewList = range(5)
# for x in mynewList:#0 1 2 3 4
#     if 4 in mynewList:
#         newList.append(x)
# print(newList)
newList = [x for x in mynewList if 4 in mynewList]
print(newList)


