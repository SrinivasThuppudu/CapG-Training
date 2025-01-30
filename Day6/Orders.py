from Customers import Customers
import datetime
class Orders(Customers):
    def __init__(self):
        super().__init__()  # Inherit from Customers class
        self.orders_list = []
    
    def add_order(self, **kwargs):

        order_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Current date and time
        kwargs['order_date'] = order_date  # Add current date to the order
        # Append the order details as a dictionary to the orders list
        self.orders_list.append(kwargs)

    def display_orders(self):

        print("\nOrder Details:")
        for order in self.orders_list:
            print(f"Order ID: {order['order_id']}, Customer ID: {order['cust_id']}, "
                  f"Status: {order['order_status']}, Date and Time: {order['order_date']}, "
                  f"Store ID: {order['store_id']}, Staff ID: {order['staff_id']}")