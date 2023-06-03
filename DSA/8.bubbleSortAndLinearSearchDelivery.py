def bubble_sort(delivery_orders):
    n = len(delivery_orders)
    for i in range(n-1):
        for j in range(n-i-1):
            if delivery_orders[j]["distance"] > delivery_orders[j+1]["distance"]:
                delivery_orders[j],delivery_orders[j+1] = delivery_orders[j+1],delivery_orders[j]

def linear_search(delivery_orders,order_number):
    for order in delivery_orders:
        if order["order_number"] == order_number:
            return order
    return None

if __name__ == '__main__':
    order1 = {"order_number":"A001","distance":5.4,"recipient":"John"}
    order2 = {"order_number": "A002", "distance": 3.2, "recipient": "Alice"}
    order3 = {"order_number": "A003", "distance": 6.1, "recipient": "Bob"}
    order4 = {"order_number": "A004", "distance": 4.8, "recipient": "Eve"}
    order5 = {"order_number": "A005", "distance": 2.7, "recipient": "Mike"}

    delivery_orders = [order1,order2,order3,order4,order5]
    target_order_number = "A003"

    bubble_sort(delivery_orders)

    found_order = linear_search(delivery_orders,target_order_number)

    if found_order is not None:
        print(f'Order {target_order_number} is assigned to {found_order["recipient"]} and is {found_order["distance"]} kilometers away.')
    else:
        print(f'Order {target_order_number} was not found!')


