"""
Q18
Create a class Building
Create Appartment, House  and Commercial Building class inheriting Building class."""


class Building():
    def __init__(self, stories, name):
        self.s = stories
        self.n = name


class Appartment(Building):
    def __init__(self, color, stories, name):
        super().__init__(stories, name)
        self.c = color

    def display(self):
        print("color:", self.c)
        print("name:", self.n)
        print("stories:", self.s)
        print("\n")


class House(Building):
    def __init__(self, room, stories, name):
        super().__init__(stories, name)
        self.r = room

    def display(self):
        print("Room:", self.r)
        print("Stories:", self.s)
        print("name:", self.n)
        print("\n")


class CommercialBuilding(Building):
    def __init__(self, amount, stories, name):
        super().__init__(stories, name)
        self.at = amount

    def display(self):
        print("Amount:", self.at)
        print("Stories:", self.s)
        print("name:", self.n)
        print("\n")


a = Appartment("dark blue", "5", "Asmin Apartment")
a.display()
b = House("3rd", "4", "Rai's")
b.display()
c = CommercialBuilding("7000", "5", "CommercialBuilding")
c.display()



