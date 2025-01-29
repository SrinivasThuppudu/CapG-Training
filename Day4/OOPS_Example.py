'''
class Employee:
    def __init__(self, emp_id, emp_name):
        self.emp_id = emp_id
        self.emp_name = emp_name

    def data(self):
        return f"{self.emp_name} ID: {self.emp_id}"
    
emp1 = Employee(1, "Srini")
emp2 = Employee(2, "Venkat")

print("Emp1", emp1.data())
print("Emp2", emp2.data())

'''

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display(self):
        print(f"Car {self.brand} is from {self.model}")

c1 = Car('Jaguar', 'OSI Model')
c2 = Car("BMW", 'Two Crores Model')

c1.display()
c2.display()