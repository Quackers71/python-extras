# Private and Public Classes

class _Private: # a private class is defined by a _ before the name in Python
    def __init__(self, name):
        self.name = name

    def _Display(self): # note capital 'D'
        print("A Super Private Hello!")


class NotPrivate:
    def __init__(self, name):
        self.name = name
        self.priv = _Private(name)
        
    def _display(self): # private method notated by the _
        print("Hello")

    def display(self):
        print("Hi")

    def _output(self):
        print("A Private Hello!")

'''
Taken from Google Search of: "private vs public java"
    public is a java keyword which declares a member's access as public.  Public
    members are visible to all other classes.  This means that any other class can
    access a public field or method.  Further, other classes can modify public 
    fields unless the field is declared as final.
'''