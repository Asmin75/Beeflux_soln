"""
class Dog:

    kind = 'canine'

    def __init__(self, name):
        self.name = name    # instance variable unique to each instance

    # >>> d = Dog('Fido')
    # >>> e = Dog('Buddy')

What Is the output of
d.kind

d.name

e.kind
e.name"""


class Dog:
    kind = 'canine'

    def __init__(self,name):
        self.name = name


d = Dog('fido')
print(d.kind)#canine
print(d.name)#fido

e = Dog('Buddy')
print(e.kind)#canine
print(e.name)#Buddy
