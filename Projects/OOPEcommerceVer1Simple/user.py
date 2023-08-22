class User:
    def __init__(self,name,email,password):
        self.name = name
        self.email = email
        self.password = password

class Customer(User):
    def __init__(self,name,email,password):
        super().__init__(name,email,password)

    def checkout(self):
        print("Checkout completed.")

class Seller(User):
    def __init__(self,name,email,password):
        super().__init__(name,email,password)
        self.inventory = []

    def add_product(self,product):
        self.inventory.append(product)
        print(f"Added {product.name} to inventory.")