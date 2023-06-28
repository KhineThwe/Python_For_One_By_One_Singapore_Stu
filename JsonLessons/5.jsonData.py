import json
with open("jdataFile1.json") as jsFile:
    data = json.load(jsFile)
    print(data)
    print(type(data))

for i in data['hobby']:
    print(i)

with open("newjDatFile.json","w") as jsFile1:
    json.dump(data,jsFile1,indent=2)