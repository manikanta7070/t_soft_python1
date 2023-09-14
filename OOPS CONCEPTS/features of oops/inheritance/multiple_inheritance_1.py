# Parent class 1
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

# Parent class 2
class Bird:
    def fly(self):
        pass

# Child class inheriting from both Animal and Bird
class Parrot(Animal, Bird):
    def speak(self):
        return f"{self.name} says 'Squawk!'"

# Child class inheriting from only Animal
class Dog(Animal):
    def speak(self):
        return f"{self.name} says 'Woof!'"

# Create instances of the Parrot and Dog classes
parrot = Parrot("Polly")
dog = Dog("Fido")

# Demonstrate multiple inheritance
print(parrot.speak())  # Output: "Polly says 'Squawk!'"
parrot.fly()  # Parrot can also fly because of Bird inheritance

print(dog.speak())  # Output: "Fido says 'Woof!'"
# dog.fly()  # This would raise an AttributeError since Dog doesn't inherit from Bird
