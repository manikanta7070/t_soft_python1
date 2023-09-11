# Private Variables(__)

class Myclass:
    __x=10 #static private variable
    def __init__(self):
        print("I am in constructor")
    def display(self):
        print("X value is",Myclass.__x)  # Private attributes can be accessed with the functions of that class
        

obj=Myclass()
#print("X value ",obj.__x)  AttributeError
#print("X value ",Myclass.__x) AttributeError

obj.display()
