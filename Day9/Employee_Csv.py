import os

class Employee:
    def __init__(self, filename="employees.csv"):
        self.filename = filename
        if not os.path.exists(self.filename):
            with open(self.filename, "w") as file:
                file.write("ID,Name,Age,Department,Salary\n")

    def add_employee(self, emp_id, name, age, department, salary):
        with open(self.filename, "a") as file:  # Append mode
            file.write(f"{emp_id},{name},{age},{department},{salary}\n")

    def read_employees(self):
        with open(self.filename, "r") as file:  # Read mode
            data = file.readlines()
            for line in data:
                print(line.strip())

custom_path = "C:/Users/SRINIVAS/Desktop/CAPGEMINI TRAINING/Day9/employees.csv"
emp = Employee(filename=custom_path)

while True:
    emp_id = int(input("Enter Employee ID: "))
    name = input("Enter Employee Name: ")
    age = int(input("Enter Employee Age: "))
    department = input("Enter Employee Department: ")
    salary = int(input("Enter Employee Salary: "))

    print("\nAdding Employee...")
    print("Employee Added Successfully!\n")
    emp.add_employee(emp_id, name, age, department, salary)

    choice = input("Do you want to add another employee? (0/1):")
    if choice.lower() == "0":
        break

print("\nEmployee Records:")
emp.read_employees()
