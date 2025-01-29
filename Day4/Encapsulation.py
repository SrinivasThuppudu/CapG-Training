class Employee:
    def __init__(self, name, salary):
        self._name = name
        self._salary = salary

    def set_salary(self, salary):
        self._salary = salary

    def get_salary(self):
        return self._salary
    
emp = Employee("Alice", 500000)
print(f"Salary before update:", emp.get_salary())
updated_salary = input("Enter the salary: ")
emp.set_salary(updated_salary)
print(f"Salary after update:", emp.get_salary())

