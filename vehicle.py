# i. Parent Class
class Vehicle:
    # Initializer / Instance attributes
    def __init__(self, year, price):
        self.year = year
        self.price = price

# ii. Child Class dari Vehicle
class Car(Vehicle):
    # Attribute
    wheel_count = 4
    capacity = 6

    # Method
    def pay_tax(self):
        print(f'Tax = {0.15*self.price}')

    def park(self, hour):
        fee = int(hour) * 1250 * self.wheel_count
        if(self.capacity > 5):
            fee += 5000
        print(f'Parking Fee = {fee}')

class Motorcycle(Vehicle):
    # Attribute
    wheel_count = 2
    capacity = 2

    # Method
    def pay_tax(self):
        print(f'Tax = {0.1*self.price}')

    def park(self, hour):
        fee = int(hour) * 1250 * self.wheel_count
        if(self.capacity > 5):
            fee += 5000
        print(f'Parking Fee = {fee}')

class Bicycle(Vehicle):
    # Attribute
    wheel_count = 2
    capacity = 1

    # Method
    def pay_tax(self):
        print(f'Tax = no tax')

    def park(self, hour):
        fee = int(hour) * 1250 * self.wheel_count
        if(self.capacity > 5):
            fee += 5000
        print(f'Parking Fee = {fee}')