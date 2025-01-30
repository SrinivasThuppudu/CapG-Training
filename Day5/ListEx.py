class Employee:
    def __init__(self):
        self.emp = [] 

    def add_employee(self, id, name, salary):
        self.emp.append((id, name, salary)) 

    def employee_details(self):
        for e in self.emp:
            return f"Employee ID: {e[0]}\nEmployee Name: {e[1]}\nEmployee Salary: {e[2]}"

    def get_input(self):
        n = int(input("Enter number of records: "))
        for _ in range(n):
            id = int(input("Enter Employee ID: "))
            name = input("Enter Employee Name: ")
            salary = int(input("Enter Employee Salary: "))
            self.add_employee(id, name, salary) 

    def display_all_employees(self):
            for e in self.emp:
                print(f"Emp_ID: {e[0]}, Emp_Name: {e[1]}, Emp_Salary: {e[2]}")

e = Employee()
e.get_input()
e.display_all_employees()
