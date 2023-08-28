from user import Customer,Seller
import json

class CustomEncoder(json.JSONEncoder):
    def default(self,obj) :
        if isinstance(obj,Customer):
            return {
                "__class__": "Customer",
                "__name__": obj.name,
                "__email__" : obj.email,
                "__password__":obj.password
            }
        elif isinstance(obj,Seller):
            return {
                "__class__": "Seller",
                "__name__": obj.name,
                "__email__": obj.email,
                "__password__": obj.password,
                "__inventory__":obj.inventory
            }
        return super().default(obj)

class Database:
    def __init__(self,file_path):
        self.file_path = file_path#data.db

    def add_user(self,user):
        users = self.load_data()
        users.append(user)
        self.save_data(users)

    def save_order(self,customer,cart):
        orders = self.load_data()
        orders.append({"customer": customer.name,
                       "cart": [(item[0].name,item[1])for item in cart.items]})
        self.save_data(orders)

    #get_orders
    def get_orders(self):
        orders = self.load_data()
        if isinstance(orders,list):
            return orders
        return []

    def load_data(self):
        try:
            with open(self.file_path, "r") as file:
                try:
                    data = json.load(file)
                except json.JSONDecodeError:
                    data = []
        except FileNotFoundError:
            data = []
        return data


    def save_data(self,data):
        try:
            with open(self.file_path, "w") as file:
                json.dump(data, file, cls=CustomEncoder)
            print("Data saved successfully")
        except Exception as e:
            print(f"Failed to save data: {str(e)}")