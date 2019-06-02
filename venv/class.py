class Person:
    def __init__(self, name, age, state):
        self.name = name
        self.age = age
        self.state = state


p1 = Person("Robiat", 18, "Lagos")


print(p1.name)
print(p1.age)
print(p1.state)


class Kitchen:

    def __init__(self, pots, plates):
        self.pots = pots
        self.plates = plates

    def my_stuff(self):
        print("I have " + str(self.pots) + " pots and " + str(self.plates) + " plates.")


k1 = Kitchen(5, 9)
k2 = Kitchen(8, 2)
k1.my_stuff()
k2.my_stuff()
