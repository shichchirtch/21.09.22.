class Protists: pass
class Plants(Protists): pass
class Animals(Protists): pass
class Mosses(Plants): pass
class Flowering(Plants): pass
class Worms(Animals): pass
class Mammals(Animals): pass
class Human(Mammals): pass
class Monkeys(Mammals): pass

class Monkey(Monkeys): # - наследуется от Monkeys и служит для описания обезьян;
    def __init__(self, name, weight, old):
        self.name, self.weight, self.old = name, weight, old
class Person(Human): # - наследуется от Human и служит для описания человека;
    def __init__(self, name, weight, old):
        self.name, self.weight, self.old = name, weight, old
class Flower(Flowering): # - наследуется от Flowering и служит для описания цветка;
    def __init__(self, name, weight, old):
        self.name, self.weight, self.old = name, weight, old
class Worm(Worms): # - наследуется от Worms и служит для описания червей.
    def __init__(self, name, weight, old):
        self.name, self.weight, self.old = name, weight, old

lst_objs = [Monkey("мартышка", 30.4, 7), Monkey("шимпанзе", 24.6, 8),
        Person("Балакирев", 88, 34), Person("Верховный жрец", 67.5, 45),
        Flower("Тюльпан", 0.2, 1), Flower("Роза", 0.1, 2),
        Worm("червь", 0.01, 1), Worm("червь 2", 0.02, 1)]

lst_animals =[animal for animal in lst_objs if isinstance(animal, Animals)]
lst_plants =[plant for plant in lst_objs if isinstance(plant, Plants)]
lst_mammals = [mam for mam in lst_objs if isinstance(mam, Mammals)]
print(lst_mammals)

