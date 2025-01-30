class Vehicle:
    def __init__(self):
        pass
    
    def diesel(self):
        return "Vehicle will run on diesel"
    
class Car(Vehicle):
    def petrol(self):
        return "Car will run on petrol"
    
class Electric_Car(Car):
    def battery(self):
        return "Electric car will run on battery"
    
ec = Electric_Car()
print(ec.battery())
print(ec.petrol())
print(ec.diesel())