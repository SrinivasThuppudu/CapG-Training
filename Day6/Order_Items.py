from Orders import Orders
class Order_Items(Orders):
    def __init__(self):
        super().__init__()  # Inherit from Orders class
        self.order_items_list = []
    
    def add_order_item(self, **kwargs):

        # Append the order item details as a dictionary to the order items list
        self.order_items_list.append(kwargs)

    def display_order_items(self):
        
        print("\nOrder Items Details:")
        for item in self.order_items_list:
            print(f"Order ID: {item['order_id']}, Item ID: {item['item_id']}, "
                  f"Product ID: {item['product_id']}, Quantity: {item['quantity']}, "
                  f"List Price: {item['list_price']}, Discount: {item['discount']}")
