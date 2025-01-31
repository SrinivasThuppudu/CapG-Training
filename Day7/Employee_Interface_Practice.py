from abc import ABC, abstractmethod

class Employee(ABC):
    @abstractmethod
    def work(self) -> str:
        pass
    
    @abstractmethod
    def get_salary(self) -> float:
        pass

class Manager(Employee):
    def __init__(self, name: str, salary: float):
        self.name = name
        self.salary = salary

    def work(self) -> str:
        return f"{self.name} is managing the team."

    def get_salary(self) -> float:
        return self.salary
    
class Developer(Employee):
    def __init__(self, name: str, salary: float):
        self.name = name
        self.salary = salary

    def work(self) -> str:
        return f"{self.name} is writing code."

    def get_salary(self) -> float:
        return self.salary
    
class Intern(Employee):
    def __init__(self, name: str, salary: float):
        self.name = name
        self.salary = salary

    def work(self) -> str:
        return f"{self.name} is learning and assisting."

    def get_salary(self) -> float:
        return self.salary
    
class Department:
    def __init__(self, name: str):
        self.name = name
        self.employees = []
        
    def hire(self, employee: Employee) -> None:
        self.employees.append(employee)
        print(f"{employee.name} has been hired.")
        
    def fire(self, employee: Employee) -> None:
        self.employees.remove(employee)
        print(f"{employee.name} has been fired.")

    def promote(self, employee: Employee, new_salary: float) -> None:
        employee.salary = new_salary
        print(f"{employee.name} has been promoted with a new salary of {employee.salary}.")
        
    def get_total_salary(self) -> float:
        return sum([employee.get_salary() for employee in self.employees])
    
    def show_employee(self) -> None:
        for employee in self.employees:
            print(employee.name)

Manager1 = Manager("John", 50000)
Developer1 = Developer("Alice", 60000)
Intern1 = Intern("Bob", 30000)

department = Department("IT")
department.hire(Manager1)
department.hire(Developer1)
department.hire(Intern1)
print(department.get_total_salary())
department.promote(Manager1, 60000)
department.fire(Intern1)
department.promote(Developer1, 70000)
print(department.get_total_salary())