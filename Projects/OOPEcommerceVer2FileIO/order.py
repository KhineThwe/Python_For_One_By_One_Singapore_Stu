from payment import *
class Order:
    def __init__(self,customer,cart,total_amount):
        self.customer = customer
        self.cart  = cart
        self.total_amount = total_amount

    def place_order(self,payment_gateway):
        try:
            if payment_gateway.process_payment(self.total_amount):
                print("Order placed successfully")
                #logic
            else:
                raise Exception("Payment failed.Order not placed")
        except Exception as e:
            print(f"Order placement failed {str(e)}")

class OrderManager:
    def __init__(self,db):
        self.db = db

    def place_order(self,customer,cart):
        total_amount = self.calculate_total_amount(cart)
        order = Order(customer,cart,total_amount)
        order.place_order(PaymentGateway())
        self.db.save_order(customer,cart)

    def calculate_total_amount(self,cart):
        total = 0
        for item in cart.items:
            product,quantity = item
            total += product.price * quantity
        return total