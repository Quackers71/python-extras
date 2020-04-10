# Inheritance & Overloading

class Dog(object): # The Parent Class - super()
    def __init__(self, name, age): # this is the constructor method - you need this when you first create your class
        self.name = name # 'self' is the instance and 'name' is the attribute / (parameter)
        self.age = age


    def speak(self): # a method
        print("Hi, I am",self.name,'& I\'m',self.age,'years old.')

    def talk(self):
        print('Bark!')


class Cat(Dog): # This inherits the Dog class - including methods and attributes - this is known as the child (or derived) class
    def __init__(self, name, age, colour):
        super().__init__(name, age) # This inherits the attributes from the Dog (Parent) class i.e. self.name
        self.colour = colour # setting this attribute as it doesn't belong to the Parent class

    def talk(self):
        print('Meow!') # This will overload (override) the talk() method from the Parent class


dexter = Dog('Dexter', 7)
dexter.speak()
dexter.talk()

fluffy = Cat('Fluffy', 5, 'blue') # 'fluffy' is the object of the Child - Cat class
fluffy.speak() # speak method inheritted from the Dog class
fluffy.talk() # this talk method in the Cat class, will override the talk method from the Dog class