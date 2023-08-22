class Product:
    def __init__(self,name,price):
        self.name = name
        self.price = price

class PhysicalProduct(Product):
    def __init__(self,name,price,stock):
        super().__init__(name,price)
        self.stock = stock

class DigitalProduct(Product):
    def __init__(self,name,price,d_name):
        super().__init__(name,price)
        self.d_name = d_name

