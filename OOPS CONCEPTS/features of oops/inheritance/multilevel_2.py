# Multilevel Inheritance with Methods
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        print("Dog barks")

class Labrador(Dog):
    def speak(self):
        print("Labrador barks")

labrador_instance = Labrador()
labrador_instance.speak()
