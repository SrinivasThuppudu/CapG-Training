class Man:
    def eat(self):
        return "Man can eat food"
    
class Woman:
    def drink(self):
        return "Woman can drink water"
    
class Child(Man, Woman):
    def play(self):
        return "Child can eat food, drink water and play games"

child = Child()
print(child.eat())
print(child.drink())
print(child.play())

m = Man()
m = child
print(m.play(),"\n",m.drink(),"\n",m.eat())

w = Woman()
w = m
print(w.drink(),"\n",w.eat(),"\n",w.play())
