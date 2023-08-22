class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self,product,quantity=1):
        self.items.append((product,quantity))
        print(f"Added {quantity}x{product.name} to cart")