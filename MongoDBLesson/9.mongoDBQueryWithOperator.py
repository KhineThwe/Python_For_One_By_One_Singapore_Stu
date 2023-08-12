import pymongo
import random
connection = pymongo.MongoClient("localhost",27017)
database = connection["online"]
collection = database["user_info"]

query = {"_id": {"$gt":40187}}
# query = {"name": {"$gt":"K"}}
try:
    data = collection.find(query)
    for d in data:
        print(d)
except Exception as error:
    print(error)