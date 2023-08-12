import pymongo
connection = pymongo.MongoClient("localhost",27017)
database = connection["online"]
collection = database["user_info"]
r_email = input("Enter your email to register: ")

for i in collection.find():
    if r_email == i["email"]:
        print("Already Register")
        break

