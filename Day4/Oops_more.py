class Employee:
    def __init__(self,name, gross_salary, allowance, deduction):
        self.name = name
        self.gross_salary = gross_salary
        self.allowance = allowance
        self.deduction = deduction
    
    def set_salary(self, gross_salary):
        self.gross_salary = gross_salary
    
    def set_allowance(self, allowance):
        self.allowance = allowance
    
    def set_deduction(self, deduction):
        self.deduction = deduction

    def get_salary(self):
        return self.gross_salary
    
    def get_allowance(self):
        return self.allowance

    def get_deduction(self):
        return self.deduction
    
    def net_salary(self):
        net = self.gross_salary + self.allowance - self.deduction
        return net

name = input("Enter the name of the Employee:")
gross_salary = int(input("Enter the gross salary of the Employee:"))
allowance = int(input("Enter the allowance amount:"))
deduction = int(input("Enter the deduction amount:"))
emp = Employee(name, gross_salary, allowance, deduction)
print(f"{name}'s final In Hand Salary:", emp.net_salary())
