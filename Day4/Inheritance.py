class Parent:
    def __init__(self):
        self.bigNose = "10CM"
        print(self.bigNose)

    def display_parent(self):
        print("This is parent class")

class Child(Parent):
    def display_child(self):
        print("This is child class")
        
child = Child()
child.display_child()
child.display_parent()
print(child.bigNose)

