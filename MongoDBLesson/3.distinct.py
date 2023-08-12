import pymongo
connection = pymongo.MongoClient("localhost",27017)
database = connection["online"]
collection = database["user_info"]
_ids = collection.find().distinct('_id')
print(_ids)