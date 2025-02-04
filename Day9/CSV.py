import os

class Employee:
    def __init__(self, file = "emp.csv"):
        self.file = file
        if not os.path.exists(self.file):
            with open(self.file, "w"):
                file.write("Id, Name, Salary\n")

    def add_emp(self, id, name, salary):
        with open(self.file, "a") as file:
            file.write(f"{id}, {name}, {salary}\n")

    def read_emp(self):
        with open(self.file, "r") as file:
            data = file.readlines()
            for line in data:
                print(line.strip())

path = "C:/Users/SRINIVAS/Desktop/CAPGEMINI TRAINING/Day9/emp.csv"
emp = Employee()
emp.add_emp(101, "Srini", 32000)
emp.add_emp(102, "Venkat", 31000)
print("\nEmployee Records:")
emp.read_emp()