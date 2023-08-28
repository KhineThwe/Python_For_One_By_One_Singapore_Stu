class PaymentGateway:
    def process_payment(self,amount):
        try:
            print(f"Processing payment of ${amount:.2f}")
            print("Payment processed successfully")
            return True
        except Exception as e:
            print(f"Payment failed {str(e)}")
            return False
