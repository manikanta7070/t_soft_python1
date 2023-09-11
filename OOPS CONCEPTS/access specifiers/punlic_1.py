# pulbic variable
class Myclass:
    x=10 #static public variable
    def __init__(self):
        print("I am in constructor")
    def display(self):
        print("X value is",Myclass.x)

obj=Myclass()
print("X value ",obj.x)
print("X value ",Myclass.x)
