class Customers:
    def __init__(self):
        # Initialize an empty list to store customers
        self.customer_list = []
    
    def add_customer(self, **kwargs):
        # Append the customer details as a dictionary to the customer list
        self.customer_list.append(kwargs)

    def display_customers(self):
        print("\nCustomer Details:")
        for customer in self.customer_list:
            print(f"Customer ID: {customer['cust_id']}, Name: {customer['name']}, "
                  f"Phone: {customer['phone']}, Email: {customer['email']}, "
                  f"Address: {customer['address']}")