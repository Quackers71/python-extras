class Dog:
    dogs = []

    def __init__(self, name):
        self.name = name
        self.dogs.append(self)

    @classmethod
    def num_dogs(cls):
        return len(cls.dogs)

    @staticmethod
    def bark(n):
        """barks n times"""
        for _ in range(n):
            print("Bark!")


dex = Dog("Dexter")
pop = Dog("Poppy")
