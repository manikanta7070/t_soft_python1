class Myclass:
    _x=10 #static protected variable
    def __init__(self):
        print("I am in constructor")
    def display(self):
        print("X value is",Myclass._x)

obj=Myclass()
print("X value ",obj._x)
print("X value ",Myclass._x)
