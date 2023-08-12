import pymongo
connection = pymongo.MongoClient("localhost",27017)
database = connection["online"]
collection = database["user_info"]
data = [
    {"_id":6,"TunTun":"CrazyCoder","age":27,"Hobby":"BuildingTools"},
    {"_id":7,"SuSu":"CrazyCoder Senior","age":28,"Hobby":"BuildingTools"},
    {"_id":8,"PhyuPhyu":"CrazyCoder Junior","age":29,"Hobby":"BuildingTools"}
]
try:
    obj = collection.insert_many(data)
    print("Data are successfully inserted")
    print(obj.inserted_ids)
except Exception as error:
    print(error)