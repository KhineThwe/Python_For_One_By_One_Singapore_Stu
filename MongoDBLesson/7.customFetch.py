import pymongo
connection = pymongo.MongoClient("localhost",27017)
database = connection["online"]
collection = database["user_info"]

try:
    for i in collection.find({},{"_id":0,"phone":1}):
        print(i)
except Exception as error:
    print(error)