class Product:
    def __init__(self,id,name,price):
        self.id = id
        self.name = name
        self.price = price

def selection_sort(products):
    n = len(products)
    for i in range(n):
        min_index = i
        for j in range(i+1,n):
            if products[j].price < products[min_index].price:
                min_index = j
        products[i],products[min_index] = products[min_index],products[i]

def binary_search(products,target):
    low = 0
    high = len(products) - 1

    while low <= high:
        mid = (low+high)//2

        if products[mid].price == target:
            return mid
        elif products[mid].price < target:
            low = mid +1
        else:
            high = mid - 1
    return -1

if __name__ == '__main__':
    products = [
        Product(1,"Keyboard",25.99),
        Product(2, "Mouse", 19.99),
        Product(3, "Monitor", 125.99),
        Product(4, "Headphones", 225.99),
        Product(5, "Speakers", 215.99),
    ]

    #sorting
    selection_sort(products)

    target_price = float(input("Enter your target price: "))
    index = binary_search(products,target_price)

    if index != -1:
        product = products[index]
        print(f'Product found - ID:{product.id},Name:{product.name},Price:{product.price}')
    else:
        print("Product not found")
