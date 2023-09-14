class Engine:
    def __init__(self):
        self.engine_type = "Internal Combustion Engine"

class ElectricMixin:
    def __init__(self):
        self.engine_type = "Electric Motor"

class Car(Engine):
    def __init__(self):
        super().__init__()

class ElectricCar(Engine, ElectricMixin):
    pass

regular_car = Car()
electric_car = ElectricCar()

print("Regular Car Engine Type:", regular_car.engine_type)
print("Electric Car Engine Type:", electric_car.engine_type)
