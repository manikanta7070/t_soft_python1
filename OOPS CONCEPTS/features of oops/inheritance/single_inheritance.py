class Parent():
    def first(self):
        print("first function")
        return
class Child(Parent):
    def second(self):
        print("second function")
        return
ob = Child()
ob.first()
ob.second()
