from vehicle import *

print("Tes Parent")
veh = Vehicle(2018, 2019)
print(f'Vehicle Year : {veh.year}')
print(f'Vehicle Price : {veh.price}')

print("\n\nTes Child : Car")
bmw = Car(2016, 2000)
bmw.park(1)
bmw.pay_tax()

print("\n\nTes Child : Motorcycle")
ninja = Motorcycle(2017, 1500)
ninja.park(1)
ninja.pay_tax()

print("\n\nTes Child : Bicycle")
bmx = Bicycle(2015, 1000)
bmx.park(1)
bmx.pay_tax()