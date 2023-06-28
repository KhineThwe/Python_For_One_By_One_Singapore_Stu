import json
myPython = {
    "name" : "tech",
    "age": 100,
    "hobby" : ["coding","training","building IOT"]
}
print(myPython)
print(type(myPython))

with open("jdataFile1.json","w") as jsFile:
     json.dump(myPython,jsFile,indent=2,sort_keys=True)