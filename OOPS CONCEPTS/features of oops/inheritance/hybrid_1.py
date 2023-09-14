 #Hybrid Inheritance with Multiple and Multilevel Inheritance
class Animal:
    def speak(self):
        pass

class Mammal(Animal):
    def feed_milk(self):
        print("Mammal feeds milk")

class Bird(Animal):
    def fly(self):
        print("Bird can fly")

class Bat(Mammal, Bird):
    def speak(self):
        print("Bat says 'Screech'")

bat_instance = Bat()
bat_instance.feed_milk()
bat_instance.fly()
bat_instance.speak()
