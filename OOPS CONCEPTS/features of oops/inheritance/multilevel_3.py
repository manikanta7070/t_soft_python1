#Multilevel Inheritance with Attributes
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

class Sedan(Car):
    def __init__(self, brand, model, year):
        super().__init__(brand, model)
        self.year = year

sedan_instance = Sedan("Toyota", "Camry", 2022)
print(f"Brand: {sedan_instance.brand}, Model: {sedan_instance.model}, Year: {sedan_instance.year}")
