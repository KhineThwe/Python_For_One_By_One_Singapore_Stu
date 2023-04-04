#List methods
#Accessing List items
myList = ["juice","glasses","glasses","flower"]
print(myList[1])
#Change list items
myList[1] = "blackberry"
print(myList)
myList[1:3] = ["gg","hh"]
print(myList)
#Insert elements
myList.insert(4,"index4")
print(myList)
#add list elements
myList.append("book")
print(myList)
newList = ["new1","new2"]
myList.extend(newList)
print(myList)

#remove list items
myList.remove("gg")
print(myList)

#loop list
# for x in myList:
#     print(x)

#loop through the index numbers
range(5) # 0 1 2 3 4
print(len(myList))
# for i in range(len(myList)):# range(7) # 0 1 2 3 4 5 6
#     print(myList[i])

#for(start;stop;++--)
# for(int i=0;i<=5;i++){
#
# }

    # while loop
i = 0
while (i < len(myList)):
    print(myList[i])
    i = i + 1




