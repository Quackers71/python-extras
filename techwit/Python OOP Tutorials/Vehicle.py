# Inheritance & Overloading

class Vehicle(): # Constructor class
    def __init__(self, name, price, gas, colour):
        self.name = name
        self.price = price
        self.gas = gas
        self.colour = colour

    def outPut(self):
        print("My Vehicle is a", self.name)
        print("The price is £", self.price)
        print("It has", self.gas,"litres of fuel")
        print("The colour is", self.colour)

    def fillUpTank(self):
        self.gas = 100

    def emptyTank(self):
        self.gas = 0

    def gasLeft(self):
        return self.gas


class Car(Vehicle): # Child class of the Vehicle class
    def __init__(self, name, price, gas, colour, speed):
        super().__init__(name, price, gas, colour)
        self.speed = speed

    def outPut(self):
        print("My Vehicle is a", self.name)
        print("The price is £", self.price)
        print("It has", self.gas,"litres of fuel")
        print("The colour is", self.colour)
        print("The top speed is", self.speed)

    def beep(self):
        print("Beep! Beep!")


class Truck(Car): # Child class of the Car class
    def __init__(self, name, price, gas, colour, speed, tyres):
        super().__init__(name, price, gas, colour, speed)
        self.tyres = tyres

    def beep(self):
        print("Honk! Honk!")
        print("Just to mention this Vehicle is an",self.tyres,"wheeler")


seat = Car('Leon', 21000, 100, 'White', 130)
seat.outPut()

hgv = Truck('bobs-hgv',45000,200,'Red',70,18)
hgv.outPut()
hgv.beep()