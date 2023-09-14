class Parent1:
    def method1(self):
        print("Method from Parent1")

class Parent2:
    def method2(self):
        print("Method from Parent2")

class Child(Parent1, Parent2):
    def child_method(self):
        self.method1()  # Calls method from Parent1
        self.method2()  # Calls method from Parent2

child_instance = Child()
child_instance.child_method()
