
class Person(object):
    def __init__(self, name, age): # this is the constructor method - you need this when you first create your class
        self.name = name # 'self' is the instance and name is the attribute / (parameter)
        self.age = age
        self.li = [1,3,4]

    def speak(self): # a method
        print("Hi, I am",self.name,'& I\'m',self.age,'years old.')

    def change_age(self, age): # a method
        self.age = age

    def person_weight(self, weight): # another method
        self.weight = weight


q = Person('Rob', 49) # q is an object or instance of the class Person
fred = Person('Fred', 70) # 'Fred',name & 70,age are parameters passed into the instance 'fred' of the class 'Person'
q.change_age(25)
q.person_weight(83)
q.speak()
fred.speak()

print(q.name,"is",q.age)
print(q.name,"weighs in at",q.weight,"kgs")
print("fred.li =",fred.li)

print("You won't be able to use fred.weight as you haven't yet called add_weight on the instance of 'fred'")