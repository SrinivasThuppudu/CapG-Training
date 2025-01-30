class Customers:
    def __init__(self):
        self.customer_list = []
    
    def add_customers(self, cust_id, name, phone, email, address):
        self.customer_list.append((cust_id, name, phone, email, address))

class Orders:
    def __init__(self):
        self.orders_list = []

    def add_orders(self, order_id, cust_id, order_status, order_date, store_id, staff_id):
        self.orders_list.append((order_id, cust_id, order_status, order_date, store_id, staff_id))

class Order_Items:
    def __init__(self):
        self.order_items_list = []

    def add_order_items(self, order_id, item_id, product_id, quantity, list_price, discount):
        self.order_items_list.append((order_id, item_id, product_id, quantity, list_price, discount))

# Create instances of each class
customers = Customers()
orders = Orders()
order_items = Order_Items()

# Add customers
customers.add_customers(1, "John Doe", "9876543210", "john@example.com", "123 Street, NY")
customers.add_customers(2, "Jane Doe", "8765432109", "jane@example.com", "456 Avenue, LA")

# Add orders
orders.add_orders(101, 1, "Shipped", "2024-08-30", 5, 2)
orders.add_orders(102, 2, "Processing", "2024-08-31", 3, 1)

# Add order items
order_items.add_order_items(101, 1, 501, 2, 100.0, 10.0)
order_items.add_order_items(102, 2, 502, 1, 50.0, 5.0)

# Print stored data
print("Customers:", customers.customer_list)
print("Orders:", orders.orders_list)
print("Order Items:", order_items.order_items_list)

