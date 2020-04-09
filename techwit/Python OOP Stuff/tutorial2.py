
class Dog(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print("Hi, I am",self.name,'& I am',self.age,'years old.')

    def change_age(self, age):
        self.age = age

q = Dog('Rob', 49)
fred = Dog('Fred', 70)
fred.change_age(65)
q.speak()
fred.speak()