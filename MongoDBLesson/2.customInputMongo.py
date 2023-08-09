import pymongo
import random
connection = pymongo.MongoClient("localhost",27017)
database = connection["online"]
collection = database["user_info"]

if __name__ == '__main__':
    while True:
        try:
            user_id = random.randint(10,100000)
            email:str  = input("Enter useremail")
            password:str = input("Enter userpassword")
            phone:int = int(input("Enter userphone: "))

            data_form = {"_id":user_id,"email":email,"password":password,"phone":phone}

            ids = collection.insert_one(data_form)
            print("inserted id",ids.inserted_id)
        except Exception as err:
            print(err)