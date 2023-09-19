# Base class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

# Subclass 1
class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

# Subclass 2
class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

# Subclass 3
class Cow(Animal):
    def speak(self):
        return f"{self.name} says Moo!"

# Create instances of the subclasses
dog = Dog("Buddy")
cat = Cat("Whiskers")
cow = Cow("Bessie")

# Make animals speak
print(dog.speak())
print(cat.speak())
print(cow.speak())
