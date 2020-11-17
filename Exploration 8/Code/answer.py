class Vehicle:
    def __init__(self, name, milage):
        self.name = name
        self.milage = milage
    
    def drive(self, miles):
        self.milage -= miles
    
    def __str__(self):
        return f'{self.name} has {self.milage}'

class Truck(Vehicle):
    def __init__(self, milage, money):
        super().__init__("Truck", milage)
        self.money = money
    
    def buy(self, price):
        self.money -= price 
    
    def sell(self, price):
        self.money += price
    
    def __str__(self):
        return f'{super().__str__()} and you have {self.money} left'

# Testing
truck = Truck(300, 500)
print(truck)
input()
truck.drive(20)
print(truck)
input()
truck.sell(200)
print(truck)
input()
truck.buy(300)
print(truck)
