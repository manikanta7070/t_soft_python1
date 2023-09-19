#clear example
# Base class
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        pass

# Subclass 1
class Dog(Animal):
    def make_sound(self):
        return "Woof!"

# Subclass 2
class Cat(Animal):
    def make_sound(self):
        return "Meow!"

# Create instances of the subclasses
dog = Dog("Buddy", "Dog")
cat = Cat("Whiskers", "Cat")

# Access attributes and methods of the base and subclasses
print(f"{dog.name} is a {dog.species} and says {dog.make_sound()}")
print(f"{cat.name} is a {cat.species} and says {cat.make_sound()}")
