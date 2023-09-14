class Grandparent:
    def grandparent_method(self):
        print("Method from Grandparent")

class Parent(Grandparent):
    def parent_method(self):
        print("Method from Parent")

class Child(Parent):
    def child_method(self):
        print("Method from Child")

child_instance = Child()
child_instance.grandparent_method()
child_instance.parent_method()
child_instance.child_method()
