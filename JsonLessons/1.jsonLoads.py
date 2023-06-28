"""
Python                 JSON
--------------------------------
dict                   object
list,tuple             array
str                    string
int,long,float           number
True                     true
False                    false
None                     null
-------------------------------
JSON ---> JavaScript Object Notation

JSON Encoding (Serialization)
json.dumps():Convert Python object to json string
json.dump():Write Python Object to a file in JSON format

JSON Decoding(Deserialization)
json.loads():Convert json string to python object
json.load():Read a json file and convert it to a Python Object
#https://jsonlint.com/
"""
import json
myJson = """
{
    "name" : "tech",
    "age": 100,
    "hobby" : ["coding","training","building IOT"]
}
"""
data = json.loads(myJson)#Decoding
print(data)
print(type(data))
