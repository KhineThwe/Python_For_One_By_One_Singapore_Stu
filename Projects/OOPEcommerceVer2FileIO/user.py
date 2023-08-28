import bcrypt

class User:
    def __init__(self,name,email,password):
        self.name = name
        self.email = email
        self.password = self._hash_password(password)

    def _hash_password(self,password):
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password.encode(),salt)
        return hashed_password.decode()

    def verify_password(self,password):
        return bcrypt.checkpw(password.encode(),self.password.encode())



class Customer(User):
    def __init__(self,name,email,password):
        super().__init__(name,email,password)

    def checkout(self,cart,db):
        print("Checkout completed.")
        db.save_order(self,cart)

class Seller(User):
    def __init__(self,name,email,password):
        super().__init__(name,email,password)
        self.inventory = []

    def add_product(self,product):
        self.inventory.append(product)
        print(f"Added {product.name} to inventory.")