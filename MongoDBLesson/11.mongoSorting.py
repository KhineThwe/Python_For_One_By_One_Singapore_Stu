import pymongo
connection = pymongo.MongoClient("localhost",27017)
database = connection["online"]
collection = database["user_info"]

try:
    # data = collection.find().sort("email")
    data = collection.find().sort("email",-1)
    for d in data:
        print(d)
except Exception as error:
    print(error)
#default -> ascending
#descending ---> direction parameter ---> -1