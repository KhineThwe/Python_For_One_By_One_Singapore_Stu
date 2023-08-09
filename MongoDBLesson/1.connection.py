import pymongo

connection = pymongo.MongoClient("localhost",27017)
database = connection["online"]
collection = database["user_info"]
data = {"Khine":"Coder","age":25,"Hobby":"Building Apps"}
collection.insert_one(data)

