import pymongo
connection = pymongo.MongoClient("localhost",27017)
database = connection["online"]
collection = database["user_info"]

query = {"email":"khine@gmail.com"}
try:
    data = collection.find(query)
    for d in data:
        print(d)
except Exception as error:
    print(error)