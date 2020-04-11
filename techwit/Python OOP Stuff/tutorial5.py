#  Class Methods, Static Methods & Class Variables

class Dog:
    dogs = [] # a class variable
    xc = 5

    def __init__(self, name):
        self.name = name
        self.dogs.append(self)

    def __str__(self):
        return str(self.name)

    @classmethod # A Decorator to denote a special type of Method - which doesn't require 'self' or another attribute
    def num_dogs(cls):
        return len(cls.dogs)

    @staticmethod # Another Decorator of type staticmethod
    def bark(n):
        """barks n times"""
        for _ in range(n):
            print("Bark!")

# class Math:
#     @staticmethod
#     def add(x, x2)
#         return x + x2


dex = Dog("Dexter")
pop = Dog("Poppy")
print("Number of instances of Dog =",Dog.num_dogs())

print(dex, "&", pop,"\n")

Dog.bark(5)