import pymongo

connection = pymongo.MongoClient("localhost",27017)
database = connection["online"]
collection = database["user_info"]
data = {"_id":5,"Thwe":"Coder","age":27,"Hobby":"Machine Learning"}
collection.insert_one(data)

