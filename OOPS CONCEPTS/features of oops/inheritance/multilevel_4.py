#Multilevel Inheritance with Access Modifiers
class Grandparent:
    def __init__(self):
        self.public_var = "Public Variable"
        self._protected_var = "Protected Variable"
        self.__private_var = "Private Variable"

class Parent(Grandparent):
    def display_variables(self):
        print("From Parent:")
        print(self.public_var)        # Accessible
        print(self._protected_var)    # Accessible
        # print(self.__private_var)  # Not accessible

class Child(Parent):
    def display_variables(self):
        print("From Child:")
        print(self.public_var)        # Accessible
        print(self._protected_var)    # Accessible
        # print(self.__private_var)  # Not accessible

child_instance = Child()
child_instance.display_variables()
