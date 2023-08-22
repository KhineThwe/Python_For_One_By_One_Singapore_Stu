from user import Customer,Seller
from product import PhysicalProduct,DigitalProduct
from cart import ShoppingCart

if __name__ == '__main__':
    #Create users
    customer = Customer("John","john@gmail.com","john")
    seller = Seller("Smith","smith@gmail.com","smith")

   #Create products
    laptop = PhysicalProduct("Laptop",99.99,5)
    ebook = DigitalProduct("E-book",19.99,"book.pdf")

   #Add Products to seller's inventory
    seller.add_product(laptop)
    seller.add_product(ebook)

   #Add Products to customers's shopping cart
    cart = ShoppingCart()
    cart.add_item(laptop,2)
    cart.add_item(ebook)

    customer.checkout()



