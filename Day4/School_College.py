class CollegeUG:
    def __init__(self, name, degree, grade):
        self.name = name
        self.degree = degree
        self.grade = grade

    def set_info(self):
        self.name = input("Enter the name:")
        self.degree = input("Enter whether student is UG/PG:") 
        self.grade = input("Enter the Grade:")
        print(f"Name: {self.name}\nDegree: {self.degree}\nGrade: {self.grade}")

class CollegePG(CollegeUG):
    def __init__(self, name="", degree="", grade=""):
        super().__init__(name, degree, grade) 

c = CollegePG()
c.set_info()