#ordered,changeable,allow duplicate values,can access with index no
myList = ["juice","glasses","glasses","flower"]
myList[0] = "orange"
print(myList)

#ordered,allows duplicate values,unchangeable,can access with index no
myTuple = ("flower","juice","glasses","glasses")
#myTuple[0] = "orange" #'tuple' object does not support item assignment
print(myTuple)

#unordered,unchangeable,can't access with index no,doesn't allow duplicate values
mySet = {"flower","juice","glasses","glasses"}
#print(mySet[0]) #'set' object is not subscriptable
print(mySet)

#ordered,changeable,doesn't allow duplicate values
myDict = {
    "flower" : "rose",
    "juice": "orange juice",
    "glasses":"sunglasses",
    "glasses":"sunglasses"
}
myDict["flower"] = "jasmine"
print(myDict)