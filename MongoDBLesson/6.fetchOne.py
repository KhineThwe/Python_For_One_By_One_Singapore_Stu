import pymongo
connection = pymongo.MongoClient("localhost",27017)
database = connection["online"]
collection = database["user_info"]

try:
    data = collection.find_one()
    print(data)
except Exception as error:
    print(error)