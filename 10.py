"""Q10.

d.kind=”white”
d.name=”john”
e.name=”jonny”

what will be output of

d.kind
e.kind
d.type
e.type"""


class Dog:
    kind = 'canine'

    def __init__(self,name):
        self.name = name


d = Dog
e = Dog

d.kind = "white"
d.name = "john"
e.name = "johnny"
print(e.kind)#white
print(d.kind)#white
print(d.name)#johnny
print(e.name)#johnny