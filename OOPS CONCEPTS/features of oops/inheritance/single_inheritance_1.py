class parent():
    def m1():
        print("parent's functionality")
        return
class Child(parent):
    def m2():
        print("child's functionality")
        return
Child.m1()
Child.m2()
