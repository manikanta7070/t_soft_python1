class EngineMixin:
    def start_engine(self):
        print("Engine started")

class ElectricMixin:
    def charge_battery(self):
        print("Battery charging")

class Car(EngineMixin, ElectricMixin):
    def drive(self):
        print("Car is driving")

my_car = Car()
my_car.start_engine()
my_car.charge_battery()
my_car.drive()
